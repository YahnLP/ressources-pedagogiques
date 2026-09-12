# 🎲 ACTIVITÉ DÉCOUVERTE – S5 ANNÉE 3 – E31
## « Le Réseau dans le Nuage » : Retrouver ses Repères en Infrastructure Cloud

---

## 🎯 OBJECTIFS

- ✅ Réaliser que les **concepts réseau appris en A2 s'appliquent aussi dans le cloud**
- ✅ Identifier les équivalents cloud des objets réseau classiques (VLAN, ACL, routeur, VPN)
- ✅ Comprendre ce qui est **fondamentalement nouveau** dans le cloud (élasticité, tarification, managed services)
- ✅ Dédramatiser le cloud : ce n'est pas de la magie, c'est du réseau qu'on connaît — avec une API

---

## ⏱️ DURÉE : 25 min — GROUPES DE 4

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur pose l'accroche :**

> *"Imaginez que vous êtes responsable réseau. Votre DSI vous dit : 'On déplace notre infrastructure dans le cloud AWS. Le réseau existant doit rester fonctionnel et connecté.' Vous avez 5 minutes pour comprendre ce que vous connaissez déjà."*

---

## 🗺️ PHASE 1 — Mapping Physique → Cloud (10 min)

**Le formateur présente l'infrastructure physique existante au tableau :**

```
Infrastructure physique ON-PREMISES :
═══════════════════════════════════════════════════════════
  [PC-EMPLOYES]──[SWITCH-LAN]──[FIREWALL]──[ROUTEUR]──INTERNET
       │                           │
  VLAN 10 (DMZ)              ACL eth0 in :
  192.168.10.0/24              permit tcp any any eq 443
                               deny tcp any any eq 22
                               permit ip any any
       │
  [SERVEUR-WEB 192.168.10.5]
  [SERVEUR-DB  192.168.10.10]
═══════════════════════════════════════════════════════════
```

**Questions par groupe — 8 min :**

Pour chaque objet réseau physique, trouvez son équivalent cloud probable :

| **Objet physique** | **Votre hypothèse cloud** | **Pourquoi ?** |
|---|---|---|
| Réseau LAN complet (`192.168.10.0/24`) | | |
| VLAN (isolation logique) | | |
| ACL sur le firewall (règle permit/deny) | | |
| Routeur avec accès Internet | | |
| Passerelle par défaut | | |
| Tunnel VPN IPsec vers un partenaire | | |
| Table de routage du routeur | | |

---

## 💡 PHASE 2 — Ce qui est NOUVEAU dans le cloud (5 min)

**Réflexion en groupe :**

> *"Qu'est-ce qui existe dans le cloud que vous ne trouvez PAS dans un réseau physique classique ?"*

```
Pistes à explorer :
  - Que se passe-t-il si le serveur web reçoit 1000× plus de trafic que d'habitude ?
  - Qui s'occupe de changer le disque dur du serveur ?
  - Comment configure-t-on le réseau ? Avec un câble et un terminal SSH ?
  - Si vous supprimez une VM par erreur, que se passe-t-il ?
```

**Éléments nouveaux attendus :**

| **Concept cloud** | **Pas d'équivalent physique direct** |
|---|---|
| **Élasticité** | Auto-scaling : ajouter/supprimer des serveurs en quelques secondes |
| **Infrastructure as Code** | Déployer tout le réseau avec un fichier YAML/JSON (Terraform, CloudFormation) |
| **Zones de disponibilité (AZ)** | Datacenters géographiquement séparés mais dans la même région |
| **Managed services** | RDS, S3, Lambda — plus de matériel à gérer |
| **Tarification à l'usage** | Payer seulement ce qu'on consomme (au Go de trafic, à l'heure de VM) |
| **Régions globales** | Déployer à Paris, Tokyo, São Paulo en quelques clics |

---

## 📊 PHASE 3 — Mise en commun et tableau final (5 min)

**Correction collective — Mapping officiel :**

| **Réseau physique** | **AWS** | **Azure** |
|---|---|---|
| Réseau LAN privé | **VPC** | **vNET** |
| Sous-réseau IP | **Subnet** (dans une AZ) | **Subnet** |
| ACL/Firewall sur instance | **Security Group** (stateful) | **NSG** |
| ACL/Firewall sur sous-réseau | **NACL** (stateless) | **NSG sur subnet** |
| Routeur → Internet | **Internet Gateway** | Intégré |
| NAT/PAT | **NAT Gateway** | **Azure NAT** |
| Tunnel VPN IPsec | **Virtual Private Gateway** | **VPN Gateway** |
| Routeur distant (Cisco) | **Customer Gateway** | **Local Network Gateway** |
| Table de routage | **Route Table** | **User-Defined Routes** |

**Message de conclusion du formateur :**

> *"Vous connaissez déjà 90% du cloud networking — vous avez juste besoin d'apprendre la nouvelle terminologie et les quelques comportements différents (comme le fait que les Security Groups sont stateful, alors que les NACL sont stateless comme vos ACL Cisco). C'est pour ça qu'on a passé deux ans sur les bases réseau — elles s'appliquent partout."*

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
