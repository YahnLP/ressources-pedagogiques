# 🔬 TP PACKET TRACER – S5 ANNÉE 2 – E31
## ACL Étendues : Filtrage Port & Protocole, Placement, Vérification

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Traduire une politique de sécurité en ACL étendues IOS
- ✅ Placer les ACL sur la bonne interface dans la bonne direction
- ✅ Vérifier avec `show ip access-lists` et `show ip interface`
- ✅ Diagnostiquer et corriger une ACL mal configurée

---

## ⏱️ DURÉE : 70 min

---

## 📋 TOPOLOGIE

```
           INTERNET (203.0.113.0/30)
                  │
           ┌──────┴──────┐
           │   R-EDGE    │ 203.0.113.2
           └──┬──────┬───┘
              │      │
         Gi0/1│      │Gi0/2
    10.0.12.1 │      │ 10.0.13.1
              │      │
    ┌──────────┴─┐  ┌─┴──────────┐
    │  R-LAN     │  │  R-DMZ     │
    │ 10.0.12.2  │  │ 10.0.13.2  │
    └────┬───────┘  └──────┬─────┘
    Gi0/0│              Gi0/0│
192.168.1.1/24        10.0.1.1/24
         │                  │
    ┌────┴────┐         ┌───┴────────────────┐
    │ LAN-Users│        │      DMZ           │
    │/24       │        │                    │
    │          │      [SRV-HTTP:10.0.1.10]  [SRV-SSH:10.0.1.20]
   PC1:192.168.1.10    HTTP+HTTPS          SSH admin
   PC2:192.168.1.20    port 80/443         port 22

    ┌────┴────┐
    │LAN-Admin│
    │         │
  ADMIN:192.168.1.100
```

---

## 📋 PLAN D'ADRESSAGE

| **Équipement** | **Interface** | **IP** | **Masque** |
|---|---|---|---|
| R-EDGE | Gi0/0 (WAN) | 203.0.113.2 | /30 |
| R-EDGE | Gi0/1 (→R-LAN) | 10.0.12.1 | /30 |
| R-EDGE | Gi0/2 (→R-DMZ) | 10.0.13.1 | /30 |
| R-LAN | Gi0/0 (LAN) | 192.168.1.1 | /24 |
| R-LAN | Gi0/1 (→R-EDGE) | 10.0.12.2 | /30 |
| R-DMZ | Gi0/0 (DMZ) | 10.0.1.1 | /24 |
| R-DMZ | Gi0/1 (→R-EDGE) | 10.0.13.2 | /30 |
| PC1 | — | 192.168.1.10 | /24, GW 192.168.1.1 |
| PC2 | — | 192.168.1.20 | /24, GW 192.168.1.1 |
| ADMIN | — | 192.168.1.100 | /24, GW 192.168.1.1 |
| SRV-HTTP | — | 10.0.1.10 | /24, GW 10.0.1.1 |
| SRV-SSH | — | 10.0.1.20 | /24, GW 10.0.1.1 |

> Le routage OSPF area 0 est déjà configuré sur la topologie. Vous n'avez qu'à implémenter les ACL.

---

## 📋 POLITIQUE DE SÉCURITÉ À IMPLÉMENTER

| **Règle** | **Description** |
|---|---|
| **P1** | PC1 et PC2 peuvent accéder au SRV-HTTP en HTTP (port 80) uniquement |
| **P2** | PC1 et PC2 ne peuvent PAS accéder au SRV-SSH |
| **P3** | ADMIN peut accéder à TOUS les services de la DMZ (HTTP, HTTPS, SSH) |
| **P4** | Personne depuis Internet ne peut pinger les machines internes (bloquer ICMP echo) |
| **P5** | Le reste du trafic interne est autorisé normalement |

---

## 🧪 PARTIE 1 – Analyse et préparation (10 min)

### 1.1 – Vérification de la connectivité initiale (SANS ACL)

```
PC1# ping 10.0.1.10    → _______
PC1# ping 10.0.1.20    → _______
ADMIN# ping 10.0.1.20  → _______
```

---

### 1.2 – Traduction de la politique

> Pour chaque règle, identifiez les 4 critères et rédigez la règle ACL avant de la saisir.

**Règle P1 — PC1/PC2 → SRV-HTTP, port 80 seulement :**

```
Source     : __________________ wildcard : __________________
Destination: __________________ wildcard : __________________
Protocole  : __________________
Port       : __________________
Règle ACL  : permit _____ ________________ ________________ _____ _____
```

**Règle P2 — Bloquer PC1/PC2 → SRV-SSH :**

```
Source     : __________________
Destination: __________________
Protocole  : __________________
Port       : __________________
Règle ACL  : deny _____ ________________ ________________ _____ _____
```

**Règle P3 — ADMIN → DMZ tout autorisé :**

```
Règle ACL  : permit _____ ________________ __________________
```

**Règle P4 — Bloquer ICMP depuis Internet :**

```
Source     : __________________ (tous)
Destination: __________________ (réseau interne)
Protocole  : __________________
Type ICMP  : __________________ (requête ping)
Règle ACL  : deny _____ _____ ________________ __________________
```

---

## 🔬 PARTIE 2 – Configuration des ACL (25 min)

### 2.1 – ACL sur R-LAN (politique P1, P2, P3, P5)

> Cette ACL filtre le trafic **sortant du LAN** vers la DMZ. Elle sera placée sur l'interface Gi0/0 de R-LAN, direction **in**.

**Rédiger l'ACL nommée POLITIQUE_LAN :**

```ios
R-LAN(config)# ip access-list extended POLITIQUE_LAN
R-LAN(config-ext-nacl)# remark === Admin : acces complet DMZ ===
R-LAN(config-ext-nacl)# _________________________________________
R-LAN(config-ext-nacl)# remark === PC1/PC2 : HTTP seulement vers SRV-HTTP ===
R-LAN(config-ext-nacl)# _________________________________________
R-LAN(config-ext-nacl)# remark === Bloquer PC1/PC2 vers SRV-SSH ===
R-LAN(config-ext-nacl)# _________________________________________
R-LAN(config-ext-nacl)# remark === Autoriser le reste ===
R-LAN(config-ext-nacl)# _________________________________________
```

**Appliquer sur R-LAN :**

```ios
R-LAN(config)# interface GigabitEthernet0/0
R-LAN(config-if)# ip access-group POLITIQUE_LAN _____
```

*Direction choisie : _______ Justification : _______________________________*

---

### 2.2 – ACL sur R-EDGE (politique P4)

> Cette ACL filtre le trafic **provenant d'Internet** avant qu'il n'entre dans le réseau. Elle sera placée sur l'interface Gi0/0 (WAN) de R-EDGE.

```ios
R-EDGE(config)# ip access-list extended ANTI_PING_INTERNET
R-EDGE(config-ext-nacl)# remark === Bloquer ping depuis Internet ===
R-EDGE(config-ext-nacl)# _________________________________________
R-EDGE(config-ext-nacl)# remark === Autoriser le reste ===
R-EDGE(config-ext-nacl)# _________________________________________
```

**Appliquer sur R-EDGE :**

```ios
R-EDGE(config)# interface GigabitEthernet0/0
R-EDGE(config-if)# ip access-group ANTI_PING_INTERNET _____
```

---

## ✅ PARTIE 3 – Vérification des ACL (15 min)

### 3.1 – Afficher les ACL configurées

```ios
R-LAN# show ip access-lists
```

**Relevez la sortie :**

```
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
```

**Q1.** Combien de règles contient POLITIQUE_LAN ? ___________

**Q2.** Les compteurs de matches sont-ils tous à 0 ? Pourquoi ? ___________

---

### 3.2 – Générer du trafic et observer les hits

**Depuis PC1 :**

```
PC1# ping 10.0.1.10     → _______  (HTTP = doit passer)
PC1# ping 10.0.1.20     → _______  (SSH = doit être bloqué)
```

> *Note Packet Tracer : Pour simuler du trafic HTTP, utiliser le navigateur web intégré vers http://10.0.1.10. Pour SSH, utiliser la commande `ssh -l admin 10.0.1.20`.*

**Depuis ADMIN :**

```
ADMIN# ping 10.0.1.20   → _______  (doit passer)
```

---

### 3.3 – Re-afficher les ACL après trafic

```ios
R-LAN# show ip access-lists POLITIQUE_LAN
```

**Relevez les nouveaux compteurs :**

| **Règle** | **Matches avant trafic** | **Matches après trafic** |
|---|---|---|
| permit ip ADMIN any | 0 | |
| permit tcp LAN host SRV-HTTP eq 80 | 0 | |
| deny tcp LAN host SRV-SSH eq 22 | 0 | |
| permit ip any any | 0 | |

**Q3.** Quelle règle a le plus de matches ? Est-ce normal ?

_________________________________________________________________________

**Q4.** La règle `deny tcp LAN host SRV-SSH eq 22` a-t-elle des matches ? Que cela confirme-t-il ?

_________________________________________________________________________

---

### 3.4 – Vérifier le placement de l'ACL

```ios
R-LAN# show ip interface GigabitEthernet0/0
```

**Relevez :**

- Inbound access list : ___________
- Outbound access list : ___________

**Q5.** L'ACL est-elle appliquée dans la bonne direction ? Justifiez.

_________________________________________________________________________

---

## 🛠️ PARTIE 4 – Débogage (10 min)

### Mise en situation

> Le formateur a injecté une erreur dans la configuration. PC1 n'arrive pas à joindre SRV-HTTP alors que la règle semble correcte.

**Configuration incorrecte injectée (à identifier) :**

```ios
! Configuration POLITIQUE_LAN sur R-LAN avec une erreur :
ip access-list extended POLITIQUE_LAN
  permit ip  192.168.1.100 0.0.0.0  any
  permit tcp 192.168.1.0 0.0.0.255  host 10.0.1.10  eq 80
  deny   tcp 192.168.1.0 0.0.0.255  host 10.0.1.20  eq 22
  permit ip  any  any
```

**L'ACL est appliquée sur :**

```ios
interface GigabitEthernet0/1
  ip access-group POLITIQUE_LAN in
```

---

**Q6.** Identifiez l'erreur de placement. Pourquoi PC1 ne peut pas joindre SRV-HTTP ?

_________________________________________________________________________
_________________________________________________________________________

**Q7.** Sur quelle interface et dans quelle direction faut-il appliquer l'ACL ?

```ios
R-LAN(config)# interface _____________________
R-LAN(config-if)# ip access-group POLITIQUE_LAN _____
```

**Q8.** Une fois le placement corrigé, PC1 peut-il maintenant joindre SRV-HTTP ? Testez et notez le résultat.

_________________________________________________________________________

---

## 📊 PARTIE 5 – Questions d'analyse (10 min)

**Q9.** Pourquoi a-t-on placé l'ACL POLITIQUE_LAN sur R-LAN et non sur R-DMZ ou R-EDGE ?

_________________________________________________________________________
_________________________________________________________________________

**Q10.** Si on avait utilisé une ACL numérotée (`access-list 110`) au lieu d'une ACL nommée, quel problème aurait-on eu si on avait voulu insérer une règle entre `deny tcp ... eq 22` et `permit ip any any` ?

_________________________________________________________________________
_________________________________________________________________________

**Q11.** Après avoir généré du trafic ICMP depuis "Internet" (depuis R-EDGE) :

```ios
R-EDGE# show ip access-lists ANTI_PING_INTERNET
```

La règle `deny icmp` a-t-elle des matches ? Justifiez à quoi cela sert de vérifier ça.

_________________________________________________________________________
_________________________________________________________________________

**Q12.** Un collègue vous dit : *"J'ai mis `deny tcp any any eq 22` sur R-EDGE pour bloquer SSH depuis Internet, mais ça bloque aussi les SSH de l'Admin !"* Expliquez pourquoi et proposez une solution.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 | Ping initial + tableau de traduction P1–P5 | /3 |
| Partie 2 – POLITIQUE_LAN | ACL rédigée correctement (4 règles) + application | /6 |
| Partie 2 – ANTI_PING | ACL rédigée + application direction correcte | /3 |
| Partie 3 – show ip access-lists | Relevés + Q1–Q4 | /4 |
| Partie 3 – show ip interface | Vérification placement + Q5 | /1 |
| Partie 4 – Débogage | Identification erreur + correction + Q6–Q8 | /3 |
| Partie 5 – Analyse | Q9–Q12 | /4 |
| Présentation / soin | Clarté des réponses, commandes propres | /1 |
| **TOTAL** | | **/25** |

> *Ramené à /20 : score × 0,8*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
