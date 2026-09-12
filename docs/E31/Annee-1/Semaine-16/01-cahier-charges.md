# 📋 CAHIER DES CHARGES - S16 E31
## Projet Infrastructure PME TECHCORP

---

## 🏢 PRÉSENTATION ENTREPRISE

### **TECHCORP SAS**

**Secteur :** Solutions informatiques  
**Effectif :** 45 employés  
**Localisation :** 1 site unique (bâtiment 2 étages)  
**CA :** 3M€/an  
**Croissance prévue :** +20% (54 employés d'ici 2027)

---

## 📊 ORGANISATION

### **4 Services**

| **Service** | **Effectif** | **Matériel** | **Besoins spécifiques** |
|------------|-------------|-------------|------------------------|
| **Direction** | 5 personnes | 5 PC + 1 imprimante | Confidentialité maximale |
| **Administration** | 10 personnes | 10 PC + 2 imprimantes | Accès fichiers partagés |
| **IT (Technique)** | 15 personnes | 15 PC + serveurs | Accès total réseau |
| **Commercial** | 15 personnes | 15 PC + 2 imprimantes | Accès CRM, Internet |

**Total :** 45 PC + équipements réseau

---

## 🎯 BESOINS EXPRIMÉS

### **1. Segmentation Réseau (Sécurité)**

**Problème actuel :**
- Tous PC dans même réseau (192.168.1.0/24)
- Aucune isolation entre services
- Direction accessible depuis Commercial

**Besoin :**
- **Isoler les 4 services** (VLANs)
- Direction isolée des autres
- WiFi invité isolé du LAN

---

### **2. Serveur Centralisé**

**Problème actuel :**
- Users locaux sur chaque PC (50× créer même user)
- Aucun partage centralisé
- Aucune politique sécurité

**Besoin :**
- **Active Directory** (users centralisés)
- Partages fichiers sécurisés
- **GPO** : Mots de passe forts obligatoires

---

### **3. Attribution IP Automatique**

**Problème actuel :**
- IP statiques configurées manuellement
- Conflits IP fréquents
- Gestion lourde

**Besoin :**
- **DHCP** par VLAN
- Réservations pour serveurs/imprimantes
- Documentation plan IP

---

### **4. Résolution Noms Interne**

**Problème actuel :**
- Accès serveurs par IP (illisible)
- Aucun DNS interne

**Besoin :**
- **DNS** interne : `srv-fichiers.techcorp.local`
- Résolution automatique

---

### **5. WiFi Sécurisé**

**Besoin :**
- **WiFi employés** : WPA2-PSK (20+ car), accès LAN
- **WiFi invités** : WPA2-PSK, Internet SEULEMENT (isolé)

---

## 🏗️ INFRASTRUCTURE CIBLE

### **Équipements à configurer**

| **Équipement** | **Rôle** | **Configuration** |
|---------------|---------|------------------|
| **Switch central** | Distribution VLANs | VLANs 10/20/30/40, trunk |
| **Routeur/L3 Switch** | Routage inter-VLAN | Gateway par VLAN |
| **Serveur Windows** | AD, DHCP, DNS, Fichiers | Windows Server 2019/2022 |
| **Point accès WiFi** | WiFi employés + invités | WPA2, SSID multiples |

---

## 📐 PLAN D'ADRESSAGE IMPOSÉ

### **Classe réseau : 192.168.0.0/16 (Classe B privée)**

| **VLAN** | **Service** | **Réseau** | **Nb hôtes** | **Gateway** | **DHCP Pool** |
|---------|------------|-----------|-------------|------------|--------------|
| **VLAN 10** | Direction | 192.168.10.0/24 | 254 | .1 | .10 - .50 |
| **VLAN 20** | Administration | 192.168.20.0/24 | 254 | .1 | .10 - .50 |
| **VLAN 30** | IT | 192.168.30.0/24 | 254 | .1 | .10 - .50 |
| **VLAN 40** | Commercial | 192.168.40.0/24 | 254 | .1 | .10 - .50 |
| **VLAN 99** | WiFi Invités | 192.168.99.0/24 | 254 | .1 | .10 - .100 |

### **Serveurs (IP fixes réservées)**

| **Serveur** | **VLAN** | **IP** | **Hostname** |
|------------|---------|--------|-------------|
| Contrôleur domaine | VLAN 30 (IT) | 192.168.30.5 | SRV-DC01 |
| Fichiers | VLAN 30 (IT) | 192.168.30.6 | SRV-FILES |
| DHCP/DNS | VLAN 30 (IT) | 192.168.30.5 | (même DC) |

### **Imprimantes (IP fixes réservées)**

| **Imprimante** | **VLAN** | **IP** |
|---------------|---------|--------|
| Imprimante Direction | VLAN 10 | 192.168.10.100 |
| Imprimante Admin 1 | VLAN 20 | 192.168.20.100 |
| Imprimante Admin 2 | VLAN 20 | 192.168.20.101 |

---

## 📋 LIVRABLES ATTENDUS

### **Livrable 1 : Schémas Réseau**

**Schéma physique :**
- Topologie matérielle
- Câblage (switch ↔ routeur ↔ serveur)
- Identification ports

**Schéma logique :**
- VLANs avec codes couleur
- Plan IP par VLAN
- Flux communication

**Format :** Draw.io, Dia, ou papier scanné

---

### **Livrable 2 : Plan d'Adressage Détaillé**

**Tableau Excel/Calc :**

| VLAN | Service | Réseau | Masque | Gateway | DHCP Start | DHCP End | Nb hôtes |
|------|---------|--------|--------|---------|-----------|----------|---------|
| 10 | Direction | 192.168.10.0 | /24 | .1 | .10 | .50 | 254 |
| ... | ... | ... | ... | ... | ... | ... | ... |

---

### **Livrable 3 : Configurations Équipements**

**Fichiers texte (.txt) :**

**switch-config.txt :**
```
! Configuration VLANs
vlan 10
 name Direction
vlan 20
 name Administration
...
```

**server-config.txt :**
```
Rôles installés :
- AD DS (techcorp.local)
- DHCP (scopes VLAN 10-40)
- DNS (zones techcorp.local)
```

---

### **Livrable 4 : Tests & Validation**

**Captures Wireshark :**
- Ping inter-VLAN réussi
- DNS Query/Response
- DHCP Discover/Offer

**Tableau tests :**

| Test | Résultat | Capture |
|------|---------|---------|
| PC VLAN10 → PC VLAN20 (ping) | ✅ OK | ping-vlan10-20.pcap |
| DHCP automatique VLAN30 | ✅ OK | dhcp-vlan30.pcap |
| DNS srv-dc01.techcorp.local | ✅ OK | dns-query.pcap |

---

### **Livrable 5 : Documentation Utilisateur**

**Guide connexion WiFi :**
- SSID : TECHCORP-EMPLOYES
- Sécurité : WPA2-PSK
- MDP : [20+ caractères ANSSI]

**Guide accès serveur :**
- Connexion domaine : `TECHCORP\utilisateur`
- Partages : `\\SRV-FILES\Commun`

---

### **Livrable 6 : Présentation Orale (15 min)**

**Contenu :**
1. Présentation architecture (schéma)
2. Choix techniques (pourquoi VLANs, plan IP...)
3. Difficultés rencontrées + solutions
4. Démonstration live (ping, connexion AD)
5. Q&A formateur

---

## ⏱️ JALONS PROJET

### **Jalon 1 - Fin Séance 1 (Conception)**

**Validations formateur :**
- [ ] Plan IP cohérent (pas conflit)
- [ ] VLANs définis (ID, nom, réseau)
- [ ] Schéma logique clair

---

### **Jalon 2 - Fin Séance 2 (Implémentation)**

**Tests obligatoires :**
- [ ] VLANs créés sur switch
- [ ] Routage inter-VLAN fonctionnel
- [ ] Serveur AD accessible

---

### **Jalon 3 - Fin Séance 3 (Finalisation)**

**Livrables complets :**
- [ ] Documentation technique
- [ ] Captures Wireshark
- [ ] Présentation prête

---

## 🏆 CRITÈRES ÉVALUATION

### **Conception (/6)**

- Plan IP cohérent : /2
- VLANs justifiés : /2
- Schéma clair : /2

### **Implémentation (/10)**

- VLANs fonctionnels : /3
- Routage inter-VLAN : /3
- Serveur AD + DHCP : /3
- WiFi sécurisé : /1

### **Documentation (/4)**

- Schémas : /1
- Tableaux IP : /1
- Configs sauvegardées : /1
- Présentation orale : /1

---

## 💡 CONSEILS TECHNIQUES

**VLANs :**
- Commencer simple (VLAN 10 seul)
- Tester isolation AVANT ajouter autres
- Trunk bidirectionnel (switch ↔ routeur)

**Active Directory :**
- Installer AD DS AVANT DHCP/DNS
- Promouvoir DC avec domaine `techcorp.local`
- Créer OUs par service (S11)

**DHCP :**
- 1 scope par VLAN
- Exclure .1-.9 (réservé équipements)
- Option 003 : Gateway VLAN

**Wireshark :**
- Capturer sur interface switch (port mirror)
- Filtres : `icmp`, `dhcp`, `dns`

---

## ❓ FAQ PROJET

**Q : Packet Tracer ou matériel réel ?**

**R :** Les 2 acceptés. Packet Tracer = Simulation (accessible). Matériel réel = Bonus valorisé.

---

**Q : Combien de PC clients minimum ?**

**R :** 1 PC par VLAN (4 minimum). Idéal : 2-3 par VLAN.

---

**Q : WiFi obligatoire ?**

**R :** WiFi employés = Souhaitable. WiFi invité isolé = Bonus (+1 pt).

---

**Q : Si blocage technique ?**

**R :** Appeler formateur (fiche "Appel"). Conception + documentation = 50% note (même si implémentation échoue).

---

## 📅 PLANNING DÉTAILLÉ

**Semaine 16 - Séance 1 (4h) :**
- Lecture cahier charges
- Brainstorming architecture
- Conception plan IP + VLANs
- Schémas réseau
- **Validation Jalon 1**

**Semaine 17 - Séance 2 (4h) :**
- Configuration switch (VLANs, trunk)
- Configuration routeur (inter-VLAN)
- Installation serveur (AD, DHCP, DNS)
- Tests connectivité
- **Validation Jalon 2**

**Semaine 18 - Séance 3 (4h) :**
- WiFi sécurisé
- Documentation finale
- Préparation présentation
- **Présentations orales** (15 min/groupe)
- **Validation Jalon 3**

---

**Document - Cahier des Charges TECHCORP - Version 1.0 - Février 2026**
