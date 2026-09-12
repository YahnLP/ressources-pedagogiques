# 🔬 LAB PACKET TRACER — S11 ANNÉE 3 – E31
## Infrastructure Multi-Sites Complète : OSPF, HSRP, VPN, ACL, Nagios, IPv6

**Nom : ________________  Prénom : ________________  Date : ________________**

> **⏱️ Durée : 2h15 — Conditions d'évaluation**
> *Documents autorisés : fiche cours E31 A2/A3. Pas de correction entre les parties.*

---

## 🏢 CONTEXTE PROFESSIONNEL

> **NEXIA** est une société de services numériques avec deux sites :
> - **Site Paris (siège)** : direction, administration, serveurs
> - **Site Lyon (antenne)** : équipes techniques
>
> Vous êtes en charge du déploiement complet de l'infrastructure réseau NEXIA. Ce lab reproduit les compétences attendues lors de votre soutenance finale.

---

## 📋 TOPOLOGIE

```
                    INTERNET (WAN simulé)
                   /                      \
              Gi0/2                       Gi0/2
         [R-PARIS-A]    [R-PARIS-B]    [R-LYON]
          (HSRP Active) (HSRP Standby)
              Gi0/0          Gi0/0         Gi0/0
                  \          /               |
               [SW-PARIS-CORE]          [SW-LYON]
              /       |       \               |
          Gi0/1     Gi0/1    Gi0/1          Gi0/1
        [VLAN10]  [VLAN20]  [SRV-NAGIOS]   [VLAN50]
      (Direction) (Technique)  (Supervision) (Technique Lyon)

WAN Paris–Lyon : R-PARIS-A Gi0/1 ↔ R-LYON Gi0/1 (10.0.12.0/30)
WAN Internet A : R-PARIS-A Gi0/2 (203.0.113.1/30)
WAN Internet B : R-PARIS-B Gi0/2 (203.0.113.5/30)
WAN Internet L : R-LYON    Gi0/2 (203.0.113.9/30)
```

---

## 📋 PARTIE 1 — PLAN D'ADRESSAGE VLSM (20 min)

### Bloc alloué à NEXIA : `10.100.0.0/20`

**Découpez ce bloc pour les réseaux suivants (du plus grand au plus petit) :**

| **Réseau** | **Hôtes req.** | **Préfixe** | **Adresse réseau** | **Broadcast** | **1ère IP** |
|---|---|---|---|---|---|
| VLAN20 Paris Technique | 100 | | | | |
| VLAN10 Paris Direction | 50 | | | | |
| VLAN50 Lyon Technique | 50 | | | | |
| Management Nagios | 20 | | | | |
| WAN Paris–Lyon | 2 | | | | |

**Q1.** Combien d'adresses reste-t-il disponibles dans le bloc `/20` après ces allocations ?

_________________________________________________________________________

---

## 📋 PARTIE 2 — CONFIGURATION DE BASE (15 min)

> Configurez les interfaces de tous les routeurs avec les adresses de votre plan. Validez la connectivité WAN avant de passer à la suite.

**Checklist avant de continuer :**

```
R-PARIS-A# ping 10.0.12.2          → _______  (R-LYON WAN)
R-PARIS-A# ping 203.0.113.2        → _______  (Internet simulé)
R-PARIS-B# ping 203.0.113.6        → _______  (Internet simulé)
```

---

## 📋 PARTIE 3 — ROUTAGE OSPF (20 min)

### Politique OSPF NEXIA

- **Area 0** : liaisons WAN (tous les routeurs)
- **Area 1** : LAN Paris (R-PARIS-A et R-PARIS-B)
- Passive-interface sur toutes les interfaces LAN (côté switches)
- Router-IDs : R-PARIS-A=1.1.1.1, R-PARIS-B=2.2.2.2, R-LYON=3.3.3.3

### 3.1 — Configuration OSPF

**Sur R-PARIS-A (ABR Area 0 + Area 1) :**

```ios
R-PARIS-A(config)# router ospf 1
R-PARIS-A(config-router)# router-id _____________
R-PARIS-A(config-router)# network _____________ _____________ area 0   ! WAN Lyon
R-PARIS-A(config-router)# network _____________ _____________ area 1   ! LAN Paris
R-PARIS-A(config-router)# passive-interface _____________
```

**Sur R-PARIS-B :**

```ios
! [Compléter — router-id 2.2.2.2, LAN Paris en area 1]
```

**Sur R-LYON :**

```ios
! [Compléter — router-id 3.3.3.3, WAN en area 0, LAN Lyon en area 0]
```

### 3.2 — Vérification OSPF

```ios
R-PARIS-A# show ip ospf neighbor
```

**Q2.** Relevez l'état et les router-id des voisins de R-PARIS-A :

| **Neighbor ID** | **State** | **Interface** |
|---|---|---|
| | | |
| | | |

**Q3.** Depuis PC-PARIS-TECH (VLAN20), pouvez-vous pinger PC-LYON-TECH (VLAN50) ?

```
PC-PARIS-TECH# ping [IP_PC_LYON]   → _______
```

---

## 📋 PARTIE 4 — HSRP HAUTE DISPONIBILITÉ (20 min)

### Politique HSRP NEXIA

| **Paramètre** | **R-PARIS-A (Active)** | **R-PARIS-B (Standby)** |
|---|---|---|
| Groupe | 1 | 1 |
| IP virtuelle | `[1ère adresse dispo /]` | Même |
| Priorité | 120 | 100 |
| Preempt | ✅ | ✅ |
| Timers | Hello=1s, Hold=3s | Idem |
| Tracking | Gi0/2 (Internet), décrement=30 | — |

> L'IP virtuelle sera la passerelle de tous les PCs Paris.

**Q4.** Calculez : si R-PARIS-A WAN (Gi0/2) tombe, la bascule aura-t-elle lieu ?

```
Priorité R-PARIS-A après tracking = _____ - _____ = _____
Bascule si _____ < _____ ? : OUI / NON
```

### 4.1 — Configuration HSRP

```ios
R-PARIS-A(config)# interface GigabitEthernet0/0
R-PARIS-A(config-if)# standby _____ ip _____________
R-PARIS-A(config-if)# standby _____ priority _____
R-PARIS-A(config-if)# standby _____ preempt
R-PARIS-A(config-if)# standby _____ timers _____ _____
R-PARIS-A(config-if)# standby _____ track GigabitEthernet0/2 _____
```

### 4.2 — Vérification HSRP

```ios
R-PARIS-A# show standby brief
```

**Q5.** Recopiez la sortie et confirmez : R-PARIS-A est-il bien Active ?

```
Interface  Grp  Pri P State  Active   Standby   Virtual IP
_________  ___  ___ _ _____  ______   ________  ___________
```

---

## 📋 PARTIE 5 — VPN IPSEC PARIS–LYON (25 min)

### Politique VPN NEXIA

| **Paramètre** | **Valeur** |
|---|---|
| Phase 1 chiffrement | AES-256 |
| Phase 1 intégrité | SHA-256 |
| Groupe DH | 14 |
| Lifetime Phase 1 | 86400 s |
| PSK | `NEXIA-CIEL-2026` |
| Phase 2 | ESP-AES-256, HMAC-SHA256, mode tunnel |
| Trafic protégé | VLAN Paris ↔ VLAN50 Lyon |

### 5.1 — Configuration sur R-PARIS-A

> **Rappel :** les 5 étapes IPsec (ACL crypto, isakmp policy, PSK, transform-set, crypto map + interface)

```ios
! Étape 1 — ACL crypto
ip access-list extended CRYPTO_PARIS
  permit ip _____________ _____________ _____________ _____________

! Étape 2 — Phase 1
crypto isakmp policy 10
  encryption aes 256
  hash sha256
  authentication pre-share
  group 14
  lifetime 86400

! Étape 3 — PSK (peer = IP WAN de R-LYON)
crypto isakmp key _____________ address _____________

! Étape 4 — Phase 2
crypto ipsec transform-set TS_VPN esp-aes 256 esp-sha256-hmac
  mode tunnel

! Étape 5 — Crypto map + application
crypto map CMAP_VPN 10 ipsec-isakmp
  set peer _____________
  set transform-set TS_VPN
  match address CRYPTO_PARIS

interface GigabitEthernet0/1  ! Interface WAN Paris–Lyon
  crypto map CMAP_VPN
```

### 5.2 — Configuration sur R-LYON (miroir)

> **Rappel :** l'ACL crypto de R-LYON est le **miroir** de celle de R-PARIS-A.

```ios
! [Compléter les 5 étapes — même PSK, ACL miroir, peer = IP WAN R-PARIS-A]
```

### 5.3 — Vérification VPN

```ios
! Déclencher le trafic VPN (pinger depuis VLAN Paris vers VLAN50 Lyon)
PC-PARIS-TECH# ping [IP_PC_LYON]

R-PARIS-A# show crypto isakmp sa
```

**Q6.** Quel état attendez-vous dans `show crypto isakmp sa` ? ___________

```ios
R-PARIS-A# show crypto ipsec sa
```

**Q7.** Après un ping, les compteurs `#pkts encaps` et `#pkts decrypt` sont-ils > 0 ?

```
#pkts encaps : _____
#pkts decrypt : _____
```

---

## 📋 PARTIE 6 — POLITIQUE DE SÉCURITÉ ACL (15 min)

### Politique de filtrage NEXIA

| **Règle** | **Description** |
|---|---|
| **P1** | VLAN10 Direction ne peut PAS accéder en SSH aux équipements VLAN20 Technique |
| **P2** | VLAN10 Direction peut accéder au serveur Nagios (HTTP port 80) |
| **P3** | VLAN20 Technique a accès complet |
| **P4** | Le reste du trafic est autorisé |

### 6.1 — Rédiger et appliquer l'ACL

```ios
ip access-list extended POLITIQUE_PARIS
  remark P1 - Direction bloquée SSH vers Technique
  _____________________________________________
  remark P2 - Direction accès Nagios HTTP
  _____________________________________________
  remark P3 - Technique acces complet
  _____________________________________________
  remark P4 - Reste autorisé
  _____________________________________________

! Appliquer sur l'interface appropriée :
interface _____________
  ip access-group POLITIQUE_PARIS _____
```

**Q8.** Sur quelle interface et dans quelle direction placez-vous cette ACL ? Justifiez.

_________________________________________________________________________

---

## 📋 PARTIE 7 — SUPERVISION NAGIOS (20 min)

> Le serveur SRV-NAGIOS (dans le Management réseau) est déjà installé avec Nagios Core.

### 7.1 — Configurer deux hosts dans Nagios

**Créer `/etc/nagios/conf.d/nexia.cfg` :**

```nagios
! Host 1 — R-PARIS-A
define host {
    use                  generic-host
    host_name            R-PARIS-A
    alias                Routeur Principal Paris
    address              _____________    ! IP réelle Gi0/0 de R-PARIS-A
    max_check_attempts   3
    check_interval       5
    contacts             nagiosadmin
    notification_options d,r
}

! Host 2 — R-LYON
define host {
    use                  generic-host
    host_name            R-LYON
    alias                Routeur Lyon
    address              _____________
    max_check_attempts   3
    check_interval       5
    contacts             nagiosadmin
    notification_options d,r
}

! Service HTTP sur R-PARIS-A (si HTTP configuré)
define service {
    use                  generic-service
    host_name            R-PARIS-A
    service_description  Disponibilite ping
    check_command        check_ping!100,20%!500,60%
    check_interval       5
    contacts             nagiosadmin
}
```

### 7.2 — Valider et recharger

```bash
sudo nagios -v /etc/nagios/nagios.cfg
sudo systemctl reload nagios
```

**Q9.** Quel état devrait afficher R-PARIS-A dans le dashboard Nagios si tout est correct ?

_________________________________________________________________________

**Q10.** Testez un plugin manuellement :

```bash
/usr/lib/nagios/plugins/check_ping -H [IP_R-PARIS-A] -w 100,20% -c 500,60%
```

Résultat : ___________________________________________ Code retour (`echo $?`) : ___

---

## 📋 PARTIE 8 — IPv6 ET OSPFV3 (15 min)

> Ajoutez une couche IPv6 sur le VLAN20 Paris et le VLAN50 Lyon.

### Plan d'adressage IPv6

| **Réseau** | **Préfixe** | **IP routeur** |
|---|---|---|
| VLAN20 Paris (IPv6) | `2001:db8:paris:20::/64` | R-PARIS-A : `::1/64` |
| VLAN50 Lyon (IPv6) | `2001:db8:lyon:50::/64` | R-LYON : `::1/64` |
| WAN Paris–Lyon (IPv6) | `2001:db8:wan:12::/64` | R-PARIS-A: `::1`, R-LYON: `::2` |

### 8.1 — Configurer IPv6 + SLAAC sur VLAN20

```ios
R-PARIS-A(config)# ipv6 unicast-routing

R-PARIS-A(config)# interface GigabitEthernet0/0
R-PARIS-A(config-if)# ipv6 address _____________
R-PARIS-A(config-if)# ipv6 nd ra-interval 10
```

**Q11.** Quelle adresse IPv6 obtiendra automatiquement un PC du VLAN20 ? (Expliquez le mécanisme SLAAC)

_________________________________________________________________________

### 8.2 — Configurer OSPFv3

```ios
R-PARIS-A(config)# ipv6 router ospf 1
R-PARIS-A(config-rtr)# router-id _____________    ! router-id IPv4 obligatoire

! Sur les interfaces à inclure dans OSPFv3 :
interface GigabitEthernet0/0
  ipv6 ospf 1 area 0

interface GigabitEthernet0/1  ! WAN vers Lyon
  ipv6 ospf 1 area 0
```

**Sur R-LYON :** [même logique — router-id 3.3.3.3]

### 8.3 — Vérification OSPFv3

```ios
R-PARIS-A# show ipv6 ospf neighbor
```

**Q12.** Quelle adresse utilise OSPFv3 comme source des messages hello ? (Type d'adresse)

_________________________________________________________________________

---

## 📋 PARTIE 9 — TROUBLESHOOTING (30 min)

> Le formateur a injecté une panne dans votre topologie pendant la pause. Vous avez 30 minutes pour la trouver et la corriger.

### Méthode obligatoire

```
STEP 1 — Testez la connectivité
  ping, traceroute, show ip route

STEP 2 — Identifiez la couche du problème
  show ip ospf neighbor / show standby / show crypto isakmp sa / show ip access-lists

STEP 3 — Diagnostiquez le composant fautif
  show run | section [protocole_suspect]

STEP 4 — Corrigez et vérifiez
```

### Rapport de troubleshooting

**Symptôme observé :**

_________________________________________________________________________

**Commandes de diagnostic utilisées :**

1. _______________________________________________________________________
2. _______________________________________________________________________
3. _______________________________________________________________________

**Hypothèse formulée :**

_________________________________________________________________________

**Correction apportée :**

```ios
_____________________________________________
_____________________________________________
```

**Vérification :**

_________________________________________________________________________

**Conclusion :** ☐ Panne corrigée ☐ Partiellement corrigée ☐ Non résolue

---

## 📊 BARÈME DU LAB

| **Partie** | **Compétence** | **Points** |
|---|---|---|
| 1 – VLSM | Plan d'adressage cohérent | /3 |
| 3 – OSPF | 3 routeurs adjacents, routes distribuées | /3 |
| 4 – HSRP | Active/Standby, preempt, tracking, Q4 | /3 |
| 5 – VPN IPsec | Phase 1+2, trafic chiffré, Q6+Q7 | /3 |
| 6 – ACL | Politique correcte, placement, Q8 | /2 |
| 7 – Nagios | Hosts + service configurés, Q9+Q10 | /2 |
| 8 – IPv6 | OSPFv3, SLAAC, Q11+Q12 | /2 |
| 9 – Troubleshooting | Méthode + résultat | /2 |
| **TOTAL** | | **/20** |

**Seuil de validation : 10/20**

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
