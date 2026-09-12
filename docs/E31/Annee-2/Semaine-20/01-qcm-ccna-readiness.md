# 📋 AUTO-ÉVALUATION CCNA READINESS — S20 · 2ᵉ ANNÉE · E31
## 40 Questions de Positionnement · 6 Domaines CCNA 200-301

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Durée** : 50 minutes · **Aucune aide autorisée** · Calculatrice autorisée

> **Règle** : 1 point par bonne réponse · 0 si faux · Pas de malus
> **Objectif E31** : ≥ 28/40 · **Objectif CCNA 200-301** : ≥ 34/40

---

## 📊 Score par domaine (à remplir après correction)

| Domaine | Questions | Score | Niveau |
|---|---|---|---|
| D1 — Network Fundamentals | Q1-Q8 | /8 | |
| D2 — Network Access (L2) | Q9-Q16 | /8 | |
| D3 — IP Connectivity (L3) | Q17-Q24 | /8 | |
| D4 — IP Services | Q25-Q28 | /4 | |
| D5 — Security | Q29-Q34 | /6 | |
| D6 — Automation & Programmability | Q35-Q40 | /6 | |
| **TOTAL** | | **/40** | |

---

## 🌐 Domaine 1 — Network Fundamentals (Q1-Q8)

**Q1** — Combien d'adresses d'hôtes utilisables contient le réseau `10.0.0.0/22` ?

```
A) 512      B) 1 022      C) 1 024      D) 2 046
```
Réponse : ___

---

**Q2** — Quelle est la distance administrative d'une route OSPF ?

```
A) 1      B) 90      C) 110      D) 120
```
Réponse : ___

---

**Q3** — Quel protocole opère en couche 2 et empêche les boucles réseau ?

```
A) OSPF      B) STP      C) LACP      D) HSRP
```
Réponse : ___

---

**Q4** — Un paquet arrive sur R1 avec destination `192.168.20.55`. La table contient :
```
C  192.168.20.0/24 via Gi0/0
S  192.168.0.0/16  via 10.0.0.1
S* 0.0.0.0/0       via 10.0.0.2
```
Quelle route est utilisée ?

```
A) 0.0.0.0/0 (route par défaut)
B) 192.168.0.0/16 (route statique)
C) 192.168.20.0/24 (route connectée)
D) Le paquet est droppé
```
Réponse : ___

---

**Q5** — Quelle est la taille maximale d'une trame Ethernet standard (MTU) ?

```
A) 576 octets      B) 1 500 octets      C) 9 000 octets      D) 65 535 octets
```
Réponse : ___

---

**Q6** — Qu'est-ce que le principe de "longest prefix match" dans le routage IP ?

```
A) Préférer la route avec la plus petite distance administrative
B) Préférer la route avec le préfixe le plus long (masque le plus spécifique)
C) Préférer la route avec la meilleure métrique
D) Préférer la route apprise en dernier
```
Réponse : ___

---

**Q7** — Quel type d'adresse IPv4 commence toujours par `224.0.0.x` ?

```
A) Broadcast      B) Loopback      C) Multicast      D) Anycast
```
Réponse : ___

---

**Q8** — Quelle couche OSI encapsule les données en "segments" ?

```
A) Couche 2 (Liaison)      B) Couche 3 (Réseau)
C) Couche 4 (Transport)    D) Couche 5 (Session)
```
Réponse : ___

---

## 🔌 Domaine 2 — Network Access / L2 (Q9-Q16)

**Q9** — Quelle commande IOS affiche l'état de tous les VLANs et leurs ports membres ?

```
A) show interfaces trunk
B) show vlan brief
C) show ip vlan
D) show switchport
```
Réponse : ___

---

**Q10** — Sur un switch Cisco, quelle commande active le protocole LACP en mode initiant sur les interfaces d'un EtherChannel ?

```
A) channel-group 1 mode on
B) channel-group 1 mode desirable
C) channel-group 1 mode active
D) channel-group 1 mode passive
```
Réponse : ___

---

**Q11** — Dans `show etherchannel summary`, que signifie le code `(s)` sur un port ?

```
A) Le port est en mode standalone (stand-alone)
B) Le port est suspended (suspendu dans le bundle)
C) Le port est en mode STP blocking
D) Le port est en mode speed auto
```
Réponse : ___

---

**Q12** — Quel est le VLAN natif par défaut sur les interfaces trunk Cisco ?

```
A) VLAN 0      B) VLAN 1      C) VLAN 100      D) Aucun VLAN natif par défaut
```
Réponse : ___

---

**Q13** — Quelle combinaison de modes LACP ne permet PAS de former un EtherChannel ?

```
A) active / active
B) active / passive
C) passive / passive
D) on / on
```
Réponse : ___

---

**Q14** — Quelle commande configure un port switch pour qu'il passe immédiatement en forwarding sans attendre STP ?

```
A) spanning-tree portfast
B) spanning-tree rapid
C) spanning-tree forward-time 0
D) no spanning-tree
```
Réponse : ___

---

**Q15** — Un port access en VLAN 30 reçoit une trame Ethernet non taguée. Que fait le switch ?

```
A) Il droppe la trame
B) Il accepte la trame et la traite dans VLAN 30
C) Il envoie la trame sur tous les VLANs
D) Il demande le VLAN à l'hôte source
```
Réponse : ___

---

**Q16** — Quelle méthode de load balancing EtherChannel est la plus adaptée à un réseau avec de nombreux clients accédant à quelques serveurs ?

```
A) src-mac      B) dst-mac      C) src-dst-ip      D) src-ip
```
Réponse : ___

---

## 🌍 Domaine 3 — IP Connectivity / L3 (Q17-Q24)

**Q17** — Quelle est la wildcard mask correspondant au masque `/25` ?

```
A) 0.0.0.255      B) 0.0.0.127      C) 0.0.0.128      D) 0.0.1.255
```
Réponse : ___

---

**Q18** — Dans OSPF, comment calcule-t-on la priorité pour l'élection du Router-ID si aucun `router-id` n'est configuré manuellement ?

```
A) L'adresse MAC la plus haute
B) L'adresse IP la plus haute sur une interface Loopback active
C) L'adresse IP la plus basse sur une interface active
D) Le numéro de processus OSPF le plus élevé
```
Réponse : ___

---

**Q19** — Quelle commande IOS permet de vérifier les adjacences OSPF et leur état ?

```
A) show ip ospf database
B) show ip ospf neighbor
C) show ip route ospf
D) show ospf process
```
Réponse : ___

---

**Q20** — Une route statique flottante est configurée avec la commande :
`ip route 0.0.0.0 0.0.0.0 10.1.3.1 5`
À quel moment sera-t-elle utilisée ?

```
A) Toujours, car elle a une distance administrative plus faible
B) Jamais, la distance administrative 5 est trop élevée
C) Uniquement quand la route principale (DA=1) disparaît de la table
D) Simultanément avec la route principale (load balancing)
```
Réponse : ___

---

**Q21** — Dans une table de routage, que signifie `O IA` ?

```
A) Route OSPF intra-aire (même aire)
B) Route OSPF inter-aire (autre aire, via ABR)
C) Route OSPF externe redistribuée
D) Route vers une interface Loopback OSPF
```
Réponse : ___

---

**Q22** — Un routeur OSPF a deux chemins vers la même destination avec des coûts différents : [110/3] et [110/7]. Lequel utilise-t-il ?

```
A) [110/7] (coût plus grand = lien plus rapide)
B) [110/3] (coût plus petit = chemin préféré)
C) Les deux en même temps (ECMP)
D) Celui appris en premier
```
Réponse : ___

---

**Q23** — Quelle commande configure un tunnel GRE entre deux routeurs Cisco ?

```
A) interface GRE0 / ip address ... / gre source ... / gre destination ...
B) interface Tunnel0 / ip address ... / tunnel source ... / tunnel destination ...
C) interface VPN0 / ip address ... / tunnel mode gre
D) crypto isakmp tunnel gre ... 
```
Réponse : ___

---

**Q24** — Sur quel port UDP travaille le protocole TFTP ?

```
A) 21      B) 22      C) 69      D) 161
```
Réponse : ___

---

## 🛠️ Domaine 4 — IP Services (Q25-Q28)

**Q25** — Un routeur est configuré avec `ip route 0.0.0.0 0.0.0.0 10.0.0.1` et `ip route 0.0.0.0 0.0.0.0 10.0.0.2 10`. Quelle route sera active en fonctionnement normal ?

```
A) Les deux en ECMP
B) Via 10.0.0.1 (DA implicite = 1)
C) Via 10.0.0.2 (configurée en dernier)
D) Aucune (conflit)
```
Réponse : ___

---

**Q26** — Quel protocole permet à deux routeurs de partager une adresse IP virtuelle pour assurer la redondance de passerelle (FHRP) ?

```
A) OSPF      B) STP      C) HSRP      D) LACP
```
Réponse : ___

---

**Q27** — Quel mécanisme QoS garantit une bande passante minimale à une classe de trafic tout en permettant l'utilisation de la bande passante excédentaire par les autres classes ?

```
A) LLQ (Low Latency Queue)
B) CBWFQ (Class-Based Weighted Fair Queuing)
C) FIFO
D) Priority Queue stricte
```
Réponse : ___

---

**Q28** — Quelle valeur DSCP correspond au marquage "Best Effort" (trafic ordinaire sans priorité) ?

```
A) DSCP 0      B) DSCP 10      C) DSCP 34      D) DSCP 46
```
Réponse : ___

---

## 🛡️ Domaine 5 — Security Fundamentals (Q29-Q34)

**Q29** — Quelle commande active la sécurité de port sur une interface switch et limite à 1 adresse MAC ?

```
A) switchport port-security
   switchport port-security maximum 1
B) port-security enable maximum 1
C) ip arp inspection
D) switchport security mac 1
```
Réponse : ___

---

**Q30** — Quel est le comportement par défaut d'une ACL Cisco à la fin de ses règles ?

```
A) Permit any (autoriser tout le reste)
B) Deny any (refuser tout le reste implicitement)
C) Log and permit
D) Retourner une erreur ICMP
```
Réponse : ___

---

**Q31** — Dans le contexte 802.1X, quel équipement joue le rôle d'Authenticator ?

```
A) Le PC client
B) Le serveur RADIUS
C) Le switch ou la borne WiFi
D) Le contrôleur de domaine Active Directory
```
Réponse : ___

---

**Q32** — Quelle variante EAP nécessite un certificat **client** en plus d'un certificat serveur ?

```
A) PEAP      B) EAP-TTLS      C) EAP-TLS      D) EAP-MD5
```
Réponse : ___

---

**Q33** — Que fait la commande `ip dhcp snooping` sur un switch Cisco ?

```
A) Active un serveur DHCP interne sur le switch
B) Filtre les messages DHCP pour empêcher les serveurs DHCP non autorisés
C) Désactive le DHCP sur toutes les interfaces
D) Configure le helper-address DHCP
```
Réponse : ___

---

**Q34** — Dans la sortie `show ip route`, une route notée `S*` signifie :

```
A) Route statique standard
B) Route statique par défaut (default route)
C) Route dynamique apprise via OSPF
D) Route de secours (floating static)
```
Réponse : ___

---

## 🤖 Domaine 6 — Automation & Programmability (Q35-Q40)

**Q35** — Quel format de données est utilisé par défaut dans les API REST des contrôleurs réseau modernes (Cisco DNA Center, etc.) ?

```
A) XML      B) YAML      C) JSON      D) CSV
```
Réponse : ___

---

**Q36** — Dans un réseau SDN (Software-Defined Networking), où réside le plan de contrôle ?

```
A) Distribué sur chaque équipement réseau (comme dans les réseaux traditionnels)
B) Centralisé sur un contrôleur SDN
C) Sur les serveurs applicatifs
D) Il n'existe pas dans les réseaux SDN
```
Réponse : ___

---

**Q37** — Quel outil Cisco permet de gérer et configurer automatiquement les équipements réseau via des playbooks YAML ?

```
A) Cisco DNA Center
B) Ansible
C) Terraform
D) Chef
```
Réponse : ___

---

**Q38** — Un fichier de configuration rsyslog contient :
`if $msg contains "Failed password" then action(type="omfile" file="/var/log/ssh_alerts.log")`
Que fait cette règle ?

```
A) Bloque toutes les connexions SSH échouées
B) Envoie une alerte email pour les échecs SSH
C) Écrit les messages contenant "Failed password" dans un fichier dédié
D) Supprime les messages d'authentification du journal système
```
Réponse : ___

---

**Q39** — Qu'est-ce que le RPO (Recovery Point Objective) dans un plan de reprise d'activité ?

```
A) Le délai maximal pour rétablir le service après un incident
B) La perte de données maximale tolérée (ancienneté de la dernière sauvegarde)
C) Le nombre maximum de pannes par an tolérées
D) Le coût maximal d'une opération de reprise
```
Réponse : ___

---

**Q40** — Dans une architecture WLAN d'entreprise, quel équipement centralise la gestion de tous les points d'accès WiFi ?

```
A) Serveur RADIUS
B) Pare-feu UTM
C) WLC (Wireless LAN Controller)
D) Switch de distribution
```
Réponse : ___

---

## 📊 Analyse de ton score — À compléter après correction

### Score global

```
Mon score : _______ / 40

Interprétation :
  ≥ 36/40 (90%) → Excellent — CCNA accessible dès maintenant
  32-35/40 (80-87%) → Très bon — finaliser 1-2 domaines faibles
  28-31/40 (70-77%) → Bon — révisions ciblées nécessaires avant E31
  24-27/40 (60-69%) → Moyen — plan de révision intensif sur 4 semaines
  < 24/40 (< 60%) → Reprendre les bases avec les séances S2, S3, S13
```

### Analyse par domaine

```
D1 Fundamentals    : ___/8  →  ☐ Acquis ☐ À retravailler
D2 Network Access  : ___/8  →  ☐ Acquis ☐ À retravailler
D3 IP Connectivity : ___/8  →  ☐ Acquis ☐ À retravailler
D4 IP Services     : ___/4  →  ☐ Acquis ☐ À retravailler
D5 Security        : ___/6  →  ☐ Acquis ☐ À retravailler
D6 Automation      : ___/6  →  ☐ Acquis ☐ À retravailler
```

### Mes 3 domaines les plus faibles

```
1. ________________________________ → Questions ratées : ______________________
2. ________________________________ → Questions ratées : ______________________
3. ________________________________ → Questions ratées : ______________________
```

---

---

# ✅ CORRECTION — Document enseignant uniquement

| Q | Rép. | Justification clé |
|---|---|---|
| 1 | B | /22 → 10 bits hôte → 2¹⁰-2 = 1022 |
| 2 | C | DA OSPF = 110 |
| 3 | B | STP = Spanning Tree Protocol (couche 2, anti-boucles) |
| 4 | C | Longest prefix match : /24 > /16 > /0 |
| 5 | B | MTU Ethernet = 1500 octets |
| 6 | B | Plus long préfixe = plus spécifique = priorité |
| 7 | C | 224.0.0.x = multicast (OSPF Hello = 224.0.0.5) |
| 8 | C | Couche 4 Transport = segments (TCP/UDP) |
| 9 | B | `show vlan brief` = VLANs + ports membres |
| 10 | C | `channel-group 1 mode active` = LACP actif |
| 11 | B | (s) = suspended (config VLAN différente entre membres) |
| 12 | B | VLAN 1 = VLAN natif par défaut |
| 13 | C | passive+passive = personne n'initie → pas d'EC |
| 14 | A | `spanning-tree portfast` = forwarding immédiat |
| 15 | B | Port access VLAN 30 : trame non taguée → traitée en VLAN 30 |
| 16 | C | src-dst-ip = nombreux clients vers quelques serveurs |
| 17 | B | /25 = 255.255.255.128 → wildcard = 0.0.0.127 |
| 18 | B | Router-ID : Loopback la plus haute IP (priorité 2) |
| 19 | B | `show ip ospf neighbor` = adjacences + états |
| 20 | C | Route flottante DA=5 s'active quand DA=1 disparaît |
| 21 | B | O IA = OSPF Inter-Area (autre aire via ABR) |
| 22 | B | Coût plus petit = chemin préféré (3 < 7) |
| 23 | B | `interface Tunnel0 / tunnel source / tunnel destination` |
| 24 | C | TFTP = UDP port 69 |
| 25 | B | DA implicite = 1 pour route statique → 10.0.0.1 active |
| 26 | C | HSRP = Hot Standby Router Protocol (FHRP Cisco) |
| 27 | B | CBWFQ = bande passante garantie par classe |
| 28 | A | DSCP 0 = Default/Best Effort |
| 29 | A | `switchport port-security` + `maximum 1` |
| 30 | B | Deny any implicite en fin d'ACL (règle fondamentale) |
| 31 | C | Authenticator = switch ou AP (intermédiaire) |
| 32 | C | EAP-TLS = certificat CLIENT + serveur (authentification mutuelle) |
| 33 | B | DHCP Snooping = filtrage des serveurs DHCP non autorisés |
| 34 | B | S* = static default route (0.0.0.0/0) |
| 35 | C | JSON = format API REST standard |
| 36 | B | SDN = plan de contrôle centralisé |
| 37 | B | Ansible = orchestration réseau par playbooks YAML |
| 38 | C | Règle rsyslog : écriture dans fichier si message contient "Failed password" |
| 39 | B | RPO = perte de données tolérée (ancienneté sauvegarde) |
| 40 | C | WLC = Wireless LAN Controller (gestion centralisée APs) |

---

*QCM CCNA Readiness — BAC PRO CIEL | E31 | 2ᵉ année S20*
*Bilan compétences : tous domaines E31*
