# 🗂️ AIDE-MÉMOIRE OSPF CONCEPTS — À PLASTIFIER
## État de lien · Convergence · Aires · Router-ID · Coût · BAC PRO CIEL · E31 · 2ᵉ année S3

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## ⚡ Les 5 étapes de convergence OSPF

```
1. HELLO PACKETS
   Multicast 224.0.0.5 · toutes les 10s
   → Découverte des voisins

2. ADJACENCES (état FULL)
   Échange bidirectionnel confirmé

3. LSA (Link State Advertisement)
   Chaque routeur annonce ses liens directs
   → Inondé à toute l'aire

4. LSDB (Link State DataBase)
   Identique sur tous les routeurs de l'aire
   → show ip ospf database

5. SPF / DIJKSTRA
   Calcul du chemin de coût minimal
   → Mise à jour table de routage (code O)
   → show ip route
```

---

## 📊 États de voisinage

```
DOWN → INIT → 2-WAY → EXSTART → EXCHANGE → LOADING → FULL ✓

FULL = adjacence opérationnelle
show ip ospf neighbor
```

---

## 🏛️ Aires OSPF

```
AREA 0 = Backbone (obligatoire)
Toutes les autres aires doivent toucher Area 0

ABR = routeur membre de 2 aires ou plus
   → résume les routes entre aires

Code O    = route intra-aire
Code O IA = route inter-aire (via ABR)
DA OSPF   = 110
```

---

## 🆔 Router-ID (priorité décroissante)

```
1. Configuré manuellement :
   router-id X.X.X.X  ← priorité max

2. Plus haute IP de Loopback active

3. Plus haute IP physique active

Bonne pratique :
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
→ Stable même si interfaces physiques tombent
```

---

## 💹 Coût OSPF

```
Coût = Référence / Bande passante (bps)
Référence par défaut = 100 Mbps
Coût minimum = 1

Interface    Débit     Coût (réf 100M)
Série T1     1,5 Mbps       64
Ethernet     10 Mbps        10
FastEthernet 100 Mbps        1  ← même coût !
GigabitEth   1 000 Mbps      1  ← même coût !

⚠️ PROBLÈME : FastEthernet = GigabitEthernet = 1
SOLUTION :
auto-cost reference-bandwidth 1000
→ FastEthernet = 10, GigabitEthernet = 1
```

---

## ✅ Commandes de vérification OSPF

```
show ip ospf neighbor       ← états des adjacences
show ip ospf database       ← contenu de la LSDB
show ip route               ← table de routage (code O, O IA)
show ip ospf interface Gi0/0 ← coût, area, hello interval
show ip ospf                ← Router-ID, area, SPF runs
```

---

## 🔑 Lire une entrée OSPF dans la table

```
O    10.2.3.0/30 [110/2] via 10.1.2.2
│         │       │   │        │
│         │       │   └─ Coût total SPF
│         │       └─── DA = 110 (OSPF)
│         └─────────── Réseau / préfixe
└────────────────────── O = intra-aire

O IA = inter-aire (depuis autre area via ABR)
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| Area 1 sans toucher Area 0 | Toujours connecter à Area 0 |
| Deux routeurs avec même Router-ID | Router-ID doit être UNIQUE |
| Pas de Loopback → Router-ID instable | Créer interface Loopback0 |
| Référence par défaut sur réseau Gbps | auto-cost reference-bandwidth 1000 |
| Oublier la route retour | Vérifier O et O IA dans les deux sens |

---

*Aide-Mémoire OSPF Concepts — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S3*
*Compétences S2.3 · S2.4 · C2.1 · C2.3*
