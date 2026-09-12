# 🧭 OUTIL DE POSITIONNEMENT — S15 A3
## Identifiez Vos Lacunes et Choisissez Votre Parcours de Remédiation

**Nom : ________________  Prénom : ________________**

---

> **Mode d'emploi :** Répondez à chaque question en 1 minute maximum. Ne cherchez pas — répondez spontanément. Ce n'est pas noté : c'est un radar pour identifier où travailler.

---

## QUIZ FLASH — 18 QUESTIONS (18 min)

### Adressage IPv4

**Q1.** Quel wildcard correspond au masque `255.255.255.224` (`/27`) ?

_________

**Q2.** Vous devez loger 45 hôtes. Quel préfixe CIDR minimal choisissez-vous ?

_________

**Q3.** Dans OSPF, à quoi sert le wildcard ? (En une phrase)

_________________________________________

---

### OSPF

**Q4.** Quelle commande OSPF annonce le réseau `10.50.0.192/27` dans l'area 0 ?

```ios
network _________________ _________________ area 0
```

**Q5.** `show ip ospf neighbor` affiche l'état `EXSTART`. Quelle est la cause la plus probable ?

_________________________________________

**Q6.** Dans OSPFv3, comment déclarer une interface dans l'area 0 ? (Pas de `network` !)

```ios
interface GigabitEthernet0/0
  _________________________________________
```

---

### ACL et VPN

**Q7.** Une ACL étendue doit-elle être placée proche de la source ou de la destination ?

_________

**Q8.** L'ACL crypto de R-PARIS couvre `permit ip 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255`. Écrivez l'ACL crypto de R-LYON (miroir) :

```ios
permit ip _________________ _________________ _________________ _________________
```

**Q9.** `show crypto ipsec sa` affiche `#pkts encaps: 0`. Que signifie ce 0 ?

_________________________________________

---

### HSRP / Haute Dispo

**Q10.** R1 (prio 110) a un tracking décrement de 20. R2 a la priorité 100. Si le WAN de R1 tombe, y a-t-il bascule ?

```
R1 prio après tracking = _____ - _____ = _____
Bascule si _____ < _____ ? : OUI / NON
```

**Q11.** Quelle est la différence de comportement entre HSRP avec et sans `preempt` lors du retour de R1 après une panne ?

_________________________________________

**Q12.** Quel est approximativement le délai de bascule HSRP ? (Quel timer ?)

_________

---

### Nagios

**Q13.** Un plugin retourne `exit 1`. Quel état Nagios affiche-t-il ?

_________

**Q14.** `max_check_attempts = 4`, `retry_check_interval = 1 min`. Combien de minutes après la 1ère anomalie la première alerte est-elle envoyée ?

_________

**Q15.** Un plugin retourne `exit 3`. Qu'est-ce que cela indique ? Citez une cause possible.

_________________________________________

---

### IPv6

**Q16.** Calculez l'EUI-64 pour la MAC `A0:B1:C2:D3:E4:F5`. Donnez juste le 1er octet après inversion du bit U/L.

```
A0 = ________ binaire → 7ème bit = ___ → inverser → ___ → ________ = ________ hex
```

**Q17.** Quelle est la différence entre DHCPv6 stateless (O=1) et DHCPv6 stateful (M=1) ?

_________________________________________

**Q18.** En dual-stack, un PC résout `monserveur.fr` et reçoit un enregistrement A (IPv4) ET AAAA (IPv6). Quel enregistrement utilise-t-il en premier ?

_________

---

## 📊 GRILLE D'AUTO-ÉVALUATION

Comptez vos bonnes réponses par domaine et cochez votre niveau :

| **Domaine** | **Q** | **Mes réponses** | **Score** | **Mon niveau** |
|---|---|---|---|---|
| Adressage IPv4 | Q1–Q3 | | /3 | 🟢 ≥2 / 🟡 1 / 🔴 0 |
| OSPF | Q4–Q6 | | /3 | |
| ACL + VPN | Q7–Q9 | | /3 | |
| HSRP | Q10–Q12 | | /3 | |
| Nagios | Q13–Q15 | | /3 | |
| IPv6 | Q16–Q18 | | /3 | |

---

## 🗺️ MON PLAN DE REMÉDIATION PERSONNALISÉ

> Classez vos domaines par priorité (du plus faible au plus solide) et choisissez vos parcours :

| **Priorité** | **Domaine** | **Score** | **Parcours** |
|---|---|---|---|
| 1 — À travailler absolument | | /3 | P___ |
| 2 — À consolider | | /3 | P___ |
| 3 — À réviser rapidement | | /3 | P___ |
| Déjà maîtrisé | | /3 | — |

---

## ✅ RÉPONSES RAPIDES AU QUIZ DE POSITIONNEMENT

| **Q** | **Réponse attendue** | **Piège fréquent** |
|---|---|---|
| Q1 | `0.0.0.31` | Ne pas confondre avec le masque (224) |
| Q2 | `/26` (62 hôtes) | /27 = 30 hôtes, insuffisant pour 45 |
| Q3 | Indique quels bits ignorer pour correspondre au réseau | — |
| Q4 | `10.50.0.192 0.0.0.31` | Wildcard /27 = 0.0.0.31, pas 0.0.0.255 |
| Q5 | MTU mismatch | Pas une erreur de PSK (c'est Phase 1) |
| Q6 | `ipv6 ospf 1 area 0` | Pas de `network` en OSPFv3 |
| Q7 | Proche de la **source** | ACL standard = proche destination |
| Q8 | `permit ip 10.0.0.0 0.0.0.255 192.168.1.0 0.0.0.255` | Source/destination inversées |
| Q9 | Le routeur **n'envoie rien** dans le tunnel (ACL ne matche pas ou trafic absent) | ≠ tunnel coupé |
| Q10 | 110-20=90 < 100 → OUI, bascule | — |
| Q11 | Avec preempt : reprend Active. Sans : reste Standby | Erreur classique |
| Q12 | ≈ **Hold Timer** (défaut 10s) | Confusion avec Hello Timer (3s) |
| Q13 | **WARNING** 🟡 | exit 2 = CRITICAL, pas exit 1 |
| Q14 | 3 minutes (1 retry à 14h00+5min, puis 3×1min) | Voir calcul détaillé |
| Q15 | UNKNOWN 🟠 — API inaccessible / timeout / erreur de parsing | — |
| Q16 | A0=10100000 → bit 6 = 0 → inverser → 1 → 10100010 = A2 hex | Inverser le bon bit |
| Q17 | Stateless : adresse SLAAC + DNS via DHCPv6. Stateful : adresse ET DNS via DHCPv6 | — |
| Q18 | **IPv6 (AAAA)** — RFC 6724 | Surprise : IPv6 est préféré sur dual-stack |

---

## 📝 FICHE MÉMO PERSONNELLE

> À remplir en fin de séance (Phase 5). Maximum 1 page. Ce sont VOS repères — pas un cours complet.

```
═══════════════════════════════════════════════════════════════
  FICHE MÉMO E31 — [Votre Nom]
  Domaines travaillés : _____________  _____________
═══════════════════════════════════════════════════════════════

LES 3 ERREURS QUE JE NE FERAI PLUS :

1. ________________________________________________________________
   Pourquoi je me trompais : _____________________________________
   La règle correcte : ___________________________________________

2. ________________________________________________________________
   Pourquoi je me trompais : _____________________________________
   La règle correcte : ___________________________________________

3. ________________________________________________________________
   Pourquoi je me trompais : _____________________________________
   La règle correcte : ___________________________________________

MES COMMANDES RÉFLEXES (celles que j'oubliais) :

  Symptôme : _____________________ → Commande : __________________
  Symptôme : _____________________ → Commande : __________________
  Symptôme : _____________________ → Commande : __________________

MON POINT LE PLUS FRAGILE QUI RESTE :

  ________________________________________________________________
  Plan : __________________________________________________________
═══════════════════════════════════════════════════════════════
```

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
