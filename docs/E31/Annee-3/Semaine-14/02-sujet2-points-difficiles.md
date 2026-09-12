# 📋 SUJET 2 — POINTS DIFFICILES · S14 · 3ᵉ ANNÉE · E31
## Sujet Ciblé : BGP · ACL · Tunnel GRE · EtherChannel · Sous-réseau

---

> **⏱️ Durée : 55 minutes · Fiche de cours autorisée**
> **Objectif** : Maîtriser les 8 points où les copies perdent le plus de points
> **Nom** : ___________________________ **Groupe** : ___________________________

---

## 🎯 Mode d'emploi

> Ce sujet est conçu différemment : chaque question cible un piège spécifique.
> Après correction, tu sauras exactement **pourquoi** chaque réponse est juste ou fausse.

---

## 📐 THÈME 1 — Sous-réseau rapide (5 min)

> **Règle mnémotechnique** : `/24` part de `254h`. Chaque `/` supplémentaire divise par 2.
> `/25=126h · /26=62h · /27=30h · /28=14h · /29=6h · /30=2h`

**T1.a** — Calcule rapidement pour chaque réseau :

| Réseau | /? | Wildcard mask | Hôtes utilisables | Adresse de réseau pour 10.5.17.200 |
|---|---|---|---|---|
| 10.5.0.0 | /22 | | | |
| 192.168.50.0 | /27 | | | |
| 172.16.200.0 | /20 | | | |
| 10.0.0.0 | /30 | | | |

**T1.b** — L'adresse `10.5.17.200/22` appartient à quel sous-réseau ?

```
Astuce /22 : les 2 premiers octets + 2 bits du 3ème définissent le réseau.
/22 = masque 255.255.252.0 → le 3ème octet se lit par blocs de 4

10.5.17.200/22 :
  Bloc de 4 contenant 17 : les blocs sont 0, 4, 8, 12, 16, 20...
  17 est dans le bloc : ______ à ______
  Réseau : 10.5.______.0/22
```

---

## 🌐 THÈME 2 — BGP : sélection de chemin pièges (12 min)

> ⚠️ **Le piège le plus fréquent** : confondre le sens de Local-Pref et MED.

**T2.a** — Complète le tableau des attributs sans regarder tes notes :

| Attribut | Règle de préférence | Contrôle | Propagé à |
|---|---|---|---|
| Local-Pref (défaut=100) | + _______ = préféré | Sortie de l'AS | iBGP uniquement |
| MED (défaut=0) | + _______ = préféré | Entrée AS voisin | AS voisin direct |
| AS-path | + _______ = préféré | Transit | Tout le monde |

**T2.b** — Un routeur reçoit 4 chemins vers `8.8.8.0/24` :

```
Chemin A : via 10.0.1.2  · LocPrf=100 · MED=0   · AS-path="3215 15169"
Chemin B : via 10.0.2.2  · LocPrf=100 · MED=50  · AS-path="5511 15169"
Chemin C : via 10.0.3.2  · LocPrf=150 · MED=0   · AS-path="1299 15169"
Chemin D : via 10.0.4.2  · LocPrf=150 · MED=100 · AS-path="1299 15169"
```

Applique l'algorithme étape par étape et indique le chemin gagnant :

```
ÉTAPE 1 — Local-Pref (+ haut = préféré) :
  Valeurs : A=___ B=___ C=___ D=___
  Chemins éliminés : _____ et _____  (LocPrf trop basse)
  Chemins restants : _____ et _____

ÉTAPE 2 — AS-path length (+ court = préféré) :
  Chemin C : longueur = _____  Chemin D : longueur = _____
  Chemins identiques → continuer

ÉTAPE 3 — MED (+ bas = préféré) :
  Chemin C : MED = _____  Chemin D : MED = _____
  GAGNANT : Chemin _____

RÉPONSE FINALE : _____ car _______________________________________________
```

**T2.c** — L'admin veut que les paquets ENTRANT dans son AS arrivent par le lien C (10.0.3.2).
Quel attribut utilise-t-il et que doit-il annoncer au FAI sur ce lien ?

```
Attribut : ___________________________
Valeur à annoncer sur lien C : _____ (vs lien D : _____)
Règle : plus _______ = ce lien sera préféré par le FAI pour entrer dans notre AS
```

---

## 🛡️ THÈME 3 — ACL : le placement et le deny implicite (12 min)

> ⚠️ **Les 3 règles absolues des ACL** :
> 1. Standard → filtre IP SOURCE seulement → placer PRÈS de la DESTINATION
> 2. Étendue → filtre src+dst+port → placer PRÈS de la SOURCE
> 3. Deny implicite en fin → TOUJOURS ajouter `permit ip any any` si besoin

**T3.a** — Pour chaque scénario, indique : le type d'ACL à utiliser, l'interface et la direction.

```
Scénario 1 : Bloquer l'accès Telnet (port 23) de LAN (10.0.1.0/24) vers les serveurs
  Type ACL : ☐ Standard ☐ Étendue   Numérotation : _______ (standard) ou _______ (étendue)
  Interface recommandée : _____________________  Direction : _______
  Pourquoi cette interface ? ___________________________________________________

Scénario 2 : Interdire à un seul PC (10.0.2.50) d'accéder au réseau Serveurs (10.0.3.0/24)
  Type ACL : ☐ Standard ☐ Étendue
  Interface et direction : _______________________
  Pourquoi ACL standard ici (pas étendue) ? ___________________________________

Scénario 3 : Autoriser seulement HTTPS (443) depuis l'Agence (192.168.5.0/24)
             vers le serveur Web (192.168.1.10)
  Type ACL : ☐ Standard ☐ Étendue
  Écrire l'ACL complète (2 règles minimum) :
    ip access-list extended WEB_AGENCE
      _______________________________________________________________________
      _______________________________________________________________________
```

**T3.b** — Identifie le problème dans cette ACL et corrige-la :

```
Situation : Les PC du LAN ne peuvent plus rien faire depuis qu'on a appliqué cette ACL.

access-list 105 deny tcp 192.168.1.0 0.0.0.255 host 10.0.5.20 eq 23
(appliquée en in sur l'interface LAN)

Problème : ___________________________________________________________________
Correction à ajouter : _______________________________________________________
```

**T3.c** — Une ACL est appliquée sur une interface mais ne bloque rien.
La commande `show ip access-lists` montre **0 paquets** sur toutes les règles.
Cite 2 raisons possibles :

```
Raison 1 : ___________________________________________________________________
Raison 2 : ___________________________________________________________________
```

---

## 🔒 THÈME 4 — Tunnel GRE : l'inversion source/destination (8 min)

> ⚠️ **L'erreur la plus répandue** : configurer la même IP source et destination sur les deux routeurs.

**T4.a** — Voici une configuration défaillante. Identifie et corrige l'erreur :

```cisco
! Adresses WAN : R1=203.0.113.1 · R2=198.51.100.1

! Sur R1 :
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source 203.0.113.1
 tunnel destination 198.51.100.1    ← correcte ou incorrecte ?
 no shutdown

! Sur R2 :
interface Tunnel0
 ip address 172.16.0.2 255.255.255.252
 tunnel source 203.0.113.1          ← correcte ou incorrecte ?
 tunnel destination 198.51.100.1
 no shutdown
```

```
Erreur sur R2 :
  Problème : tunnel source = ________ (IP de R1 !)
  Correction : tunnel source = ________ (doit être l'IP WAN de ________)
  Correction complète de R2 :
    tunnel source _______________
    tunnel destination _______________

Règle à retenir : Sur R2, la SOURCE = IP WAN de ___ et la DESTINATION = IP WAN de ___
```

**T4.b** — Après correction, le tunnel reste en état `up, line protocol down`.
Quelle est la cause probable ?

```
"up" (plan physique) signifie : ______________________________________________
"line protocol down" signifie : ______________________________________________
Cause probable ici : _________________________________________________________
Commande pour vérifier : _____________________________________________________
```

---

## ⚡ THÈME 5 — EtherChannel : modes et états (8 min)

> ⚠️ **Le piège classique** : confondre les modes qui forment un EC et ceux qui échouent.

**T5.a** — Complète le tableau avec ✓ (EC formé) ou ✗ (EC impossible) :

| SW-A mode | SW-B mode | EC formé ? | Raison |
|---|---|---|---|
| active | active | | |
| active | passive | | |
| passive | passive | | |
| active | on | | |
| on | on | | |
| desirable | auto | | PAgP |
| desirable | on | | PAgP |

**T5.b** — Dans `show etherchannel summary`, un port est en état `(s)` (suspended).
Qu'est-ce que cela signifie et quelle est la cause probable ?

```
(s) = ________________________________________________________________________
Cause probable : ______________________________________________________________
Commande pour diagnostiquer : _________________________________________________
```

**T5.c** — Un admin a configuré le trunk sur l'interface physique Gi0/1 au lieu du port-channel.
Quel problème cela cause-t-il ?

```
Problème : ___________________________________________________________________
Correction : _________________________________________________________________
Règle : Toujours configurer le trunk sur l'interface _________________, pas sur les membres physiques
```

---

## 🔄 THÈME 6 — OSPF : passive-interface et wildcard (10 min)

**T6.a** — Deux configs OSPF en concurrence. Laquelle est correcte et pourquoi ?

```
Config X :
  router ospf 1
   router-id 1.1.1.1
   network 192.168.10.0 255.255.255.0 area 0
   network 10.0.1.0 255.255.255.252 area 0

Config Y :
  router ospf 1
   router-id 1.1.1.1
   network 192.168.10.0 0.0.0.255 area 0
   network 10.0.1.0 0.0.0.3 area 0
   passive-interface GigabitEthernet0/0
```

```
Config correcte : ☐ X ☐ Y  (et les deux ont des problèmes → les décrire)

Problème(s) dans Config X :
  1. ________________________________________________________________________
  
Problème(s) dans Config Y (s'il y en a) :
  ___________________________________________________________________________ ← Aucun !

Explication passive-interface GigabitEthernet0/0 dans Config Y :
  → Cette interface est côté ___________________________ (LAN ou WAN ?)
  → Sans passive-interface : _________________________________________________
  → Avec passive-interface : _________________________________________________
```

**T6.b** — Convertis ces masques en wildcards rapidement :

```
/24 → _______________   /26 → _______________   /30 → _______________
/20 → _______________   /22 → _______________   /28 → _______________
/32 → _______________   /16 → _______________   /27 → _______________

Méthode : wildcard = 255.255.255.255 - masque réseau
  Exemple /26 : 255.255.255.255 - 255.255.255.192 = 0.0.0.63
```

---

## 📊 Auto-évaluation et Score

| Thème | /pts | Score |
|---|---|---|
| T1 — Sous-réseau | /8 | |
| T2 — BGP attributs + sélection | /15 | |
| T3 — ACL placement + dépannage | /15 | |
| T4 — Tunnel GRE | /10 | |
| T5 — EtherChannel | /10 | |
| T6 — OSPF passive + wildcard | /12 | |
| **TOTAL** | **/70** | |

```
Mon score : ___/70 = ____%

Points perdus sur quel(s) thème(s) :
1. ___________________________________
2. ___________________________________

Ma priorité de révision pour l'E31 :
___________________________________________
```

---

---

# ✅ CORRECTION COMMENTÉE SUJET 2 — Document enseignant uniquement

## T1 — Sous-réseau

```
10.5.0.0/22    : wildcard=0.0.3.255 · hôtes=1022 · réseau pour .17.200 = 10.5.16.0/22
                 (blocs de /22 : 0,4,8,12,16,20... → 17 est dans 16-19 → réseau 10.5.16.0)
192.168.50.0/27: wildcard=0.0.0.31 · hôtes=30
172.16.200.0/20: wildcard=0.0.15.255 · hôtes=4094
10.0.0.0/30    : wildcard=0.0.0.3 · hôtes=2

⚠️ Point pédagogique /22 : blocs de 4 sur le 3ème octet.
   10.5.17.200 → 17 div 4 = 4, reste 1 → bloc commence à 16 → réseau 10.5.16.0/22
```

## T2 — BGP attributs

```
Tableau : Local-Pref + haut · MED + bas · AS-path + court

T2.b : Étapes :
  1. Local-Pref : A=100, B=100 éliminés (< 150) · Restent C et D
  2. AS-path C="1299 15169"=2 · D="1299 15169"=2 → identiques
  3. MED : C=0, D=100 → C gagne (0 < 100 → MED PLUS BAS = préféré)
  GAGNANT : Chemin C

⚠️ Piège : beaucoup confondent MED "plus bas = préféré" avec Local-Pref "plus haut = préféré"
   Moyen mnémotechnique : Local-Pref = "je PRÉFÈRE partir par là" → plus haut
                          MED = "je suggère d'ÉVITER ce lien" → plus bas = moins évité

T2.c : MED (suggestion d'entrée) · annoncer MED=10 sur lien C vs MED=100 sur lien D
       (plus bas = préféré pour entrer dans notre AS)
```

## T3 — ACL

```
T3.a Scénario 1 :
  Type = Étendue (100-199) car filtre destination port 23
  Interface = LAN (Gi0/0) en in → près de la source
  Pourquoi : filtrage dès la source, économise la bande passante intermédiaire

Scénario 2 :
  Type = Standard OU étendue (les deux peuvent fonctionner)
  Standard acceptable si on filtre juste le PC → placer près de la destination (Gi0/0.serveurs)

Scénario 3 :
  ip access-list extended WEB_AGENCE
    permit tcp 192.168.5.0 0.0.0.255 host 192.168.1.10 eq 443
    deny ip 192.168.5.0 0.0.0.255 host 192.168.1.10
    (permit ip any any à ajouter si d'autres flux doivent passer)

T3.b :
  Problème : L'ACL bloque Telnet vers 10.0.5.20 mais le deny implicite bloque TOUT le reste
  Correction : access-list 105 permit ip any any  (après la règle deny)

T3.c :
  Raison 1 : L'ACL est appliquée sur la mauvaise interface ou dans la mauvaise direction
  Raison 2 : Le trafic testé ne correspond pas aux règles (mauvaise IP source/destination/port)
  (Raison 3 bonus : l'ACL n'est pas appliquée du tout - show run interface pour vérifier)
```

## T4 — Tunnel GRE

```
Erreur R2 : tunnel source 203.0.113.1 → c'est l'IP de R1, pas de R2 !
  Correction :
    tunnel source 198.51.100.1     ← IP WAN de R2
    tunnel destination 203.0.113.1 ← IP WAN de R1

Règle : Sur Rx, SOURCE = IP WAN de Rx · DESTINATION = IP WAN de Ry

T4.b "up, line protocol down" :
  "up" = interface physique WAN sous-jacente est up (câble, couche physique OK)
  "line protocol down" = le tunnel CAPWAP/GRE en lui-même ne peut pas établir l'encapsulation
  Cause probable : le routing vers la destination du tunnel est absent (pas de route vers 198.51.100.1)
  OU les configs source/destination ne sont pas symétriques
  Commande : show ip route 198.51.100.1 → la route existe-t-elle ?
```

## T5 — EtherChannel

```
active + active   ✓   (LACP, les deux initient)
active + passive  ✓   (LACP, l'un initie, l'autre répond)
passive + passive ✗   (personne n'initie → jamais formé)
active + on       ✗   (active attend réponse LACP · on = statique sans LACP → incompatible)
on + on           ✓   (statique forçé, risque de boucle STP si non coordonné)
desirable + auto  ✓   (PAgP)
desirable + on    ✗   (PAgP attend négociation · on = statique → incompatible)

(s) suspended = config incompatible entre les ports membres (VLAN, mode trunk différent)
Commande : show etherchannel detail → voir les détails de la discordance

Trunk sur membre physique :
  Problème : la config trunk est écrasée/ignorée par EtherChannel qui gère le logique au niveau Po
  Correction : déplacer les commandes switchport mode trunk et allowed vlan sur interface port-channel X
```

## T6 — OSPF

```
Config X incorrecte : masques réseaux au lieu de wildcards
Config Y correcte : wildcards + passive-interface

Wildcards :
/24=0.0.0.255  /26=0.0.0.63   /30=0.0.0.3
/20=0.0.15.255 /22=0.0.3.255  /28=0.0.0.15
/32=0.0.0.0    /16=0.255.255.255 /27=0.0.0.31

passive-interface Gi0/0 (côté LAN) :
  Sans : OSPF envoie des Hello vers les PCs → inutile, consomme CPU/BW, voisinage non désiré possible
  Avec : aucun Hello envoyé sur cette interface → sécurité + performance
```

---

*Sujet 2 Points Difficiles + Correction Commentée — BAC PRO CIEL | E31 | 3ᵉ année S14*
