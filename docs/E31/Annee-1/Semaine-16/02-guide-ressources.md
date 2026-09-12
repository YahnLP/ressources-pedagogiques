# 📚 GUIDE RESSOURCES - S16 E31
## Mobiliser Compétences S1-S15 pour Projet TECHCORP

---

## 🎯 PRINCIPE

> **S16 n'apprend RIEN de nouveau. S16 UTILISE tout ce qui a été appris en S1-S15.**

**Ce guide vous aide à retrouver rapidement les connaissances nécessaires.**

---

## 🗺️ CARTE COMPÉTENCES

| **Tâche Projet** | **Séance Référence** | **Document** | **Page/Section** |
|-----------------|---------------------|-------------|-----------------|
| Câbler switch-routeur | **S2** | Fiche TP RJ45 | Procédure sertissage |
| Identifier couches OSI | **S3** | Fiche Cours | Tableau 7 couches |
| Créer plan IP | **S4** | Fiche Cours + TP | Plan adressage PME |
| Configurer VLANs | **S13** | Fiche TP | Commandes CLI |
| Installer AD | **S11** | Fiche TP | Installation AD DS |
| Créer GPO sécurité | **S12** | Fiche TP | Politique MDP |
| Sécuriser WiFi | **S14** | Fiche Cours | WPA2-PSK config |
| Diagnostiquer Wireshark | **S15** | Fiche TP | Filtres + Follow Stream |

---

## 🔧 RESSOURCES PAR TÂCHE

### **TÂCHE 1 : Plan d'Adressage IPv4**

**📘 Référence :** S4 - Adressage IPv4

**Rappels clés :**

**Classe C privée (projet) :**
- Réseau : 192.168.x.0/24
- Masque : 255.255.255.0
- Hôtes : 254 par réseau

**Règles projet :**
- 1 VLAN = 1 réseau IP distinct
- VLAN 10 → 192.168.10.0/24
- VLAN 20 → 192.168.20.0/24
- etc.

**Réservations :**
- .1 = Gateway (routeur)
- .2-.9 = Serveurs/équipements
- .10-. = DHCP pool

**Outil :** Calculateur IP (ipcalc.org) autorisé

---

### **TÂCHE 2 : VLANs Segmentation**

**📘 Référence :** S13 - VLANs 802.1Q

**Commandes Cisco (rappel) :**

**Créer VLAN :**
```cisco
enable
configure terminal
vlan 10
 name Direction
exit
```

**Port access :**
```cisco
interface fa0/1
 switchport mode access
 switchport access vlan 10
exit
```

**Port trunk :**
```cisco
interface fa0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30,40
exit
```

**Vérifier :**
```cisco
show vlan brief
show interfaces trunk
```

**⚠️ Rappel S13 :** Trunk bidirectionnel (configurer 2 côtés)

---

### **TÂCHE 3 : Routage Inter-VLAN**

**📘 Référence :** S13 (mention) + Cours complémentaire

**2 méthodes :**

**Méthode 1 : Router-on-a-stick**
- 1 interface physique
- Sous-interfaces par VLAN

**Méthode 2 : Switch L3 (recommandé si dispo)**
- Interfaces VLAN virtuelles
- Routage IP activé

**Config switch L3 (exemple) :**
```cisco
ip routing
interface vlan 10
 ip address 192.168.10.1 255.255.255.0
 no shutdown
interface vlan 20
 ip address 192.168.20.1 255.255.255.0
 no shutdown
```

**Test :**
```
PC VLAN10 → ping 192.168.20.1 (gateway VLAN20)
```

---

### **TÂCHE 4 : Active Directory**

**📘 Référence :** S11 - Active Directory

**Procédure rappel :**

**1. Installer rôle AD DS**
```
Gestionnaire Serveur → Ajouter rôles → AD DS
```

**2. Promouvoir DC**
```
Notification → Promouvoir ce serveur
Nouvelle forêt : techcorp.local
Mot de passe DSRM
```

**3. Créer OUs**
```
dsa.msc
Clic droit domaine → Nouvelle OU
Noms : Direction, Administration, IT, Commercial
```

**4. Créer users**
```
Clic droit OU → Nouveau → Utilisateur
alice.martin
Mot de passe (respecter GPO si configurée)
```

---

### **TÂCHE 5 : DHCP**

**📘 Référence :** Cours complémentaire (S16)

**Installation :**
```
Gestionnaire Serveur → Ajouter rôles → DHCP
```

**Configuration scope (1 par VLAN) :**

**VLAN 10 (Direction) :**
- Nom scope : VLAN10-Direction
- Plage : 192.168.10.10 - 192.168.10.50
- Masque : 255.255.255.0
- Gateway (003) : 192.168.10.1
- DNS (006) : 192.168.30.5 (serveur AD)

**Exclure :**
- 192.168.10.1 - 192.168.10.9 (réservé)

**Répéter pour VLANs 20, 30, 40**

---

### **TÂCHE 6 : DNS**

**📘 Référence :** Installation avec AD (S11)

**DNS installé automatiquement avec AD DS**

**Zones créées :**
- Zone directe : `techcorp.local`
- Zone inverse : `10.168.192.in-addr.arpa` (pour 192.168.10.0)

**Enregistrements A (hôtes) :**
```
SRV-DC01 → 192.168.30.5
SRV-FILES → 192.168.30.6
```

**Test :**
```cmd
nslookup srv-dc01.techcorp.local
```

---

### **TÂCHE 7 : GPO Sécurité**

**📘 Référence :** S12 - GPO

**Politique MDP stricte (rappel ANSSI) :**

**Console GPMC :**
```
gpmc.msc
Clic droit OU → Lier GPO existante
OU créer nouvelle : "Politique MDP Stricte"
```

**Configuration :**
```
Ordinateur → Stratégies → Sécurité
Stratégies compte → Stratégie mot de passe
- Longueur min : 12 caractères (ANSSI : 20)
- Complexité : Activée
- Historique : 5 MDP
- Durée vie max : 90 jours
```

**Forcer MAJ (client) :**
```cmd
gpupdate /force
```

---

### **TÂCHE 8 : WiFi Sécurisé**

**📘 Référence :** S14 - WiFi WPA2

**Configuration AP :**

**SSID 1 : Employés**
- Nom : TECHCORP-EMPLOYES
- Sécurité : WPA2-PSK (AES)
- Passphrase : 20+ caractères
- VLAN : 30 (IT) ou trunked

**SSID 2 : Invités (bonus)**
- Nom : TECHCORP-INVITES
- Sécurité : WPA2-PSK
- VLAN : 99 (isolé)
- Isolation client : Activée

**⚠️ Rappel S14 :** ANSSI recommande 20+ caractères

---

### **TÂCHE 9 : Tests Wireshark**

**📘 Référence :** S15 - Wireshark

**Captures recommandées :**

**Test ping inter-VLAN :**
```
Filtre : icmp
Capture : PC VLAN10 → ping 192.168.20.x
Observer : Echo Request/Reply
```

**Test DHCP :**
```
Filtre : dhcp
Capture : PC demande IP
Observer : Discover → Offer → Request → ACK
```

**Test DNS :**
```
Filtre : dns
Capture : nslookup srv-dc01.techcorp.local
Observer : Query → Response
```

**Follow Stream (HTTP si applicable) :**
```
Clic droit paquet → Follow TCP Stream
```

---

## 🛠️ OUTILS RECOMMANDÉS

### **Schémas Réseau**

**Draw.io (recommandé) :**
- Gratuit, en ligne
- Templates réseau
- Export PNG/PDF

**Packet Tracer :**
- Simulation + schémas
- Cisco officiel

**Dia :**
- Open source
- Formes réseau intégrées

---

### **Documentation**

**LibreOffice Calc :**
- Tableaux IP
- Tableur gratuit

**Markdown (.md) :**
- Documentation texte
- Lisible, versionnable

---

### **Tests & Diagnostic**

**Wireshark :**
- Captures réseau
- Filtres display

**Commandes réseau :**
```cmd
ping 192.168.x.x        # Test connectivité
ipconfig /all           # Config IP locale
nslookup hostname       # Test DNS
tracert IP             # Chemin réseau
```

---

## 📋 CHECKLIST PROJET

### **Avant Séance 1 (Préparation)**

- [ ] Relire cahier charges TECHCORP
- [ ] Réviser S4 (plan IP), S13 (VLANs)
- [ ] Préparer outils (Draw.io, calculateur IP)

---

### **Séance 1 (Conception)**

- [ ] Définir VLANs (ID, nom, service)
- [ ] Calculer plan IP (réseau, masque, gateway)
- [ ] Dessiner schéma logique (VLANs, IP)
- [ ] **Validation formateur Jalon 1**

---

### **Séance 2 (Implémentation)**

- [ ] Configurer VLANs switch
- [ ] Configurer trunk
- [ ] Configurer routage inter-VLAN
- [ ] Installer AD DS (domaine techcorp.local)
- [ ] Configurer DHCP (scopes par VLAN)
- [ ] Tester connectivité (ping inter-VLAN)
- [ ] **Validation formateur Jalon 2**

---

### **Séance 3 (Finalisation)**

- [ ] Configurer WiFi WPA2
- [ ] (Bonus) WiFi invité isolé VLAN 99
- [ ] (Bonus) GPO sécurité MDP
- [ ] Capturer Wireshark (DHCP, DNS, ping)
- [ ] Finaliser documentation (schémas, tableaux)
- [ ] Préparer présentation orale
- [ ] **Présentation 15 min**
- [ ] **Validation formateur Jalon 3**

---

## ❓ FAQ RESSOURCES

**Q : Où trouver commandes CLI Cisco ?**

**R :** Fiche S13 VLANs, section "Configuration AP"

---

**Q : Comment calculer nb hôtes /24 ?**

**R :** Fiche S4 IPv4 : 2^8 - 2 = 254 hôtes

---

**Q : AD DS = quels ports ?**

**R :** 
- LDAP : 389
- Kerberos : 88
- DNS : 53

---

**Q : Wireshark filtre DHCP ?**

**R :** Fiche S15, section "Filtres Display" : `dhcp`

---

## 🎯 CONSEIL FINAL

**Ne réinventez pas la roue :**
- Tout a déjà été vu en S1-S15
- Utilisez VOS fiches de cours
- Adaptez au contexte TECHCORP

**Méthodologie :**
1. Lire cahier charges
2. Identifier tâches nécessaires
3. Retrouver séances correspondantes (ce guide)
4. Appliquer connaissances au projet

**En cas de doute :**
→ Consultez fiches cours S1-S15  
→ Appelez formateur (fiche "Appel")

---

**Document - Guide Ressources TECHCORP - Version 1.0 - Février 2026**
