# 🗂️ AIDE-MÉMOIRE CCNA EXAM DAY — À PLASTIFIER
## La Dernière Fiche · Tout ce dont tu as besoin · BAC PRO CIEL · E31 · S6

---

> *Lis cette fiche le matin de l'examen. 10 minutes. Pas plus.*

---

## ⚡ Sous-réseau en 10 secondes

```
/24=254h · /25=126h · /26=62h · /27=30h · /28=14h · /29=6h · /30=2h
Wildcard = inverse du masque : /24→0.0.0.255 · /30→0.0.0.3
Longest prefix match = toujours prioritaire sur DA et métrique
```

---

## 🔌 EtherChannel LACP — 30 secondes

```
active+active ✓   active+passive ✓   passive+passive ✗   active+on ✗
(P)=actif · (I)=stand-alone ✗ · (D)=down ✗
Config sur PORT-CHANNEL, pas sur les membres !
```

---

## 🌍 OSPF — l'essentiel

```
DA=110 · Hello=10s · Dead=40s · Multicast=224.0.0.5
Wildcard dans network (/24=0.0.0.255) !
show ip ospf neighbor → FULL = OK
Coût = 10⁸/bps · auto-cost reference-bandwidth 1000
```

---

## 🛡️ Sécurité — pièges classiques

```
ACL standard = filtre IP SOURCE uniquement
ACL étendue  = source + destination + port + protocole
Placer étendue PRÈS de la source · standard PRÈS destination
Deny implicite en fin d'ACL → toujours permit any à la fin si besoin
DHCP Snooping = bloque faux serveurs DHCP
err-disabled = shutdown puis no shutdown pour récupérer
```

---

## 🤖 SDN / BGP — clés

```
BGP Local-Pref : sortie AS · + HAUT = préféré · propagé iBGP
BGP AS-path    : + COURT = préféré
BGP MED        : entrée voisin · + BAS = préféré
show bgp summary : chiffre=OK · Active=session KO

SDN : Plan Contrôle (décide) séparé Plan Données (transmet)
Northbound=vers apps (REST) · Southbound=vers switches (OpenFlow)
```

---

## 📋 Distances administratives

```
Connected=0 · Static=1 · eBGP=20 · OSPF=110 · iBGP=200 · RIP=120
```

---

## ✅ Stratégie 120 minutes

```
0-60 min  → Questions faciles (< 60s chacune), marquer les douteuses
60-100 min → Questions difficiles (2-3 min max chacune)
100-120 min → Vérification finale, ne pas changer sans raison solide
Simulations PT → lire TOUTES les missions avant de commencer
Répondre à TOUT (pas de pénalité pour mauvaise réponse)
```

---

## 🚨 Les 5 erreurs fatales

```
❌ Masque au lieu de wildcard dans OSPF
❌ Rester bloqué > 3 min sur 1 question
❌ Changer une réponse sans raison solide
❌ Oublier de répondre aux questions non vues
❌ Lire trop vite les questions avec "NOT" ou "EXCEPT"
```

---

## 💪 Rappel

```
Seuil : 825 / 1000
Tu as travaillé pour ça.
Respire. Lis bien. Tu sais répondre.
```

---

*Aide-Mémoire CCNA Exam Day — À plastifier*
*BAC PRO CIEL | E31 | 3ᵉ année S6 · Cisco CCNA 200-301*
