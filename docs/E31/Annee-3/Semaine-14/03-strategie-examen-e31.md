# 🎯 STRATÉGIE D'EXAMEN E31 — S14 · 3ᵉ ANNÉE
## Comment aborder l'épreuve · Gestion du temps · Pièges à éviter

---

> **Nom** : ___________________________
> **Date de l'examen** : ___________________________
> **Mon score Sujet 1** : ___/100 · **Mon score Sujet 2** : ___/70

---

## ⏱️ Gérer les 4 heures de l'E31

### La réalité de l'épreuve E31

```
L'E31 est une épreuve PRATIQUE. La majorité des points (60-70%) vient du Packet Tracer.
Le temps passe TRÈS vite. Voici comment le distribuer :

Phase 1 — Lecture et analyse (15 min)
  → Lire TOUT le sujet sans toucher à PT
  → Identifier les 4-5 blocs de configuration
  → Repérer les dépendances (OSPF dépend de l'adressage → adressage d'abord)
  → Dessiner un schéma rapide sur brouillon

Phase 2 — Conception / Plan d'adressage (20 min)
  → Compléter le tableau d'adressage AVANT de configurer
  → Vérifier : pas de chevauchement · assez d'hôtes · wildcard calculée

Phase 3 — Configuration PT (2h15)
  → Suivre l'ordre logique : L2 (VLANs) → L3 (adressage) → Routage → Services
  → PINGALL après chaque bloc pour vérifier avant de continuer
  → copy run start après chaque bloc validé

Phase 4 — Documentation (25 min)
  → Schéma annoté (VLANs, areas, adresses, liens)
  → Justifications (4-5 questions courtes)
  → Tableau de tests (remplir avec les résultats réels de PT)

Phase 5 — Révision finale (5 min)
  → Vérifier que TOUS les copy run start ont été faits
  → Vérifier passive-interface sur tous les LAN OSPF
  → Relire les questions de documentation
```

### L'ordre optimal de configuration

```
ORDRE RECOMMANDÉ (du plus critique au plus risqué à sauter) :

1. Adressage IP (interfaces, Loopback, WAN) ← Base de tout
2. VLANs + trunks + ports access              ← Couche 2
3. EtherChannel (si demandé)                  ← Avant les trunks !
4. Inter-VLAN routing (sous-interfaces)       ← Après VLANs
5. OSPF / BGP                                 ← Après adressage
6. Tunnel GRE/VPN                             ← Services optionnels
7. ACL / QoS / Sécurité                       ← En dernier (risque de bloquer)
8. Documentation + tests                       ← Pendant et après

⚠️ Pourquoi ACL EN DERNIER ?
  Une ACL mal configurée peut bloquer tous les pings de validation.
  Si tu la mets en premier et qu'elle bloque le trafic, tu ne verras pas tes autres erreurs.
```

---

## 🔍 Les 5 vérifications avant de rendre

```
CHECKLIST OBLIGATOIRE avant de fermer PT :

☐ 1. copy running-config startup-config sur CHAQUE équipement
   (1 équipement oublié = config perdue si examinateur recharge PT)

☐ 2. show ip ospf neighbor → FULL sur tous les routeurs OSPF
   Si INIT ou ATTEMPT → problème à résoudre

☐ 3. Ping end-to-end : PC le plus éloigné vers PC le plus éloigné
   Si échec → diagnostiquer AVANT de rendre

☐ 4. show etherchannel summary → Po(SU), tous les ports en (P)
   Si (I) ou (D) → problème à corriger

☐ 5. Schéma : toutes les adresses IP annotées ? Areas OSPF dessinées ?
   VLANs numérotés et nommés ?
```

---

## 🧩 Les 12 points "gratuits" à ne jamais rater

```
Ces points ne nécessitent aucune compétence avancée — juste de la rigueur :

1.  Hostname sur chaque équipement (souvent demandé, facile)
2.  no shutdown sur TOUTES les interfaces (Gi, Se, Tunnel, sous-interfaces)
3.  description sur les interfaces WAN ("Lien vers FAI", "Lien Agence")
4.  copy run start après chaque bloc validé
5.  Loopback0 configurée sur les routeurs OSPF (router-id stable)
6.  passive-interface sur tous les LANs OSPF
7.  encapsulation dot1Q X avant l'adresse IP sur les sous-interfaces
8.  no shutdown sur l'interface PARENT avant les sous-interfaces
9.  ping de vérification noté dans le tableau de tests
10. Wildcard calculée correctement (0.0.0.255 pour /24, pas 255.255.255.0)
11. Trunk allowed vlan précis (vlan 10,20,30) et pas seulement "all"
12. show etherchannel summary copié dans la documentation
```

---

## 🚨 Les 8 pièges fatals — ce qui transforme une bonne note en mauvaise

```
PIÈGE 1 : MASQUE OSPF
  "network 192.168.1.0 255.255.255.0 area 0"  ← FAUX !
  → wildcard = 0.0.0.255  →  "network 192.168.1.0 0.0.0.255 area 0"
  Impact : l'interface n'est pas annoncée dans OSPF → adjacence impossible

PIÈGE 2 : ACL QUI BLOQUE TROP
  Ajouter une règle deny spécifique sans permit ip any any en fin
  → le deny implicite bloque TOUT le reste → cascade de problèmes

PIÈGE 3 : TUNNEL GRE INVERSÉ
  Sur R2 : tunnel source = IP de R1 au lieu de IP de R2
  → tunnel down → VPN non fonctionnel

PIÈGE 4 : SOUS-INTERFACE PARENT DOWN
  Interface Gi0/0 en "administratively down" → toutes les sous-interfaces down
  → Toujours "no shutdown" sur l'interface parent

PIÈGE 5 : ETHERCHANNEL MAL CONFIGURÉ
  trunk sur Gi0/1 au lieu de port-channel 1
  → la config trunk est ignorée par l'EC

PIÈGE 6 : BGP RÉSEAU ABSENT DE LA TABLE
  "network 192.168.1.0 mask 255.255.255.0" sans route vers ce réseau
  → BGP n'annonce rien

PIÈGE 7 : ACL MAL PLACÉE
  ACL étendue côté destination au lieu de la source
  → bloque le bon trafic mais laisse passer plus longtemps le trafic indésirable
  → perte de points sur le placement

PIÈGE 8 : COPY RUN START OUBLIÉ
  L'examinateur reload PT pour vérifier
  → la configuration disparaît → 0 point sur les missions non sauvegardées
```

---

## 📊 Ma carte de risques personnelle

> Remplis cette carte en te basant sur tes erreurs dans les sujets d'aujourd'hui.

```
ZONE ROUGE — Je dois absolument retravailler :
1. ___________________________________________________________________________
2. ___________________________________________________________________________

ZONE ORANGE — Je fais parfois des erreurs :
1. ___________________________________________________________________________
2. ___________________________________________________________________________

ZONE VERTE — Je maîtrise :
1. ___________________________________________________________________________
2. ___________________________________________________________________________

MON OBJECTIF DE NOTE E31 : _______ / 20
MON PLAN D'ACTION pour les X jours restants :

Jour 1-2 : ___________________________________________________________________
Jour 3-4 : ___________________________________________________________________
Jour 5   : Simulation complète chronométrée (4h) + correction
Jour 6+  : Relecture aide-mémoires + labs rapides
```

---

## 💡 Conseils spécifiques selon le niveau

### Si tu es à < 50% aux deux sujets

```
Priorité absolue : les fondamentaux
  ☐ Adressage IP : calcul de sous-réseaux en < 30 secondes
  ☐ VLANs + trunks : faire le lab de base 3 fois de suite
  ☐ OSPF : ne pas essayer les multi-aires → single area d'abord
  ☐ Ping qui fonctionne : c'est l'objectif minimum
```

### Si tu es entre 50% et 70%

```
Consolider les points fréquents
  ☐ Passive-interface : faire le réflexe systématique
  ☐ Wildcard : tableau de conversion à mémoriser
  ☐ EtherChannel : mode active/active + trunk sur Po (pas sur Gi)
  ☐ ACL étendue + placement + permit any en fin
```

### Si tu es à > 70%

```
Chercher les points bonus
  ☐ QoS : configurer LLQ en moins de 5 min
  ☐ BGP : manipulation Local-Pref via route-map
  ☐ GRE tunnel : configurer + OSPF via tunnel
  ☐ Documentation : schéma pro avec tous les labels
  ☐ Justifications : réponses précises avec les bons termes
```

---

*Stratégie d'Examen E31 — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S14*
*Document apprenant — Conserver jusqu'à l'épreuve*
