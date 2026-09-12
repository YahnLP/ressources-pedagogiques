# 🔬 TP PACKET TRACER – S7 ANNÉE 2 – E31
## VPN IPsec Site-à-Site : Configuration, Vérification, Débogage

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Configurer un VPN IPsec site-à-site complet en 5 étapes sur deux routeurs Cisco IOS
- ✅ Vérifier Phase 1 avec `show crypto isakmp sa` et Phase 2 avec `show crypto ipsec sa`
- ✅ Générer du trafic intéressant et observer les compteurs encrypt/decrypt
- ✅ Diagnostiquer et corriger une configuration VPN défaillante

---

## ⏱️ DURÉE : 70 min

---

## 📋 TOPOLOGIE

```
     LAN-PARIS                                    LAN-LYON
  192.168.10.0/24                             192.168.20.0/24
        │                                            │
    Gi0/0                                        Gi0/0
  ┌─────────────┐   Gi0/1       Gi0/1    ┌─────────────┐
  │  R-PARIS    │──203.0.113.1 ─────── 203.0.113.2──│   R-LYON    │
  │  (site A)   │   WAN (lien simulé Internet)   │  (site B)   │
  └─────────────┘                                └─────────────┘

PC-PARIS : 192.168.10.10/24  GW: 192.168.10.1
PC-LYON  : 192.168.20.10/24  GW: 192.168.20.1
```

---

## 📋 PLAN D'ADRESSAGE

| **Équipement** | **Interface** | **IP** | **Masque** | **Rôle** |
|---|---|---|---|---|
| R-PARIS | Gi0/0 | 192.168.10.1 | /24 | Passerelle LAN-PARIS |
| R-PARIS | Gi0/1 | 203.0.113.1 | /30 | WAN (vers Internet) |
| R-LYON | Gi0/0 | 192.168.20.1 | /24 | Passerelle LAN-LYON |
| R-LYON | Gi0/1 | 203.0.113.2 | /30 | WAN (vers Internet) |
| PC-PARIS | — | 192.168.10.10 | /24 | GW 192.168.10.1 |
| PC-LYON | — | 192.168.20.10 | /24 | GW 192.168.20.1 |

> **Prérequis :** Les adresses IP des interfaces et le routage IP de base (route statique ou OSPF entre WAN) sont déjà configurés. Vérifiez avant de commencer avec `ping 203.0.113.2` depuis R-PARIS.

---

## 📋 POLITIQUE VPN À IMPLÉMENTER

| **Paramètre Phase 1** | **Valeur** |
|---|---|
| Chiffrement | AES 256 |
| Intégrité | SHA-256 |
| Authentification | Pre-shared key |
| Groupe DH | 14 |
| Lifetime | 86400 s |
| PSK | `VPN-CIEL-2026` |

| **Paramètre Phase 2** | **Valeur** |
|---|---|
| Protocole | ESP |
| Chiffrement | AES 256 |
| Intégrité | HMAC-SHA-256 |
| Mode | Tunnel |
| Lifetime | 3600 s |

---

## 🧪 PARTIE 1 – Vérification préliminaire (5 min)

### 1.1 – Connectivité WAN (avant VPN)

```
R-PARIS# ping 203.0.113.2     → _______
```

### 1.2 – Connectivité LAN → LAN (avant VPN, en clair)

```
PC-PARIS# ping 192.168.20.10  → _______
```

**Q1.** Le ping PC-PARIS → PC-LYON fonctionne-t-il avant le VPN ? Pourquoi ?

_________________________________________________________________________

---

## 🔬 PARTIE 2 – Configuration VPN IPsec (30 min)

### 2.1 – ÉTAPE 1 : ACL Crypto

**Sur R-PARIS :**

```ios
R-PARIS(config)# ip access-list extended CRYPTO_PARIS
R-PARIS(config-ext-nacl)# permit ip _____________ _____________ _____________ _____________
```

*Compléter : source = LAN-PARIS, destination = LAN-LYON*

**Sur R-LYON :**

```ios
R-LYON(config)# ip access-list extended CRYPTO_LYON
R-LYON(config-ext-nacl)# permit ip _____________ _____________ _____________ _____________
```

*Rappel : l'ACL de R-LYON est le MIROIR de celle de R-PARIS.*

---

### 2.2 – ÉTAPE 2 : Phase 1 — Politique ISAKMP

**Sur R-PARIS (et identique sur R-LYON) :**

```ios
R-PARIS(config)# crypto isakmp policy 10
R-PARIS(config-isakmp)# encryption _______ _______
R-PARIS(config-isakmp)# hash _______
R-PARIS(config-isakmp)# authentication _______
R-PARIS(config-isakmp)# group _______
R-PARIS(config-isakmp)# lifetime _______

R-PARIS(config)# crypto isakmp key _____________ address _____________
```

*PSK : `VPN-CIEL-2026` | Peer R-PARIS → adresse WAN de R-LYON*

**Sur R-LYON :**

```ios
R-LYON(config)# crypto isakmp policy 10
! [commandes identiques à R-PARIS]

R-LYON(config)# crypto isakmp key _____________ address _____________
```

*Peer R-LYON → adresse WAN de R-PARIS*

---

### 2.3 – ÉTAPE 3 : Phase 2 — Transform-Set

**Sur R-PARIS ET R-LYON (identique) :**

```ios
R-PARIS(config)# crypto ipsec transform-set TS_VPN _______ _______ _______
R-PARIS(cfg-crypto-trans)# mode _______
```

---

### 2.4 – ÉTAPE 4 : Crypto Map

**Sur R-PARIS :**

```ios
R-PARIS(config)# crypto map CMAP 10 ipsec-isakmp
R-PARIS(config-crypto-map)# set peer _____________
R-PARIS(config-crypto-map)# set transform-set _____________
R-PARIS(config-crypto-map)# match address _____________
```

**Sur R-LYON :**

```ios
R-LYON(config)# crypto map CMAP 10 ipsec-isakmp
R-LYON(config-crypto-map)# set peer _____________
R-LYON(config-crypto-map)# set transform-set _____________
R-LYON(config-crypto-map)# match address _____________
```

---

### 2.5 – ÉTAPE 5 : Application sur interface WAN

**Sur R-PARIS :**

```ios
R-PARIS(config)# interface GigabitEthernet0/1
R-PARIS(config-if)# crypto map _____________
```

**Sur R-LYON :**

```ios
R-LYON(config)# interface GigabitEthernet0/1
R-LYON(config-if)# crypto map _____________
```

---

## ✅ PARTIE 3 – Vérification (20 min)

### 3.1 – Déclencher le tunnel (trafic intéressant)

```
PC-PARIS# ping 192.168.20.10
```

**Résultat : _______**

> *Note : Le premier ping peut échouer (le temps que Phase 1 et Phase 2 s'établissent). Répétez le ping.*

---

### 3.2 – Vérifier Phase 1

```ios
R-PARIS# show crypto isakmp sa
```

**Relevez la sortie :**

```
dst             src             state          conn-id
___________     ___________     ___________    _______
```

**Q2.** Quel état indique que la Phase 1 est établie ? L'obtenez-vous ?

_________________________________________________________________________

**Q3.** Si l'état est `MM_NO_STATE` ou rien, quelle est la première chose à vérifier ?

_________________________________________________________________________

---

### 3.3 – Vérifier Phase 2

```ios
R-PARIS# show crypto ipsec sa
```

**Relevez les compteurs :**

| **Compteur** | **Valeur après le ping** |
|---|---|
| `#pkts encaps` | |
| `#pkts encrypt` | |
| `#pkts decaps` | |
| `#pkts decrypt` | |
| `#pkts send errors` | |

**Q4.** Les compteurs `encaps` et `decrypt` sont-ils > 0 ? Qu'est-ce que cela confirme ?

_________________________________________________________________________

**Q5.** Que signifie un compteur `#pkts send errors > 0` ?

_________________________________________________________________________

---

### 3.4 – Vérifier depuis R-LYON

```ios
R-LYON# show crypto isakmp sa
R-LYON# show crypto ipsec sa
```

**Q6.** Les compteurs `encaps` et `decaps` sont-ils cohérents entre R-PARIS et R-LYON ? (Le encrypt de R-PARIS doit correspondre au decrypt de R-LYON, et vice-versa)

_________________________________________________________________________

---

### 3.5 – Vérifier la crypto map

```ios
R-PARIS# show crypto map
```

**Relevez :**

- Peer configuré : ___________
- Transform-set utilisé : ___________
- ACL associée : ___________

---

## 🛠️ PARTIE 4 – Débogage (10 min)

### Mise en situation

> Le formateur a injecté une erreur de configuration sur R-LYON. Le tunnel ne monte pas après vos pings.

**Configuration erronée injectée (à identifier) :**

```ios
! R-LYON a été configuré avec :
crypto isakmp key VPN-CIEL-2026 address 203.0.113.1

! Mais le transform-set est :
crypto ipsec transform-set TS_VPN esp-aes esp-sha-hmac
  mode tunnel
! (SHA-1 au lieu de SHA-256)
```

---

**Q7.** `show crypto isakmp sa` montre l'état `QM_IDLE` (Phase 1 OK). Mais `show crypto ipsec sa` ne montre aucun paquet chiffré. Quelle phase est bloquée ?

_________________________________________________________________________

**Q8.** Quelle est l'erreur dans le transform-set de R-LYON ?

_________________________________________________________________________

**Q9.** Écrivez la commande de correction sur R-LYON :

```ios
R-LYON(config)# crypto ipsec transform-set TS_VPN _______ _______ _______
R-LYON(cfg-crypto-trans)# mode _______
```

---

## 📊 PARTIE 5 – Questions d'analyse (5 min)

**Q10.** Un paquet provenant de PC-PARIS (192.168.10.10) vers 8.8.8.8 (Internet) passera-t-il dans le tunnel VPN ? Justifiez.

_________________________________________________________________________
_________________________________________________________________________

**Q11.** Pourquoi l'ACL crypto ne doit-elle PAS avoir de règle `permit ip any any` ?

_________________________________________________________________________
_________________________________________________________________________

**Q12.** Après 3 600 secondes (1 heure), que se passe-t-il avec la Phase 2 ? Et après 86 400 secondes (24 heures) ?

_________________________________________________________________________
_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 | Ping WAN + Q1 | /2 |
| Partie 2 – ACL | ACL miroir correcte sur les deux routeurs | /3 |
| Partie 2 – Phase 1 | isakmp policy + PSK correct | /4 |
| Partie 2 – Phase 2/Map | transform-set + crypto map + application interface | /4 |
| Partie 3 – isakmp sa | show + QM_IDLE + Q2–Q3 | /3 |
| Partie 3 – ipsec sa | Compteurs > 0 + Q4–Q6 | /4 |
| Partie 4 – Debug | Identification + correction + Q7–Q9 | /3 |
| Partie 5 – Analyse | Q10–Q12 | /3 |
| Présentation / soin | — | /1 |
| **TOTAL** | | **/27** |

> *Ramené à /20 : score × 0,74*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
