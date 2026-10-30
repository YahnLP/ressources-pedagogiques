# 🧪 FICHE PROTOCOLE DE TESTS & RAPPORT DE DIAGNOSTIC — S17
## Document de référence technique — à compléter lors du TP

---

> **Nom de l'apprenant** : ___________________________
> **Binôme** : ___________________________
> **Date** : ___________________________
> **N° de projet** : _____
> **Version du sketch testé** : V _____

---

## 📋 Partie 1 — Informations sur le système testé

| Champ | Valeur |
|---|---|
| Nom du projet | |
| Fonctionnalité principale | |
| Nombre de DEL contrôlées | |
| Nom du module Bluetooth configuré | |
| PIN Bluetooth | |
| Baudrate de communication | |
| Broche RX (SoftwareSerial) | |
| Broche TX (SoftwareSerial) | |
| Broches DEL utilisées | Broche ___ (Rouge) / Broche ___ (Jaune) / Broche ___ (Verte) |

---

## 🧪 Partie 2 — Protocole de tests d'intégration

> **Instruction** : Pour chaque test, réalise l'action décrite, note le résultat obtenu et indique le statut.
> ✅ = Conforme | ❌ = Non-conforme | ⚠️ = Partiellement conforme

### 2.1 Tests de communication Bluetooth

| N° | Fonctionnalité testée | Précondition | Action à réaliser | Résultat attendu | Résultat obtenu | Statut |
|---|---|---|---|---|---|---|
| T-01 | Alimentation du HC-05 | Câblage complet | Brancher le câble USB | LED HC-05 clignote rapidement | | |
| T-02 | Appairage Bluetooth | T-01 OK | Connecter depuis *Serial BT Terminal* | LED HC-05 fixe (ou clignotement lent) | | |
| T-03 | Réception message smartphone | T-02 OK | Envoyer `TEST` depuis l'app | `TEST` apparaît dans le moniteur série PC | | |
| T-04 | Envoi message vers smartphone | T-02 OK | Taper dans le moniteur série PC | Texte reçu sur le smartphone | | |

### 2.2 Tests de contrôle des DEL

| N° | Fonctionnalité testée | Précondition | Action | Résultat attendu | Résultat obtenu | Statut |
|---|---|---|---|---|---|---|
| T-05 | Allumage DEL rouge | T-02 OK | Envoyer `R1` | DEL rouge allumée + `"DEL rouge allumee"` reçu | | |
| T-06 | Extinction DEL rouge | T-05 OK | Envoyer `R0` | DEL rouge éteinte + message reçu | | |
| T-07 | Allumage DEL jaune | T-02 OK | Envoyer `J1` | DEL jaune allumée + message reçu | | |
| T-08 | Extinction DEL jaune | T-07 OK | Envoyer `J0` | DEL jaune éteinte + message reçu | | |
| T-09 | Allumage DEL verte | T-02 OK | Envoyer `V1` | DEL verte allumée + message reçu | | |
| T-10 | Extinction DEL verte | T-09 OK | Envoyer `V0` | DEL verte éteinte + message reçu | | |

### 2.3 Tests des fonctions avancées

| N° | Fonctionnalité testée | Précondition | Action | Résultat attendu | Résultat obtenu | Statut |
|---|---|---|---|---|---|---|
| T-11 | Commande ETAT — une DEL allumée | T-05 OK (R1 envoyé) | Envoyer `ETAT` | 3 lignes d'état dont "Rouge: ALLUMEE" | | |
| T-12 | Commande ETAT — toutes éteintes | Toutes éteintes | Envoyer `ETAT` | 3 lignes "ETEINTE" | | |
| T-13 | Commande inconnue | T-02 OK | Envoyer `XYZ` | Message d'erreur retourné | | |
| T-14 | Contrôle simultané | T-02 OK | R1 puis J1 puis V1 en rapide | 3 DEL allumées sans interférence | | |

### 2.4 Tests de robustesse et portée

| N° | Fonctionnalité testée | Distance | Action | Résultat attendu | Résultat obtenu | Statut |
|---|---|---|---|---|---|---|
| T-15 | Portée 2 m | 2 m | Envoyer `R1` | Commande exécutée | | |
| T-16 | Portée 5 m | 5 m | Envoyer `R1` | Commande exécutée | | |
| T-17 | Portée max | Distance max | Reculer progressivement | Note la distance de rupture | Distance de rupture : ___ m | |

---

## 📊 Partie 3 — Bilan des tests

| Critère | Valeur |
|---|---|
| Nombre de tests réalisés | ___ / 17 |
| Nombre de tests **Conformes** (✅) | ___ |
| Nombre de tests **Non-conformes** (❌) | ___ |
| Nombre de tests **Partiels** (⚠️) | ___ |
| Taux de conformité | ___ % |

**Liste des tests non-conformes et actions correctives :**

| N° test | Description du problème | Action corrective réalisée | Résultat après correction |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

## 🐛 Partie 4 — Rapport de diagnostic (si panne rencontrée)

> À compléter pour chaque panne rencontrée sur le projet. Utiliser la méthode **SVARC**.

### Fiche de panne N°1

| Étape SVARC | Description |
|---|---|
| **S — Symptôme** | *Décris précisément ce qui ne fonctionne pas :* |
| | |
| **V — Vérification** | *Qu'as-tu mesuré ou observé pour confirmer ? (tension, câblage, moniteur série…)* |
| | |
| **A — Analyse** | *Quelle est la cause probable identifiée ? Pourquoi ?* |
| | |
| **R — Remède** | *Quelle correction as-tu apportée ?* |
| | |
| **C — Contrôle** | *Quel test as-tu refait pour confirmer la résolution ? Résultat ?* |
| | |
| **Durée de résolution** | ___ min |
| **Panne résolue ?** | ☐ Oui ☐ Non ☐ Partiellement |

---

### Fiche de panne N°2 *(si applicable)*

| Étape SVARC | Description |
|---|---|
| **S — Symptôme** | |
| **V — Vérification** | |
| **A — Analyse** | |
| **R — Remède** | |
| **C — Contrôle** | |
| **Durée de résolution** | ___ min |
| **Panne résolue ?** | ☐ Oui ☐ Non ☐ Partiellement |

---

## 📸 Partie 5 — Captures d'écran et preuves visuelles

> Colle ici tes captures d'écran annotées (application smartphone, moniteur série) ou joins-les en fichier séparé nommé : `S17_Captures_[TonNom].pdf`

| N° | Capture | Description |
|---|---|---|
| C-01 | *[Coller capture]* | Appairage Bluetooth réussi |
| C-02 | *[Coller capture]* | Test T-05 : DEL rouge allumée + message retour |
| C-03 | *[Coller capture]* | Commande ETAT avec résultat |
| C-04 | *[Coller capture]* | Moniteur série montrant la communication |

---

## ✅ Validation enseignant

| Critère évalué | Note /5 | Commentaire |
|---|---|---|
| Protocole complet (tous les tests renseignés) | | |
| Résultats cohérents et honnêtes | | |
| Pannes diagnostiquées avec méthode SVARC | | |
| Captures d'écran présentes et annotées | | |
| Rédaction claire et professionnelle | | |
| **TOTAL** | **/25** | |

**Signature enseignant** : ___________________________ **Date** : ___________

---

*Fiche Protocole de Tests & Rapport de Diagnostic — BAC PRO CIEL | Module E2 | S17*
*Document à conserver dans le Portfolio de l'apprenant (Épreuve E5) — Compétences C3.2 – C4.2*
