# 🎤 GUIDE DE PRÉPARATION ORAL — E31 · S16 · 3ᵉ ANNÉE
## Structure de la présentation · Questions types · Démonstration live

---

> **Distribuer aux apprenants à 11h15** (pendant la transition pratique → oral)
> **Temps de préparation** : 15-20 minutes pendant que les premiers passent

---

## ⏱️ Déroulé des 20 minutes

```
0 – 5 min   : Présentation par l'apprenant (sans interruption du jury)
5 – 15 min  : Questions du jury (techniques + démonstration live)
15 – 18 min : Questions de compréhension ("et si...")
18 – 20 min : Conclusion par l'apprenant — "ce que j'améliorerais"
```

---

## 🗣️ Structure de ta présentation (5 minutes)

### Modèle en 4 temps

```
TEMPS 1 — Introduction (30 secondes)
  "NEXALINK est une entreprise avec deux sites. J'ai été chargé(e) de déployer
  une infrastructure réseau multi-sites répondant aux besoins suivants : [liste rapide]."

TEMPS 2 — Architecture (2 minutes)
  Montrer le schéma. Décrire en partant du plus général au plus spécifique :
  → "Le site Lyon est composé de... Le site Marseille de..."
  → "J'ai utilisé OSPF multi-aires parce que..."
  → "L'EtherChannel ici assure la redondance entre..."
  → "La QoS priorise le trafic VoIP sur le lien WAN."

TEMPS 3 — Démonstration (2 minutes)
  Ouvrir PT. Montrer 2-3 commandes en direct :
  → show ip ospf neighbor → FULL ✓
  → ping PC_Direction → PC_Technique → Succès ✓
  → show etherchannel summary → Po1(SU) ✓

TEMPS 4 — Réflexion critique (30 secondes)
  "Ce que j'améliorerais : j'aurais pu ajouter une ACL pour protéger la DMZ
  et un VPN pour sécuriser le lien WAN. La documentation aurait pu être plus détaillée."
```

---

## ❓ Questions types — Prépare tes réponses

### Questions sur l'architecture

```
Q : "Pourquoi OSPF multi-aires et pas single-area ?"
R : "OSPF multi-aires limite la propagation des LSA. L'Area 0 backbone
    regroupe les réseaux Lyon, et l'Area 1 isole le lien WAN et Marseille.
    Cela améliore la scalabilité et réduit les recalculs SPF si un lien
    de Marseille tombe — l'Area 0 n'est pas impactée."

Q : "Pourquoi EtherChannel entre les deux switches Lyon ?"
R : "L'EtherChannel agrège 2 liens Gigabit en un lien logique de 2 Gbps.
    Si l'un des liens tombe, le trafic continue automatiquement sur le second.
    C'est de la redondance et de l'agrégation en un seul mécanisme."

Q : "Qu'est-ce que passive-interface fait dans OSPF ?"
R : "passive-interface empêche l'envoi de paquets Hello OSPF sur cette interface.
    Je l'ai appliqué sur les interfaces LAN car les PCs ne font pas tourner OSPF.
    Ça évite d'établir des voisinages non désirés et économise la bande passante."
```

### Questions sur la configuration

```
Q : "Pourquoi une wildcard dans la commande network OSPF ?"
R : "La commande network d'OSPF utilise un wildcard mask, pas un masque réseau.
    C'est l'inverse du masque : 0 = bit doit correspondre, 1 = bit ignoré.
    Pour /26, le masque est 255.255.255.192 donc la wildcard est 0.0.0.63."

Q : "Que se passe-t-il si le lien WAN Lyon-Marseille tombe ?"
R : "OSPF détecte la perte d'adjacence en 40 secondes (4 × Hello). R_MARSEILLE
    perd les routes O IA vers Lyon. Le trafic s'arrête. Pour éviter ça,
    on pourrait configurer une route de secours ou un deuxième lien WAN."

Q : "Expliquez votre QoS VoIP."
R : "J'ai utilisé une Low Latency Queue avec priority percent 30. La classe VOIX
    identifie les paquets DSCP EF (valeur 46). Ces paquets sont traités en priorité
    stricte, ce qui garantit une latence < 150ms et une gigue < 30ms.
    Sans QoS, un gros téléchargement pourrait saturer le WAN et couper les appels."
```

### Questions "et si..." (niveau avancé)

```
Q : "Si on ajoutait un 3ème site demain, que changeriez-vous ?"
R : "Je créerais une nouvelle Area OSPF (Area 2) pour le 3ème site.
    R_LYON resterait l'ABR backbone. Je n'aurais pas à reconfigurer
    les sites existants — c'est l'avantage du multi-aire."

Q : "Comment sécuriseriez-vous ce réseau pour une mise en production réelle ?"
R : "J'ajouterais :
    - Des ACL pour filtrer l'accès à la DMZ (seulement HTTP/HTTPS depuis l'extérieur)
    - Un tunnel VPN IPsec pour chiffrer le lien WAN
    - SSH et désactivation de Telnet sur tous les équipements
    - 802.1X sur les ports access pour l'authentification des postes"
```

---

## 🖥️ Démonstration live — Ce que le jury attend

```
DÉMONSTRATIONS À PRÉPARER (dans l'ordre de priorité) :

1. OSPF convergé (obligatoire) :
   R_LYON# show ip ospf neighbor
   → Montrer : R_MARSEILLE en état FULL

2. Connectivité E2E (obligatoire) :
   Depuis PC_Direction :
   PC_Direction> ping 10.20.2.10 (PC_Technique à Marseille)
   → Montrer : 5 paquets envoyés, 5 reçus

3. EtherChannel (si demandé) :
   SW_CORE_LYON# show etherchannel summary
   → Montrer : Po1(SU), Gi0/1(P), Gi0/2(P)

4. QoS (si demandé) :
   R_LYON# show policy-map interface GigabitEthernet0/1
   → Montrer : classe VOIX avec priority

5. Table de routage (si demandé) :
   R_MARSEILLE# show ip route
   → Pointer : les routes O IA vers 10.20.1.0, 10.20.3.0, 10.20.4.0
```

---

## 💬 Phrases professionnelles utiles

```
Pour introduire un choix technique :
  "J'ai choisi [X] car [raison technique précise]."
  "La contrainte [Y] m'a amené(e) à opter pour [X]."

Pour admettre une lacune (valorisé par le jury) :
  "Je n'ai pas eu le temps de configurer [X], mais j'aurais fait [Y]."
  "Cette partie fonctionne, mais je sais qu'elle pourrait être améliorée par [Z]."

Pour répondre à une question difficile :
  "Je ne suis pas sûr(e) de la réponse exacte, mais je sais que le principe est [X]."
  (Ne pas bluffer — le jury préfère l'honnêteté à une réponse fausse assurée)

Pour conclure :
  "En résumé, l'infrastructure NEXALINK répond aux besoins essentiels du cahier des charges.
  Les points que j'améliorerais sont [X et Y]. Des questions ?"
```

---

## 🚫 Ce qui fait perdre des points à l'oral

```
❌ Lire ses notes intégralement → montre qu'on n'a pas compris
❌ Répondre "je sais pas" sans essayer → montrer une démarche vaut des points
❌ Citer des commandes sans expliquer à quoi elles servent
❌ Ne pas regarder les membres du jury (parler à l'écran)
❌ S'excuser en permanence ("c'est pas terrible mais...")
❌ Trop détailler des parties anecdotiques, sauter les parties clés
❌ Dépasser 6 minutes sans avoir abordé l'essentiel
```

---

## ✅ Ce qui fait gagner des points à l'oral

```
✓ Schéma à la main prêt (pas besoin d'ouvrir PT pour expliquer)
✓ Vocabulaire technique précis et naturel (pas récité)
✓ Démonstration live fluide (commandes tapées sans hésitation)
✓ Réflexion critique sur son propre travail
✓ Lien avec le monde professionnel ("en entreprise, on ferait aussi X")
✓ Proposer une amélioration non demandée dans le sujet
```

---

*Guide Préparation Oral E31 — BAC PRO CIEL | E31 | 3ᵉ année S16*
*Distribuer après le rendu de la partie pratique*
