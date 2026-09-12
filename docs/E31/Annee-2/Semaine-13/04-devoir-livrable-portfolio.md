# 📝 DEVOIR & LIVRABLE PORTFOLIO — S13 · 2ᵉ ANNÉE · E31
## EtherChannel LACP : Concepts · Configuration · Load balancing · Dépannage

---

> **Module** : E31 – Infrastructure Réseau
> **Épreuve visée** : **E31** – Épreuve pratique infrastructure réseau
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)
> **Format du rendu** : Fiche complétée, commandes IOS rédigées proprement

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S2.1** | Principes EtherChannel — bande passante, redondance, STP | /20 |
| **S2.2** | Protocoles LACP/PAgP — modes et compatibilité | /20 |
| **S2.3** | Load balancing — méthodes et choix | /15 |
| **C2.2** | Écrire les commandes de configuration IOS | /25 |
| **C2.3** | Dépannage via `show etherchannel summary` | /20 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation professionnelle

> **Tu es technicien réseau** dans un datacenter qui héberge les serveurs d'une entreprise.
> Le DSI vient de décider de doubler les liens entre les deux switches de distribution (SW-Dist1 et SW-Dist2)
> pour anticiper la croissance du trafic et garantir la continuité de service.
>
> Il te confie la mission de concevoir, configurer et documenter la solution.

---

## 🅰️ PARTIE A — En classe (45 min)

### ⚡ Exercice 1 — Concepts et justifications (/20)

**1.a** — Sans EtherChannel, si tu relies SW-Dist1 et SW-Dist2 avec 4 câbles GigabitEthernet, que fait STP ? Quel est le débit effectif ? *(6 pts)*

```
Action de STP : ______________________________________________________________
Nombre de liens actifs : _______ sur _______
Débit effectif : _______ Gbps   Débit théorique si tous actifs : _______ Gbps
```

**1.b** — Cite les 3 bénéfices apportés par EtherChannel dans ce contexte. *(6 pts)*

```
Bénéfice 1 : _________________________________________________________________
Bénéfice 2 : _________________________________________________________________
Bénéfice 3 : _________________________________________________________________
```

**1.c** — En cas de panne d'un des 4 liens membres du port-channel, compare le comportement avec et sans EtherChannel en termes de reconvergence : *(8 pts)*

```
Sans EtherChannel (STP classique) :
  Lien de secours : ________________________________________________________
  STP doit recalculer : ☐ Oui ☐ Non
  Délai avant retour au service : _________ secondes
  Utilisateurs impactés ? ☐ Oui ☐ Non

Avec EtherChannel :
  Les _______ liens restants continuent de transporter le trafic
  EtherChannel doit-il recalculer ? ☐ Oui ☐ Non
  Délai avant retour au service : _________ (ms ou s ?)
  Utilisateurs impactés ? ☐ Oui ☐ Non
```

---

### 🔄 Exercice 2 — Protocoles et modes (/20)

**2.a** — Complète le tableau de compatibilité LACP : *(8 pts)*

| SW-Dist1 mode | SW-Dist2 mode | EC formé ? | Protocole utilisé |
|---|---|---|---|
| active | active | | |
| active | passive | | |
| passive | passive | | |
| on | on | | |
| active | on | | |
| desirable | auto | | |
| desirable | desirable | | |

**2.b** — Pour la configuration du datacenter, lequel des modes LACP recommandes-tu ? Justifie. *(6 pts)*

```
Mode recommandé : ______________ sur SW-Dist1 ET ______________ sur SW-Dist2
Justification : _______________________________________________________________
Pourquoi pas le mode `on` ? ___________________________________________________
```

**2.c** — Quelle est la différence entre LACP et PAgP ? Dans quel cas utiliser LACP obligatoirement ? *(6 pts)*

```
LACP : standard _______________ fonctionnant entre équipements ________________
PAgP : protocole _______________ fonctionnant uniquement entre équipements ____

Utiliser LACP obligatoirement quand : ________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/60)

### ⌨️ Exercice 3 — Configuration complète (/25)

> **Topologie à configurer :**
> ```
> PC_Srv1 (192.168.100.10/24) ── SW-Dist1 ═══(4 liens)═══ SW-Dist2 ── PC_Srv2 (192.168.100.20/24)
>                                                   Po1                PC_Srv3 (192.168.200.10/24)
> VLAN 100 : Serveurs    PC_Srv4 (192.168.200.20/24)
> VLAN 200 : Admin
> ```
> Interfaces : Gi0/1, Gi0/2, Gi0/3, Gi0/4 entre les deux switches.

**3.a** — Écris la configuration complète pour **SW-Dist1** (toutes les commandes, dans l'ordre) : *(15 pts)*

```cisco
! SW-Dist1 — Configuration EtherChannel LACP
! Rédigé par : ___________________  Date : ____________

___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**3.b** — La configuration de SW-Dist2 est-elle identique à SW-Dist1 ? Justifie. *(4 pts)*

```
☐ Identique — car : __________________________________________________________
☐ Différente — différences : _________________________________________________
```

**3.c** — Après configuration, tu veux vérifier que les 4 liens sont actifs. Quelle commande taper et quel résultat attendre ? *(6 pts)*

```
Commande : __________________________________________________________________
Résultat attendu (recopie le format de la sortie avec les bons états) :

Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------
___    Po___(__)     ________    Gi0/1(___)  Gi0/2(___)  Gi0/3(___)  Gi0/4(___)
```

---

### 📊 Exercice 4 — Load balancing (/15)

**4.a** — Le datacenter héberge 50 clients (PC) qui accèdent à 3 serveurs (IP fixes).
Quelle méthode de load balancing est la plus appropriée et pourquoi ? *(5 pts)*

```
Méthode recommandée : ________________________
Justification : _____________________________________________________________
___________________________________________________________________________
```

**4.b** — Décris en 3 lignes comment EtherChannel décide sur quel lien membre envoyer un paquet, et pourquoi tous les paquets d'une même session TCP restent sur le même lien : *(5 pts)*

```
Mécanisme de décision : _____________________________________________________
___________________________________________________________________________
Garantie pour TCP : _________________________________________________________
```

**4.c** — Écris les 2 commandes IOS pour configurer et vérifier le load balancing `src-dst-ip` sur SW-Dist1 : *(5 pts)*

```cisco
SW-Dist1(config)# __________________________________________________________
SW-Dist1# __________________________________________________________
```

---

### 🔎 Exercice 5 — Dépannage (/20)

> Voici la sortie `show etherchannel summary` obtenue sur SW-Dist1 après une tentative de configuration :

```
SW-Dist1# show etherchannel summary
Flags:  D - down        P - bundled in port-channel
        I - stand-alone s - suspended
        H - Hot-standby (LACP only)
        R - Layer3      S - Layer2
        U - in-use

Group  Port-channel  Protocol    Ports
------+-------------+-----------+----------------------------
1      Po1(SD)       LACP        Gi0/1(D)   Gi0/2(D)
                                 Gi0/3(I)   Gi0/4(s)
```

**5.a** — Que signifie `Po1(SD)` ? Le port-channel est-il opérationnel ? *(4 pts)*

```
S = ________________________   D = ________________________
Po1(SD) signifie : __________________________________________________________
Trafic en cours de transit : ☐ Oui ☐ Non
```

**5.b** — Pour chaque port, identifie le problème probable : *(8 pts)*

| Port | Code | Problème probable | Action corrective |
|---|---|---|---|
| Gi0/1 | (D) | | |
| Gi0/2 | (D) | | |
| Gi0/3 | (I) | | |
| Gi0/4 | (s) | | |

**5.c** — La commande `show lacp 1 neighbor` sur SW-Dist1 révèle que SW-Dist2 a ses interfaces Gi0/1 et Gi0/2 en mode `on`. Quel est l'impact ? *(4 pts)*

```
Mode SW-Dist1 : active (LACP)   Mode SW-Dist2 : on (static)
Ces modes sont-ils compatibles ? ☐ Oui ☐ Non
Impact : ____________________________________________________________________
Fix : _______________________________________________________________________
```

**5.d** — Écris la séquence complète de correction pour rendre Po1 pleinement opérationnel avec les 4 ports actifs (en supposant que les câbles Gi0/1 et Gi0/2 sont juste déconnectés physiquement, que Gi0/3 a un problème de mode, et que Gi0/4 a un VLAN différent) : *(4 pts)*

```cisco
! Corrections à apporter

! 1. Câbles Gi0/1 et Gi0/2 — intervention physique requise
(Rebrancher les câbles)

! 2. Corriger le mode sur SW-Dist2
SW-Dist2(config)# interface range GigabitEthernet0/1-4
SW-Dist2(config-if-range)# ________________________________________________

! 3. Corriger le VLAN sur Gi0/4
(Vérifier qu'il n'y a pas de config VLAN sur l'interface physique — c'est Po1 qui doit la porter)
SW-Dist1(config)# interface GigabitEthernet0/4
SW-Dist1(config-if)# ________________________________________________
(supprimer toute config VLAN/trunk sur le membre individuel)
```

---

## 🏅 Barème global et grille Qualiopi

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Concepts EtherChannel | S2.1 | /20 | ≥ 11 |
| Ex. 2 — Protocoles et modes | S2.2 | /20 | ≥ 11 |
| Ex. 3 — Configuration IOS complète | C2.2 | /25 | ≥ 14 |
| Ex. 4 — Load balancing | S2.3 | /15 | ≥ 8 |
| Ex. 5 — Dépannage show ec summary | C2.3 | /20 | ≥ 11 |
| **TOTAL** | | **/100** | **≥ 55** |

> 📌 **Note Qualiopi** : Ce devoir constitue une preuve d'acquisition des compétences **S2.1, S2.2, S2.3, C2.2, C2.3** pour le dossier **E31**. Conserver avec signature enseignant et date.

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** : STP bloque 3 liens et laisse 1 actif → 1 Gbps effectif sur 4 Gbps théoriques

**1.b** :
1. Bande passante agrégée (4×1 Gbps = 4 Gbps)
2. Redondance intégrée (si un lien tombe → les autres continuent)
3. Compatibilité STP (STP voit Po1 comme un seul port, pas de blocage)

**1.c** :
- Sans EC : STP doit recalculer (30-50s), utilisateurs coupés
- Avec EC : les 3 liens restants continuent, EtherChannel ne reconverge pas (LACP reconfigure en ms), utilisateurs non impactés ou très brièvement (< 1s)

## Correction Exercice 2

**2.a** :

| Mode SW1 | Mode SW2 | EC formé | Protocole |
|---|---|---|---|
| active | active | ✓ | LACP |
| active | passive | ✓ | LACP |
| passive | passive | ✗ | — |
| on | on | ✓ | Aucun (static) |
| active | on | ✗ | Incompatible |
| desirable | auto | ✓ | PAgP |
| desirable | desirable | ✓ | PAgP |

**2.b** : active/active recommandé — les deux côtés négocient activement, plus robuste

**2.c** : LACP = standard IEEE 802.3ad / entre équipements hétérogènes · PAgP = propriétaire Cisco uniquement entre Cisco

## Correction Exercice 3

**3.a** Configuration SW-Dist1 :
```cisco
interface range GigabitEthernet0/1-4
  channel-group 1 mode active
  exit
interface port-channel 1
  switchport mode trunk
  switchport trunk allowed vlan all
  exit
port-channel load-balance src-dst-ip
```

**3.b** : Identique côté SW-Dist2 (même mode active, même config trunk sur Po1)

**3.c** : `show etherchannel summary` → attendu : `1 Po1(SU) LACP Gi0/1(P) Gi0/2(P) Gi0/3(P) Gi0/4(P)`

## Correction Exercice 5

**5.a** : S=Layer2 · D=down → Po1 est un port-channel L2 qui est DOWN → pas de trafic

**5.b** :

| Port | Problème | Fix |
|---|---|---|
| Gi0/1 (D) | Câble déconnecté ou interface shutdown | Rebrancher / no shutdown |
| Gi0/2 (D) | Même | Même |
| Gi0/3 (I) | Mode incompatible (probably on vs active) | Harmoniser les modes |
| Gi0/4 (s) | Config VLAN différente sur le membre physique | Supprimer config VLAN sur Gi0/4, la mettre sur Po1 |

**5.c** : active + on = incompatibles → Po1 ne peut pas se former. Fix : `channel-group 1 mode active` sur SW-Dist2

**5.d** :
```cisco
SW-Dist2(config)# interface range GigabitEthernet0/1-4
SW-Dist2(config-if-range)# channel-group 1 mode active

SW-Dist1(config)# interface GigabitEthernet0/4
SW-Dist1(config-if)# no switchport access vlan  (ou no switchport mode access)
```

---

*Devoir & Livrable Portfolio + Correction — Ne pas distribuer avant le rendu*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S13*
*Épreuve E31 | Compétences S2.1 · S2.2 · S2.3 · C2.2 · C2.3*
*Conforme référentiel Qualiopi*
