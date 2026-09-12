# 📋 ÉVALUATION DIAGNOSTIQUE A3 — E31/U31
## Retour de Stage : Où en Êtes-Vous ?

**Nom : ________________  Prénom : ________________  Date : ________________**
**Durée : 25 min — SANS DOCUMENT — Ce diagnostic n'est PAS noté**

---

> *Ce questionnaire sert uniquement à identifier les points à retravailler en début d'A3. Répondez au mieux de vos souvenirs. Laissez blanc plutôt que d'inventer.*

---

## BLOC 1 — Adressage IPv4 (5 questions)

**Q1.** Quelle est la formule pour calculer le wildcard mask depuis un masque réseau ?

_________________________________________________________________________

**Q2.** Vous avez besoin d'un réseau pour 12 hôtes. Quel préfixe CIDR minimal choisissez-vous ? Donnez le masque et le wildcard correspondants.

```
Préfixe : /______
Masque  : 255.255.255.______
Wildcard: 0.0.0.______
```

**Q3.** Découpez `172.16.4.0/22` en deux sous-réseaux égaux. Donnez les adresses réseau et les masques des deux sous-réseaux.

```
Sous-réseau A : ________________ / ____
Sous-réseau B : ________________ / ____
```

**Q4.** Une liaison point-à-point entre deux routeurs utilise le préfixe /30. Combien d'adresses hôtes sont disponibles ? Quelle est l'adresse broadcast du réseau `10.0.0.8/30` ?

```
Hôtes : ______
Broadcast : ______
```

**Q5.** Quelle est la différence entre un masque réseau et un wildcard mask ? Dans quel protocole le wildcard est-il utilisé ?

_________________________________________________________________________
_________________________________________________________________________

---

## BLOC 2 — OSPF v2 (5 questions)

**Q6.** Sur `show ip ospf neighbor`, un voisin affiche l'état `FULL/DR`. Que signifient ces deux parties ?

```
FULL : _________________________________________________________________
DR   : _________________________________________________________________
```

**Q7.** Deux routeurs ne parviennent pas à établir une adjacence OSPF — ils restent bloqués en état `EXSTART`. Citez la cause la plus probable.

_________________________________________________________________________

**Q8.** Écrivez le network statement OSPF pour annoncer le réseau `192.168.50.0/25` dans l'area 0 :

```ios
router ospf 1
  network ________________ ________________ area ___
```

**Q9.** Qu'est-ce que la `passive-interface` dans OSPF ? Pourquoi l'utilise-t-on sur les interfaces LAN (côté utilisateurs) ?

_________________________________________________________________________
_________________________________________________________________________

**Q10.** Citez deux informations visibles dans `show ip ospf neighbor` qui permettent de détecter un problème d'adjacence.

1. _______________________________________________________________________
2. _______________________________________________________________________

---

## BLOC 3 — HSRP et IPv6 (5 questions)

**Q11.** En HSRP, quelle est la différence de comportement entre un routeur configuré avec `preempt` et un routeur sans `preempt`, lors du retour de l'Active après une panne ?

_________________________________________________________________________
_________________________________________________________________________

**Q12.** R-A a une priorité HSRP de 110, R-B de 90. Le tracking de R-A est configuré avec un décrement de 25. L'interface WAN de R-A tombe. R-B prend-il le rôle Active ?

```
Priorité R-A après tracking = _____ - _____ = _____
Bascule si _____ < _____ ? OUI / NON
```

**Q13.** Simplifiez ces deux adresses IPv6 :

```
2001:0db8:0000:0000:0000:0000:0000:0001 → _______________
fe80:0000:0000:0000:0210:a4ff:fe01:0001 → _______________
```

**Q14.** Qu'est-ce qu'une adresse Link-Local (LLA) en IPv6 ? Par quel préfixe commence-t-elle ? Peut-elle être routée sur Internet ?

_________________________________________________________________________
_________________________________________________________________________

**Q15.** Quelle commande IOS est indispensable sur tout routeur pour activer le routage IPv6 ?

```ios
_________________________________________
```

---

## 📊 AUTO-POSITIONNEMENT

> Cochez honnêtement pour chaque domaine :

| **Domaine** | **Je maîtrise** ✅ | **Fragile** ⚠️ | **À refaire** ❌ |
|---|---|---|---|
| Calcul adressage IPv4 | | | |
| OSPF v2 : config + vérification | | | |
| OSPF : DR/BDR + adjacences | | | |
| HSRP : préemption + tracking | | | |
| IPv6 : notation simplification | | | |
| IPv6 : types d'adresses GUA/LLA | | | |

---

## 📊 CORRECTION DIAGNOSTIQUE

### BLOC 1

**Q1.** Wildcard = **255.255.255.255 − masque réseau** ✅

**Q2.** Pour 12 hôtes : 2⁴ − 2 = 14 ≥ 12 → **/28**. Masque : 255.255.255.240. Wildcard : 0.0.0.15 ✅

**Q3.** `172.16.4.0/22` = 4 × /24 blocs (172.16.4.0 à 172.16.7.255). Couper en /23 :

```
Sous-réseau A : 172.16.4.0/23  (172.16.4.0 à 172.16.5.255)
Sous-réseau B : 172.16.6.0/23  (172.16.6.0 à 172.16.7.255)
```
✅

**Q4.** /30 → 2² − 2 = **2 hôtes**. `10.0.0.8/30` : bloc de 4 → broadcast = 10.0.0.8 + 3 = **10.0.0.11** ✅

**Q5.** Le masque réseau indique la frontière réseau/hôte (bits à 1 = réseau). Le wildcard est son inverse (bits à 1 = "ignorer ce bit"). Le wildcard est utilisé dans **OSPF** (network statements) et dans les ACL. ✅

---

### BLOC 2

**Q6.** FULL = adjacence complète, LSDB synchronisée. DR = le voisin est le Designated Router du segment. ✅

**Q7.** Cause la plus probable : **MTU mismatch** entre les deux interfaces (une accepte des paquets de 1500 octets, l'autre de 1476 octets par exemple). ✅

**Q8.**
```ios
network 192.168.50.0 0.0.0.127 area 0
```
(wildcard /25 = 255.255.255.128 → wildcard = 0.0.0.127) ✅

**Q9.** `passive-interface` empêche l'envoi de hellos OSPF sur cette interface (pas de voisin routeur de ce côté) tout en continuant à annoncer le réseau dans la LSDB. Utilisé sur les interfaces LAN côté utilisateurs pour ne pas attendre de voisins qui n'existent pas et économiser la bande passante. ✅

**Q10.** Parmi : état (si FULL = ok, sinon problème) ; Dead Timer (si proche de 0 = voisin instable) ; priorité (si 0 = exclu élection) ; ID du voisin (identifier qui est en face) ✅

---

### BLOC 3

**Q11.** Avec `preempt` : après le retour de l'Active, il reprend automatiquement son rôle Active s'il a une priorité plus haute. Sans `preempt` : il reste Standby même si sa priorité est supérieure au routeur actuellement Active. ✅

**Q12.**
```
Priorité R-A après tracking = 110 - 25 = 85
Bascule si 85 < 90 ? OUI ✅
```

**Q13.**
```
2001:0db8:0000:0000:0000:0000:0000:0001 → 2001:db8::1
fe80:0000:0000:0000:0210:a4ff:fe01:0001 → fe80::210:a4ff:fe01:1
```
✅

**Q14.** LLA = adresse IPv6 locale au lien, préfixe **fe80::/10**, jamais routée sur Internet (invisible au-delà du segment local). Elle est automatiquement générée sur toute interface IPv6 active. ✅

**Q15.** `ipv6 unicast-routing` ✅

---

## 📊 GRILLE DE POSITIONNEMENT FORMATEUR

| **Score Bloc 1 (Q1–Q5)** | **Interprétation** | **Action** |
|---|---|---|
| 4–5/5 | Adressage maîtrisé | Rien — poursuivre |
| 2–3/5 | Fragilités sur VLSM | Fiche rappel VLSM + 15 min exercices supplémentaires |
| 0–1/5 | Adressage non acquis | Plan de remédiation individuel |

| **Score Bloc 2 (Q6–Q10)** | **Interprétation** | **Action** |
|---|---|---|
| 4–5/5 | OSPF v2 solide | Lab OSPF version complète |
| 2–3/5 | Concepts présents, config fragile | Lab OSPF version guidée |
| 0–1/5 | OSPF à reconstruire | Lab OSPF version assistée + rappel cours S4-A2 |

| **Score Bloc 3 (Q11–Q15)** | **Interprétation** | **Action** |
|---|---|---|
| 4–5/5 | HSRP + IPv6 solides | Cours OSPFv3 complet |
| 2–3/5 | IPv6 à consolider | Révision notation + types avant OSPFv3 |
| 0–1/5 | IPv6 non acquis | Reprendre S15-A2 avant OSPFv3 |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
