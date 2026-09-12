# 🎯 TD RÉVISIONS — HAUTE DISPONIBILITÉ
## S13 Année 3 – E31

**Nom : ________________  Prénom : ________________**

---

## 📋 RAPPEL SYNTHÉTIQUE HAUTE DISPONIBILITÉ

### HSRP vs VRRP — Différences clés

| **Critère** | **HSRP** | **VRRP** |
|---|---|---|
| Propriétaire | Cisco uniquement | Standard ouvert (RFC 5798) |
| Rôle principal | **Active** | **Master** |
| Rôle de secours | **Standby** | **Backup** |
| Priorité défaut | **100** | **100** |
| MAC virtuelle | `0000.0C07.ACxx` | `0000.5E00.01xx` |
| Multicast hellos | 224.0.0.2 | 224.0.0.18 |
| Préemption par défaut | ❌ Non | ✅ Oui |

> **Rappel HSRP :** Hold Timer ≈ délai de bascule. `preempt` = reprendre Active si prio plus haute.

### STP — États des ports

| **État** | **Apprend MAC ?** | **Forward trames ?** | **Quand ?** |
|---|---|---|---|
| **Blocking** | ❌ | ❌ | Port redondant — évite les boucles |
| **Listening** | ❌ | ❌ | Transition vers Forwarding |
| **Learning** | ✅ | ❌ | Remplit la table MAC |
| **Forwarding** | ✅ | ✅ | Port actif normal |
| **Disabled** | ❌ | ❌ | Port administrativement désactivé |

> **Root Bridge** = switch avec le Bridge ID le plus bas (priorité la plus basse + MAC). Les ports vers le Root Bridge = **Root Ports**. Les autres ports actifs = **Designated Ports**. Ports bloqués = **Blocked/Alternate Ports**.

---

## 🧪 TD-HA1 — HSRP : Calculs et Analyse (5 pts)

### Contexte

> Infrastructure : LAN `192.168.20.0/25`, deux routeurs :

| | **R-MAIN** | **R-BACKUP** |
|---|---|---|
| IP réelle | 192.168.20.1 | 192.168.20.2 |
| Priorité HSRP | 140 | 100 |
| Preempt | Oui | Oui |
| Timers | Hello=1s, Hold=3s | Idem |
| Interface WAN | Gi0/1 trackée, décrement=50 | — |
| IP virtuelle | 192.168.20.126 | 192.168.20.126 |

**HA1.1 *(0,5 pt)*** — Qui est Active au démarrage ? Pourquoi ?

_________________________________________________________________________

**HA1.2 *(1 pt)*** — Le WAN (Gi0/1) de R-MAIN tombe. Calculez la nouvelle priorité de R-MAIN et déterminez si la bascule aura lieu :

```
Priorité R-MAIN après tracking = _____ - _____ = _____
Bascule si _____ < _____ ? : OUI / NON
Routeur Active après panne WAN : _____
```

**HA1.3 *(1 pt)*** — Le WAN de R-MAIN revient. R-MAIN reprend-il automatiquement Active ? Justifiez avec la commande IOS concernée.

_________________________________________________________________________
_________________________________________________________________________

**HA1.4 *(1 pt)*** — Voici `show standby brief` après la panne WAN :

```
Interface  Grp Pri P State   Active   Standby          Virtual IP
Gi0/0      1   90  P Standby local    192.168.20.2     192.168.20.126
```

Confirmez que c'est cohérent avec votre calcul HA1.2. Que signifie la colonne `P` ?

_________________________________________________________________________
_________________________________________________________________________

**HA1.5 *(1,5 pt)*** — Un collègue configure HSRP mais les deux routeurs affichent simultanément l'état `Active`. Quelle est la cause et quelle commande de diagnostic le prouve immédiatement ?

_________________________________________________________________________
_________________________________________________________________________

---

## 🧪 TD-HA2 — HSRP vs VRRP : Interopérabilité (3 pts)

**HA2.1 *(1 pt)*** — Un réseau existant a un routeur Cisco (R-CISCO) configuré avec HSRP groupe 1. Un nouveau routeur Juniper (R-JUNIPER) doit assurer la redondance. Peut-on utiliser HSRP entre eux ? Que faut-il faire ?

_________________________________________________________________________
_________________________________________________________________________

**HA2.2 *(1 pt)*** — Réécrivez la configuration HSRP suivante en son équivalent VRRP sur Cisco IOS :

```ios
! HSRP existant :
interface GigabitEthernet0/0
  standby 2 ip 10.50.0.254
  standby 2 priority 150
  standby 2 preempt
  standby 2 timers 1 3
```

```ios
! Équivalent VRRP :
interface GigabitEthernet0/0
  _____________________________________________
  _____________________________________________
  _____________________________________________
  _____________________________________________
```

**HA2.3 *(1 pt)*** — En VRRP, la préemption est activée par défaut (contrairement à HSRP). Expliquez concrètement ce que cela change en cas de retour du routeur de priorité supérieure après une panne.

_________________________________________________________________________
_________________________________________________________________________

---

## 🧪 TD-HA3 — STP : Analyse d'une Topologie (4 pts)

### Topologie

```
       [SW-CORE]
       Prio: 4096
      /         \
  Gi0/1         Gi0/2
  Coût: 4       Coût: 4
    /               \
[SW-A]           [SW-B]
Prio: 32768      Prio: 32768
MAC: aa:bb       MAC: cc:dd
    \               /
   Gi0/3 ─────── Gi0/3
      (lien direct entre SW-A et SW-B)
```

**HA3.1 *(1 pt)*** — Identifiez le Root Bridge. Justifiez votre réponse avec les valeurs numériques.

_________________________________________________________________________
_________________________________________________________________________

**HA3.2 *(1 pt)*** — Le lien direct entre SW-A et SW-B forme une boucle potentielle. STP doit bloquer un port. Lequel sera bloqué (SW-A Gi0/3 ou SW-B Gi0/3) ? Quel est ce type de port dans la nomenclature STP ?

_________________________________________________________________________
_________________________________________________________________________

**HA3.3 *(1 pt)*** — Un stagiaire voit le port Gi0/3 de SW-B bloqué dans `show spanning-tree` et conclut : "Ce port est en panne, je dois le reconfigurer." A-t-il raison ? Expliquez.

_________________________________________________________________________
_________________________________________________________________________

**HA3.4 *(1 pt)*** — Pour réduire le temps de convergence STP sur les ports reliés aux PCs (qui ne peuvent jamais créer de boucle), quelle fonctionnalité STP active-t-on ? Comment la configurer en IOS ?

```ios
interface GigabitEthernet0/10   ! port vers un PC
  _____________________________________________
```

---

## 🧪 TD-HA4 — Scénario Intégré : Choisir son Architecture HA (3 pts)

> Pour chaque cas, choisissez la solution de redondance la plus adaptée et justifiez en 2 phrases.

**HA4.1 *(1 pt)*** — PME de 50 employés, 1 seul site, 2 routeurs de bordure, budget limité, besoin de redondance passerelle en < 5 secondes.

Choix : ___________  Justification : ________________________________________
_________________________________________________________________________

**HA4.2 *(1 pt)*** — Réseau multi-constructeur (Cisco + Fortinet + Juniper), 3 routeurs de bordure, besoin de redondance interopérable.

Choix : ___________  Justification : ________________________________________
_________________________________________________________________________

**HA4.3 *(1 pt)*** — Datacenter avec 100 serveurs dans des VLANs différents, liens redondants entre tous les switches, besoin d'éviter les boucles L2 tout en maintenant la disponibilité.

Choix : ___________  Justification : ________________________________________
_________________________________________________________________________

---

## 📊 BARÈME TD HAUTE DISPONIBILITÉ

| **Section** | **Points** |
|---|---|
| TD-HA1 | /5 |
| TD-HA2 | /3 |
| TD-HA3 | /4 |
| TD-HA4 | /3 |
| **TOTAL** | **/15** |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
