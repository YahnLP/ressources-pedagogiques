# 📘 FICHE MÉTHODE — S14 · 2ᵉ ANNÉE · E31
## Stratégie d'examen CCNA · Approche des labs Packet Tracer · Vérifications systématiques

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences visées** : C2.2 · C2.3 · C3.1 — Synthèse du parcours E31

> ℹ️ Cette fiche est un **guide de méthode**, pas un cours. Elle te donne les stratégies
> pour optimiser ton score en conditions d'examen. À mémoriser avant le E31 et le CCNA.

---

## 🎯 Comprendre le format CCNA 200-301

### L'examen en chiffres

```
Durée totale       : 120 minutes
Nombre de questions : 90 à 110 questions (variable)
Score minimum      : 825 / 1000 pour obtenir la certification
Types de questions :
  • QCM (1 bonne réponse)
  • QCM multiples (plusieurs bonnes réponses indiquées)
  • Drag-and-drop (faire correspondre / ordonner)
  • Simlet (lire des sorties de commandes et répondre)
  • Simulation Packet Tracer (configurer sur un vrai équipement virtuel)
Retour arrière     : NON possible une fois la question soumise
Pause              : non disponible
```

### Répartition du temps recommandée

```
Type de question        Temps recommandé   Proportion
QCM classique           60-90 sec          ~50% des questions
QCM avec analyse (simlet) 2-4 min           ~25% des questions
Simulation PT           10-15 min          ~25% du temps
```

---

## ⏱️ Stratégie de gestion du temps en lab PT

### La règle des 3 passes

```
PASSE 1 — Les "points faciles" (40% du temps alloué)
  → Adressage IP et passerelles → vérifier immédiatement avec ping
  → Interfaces UP (no shutdown)
  → VLANs créés et ports assignés
  → Lignes qui ne demandent qu'une ou deux commandes

PASSE 2 — Les configurations complexes (40% du temps)
  → OSPF (network, area, router-id)
  → EtherChannel (channel-group, port-channel trunk)
  → Routes statiques manquantes

PASSE 3 — Vérification et récupération (20% du temps)
  → Ping E2E systématique
  → show ip route sur chaque routeur
  → show etherchannel summary sur chaque switch
  → Corriger ce qui échoue
```

### Ne jamais rester bloqué

> Si une question te résiste depuis 3 minutes → **passer à la suivante**.
> Mieux vaut 28 configurations correctes sur 30 que 25 parfaites et 5 non abordées.
> Les points perdus sur une config à moitié faite sont souvent récupérables en revenant dessus.

---

## 🔁 La séquence de configuration universelle

### Pour tout nouveau lab — dans cet ordre

```
ÉTAPE 1 — Lire le cahier des charges EN ENTIER avant de taper quoi que ce soit
  → Identifier : adressage · VLANs · protocoles de routage · EtherChannel
  → Surligner les points qui comptent beaucoup de points

ÉTAPE 2 — Schéma rapide sur brouillon (2 minutes max)
  → Topologie · VLANs par port · liens trunk/access · routeurs

ÉTAPE 3 — Configurer couche par couche (bas vers haut)
  Couche 1 : no shutdown sur toutes les interfaces
  Couche 2 : VLANs → trunks → EtherChannel → STP check
  Couche 3 : adressage IP → routage statique → OSPF

ÉTAPE 4 — Vérifier après chaque bloc, pas seulement à la fin
  → Après les VLANs : show vlan brief
  → Après le trunk : show interfaces trunk
  → Après OSPF : show ip ospf neighbor
  → Après tout : ping E2E

ÉTAPE 5 — Sauvegarder (copy running-config startup-config)
```

---

## ✅ Les vérifications incontournables — par thème

### VLANs et trunks

```cisco
show vlan brief                       → VLANs créés + ports assignés
show interfaces trunk                 → liens trunk actifs + VLANs autorisés
show interfaces Gi0/1 switchport      → mode (access/trunk) + VLAN natif
ping [IP dans un autre VLAN]          → test inter-VLAN routing
```

### Routage statique et OSPF

```cisco
show ip route                         → table complète (C, S, O, S*)
show ip ospf neighbor                 → adjacences (état FULL ?)
show ip ospf interface                → coût, area, hello interval
ping [destination distante]           → test end-to-end
traceroute [destination]             → voir le chemin exact
```

### EtherChannel

```cisco
show etherchannel summary             → états (P/I/D/s) + protocole
show interfaces port-channel 1 trunk  → trunk sur Po1 ?
show lacp 1 neighbor                  → mode du voisin
ping [IP de l'autre côté]             → test à travers le bundle
```

### Sécurité de base

```cisco
show port-security interface Gi0/1    → statut + violations
show ip dhcp snooping binding          → entrées DHCP validées
show ip access-lists                   → compteurs hits sur les ACL
```

---

## 🎯 Les commandes les plus rentables (score/effort)

> Ces commandes apparaissent dans presque tous les sujets E31 et CCNA.
> Les maîtriser parfaitement = gagner des points facilement.

```
TOP 10 COMMANDES À CONNAÎTRE PAR CŒUR :

1.  ip address [IP] [MASQUE]                       → interface L3
2.  ip route [réseau] [masque] [next-hop]           → route statique
3.  router ospf [PID] / network [X] [wildcard] area [N] → OSPF
4.  switchport mode trunk                           → lien trunk
5.  switchport access vlan [N]                      → port access
6.  channel-group [N] mode active                   → EtherChannel LACP
7.  show ip route                                   → table de routage
8.  show etherchannel summary                       → état EC
9.  show ip ospf neighbor                           → adjacences OSPF
10. ping [IP] / traceroute [IP]                     → tests connectivité
```

---

## 🚨 Les 10 erreurs classiques qui font perdre des points

```
❌ Erreur 1 : Oublier `no shutdown` sur les interfaces
   → Interface en "administratively down" = rien ne passe
   Fix : toujours taper `no shutdown` après la config IP

❌ Erreur 2 : Masque en notation décimale dans OSPF (mettre le masque générique)
   → network 192.168.1.0 255.255.255.0 area 0  ← FAUX
   → network 192.168.1.0 0.0.0.255 area 0      ← CORRECT (wildcard)

❌ Erreur 3 : Config trunk sur Gi0/x au lieu de Po1 (EtherChannel)
   → La trunk doit aller sur port-channel, pas sur les membres

❌ Erreur 4 : Modes LACP incompatibles (active + on)
   → Toujours vérifier les modes des deux côtés

❌ Erreur 5 : Oublier la route retour
   → Si A→B fonctionne mais B→A non : route retour manquante

❌ Erreur 6 : OSPF sans `network` pour tous les réseaux
   → Chaque réseau à annoncer nécessite une ligne `network`

❌ Erreur 7 : VLAN trunk sans `switchport trunk allowed vlan`
   → Par défaut : tous les VLANs passent, mais si modifié, vérifier la liste

❌ Erreur 8 : Inter-VLAN routing sans sous-interfaces ou SVI
   → Sans `interface Gi0/0.10` et `encapsulation dot1Q 10`, pas de routage inter-VLAN

❌ Erreur 9 : Ne pas sauvegarder (copy run start)
   → En exam CCNA, la topologie peut être réinitialisée entre les questions

❌ Erreur 10 : Tester uniquement le ping "facile" (même switch, même VLAN)
   → Toujours tester le cas le plus difficile : PC d'un VLAN vers un serveur dans un autre VLAN
      et depuis l'autre côté d'un lien WAN
```

---

## 📊 Auto-évaluation par domaine — À remplir après chaque lab

> Coche ton niveau réel sur chaque thème (honnêteté requise) :

| Thème | Je configure sans aide | J'ai besoin de la fiche | Je dois revoir |
|---|---|---|---|
| Adressage IP / masques | ☐ | ☐ | ☐ |
| VLANs + trunks | ☐ | ☐ | ☐ |
| STP — lecture et dépannage | ☐ | ☐ | ☐ |
| Routes statiques + route par défaut | ☐ | ☐ | ☐ |
| OSPF — config + vérification | ☐ | ☐ | ☐ |
| EtherChannel LACP | ☐ | ☐ | ☐ |
| Lecture `show etherchannel summary` | ☐ | ☐ | ☐ |
| Inter-VLAN routing (Router-on-a-stick) | ☐ | ☐ | ☐ |
| Port Security | ☐ | ☐ | ☐ |
| ACL standard | ☐ | ☐ | ☐ |

---

## 🗓️ Plan de révision personnel (à remplir après S14)

```
Mes 3 points les plus forts (à conserver) :
  1. __________________________________________________________________________
  2. __________________________________________________________________________
  3. __________________________________________________________________________

Mes 3 points les plus faibles (à retravailler en priorité) :
  1. ______________________ → Revoir séance _______ · Exercice prioritaire : _______
  2. ______________________ → Revoir séance _______ · Exercice prioritaire : _______
  3. ______________________ → Revoir séance _______ · Exercice prioritaire : _______

Nombre de labs PT à refaire cette semaine : _______
Score cible au prochain QCM : _______ / 30
```

---

**🖼️ ILLUSTRATION 1**
> *Légende* : Diagramme circulaire de la répartition du temps CCNA 200-301 en 3 zones colorées. Zone externe : le cercle représente 120 minutes totales. Trois secteurs : "QCM classiques" (50% du temps, bleu), "Simlets/Analyse" (25%, orange), "Simulations PT" (25%, vert). En dessous, un axe temporel de lab PT en 3 phases annotées : Passe 1 "Points faciles" / Passe 2 "Config complexe" / Passe 3 "Vérification".
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

**🖼️ ILLUSTRATION 2**
> *Légende* : Checklist visuelle "Vérification après config" en 4 blocs thématiques côte à côte : VLANs (show vlan brief + show interfaces trunk), OSPF (show ip ospf neighbor + show ip route), EtherChannel (show etherchannel summary + codes P/I/D), Tests finaux (ping E2E + traceroute). Chaque bloc est une carte avec fond coloré, la commande en monospace et l'état "OK" attendu.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 📌 Les essentiels à retenir pour l'examen

> ✅ **Lire le sujet entier AVANT de commencer** — identifier les points les plus valorisés
> ✅ **Configurer couche par couche** : L1 (no shutdown) → L2 (VLAN/trunk/EC) → L3 (IP/routage)
> ✅ **Vérifier après chaque bloc** — ne pas attendre la fin pour tester
> ✅ **Si bloqué depuis 3 minutes → passer** et revenir
> ✅ Wildcard mask = inverse du masque réseau → `/24 = 0.0.0.255`
> ✅ `copy running-config startup-config` à la fin de chaque lab
> ✅ Les 10 commandes incontournables : les connaître parfaitement = points assurés

---

*Fiche Méthode — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S14*
*Synthèse compétences : C2.2 · C2.3 · C3.1 · S2.1 · S2.2 · S2.3 · S3.3*
