## 📚 FICHE DE COURS ÉLÈVE
### "Architecture Serveur, Connectique & BIOS/UEFI"

*Version 1.0 - BTS SIO SISR - Semestre 1 - Semaine 2*

---

### 🎯 Compétences Travaillées

| **Code** | **Compétence** |
|----------|----------------|
| **B1.1** | Recenser et identifier les ressources numériques |
| **B2.2** | Installer et configurer des éléments d'infrastructure |
| **B2.3** | Exploiter, dépanner et superviser une solution d'infrastructure réseau |

---

### I. PC vs Serveur : Deux Mondes, Deux Philosophies

#### A. Rappel : Le PC de Bureau (Desktop Computer)

**Définition :** Ordinateur personnel conçu pour un **usage individuel**, généralement utilisé 8 heures par jour en moyenne.

**Caractéristiques principales :**
- **Format** : Tour (ATX, Micro-ATX) ou All-in-One
- **Utilisateur** : 1 personne
- **Durée de vie** : 3-5 ans
- **Priorités** : Coût, polyvalence, confort utilisateur (silence, esthétique)

---

#### B. Le Serveur : Définition et Rôle

**Définition :** Machine informatique **dédiée** à fournir des **services** à d'autres ordinateurs (clients) via un réseau, fonctionnant **en continu** (24h/24, 7j/7).

**Analogie :** Un serveur est comme un **restaurant** : il reste ouvert toute la journée pour servir de nombreux clients, alors qu'un PC est comme une **cuisine personnelle** utilisée quelques heures par jour.

💡 **Lien avec ITIL :** Le serveur est un **actif de configuration (CI)** critique dans la CMDB. Sa disponibilité conditionne la **continuité de service** de toute l'organisation !

---

#### C. Tableau Comparatif Détaillé

| **Critère** | **PC de Bureau** | **Serveur Professionnel** |
|-------------|------------------|---------------------------|
| **Usage principal** | Bureautique, jeux, création | Hébergement de services (web, fichiers, bases de données, mails...) |
| **Nombre d'utilisateurs** | 1 | De 10 à plusieurs milliers simultanément |
| **Temps de fonctionnement** | 8h/jour en moyenne | **24h/24, 7j/7, 365j/an** |
| **Format** | Tour (verticale), All-in-One | **Rack** (horizontal 1U/2U/4U) ou Tour |
| **Emplacement** | Bureau, domicile | **Datacenter**, salle serveur climatisée |
| **Processeur** | Intel Core i3/i5/i7, AMD Ryzen | Intel Xeon, AMD EPYC (multi-socket possibles) |
| **RAM** | 8-32 Go | 32 Go à plusieurs **To** (ECC pour fiabilité) |
| **Stockage** | 500 Go - 2 To | Plusieurs To à plusieurs dizaines de To (RAID) |
| **Alimentation** | 1 bloc (450-750W) | **2 blocs redondants** (hot-swap) |
| **Refroidissement** | 2-3 ventilateurs | **Ventilateurs redondants** + climatisation dédiée |
| **Cartes réseau** | 1 port Gigabit | **2-4 ports Gigabit ou 10 Gbps** (redondance) |
| **Administration** | Locale (écran+clavier branchés) | **À distance** (SSH, RDP, iLO, iDRAC) |
| **Système d'exploitation** | Windows 10/11, Linux Desktop | Windows Server, Linux Server (CentOS, Ubuntu Server, Debian...) |
| **Disponibilité attendue** | 95% (acceptable s'il plante) | **99.9% à 99.999%** (= 8h à 5 min d'indispo par an) |
| **Garantie** | 1-3 ans | 3-5 ans (support 24/7 possible) |
| **Prix** | 400 - 2 000 € | 2 000 - 50 000 €+ |

---

#### D. Technologies Spécifiques aux Serveurs

##### 🔹 **Redondance des Composants**

**Définition :** Duplication des composants critiques pour qu'en cas de panne de l'un, l'autre prenne automatiquement le relais **sans interruption de service**.

**Composants redondés :**

| Composant | Risque si panne | Solution serveur |
|-----------|----------------|------------------|
| **Alimentation** | Arrêt complet du serveur | **2 blocs d'alimentation** (dual PSU) |
| **Disques durs** | Perte de données | **RAID** (plusieurs disques avec redondance) |
| **Cartes réseau** | Perte de connexion | **2 cartes réseau** (bonding/teaming) |
| **Ventilateurs** | Surchauffe → arrêt | **Ventilateurs multiples** + alerte |

![Alimentation Redondante](serveur_dual_psu.png)
*Légende : Serveur Dell PowerEdge avec deux blocs d'alimentation hot-swap. Si l'un tombe en panne, le second continue seul à alimenter le serveur sans coupure.*

---

##### 🔹 **Hot-Swap (Échange à Chaud)**

**Définition :** Capacité à **remplacer un composant défectueux sans éteindre le serveur**.

**Composants hot-swap courants :**
- Disques durs (baies hot-swap)
- Alimentations
- Ventilateurs
- Cartes réseau (sur certains modèles haut de gamme)

**Avantage :** Maintenance **sans interruption de service** → continuité d'activité préservée.

![Baie Hot-Swap](serveur_baie_hotswap.png)
*Légende : Baie de disques durs hot-swap sur serveur HP ProLiant. Chaque disque se retire par simple pression sur le loquet, sans vis, serveur allumé.*

---

##### 🔹 **Format Rack**

**Définition :** Format standardisé permettant de monter les serveurs dans une **armoire (baie) de 19 pouces**.

**Unité de mesure :** Le **"U"** (Rack Unit)
- 1U = 1.75 pouce = **44.45 mm de hauteur**
- Les armoires font généralement **42U** de haut (environ 2 mètres)

**Formats courants :**
- **1U** : Serveur très plat, haute densité (ex: serveur web, firewall)
- **2U** : Format standard (bon compromis densité/performance)
- **4U** : Serveur puissant avec beaucoup de disques

![Rack Serveur](rack_42u_schema.png)
*Légende : Armoire rack 42U pouvant accueillir jusqu'à 42 serveurs 1U, ou 21 serveurs 2U, etc. Les serveurs se fixent sur des rails coulissants pour faciliter la maintenance.*

**Avantages du format rack :**
- ✅ **Gain de place** : densité maximale
- ✅ **Gestion des câbles** optimisée
- ✅ **Climatisation centralisée** de l'armoire
- ✅ **Sécurité physique** (armoire verrouillable)

---

##### 🔹 **Administration à Distance**

**Pourquoi ?** Un datacenter peut contenir des **centaines de serveurs**. Impossible d'avoir un écran/clavier branché sur chacun !

**Technologies d'administration à distance :**

| **Technologie** | **Type** | **Description** |
|-----------------|----------|-----------------|
| **SSH** (Secure Shell) | Logiciel | Accès en ligne de commande sécurisé (Linux/Unix) |
| **RDP** (Remote Desktop Protocol) | Logiciel | Bureau à distance (Windows Server) |
| **iLO** (HP) / **iDRAC** (Dell) / **IPMI** | Matériel | Carte d'administration intégrée au serveur, accessible même serveur éteint |

**Carte d'administration (iLO/iDRAC) :**
- Petit ordinateur **indépendant** intégré au serveur
- Possède sa **propre carte réseau** et son **IP dédiée**
- Permet de :
  - ✅ Allumer/éteindre le serveur à distance
  - ✅ Accéder au BIOS à distance
  - ✅ Voir l'écran de démarrage (KVM over IP)
  - ✅ Monter une ISO virtuelle pour installer un OS
  - ✅ Surveiller la santé du serveur (températures, pannes disques...)

![iLO Interface](ilo_interface.png)
*Légende : Interface web HP iLO permettant d'administrer complètement un serveur à distance via un navigateur, même serveur éteint.*

---

#### E. Cas d'Usage : Quand Utiliser un Serveur ?

**On utilise un serveur quand :**

1. ✅ **Plusieurs utilisateurs** doivent accéder aux **mêmes données** (ex: serveur de fichiers)
2. ✅ Un **service doit être disponible 24/7** (ex: site web, serveur mail)
3. ✅ On a besoin de **centraliser la gestion** (ex: Active Directory pour gérer les comptes utilisateurs)
4. ✅ La **sécurité des données** est critique (sauvegardes, RAID, accès contrôlés)
5. ✅ La **puissance de calcul** nécessaire dépasse un PC standard (ex: serveur de bases de données, serveur de rendu 3D)

**On peut utiliser un PC (ou mini-PC) quand :**

1. ✅ Usage très limité (1-5 utilisateurs occasionnels)
2. ✅ Budget serré (TPE, association, particulier)
3. ✅ Service non critique (tolérance à l'indisponibilité)
4. ✅ Apprentissage / maquettage (comme en BTS SIO !)

💡 **Note :** Dans un contexte professionnel d'entreprise, on privilégie **toujours un serveur** pour les services critiques.

---

### II. Périphériques et Connectique : Le Grand Tour

#### A. Pourquoi Connaître les Connectiques ?

En tant que **technicien systèmes et réseaux**, vous serez amené à :

- ✅ **Brancher** des équipements (serveurs, switchs, écrans, périphériques...)
- ✅ **Diagnostiquer** des problèmes de connexion (mauvais câble, port défectueux...)
- ✅ **Conseiller** les utilisateurs sur le bon câble à utiliser
- ✅ **Auditer** l'infrastructure existante (inventaire des câblages)

💡 **Anecdote pro :** 30% des pannes en helpdesk sont des problèmes de **câbles** (mal branché, défectueux, mauvais type) !

---

#### B. Les Connectiques USB : L'Universel

**USB = Universal Serial Bus** (Bus série universel)

##### 🔸 Les Différents Formats (Types de Connecteurs)

| **Type** | **Forme** | **Usage Principal** | **Image** |
|----------|-----------|---------------------|-----------|
| **USB Type-A** | Rectangle plat | Côté ordinateur (hôte) | Standard depuis 1996 |
| **USB Type-B** | Carré/trapèze | Côté périphérique (imprimante, scanner) | Moins courant aujourd'hui |
| **USB Type-C** | Ovale symétrique | **Standard moderne** (réversible) | Remplace progressivement A et B |
| **Micro-USB** | Petit trapèze | Anciens smartphones, petits appareils | En voie de disparition |
| **Mini-USB** | Plus gros que micro | Vieux appareils photo, GPS | Obsolète |

![USB Types](usb_types_comparaison.png)
*Légende : Comparaison des différents types de connecteurs USB. De gauche à droite : Type-A, Type-B, Type-C, Micro-USB, Mini-USB.*

---

##### 🔸 Les Versions USB (Vitesses)

| **Version** | **Débit Max** | **Année** | **Reconnaissable à** |
|-------------|---------------|-----------|----------------------|
| **USB 1.0/1.1** | 12 Mb/s | 1996 | Port **blanc** ou sans couleur |
| **USB 2.0** | 480 Mb/s (60 Mo/s) | 2000 | Port **noir** |
| **USB 3.0 / 3.1 Gen 1** | 5 Gb/s (625 Mo/s) | 2008 | Port **bleu** |
| **USB 3.1 Gen 2** | 10 Gb/s (1.25 Go/s) | 2013 | Port bleu ou **bleu-vert** |
| **USB 3.2** | 20 Gb/s | 2017 | Port USB-C (parfois marqué SS20) |
| **USB4** | 40 Gb/s | 2019 | Port USB-C (compatible Thunderbolt 3) |

⚠️ **Rétrocompatibilité :** Un périphérique USB 2.0 fonctionne sur un port USB 3.0 (mais à vitesse USB 2.0). Un câble USB 3.0 est **nécessaire** pour atteindre les vitesses USB 3.0+.

![USB Port Colors](usb_port_colors.png)
*Légende : Ports USB reconnaissables à leur couleur. Noir = USB 2.0, Bleu = USB 3.0, Rouge = USB haute puissance (chargement rapide).*

---

##### 🔸 USB Type-C : La Révolution

**Avantages :**
- ✅ **Réversible** : se branche dans les 2 sens (enfin !)
- ✅ **Universel** : même connecteur pour smartphones, PC, tablettes, écrans...
- ✅ **Multifonction** : données + vidéo + alimentation (jusqu'à 100W)
- ✅ **Rapide** : jusqu'à 40 Gb/s (USB4)

**Attention piège :** Tous les câbles USB-C ne se valent pas !
- Certains sont **charge uniquement** (pas de données)
- Certains sont USB 2.0 (lents) même s'ils ont un connecteur Type-C
- Il faut vérifier les **spécifications** du câble !

---

#### C. Les Connectiques Vidéo : VGA, HDMI, DisplayPort

##### 🔸 Tableau Comparatif

| **Connecteur** | **Type** | **Résolution Max** | **Audio** | **État** |
|----------------|----------|-------------------|-----------|----------|
| **VGA** | Analogique | 1920×1200 | ❌ Non | ⚠️ Obsolète |
| **DVI** | Numérique | 2560×1600 | ❌ Non | ⚠️ En voie de disparition |
| **HDMI** | Numérique | 8K à 60 Hz (v2.1) | ✅ Oui | ✅ Standard TV/multimédia |
| **DisplayPort** | Numérique | 8K à 60 Hz (v1.4) | ✅ Oui | ✅ Standard PC/professionnel |
| **USB-C (alt mode)** | Numérique | 8K à 60 Hz | ✅ Oui | ✅ Futur standard |

![Video Connectors](connecteurs_video.png)
*Légende : De gauche à droite : VGA (15 broches, bleu, analogique), DVI (blanc, numérique), HDMI (noir, multimédia), DisplayPort (vert/noir, professionnel).*

---

##### 🔸 **VGA (Video Graphics Array)** - Obsolète

**Reconnaissable à :** Connecteur **trapézoïdal bleu à 15 broches**

**Caractéristiques :**
- Technologie **analogique** (années 1980)
- Signal dégradé sur longues distances (>5m)
- Qualité d'image inférieure au numérique

**Usage actuel :** Encore présent sur vieux projecteurs ou écrans, mais **à éviter**.

---

##### 🔸 **HDMI (High-Definition Multimedia Interface)**

**Reconnaissable à :** Connecteur **rectangulaire noir/doré plat**

**Caractéristiques :**
- Transporte **vidéo + audio** sur un seul câble
- Standard sur les **TV, consoles de jeu, lecteurs Blu-ray**
- Plusieurs versions (1.4, 2.0, 2.1) avec résolutions/fréquences croissantes
- Longueur maximale : **10-15 m** (au-delà, signal dégradé ou nécessité d'amplificateur)

**Versions courantes :**
- **HDMI 1.4** : Full HD 1080p à 60 Hz
- **HDMI 2.0** : 4K à 60 Hz
- **HDMI 2.1** : 8K à 60 Hz, 4K à 120 Hz (gaming)

---

##### 🔸 **DisplayPort**

**Reconnaissable à :** Connecteur **rectangulaire noir avec un coin coupé**

**Caractéristiques :**
- Concurrent de HDMI, privilégié dans le **monde professionnel**
- Supporte le **Multi-Stream Transport (MST)** : plusieurs écrans sur un seul câble (daisy-chaining)
- Débits supérieurs à HDMI à version équivalente
- Pas de royalties (HDMI est soumis à licence)

**Avantage pro :** Idéal pour setups multi-écrans (trading, design, développement)

---

#### D. Les Connectiques Réseau : RJ45 et Fibre Optique

##### 🔸 **RJ45 (Ethernet sur Câble Cuivre)**

**Reconnaissable à :** Connecteur **transparent/translucide avec 8 contacts dorés**

**Caractéristiques :**
- Standard pour les **réseaux locaux (LAN)**
- Câble appelé **paire torsadée** (Twisted Pair)
- Plusieurs catégories selon la vitesse supportée

| **Catégorie** | **Débit Max** | **Distance Max** | **Usage** |
|---------------|---------------|------------------|-----------|
| **Cat 5** | 100 Mb/s | 100 m | ⚠️ Obsolète |
| **Cat 5e** | 1 Gb/s | 100 m | Standard actuel maisons/bureaux |
| **Cat 6** | 10 Gb/s (55 m) | 100 m (1 Gb/s) | Recommandé pour nouvelles installations |
| **Cat 6a** | 10 Gb/s | 100 m | Datacenters |
| **Cat 7 / Cat 8** | 40 Gb/s | 30 m | Très haut débit (rare) |

![RJ45 Cable](cable_rj45_interieur.png)
*Légende : Câble RJ45 coupé montrant les 8 fils torsadés par paires. Les couleurs suivent un standard précis (T568A ou T568B) pour garantir la compatibilité.*

**Types de câbles RJ45 :**
- **Câble droit** (Straight-through) : PC ↔ Switch, Switch ↔ Routeur
- **Câble croisé** (Crossover) : PC ↔ PC direct (obsolète grâce à l'Auto-MDIX)

⚠️ **Limitation :** Distance maximale de **100 mètres**. Au-delà, il faut un équipement intermédiaire (switch) ou passer à la fibre.

---

##### 🔸 **Fibre Optique**

**Principe :** Transmission de données par **lumière** dans un câble en verre ou plastique.

**Avantages par rapport au cuivre (RJ45) :**
- ✅ **Débits très élevés** : 10 Gb/s, 40 Gb/s, 100 Gb/s, voire plus
- ✅ **Distances énormes** : jusqu'à **plusieurs kilomètres** sans perte de signal
- ✅ **Immunité aux interférences électromagnétiques** (EMI)
- ✅ **Légèreté et finesse** du câble
- ✅ **Sécurité** : impossible d'écouter la ligne par induction électromagnétique

**Inconvénients :**
- ❌ Plus **coûteuse** que le cuivre
- ❌ Nécessite des équipements spécialisés (switches fibre, transceivers)
- ❌ Plus **fragile** (ne pas plier à moins de 3 cm de rayon)

---

**Types de Fibre Optique :**

| **Type** | **Cœur** | **Distance** | **Usage** | **Connecteurs Courants** |
|----------|----------|--------------|-----------|--------------------------|
| **Multimode (MMF)** | 50 ou 62.5 µm | 300 m - 2 km | LAN (campus, datacenters) | LC, SC, ST |
| **Monomode (SMF)** | 9 µm | 10 - 100 km | WAN (liaisons longue distance) | LC, SC |

![Fiber Connectors](connecteurs_fibre.png)
*Légende : Connecteurs fibre optique courants. De gauche à droite : LC (petit, moderne), SC (push-pull, carré), ST (baïonnette, ancien).*

**Code couleur des câbles fibre :**
- **Jaune** : Monomode (SMF)
- **Orange / Aqua** : Multimode (MMF)

💡 **À retenir :** 
- **Cuivre (RJ45)** : bon marché, 1 Gb/s, max 100m → LANs bureaux
- **Fibre Optique** : cher, très haut débit, longues distances → Datacenters, liaisons inter-sites

---

### III. Le BIOS/UEFI : Le Gardien du Démarrage

#### A. Qu'est-ce que le BIOS/UEFI ?

##### 🔸 **BIOS (Basic Input/Output System)**

**Définition :** Programme **firmware** (logiciel intégré au matériel) stocké dans une **puce mémoire flash** sur la carte mère, s'exécutant **avant le système d'exploitation**.

**Analogie :** Le BIOS est le **gardien de nuit** de l'immeuble (PC). Avant que l'immeuble ouvre officiellement (démarrage de Windows), le gardien vérifie que tout fonctionne (électricité, portes, alarmes...).

**Rôle principal :**
1. **POST (Power-On Self Test)** : Test automatique de tous les composants au démarrage
2. **Initialisation du matériel** : Configuration des composants (CPU, RAM, disques...)
3. **Lancement du système d'exploitation** : Chargement du bootloader (programme de démarrage de l'OS)

---

##### 🔸 **UEFI (Unified Extensible Firmware Interface)**

**Définition :** Successeur moderne du BIOS, développé par Intel dans les années 2000.

**Différences BIOS vs UEFI :**

| **Critère** | **BIOS (Legacy)** | **UEFI** |
|-------------|-------------------|----------|
| **Année** | 1975-2000 | 2005-Aujourd'hui |
| **Interface** | Texte uniquement, navigation clavier | **Graphique**, souris supportée |
| **Taille disque max** | 2.2 To (MBR) | >2 To (GPT) |
| **Sécurité** | Faible (pas de vérification) | **Secure Boot** (protection contre rootkits) |
| **Vitesse de démarrage** | Lente | **Rapide** |
| **Support 32/64 bits** | 16 bits | 32 et 64 bits |
| **Réseau** | Non | Oui (PXE boot amélioré) |

![BIOS vs UEFI Interface](bios_vs_uefi_interface.png)
*Légende : À gauche, interface BIOS classique en mode texte bleu/gris. À droite, interface UEFI moderne graphique avec icônes et support de la souris.*

💡 **À retenir :** Tous les PC récents (depuis ~2012) utilisent **UEFI**, mais beaucoup conservent un **mode Legacy** (compatibilité BIOS) pour installer de vieux OS.

---

#### B. Accéder au BIOS/UEFI

##### 🔸 Touches d'Accès selon les Constructeurs

| **Constructeur** | **Touche(s)** | **Alternative** |
|------------------|---------------|-----------------|
| **Dell** | F2 | DEL |
| **HP** | F10 | ESC, puis F10 |
| **Lenovo** | F2 ou F1 | Bouton "Novo" (petits PC portables) |
| **Asus** | DEL | F2 |
| **Acer** | F2 | DEL |
| **MSI** | DEL | F2 |
| **Gigabyte** | DEL | F2 |
| **Autres** | ESC, F12 (menu de boot) | Consulter manuel |

⚠️ **Astuce :** **Marteler la touche dès l'allumage** du PC (ne pas attendre le logo Windows) !

---

##### 🔸 Méthode Alternative (Windows 10/11)

**Si le PC démarre trop vite pour intercepter la touche :**

1. Windows → **Paramètres** (⚙️)
2. **Mise à jour et sécurité** → **Récupération**
3. **Démarrage avancé** → **Redémarrer maintenant**
4. **Dépannage** → **Options avancées** → **Paramètres du microprogramme UEFI**
5. Clic sur **Redémarrer** → Le PC démarre directement dans l'UEFI

---

#### C. Navigation dans le BIOS/UEFI

##### 🔸 Menus Principaux (Exemple UEFI Typique)

| **Menu** | **Fonction Principale** |
|----------|------------------------|
| **Main / Information** | Informations système (CPU, RAM, version BIOS, date/heure) |
| **Boot** | **Ordre de démarrage** (priorité des périphériques de boot) |
| **Advanced** | Paramètres avancés (virtualisation, overclocking, gestion énergie) |
| **Security** | Mots de passe BIOS, Secure Boot, TPM |
| **Exit** | Sauvegarder et quitter / Quitter sans sauvegarder / Charger les défauts |

![UEFI Main Menu](uefi_main_menu_example.png)
*Légende : Menu principal d'un UEFI moderne (exemple MSI Click BIOS). Interface graphique avec navigation souris ou clavier fléchée.*

---

##### 🔸 Paramètres Essentiels à Connaître

**1. Date et Heure**
- Impact : Windows et Linux nécessitent une date correcte pour les certificats SSL/TLS
- Réglage : Menu **Main** ou **Advanced → System Time**

**2. Ordre de Boot (Boot Priority)**
- Impact : Définit sur quel périphérique le PC cherche l'OS en premier
- Ordre recommandé classique :
  1. SSD/HDD interne (OS principal)
  2. USB (pour installer un OS ou dépanner)
  3. CD/DVD (rare aujourd'hui)
  4. Réseau (PXE boot - pour installations centralisées)

**3. Virtualization Technology (Intel VT-x / AMD-V)**
- Impact : **Obligatoire** pour utiliser des machines virtuelles (VirtualBox, VMware, Hyper-V)
- Réglage : Menu **Advanced → CPU Configuration**
- ⚠️ **À activer systématiquement** en BTS SIO !

**4. Secure Boot**
- Impact : Empêche le démarrage de logiciels non signés (protection contre rootkits)
- Problème : Peut **bloquer l'installation de Linux** ou de Windows non officiels
- Réglage : Menu **Security → Secure Boot**
- Conseil : **Désactiver** si problème d'installation d'OS

**5. SATA Mode (IDE / AHCI / RAID)**
- Impact : Mode de fonctionnement des disques SATA
- Réglage recommandé : **AHCI** (Advanced Host Controller Interface) pour performances optimales
- ⚠️ Changer ce paramètre sur un Windows déjà installé peut causer un **écran bleu au démarrage** !

---

#### D. La Séquence de Démarrage (Boot Sequence)

##### 🔸 Étapes Détaillées du Démarrage

```
┌──────────────────────────────────────────────────┐
│ 1. APPUI SUR LE BOUTON POWER                     │
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 2. ALIMENTATION envoie signal "POWER GOOD"       │
│    → CPU démarre                                 │
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 3. CPU exécute la première instruction           │
│    → Chargement du BIOS/UEFI depuis la puce ROM │
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 4. POST (Power-On Self Test)                     │
│    • Test RAM                                    │
│    • Test CPU                                    │
│    • Détection disques durs                      │
│    • Détection carte graphique                   │
│    • Test clavier                                │
│    → Si erreur : BIPs sonores ou message        │
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 5. Initialisation des périphériques              │
│    (Carte graphique, clavier, souris, etc.)     │
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 6. Recherche du périphérique BOOTABLE            │
│    selon l'ORDRE DE BOOT défini                  │
│    (1. SSD → 2. USB → 3. CD/DVD → 4. Réseau)   │
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 7. Lecture du MBR ou GPT du disque               │
│    → Chargement du BOOTLOADER                    │
│    (Windows Boot Manager, GRUB pour Linux...)    │
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 8. Le BOOTLOADER charge le noyau de l'OS         │
│    (ntoskrnl.exe pour Windows, vmlinuz pour Linux│
└────────────────┬─────────────────────────────────┘
                 ▼
┌──────────────────────────────────────────────────┐
│ 9. Chargement de l'OS complet                    │
│    → Écran de connexion Windows/Linux           │
└──────────────────────────────────────────────────┘
```

*Légende : Séquence complète de démarrage d'un PC, du bouton Power jusqu'à l'écran de connexion de l'OS. Le BIOS/UEFI intervient dans les étapes 3 à 6.*

---

##### 🔸 Codes BIP (Beep Codes)

Si un problème est détecté durant le POST, le BIOS émet des **bips sonores** pour indiquer l'erreur.

| **Nombre de Bips** | **Signification (Award BIOS)** | **Signification (AMI BIOS)** |
|--------------------|--------------------------------|------------------------------|
| **1 bip court** | ✅ POST réussi (normal) | ✅ POST réussi |
| **1 bip long** | Problème mémoire (RAM) | Problème mémoire |
| **2 bips courts** | Erreur POST (général) | Erreur RAM |
| **3 bips courts** | Erreur RAM (64 premiers Ko) | Erreur RAM |
| **Bips continus** | Problème alimentation ou carte mère | Problème alimentation |
| **Aucun bip** | Problème haut-parleur, CPU ou carte mère | Problème carte mère ou CPU |

⚠️ **Important :** Les codes varient selon le fabricant du BIOS (Award, AMI, Phoenix...). Consulter le manuel de la carte mère !

---

### IV. TP Guidé : Installation de Windows 10/11 en Machine Virtuelle

#### A. Prérequis

**Vérifications à effectuer AVANT de commencer :**

1. ✅ **Virtualisation activée dans le BIOS** (Intel VT-x ou AMD-V)
2. ✅ **Logiciel de virtualisation installé** (VirtualBox, VMware, Hyper-V)
3. ✅ **ISO Windows 10/11 téléchargée** (fichier .iso sur le réseau ou USB)
4. ✅ **Espace disque suffisant** : minimum 20 Go libres
5. ✅ **RAM disponible** : minimum 4 Go pour la VM (donc 8 Go sur le PC hôte)

---

#### B. Étape 1 : Créer une Machine Virtuelle (10 min)

**Sur VirtualBox (exemple) :**

1. Ouvrir **VirtualBox**
2. Clic sur **Nouvelle** (New)
3. Remplir les paramètres :
   - **Nom** : `Windows10_BTS_SIO`
   - **Type** : Microsoft Windows
   - **Version** : Windows 10 (64-bit) ou Windows 11 (64-bit)
4. **Mémoire vive** : Allouer **4096 Mo** (4 Go) minimum
5. **Disque dur** :
   - Sélectionner **Créer un disque dur virtuel maintenant**
   - Type : **VDI (VirtualBox Disk Image)**
   - Stockage : **Dynamiquement alloué** (économise l'espace)
   - Taille : **40 Go** (recommandé)
6. Clic sur **Créer**

---

#### C. Étape 2 : Configurer la VM (5 min)

**Avant de démarrer la VM, configurer :**

1. Sélectionner la VM → Clic droit → **Configuration** (Settings)
2. **Système** :
   - Onglet **Carte mère** : ordre de démarrage → **Optique** en premier, puis **Disque dur**
   - Onglet **Processeur** : Allouer **2 cœurs CPU**
   - Cocher **Activer PAE/NX** si disponible
3. **Affichage** :
   - Mémoire vidéo : **128 Mo**
   - Cocher **Activer l'accélération 3D**
4. **Stockage** :
   - Clic sur l'icône **CD** (Vide)
   - Clic sur l'icône CD à droite → **Choisir un fichier de disque**
   - Sélectionner le fichier **ISO Windows 10/11**
5. **Réseau** :
   - Vérifier que **Mode d'accès réseau** est sur **NAT** ou **Accès par pont**
6. Clic sur **OK**

---

#### D. Étape 3 : Démarrer et Installer Windows (30 min)

**Lancement de l'installation :**

1. Clic droit sur la VM → **Démarrer** → **Démarrage normal**
2. La VM démarre sur l'ISO Windows (comme si on bootait sur un DVD)
3. **Écran "Appuyez sur une touche pour démarrer..."** → Appuyer rapidement sur **Entrée**

**Assistant d'installation Windows :**

1. **Langue d'installation** : Français (France)
2. **Format de l'heure** : Français (France)
3. **Clavier** : Français
4. Clic sur **Suivant** puis **Installer maintenant**
5. **Clé de produit** : 
   - Clic sur **Je n'ai pas de clé de produit** (Windows fonctionnera en mode évaluation 90 jours)
   - Ou utiliser une clé fournie par l'établissement (licence éducation)
6. **Version de Windows** : Sélectionner **Windows 10 Pro** ou **Windows 11 Pro**
7. **Type d'installation** : **Personnalisée (avancée)**
8. **Où voulez-vous installer Windows ?** :
   - Sélectionner le disque virtuel (non alloué, ~40 Go)
   - Clic sur **Suivant** (Windows crée automatiquement les partitions)
9. **Installation en cours** : Patientez 10-20 minutes (copie des fichiers + installation)
10. **Redémarrage automatique** : La VM redémarre automatiquement

**Configuration initiale Windows :**

1. **Région** : France
2. **Disposition du clavier** : Français
3. **Ajouter une deuxième disposition clavier** : Ignorer
4. **Se connecter à un réseau** : Ignorer (ou se connecter si souhaité)
5. **Compte Microsoft** : 
   - Windows 11 : Peut demander obligatoirement un compte Microsoft
   - Astuce : Déconnecter le réseau pour pouvoir créer un compte local
   - Ou utiliser un compte Microsoft éducation si disponible
6. **Compte local** : 
   - Nom : `Administrateur` ou votre nom
   - Mot de passe : Au choix (ne pas oublier !)
7. **Questions de sécurité** : Répondre (nécessaire pour récupération mot de passe)
8. **Paramètres de confidentialité** : Tout **désactiver** (facultatif)
9. **Cortana** : Refuser

**Finalisation :**

10. Windows finalise la configuration (2-5 min)
11. **Bureau Windows** s'affiche → ✅ **Installation réussie !**

---

#### E. Étape 4 : Installation des Guest Additions (10 min)

**Pourquoi ?** Les **Guest Additions** (ou VMware Tools) améliorent les performances et ajoutent des fonctionnalités :
- ✅ Meilleure résolution d'écran (plein écran fluide)
- ✅ Copier-coller entre hôte et VM
- ✅ Partage de dossiers
- ✅ Meilleure gestion de la souris

**Installation (VirtualBox) :**

1. VM démarrée et sur le bureau Windows
2. Menu VirtualBox → **Périphériques** → **Insérer l'image CD des Additions invité...**
3. Windows détecte un CD → **Ouvrir l'Explorateur de fichiers**
4. Double-clic sur le lecteur CD → Lancer **VBoxWindowsAdditions-amd64.exe**
5. Suivre l'assistant (tout laisser par défaut) → **Installer**
6. **Redémarrer** la VM
7. Tester le **plein écran** (Hôte+F ou menu Affichage → Plein écran)

---

### V. Vocabulaire Clé à Maîtriser pour l'Examen

| **Terme** | **Définition** |
|-----------|----------------|
| **Serveur** | Machine dédiée à fournir des services à des clients via un réseau, fonctionnant 24/7 |
| **Redondance** | Duplication de composants critiques pour assurer la continuité en cas de panne |
| **Hot-Swap** | Remplacement d'un composant sans éteindre la machine |
| **Rack** | Armoire standardisée 19 pouces pour monter des serveurs |
| **1U** | Unité de mesure de hauteur dans un rack (1U = 44.45 mm) |
| **iLO / iDRAC** | Carte d'administration à distance intégrée au serveur (HP / Dell) |
| **USB Type-C** | Connecteur USB réversible moderne, multifonction (données + vidéo + alimentation) |
| **HDMI** | Connecteur vidéo numérique + audio, standard multimédia |
| **DisplayPort** | Connecteur vidéo numérique + audio, standard professionnel (support multi-écrans) |
| **RJ45** | Connecteur réseau Ethernet sur câble cuivre (paire torsadée) |
| **Fibre optique** | Câble de transmission de données par lumière, très haut débit et longues distances |
| **Monomode (SMF)** | Fibre optique à cœur fin (9 µm), longues distances (10-100 km) |
| **Multimode (MMF)** | Fibre optique à cœur large (50/62.5 µm), courtes distances (300 m - 2 km) |
| **BIOS** | Basic Input/Output System, firmware gérant le démarrage et l'initialisation matérielle |
| **UEFI** | Unified Extensible Firmware Interface, successeur moderne du BIOS |
| **POST** | Power-On Self Test, test automatique des composants au démarrage |
| **Bootloader** | Programme chargeant le système d'exploitation (ex: Windows Boot Manager, GRUB) |
| **Séquence de boot** | Ordre dans lequel le BIOS cherche un OS sur les périphériques |
| **Secure Boot** | Fonctionnalité UEFI empêchant le démarrage de logiciels non signés |
| **Virtualization Technology** | Extension CPU permettant la virtualisation matérielle (Intel VT-x, AMD-V) |
| **Machine Virtuelle (VM)** | Ordinateur virtuel émulé par logiciel dans un ordinateur physique (hôte) |
| **ISO** | Fichier image d'un CD/DVD, utilisé pour installer des OS |
| **Guest Additions** | Pilotes et outils améliorant les performances d'une VM (VirtualBox) |

---

### VI. Questions de Réflexion (Pour aller plus loin)

1. **Pourquoi un serveur coûte-t-il 5 à 10 fois plus cher qu'un PC de bureau ?**
   - *Piste : Composants redondés, qualité supérieure (RAM ECC, CPU Xeon...), garanties étendues*

2. **Peut-on utiliser un PC de gamer comme serveur ?**
   - *Réponse : Techniquement oui, mais pas de redondance, pas de gestion à distance, moins fiable en 24/7*

3. **Que se passe-t-il si on branche un câble USB 2.0 sur un port USB 3.0 ?**
   - *Réponse : Ça fonctionne, mais à vitesse USB 2.0 (rétrocompatibilité)*

4. **Pourquoi la fibre optique n'est-elle pas utilisée partout à la place du cuivre ?**
   - *Réponse : Coût plus élevé, équipements spécialisés nécessaires, installation plus complexe*

5. **Que signifie "UEFI en mode Legacy" ?**
   - *Réponse : UEFI émulant le comportement d'un BIOS classique pour compatibilité avec vieux OS*

6. **Pourquoi Windows ne démarre-t-il pas si on change SATA de AHCI à IDE après installation ?**
   - *Réponse : Windows charge un driver différent selon le mode SATA au démarrage. Changer après installation fait échouer le chargement du driver.*

---

### VII. Ressources pour Approfondir

**Sites Web :**
- [Wikipedia - BIOS](https://fr.wikipedia.org/wiki/BIOS_(informatique))
- [Wikipedia - UEFI](https://fr.wikipedia.org/wiki/UEFI)
- [TechTarget - Server vs Desktop](https://www.techtarget.com/searchdatacenter/definition/server)

**Vidéos YouTube :**
- "C'est quoi le BIOS ?" - Vulgarisation complète
- "Installer Windows 10 sur VirtualBox" - Tutoriel complet
- "Différences USB 2.0 / 3.0 / 3.1 / Type-C" - Comparatif

**Documentation :**
- Manuels des constructeurs de cartes mères (Asus, MSI, Gigabyte...)
- Documentation VirtualBox officielle
- Guide Microsoft d'installation de Windows

---

### ✅ Auto-évaluation : Suis-je Prêt ?

Après avoir terminé cette séance, je suis capable de :

- [ ] Expliquer les 5 différences principales entre un PC et un serveur
- [ ] Nommer 3 technologies spécifiques aux serveurs (redondance, hot-swap, rack)
- [ ] Identifier visuellement les connecteurs USB Type-A, Type-B et Type-C
- [ ] Différencier HDMI et DisplayPort et expliquer leurs usages
- [ ] Expliquer la différence entre RJ45 et fibre optique
- [ ] Accéder au BIOS/UEFI de mon PC
- [ ] Modifier l'ordre de boot dans le BIOS
- [ ] Décrire la séquence de démarrage d'un PC (POST → Bootloader → OS)
- [ ] Créer une machine virtuelle et y installer Windows
- [ ] Expliquer à quoi sert l'activation de la virtualisation dans le BIOS

---
