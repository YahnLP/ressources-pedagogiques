# 🎲 ACTIVITÉ – S15 ANNÉE 2 – E31
## Partie 1 : Quiz Diagnostic E31 A2 — Partie 2 : « Votre Téléphone Parle Déjà IPv6 »

---

# ════════════════════════════════════════════
# PARTIE 1 — QUIZ DIAGNOSTIC E31 A2
# ════════════════════════════════════════════

## ⏱️ DURÉE : 10 min — INDIVIDUEL — SANS DOCUMENT

> **Ce quiz n'est pas noté.** Il sert à identifier où vous en êtes avant les révisions.
> Répondez en 30 secondes maximum par question. Laissez blanc si vous ne savez plus.

---

**Q1.** Quel préfixe CIDR permet d'adresser exactement 30 hôtes ?

_______

**Q2.** Dans OSPF, que représente le wildcard `0.0.0.255` ?

_________________________________________________________________________

**Q3.** Sur `show ip ospf neighbor`, que signifie l'état `FULL/DR` ?

_________________________________________________________________________

**Q4.** Une ACL étendue doit-elle être placée proche de la source ou de la destination ?

_______

**Q5.** Dans un VPN IPsec site-à-site, l'ACL crypto de R2 est-elle identique ou miroir de celle de R1 ?

_______

**Q6.** En HSRP, quel routeur devient Active si R1 a priorité 110 et R2 a priorité 90 ?

_______

**Q7.** La commande `standby 1 preempt` est configurée sur R1. R1 tombe puis revient. Que se passe-t-il ?

_________________________________________________________________________

**Q8.** Dans Nagios, quel code retour indique un état CRITICAL ?

_______

**Q9.** En WPA2-Enterprise, quel serveur prend la décision Access-Accept ou Access-Reject ?

_______

**Q10.** En VPN IPsec, quel état dans `show crypto isakmp sa` indique que la Phase 1 est établie ?

_______

---

**Mon auto-évaluation :**

| **Thème** | **Je maîtrise** ✅ | **À revoir** ❌ |
|---|---|---|
| Adressage IPv4 | | |
| OSPF | | |
| ACL étendues | | |
| VPN IPsec | | |
| HSRP/VRRP | | |
| Nagios | | |
| Wi-Fi sécurisé | | |

---

# ════════════════════════════════════════════
# PARTIE 2 — DÉCOUVERTE IPv6
# ════════════════════════════════════════════

## ⏱️ DURÉE : 15 min — GROUPES DE 4

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur pose la question :**

> *"Depuis combien d'années entend-on parler de la 'pénurie d'adresses IPv4' ? Et pourtant Internet continue de fonctionner. Comment est-ce possible ? Et qu'est-ce que ça va changer dans votre métier ?"*

---

## 🔢 PHASE 1 — Le Problème des Chiffres (5 min)

**Le formateur présente :**

```
IPv4 : 32 bits = 2³² = 4 294 967 296 adresses publiques uniques

Inventaire mondial IANA en 2025 :
 → Dernier /8 attribué en Asie-Pacifique : 2011
 → RIPE (Europe) : plus d'adresses disponibles depuis 2019
 → ARIN (Amériques) : liste d'attente depuis 2015
 → Actuellement ~20 milliards d'appareils connectés à Internet
```

**Question aux groupes :**

> *"Comment est-ce qu'Internet fonctionne encore avec 4 milliards d'adresses pour 20 milliards d'appareils ?"*

| **Mécanisme actuel** | **Limite** |
|---|---|
| NAT / PAT (une IP publique = 65 535 ports) | Complexifie P2P, IoT, VoIP |
| Réutilisation des adresses RFC1918 | Espace limité en interne |
| Sous-allocation des blocs | Gaspillage addressé mais épuisement réel |

---

## 📱 PHASE 2 — Votre Téléphone Parle Déjà IPv6 (5 min)

**Le formateur demande :**

> *"Qui peut vérifier son adresse IPv6 sur son smartphone ?"*

**Sur iPhone :** Réglages → Wi-Fi → (réseau) → Adresse IPv6

**Sur Android :** Réglages → À propos → Statut → Adresse IPv6

**Exemple d'adresse IPv6 typique qu'on voit :**

```
2a01:cb19:8a4:cd00:1c2f:5e:3d7a:f820
```

**Questions :**

**Q1.** Combien de groupes y a-t-il dans cette adresse ? _______________

**Q2.** En quoi les chiffres sont-ils différents de l'IPv4 ? _______________

**Q3.** Si vous avez une adresse qui commence par `fe80`, c'est différent. Pourquoi cette adresse ne peut-elle pas être utilisée pour aller sur Google ?

_________________________________________________________________________

---

## 📊 PHASE 3 — Synthèse émergente (3 min)

**Le formateur formalise :**

```
┌────────────────────────────────────────────────────────────────────┐
│  IPv6 = réponse à l'épuisement des adresses IPv4                  │
│                                                                    │
│  128 bits = 2¹²⁸ = 340 000 000 000 000 000 000 000 000 000 000   │
│           = 340 undécillions d'adresses                            │
│  → Assez pour donner ~4,8 × 10²⁸ adresses par être humain sur    │
│    Terre. L'épuisement est terminé.                                │
│                                                                    │
│  Ce qu'on va apprendre aujourd'hui :                               │
│  • Comment se lit et s'écrit une adresse IPv6                      │
│  • Les différents types d'adresses (publique, locale, loopback…)  │
│  • Comment configurer IPv6 sur un routeur Cisco                    │
│                                                                    │
│  Ce qu'on verra en A3 : OSPFv3, SLAAC, NDP, dual-stack           │
└────────────────────────────────────────────────────────────────────┘
```

---

## ✅ RÉPONSES QUIZ DIAGNOSTIC (correction collective)

| **Q** | **Réponse** | **Révision si manqué** |
|---|---|---|
| Q1 | /27 (2⁵-2=30) | S1-A2 |
| Q2 | Tout le sous-réseau /24 | S4-A2 |
| Q3 | Adjacence complète, voisin est le DR | S4-A2 |
| Q4 | Proche de la source | S5-A2 |
| Q5 | Miroir (source/dest inversées) | S7-A2 |
| Q6 | R1 (priorité 110 > 90) | S12-A2 |
| Q7 | R1 reprend le rôle Active (preempt) | S12-A2 |
| Q8 | Code 2 | S10-A2 |
| Q9 | Serveur RADIUS | S8-A2 |
| Q10 | QM_IDLE | S7-A2 |

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
