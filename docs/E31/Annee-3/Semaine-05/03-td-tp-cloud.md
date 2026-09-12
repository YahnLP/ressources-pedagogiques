# 🎯 TD + TP CLOUD NETWORKING – S5 ANNÉE 3 – E31
## AWS VPC, Azure vNET, Security Groups, NSG, VPN Site-à-Site

**Nom : ________________  Prénom : ________________  Date : ________________**

---

# ═══════════════════════════════════════════
# PARTIE 1 — TD : Conception Architecture Cloud (30 min)
# ═══════════════════════════════════════════

## Contexte

> **MediCloud** est une startup qui développe une application de gestion médicale. Elle doit déployer son infrastructure sur AWS. La réglementation impose que les données patients soient sur un subnet isolé d'Internet.

---

## TD1 — Plan d'adressage VPC (4 pts)

### Spécifications

| **Subnet** | **Nb d'hôtes min.** | **Type** | **Rôle** |
|---|---|---|---|
| Public A (AZ-A) | 15 | Public | Load Balancer + Bastion |
| Public B (AZ-B) | 15 | Public | Load Balancer (HA) |
| App A (AZ-A) | 50 | Privé | Serveurs applicatifs |
| App B (AZ-B) | 50 | Privé | Serveurs applicatifs (HA) |
| DB A (AZ-A) | 10 | Isolé | Base de données patients |
| DB B (AZ-B) | 10 | Isolé | Base de données (HA) |

**VPC CIDR de base : `10.10.0.0/16`**

**TD1.1 *(2 pts)*** — Complétez le plan d'adressage (choisir le préfixe minimal adapté) :

| **Subnet** | **Préfixe** | **CIDR** | **Broadcast** |
|---|---|---|---|
| Public A | | 10.10.1.0/____ | |
| Public B | | 10.10.2.0/____ | |
| App A | | 10.10.11.0/____ | |
| App B | | 10.10.12.0/____ | |
| DB A | | 10.10.21.0/____ | |
| DB B | | 10.10.22.0/____ | |

**TD1.2 *(1 pt)*** — Le médecin-chef IT vous dit : "Nos serveurs App ont besoin de télécharger les mises à jour depuis Internet, mais ils ne doivent pas être joignables depuis Internet." Quelle combinaison de composants AWS permet ça ?

_________________________________________________________________________
_________________________________________________________________________

**TD1.3 *(1 pt)*** — Complétez les route tables :

```
Route Table Subnet Public :
  Destination    Target
  10.10.0.0/16   _______________
  0.0.0.0/0      _______________  ← accès Internet complet

Route Table Subnet App (privé) :
  Destination    Target
  10.10.0.0/16   _______________
  0.0.0.0/0      _______________  ← sortie Internet seulement
  
Route Table Subnet DB (isolé) :
  Destination    Target
  10.10.0.0/16   _______________  ← accès interne VPC seulement
```

---

## TD2 — Security Groups MediCloud (6 pts)

### Architecture 3 tiers

```
Internet → [Load Balancer (subnet public)] → [App Server (subnet app)] → [DB (subnet DB)]
           SG-LB                              SG-APP                       SG-DB
```

**TD2.1 *(2 pts)*** — Rédigez les règles inbound de SG-LB (Load Balancer) :

> Contexte : Le LB reçoit le trafic HTTPS public (443) et HTTP (80, redirigé vers HTTPS). Les administrateurs peuvent se connecter en SSH uniquement depuis le réseau VPN d'entreprise (10.100.0.0/24). Aucun autre accès.

| **Type** | **Protocole** | **Port** | **Source** | **Description** |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

**TD2.2 *(2 pts)*** — Rédigez les règles inbound de SG-APP :

> Contexte : Les serveurs App reçoivent le trafic de l'application depuis le LB sur le port 8443 (HTTPS custom). Ils acceptent aussi SSH depuis le réseau de management interne (10.10.100.0/24, à ajouter dans votre plan si besoin). Aucun autre accès.

| **Type** | **Protocole** | **Port** | **Source** | **Description** |
|---|---|---|---|---|
| | | | | |
| | | | | |

**TD2.3 *(1 pt)*** — Rédigez les règles inbound de SG-DB :

> Contexte : La base de données PostgreSQL (port 5432) accepte uniquement les connexions des serveurs applicatifs. Aucun accès depuis Internet ni depuis les admins.

| **Type** | **Protocole** | **Port** | **Source** | **Description** |
|---|---|---|---|---|
| | | | | |

**TD2.4 *(1 pt)*** — Pourquoi n'y a-t-il pas besoin d'écrire des règles outbound spécifiques pour SG-DB ?

_________________________________________________________________________

---

## TD3 — VPN Hybride MediCloud (4 pts)

> MediCloud veut connecter son datacenter on-premises (où se trouve son système de facturation legacy, réseau `172.20.0.0/16`) à son VPC AWS.

**TD3.1 *(1 pt)*** — Nommez les deux objets AWS à créer côté cloud pour ce VPN :

1. _______________________ (attaché au VPC, côté AWS du tunnel)
2. _______________________ (décrit le routeur on-premises Cisco)

**TD3.2 *(1 pt)*** — Côté routeur Cisco on-premises, quelle configuration doit-on écrire pour que le trafic `172.20.0.0/16 → 10.10.0.0/16` passe dans le tunnel ? (Nommez juste le type d'objet de config, pas la syntaxe complète)

_________________________________________________________________________

**TD3.3 *(1 pt)*** — Dans la route table du subnet App, quelle route faut-il ajouter pour que les serveurs App puissent joindre le système de facturation à `172.20.0.0/16` ?

```
Route Table Subnet App — Ligne à ajouter :
  Destination    Target
  _______________  _______________
```

**TD3.4 *(1 pt)*** — La connexion VPN AWS fournit deux tunnels IPsec simultanés (tunnel A et tunnel B). Quel avantage cela apporte-t-il par rapport à la configuration de S7-A2 qui n'avait qu'un seul tunnel ?

_________________________________________________________________________
_________________________________________________________________________

---

# ═══════════════════════════════════════════
# PARTIE 2 — TP : Schéma et Documentation (40 min)
# ═══════════════════════════════════════════

## Mode A — Console AWS Sandbox (si disponible)

> Connectez-vous au compte sandbox AWS fourni par le formateur et deployez :
> 1. Un VPC `10.20.0.0/16`
> 2. Un subnet public `10.20.1.0/24` et un subnet privé `10.20.11.0/24`
> 3. Une Internet Gateway attachée au VPC
> 4. Une route table pour le subnet public (0.0.0.0/0 → IGW)
> 5. Un Security Group avec les règles : inbound SSH TCP 22 depuis votre IP, inbound HTTP TCP 80 depuis partout

## Mode B — Documentation Draw.io / Schéma (si pas de console)

> Reproduisez sur papier (ou Draw.io) le schéma d'architecture suivant en complétant tous les éléments manquants :

```
┌────────────────────── VPC 10.20.0.0/16 ──────────────────────────┐
│                                                                    │
│  ┌─── AZ-A ──────────────────────────────────────────────────┐   │
│  │                                                            │   │
│  │  ┌─ Subnet Public 10.20.1.0/____ ──────┐                  │   │
│  │  │  [EC2 WEB]  [EC2 WEB2]              │──── Route ──────►│IGW│─► Internet
│  │  │  SG-WEB                             │                  │   │
│  │  └─────────────────────────────────────┘                  │   │
│  │                 │ (port 8080)                             │   │
│  │  ┌─ Subnet Privé 10.20.11.0/____ ──────┐                 │   │
│  │  │  [EC2 APP]                          │                  │   │
│  │  │  SG-APP                             │──── Route ──────►│NAT│─► Internet
│  │  └─────────────────────────────────────┘                  │   │
│  │                 │ (port 5432)                             │   │
│  │  ┌─ Subnet DB 10.20.21.0/____ ─────────┐                 │   │
│  │  │  [RDS PostgreSQL]                   │                  │   │
│  │  │  SG-DB                              │                  │   │
│  │  └─────────────────────────────────────┘                  │   │
│  └────────────────────────────────────────────────────────────┘   │
│                                                                    │
│                      [Virtual Private Gateway] ◄──── VPN ─────── [Routeur Cisco]
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### Questions TP (Mode A ou B)

**Q1.** Complétez les préfixes des 3 subnets dans le schéma (choisir /27 ou /28 selon les besoins).

**Q2.** Remplissez le tableau des Security Groups :

| **SG** | **Règle inbound** | **Port** | **Source** |
|---|---|---|---|
| SG-WEB | HTTP | 80 | |
| SG-WEB | HTTPS | 443 | |
| SG-WEB | SSH | 22 | |
| SG-APP | App traffic | 8080 | |
| SG-APP | SSH | 22 | |
| SG-DB | PostgreSQL | 5432 | |

**Q3.** Où doit se trouver la NAT Gateway dans le schéma ? Sur quel subnet est-elle déployée ?

_________________________________________________________________________

**Q4.** Vous devez permettre aux EC2 APP de se mettre à jour (`apt update`) mais ils ne doivent pas être joignables depuis Internet. Est-ce que votre architecture actuelle le permet ? Justifiez.

_________________________________________________________________________
_________________________________________________________________________

**Q5.** Si vous deviez ajouter un 2ème AZ pour la haute disponibilité, citez les 3 éléments qu'il faudrait dupliquer :

1. _______________________________________________________________________
2. _______________________________________________________________________
3. _______________________________________________________________________

---

## 📊 BARÈME

| **Section** | **Points** |
|---|---|
| TD1 — Plan d'adressage | /4 |
| TD2 — Security Groups | /6 |
| TD3 — VPN hybride | /4 |
| TP — Schéma + Q1 à Q5 | /6 |
| **TOTAL** | **/20** |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
