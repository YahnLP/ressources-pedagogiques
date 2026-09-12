# 📝 DEVOIR & LIVRABLE PORTFOLIO — S12 · 3ᵉ ANNÉE · E31
## Révisions (2) : BGP · ACL · VPN · Firewall · Routage Avancé + Sécurité

---

> **Module** : E31 – Infrastructure Réseau — Routage avancé + Sécurité
> **Épreuve visée** : **E31** · **E32** (sécurité) · CCNP ENARSI
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 55 min)

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S2.4 / S2.5** | BGP — AS, eBGP/iBGP, attributs, sélection chemin | /30 |
| **S5.1** | ACL — standard, étendue, nommée, placement | /25 |
| **S5.2** | VPN — GRE, IPsec, tunnel site-à-site | /25 |
| **S5.3** | Firewall — ZPF, stateful inspection, politiques | /20 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation

> **NETSERV SA** est un opérateur réseau régional qui gère 3 sites pour un client grand compte.
> En tant qu'administrateur réseau senior, tu dois :
> — Sécuriser les interconnexions inter-sites
> — Filtrer le trafic selon une politique de sécurité stricte
> — Configurer un VPN entre le siège et l'agence distante
> — Expliquer le choix de firewall à la direction technique

---

## 🅰️ PARTIE A — En classe (45 min)

### 🌐 Exercice 1 — BGP : analyse et sélection de chemin (/30)

**1.a** — Voici la table BGP du routeur de bordure de NETSERV :

```
BGP router identifier 10.10.10.10, local AS number 64513

   Network          Next Hop     Metric  LocPrf  Weight  Path
*> 192.168.0.0/24   0.0.0.0           0          32768  i
*  203.0.113.0/24   10.0.1.2          0      80       0  3215 i
*> 203.0.113.0/24   10.0.2.2          0     120       0  5511 i
*  198.51.100.0/24  10.0.1.2         30     120       0  3215 i
*> 198.51.100.0/24  10.0.2.2          0     120       0  5511 i
   172.20.0.0/16    10.0.1.2                      0  3215 1234 i
```

**Q1.a.1** — Pour `203.0.113.0/24`, quel chemin BGP a été choisi ? Justifie avec l'étape de l'algorithme : *(6 pts)*

```
Chemin choisi : via _______________________
Étape décisive de l'algorithme : ___________________________________________
Valeur déterminante : via 10.0.1.2 = _______  vs  via 10.0.2.2 = _______
Règle appliquée : _________________________________________________________
```

**Q1.a.2** — Pour `198.51.100.0/24`, les deux chemins ont `LocPrf=120`. Quel critère départage-t-il ? *(6 pts)*

```
Critère suivant dans l'algorithme : ________________________________________
Via 10.0.1.2 : Metric = _______    Via 10.0.2.2 : Metric = _______
Chemin choisi : _____________________
Règle : plus _______ = préféré pour ce critère
```

**Q1.a.3** — La route `172.20.0.0/16` n'a ni `*` ni `>`. Qu'est-ce que cela signifie ? Cite une cause probable. *(6 pts)*

```
Absence de `*` signifie : ___________________________________________________
Cause probable la plus fréquente : __________________________________________
Commande pour diagnostiquer : _______________________________________________
```

**Q1.a.4** — L'admin veut que NETSERV sorte **toujours** via le FAI 5511 (10.0.2.2) pour tous les préfixes, même si 3215 a un meilleur chemin. Quel attribut modifier, avec quelle valeur ? *(6 pts)*

```
Attribut à utiliser : ______________________________________________________
Valeur à appliquer sur les routes reçues de 10.0.2.2 : _______  (vs valeur actuelle pour 10.0.1.2)
Règle : plus _______ = préféré
Commande route-map :

route-map PREFER_5511 permit 10
 ___________________________________________________________________________

router bgp 64513
 neighbor 10.0.2.2 route-map __________________ __
```

**Q1.a.5** — Quelle est la différence fondamentale entre **eBGP** et **iBGP** concernant la modification de l'AS-path ? *(6 pts)*

```
eBGP : lorsqu'un routeur envoie une route à un voisin eBGP, il __________________
      → L'AS-path de "200 300" devient _______ après passage par AS 100

iBGP : lorsqu'un routeur envoie une route à un voisin iBGP, l'AS-path est _______
      Raison : _______________________________________________________________

Conséquence importante (split horizon iBGP) : _________________________________
```

---

### 🛡️ Exercice 2 — ACL : écriture et analyse (/25)

> **Politique de sécurité NETSERV** :
> - LAN Siège (192.168.10.0/24) → peut accéder à tout SAUF Telnet vers DMZ
> - LAN Agence (192.168.20.0/24) → accès UNIQUEMENT HTTP et HTTPS vers les serveurs DMZ (192.168.100.0/24)
> - Internet (any) → accès interdit vers LAN Siège · HTTPS (443) autorisé vers SRV_WEB DMZ (192.168.100.10)

**Q2.a** — Écris l'ACL étendue nommée pour le LAN Siège sur R_Siege (interface Gi0/0, trafic **entrant** depuis le LAN) : *(10 pts)*

```cisco
ip access-list extended POLITIQUE_SIEGE
  ! Bloquer Telnet vers la DMZ
  _________________________________________________________________________
  ! Autoriser tout le reste du LAN Siège
  _________________________________________________________________________

interface GigabitEthernet0/0
  ip access-group ______________________ ______
```

**Q2.b** — Écris l'ACL pour LAN Agence sur R_Agence (interface Gi0/0, trafic entrant) : *(8 pts)*

```cisco
ip access-list extended POLITIQUE_AGENCE
  ! Autoriser HTTP vers DMZ seulement
  _________________________________________________________________________
  ! Autoriser HTTPS vers DMZ seulement
  _________________________________________________________________________
  ! Bloquer tout le reste
  _________________________________________________________________________

interface GigabitEthernet0/0
  ip access-group ______________________ ______
```

**Q2.c** — Explique pourquoi ces deux ACL sont placées en entrée (in) sur les interfaces LAN et non en sortie sur les interfaces WAN : *(7 pts)*

```
Pour une ACL étendue, le placement optimal est près de la ____________________
Raison technique : __________________________________________________________
Si on la plaçait côté WAN en sortie : _______________________________________
Impact sur les performances : ________________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/50)

### 🔐 Exercice 3 — VPN Site-à-Site (/25)

> NETSERV doit relier le Siège (R1, WAN : 10.1.1.1) et l'Agence (R3, WAN : 10.3.3.3).
> Mission 1 : Configurer un tunnel GRE. Mission 2 : Expliquer l'ajout d'IPsec.

**Q3.a** — Écris la configuration complète du tunnel GRE des **deux côtés** : *(12 pts)*

```cisco
! === R1 (Siège) ===
interface Tunnel0
  ip address _______________ _______________     ! IP : 172.16.100.1/30
  tunnel source _______________                  ! Interface WAN R1
  tunnel destination _______________             ! IP WAN R3
  _______________________________________________  ! Ne pas oublier

! === R3 (Agence) — configuration miroir ===
interface Tunnel0
  ip address _______________ _______________     ! IP : 172.16.100.2/30
  tunnel source _______________                  ! Interface WAN R3
  tunnel destination _______________             ! IP WAN R1 ← INVERSÉ
  _______________________________________________
```

**Q3.b** — Écris les deux commandes de vérification à exécuter sur R1 après configuration et indique le résultat attendu : *(6 pts)*

```
Vérification 1 :
  Commande : _______________________________________________________________
  Résultat attendu : _______________________________________________________

Vérification 2 :
  Commande : _______________________________________________________________
  Résultat attendu : _______________________________________________________
```

**Q3.c** — GRE seul ne chiffre pas les données. Complète le tableau pour expliquer l'ajout d'IPsec : *(7 pts)*

| Aspect | GRE seul | GRE + IPsec |
|---|---|---|
| Encapsulation | Oui (IP proto 47) | Oui |
| Chiffrement | | |
| Authentification des paquets | | |
| Protection contre l'écoute | | |
| Configuration côté IOS | Simple | |
| Usage recommandé | Lab, transit interne | |

---

### 🔥 Exercice 4 — Firewall ZPF (/20)

> NETSERV installe un routeur pare-feu à l'entrée de son datacenter avec :
> - Interface Gi0/0 → Zone INSIDE (172.16.0.0/16, serveurs internes)
> - Interface Gi0/1 → Zone OUTSIDE (Internet)
> - Interface Gi0/2 → Zone DMZ (192.168.100.0/24, serveurs web publics)

**Q4.a** — Complète les deux règles fondamentales du ZPF : *(4 pts)*

```
Règle 1 : Trafic INTRA-ZONE (même zone) → autorisé par ___________________
Règle 2 : Trafic INTER-ZONES sans policy-map → ___________________________
```

**Q4.b** — Complète la configuration ZPF pour permettre aux serveurs INSIDE d'accéder à Internet en HTTP/HTTPS, et à Internet d'accéder aux serveurs DMZ en HTTP/HTTPS uniquement : *(12 pts)*

```cisco
! 1. Créer les zones
zone security _________________
zone security _________________
zone security _________________

! 2. Assigner les interfaces
interface GigabitEthernet0/0
  zone-member security ___________________

interface GigabitEthernet0/1
  zone-member security ___________________

interface GigabitEthernet0/2
  zone-member security ___________________

! 3. Class-map pour trafic web
class-map type inspect match-any TRAFIC_WEB
  match protocol ___________________
  match protocol ___________________

! 4. Policy-map INSIDE → OUTSIDE
policy-map type inspect INSIDE_VERS_OUTSIDE
  class type inspect TRAFIC_WEB
    ___________________               ! Inspection stateful
  class class-default
    ___________________               ! Tout le reste : bloqué

! 5. Policy-map OUTSIDE → DMZ
policy-map type inspect OUTSIDE_VERS_DMZ
  class type inspect ___________________
    inspect
  class class-default
    drop

! 6. Zone-pairs
zone-pair security INSIDE_OUT source INSIDE destination ___________________
  service-policy type inspect ___________________

zone-pair security OUTSIDE_DMZ source ___________________ destination DMZ
  service-policy type inspect ___________________
```

**Q4.c** — Compare ACL statique et ZPF stateful pour le filtrage DNS (UDP port 53) : *(4 pts)*

```
Avec ACL statique :
  Pour autoriser les requêtes DNS sortantes, on écrit : ________________________
  Problème de sécurité : ______________________________________________________

Avec ZPF + inspect :
  Le firewall suit l'état des connexions → les réponses DNS sont autorisées
  automatiquement seulement si : ______________________________________________
  Avantage sécurité : _________________________________________________________
```

---

---

## 🏅 Barème global

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — BGP attributs et sélection | S2.4 + S2.5 | /30 | ≥ 17 |
| Ex. 2 — ACL étendue nommée | S5.1 | /25 | ≥ 14 |
| Ex. 3 — VPN GRE + IPsec | S5.2 | /25 | ≥ 14 |
| Ex. 4 — Firewall ZPF | S5.3 | /20 | ≥ 11 |
| **TOTAL** | | **/100** | **≥ 55** |

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**Q1.a.1** : Chemin via 10.0.2.2 (FAI 5511) choisi · Étape 2 — Local-Pref : 120 > 80 → 10.0.2.2 préféré

**Q1.a.2** : Critère suivant = MED (Metric) · Via 10.0.1.2 MED=30 vs via 10.0.2.2 MED=0 · Choix : 10.0.2.2 · Règle : MED **plus bas** = préféré

**Q1.a.3** : Absence de `*` = route invalide (next-hop inaccessible ou autre problème de validation) · Cause probable : next-hop 10.0.1.2 non joignable dans la table de routage locale · Commande : `show bgp ipv4 unicast 172.20.0.0/16` ou `show ip route 10.0.1.2`

**Q1.a.4** :
```
route-map PREFER_5511 permit 10
  set local-preference 200           ! Valeur haute pour favoriser 5511

router bgp 64513
  neighbor 10.0.2.2 route-map PREFER_5511 in
```
Valeur actuelle pour 5511 = 120 → passer à 200 · Valeur pour 3215 reste à 80 → 200 > 80 → 5511 toujours gagne

**Q1.a.5** : eBGP → l'AS local est **ajouté** à l'AS-path ("200 300" devient "100 200 300") · iBGP → AS-path **non modifié** (pas d'ajout du propre AS) car on reste dans le même AS · Split horizon iBGP : une route apprise en iBGP n'est **pas re-propagée** à un autre voisin iBGP (évite les boucles) → nécessite mesh complet ou Route Reflector

## Correction Exercice 2

**Q2.a** :
```cisco
ip access-list extended POLITIQUE_SIEGE
  deny  tcp 192.168.10.0 0.0.0.255 192.168.100.0 0.0.0.255 eq 23
  permit ip any any

interface GigabitEthernet0/0
  ip access-group POLITIQUE_SIEGE in
```

**Q2.b** :
```cisco
ip access-list extended POLITIQUE_AGENCE
  permit tcp 192.168.20.0 0.0.0.255 192.168.100.0 0.0.0.255 eq 80
  permit tcp 192.168.20.0 0.0.0.255 192.168.100.0 0.0.0.255 eq 443
  deny ip any any

interface GigabitEthernet0/0
  ip access-group POLITIQUE_AGENCE in
```

**Q2.c** : Placement près de la **source** · Raison : l'ACL étendue peut filtrer avec précision (src+dst+port) → doit agir le plus tôt possible pour éviter que le trafic indésirable parcourt le réseau · Si côté WAN sortie → le trafic traverse inutilement tous les liens intermédiaires avant d'être bloqué · Impact performance : économise la bande passante des liens intermédiaires

## Correction Exercice 3

**Q3.a** :
```cisco
! R1
interface Tunnel0
  ip address 172.16.100.1 255.255.255.252
  tunnel source 10.1.1.1
  tunnel destination 10.3.3.3
  no shutdown

! R3
interface Tunnel0
  ip address 172.16.100.2 255.255.255.252
  tunnel source 10.3.3.3
  tunnel destination 10.1.1.1
  no shutdown
```

**Q3.b** : `show interfaces Tunnel0` → "Tunnel0 is up, line protocol is up" · `ping 172.16.100.2 source Tunnel0` → "Success rate is 100 percent"

**Q3.c** :

| Aspect | GRE seul | GRE + IPsec |
|---|---|---|
| Chiffrement | **Non** | **Oui (ESP avec AES)** |
| Authentification | **Non** | **Oui (IKE + PSK ou cert)** |
| Protection écoute | **Non (clair)** | **Oui** |
| Config IOS | Simple | **Complexe (IKE policy, transform-set, crypto map)** |
| Usage recommandé | Lab, transit interne | **Production, données sensibles** |

## Correction Exercice 4

**Q4.a** : Intra-zone → autorisé **par défaut** · Inter-zones sans policy → **refusé par défaut**

**Q4.b** :
```cisco
zone security INSIDE
zone security OUTSIDE
zone security DMZ

interface GigabitEthernet0/0
  zone-member security INSIDE
interface GigabitEthernet0/1
  zone-member security OUTSIDE
interface GigabitEthernet0/2
  zone-member security DMZ

class-map type inspect match-any TRAFIC_WEB
  match protocol http
  match protocol https

policy-map type inspect INSIDE_VERS_OUTSIDE
  class type inspect TRAFIC_WEB
    inspect
  class class-default
    drop

policy-map type inspect OUTSIDE_VERS_DMZ
  class type inspect TRAFIC_WEB
    inspect
  class class-default
    drop

zone-pair security INSIDE_OUT source INSIDE destination OUTSIDE
  service-policy type inspect INSIDE_VERS_OUTSIDE

zone-pair security OUTSIDE_DMZ source OUTSIDE destination DMZ
  service-policy type inspect OUTSIDE_VERS_DMZ
```

**Q4.c** : ACL statique = `permit udp any any eq 53` → ouvre aussi les paquets UDP entrants sur port 53 (exploitable) · Problème : réponse DNS ne peut pas être distinguée d'une attaque UDP port 53 · ZPF inspect → autorise la réponse **seulement si** une requête sortante a été tracée dans la table d'état → DNS spoofing depuis l'extérieur impossible · Avantage : protection contre les attaques par réflexion DNS

---

*Devoir + Correction S12 — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année*
*Épreuves E31 + E32 | Compétences S2.4 · S2.5 · S5.1 · S5.2 · S5.3 · C2.2 · C2.3*
