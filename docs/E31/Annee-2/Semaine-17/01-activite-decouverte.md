# 🎲 ACTIVITÉ DÉCOUVERTE – S17 ANNÉE 2 – E31
## « Ce que Voit l'Analyste » : Capture de Trafic pendant une Bascule HSRP

---

## 🎯 OBJECTIFS

- ✅ Visualiser concrètement les messages HSRP hello, coup et resign dans une capture
- ✅ Comprendre le rôle des **Gratuitous ARP** lors d'une bascule
- ✅ Mesurer l'impact d'une bascule sur le trafic ICMP en cours (perte de paquets)
- ✅ Relier la théorie HSRP (S12) à l'observable réel dans Wireshark

---

## ⏱️ DURÉE : 20 min — COLLECTIF

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur projette une capture Wireshark annotée (ou une simulation sur Packet Tracer en mode simulation) et pose la question :**

> *"Voici une capture réseau d'un LAN pendant une bascule HSRP. Qu'est-ce qu'on voit ? Dans quel ordre ? Pourquoi ?"*

---

## 📊 PHASE 1 – Lecture de la Capture Annotée (8 min)

**Extrait de capture Wireshark (représentation textuelle) :**

```
N°    Heure      Source           Destination    Protocole  Info
──────────────────────────────────────────────────────────────────────────────
1     0.000      192.168.1.1      224.0.0.2      HSRP       Hello  State=Active  Pri=110
2     1.002      192.168.1.1      224.0.0.2      HSRP       Hello  State=Active  Pri=110
3     2.004      192.168.1.1      224.0.0.2      HSRP       Hello  State=Active  Pri=110

← À t=2,5s : interface LAN de R1 désactivée (panne simulée) ←

4     3.006      192.168.1.2      224.0.0.2      HSRP       Hello  State=Standby Pri=90
5     3.006      192.168.1.2      224.0.0.2      HSRP       Hello  State=Speak   Pri=90
6     12.100     192.168.1.2      224.0.0.2      HSRP       Coup   State=Active  Pri=90

← Hold timer expiré (10 s) → R2 prend Active ←

7     12.101     192.168.1.2      ff:ff:ff:ff:ff:ff  ARP    Who has 192.168.1.254? Tell 192.168.1.2
      (Gratuitous ARP — R2 annonce que c'est maintenant lui qui "possède" 192.168.1.254)

8     12.102     192.168.1.2      224.0.0.2      HSRP       Hello  State=Active  Pri=90
9     13.104     192.168.1.2      224.0.0.2      HSRP       Hello  State=Active  Pri=90
──────────────────────────────────────────────────────────────────────────────

Trafic ICMP en parallèle (PC → Internet via passerelle 192.168.1.254) :
N°    Heure      Source           Destination    Protocole  Info
──────────────────────────────────────────────────────────────────────────────
A     0.500      192.168.1.10     8.8.8.8        ICMP       Echo Request  seq=1
B     0.502      8.8.8.8          192.168.1.10   ICMP       Echo Reply    seq=1
C     1.500      192.168.1.10     8.8.8.8        ICMP       Echo Request  seq=2
D     1.502      8.8.8.8          192.168.1.10   ICMP       Echo Reply    seq=2
E     2.500      192.168.1.10     8.8.8.8        ICMP       Echo Request  seq=3
                                                             ← Pas de réponse →
F     3.500      192.168.1.10     8.8.8.8        ICMP       Echo Request  seq=4
                                                             ← Pas de réponse →
...
G    12.500      192.168.1.10     8.8.8.8        ICMP       Echo Request  seq=13
H    12.502      8.8.8.8          192.168.1.10   ICMP       Echo Reply    seq=13
     ← Reprend ! Après le GARP de R2 ←
```

---

**Questions à répondre collectivement :**

**Q1.** Entre la ligne 3 (dernier hello de R1) et la ligne 6 (coup de R2), combien de secondes se sont écoulées ? Qu'est-ce qui explique ce délai ?

_________________________________________________________________________
_________________________________________________________________________

**Q2.** Que signifie le message "Coup" (ligne 6) envoyé par R2 ?

_________________________________________________________________________

**Q3.** À quoi sert le "Gratuitous ARP" de la ligne 7 ? Sans ce message, que se passerait-il ?

_________________________________________________________________________
_________________________________________________________________________

**Q4.** Entre le début de la panne et le rétablissement du trafic ICMP (entre les séquences 3 et 13), combien de paquets ICMP ont été perdus ? Combien de secondes ont-ils été perdus ?

_________________________________________________________________________

**Q5.** En regardant les timers utilisés (Hello=1s, Hold=10s dans cet exemple), comment réduire le temps de coupure de 10s à 3s ?

_________________________________________________________________________

---

## 💡 PHASE 2 – La Pièce Manquante : le Cache ARP (5 min)

**Le formateur dessine au tableau :**

```
AVANT la bascule :
PC_A : ARP cache = { 192.168.1.254 → 0000.0C07.AC01 (MAC de R1 "Active") }
       PC_A envoie ses paquets vers MAC R1 → OK ✅

PENDANT la bascule (entre t=2.5s et t=12.1s) :
PC_A : ARP cache = { 192.168.1.254 → 0000.0C07.AC01 (MAC de R1 — TOUJOURS) }
       PC_A envoie ses paquets vers MAC R1 → Perdu car R1 est down ❌

APRÈS le GARP de R2 (t=12.1s) :
PC_A reçoit le GARP de R2 : "192.168.1.254 c'est moi (MAC R2)"
PC_A : ARP cache = { 192.168.1.254 → MAC_R2 }
       PC_A envoie ses paquets vers MAC R2 → OK ✅
```

> **Point clé :** En HSRP v1, le nouveau Active envoie 3 Gratuitous ARP pour s'assurer que tous les équipements du LAN ont bien mis à jour leur cache.

---

## ✍️ PHASE 3 – Synthèse (3 min)

**À noter — Séquence complète d'une bascule HSRP :**

```
1. Arrêt des hellos de R1 (panne ou shutdown)
2. R2 ne reçoit plus de hello → attend le Hold timer (10s ou selon config)
3. Hold timer expire → R2 envoie un message "Coup" et passe Active
4. R2 envoie des Gratuitous ARP pour mettre à jour les caches ARP du LAN
5. Le trafic reprend via R2

Temps total de coupure ≈ Hold Timer + temps GARP ≈ Hold Timer
→ Pour réduire : diminuer Hold Timer (ex: timers 1 3)
```

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
