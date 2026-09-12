# 📋 SYNTHÈSE BILAN E31 — S20 · 2ᵉ ANNÉE
## Ce que tu sais faire · Ce qui reste · Conseils pour l'épreuve

---

> **Nom** : ___________________________
> **Date** : ___________________________

---

## 🗺️ La carte complète du parcours E31

### Ce que tu as appris, semaine par semaine

```
2ᵉ ANNÉE — MODULE E31

S2   → Routage statique + table de routage · dépannage pannes
S3   → OSPF concepts : LSA, LSDB, SPF, aires, Router-ID, coût
S6   → QoS : marquage DSCP, files d'attente, priorisation VoIP
S9   → WiFi 802.1X : RADIUS, EAP-TLS, architecture WLAN
S11  → Syslog centralisé : rsyslog, filtres, logrotate, SIEM
S13  → EtherChannel LACP : agrégation, load balancing, dépannage
S14  → CCNA révisions : QCM 200-301, labs en temps limité
S16  → Projet A2 : infrastructure multi-sites OSPF+VPN+QoS+HA
S18  → Procédures exploitation : sauvegarde TFTP, MàJ IOS, PRA
S20  → Bilan A2 + auto-évaluation CCNA Readiness (cette séance)
```

---

## ✅ Ce que tu dois savoir faire le jour de l'épreuve E31

### Les 10 configurations incontournables

```
1. ip address + no shutdown                         → toujours
2. ip route [réseau] [masque] [next-hop]            → routage statique
3. router ospf 1 + network + wildcard + area        → OSPF
4. switchport mode trunk                            → trunks
5. channel-group 1 mode active                      → EtherChannel
6. interface port-channel 1 / switchport mode trunk → EC trunk
7. priority percent 30 / class VOIX / service-policy → QoS
8. ip route 0.0.0.0 0.0.0.0 [nh2] 5               → route flottante
9. copy running-config tftp:                        → sauvegarde
10. ping / traceroute / show ip route               → vérification
```

### Les 10 commandes de vérification incontournables

```
show ip route                → table de routage complète
show ip ospf neighbor        → adjacences OSPF (FULL ?)
show etherchannel summary    → états Po1 (SU, P, I, D)
show interfaces trunk        → VLANs autorisés sur trunks
show vlan brief              → VLANs + ports membres
show policy-map interface    → QoS appliquée ?
show interfaces Tunnel0      → tunnel GRE actif ?
show version                 → version IOS
ping [IP] source [interface] → connectivité depuis une source
traceroute [IP]              → chemin exact emprunté
```

---

## 📐 Les formules et valeurs à connaître par cœur

```
OSPF :
  DA = 110 · Coût = 10⁸ / bande passante (bps)
  Wildcard /24 = 0.0.0.255 · /30 = 0.0.0.3 · /32 = 0.0.0.0
  Hello = 10s · Dead = 40s · Multicast = 224.0.0.5

EtherChannel :
  active+active ✓ · active+passive ✓ · passive+passive ✗ · active+on ✗
  (P) actif · (I) stand-alone · (D) down · (s) suspendu

QoS :
  DSCP EF = 46 (VoIP) · DSCP 0 = Best Effort
  LLQ = priority percent [X] · CBWFQ = bandwidth percent [X]

Sauvegarde :
  copy run tftp: → externe · copy run start → NVRAM locale
  Convention : [HOSTNAME]_running_[AAAA-MM-JJ]_[HHMM].cfg

LACP :
  Mode active = initie · Mode passive = répond · Mode on = statique
```

---

## 🔴 Les 12 erreurs qui font perdre des points à l'épreuve

```
❌  1. Masque au lieu de wildcard dans OSPF
       ip network 192.168.10.0 255.255.255.0 area 0  ← FAUX
       ip network 192.168.10.0 0.0.0.255 area 0      ← CORRECT

❌  2. Oublier no shutdown après ip address
       → Interface reste administratively down

❌  3. Config trunk sur Gi0/x au lieu de port-channel
       → EtherChannel ignore la config sur les membres physiques

❌  4. Modes LACP incompatibles (active + on)
       → Po1 reste en SD (down)

❌  5. Oublier passive-interface sur les LANs OSPF
       → Paquets Hello inutiles sur les VLANs utilisateurs

❌  6. Route flottante avec même DA que la principale
       → Les deux routes coexistent (load balancing involontaire)

❌  7. Service-policy QoS sur la mauvaise interface
       → Doit être sur le lien WAN en OUTPUT (pas sur les LANs)

❌  8. Pas de route retour (asymétrie aller/retour)
       → Ping aller OK, retour timeout

❌  9. Tunnel GRE sans no shutdown
       → Tunnel0 reste administratively down

❌ 10. copy run start sans copy run tftp:
       → Pas de sauvegarde externe → rollback impossible après sinistre

❌ 11. Procédure MàJ IOS sans sauvegarde préalable
       → Si ça rate, impossible de revenir en arrière

❌ 12. Oublier copy run start à la fin
       → Toute la config est perdue au prochain redémarrage
```

---

## 🎯 Conseils stratégiques pour l'épreuve E31

### Avant l'épreuve (J-7)

```
→ Refaire le Lab 3 de S14 (infrastructure complète) en 50 min chrono
→ Relire la fiche méthode d'examen (S14 doc 03) — règle des 3 passes
→ Mémoriser les 10 commandes incontournables
→ Relire son propre dossier A2 : être capable de l'expliquer en 5 min
→ Dormir 8h la veille — la fatigue tue la précision sous pression
```

### Pendant l'épreuve

```
→ LIRE TOUT LE SUJET AVANT de toucher au clavier (2-3 min)
→ Dessiner un schéma rapide sur brouillon (même si pas demandé)
→ Configurer couche par couche : L1 → L2 → L3
→ Ping après CHAQUE bloc de configuration
→ Gérer le temps : si bloqué > 3 min → passer, revenir après
→ copy run start à chaque étape terminée
```

### Les points gratuits à ne jamais rater

```
→ Hostname sur chaque équipement (facile, souvent demandé)
→ no shutdown partout
→ Adressage IP cohérent avec le plan fourni
→ show ip route sur chaque routeur (1 ligne = 1 point souvent)
→ ping end-to-end final (les correcteurs testent ça en premier)
```

---

## 🔭 Et après l'épreuve E31 ?

### Portes ouvertes par la certification CCNA

```
Métiers accessibles :
  → Technicien réseau junior (N2)
  → Administrateur systèmes et réseaux
  → Technicien support infrastructure
  → Intégrateur réseau

Salaires moyens France (jeune diplômé + CCNA, 2024) :
  → 24 000 – 30 000 € brut/an en sortie de BAC PRO + CCNA

Poursuites d'études avec BAC PRO CIEL :
  → BTS SIO (Services Informatiques aux Organisations)
  → BTS CIEL (Cybersécurité, Informatique, Électronique)
  → Licence Pro Réseaux et Télécommunications
  → Titre RNCP niveau 5 (technicien cybersécurité)

Prochaines certifications Cisco après CCNA :
  → CCNP Enterprise (niveau expert)
  → CCNA CyberOps (cybersécurité)
  → Cisco DevNet Associate (automatisation réseau)
```

---

## 📝 Ma feuille de route personnelle

```
Mon objectif après E31 :
□ Viser la certification CCNA officielle
□ Continuer en BTS : ____________________________
□ Entrer directement en emploi comme : __________
□ Autre : ______________________________________

Ma date cible pour l'épreuve E31 : _____________
Mon score CCNA Readiness aujourd'hui : ___/40
Mon score cible dans 4 semaines : ___/40

Ce que je fais dès demain :
→ ________________________________________
```

---

*Synthèse Bilan E31 — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S20*
*Document apprenant — À conserver jusqu'à l'épreuve*
