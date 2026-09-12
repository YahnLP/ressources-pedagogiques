# 📄 ÉPREUVE PRATIQUE — E31 BLANC
## Infrastructure Réseau Multi-Sites : Conception, Déploiement, Sécurisation

**Nom : ________________  Prénom : ________________  Date : ________________**

| **Durée** | **2h30 (chrono strict)** | **Documents** | Fiche cours autorisée | **Barème** | **/60 pts** |
|---|---|---|---|---|---|

---

> ⚠️ **RÈGLES D'EXAMEN**
> - Vous travaillez seul(e). Toute communication est interdite.
> - Packet Tracer est ouvert. La topologie de câblage est déjà réalisée.
> - Vous pouvez attaquer les parties dans l'ordre de votre choix.
> - Indiquez clairement sur votre feuille le numéro de chaque réponse.
> - **Conseil de gestion du temps :** Parties 1–2 (35 min) → Partie 3 (25 min) → Partie 4 (30 min) → Partie 5 (20 min) → Partie 6 (20 min) → Relecture (20 min)

---

## 🏢 CONTEXTE PROFESSIONNEL

> **SYNTHETIX** est une entreprise pharmaceutique avec deux sites :
> - **Site Bordeaux (siège)** : R&D, administration, serveurs internes
> - **Site Marseille (production)** : chaîne de production, laboratoires
>
> Vous êtes l'ingénieur réseau en charge du déploiement complet. Ce déploiement engage la conformité réglementaire (traçabilité des accès aux données de recherche) et la continuité de production (zéro coupure acceptée).

---

## 📋 PARTIE 1 — CONCEPTION : PLAN D'ADRESSAGE (10 pts)

### Topologie

```
INTERNET (WAN simulé)
      │          │
  Gi0/2       Gi0/2
[R-BDX-A]   [R-BDX-B]      ← HSRP sur le LAN Bordeaux
  Gi0/0       Gi0/0
      └─────────┘
       SW-BDX-CORE
      /      |      \
  VLAN10  VLAN20  VLAN30
  (R&D)  (Admin) (Serveurs)

R-BDX-A Gi0/1 ←──── WAN BDX–MRS ────→ R-MRS Gi0/1
                   (liaison dédiée)

[R-MRS]
  Gi0/0
  SW-MRS
    │
  VLAN50 (Production)
  VLAN60 (Labo)
```

### Bloc SYNTHETIX : `172.18.0.0/19`

**Q1.1 *(4 pts)*** — Calculez le plan d'adressage complet en allouant du plus grand au plus petit. Pour chaque réseau, donnez le préfixe CIDR minimal, l'adresse réseau, le broadcast et la première IP utilisable.

| **Réseau** | **Hôtes requis** | **Préfixe** | **Adresse réseau** | **Broadcast** | **1ère IP** |
|---|---|---|---|---|---|
| VLAN20 Administration | 150 | | | | |
| VLAN10 R&D | 100 | | | | |
| VLAN30 Serveurs | 60 | | | | |
| VLAN50 Production | 60 | | | | |
| VLAN60 Laboratoire | 30 | | | | |
| WAN Bordeaux–Marseille | 2 | | | | |

**Q1.2 *(2 pts)*** — Quelle est l'adresse IP virtuelle HSRP Bordeaux ? (Justifiez votre choix dans la plage VLAN20.)

_________________________________________________________________________

**Q1.3 *(2 pts)*** — Quelle est l'adresse IPv6 GUA de R-BDX-A sur le VLAN20 si le préfixe attribué est `2001:db8:bdx:20::/64` ? (Donner aussi la LLA manuellement configurée : `fe80::1`)

Adresse GUA : _______________________________________________

**Q1.4 *(2 pts)*** — La réglementation pharmaceutique impose de savoir quelle machine avait quelle adresse IP à tout moment. Quel mode d'attribution d'adresses IPv6 doit être utilisé sur le LAN VLAN20 (R&D) ? Justifiez.

_________________________________________________________________________

---

## 📋 PARTIE 2 — ROUTAGE OSPF (8 pts)

### Politique OSPF SYNTHETIX

- Area 0 : liaison WAN BDX–MRS
- Area 1 : tous les réseaux Bordeaux (R-BDX-A et R-BDX-B)
- Area 2 : tous les réseaux Marseille (R-MRS)
- Router-IDs : R-BDX-A = 1.1.1.1, R-BDX-B = 2.2.2.2, R-MRS = 3.3.3.3
- Passive-interface sur toutes les interfaces LAN

**Q2.1 *(3 pts)*** — Rédigez la configuration OSPF complète de **R-BDX-A** (ABR Area 0 + Area 1) :

```ios
R-BDX-A(config)# router ospf 1
R-BDX-A(config-router)# router-id _____________
R-BDX-A(config-router)# network _____________ _____________ area 0   ! WAN
R-BDX-A(config-router)# network _____________ _____________ area 1   ! VLAN20
R-BDX-A(config-router)# network _____________ _____________ area 1   ! VLAN10
R-BDX-A(config-router)# network _____________ _____________ area 1   ! VLAN30
R-BDX-A(config-router)# passive-interface _____________
```

**Q2.2 *(2 pts)*** — Vérification : relevez la sortie attendue de `show ip ospf neighbor` sur R-BDX-A après convergence complète.

```
Neighbor ID  Pri  State     Dead Time  Address   Interface
___________  ___  ________  _________  ________  _________
___________  ___  ________  _________  ________  _________
```

**Q2.3 *(1 pt)*** — Les routes du VLAN50 Marseille apparaissent dans `show ip route` de R-BDX-A avec le marqueur `OI`. Qu'est-ce que cela signifie ?

_________________________________________________________________________

**Q2.4 *(2 pts)*** — Configurez OSPFv3 sur R-BDX-A pour les interfaces WAN et VLAN20 (router-id = 1.1.1.1) :

```ios
ipv6 unicast-routing
ipv6 router ospf 1
  router-id _____________

interface GigabitEthernet0/0   ! VLAN20
  ipv6 ospf 1 area _____________

interface GigabitEthernet0/1   ! WAN
  ipv6 ospf 1 area _____________
```

---

## 📋 PARTIE 3 — HAUTE DISPONIBILITÉ HSRP (10 pts)

### Politique HSRP SYNTHETIX

| **Paramètre** | **R-BDX-A** | **R-BDX-B** |
|---|---|---|
| Rôle souhaité | Active | Standby |
| Groupe HSRP | 1 | 1 |
| IP virtuelle | Dernière IP utilisable VLAN20 | Identique |
| Priorité | 130 | 100 |
| Preempt | Oui | Oui |
| Timers | Hello=1s, Hold=3s | Idem |
| Tracking WAN | Gi0/2 (Internet), décrement 40 | Non |

**Q3.1 *(2 pts)*** — Calculez : si le lien Internet (Gi0/2) de R-BDX-A tombe, la bascule HSRP vers R-BDX-B aura-t-elle lieu ? Montrez le calcul.

```
Priorité R-BDX-A après panne Internet = _____ - _____ = _____
Bascule si _____ < _____ ? : _____  Routeur Active résultant : _____
```

**Q3.2 *(3 pts)*** — Rédigez la configuration HSRP complète sur R-BDX-A :

```ios
interface GigabitEthernet0/0
  standby _____ ip _____________
  standby _____ priority _____
  standby _____ preempt
  standby _____ timers _____ _____
  standby _____ track GigabitEthernet0/2 _____
```

**Q3.3 *(2 pts)*** — Analysez cette sortie `show standby brief` relevée pendant un audit :

```
Interface  Grp  Pri P State   Active        Standby          Virtual IP
Gi0/0      1    130   Active  local         172.18.0.2       172.18.0.254
```

Identifiez **un problème de configuration** et sa conséquence en production.

_________________________________________________________________________
_________________________________________________________________________

**Q3.4 *(1 pt)*** — Un équipement Fortinet doit remplacer R-BDX-B. HSRP est-il encore utilisable ? Quelle alternative standard proposez-vous et quelle différence de vocabulaire y a-t-il pour les rôles ?

_________________________________________________________________________

**Q3.5 *(2 pts)*** — Suite à une bascule HSRP, les PCs du VLAN20 continuent d'envoyer leurs paquets vers le MAC de R-BDX-A (désormais inactif). Quel mécanisme corrige automatiquement ce problème et en combien de temps approximativement (avec les timers actuels) ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📋 PARTIE 4 — SÉCURITÉ VPN ET ACL (14 pts)

### 4.1 — VPN IPsec SYNTHETIX (8 pts)

> Sécuriser le lien WAN BDX–MRS : seul le trafic entre le VLAN30 Serveurs (Bordeaux) et le VLAN50 Production (Marseille) doit être chiffré.

| **Paramètre** | **Valeur** |
|---|---|
| Chiffrement Phase 1 | AES-256 |
| Intégrité Phase 1 | SHA-256 |
| Groupe DH | 14 |
| PSK | `SYNTHETIX-SECURE-2026` |
| Algorithme Phase 2 | ESP-AES-256 + SHA-256 HMAC |
| Mode | Tunnel |

**Q4.1.1 *(1 pt)*** — Écrivez l'ACL crypto de R-BDX-A (trafic VLAN30 ↔ VLAN50 MRS). Utilisez les adresses de votre plan d'adressage Partie 1.

```ios
ip access-list extended CRYPTO_BDX
  permit ip _____________ _____________ _____________ _____________
```

**Q4.1.2 *(1 pt)*** — Écrivez l'ACL crypto de R-MRS (miroir exact).

```ios
ip access-list extended CRYPTO_MRS
  permit ip _____________ _____________ _____________ _____________
```

**Q4.1.3 *(4 pts)*** — Rédigez la configuration VPN IPsec complète (5 étapes) sur R-BDX-A. Le peer est l'IP WAN de R-MRS sur le lien dédié.

```ios
! Étape 2 — Phase 1 :
crypto isakmp policy 10
  _____________________________________________
  _____________________________________________
  _____________________________________________
  _____________________________________________
  _____________________________________________

! Étape 3 — PSK :
crypto isakmp key _____________ address _____________

! Étape 4 — Phase 2 :
crypto ipsec transform-set TS_SYNTHETIX _____________ _____________
  mode _____________

! Étape 5 — Crypto map + application :
crypto map CMAP_SYNTHETIX 10 ipsec-isakmp
  set peer _____________
  set transform-set _____________
  match address _____________

interface GigabitEthernet0/1
  crypto map _____________
```

**Q4.1.4 *(2 pts)*** — Après un ping entre VLAN30 et VLAN50, `show crypto ipsec sa` affiche sur R-BDX-A : `#pkts encaps: 5, #pkts decaps: 0`. Identifiez le problème et proposez une commande de diagnostic.

_________________________________________________________________________
_________________________________________________________________________

### 4.2 — Politique de Filtrage ACL (6 pts)

> La direction SYNTHETIX exige les règles suivantes sur le LAN Bordeaux :
>
> **P1** : Le VLAN10 (R&D, données sensibles) **ne peut pas** accéder en SSH (22) ni en RDP (3389) aux serveurs VLAN30
> **P2** : Le VLAN10 peut accéder en HTTPS (443) au serveur de supervision `172.18.X.Y` (Nagios)
> **P3** : Le VLAN20 (Administration) a accès complet
> **P4** : Tout le reste est autorisé

**Q4.2.1 *(3 pts)*** — Rédigez l'ACL nommée `POLITIQUE_BDX`. Utilisez les adresses de votre plan.

```ios
ip access-list extended POLITIQUE_BDX
  remark P1a - R&D bloquée SSH vers Serveurs
  _____________________________________________
  remark P1b - R&D bloquée RDP vers Serveurs
  _____________________________________________
  remark P2 - R&D accès HTTPS Nagios
  _____________________________________________
  remark P3 - Administration acces complet
  _____________________________________________
  remark P4 - Reste autorisé
  _____________________________________________
```

**Q4.2.2 *(1 pt)*** — Sur quelle interface et dans quelle direction appliquez-vous cette ACL ? Justifiez le choix avec le principe de placement des ACL étendues.

_________________________________________________________________________

**Q4.2.3 *(2 pts)*** — `show ip access-lists POLITIQUE_BDX` relève 0 matches sur la règle P1a après 2h de fonctionnement. Proposez **2 interprétations** : l'une indique que tout va bien, l'autre indique un problème.

Interprétation 1 (normale) : _____________________________________________
Interprétation 2 (problème) : ___________________________________________

---

## 📋 PARTIE 5 — SUPERVISION NAGIOS (10 pts)

> Le serveur Nagios supervise toute l'infrastructure SYNTHETIX depuis un hôte dédié dans le VLAN30.

**Q5.1 *(2 pts)*** — Rédigez la définition complète du host R-BDX-A dans Nagios :

```nagios
define host {
    use                  generic-host
    host_name            _____________
    alias                _____________
    address              _____________
    max_check_attempts   _____________
    check_interval       _____________
    contacts             nagiosadmin
    notification_options d,r,u
}
```

**Q5.2 *(2 pts)*** — Nagios est configuré avec `max_check_attempts=4` et `retry_check_interval=1 min`. R-BDX-A tombe à 14h00. À quelle heure la première alerte est-elle envoyée ? Montrez le calcul complet.

```
normal_check_interval = 5 min

14h00 + ___min → Soft 1/4
       + ___min → Soft 2/4
       + ___min → Soft 3/4
       + ___min → HARD → ALERTE ✅
Heure : _______   Délai : _____ min
```

**Q5.3 *(2 pts)*** — Le plugin de supervision du capteur de température de la salle serveur retourne :

```bash
$ /usr/lib/nagios/plugins/check_temp -H 172.18.1.50 -w 28 -c 35
TEMPERATURE CRITICAL - 37.2°C | temp=37.2;28;35;0;50
$ echo $?
2
```

**a)** Quel état Nagios affiche-t-il ?

_________

**b)** Décomposez le champ de perf data `temp=37.2;28;35;0;50` :

| **Champ** | **Valeur** | **Rôle** |
|---|---|---|
| Valeur mesurée | | |
| Seuil WARNING | | |
| Seuil CRITICAL | | |
| Minimum | | |
| Maximum | | |

**Q5.4 *(2 pts)*** — L'admin souhaite superviser l'état HSRP de R-BDX-A (vérifier qu'il est bien Active) plutôt que juste son ping. Expliquez en 3 étapes comment concevoir ce check custom dans Nagios.

1. _______________________________________________________________________
2. _______________________________________________________________________
3. _______________________________________________________________________

**Q5.5 *(2 pts)*** — `[INTÉGRATION]` Nagios est en état OK sur R-BDX-A. Pourtant, R-BDX-A a basculé en Standby HSRP suite à une panne WAN (tracking déclenché). Les utilisateurs se plaignent. Expliquez pourquoi Nagios peut afficher OK alors que l'infrastructure est dégradée, et quelle amélioration de la supervision corriger ce point aveugle.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

## 📋 PARTIE 6 — ANALYSE ET TROUBLESHOOTING (8 pts)

**Q6.1 *(2 pts)*** — Analysez cette sortie :

```
R-BDX-A# show crypto isakmp sa
(aucun résultat)

R-BDX-A# ping 172.18.WAN.2   (IP WAN R-MRS)
!!!!!   → success
```

Que pouvez-vous déduire ? Citez **3 causes possibles** pour l'absence d'IKE SA.

1. _______________________________________________________________________
2. _______________________________________________________________________
3. _______________________________________________________________________

**Q6.2 *(2 pts)*** — `show ip ospf neighbor` sur R-BDX-A ne montre que R-BDX-B (sur le LAN) mais pas R-MRS (sur le WAN). La connectivité IP WAN est confirmée. Citez 2 causes OSPF possibles.

1. _______________________________________________________________________
2. _______________________________________________________________________

**Q6.3 *(2 pts)*** — Un administrateur réalise un `no shutdown` sur le port Gi0/3 d'un switch déjà doté de redondance STP. Immédiatement après, le réseau VLAN20 subit une tempête de broadcast. Expliquez le lien avec STP.

_________________________________________________________________________
_________________________________________________________________________

**Q6.4 *(2 pts)*** — Dans `show ipv6 ospf neighbor`, un voisin affiche `FULL/ -` (tiret). Qu'est-ce que le tiret signifie dans ce contexte OSPFv3 ? Quel type de lien cela présuppose-t-il ?

_________________________________________________________________________

---

## 📊 BARÈME RÉCAPITULATIF

| **Partie** | **Compétence** | **Points** |
|---|---|---|
| 1 — Plan d'adressage | VLSM, IPv6, choix DHCPv6 | /10 |
| 2 — OSPF | Multi-area, OSPFv3 | /8 |
| 3 — HSRP | Calcul, config, analyse, VRRP | /10 |
| 4.1 — VPN IPsec | 5 étapes, ACL miroir, diagnostic | /8 |
| 4.2 — ACL | Politique, placement, interprétation | /6 |
| 5 — Nagios | Host, timing, plugin, intégration | /10 |
| 6 — Troubleshooting | Diagnostic, STP, OSPFv3 | /8 |
| **TOTAL** | | **/60** |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026 — ÉPREUVE BLANCHE CONFIDENTIELLE**
