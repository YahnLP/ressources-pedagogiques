# 📝 EXERCICES - S13 E31
## VLANs - Pratique

**Nom : ________________  Prénom : ________________**

---

## EXERCICE 1 : Concepts VLANs (5 pts)

**Complète :**

| **Question** | **Réponse** | **(1 pt)** |
|-------------|------------|----------|
| VLAN = Virtual __________ | | |
| Couche OSI des VLANs | | |
| Protocole tagging | | |
| VLAN par défaut (ID) | | |
| DMZ signifie | | |

---

## EXERCICE 2 : Access vs Trunk (4 pts)

**Coche la bonne case :**

| **Caractéristique** | **Access** | **Trunk** |
|-------------------|-----------|----------|
| Connecte 1 PC | ☐ | ☐ |
| Connecte 1 switch | ☐ | ☐ |
| 1 seul VLAN | ☐ | ☐ |
| Plusieurs VLANs | ☐ | ☐ |
| Tagué 802.1Q | ☐ | ☐ |
| Non tagué | ☐ | ☐ |

**Barème :** 0,66 pt par ligne correcte

---

## EXERCICE 3 : Configuration (6 pts)

**Complète les commandes Cisco :**

**Créer VLAN 20 "Compta" :**
```
enable
configure terminal
vlan ______
name ______
exit
```

**Port Fa0/5 en access VLAN 20 :**
```
interface ______
switchport mode ______
switchport access vlan ______
```

**Barème :** 1 pt par blanc

---

## EXERCICE 4 : Segmentation (5 pts)

**Entreprise ABC (3 services) :**

| **Service** | **VLAN ID** | **Réseau IP** | **(1 pt)** |
|------------|------------|--------------|----------|
| DMZ (serveurs web) | 10 | 192.168.10.0/24 | ✅ |
| Production (50 PC) | ____ | 192.168.____.0/24 | |
| Administration (5 PC) | ____ | 192.168.____.0/24 | |

**Question (2 pts) :** Pourquoi isoler DMZ de Production ?

___________________________________________________

___________________________________________________

---

## 📊 BARÈME

| **Exercice** | **Points** | **Note** |
|-------------|-----------|----------|
| Concepts | /5 | |
| Access/Trunk | /4 | |
| Configuration | /6 | |
| Segmentation | /5 | |
| **TOTAL** | **/20** | |

---

**Document - Version 1.0 - Février 2026**
