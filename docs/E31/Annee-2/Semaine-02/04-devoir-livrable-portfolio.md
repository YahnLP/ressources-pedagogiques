# 📝 DEVOIR & LIVRABLE PORTFOLIO — S2 · 2ᵉ ANNÉE · E31
## Routage statique · Table de routage · Diagnostic · Commandes IOS

---

> **Module** : E31 – Infrastructure Réseau · Routage statique
> **Épreuve visée** : **E31** – Épreuve pratique infrastructure réseau
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)
> **Format du rendu** : Fiche complétée (papier ou PDF scanné), commandes IOS écrites avec soin

---

## 📌 Compétences du référentiel évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S2.3** | Lire et interpréter une table de routage | /25 |
| **C2.2** | Écrire des commandes ip route correctes | /25 |
| **C2.3** | Diagnostiquer un dysfonctionnement de routage | /30 |
| **C3.1** | Rédiger un compte rendu d'intervention | /20 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation professionnelle

> Tu es **technicien CIEL** en charge de l'infrastructure réseau d'une PME.
>
> La PME dispose de 3 sites connectés par des liaisons WAN louées.
> Elle vient d'embaucher un stagiaire qui a commis des erreurs dans la configuration
> des routeurs du Site B.
>
> **Ta mission** :
> 1. Analyser les tables de routage fournies
> 2. Identifier les erreurs de configuration
> 3. Écrire les commandes correctives
> 4. Rédiger le compte rendu d'intervention

---

## 🅰️ PARTIE A — En classe (45 min)

### 🗺️ Topologie du réseau de la PME

```
  Site A                   Site B                   Site C
192.168.1.0/24           192.168.2.0/24           192.168.3.0/24
      │                        │                        │
   Gi0/0                    Gi0/0                    Gi0/0
  ┌──────┐  10.0.12.0/30   ┌──────┐  10.0.23.0/30   ┌──────┐
  │  RA  ├─Gi0/1─── Gi0/0 ─┤  RB  ├─Gi0/1───Gi0/0──┤  RC  │
  └──────┘                 └──────┘                  └──────┘

Adresses :
  RA Gi0/0 : 192.168.1.1     RA Gi0/1 : 10.0.12.1
  RB Gi0/0 : 10.0.12.2       RB Gi0/1 : 10.0.23.1
  RC Gi0/0 : 10.0.23.2       RC Gi0/1 : 192.168.3.1

Poste Site A : 192.168.1.50    Serveur Site C : 192.168.3.100
```

---

### 📋 Exercice 1 — Lire les tables de routage (/25)

> Tables de routage relevées après la configuration du stagiaire :

**RB — `show ip route`**

```
Codes: C - connected, S - static

C    10.0.12.0/30 is directly connected, GigabitEthernet0/0
C    10.0.23.0/30 is directly connected, GigabitEthernet0/1
C    192.168.2.0/24 is directly connected, GigabitEthernet1/0
S    192.168.1.0/24 [1/0] via 10.0.12.1
S    192.168.3.0/16 [1/0] via 10.0.23.2
```

**RC — `show ip route`**

```
Codes: C - connected, S - static

C    10.0.23.0/30 is directly connected, GigabitEthernet0/0
C    192.168.3.0/24 is directly connected, GigabitEthernet0/1
S    192.168.1.0/24 [1/0] via 10.0.23.1
S    192.168.2.0/24 [1/0] via 10.5.5.1
```

---

**1.a** — Sur RB, que signifie `[1/0]` dans l'entrée `S 192.168.1.0/24 [1/0] via 10.0.12.1` ? *(4 pts)*

```
[1/0] signifie : 1 = ________________________ · 0 = ________________________
Distance administrative 1 correspond à une route de type : ____________________
```

**1.b** — Identifie TOUTES les anomalies dans la table de routage de RB. *(6 pts)*

```
Anomalie 1 : Route vers _________________ a le masque /_____  au lieu de /_____
Anomalie 2 : ___________________________________________________________________
(Y a-t-il une route par défaut ? Est-ce un problème ici ? _______________________)
```

**1.c** — Dans la table de RC, la route `S 192.168.2.0/24 [1/0] via 10.5.5.1` : le next-hop `10.5.5.1` est-il correct ? Justifie en t'appuyant sur la topologie. *(5 pts)*

```
Pour atteindre 192.168.2.0/24 depuis RC, le paquet doit passer par : ___________
L'interface connectée à ce chemin sur le routeur voisin de RC est : _____________
Adresse correcte du next-hop : _______________
L'adresse 10.5.5.1 est-elle dans le réseau WAN23 (10.0.23.0/30) ? ☐ Oui ☐ Non
Type de panne : ________________________________________________________________
```

**1.d** — RA n'a pas été fourni mais on sait que le poste Site A (192.168.1.50) ne peut pas joindre le serveur Site C (192.168.3.100). En dehors des erreurs de RB et RC, quelle route MINIMALE doit posséder RA ? *(5 pts)*

```
RA doit avoir une route vers : ________________________________________________
Commande : ip route _________________ _________________ _________________
Pourquoi cette route est-elle suffisante (et non 2 routes) ? ___________________
______________________________________________________________________________
```

**1.e** — Pour quels réseaux RC n'a-t-il PAS besoin de route statique ? Pourquoi ? *(5 pts)*

```
RC n'a pas besoin de route vers : ____________________________________________
Car ces réseaux sont : ________________________________________________________
```

---

### ⌨️ Exercice 2 — Écrire les commandes correctives (/25)

**2.a** — Écris toutes les commandes nécessaires pour corriger la configuration de **RB** : *(10 pts)*

```
RB> enable
RB# configure terminal

(Corriger l'anomalie de masque)
RB(config)# no ip route _________________ _________________ _________________
RB(config)# ip route _________________ _________________ _________________

RB(config)# end
RB# show ip route
```

**2.b** — Écris toutes les commandes pour corriger la configuration de **RC** : *(10 pts)*

```
RC> enable
RC# configure terminal

(Corriger le next-hop injoignable)
RC(config)# no ip route _________________ _________________ _________________
RC(config)# ip route _________________ _________________ _________________

RC(config)# end
```

**2.c** — Après correction, quelles tables de routage complètes et correctes attends-tu sur RB et RC ? *(5 pts)*

**RB (après correction) :**

```
C    _________________________________  directly connected, ________________
C    _________________________________  directly connected, ________________
C    _________________________________  directly connected, ________________
S    _________________________________ [1/0] via _________________
S    _________________________________ [1/0] via _________________
```

**RC (après correction) :**

```
C    _________________________________  directly connected, ________________
C    _________________________________  directly connected, ________________
S    _________________________________ [1/0] via _________________
S    _________________________________ [1/0] via _________________
```

---

## 🅱️ PARTIE B — En autonomie (/30)

### 🔧 Exercice 3 — Diagnostic complet d'un nouveau scénario (/30)

> Un client signale que ses **PC du réseau 172.16.1.0/24** ne peuvent pas joindre le **serveur 10.10.10.0/24**.
> Tu as accès aux tables de routage de 2 routeurs.

**Topologie :**

```
172.16.1.0/24 ── R_BUREAU ── 192.168.100.0/30 ── R_SERVEUR ── 10.10.10.0/24
    PC_A : .10          .1               .2          .1              Srv : .50
```

**R_BUREAU — `show ip route`**

```
C    172.16.1.0/24 is directly connected, GigabitEthernet0/0
C    192.168.100.0/30 is directly connected, GigabitEthernet0/1
S    10.10.10.0/24 [1/0] via 192.168.100.2
S*   0.0.0.0/0 [1/0] via 192.168.101.1
```

**R_SERVEUR — `show ip route`**

```
C    192.168.100.0/30 is directly connected, GigabitEthernet0/0
C    10.10.10.0/24 is directly connected, GigabitEthernet0/1
```

---

**3.a** — PC_A fait un `ping 10.10.10.50`. Quel chemin le paquet emprunte-t-il ? S'arrête-t-il quelque part ? *(6 pts)*

```
PC_A (172.16.1.10) envoie vers 10.10.10.50
  → R_BUREAU cherche dans sa table : route trouvée ? ☐ Oui ☐ Non
    Route utilisée : _______________________________________________________
  → Next-hop = 192.168.100.2 = interface _________ de R_SERVEUR
  → R_SERVEUR reçoit le paquet, le délivre à 10.10.10.50
  
Paquet aller : ☐ OK jusqu'au serveur  ☐ Bloqué à ___________
```

**3.b** — Le serveur répond (paquet retour de 10.10.10.50 vers 172.16.1.10). R_SERVEUR a-t-il une route vers 172.16.1.0/24 ? *(5 pts)*

```
R_SERVEUR cherche une route vers 172.16.1.0/24 dans sa table : ☐ Trouvée ☐ ABSENT
Que fait R_SERVEUR avec le paquet de retour ? ________________________________
Type de panne : ______________________________________________________________
```

**3.c** — Quel est le résultat final du ping de PC_A vers 10.10.10.50 ? Explique le phénomène. *(4 pts)*

```
Résultat du ping côté PC_A : _________________________________________________
Phénomène (asymétrie aller/retour) : _________________________________________
___________________________________________________________________________
```

**3.d** — Sur R_BUREAU, une route par défaut `S* 0.0.0.0/0 via 192.168.101.1` est configurée. 
L'interface 192.168.101.x n'existe pas dans la topologie. Est-ce une panne ? Quel risque cela pose-t-il ? *(5 pts)*

```
Interface 192.168.101.1 existe dans la topologie ? ☐ Oui ☐ Non
La route par défaut est-elle active ? ☐ Oui ☐ Non (next-hop injoignable)
Risque : ___________________________________________________________________
```

**3.e** — Écris les commandes correctives complètes pour résoudre TOUTES les pannes du scénario 3 : *(10 pts)*

```
Sur R_SERVEUR :
R_SERVEUR(config)# ip route _________________ _________________ _________________

Sur R_BUREAU (corriger la route par défaut) :
R_BUREAU(config)# no ip route 0.0.0.0 0.0.0.0 _________________
R_BUREAU(config)# ip route 0.0.0.0 0.0.0.0 _________________
   (Quel est le bon next-hop pour la route par défaut de R_BUREAU ? ____________)
```

---

### 📝 Exercice 4 — Note de synthèse (/20)

> Rédige une **note de synthèse technique** de 10 à 12 lignes destinée au chef de projet.
>
> *"Quelles sont les 4 pannes de routage statique que tu as rencontrées cette semaine ? Pour chacune, explique comment elle se manifeste, comment tu la détectes et comment tu la corriges. Conclus sur pourquoi le routage dynamique (OSPF) sera préférable à grande échelle."*

```
Note de synthèse :

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
___________________________________________________________________________
___________________________________________________________________________
```

---

## 🏅 Barème global et grille Qualiopi

| Exercice | Compétences RNCP | Barème | Seuil de validation |
|---|---|---|---|
| Ex. 1 — Lecture et analyse des tables | S2.3 | /25 | ≥ 14/25 |
| Ex. 2 — Commandes correctives | C2.2 | /25 | ≥ 14/25 |
| Ex. 3 — Diagnostic scénario complet | C2.3 | /30 | ≥ 17/30 |
| Ex. 4 — Note de synthèse | C3.1 | /20 | ≥ 11/20 |
| **TOTAL** | | **/100** | **≥ 55/100** |

> 📌 **Note Qualiopi** : Ce devoir constitue une **preuve d'acquisition des compétences C2.2, C2.3, C3.1, S2.3** pour le dossier **E31**. Conserver avec signature enseignant et date.

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

---

## Correction Exercice 1

**1.a** : [1/0] → 1 = distance administrative (source statique) · 0 = métrique

**1.b** : Anomalies RB :
1. `S 192.168.3.0/16` → masque /16 au lieu de /24
2. Pas d'anomalie fonctionnelle sur la route vers 192.168.1.0/24 (correcte)

**1.c** : RC → 192.168.2.0/24 → doit passer par RB via le lien WAN23 → next-hop correct = R_B Gi0/1 = **10.0.23.1** · 10.5.5.1 n'est pas dans 10.0.23.0/30 → next-hop injoignable

**1.d** : RA doit avoir `ip route 192.168.3.0 255.255.255.0 10.0.12.2` — une seule route suffit car RA n'a pas besoin de connaître Site B pour transiter vers Site C (RB fera le relais)

**1.e** : RC n'a pas besoin de routes vers 10.0.23.0/30 ni 192.168.3.0/24 car ces réseaux sont **directement connectés**

---

## Correction Exercice 2

**2.a** :
```
RB(config)# no ip route 192.168.3.0 255.255.0.0 10.0.23.2
RB(config)# ip route 192.168.3.0 255.255.255.0 10.0.23.2
```

**2.b** :
```
RC(config)# no ip route 192.168.2.0 255.255.255.0 10.5.5.1
RC(config)# ip route 192.168.2.0 255.255.255.0 10.0.23.1
```

**2.c** : Tables complètes corrigées :

RB : C 10.0.12.0/30 · C 10.0.23.0/30 · C 192.168.2.0/24 · S 192.168.1.0/24 via 10.0.12.1 · S 192.168.3.0/24 via 10.0.23.2

RC : C 10.0.23.0/30 · C 192.168.3.0/24 · S 192.168.1.0/24 via 10.0.23.1 · S 192.168.2.0/24 via 10.0.23.1

---

## Correction Exercice 3

**3.a** : Paquet aller OK → R_BUREAU a une route vers 10.10.10.0/24 via 192.168.100.2 ✓

**3.b** : R_SERVEUR n'a PAS de route vers 172.16.1.0/24 → paquet de retour droppé → **asymétrie aller/retour**

**3.c** : PC_A reçoit des timeout (`....`) — le paquet part mais la réponse ne revient pas (R_SERVEUR drop le paquet retour)

**3.d** : 192.168.101.1 n'existe pas → route par défaut inactive (next-hop injoignable) · Risque : tout trafic vers des réseaux inconnus est perdu silencieusement

**3.e** :
```
R_SERVEUR(config)# ip route 172.16.1.0 255.255.255.0 192.168.100.1
R_BUREAU(config)# no ip route 0.0.0.0 0.0.0.0 192.168.101.1
R_BUREAU(config)# ip route 0.0.0.0 0.0.0.0 192.168.100.2
   (le bon next-hop = R_SERVEUR = 192.168.100.2 qui est le seul voisin)
```

---

## Éléments attendus Note de synthèse

1. **Route manquante** : aucune route → paquet droppé silencieusement · `show ip route` → réseau absent · `ip route [réseau] [masque] [nh]`
2. **Masque incorrect** : route présente mais inexacte → comportement imprévisible · Vérifier /notation et réseau réel · `no ip route` + corriger
3. **Next-hop injoignable** : route présente mais inactive · `ping [nh]` → timeout · Corriger l'adresse
4. **Asymétrie aller/retour** : ping marche dans un sens, pas l'autre · `traceroute` + `show ip route` sur chaque routeur · Ajouter route retour

Conclusion OSPF : sur 50+ routeurs, configurer manuellement toutes les routes = erreurs fréquentes, maintenance lourde, aucune récupération sur panne. OSPF propage automatiquement, converge en cas de panne, ne nécessite pas de maintenance manuelle des routes.

---

*Devoir & Livrable Portfolio + Correction — Ne pas distribuer avant le rendu*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S2*
*Épreuve E31 | Compétences C2.2 · C2.3 · C3.1 · S2.3*
*Conforme référentiel Qualiopi*
