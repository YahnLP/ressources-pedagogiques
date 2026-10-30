# 🔬 ATELIER PRODUCTION — S18 ANNÉE 2 – E2
## Rédaction Complète du DAT de Votre Projet A2

---

## 🎯 OBJECTIFS DE L'ATELIER

Produire en 2h30 un **Dossier des Architectures Techniques** complet pour votre projet A2 (S16), qui sera :

- ✅ Réutilisé comme support pour la soutenance S19
- ✅ Versé dans le dossier de compétences E2
- ✅ Évalué sur la qualité documentaire (voir grille)

---

## ⏱️ SÉQUENÇAGE DES TÂCHES

| **Tâche** | **Temps** | **Livrable** |
|---|---|---|
| T1 — Structure du DAT + page de garde | 20 min | Fichier DAT créé, pages 1–2 |
| T2 — Architecture + description composants | 25 min | Diagramme bloc + tableau composants |
| T3 — Schéma de câblage (Draw.io ou KiCad) | 40 min | Schéma exporté en PDF/SVG |
| T4 — BOM complète | 20 min | Tableau Excel/LibreOffice |
| T5 — Section configuration | 15 min | Paramètres réseau, AWS, MQTT, seuils |
| T6 — Procédures (installation + maintenance) | 30 min | 2 procédures numérotées |
| T7 — Peer review | 10 min | Liste corrections formulées |
| T8 — Finalisation et export PDF | 10 min | Fichier DAT-final.pdf |

---

# TÂCHE T1 — PAGE DE GARDE ET STRUCTURE (20 min)

## Créer votre fichier DAT

> Ouvrir LibreOffice Writer (ou Word). Créer le fichier `DAT-[VotreNom]-[Sujet]-v1.0.odt`

### À remplir :

```
DOSSIER DES ARCHITECTURES TECHNIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Projet   : _______________________________
Client   : INDUSTECH SAS
Référence: DAT-ESP32-[VOTRE_SUJET]-001
Version  : 1.0
Date     : 2026-___-___
Statut   : ☐ Brouillon  ☑ Pour Validation
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Auteur(s): _______________________________
```

### Tableau de révisions (à compléter maintenant)

| **Version** | **Date** | **Auteur** | **Description** |
|---|---|---|---|
| 0.1 | 2026-\_\_\_-\_\_\_ | | Création initiale |

### Créer le sommaire avec les 13 sections

> Insérer les titres de section (Titre 1) dans le document. LibreOffice génère le sommaire automatiquement.

**Q1.** Combien de pages minimum votre DAT devrait-il faire pour être complet ?

\_\_\_\_\_\_\_\_\_

??? success "Éléments de réponse"
    **Q1** — Un DAT complet à 13 sections fait en général **15 à 25 pages** (une à deux pages par section, plus le schéma et la BOM) ; l'important est que **chaque section soit présente et renseignée**.

---

# TÂCHE T2 — ARCHITECTURE ET COMPOSANTS (25 min)

## Section 4 — Architecture Générale

### Diagramme bloc à produire dans Draw.io

> Ouvrir draw.io (app.diagrams.net). Créer un diagramme bloc avec :

```
Éléments à représenter :
  ☐ Capteur 1 (nom + interface : I2C / ADC / GPIO)
  ☐ Capteur 2 si présent
  ☐ ESP32 (microcontrôleur central)
  ☐ Wi-Fi (lien de communication)
  ☐ AWS IoT Core (broker MQTT TLS)
  ☐ IoT Rule SQL (filtre + enrichissement)
  ☐ CloudWatch (métriques + dashboard)
  ☐ Alarme SNS (optionnel)
  ☐ Batterie / alimentation

Annotations obligatoires sur les flèches :
  ☐ Protocole (I2C, SPI, ADC, MQTT TLS...)
  ☐ Port ou fréquence si pertinent (port 8883, 400kHz...)
```

> Exporter en PDF et insérer dans la section 4 du DAT.

## Section 5 — Description des Composants

**Remplir le tableau :**

| **Réf. schéma** | **Désignation** | **Modèle exact** | **Version FW/HW** | **Rôle dans le système** |
|---|---|---|---|---|
| U1 | Microcontrôleur | ESP32 DevKit v1 | Arduino SDK 2.x | Acquisition, traitement, communication |
| U2 | | | | |
| U3 | | | | |
| REG1 | | | | |
| BAT1 | | | | |

---

# TÂCHE T3 — SCHÉMA DE CÂBLAGE (40 min)

## Section 6 — Schémas de Câblage

### Créer le schéma dans KiCad Eeschema ou Draw.io

**Éléments obligatoires à inclure :**

```
☐ Tous les composants avec leur référence (U1, U2, REG1...)
☐ Toutes les connexions (fils) avec repérages aux deux extrémités
☐ Codes couleurs IEC 60446 appliqués
☐ Broches nommées (GPIO21/SDA, GPIO22/SCL, GPIO4/DATA...)
☐ Valeurs des composants passifs (R=4,7kΩ, C=100nF)
☐ Symboles d'alimentation (VCC 3.3V, VCC 5V, GND)
☐ Cartouche (titre, version, date, auteur)
☐ Légende des couleurs et symboles
```

### Tableau de repérage des fils (à compléter)

| **Repère fil** | **De** | **Vers** | **Couleur** | **Section** | **Remarque** |
|---|---|---|---|---|---|
| ESP32-DHT22-VCC | ESP32 pin 3V3 | DHT22 pin VCC | Rouge | 0,2mm² | |
| ESP32-DHT22-GND | ESP32 GND | DHT22 GND | Noir | 0,2mm² | |
| ESP32-DHT22-DATA | ESP32 GPIO4 | DHT22 DATA | Jaune | 0,2mm² | |
| ESP32-ADXL-SDA | ESP32 GPIO21 | ADXL345 SDA | Violet | 0,2mm² | Pull-up 4,7kΩ |
| ESP32-ADXL-SCL | ESP32 GPIO22 | ADXL345 SCL | Blanc | 0,2mm² | Pull-up 4,7kΩ |
| BATT-REG-+ | Batterie + | REG1 Vin | Rouge | 0,5mm² | |
| | | | | | |
| | | | | | |

**Q2.** Votre schéma de câblage comporte-t-il des fils croisés ? Si oui, comment les distingue-t-on d'un point de jonction ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Éléments de réponse"
    **Q2** — Deux fils qui se croisent **sans point plein** ne sont **pas reliés** (simple croisement). Une **jonction** se reconnaît au **point plein** à l'intersection. Il vaut mieux éviter les croisements en utilisant des étiquettes de net.

---

# TÂCHE T4 — BOM (20 min)

## Section 7 — Bill Of Materials

> Créer un onglet "BOM" dans un tableau LibreOffice Calc ou dans le DAT.

### À remplir (ajouter toutes les lignes nécessaires)

| **Réf.** | **Désignation** | **Modèle** | **Qté** | **Fournisseur** | **Réf. Fournisseur** | **PU HT (€)** | **Total** |
|---|---|---|---|---|---|---|---|
| U1 | Microcontrôleur Wi-Fi | ESP32 DevKit v1 | 1 | AZ-Delivery | B08BTXCZC1 | 7,99 | 7,99 |
| | | | | | | | |
| | | | | | | | |
| | | | | | | **TOTAL** | |

**Q3.** Comment trouvez-vous la référence fournisseur d'un composant que vous ne connaissez pas ? Citez 2 sites de recherche :

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Q4.** Si un composant de la BOM n'est plus disponible (rupture de stock), quel champ de la BOM vous permet de trouver rapidement un substitut ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Éléments de réponse"
    **Q3** — Sites de recherche : **Mouser**, **Farnell**, **RS Components**, **Digi-Key**, **LCSC** (recherche par référence fabricant ou par désignation).  
    **Q4** — La **référence fabricant (le modèle exact)** : elle permet de chercher un composant équivalent chez un autre fournisseur.

---

# TÂCHE T5 — SECTION CONFIGURATION (15 min)

## Section 8 — Configuration du Système

> Remplir les paramètres réels de votre projet :

```
8.1 RÉSEAU
  SSID Wi-Fi       : _______ (ne pas mettre le mot de passe en clair)
  Adresse IP ESP32 : DHCP
  Hostname         : _______

8.2 AWS IOT CORE
  Endpoint         : _______-ats.iot.eu-west-1.amazonaws.com
  Port MQTT        : 8883 (TLS)
  Client ID        : _______
  
8.3 TOPICS MQTT
  Publication data : _______
  Publication status: _______
  Subscribe commande: _______
  LWT              : topic _______ → message "_______"
  QoS              : ___

8.4 SEUILS MAINTENANCE PRÉDICTIVE
  Seuil alerte     : _______ > _______ [unité]
  Seuil critique   : _______ > _______ [unité]
  MTBF cible       : _______ min
  
8.5 CLOUDWATCH
  Espace de noms   : _______
  Métriques        : _______, _______
  Seuil alarme     : _______
```

---

# TÂCHE T6 — PROCÉDURES (30 min)

## Section 9 — Procédure d'Installation

> Rédiger la procédure complète d'installation de votre système. Chaque étape doit être :
> - Numérotée
> - Précise (pas "brancher les composants" mais "connecter SDA → GPIO21")
> - Accompagnée d'une vérification

```
PROCÉDURE D'INSTALLATION — REF: PROC-INSTALL-001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRÉREQUIS :
  ☐ ___________________________________________
  ☐ ___________________________________________
  ☐ ___________________________________________

1. CÂBLAGE MATÉRIEL
  ☐ 1.1 _______________________________________
  ☐ 1.2 _______________________________________
  ☐ 1.3 _______________________________________
  Validation : _________________________________

2. CONFIGURATION AWS IOT CORE
  ☐ 2.1 _______________________________________
  ☐ 2.2 _______________________________________
  Validation : _________________________________

3. CHARGEMENT DU FIRMWARE
  ☐ 3.1 _______________________________________
  ☐ 3.2 _______________________________________
  Validation : _________________________________

4. VÉRIFICATION OPÉRATIONNELLE
  ☐ 4.1 _______________________________________
  Validation : _________________________________

RÉSULTAT ATTENDU : ____________________________
```

## Section 10 — Procédure de Maintenance Corrective

> Rédiger la procédure pour le problème le plus courant de votre système.
> Symptôme couvert : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

```
PROCÉDURE MAINTENANCE — REF: PROC-MAINT-001
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Première vérification : ______________________
   Action   : _______________________________
   Si OK    : Passer à l'étape 2
   Si FAIL  : _______________________________

2. Deuxième vérification : ______________________
   Action   : _______________________________
   Si OK    : Passer à l'étape 3
   Si FAIL  : _______________________________

3. Correction et validation :
   Action   : _______________________________
   Validation : Confirmer que ________________
```

---

# TÂCHE T7 — PEER REVIEW (10 min)

## Échange de DAT entre binômes

> Donner votre DAT (version draft) à un binôme. Utiliser la grille ci-dessous.

### Grille de peer review

| **Critère** | **Présent ?** | **Commentaire correctif** |
|---|---|---|
| Page de garde avec version et date | ☐ Oui ☐ Non | |
| Tableau de révisions | ☐ Oui ☐ Non | |
| Diagramme bloc (architecture) | ☐ Oui ☐ Non | |
| Schéma câblage avec légende | ☐ Oui ☐ Non | |
| Repères de fils | ☐ Oui ☐ Non | |
| BOM avec références fournisseurs | ☐ Oui ☐ Non | |
| Section configuration complète | ☐ Oui ☐ Non | |
| Procédure installation avec tests | ☐ Oui ☐ Non | |
| Procédure maintenance | ☐ Oui ☐ Non | |
| **Commentaire global** | | |

**Q5.** Après la peer review, listez les 3 améliorations prioritaires à apporter à votre DAT :

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Éléments de réponse"
    **Q5** — Exemples d'améliorations prioritaires : schéma plus lisible (légende, repères), BOM complète (références fournisseur, quantités), section configuration sans mot de passe en clair, procédures numérotées et testables.

---

## 📊 GRILLE D'ÉVALUATION DE L'ATELIER

| **Section** | **Points** | **Critères** |
|---|---|---|
| T1 — Page de garde + structure | /3 | Version, date, tableau révisions, 13 sections présentes |
| T2 — Architecture + composants | /5 | Diagramme bloc complet, tableau composants avec FW |
| T3 — Schéma câblage | /7 | Légende, repères fils, couleurs IEC, cartouche |
| T4 — BOM | /5 | Toutes lignes, références fournisseurs, prix total |
| T5 — Configuration | /4 | Tous paramètres renseignés avec valeurs réelles |
| T6 — Procédures | /6 | Numérotées, cases à cocher, tests de validation |
| T7 — Peer review | /2 | Grille remplie + 3 améliorations identifiées |
| Qualité générale (orthographe, mise en forme) | /3 |  |
| **TOTAL** | **/35** |  |

> *Ramené à /20 : score × 0,57*

---

**Document – BAC PRO CIEL – A2 – E2/U21 – Version 1.0 – 2026**
