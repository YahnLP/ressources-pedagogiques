# 🔍 ACTIVITÉ DE DÉCOUVERTE — S2 · 3ᵉ ANNÉE · E31
## « Même protocole, deux familles » — Décoder OSPFv3 Multi-AF sans cours préalable

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement
> **Principe** : Tu connais déjà OSPFv2. On te présente une config OSPFv3 Multi-AF et les sorties de vérification. Tu dois identifier les différences par toi-même.

---

## 🎯 Mise en situation

> Ton entreprise vient d'embaucher un consultant qui a configuré un routeur en "OSPFv3 Multi-AF".
> Il est reparti sans laisser de documentation. Tu dois comprendre ce qu'il a fait
> à partir de la configuration et des sorties de commandes qu'il a laissées.

---

## 📋 Configuration laissée par le consultant

### `show running-config` (extrait — R2)

```
!
hostname R2
!
ipv6 unicast-routing
!
interface GigabitEthernet0/0
 ip address 10.0.12.2 255.255.255.252
 ipv6 address 2001:DB8:12::2/64
 ipv6 address FE80::2 link-local
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
 no shutdown
!
interface GigabitEthernet0/1
 ip address 10.0.23.1 255.255.255.252
 ipv6 address 2001:DB8:23::1/64
 ipv6 address FE80::1 link-local
 ospfv3 1 ipv4 area 0
 ospfv3 1 ipv6 area 0
 no shutdown
!
router ospfv3 1
 router-id 2.2.2.2
 !
 address-family ipv4 unicast
 exit-address-family
 !
 address-family ipv6 unicast
 exit-address-family
!
```

### `show ip route ospf` (sur R2)

```
O     192.168.1.0/24 [110/2] via 10.0.12.1, GigabitEthernet0/0
O     192.168.3.0/24 [110/2] via 10.0.23.2, GigabitEthernet0/1
```

### `show ipv6 route ospf` (sur R2)

```
O   2001:DB8:1::/64 [110/2]
     via FE80::1, GigabitEthernet0/0
O   2001:DB8:3::/64 [110/2]
     via FE80::2, GigabitEthernet0/1
```

### `show ipv6 ospf neighbor` (sur R2)

```
          OSPFv3 Router with ID (2.2.2.2) (Process ID 1)

Neighbor ID     Pri   State           Dead Time   Interface ID    Interface
1.1.1.1           1   FULL/  -        00:00:36    4               GigabitEthernet0/0
3.3.3.3           1   FULL/  -        00:00:39    4               GigabitEthernet0/1
```

---

## 🔍 PARTIE 1 — Comparer avec OSPFv2 (12 min)

**Question 1.1** — Dans la config OSPFv2 que tu connais (2A S3), comment activait-on OSPF sur une interface ?

```
Méthode OSPFv2 (dans le process) :
  router ospf 1
  network ______________ ______________ area __

Méthode OSPFv3 Multi-AF (sur l'interface) :
  ospfv3 1 ______ area __
  ospfv3 1 ______ area __
```

**Question 1.2** — Dans la config du consultant, sur l'interface Gi0/0 de R2, combien de fois la commande `ospfv3` apparaît-elle ? Pourquoi selon toi ?

```
Nombre d'occurrences : _______
L'une active OSPF pour : _______________________ (famille d'adresses IPv_)
L'autre active OSPF pour : ____________________ (famille d'adresses IPv_)
```

**Question 1.3** — Compare le process OSPF :

| Élément | OSPFv2 (ta config 2A) | OSPFv3 Multi-AF (config du consultant) |
|---|---|---|
| Commande process | `router ospf 1` | |
| Router-ID | Adresse IPv4 ou Loopback | |
| Sections internes | Aucune | `address-family __` et `address-family __` |
| Commande `network` | Dans le process | |

---

## 🔍 PARTIE 2 — Analyser les sorties de vérification (12 min)

**Question 2.1** — `show ip route ospf` montre des routes IPv4 apprises via OSPF.
`show ipv6 route ospf` montre des routes IPv6.
Ces deux tables coexistent-elles sur le même routeur ?

```
☐ Oui — le même routeur a deux tables de routage distinctes (IPv4 et IPv6)
☐ Non — une seule table contient tout
```

**Question 2.2** — Dans `show ipv6 route ospf`, le next-hop est `FE80::1` et non `2001:DB8:12::1`.
`FE80::` est une adresse de type : ☐ Global Unicast ☐ **Link-Local** ☐ Multicast.
Pourquoi OSPFv3 utilise-t-il les adresses link-local comme next-hop ?

```
Une adresse FE80:: est valable uniquement sur : ______________________________
Les paquets OSPFv3 Hello sont envoyés en multicast vers : ____________________
L'avantage d'utiliser les link-local comme next-hop : _________________________
```

**Question 2.3** — Dans `show ipv6 ospf neighbor`, les Neighbor ID sont `1.1.1.1` et `3.3.3.3`.
Ce sont des adresses IPv4, pas IPv6. Pourquoi ?

```
Le Router-ID OSPFv3 est toujours au format : ________________________________
Même si le routeur ne transporte que de l'IPv6, le Router-ID doit être configuré
en format : ☐ IPv6 ☐ IPv4

Si un routeur n'a aucune interface IPv4 active, comment configurer le Router-ID ?
→ ___________________________________________________________________________
```

**Question 2.4** — L'état des voisins est `FULL/  -`. Dans OSPFv2, l'état était `FULL/DR` ou `FULL/BDR`.
Pourquoi le rôle DR/BDR est-il absent ici (indiqué par `-`) ?

```
Le rôle DR/BDR est élu sur les réseaux de type : ___________________________
Les interfaces ici sont de type : _________ (2 routeurs = lien point à point)
Sur un lien point à point : DR/BDR est : ☐ Élu ☐ Pas nécessaire
```

---

## 🔍 PARTIE 3 — Déduire les règles (11 min)

**Question 3.1** — Le consultant a tapé `ipv6 unicast-routing` en début de config. À quoi sert cette commande ?

```
Sans cette commande, le routeur : ___________________________________________
C'est l'équivalent IPv6 de : ________________________________________________
```

**Question 3.2** — Résume en 3 points ce qu'OSPFv3 Multi-AF fait différemment d'OSPFv2 :

```
Différence 1 : _______________________________________________________________
Différence 2 : _______________________________________________________________
Différence 3 : _______________________________________________________________
```

**Question 3.3** — Si un PC veut pinguer en IPv6 un serveur de l'autre côté du réseau, quelle table de routage le routeur consulte-t-il ?

```
Pour un paquet IPv4 : le routeur consulte → show ___ route
Pour un paquet IPv6 : le routeur consulte → show ___ route
```

---

## 🏁 Bilan

```
OSPFv3 Multi-AF permet de faire tourner OSPF pour :
  → ________________ (adresses IPv4)  ET  ________________ (adresses IPv6)
  dans le ________________ processus OSPF

La commande pour activer OSPFv3 sur une interface est :
  ospfv3 ___ ___ area ___

Le Router-ID OSPFv3 est toujours au format : ________________________________

L'adresse multicast des Hello OSPFv3 est : ___________________________________
(contre 224.0.0.5 pour OSPFv2)
```

> ✅ Tu viens de comprendre l'essence d'OSPFv3 Multi-AF sans cours préalable.
> Le cours va maintenant t'expliquer POURQUOI ces choix ont été faits.

---

## 📎 Pour l'enseignant — Réponses

**1.2** : 2 occurrences — `ospfv3 1 ipv4 area 0` pour l'AF IPv4 et `ospfv3 1 ipv6 area 0` pour l'AF IPv6

**2.2** : FE80 = Link-Local · valide sur un seul lien · Hello OSPFv3 → FF02::5 · Avantage : indépendant de l'adressage global, toujours disponible même si l'adresse globale change

**2.3** : Router-ID = format IPv4 obligatoire · Sans interface IPv4 → `router-id X.X.X.X` obligatoire dans le process

**2.4** : DR/BDR sur réseaux multi-accès (Ethernet) mais ici liens point-à-point → `-` = pas de DR/BDR élu

**3.1** : Sans `ipv6 unicast-routing`, le routeur ne relaie pas les paquets IPv6 (comme `ip routing` pour IPv4)

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S2*
*Compétences : S2.2 · S2.6 · C2.3*
