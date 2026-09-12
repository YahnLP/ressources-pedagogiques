# 📊 GRILLE ÉVALUATION - S16 E31
## Projet Infrastructure PME TECHCORP

**Groupe : ________________**  
**Membres : ________________**

---

## 🎯 BARÈME GLOBAL (/20)

| **Critère** | **Points** | **Note** |
|------------|-----------|----------|
| **1. CONCEPTION** | /6 | |
| **2. IMPLÉMENTATION** | /10 | |
| **3. DOCUMENTATION** | /4 | |
| **TOTAL** | **/20** | |
| **Bonus** (max +3) | | |
| **TOTAL FINAL** | **/20** | |

---

## 1️⃣ CONCEPTION (/6)

### **1.1 Plan d'Adressage IPv4 (/2)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Expert** | Plan IP cohérent, aucun conflit, réservations serveurs/imprimantes, documentation complète | **2** |
| **Maîtrisé** | Plan IP cohérent, pas de conflit majeur, réservations basiques | **1,5** |
| **Fragile** | Plan IP avec erreurs mineures (quelques conflits corrigés) | **1** |
| **Non acquis** | Plan IP incohérent ou absent | **0** |

**Vérifications :**
- [ ] VLANs différents = réseaux IP différents
- [ ] Pas de chevauchement plages
- [ ] Gateway cohérente (.1)
- [ ] Pools DHCP ne chevauchent pas IP fixes

---

### **1.2 Segmentation VLANs (/2)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Expert** | 4+ VLANs justifiés (Direction, Admin, IT, Commercial) + WiFi invité (VLAN 99) | **2** |
| **Maîtrisé** | 4 VLANs services, justification claire | **1,5** |
| **Fragile** | 2-3 VLANs, justification partielle | **1** |
| **Non acquis** | 1 VLAN ou aucune segmentation | **0** |

**Vérifications :**
- [ ] Chaque service = 1 VLAN
- [ ] WiFi invité isolé (VLAN dédié)
- [ ] Justification sécurité claire

---

### **1.3 Schémas Réseau (/2)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Expert** | Schémas physique ET logique, clairs, légende, codes couleur VLANs | **2** |
| **Maîtrisé** | Schéma logique clair, VLANs identifiés | **1,5** |
| **Fragile** | Schéma basique lisible | **1** |
| **Non acquis** | Schéma illisible ou absent | **0** |

**Vérifications :**
- [ ] Topologie visible (switch ↔ routeur ↔ serveur)
- [ ] VLANs représentés (couleurs ou labels)
- [ ] Plan IP intégré au schéma

---

## 2️⃣ IMPLÉMENTATION (/10)

### **2.1 VLANs Fonctionnels (/3)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Expert** | 4+ VLANs créés, ports access corrects, trunk bidirectionnel OK, tests isolation réussis | **3** |
| **Maîtrisé** | 3-4 VLANs fonctionnels, isolation testée | **2** |
| **Fragile** | 2 VLANs créés, tests partiels | **1** |
| **Non acquis** | VLANs non créés ou non fonctionnels | **0** |

**Tests obligatoires :**
- [ ] PC VLAN10 → PC VLAN10 (ping ✅)
- [ ] PC VLAN10 → PC VLAN20 (ping ❌ AVANT routage)
- [ ] `show vlan brief` = VLANs listés

---

### **2.2 Routage Inter-VLAN (/3)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Expert** | Routage inter-VLAN fonctionnel, tous VLANs communiquent, gateway configurées | **3** |
| **Maîtrisé** | Routage partiel (2-3 VLANs), tests OK | **2** |
| **Fragile** | Routage configuré mais tests échouent | **1** |
| **Non acquis** | Pas de routage configuré | **0** |

**Tests obligatoires :**
- [ ] PC VLAN10 → PC VLAN20 (ping ✅)
- [ ] PC VLAN30 → PC VLAN40 (ping ✅)
- [ ] `traceroute` montre passage gateway

---

### **2.3 Serveur AD + DHCP + DNS (/3)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Expert** | AD DS installé, domaine créé, OUs par service, users créés, DHCP 4+ scopes, DNS résolution OK | **3** |
| **Maîtrisé** | AD fonctionnel, 1-2 users, DHCP 2+ scopes, DNS basique | **2** |
| **Fragile** | AD installé, DHCP partiel OU DNS partiel | **1** |
| **Non acquis** | Serveur non configuré | **0** |

**Tests obligatoires :**
- [ ] PC joint domaine `techcorp.local`
- [ ] User AD se connecte
- [ ] PC obtient IP DHCP automatiquement
- [ ] `nslookup srv-dc01.techcorp.local` = IP

---

### **2.4 WiFi Sécurisé (/1)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Maîtrisé** | WiFi employés WPA2 (20+ car), connexion testée | **1** |
| **Fragile** | WiFi WPA2 mais MDP < 20 car | **0,5** |
| **Non acquis** | WiFi absent ou ouvert | **0** |

**Bonus (+1) :** WiFi invité isolé (VLAN 99)

---

## 3️⃣ DOCUMENTATION (/4)

### **3.1 Schémas Techniques (/1)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Complet** | Schémas physique + logique, exportés (PNG/PDF) | **1** |
| **Partiel** | 1 schéma seulement | **0,5** |
| **Absent** | Pas de schéma livré | **0** |

---

### **3.2 Tableaux IP (/1)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Complet** | Tableau VLANs complet (réseau, masque, gateway, DHCP pool) | **1** |
| **Partiel** | Tableau incomplet | **0,5** |
| **Absent** | Pas de tableau | **0** |

---

### **3.3 Configurations Sauvegardées (/1)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Complet** | Configs switch, routeur, serveur sauvegardées (.txt) | **1** |
| **Partiel** | 1-2 configs | **0,5** |
| **Absent** | Aucune config | **0** |

---

### **3.4 Présentation Orale (/1)**

| **Niveau** | **Critères** | **Points** |
|-----------|-------------|-----------|
| **Expert** | Présentation claire (15 min), tous membres parlent, démo live réussie | **1** |
| **Maîtrisé** | Présentation OK, participation déséquilibrée | **0,75** |
| **Fragile** | Présentation brouillonne, pas de démo | **0,5** |
| **Non acquis** | Pas de présentation | **0** |

---

## 🎁 BONUS (max +3)

| **Bonus** | **Points** |
|----------|-----------|
| WiFi invité isolé (VLAN 99) fonctionnel | **+1** |
| Captures Wireshark pertinentes (DHCP, DNS, ping) | **+1** |
| GPO sécurité configurée (politiques MDP) | **+1** |
| Matériel réel (vs Packet Tracer) | **+0,5** |
| Documentation exemplaire (guide utilisateur) | **+0,5** |

---

## ✅ VALIDATION PROJET

| **Note** | **Niveau** | **Commentaire** |
|---------|-----------|----------------|
| **16-20** | **Expert** | Projet exemplaire, compétences A1 maîtrisées |
| **12-15** | **Maîtrisé** | Projet solide, quelques améliorations possibles |
| **10-11** | **Fragile** | Validation minimale, révisions conseillées |
| **< 10** | **Non acquis** | Rattrapage obligatoire (projet simplifié) |

**Seuil passage A2 :** **10/20**

---

## 💬 COMMENTAIRES FORMATEUR

**Points forts :**

___________________________________________________

___________________________________________________

**Points à améliorer :**

___________________________________________________

___________________________________________________

**Recommandations A2 :**

___________________________________________________

---

**Évaluateur : ________________  Date : ____/____/2026**

---

**Document - Version 1.0 - Février 2026**
