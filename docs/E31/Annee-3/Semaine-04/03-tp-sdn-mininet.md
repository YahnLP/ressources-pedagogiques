# 🔬 TRAVAUX PRATIQUES — S4 · 3ᵉ ANNÉE · E31
## SDN avec Mininet : Topologies · Flow Tables · Politiques de Forwarding

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **VM Linux + Mininet**
> **Prérequis** : Mininet installé et fonctionnel (`sudo mn --test pingall` → 0% dropped)
> **Épreuve ciblée** : **E31** – Administration systèmes · CCNA Automation

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S6.1** | Observer la séparation plan contrôle / données |
| **S6.2** | Lire et analyser une flow table OpenFlow |
| **C2.2** | Utiliser les commandes Mininet et Open vSwitch |
| **C3.1** | Documenter une architecture SDN |

---

## 🟢 NIVEAU 1 — Première topologie et ping (10 min)

**1.1** — Lance Mininet avec une topologie minimale :

```bash
$ sudo mn
```

**1.2** — Dans le CLI Mininet, affiche les informations sur les nœuds :

```
mininet> dump
```

```
Recopie la sortie :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

Nombre d'hôtes : _______   Nombre de switches : _______
```

**1.3** — Affiche la topologie des liens :

```
mininet> net
```

```
Recopie :
___________________________________________________________________________
```

**1.4** — Teste la connectivité entre tous les hôtes :

```
mininet> pingall
```

```
Résultat : ☐ 0% dropped (tout fonctionne) ☐ ___ % dropped
Hôtes présents : ☐ h1 ☐ h2 ☐ h3 ☐ h4
```

**1.5** — Depuis h1, affiche la configuration réseau :

```
mininet> h1 ifconfig
```

```
Adresse IP de h1 : _______________________
Interface : _______________________________
```

---

## 🟡 NIVEAU 2 — Explorer les flow tables (20 min)

> **Concept clé** : Sans contrôleur externe, Open vSwitch utilise un comportement par défaut (learning switch). Observe les règles générées automatiquement.

**2.1** — Affiche les flow tables du switch s1 AVANT tout ping :

```
mininet> sh ovs-ofctl dump-flows s1
```

```
Nombre de règles : _______
Si aucune règle : c'est normal — les tables sont vides au démarrage
```

**2.2** — Lance un ping de h1 vers h2 :

```
mininet> h1 ping -c 3 h2
```

**2.3** — Affiche les flow tables APRÈS le ping :

```
mininet> sh ovs-ofctl dump-flows s1
```

```
Recopie les règles créées :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**2.4** — Analyse les règles :

```
Règle 1 :
  Correspond à (match) : ___________________________________________________
  Action : _______________________________________________________________
  Nombre de paquets traités (n_packets) : _______

Règle 2 (trafic de retour) :
  Correspond à : ___________________________________________________________
  Action : _______________________________________________________________
```

**2.5** — Qu'est-ce qui a créé ces règles ? (Rappel : comportement par défaut d'OVS)

```
Sans contrôleur externe, Open vSwitch fonctionne comme un : __________________
Les règles ont été créées : ☐ manuellement ☐ automatiquement par OVS (learning)
```

**2.6** — Attends 10-15 secondes puis vérifie à nouveau les flow tables :

```
mininet> sh ovs-ofctl dump-flows s1
```

```
Les règles ont-elles disparu ? ☐ Oui ☐ Non
Cela s'explique par : le paramètre __________________ (expiration de règle)
```

---

## 🟠 NIVEAU 3 — Topologies avancées et connectivité (20 min)

**3.1** — Quitte Mininet et crée une topologie **linéaire** de 3 switches :

```bash
mininet> exit
$ sudo mn --topo linear,3
```

**3.2** — Dessine la topologie en complétant le schéma :

```
h1 ─── [  ] ─── [  ] ─── [  ] ─── h2
       s___       s___      s___

Adresses IP :
  h1 : ___________________
  h2 : ___________________
```

**3.3** — Lance `pingall` et note le résultat :

```
mininet> pingall
Résultat : _______% dropped
```

**3.4** — Affiche les flow tables de s1, s2 et s3 après le ping :

```
mininet> sh ovs-ofctl dump-flows s1
mininet> sh ovs-ofctl dump-flows s2
mininet> sh ovs-ofctl dump-flows s3
```

```
Chaque switch a-t-il ses propres règles ? ☐ Oui ☐ Non
Cela illustre le principe : ___________________________________________________
```

**3.5** — Crée maintenant une topologie en arbre :

```bash
mininet> exit
$ sudo mn --topo tree,2,2
```

```
Décris la topologie (nombre d'hôtes, switches, structure) :
___________________________________________________________________________
Adresses attribuées aux hôtes (h1 à h4) : ____________________________________
pingall → résultat : _______% dropped
```

---

## 🔵 NIVEAU 4 — Installer une règle manuellement (15 min)

> **Objectif** : Simuler ce que ferait un contrôleur SDN — installer des règles manuellement dans les flow tables.

**4.1** — Lance une topologie simple et **bloque** tout le trafic par défaut :

```bash
$ sudo mn --topo single,2 --controller none
```

> Le paramètre `--controller none` simule l'absence de contrôleur.

**4.2** — Vérifie que les pings échouent :

```
mininet> h1 ping -c 2 h2
```

```
Résultat : ☐ Succès ☐ Échec (normal — aucune règle de forwarding)
```

**4.3** — Installe manuellement les règles pour permettre à h1 de pinguer h2 :

> D'abord, trouve les numéros de ports :

```
mininet> sh ovs-ofctl show s1
```

```
Port h1 connecté sur port n° : _______
Port h2 connecté sur port n° : _______
```

```bash
# Règle : si paquet reçu sur port de h1 → envoyer sur port de h2
mininet> sh ovs-ofctl add-flow s1 in_port=1,actions=output:2

# Règle de retour : si paquet reçu sur port de h2 → envoyer sur port de h1
mininet> sh ovs-ofctl add-flow s1 in_port=2,actions=output:1
```

**4.4** — Teste à nouveau :

```
mininet> h1 ping -c 3 h2
```

```
Résultat : ☐ Succès ☐ Échec
```

**4.5** — Vérifie les règles installées :

```
mininet> sh ovs-ofctl dump-flows s1
```

```
Ces règles ont été installées : ☐ manuellement ☐ automatiquement
C'est exactement ce que ferait : ☐ un routeur OSPF ☐ un contrôleur SDN via Flow-Mod
```

**4.6** — Maintenant, installe une règle de **DROP** pour h1 → h2 avec priorité plus haute :

```bash
mininet> sh ovs-ofctl add-flow s1 priority=100,in_port=1,actions=drop
```

```
mininet> h1 ping -c 2 h2
Résultat : ☐ Succès ☐ Échec (la règle DROP prend la priorité)
```

**Question 4.7** — Explique pourquoi la règle DROP prend le dessus sur la règle forward :

```
La règle DROP a une priorité de : _______
La règle forward a une priorité de : _______
Dans les flow tables OpenFlow, la règle avec la priorité : ☐ la plus basse ☐ la plus haute
est évaluée en premier → elle "gagne"
```

---

## 🔴 NIVEAU 5 — Architecture SDN complète et documentation (15 min)

**5.1** — Crée une topologie personnalisée en Python :

```bash
# Quitter Mininet d'abord
mininet> exit

# Créer le fichier de topologie
$ nano custom_topo.py
```

Contenu du fichier :

```python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel

class CustomTopo(Topo):
    def build(self):
        # Créer 2 switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        
        # Créer 4 hôtes
        h1 = self.addHost('h1', ip='192.168.1.1/24')
        h2 = self.addHost('h2', ip='192.168.1.2/24')
        h3 = self.addHost('h3', ip='192.168.2.1/24')
        h4 = self.addHost('h4', ip='192.168.2.2/24')
        
        # Connecter h1, h2 à s1 | h3, h4 à s2 | s1 ─── s2
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(s1, s2)

topos = {'custom': CustomTopo}
```

```bash
$ sudo mn --custom custom_topo.py --topo custom
```

**5.2** — Dessine le schéma de cette topologie en annotant les adresses IP :

```
┌──────────────────────────────────────────────────────────────┐
│  Dessine le schéma complet avec h1, h2, s1, s2, h3, h4     │
│  et les adresses IP sur chaque hôte                         │
│                                                              │
│                                                              │
│                                                              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**5.3** — Teste la connectivité :

```
mininet> pingall
```

```
h1 peut pinguer h2 ? ☐ Oui ☐ Non    (même switch s1)
h1 peut pinguer h3 ? ☐ Oui ☐ Non    (switches différents)
h3 peut pinguer h4 ? ☐ Oui ☐ Non    (même switch s2)
```

**5.4** — Réflexion : dans une vraie architecture SDN avec contrôleur, comment empêcherait-on la communication entre le VLAN 192.168.1.0/24 et le VLAN 192.168.2.0/24 ?

```
Dans un réseau traditionnel : utiliser des ____________________________________
Dans SDN avec contrôleur : écrire une règle de type ___________________________
  match=ip,nw_src=192.168.1.0/24,nw_dst=192.168.2.0/24 → actions=drop
Avantage SDN : cette règle est déployée sur ___________________________________ switch(es)
              en une seule commande au lieu de ________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Lancer Mininet et créer une topologie de base | ☐ | ☐ | ☐ |
| Afficher et lire les flow tables (`ovs-ofctl dump-flows`) | ☐ | ☐ | ☐ |
| Installer manuellement une règle de forwarding | ☐ | ☐ | ☐ |
| Comprendre le rôle de la priorité dans les flow tables | ☐ | ☐ | ☐ |
| Expliquer la séparation plan contrôle / données | ☐ | ☐ | ☐ |
| Créer une topologie personnalisée en Python | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.1-2 — Topologie lancée, flow tables lues et analysées | /7 |
| Niv.3 — Topologies linéaire et arbre explorées | /5 |
| Niv.4 — Règle manuelle installée, DROP testé avec priorité | /8 |
| Niv.5 — Topologie Python créée, schéma annoté | /5 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 2

```
Sans contrôleur, OVS fonctionne comme un "learning switch" :
  - Premier paquet → OVS apprend l'adresse MAC src et son port
  - Flood sur tous les ports si destination inconnue
  - Installe une règle quand la destination est connue
  - Les règles ont un idle_timeout de 60s (expiration si inactif)

Les flow tables après le ping contiendront des règles du type :
  priority=0, table=0 → NORMAL (comportement learning)
  ou des règles spécifiques pour les adresses MAC échangées
```

## Correction Niveau 4

```
Règle forward : priority=0 (ou non spécifié = 0 par défaut)
Règle DROP    : priority=100

OpenFlow évalue les règles par ordre décroissant de priorité :
100 > 0 → la règle DROP est évaluée en premier → elle s'applique

Pour retirer la règle DROP et restaurer le forwarding :
mininet> sh ovs-ofctl del-flows s1 in_port=1
(ou del-flows s1 priority=100,in_port=1)
```

## Correction Niveau 5

```
Topologie custom_topo.py :
  h1 (192.168.1.1) ─┬─ s1 ─── s2 ─┬─ h3 (192.168.2.1)
  h2 (192.168.1.2) ─┘              └─ h4 (192.168.2.2)

pingall résultats :
  h1↔h2 = même switch s1 → OK (OVS learning)
  h3↔h4 = même switch s2 → OK
  h1↔h3 = inter-switches → OK (OVS flood et apprentissage)

5.4 : SDN = règle drop installée sur s1 et s2 simultanément via 1 commande contrôleur
       vs traditionnel = ACL sur chaque switch manuellement
```

---

*TP SDN Mininet + Correction — BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S4*
*Document Portfolio E31 — Compétences S6.1 · S6.2 · C2.2 · C3.1*
