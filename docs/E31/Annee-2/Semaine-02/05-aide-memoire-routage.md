# 🗂️ AIDE-MÉMOIRE ROUTAGE STATIQUE — À PLASTIFIER
## Table de routage · ip route · Dépannage · BAC PRO CIEL · E31 · 2ᵉ année S2

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 📋 Lire une table de routage

```
S    192.168.40.0/24 [1/0] via 10.1.2.2
│         │          │ │       │
│         │          │ └─ Métrique (0 pour statique)
│         │          └─── Distance admin (1=statique)
│         └──────────── Réseau destination/préfixe
└────────────────────── Code source de la route
```

### Codes à connaître

| Code | Source | DA |
|---|---|---|
| **C** | Connecté (interface UP) | 0 |
| **S** | Statique (`ip route`) | 1 |
| **S*** | Route par défaut | 1 |
| **O** | OSPF | 110 |
| **R** | RIP | 120 |

---

## ⌨️ Commandes ip route

```
AJOUTER :
Router(config)# ip route [réseau] [masque] [next-hop]
Ex : ip route 192.168.40.0 255.255.255.0 10.1.2.2

SUPPRIMER :
Router(config)# no ip route 192.168.40.0 255.255.255.0 10.1.2.2

ROUTE PAR DÉFAUT :
Router(config)# ip route 0.0.0.0 0.0.0.0 [next-hop]
```

---

## 🔑 Masques courants

| CIDR | Masque décimal | Hôtes |
|---|---|---|
| /24 | 255.255.255.0 | 254 |
| /30 | 255.255.255.252 | **2** (WAN) |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |

---

## 🔴 4 Pannes fréquentes

```
1. ROUTE MANQUANTE   → réseau absent de la table
   Détection : show ip route → réseau introuvable
   Correction : ip route [réseau] [masque] [next-hop]

2. MASQUE INCORRECT  → /16 au lieu de /24 par ex.
   Détection : show ip route → masque ≠ topologie
   Correction : no ip route (mauvais) + ip route (corrigé)

3. NEXT-HOP INJOIGNABLE → adresse next-hop inexistante
   Détection : ping [next-hop] → timeout
   Correction : no ip route + ip route avec bonne @

4. ASYMÉTRIE A/R     → ping OK dans un sens, timeout de l'autre
   Détection : traceroute + show ip route sur chaque routeur
   Correction : ajouter la route retour manquante
```

---

## 🔬 Méthode dépannage 5 étapes

```
1. SYMPTÔME  → Qui ne joint pas qui ?
2. PING      → ping de proche en proche → où s'arrête-t-il ?
3. TRACEROUTE → traceroute [dest] → dernier hop qui répond
4. SHOW IP ROUTE → sur chaque routeur → route présente ? masque ? next-hop ?
5. CORRIGER + VÉRIFIER → ping end-to-end !!!
```

---

## ✅ Commandes de vérification

```
show ip route                  ← table de routage complète
show ip interface brief        ← état de toutes les interfaces
ping [adresse]                 ← test de joignabilité
ping [adresse] source [intf]   ← ping avec source spécifique
traceroute [adresse]           ← tracer le chemin
show running-config | include ip route  ← voir les routes statiques
```

---

## ⚠️ Règle d'or du routage

```
Pour que A communique avec B :
TOUS les routeurs sur le chemin doivent avoir :
  ✓ une route vers le réseau de B (aller)
  ✓ une route vers le réseau de A (retour)

Oublier le retour = ping timeout côté A = panne asymétrique
```

---

*Aide-Mémoire Routage Statique — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S2*
*Compétences C2.2 · C2.3 · S2.3*
