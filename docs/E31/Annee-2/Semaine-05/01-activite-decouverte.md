# 🎲 ACTIVITÉ DÉCOUVERTE – S5 ANNÉE 2 – E31
## « Le Vigile du Réseau » : Pourquoi les ACL Standard ne Suffisent Pas

---

## 🎯 OBJECTIFS

- ✅ Faire émerger les **limites des ACL standard** par l'exemple
- ✅ Faire exprimer le besoin de filtrer par **protocole, port et destination**
- ✅ Introduire la notion de **politique de sécurité** traduite en règles réseau
- ✅ Poser les bases du raisonnement "source → destination → service"

---

## ⏱️ DURÉE : 30 min

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur pose la situation :**

> *"Vous gérez le réseau d'une PME. Vous avez des ACL standard qu'on a vues en A1. Quelqu'un vous donne une liste de règles de sécurité à appliquer. Essayons de les traduire avec ce qu'on sait déjà."*

---

## 📋 PHASE 1 – La politique de sécurité (10 min)

**Le formateur affiche cette topologie au tableau :**

```
         INTERNET
             │
         [Routeur FAI]
             │
┌────────────┼────────────────────┐
│          [R-EDGE]               │
│         /        \              │
│   [LAN-Users]  [Serveur-Web]    │
│  192.168.1.0/24  10.0.1.10      │
│                                 │
│   [LAN-Admin]                   │
│   192.168.2.0/24                │
└─────────────────────────────────┘
```

**La politique de sécurité demandée (en langage naturel) :**

| **Règle** | **Description** |
|---|---|
| **R1** | Les utilisateurs LAN peuvent naviguer sur le Web (HTTP et HTTPS) vers Internet |
| **R2** | Les utilisateurs LAN NE peuvent PAS accéder en SSH aux serveurs |
| **R3** | Seul LAN-Admin peut accéder au Serveur-Web en HTTP |
| **R4** | Personne d'Internet ne peut pinger les machines internes |
| **R5** | Les admins peuvent accéder en SSH à tous les équipements |

---

**Exercice groupes de 4 (8 min) :**

> *"Essayez de traduire chaque règle avec la syntaxe ACL standard que vous connaissez :*
> `access-list <1-99> {permit|deny} <source> <wildcard>`"

| **Règle** | **Traduction ACL standard possible ?** | **Problème rencontré** |
|---|---|---|
| R1 (HTTP/HTTPS seulement) | OUI / NON | |
| R2 (bloquer SSH depuis LAN) | OUI / NON | |
| R3 (seulement Admin → Serveur-Web) | OUI / NON | |
| R4 (bloquer ICMP depuis Internet) | OUI / NON | |
| R5 (SSH Admin → partout) | OUI / NON | |

---

**Résultats attendus et discussion (5 min) :**

| **Règle** | **Résultat** | **Pourquoi ça coince** |
|---|---|---|
| R1 | ❌ Impossible | Une ACL standard ne peut pas distinguer HTTP (port 80) de SSH (port 22). On ne peut filtrer que la source. |
| R2 | ❌ Impossible | Pour bloquer SSH, il faut filtrer le port 22 (TCP). ACL standard : pas de notion de port. |
| R3 | ⚠️ Partiel | On peut autoriser 192.168.2.0, mais on ne peut pas préciser "uniquement HTTP vers ce serveur précis". |
| R4 | ❌ Impossible | Pour filtrer ICMP, il faut préciser le protocole. ACL standard ne le fait pas. |
| R5 | ⚠️ Partiel | On peut autoriser la source Admin, mais pas restreindre "uniquement SSH". |

---

## 💡 PHASE 2 – Ce qu'il nous manque (8 min)

**Le formateur demande :**

> *"Pour implémenter ces règles, de quoi avez-vous besoin dans l'ACL ?"*

**Brainstorming à noter :**

```
Pour filtrer correctement, une ACL doit pouvoir exprimer :

  1. L'adresse SOURCE         → déjà dans les ACL standard
  2. L'adresse DESTINATION    → manquant dans les ACL standard
  3. Le PROTOCOLE             → TCP ? UDP ? ICMP ? IP ?
  4. Le PORT de destination   → HTTP=80, SSH=22, HTTPS=443...
  5. Le PORT source           → parfois utile (ports éphémères)
```

**Le formateur conclut :**

> *"Les ACL étendues ajoutent exactement ces 4 capacités. La syntaxe est plus longue, mais chaque champ correspond à une question concrète : QUI ? VERS QUI ? PAR QUEL SERVICE ?"*

---

## ✍️ PHASE 3 – Tableau comparatif (5 min)

**À noter dans la fiche cours :**

| **Critère** | **ACL Standard (1–99)** | **ACL Étendue (100–199)** |
|---|---|---|
| Filtre sur source | ✅ | ✅ |
| Filtre sur destination | ❌ | ✅ |
| Filtre sur protocole (TCP/UDP/ICMP) | ❌ | ✅ |
| Filtre sur port | ❌ | ✅ |
| Placement recommandé | Proche de la **destination** | Proche de la **source** |
| Numérotation | 1–99 | 100–199 |
| ACL nommée | Possible | Possible |

---

## ✅ VALIDATION DE L'ACTIVITÉ

**L'activité est réussie si :**

- ✅ Les apprentis identifient pourquoi R1, R2, R4 sont impossibles en ACL standard
- ✅ Ils formulent les 4 critères manquants (destination, protocole, port)
- ✅ Ils comprennent que les ACL étendues sont plus précises → placement proche de la source

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
