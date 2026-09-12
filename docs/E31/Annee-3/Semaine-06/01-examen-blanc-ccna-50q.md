# 📋 EXAMEN BLANC CCNA 200-301 — S6 · 3ᵉ ANNÉE · E31
## 50 Questions · Conditions Réelles · 80 Minutes

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **⏱️ Durée : 80 minutes · SILENCE OBLIGATOIRE**
> **Règles** : Calculatrice autorisée · Papier brouillon · Aucune fiche · Aucun téléphone
> **Barème** : 2 pts par bonne réponse · 0 si faux · **TOTAL /100**

---

> ⚠️ **Pas de retour arrière possible sur le vrai examen.** Entraîne-toi à répondre dans l'ordre.

---

## 🌐 Domaine 1 — Network Fundamentals (Q1-Q10)

**Q1** — Quel sous-réseau contient l'adresse `172.16.45.200/20` ?

```
A) 172.16.32.0/20    B) 172.16.48.0/20
C) 172.16.45.0/20    D) 172.16.40.0/20
```
___

**Q2** — Combien d'hôtes utilisables dans un `/26` ?

```
A) 30    B) 62    C) 64    D) 126
```
___

**Q3** — Un hôte a `192.168.5.33/28`. Quelle est son adresse de broadcast ?

```
A) 192.168.5.47    B) 192.168.5.63
C) 192.168.5.255   D) 192.168.5.48
```
___

**Q4** — Quel protocole résout les adresses IP en adresses MAC sur un LAN IPv4 ?

```
A) DNS    B) DHCP    C) ARP    D) RARP
```
___

**Q5** — Quelle couche OSI segmente les données en "segments" via TCP ?

```
A) Réseau (L3)    B) Transport (L4)    C) Session (L5)    D) Liaison (L2)
```
___

**Q6** — Quel protocole utilise UDP et le port 69 ?

```
A) SSH    B) FTP    C) TFTP    D) SNMP
```
___

**Q7** — Un switch reçoit une trame avec une adresse MAC destination inconnue. Que fait-il ?

```
A) La supprime    B) La renvoie à la source    C) La flood sur tous les ports sauf l'entrant    D) La transfère au routeur
```
___

**Q8** — Quelle affirmation sur IPv6 est VRAIE ?

```
A) IPv6 utilise des adresses 32 bits
B) IPv6 n'a pas d'adresses broadcast
C) IPv6 exige NAT pour la communication Internet
D) IPv6 utilise ARP pour la résolution d'adresses
```
___

**Q9** — Quelle plage d'adresses est définie comme privée par la RFC 1918 ?

```
A) 169.254.0.0/16    B) 172.16.0.0/12
C) 192.0.0.0/8       D) 10.0.0.0/24
```
___

**Q10** — Le modèle TCP/IP a combien de couches ?

```
A) 3    B) 4    C) 5    D) 7
```
___

---

## 🔌 Domaine 2 — Network Access (Q11-Q20)

**Q11** — Quel protocole prévient les boucles de couche 2 ?

```
A) OSPF    B) STP    C) LACP    D) RSTP uniquement
```
___

**Q12** — Quelle commande affiche les VLANs et leurs ports membres sur un switch Cisco ?

```
A) show ip vlan    B) show vlan brief    C) show interfaces trunk    D) show switchport
```
___

**Q13** — Un port trunk refuse de laisser passer le VLAN 40. Quelle commande le permet ?

```
A) switchport trunk native vlan 40
B) switchport trunk allowed vlan add 40
C) switchport access vlan 40
D) vlan 40 trunk
```
___

**Q14** — Quelle combinaison de modes LACP forme un EtherChannel ?

```
A) passive / passive    B) active / on    C) active / passive    D) on / passive
```
___

**Q15** — Dans `show etherchannel summary`, un port affiche `(I)`. Que signifie ce code ?

```
A) Interface inactive (shutdown)
B) Interface stand-alone (pas dans le bundle)
C) Interface en LACP initiant
D) Interface isolée par STP
```
___

**Q16** — Quelle commande configure `portfast` sur une interface switch ?

```
A) spanning-tree portfast    B) no spanning-tree    C) switchport portfast    D) spanning-tree mode rapid
```
___

**Q17** — Quel VLAN est natif par défaut sur les interfaces trunk Cisco ?

```
A) VLAN 0    B) VLAN 1    C) VLAN 100    D) VLAN 1002
```
___

**Q18** — Sur un switch Cisco, la commande `switchport mode dynamic desirable` signifie :

```
A) Force le port en mode trunk
B) Le port tente activement de négocier un trunk (DTP)
C) Le port répond aux tentatives de trunk mais n'initie pas
D) Désactive DTP
```
___

**Q19** — Quel type de câble Ethernet était requis pour connecter deux switches (avant l'auto-MDIX) ?

```
A) Droit (straight-through)    B) Croisé (crossover)
C) Console (rollover)          D) Série
```
___

**Q20** — Un port switch est configuré `switchport port-security maximum 2 violation restrict`. Que se passe-t-il à la 3ᵉ adresse MAC ?

```
A) Le port passe en err-disabled
B) Les trames non autorisées sont supprimées (dropped) mais le port reste actif
C) Une alerte est générée mais le trafic passe
D) Le port est mis en shutdown forcé
```
___

---

## 🌍 Domaine 3 — IP Connectivity (Q21-Q30)

**Q21** — Quel est le code d'une route OSPF dans la table de routage IOS ?

```
A) R    B) D    C) O    D) B
```
___

**Q22** — Qu'est-ce qu'une route flottante (floating static route) ?

```
A) Une route avec une métrique de 0
B) Une route statique avec une distance administrative plus élevée que la route principale
C) Une route apprise dynamiquement avec une priorité flottante
D) Une route qui change de next-hop automatiquement
```
___

**Q23** — Quelle est la distance administrative d'une route OSPF ?

```
A) 1    B) 90    C) 110    D) 120
```
___

**Q24** — La commande `ip route 0.0.0.0 0.0.0.0 10.0.0.1` configure :

```
A) Une route vers le réseau 10.0.0.0
B) Une route par défaut vers 10.0.0.1
C) Un résumé de routes vers 0.0.0.0
D) Une route nulle (blackhole)
```
___

**Q25** — Dans OSPF, quel est l'intervalle par défaut entre les Hello packets sur un lien Ethernet ?

```
A) 5 secondes    B) 10 secondes    C) 30 secondes    D) 40 secondes
```
___

**Q26** — Un routeur a ces routes pour la destination `10.1.1.1` :
```
O   10.0.0.0/8   via 192.168.1.1
S   10.1.0.0/16  via 192.168.1.2
C   10.1.1.0/24  directly connected
```
Laquelle utilise-t-il ?

```
A) O 10.0.0.0/8 (OSPF)    B) S 10.1.0.0/16 (statique)
C) C 10.1.1.0/24 (directe)    D) La route avec la DA la plus basse
```
___

**Q27** — Dans OSPFv3 Multi-AF, quelle commande active OSPF sur une interface pour IPv6 ?

```
A) ipv6 ospf 1 area 0
B) network :: ::/0 area 0
C) ospfv3 1 ipv6 area 0
D) router ospf 1 / ipv6 network area 0
```
___

**Q28** — Quel protocole BGP est utilisé entre routeurs de différents AS ?

```
A) iBGP    B) eBGP    C) BGP-4    D) OSPF externe
```
___

**Q29** — Dans BGP, quel attribut contrôle la SORTIE de trafic d'un AS ?

```
A) MED (Multi-Exit Discriminator)
B) AS-path length
C) Local-Preference
D) Weight (Cisco local uniquement)
```
___

**Q30** — Quelle commande vérifie les adjacences OSPF et leur état ?

```
A) show ip ospf database    B) show ip ospf neighbor
C) show ip route ospf       D) debug ip ospf events
```
___

---

## 🛠️ Domaine 4 — IP Services (Q31-Q36)

**Q31** — Un routeur est configuré comme serveur DHCP. Quelle commande exclut l'adresse `192.168.1.1` du pool ?

```
A) ip dhcp pool exclude 192.168.1.1
B) ip dhcp excluded-address 192.168.1.1
C) no ip dhcp 192.168.1.1
D) ip dhcp reserve 192.168.1.1
```
___

**Q32** — Qu'est-ce que NAT overload (PAT) ?

```
A) Traduction de plusieurs adresses IP privées vers plusieurs adresses publiques
B) Traduction de plusieurs adresses privées vers une seule adresse publique via les ports TCP/UDP
C) Traduction statique d'une adresse privée vers une adresse publique
D) Traduction d'adresses MAC en adresses IP
```
___

**Q33** — Quel protocole est utilisé pour synchroniser l'heure sur un réseau ?

```
A) SNMP    B) NTP    C) Syslog    D) TFTP
```
___

**Q34** — Quelle valeur DSCP correspond au trafic VoIP (Expedited Forwarding) ?

```
A) DSCP 0    B) DSCP 26    C) DSCP 46    D) DSCP 56
```
___

**Q35** — Dans le contexte 802.1X, quel est le rôle du serveur RADIUS ?

```
A) Bloquer physiquement les ports non autorisés
B) Décider si un utilisateur est autorisé à accéder au réseau
C) Chiffrer le trafic entre le client et le switch
D) Assigner automatiquement des adresses IP
```
___

**Q36** — Quelle commande envoie les messages syslog vers un serveur distant `192.168.1.50` ?

```
A) logging 192.168.1.50
B) syslog server 192.168.1.50
C) ip logging destination 192.168.1.50
D) log forward 192.168.1.50
```
___

---

## 🛡️ Domaine 5 — Security Fundamentals (Q37-Q43)

**Q37** — Une ACL standard est appliquée en `in` sur `Gi0/0`. Quel critère filtre-t-elle ?

```
A) L'adresse IP destination    B) Le port TCP/UDP source
C) L'adresse IP source         D) L'adresse MAC source
```
___

**Q38** — Quelle commande active le chiffrement de tous les mots de passe en clair dans la configuration ?

```
A) enable secret level 5    B) service password-encryption
C) crypto password all      D) password encrypt global
```
___

**Q39** — Un attaquant envoie des messages DHCP pour se faire passer pour un serveur DHCP légitime. Quelle fonctionnalité du switch empêche cela ?

```
A) DAI (Dynamic ARP Inspection)    B) Port Security
C) DHCP Snooping                   D) 802.1X
```
___

**Q40** — Quel protocole remplace Telnet pour l'administration sécurisée des équipements Cisco ?

```
A) HTTPS    B) SSL    C) SSH    D) TLS
```
___

**Q41** — Quelle est la différence entre WPA2-Personal et WPA2-Enterprise ?

```
A) WPA2-Enterprise utilise un serveur RADIUS pour l'authentification individuelle
B) WPA2-Enterprise est moins sécurisé car il partage un mot de passe
C) WPA2-Personal ne peut pas être utilisé en entreprise
D) WPA2-Enterprise ne supporte pas le protocole AES
```
___

**Q42** — Dans une ACL étendue, la commande suivante :
`access-list 110 deny tcp 10.0.0.0 0.0.0.255 any eq 23`
Que fait-elle ?

```
A) Bloque Telnet (port 23) depuis n'importe quelle source vers 10.0.0.0/24
B) Bloque Telnet depuis 10.0.0.0/24 vers n'importe quelle destination
C) Bloque tout le trafic TCP depuis 10.0.0.0/24
D) Bloque le port 23 UDP depuis 10.0.0.0/24
```
___

**Q43** — Un port switch affiche `err-disabled`. Quelle commande le remet en service ?

```
A) no shutdown
B) shutdown puis no shutdown
C) spanning-tree portfast reset
D) clear port security
```
___

---

## 🤖 Domaine 6 — Automation & Programmability (Q44-Q50)

**Q44** — Quel format de données est utilisé par les API REST des contrôleurs SDN modernes ?

```
A) XML    B) CSV    C) JSON    D) YAML uniquement
```
___

**Q45** — Quelle affirmation sur SDN est CORRECTE ?

```
A) SDN supprime le plan de données des équipements
B) SDN centralise le plan de contrôle dans un logiciel
C) SDN nécessite obligatoirement le protocole OpenFlow
D) SDN est uniquement applicable aux datacenters
```
___

**Q46** — Dans l'architecture SDN, l'interface entre le contrôleur et les applications s'appelle :

```
A) Southbound API    B) Eastbound API    C) Northbound API    D) Westbound API
```
___

**Q47** — Quel outil permet d'automatiser la configuration de plusieurs équipements réseau via des playbooks YAML ?

```
A) Cisco DNA Center    B) Ansible    C) Python seul    D) Terraform uniquement
```
___

**Q48** — Qu'est-ce que NFV (Network Functions Virtualization) ?

```
A) Virtualiser les switches physiques en switches logiciels
B) Déployer des fonctions réseau (pare-feu, LB) sur des VMs plutôt que sur matériel dédié
C) Un protocole de contrôle entre contrôleur SDN et switches
D) La même chose que SDN
```
___

**Q49** — Quelle commande Python utilise-t-on avec la bibliothèque `requests` pour faire un GET sur une API REST Cisco IOS XE ?

```
A) requests.get('https://router/api')
B) cisco.api.get('router', endpoint)
C) rest.call('GET', 'https://router')
D) urllib.get('https://router/api')
```
___

**Q50** — Dans un réseau traditionnel, chaque équipement gère son propre plan de contrôle. Quel est l'inconvénient principal pour un administrateur de 500 switches ?

```
A) Les performances réseau sont réduites
B) Chaque changement de politique doit être appliqué sur chaque équipement individuellement
C) Les protocoles de routage deviennent instables
D) La sécurité est réduite car les équipements sont indépendants
```
___

---

## 📊 Grille de score — à remplir après correction

| Domaine | Questions | Mon score | / Total |
|---|---|---|---|
| D1 — Fundamentals | Q1-Q10 | | /20 |
| D2 — Network Access | Q11-Q20 | | /20 |
| D3 — IP Connectivity | Q21-Q30 | | /20 |
| D4 — IP Services | Q31-Q36 | | /12 |
| D5 — Security | Q37-Q43 | | /14 |
| D6 — Automation | Q44-Q50 | | /14 |
| **TOTAL** | | | **/100** |

**Estimation CCNA (/1000)** : Score × 10 ≈ _______ / 1000
**Seuil CCNA** : 825/1000 → nécessite **≥ 83/100** à cet examen blanc

**Interprétation** :
- ≥ 88/100 → Prêt · S'inscrire dans les 2 semaines
- 80-87/100 → Très proche · 10 jours de révision ciblée
- 70-79/100 → Bien · 3-4 semaines de révision
- < 70/100 → Reprendre les fondamentaux avant de s'inscrire

---

---

# ✅ CORRECTION COMPLÈTE — Document enseignant uniquement

| Q | Rep | Justification |
|---|---|---|
| 1 | A | 172.16.32.0/20 : incréments de 16 sur 3ème octet → 32, 48, 64… · 45 est dans 32-47 |
| 2 | B | /26 = 6 bits hôtes → 2⁶-2 = 62 |
| 3 | A | /28 : incréments de 16 → 32, 48… · 33 est dans 32-47 · broadcast = .47 |
| 4 | C | ARP = Address Resolution Protocol (IP→MAC) |
| 5 | B | Transport (L4) = segments TCP/UDP |
| 6 | C | TFTP = Trivial FTP · UDP 69 |
| 7 | C | MAC inconnue → flood (sauf port source) = comportement normal |
| 8 | B | IPv6 : pas de broadcast · remplacé par multicast |
| 9 | B | RFC 1918 : 10.0.0.0/8 · 172.16.0.0/12 · 192.168.0.0/16 |
| 10 | B | TCP/IP : 4 couches (Application/Transport/Internet/Network Access) |
| 11 | A | STP = Spanning Tree Protocol (réponse B et D sont des variantes/compléments) · Réponse A (note: STP est une famille qui inclut RSTP) → réponse la plus complète = A |
| 12 | B | `show vlan brief` = liste VLANs + ports |
| 13 | B | `switchport trunk allowed vlan add 40` |
| 14 | C | active/passive = EC LACP formé ✓ |
| 15 | B | (I) = stand-alone, hors bundle |
| 16 | A | `spanning-tree portfast` |
| 17 | B | VLAN 1 = natif par défaut |
| 18 | B | `dynamic desirable` = initie activement la négociation trunk (DTP) |
| 19 | B | Crossover pour switch-switch (avant auto-MDIX) |
| 20 | B | `restrict` = drop les trames non autorisées + log, port reste actif |
| 21 | C | Code O = OSPF |
| 22 | B | Floating static = DA plus élevée que la route principale |
| 23 | C | DA OSPF = 110 |
| 24 | B | 0.0.0.0/0 = route par défaut |
| 25 | B | Hello OSPF Ethernet = 10 secondes |
| 26 | C | Longest prefix match : /24 > /16 > /8 |
| 27 | C | `ospfv3 1 ipv6 area 0` sur l'interface = syntaxe Multi-AF |
| 28 | B | eBGP = External BGP = entre AS différents |
| 29 | C | Local-Preference = contrôle la sortie de l'AS (plus haut = préféré) |
| 30 | B | `show ip ospf neighbor` |
| 31 | B | `ip dhcp excluded-address` |
| 32 | B | PAT/NAT overload = N adresses privées → 1 IP publique via ports |
| 33 | B | NTP = Network Time Protocol |
| 34 | C | DSCP 46 = EF (Expedited Forwarding) = VoIP |
| 35 | B | RADIUS = authentication server = décide OUI/NON |
| 36 | A | `logging [IP]` = envoyer syslog vers serveur distant |
| 37 | C | ACL standard = filtre sur IP SOURCE uniquement |
| 38 | B | `service password-encryption` = chiffre tous les mots de passe |
| 39 | C | DHCP Snooping = filtre serveurs DHCP non autorisés |
| 40 | C | SSH remplace Telnet (chiffré) |
| 41 | A | WPA2-Enterprise = serveur RADIUS = authentification individuelle |
| 42 | B | ACL étendue : src=10.0.0.0/0.0.0.255 → bloque Telnet DEPUIS ce réseau |
| 43 | B | err-disabled : shutdown puis no shutdown pour remettre |
| 44 | C | JSON = format API REST standard |
| 45 | B | SDN = plan de contrôle centralisé |
| 46 | C | Northbound = contrôleur ↔ applications (vers le haut) |
| 47 | B | Ansible = automatisation réseau par playbooks |
| 48 | B | NFV = fonctions réseau sur VMs |
| 49 | A | `requests.get()` = méthode HTTP GET en Python |
| 50 | B | 500 switches = 500 configurations manuelles = problème SDN résout |

**Erreurs pièges fréquentes** :
- Q1 : calcul de sous-réseau /20 → bien identifier le bloc de 16 sur le 3ème octet
- Q20 : confondre restrict (drop + log) vs shutdown (err-disabled) vs protect (drop silencieux)
- Q26 : longest prefix match prime sur DA et métrique
- Q42 : ACL étendue : lire src PUIS dst (10.0.0.0/24 est la source, `any` est la destination)

---

*Examen Blanc CCNA 200-301 + Correction — BAC PRO CIEL | E31 | 3ᵉ année S6*
