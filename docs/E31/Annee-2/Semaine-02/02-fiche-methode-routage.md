# 📘 FICHE MÉTHODE — S2 · 2ᵉ ANNÉE · E31
## Table de routage · Routage statique · Méthode de dépannage · Consolidation avant OSPF

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences travaillées** : C2.1 · C2.2 · C2.3 · C3.1 · S2.3

---

## 🔑 Vocabulaire clé à maîtriser

| Terme | Définition |
|---|---|
| **Routage** | Mécanisme par lequel un routeur décide vers quelle interface transmettre un paquet IP |
| **Table de routage** | Base de données interne du routeur listant tous les réseaux connus et comment les atteindre |
| **Route connectée** (C) | Réseau directement branché sur une interface du routeur — ajoutée automatiquement |
| **Route statique** (S) | Route configurée manuellement par l'administrateur — ne s'adapte pas aux pannes |
| **Route par défaut** (S*) | Route "attrape-tout" utilisée quand aucune autre route ne correspond (0.0.0.0/0) |
| **Next-hop** | Adresse IP du **prochain routeur** sur le chemin vers la destination |
| **Distance administrative** (AD) | Indice de confiance d'une source de routage : plus petite = plus fiable (C=0, S=1, OSPF=110) |
| **Métrique** | Coût d'une route selon le protocole (OSPF : coût lié au débit · RIP : nombre de sauts) |
| **Masque de sous-réseau** | Délimite la partie réseau et la partie hôte d'une adresse IP |
| **Asymétrie de routage** | Situation où le chemin aller et le chemin retour sont différents — source fréquente de bugs |

---

## 1️⃣ — Structure d'une table de routage IOS

### Lire une entrée de table de routage

```
S    192.168.40.0/24 [1/0] via 10.1.2.2, 00:45:12, GigabitEthernet0/1
│         │          │ │       │           │           │
│         │          │ │       │           │           └─ Interface de sortie
│         │          │ │       │           └─────────── Temps depuis l'ajout
│         │          │ │       └───────────────────────── Next-hop
│         │          │ └─ Métrique (0 pour route statique)
│         │          └─── Distance administrative (1 = statique)
│         └──────────────── Réseau destination / longueur du préfixe
└────────────────────────── Code source de la route
```

### Les codes à connaître

| Code | Signification | Distance admin | Comment elle apparaît |
|---|---|---|---|
| **C** | Connected — réseau directement connecté | 0 | Automatique dès qu'une interface est UP |
| **L** | Local — adresse de l'interface elle-même | 0 | Automatique (IOS 15+) |
| **S** | Static — route configurée manuellement | 1 | `ip route` |
| **S*** | Static default route — route par défaut | 1 | `ip route 0.0.0.0 0.0.0.0 ...` |
| **O** | OSPF — appris par le protocole OSPF | 110 | Automatique si OSPF configuré |
| **R** | RIP — appris par le protocole RIP | 120 | Automatique si RIP configuré |

### Exemple de table de routage complète

```
R1# show ip route

Codes: C - connected, S - static, O - OSPF

      10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
C        10.1.2.0/30 is directly connected, GigabitEthernet0/1
L        10.1.2.1/32 is directly connected, GigabitEthernet0/1
      192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.10.0/24 is directly connected, GigabitEthernet0/0
L        192.168.10.1/32 is directly connected, GigabitEthernet0/0
S     192.168.40.0/24 [1/0] via 10.1.2.2
S*    0.0.0.0/0 [1/0] via 10.1.2.2
```

**Analyse de cet exemple :**
- R1 est directement connecté à deux réseaux (C)
- R1 connaît 192.168.40.0/24 via route statique
- R1 a une route par défaut (S*) — tout paquet non reconnu part vers 10.1.2.2

---

**🖼️ ILLUSTRATION 1**
> *Légende* : Schéma annoté d'une ligne de table de routage IOS avec 7 flèches pointant vers chaque champ : code (S), réseau destination, masque préfixe, distance administrative, métrique, next-hop, interface de sortie. Chaque flèche est accompagnée d'une explication en français. En dessous, un tableau récapitulatif des codes C/S/S*/O/R avec leur couleur distinctive et leur distance administrative.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 2️⃣ — Le routage statique : commandes IOS

### Ajouter une route statique

```cisco
Syntaxe :
Router(config)# ip route [réseau_dest] [masque] [next-hop]
                                               ou [interface_sortie]

Exemples :
Router(config)# ip route 192.168.40.0 255.255.255.0 10.1.2.2
Router(config)# ip route 192.168.40.0 255.255.255.0 GigabitEthernet0/1
```

> ⚠️ **Next-hop ou interface de sortie ?**
> - Préférer le **next-hop** (adresse IP) pour les liens point à point — plus fiable
> - L'interface seule fonctionne pour les liaisons Ethernet mais peut créer des ambiguïtés

### Route par défaut

```cisco
Router(config)# ip route 0.0.0.0 0.0.0.0 [next-hop]

Exemple — tout ce qui n'est pas connu part vers 10.1.2.2 :
Router(config)# ip route 0.0.0.0 0.0.0.0 10.1.2.2
```

> 💡 La route par défaut est reconnaissable dans `show ip route` par le code **S*** et l'adresse `0.0.0.0/0`.

### Supprimer une route statique

```cisco
Router(config)# no ip route [réseau_dest] [masque] [next-hop]

Exemple :
Router(config)# no ip route 192.168.40.0 255.255.255.0 10.1.2.2
```

### Tableau des masques courants

| Notation CIDR | Masque décimal | Nb d'hôtes utilisables |
|---|---|---|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /30 | 255.255.255.252 | 2 ← liaisons WAN point à point |
| /32 | 255.255.255.255 | 1 ← route hôte |

---

**🖼️ ILLUSTRATION 2**
> *Légende* : Topologie réseau avec 3 routeurs (R1, R2, R3) et 2 LANs (LAN1 en bleu, LAN4 en orange). Les routes statiques de R1 vers LAN4 et de R3 vers LAN1 sont représentées par des flèches pointillées traversant R2. À côté de chaque routeur, une mini-table de routage simplifiée montre les routes nécessaires. La commande ip route correspondante est affichée sous chaque flèche.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 3️⃣ — Les 4 pannes de routage les plus fréquentes

| # | Type de panne | Symptôme | Commande de détection | Correction |
|---|---|---|---|---|
| **1** | **Route manquante** | ping timeout destination | `show ip route` → réseau absent | `ip route [réseau] [masque] [nh]` |
| **2** | **Masque incorrect** | ping timeout ou instable | `show ip route` → masque ≠ réseau réel | `no ip route` + `ip route` corrigé |
| **3** | **Next-hop injoignable** | route présente mais inactive | `show ip route` → `*` ou absent · `ping [next-hop]` | `no ip route` + corriger l'adresse nh |
| **4** | **Asymétrie aller/retour** | ping fonctionne dans un sens seulement | `traceroute` + `show ip route` sur chaque routeur | Ajouter la route retour manquante |

> 🔑 **Règle d'or** : Pour qu'une communication fonctionne entre A et B, **TOUS les routeurs** sur le chemin doivent avoir une route vers le réseau source ET une route vers le réseau destination.

---

## 4️⃣ — Méthode de dépannage en 5 étapes

```
ÉTAPE 1 — IDENTIFIER LE SYMPTÔME
  → Qui ne peut pas joindre qui ?
  → Depuis quel équipement le problème se manifeste-t-il ?

ÉTAPE 2 — TESTER LA CONNECTIVITÉ (ping)
  → ping depuis la source vers la destination
  → Si timeout : le problème est au niveau 3 (routage) ou niveau 1/2 (lien)
  → ping de proche en proche : source → R1 → R2 → R3 → destination
     (permet de localiser où le paquet se perd)

ÉTAPE 3 — TRACER LE CHEMIN (traceroute)
  → traceroute [destination] depuis la source
  → Repérer le dernier routeur qui répond → c'est là que le paquet s'arrête

ÉTAPE 4 — INSPECTER LES TABLES DE ROUTAGE
  → show ip route sur chaque routeur du chemin
  → Vérifier : la route vers la destination est-elle présente ? masque correct ? next-hop correct ?
  → Vérifier aussi le CHEMIN RETOUR (route vers le réseau source)

ÉTAPE 5 — CORRIGER ET VÉRIFIER
  → Appliquer la correction (no ip route / ip route)
  → Retester avec ping end-to-end
  → Documenter dans le compte rendu d'intervention
```

---

**🖼️ ILLUSTRATION 3**
> *Légende* : Diagramme de flux "Méthode de dépannage routage" en 5 boîtes verticales numérotées et colorées, reliées par des flèches descendantes. Chaque boîte contient le nom de l'étape, la commande IOS associée, et un exemple de ce qu'on cherche. Des branches de décision apparaissent aux étapes 2 et 4 (OK → continuer / KO → retourner à l'étape précédente). Fond sombre, style terminal.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 5️⃣ — Limites du routage statique → vers OSPF

### Ce que le routage statique ne sait pas faire

| Limitation | Conséquence | Solution |
|---|---|---|
| Ne s'adapte pas aux pannes | Si un lien tombe, les routes statiques restent — trafic perdu | OSPF recalcule automatiquement |
| Doit être configuré sur CHAQUE routeur | Sur 50 routeurs = travail énorme, erreurs fréquentes | OSPF propage automatiquement les routes |
| Ne connaît pas l'état des liens | Une route peut pointer vers un lien mort | OSPF monitore les liens (Hello packets) |
| Aucune convergence | En cas de changement topologique, reconfiguration manuelle | OSPF converge en quelques secondes |

> **Question de transition** : *"Si le lien WAN entre R1 et R2 tombe, que se passe-t-il avec des routes statiques ? Et avec OSPF ?"*
>
> → Avec statique : les routes restent, les paquets arrivent à R1 qui n'a plus de chemin → **perte de trafic permanente** jusqu'à intervention manuelle
> → Avec OSPF : R1 et R2 détectent la panne (30s), recalculent, reroutent par R3 si possible → **récupération automatique**

---

**🖼️ ILLUSTRATION 4**
> *Légende* : Comparaison côte à côte de deux topologies identiques (R1-R2-R3, LAN1, LAN4). Colonne gauche "Routage statique" : le lien R1-R2 est barré d'une croix rouge, les routes statiques restent affichées (erreur), PC1 ne peut plus joindre PC4, icône X rouge. Colonne droite "OSPF" : même lien coupé mais une flèche pointillée montre un chemin de reroutage R1→R3→LAN4, icône checkmark vert. Texte comparatif en dessous.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

**🖼️ ILLUSTRATION 5**
> *Légende* : Tableau de synthèse comparant Statique vs OSPF sur 5 critères : Configuration (manuel vs automatique), Adaptation aux pannes (non vs oui), Scalabilité (difficile vs bonne), Convergence (aucune vs rapide), Utilisation recommandée (réseaux simples / stables vs réseaux complexes / dynamiques). Chaque critère a une icône et un code couleur (rouge = mauvais, vert = bon, orange = moyen).
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 📌 Les essentiels à retenir

> ✅ Table de routage : codes **C** (connecté) · **S** (statique) · **S*** (par défaut) · **O** (OSPF)
> ✅ Syntaxe : `ip route [réseau] [masque] [next-hop]` — supprimer avec `no`
> ✅ Route par défaut : `ip route 0.0.0.0 0.0.0.0 [next-hop]`
> ✅ **4 pannes fréquentes** : route manquante · masque incorrect · next-hop injoignable · asymétrie
> ✅ **Méthode 5 étapes** : symptôme → ping → traceroute → show ip route → correction
> ✅ Commandes de vérification : `show ip route` · `ping` · `traceroute` · `show ip interface brief`
> ✅ Routage statique = **simple mais rigide** → OSPF résout les problèmes de scalabilité et de convergence

---

*Fiche Méthode — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S2*
*Compétences : C2.1 · C2.2 · C2.3 · C3.1 · S2.3*
