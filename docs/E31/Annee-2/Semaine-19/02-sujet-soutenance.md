# 📄 SUJET DE SOUTENANCE – U31 ANNÉE 2
## Infrastructure Multi-Sites CIEL-Corp — Démo, Topologie, Troubleshooting

**Nom : ________________  Prénom : ________________**
**Date de soutenance : ________________  Jury : ________________**

---

## 🎯 CONTEXTE PROFESSIONNEL

> *Vous êtes technicien réseau chez **CIEL-Corp**, une PME avec deux sites (Paris et Lyon). Après plusieurs mois de travail, vous présentez aujourd'hui l'infrastructure réseau multi-sites que vous avez conçue et déployée. Vous allez présenter votre topologie, démontrer son fonctionnement, défendre vos choix techniques, puis diagnostiquer une panne injectée par le jury.*

---

## 📋 CAHIER DES CHARGES DE L'INFRASTRUCTURE

### Contraintes imposées

L'infrastructure **CIEL-Corp** doit respecter les spécifications suivantes :

#### Site Paris (siège)

| **Élément** | **Spécification** |
|---|---|
| Réseau LAN | 1 LAN minimum, /24, 50 hôtes max |
| Redondance passerelle | HSRP avec 2 routeurs, bascule < 5s, preempt configuré |
| Routage | OSPF area 0, interconnexion avec Lyon |
| Sécurité accès | ACL étendue bloquant SSH depuis le LAN vers la DMZ |
| Supervision | Nagios avec au minimum 2 checks opérationnels |

#### Site Lyon (antenne)

| **Élément** | **Spécification** |
|---|---|
| Réseau LAN | 1 LAN minimum, /24 différent de Paris |
| Routage | OSPF area 0, connexion WAN vers Paris |
| VPN | Tunnel IPsec site-à-site opérationnel avec Paris |
| Redondance passerelle | HSRP ou au minimum un routeur actif/passif |

#### Liaisons inter-sites

| **Élément** | **Spécification** |
|---|---|
| WAN principal | Lien point-à-point /30 |
| Protocole routage | OSPF area 0 |
| VPN IPsec | Chiffrement AES-256, SHA-256, PSK, mode tunnel |

---

## 📐 TOPOLOGIE MINIMALE ATTENDUE

```
               [PC-PARIS-1]    [PC-PARIS-2]
                     │               │
               ┌─────┴───────────────┴─────┐
               │        SW-PARIS           │
               └──────┬──────────┬─────────┘
                      │          │
                [R-PARIS-A]  [R-PARIS-B]       ← HSRP
                  (Active)   (Standby)
                      │          │
              WAN-A ──┘          └── WAN-B     ← optionnel (redondance WAN)
                      │
                [R-LYON-A]
                      │
               ┌──────┴──────┐
               │   SW-LYON   │
               └──────┬──────┘
                      │
               [PC-LYON-1]
```

> **Note :** La topologie ci-dessus est le minimum requis. Vous pouvez l'enrichir (VLAN, DMZ, second lien WAN, serveur Nagios, etc.) pour valoriser votre travail.

---

## 🎤 DÉROULÉ DE VOTRE SOUTENANCE (35 min)

### Phase 1 — Présentation de la topologie (5 min)

> Présentez votre infrastructure en vous appuyant sur votre schéma réseau.

Vous devez couvrir :

- [ ] Le plan d'adressage complet (réseaux, masques, passerelles)
- [ ] Les protocoles déployés et leur rôle (OSPF, HSRP, VPN, ACL, Nagios)
- [ ] Les choix de conception (pourquoi ce découpage, ces adresses, ces priorités)
- [ ] L'architecture de haute disponibilité (quels équipements sont redondants)

**Conseil :** préparez un schéma imprimé ou dessiné — la présentation du diagramme réseau est plus efficace que de lire des slides.

---

### Phase 2 — Démonstration fonctionnelle (10 min)

> Ouvrez votre fichier Packet Tracer et exécutez les tests suivants devant le jury.

**Tests obligatoires à démontrer :**

| **Test** | **Commande attendue** | **Résultat attendu** |
|---|---|---|
| T1 — Connectivité LAN Paris | `ping 192.168.X.X` depuis PC-PARIS | 100% succès |
| T2 — Connectivité inter-sites | `ping <IP_Lyon>` depuis PC-PARIS | 100% succès |
| T3 — OSPF actif | `show ip ospf neighbor` sur R-PARIS-A | FULL visible |
| T4 — HSRP état | `show standby brief` sur R-PARIS-A et R-PARIS-B | Active / Standby |
| T5 — Bascule HSRP | `shutdown` Gi0/0 R-PARIS-A → observer R-PARIS-B | R-PARIS-B passe Active |
| T6 — VPN IPsec actif | `show crypto ipsec sa` sur R-PARIS-A | pkts encrypt > 0 |
| T7 — ACL en place | `show ip access-lists` + test trafic bloqué | Matches visibles |
| T8 — Nagios (check CLI) | Tester un plugin manuellement | Output OK / WARNING / CRITICAL |

**Tests valorisants (bonus) :**

- Démontrer le retour de l'Active après preempt
- Démontrer que le tracking WAN déclenche la bascule
- Montrer `show crypto isakmp sa` avec état QM_IDLE
- Montrer `show ip route ospf` avec les routes apprises

---

### Phase 3 — Défense des choix techniques (5 min)

> Le jury vous posera 2 à 3 questions sur vos décisions de conception.

**Exemples de questions possibles :**

- *"Pourquoi avez-vous choisi une priorité HSRP de 120 pour R-PARIS-A ?"*
- *"Pourquoi avez-vous placé votre ACL sur cette interface et dans cette direction ?"*
- *"Comment avez-vous calculé la valeur de décrement pour le tracking HSRP ?"*
- *"Pourquoi l'ACL crypto de Lyon est-elle l'inverse de celle de Paris ?"*
- *"Quel est l'impact sur le réseau si OSPF n'était pas configuré ?"*

**Préparez pour chaque technologie : une justification en 2 phrases.**

---

### Phase 4 — Troubleshooting Live (10 min)

> Le jury va injecter une panne dans votre topologie. Vous devez la trouver et la corriger en 10 minutes **en expliquant votre démarche à voix haute.**

**Ce qui sera évalué :**

1. **La méthode** : commencez-vous par identifier les symptômes ? Utilisez-vous les bonnes commandes `show` ?
2. **La logique** : raisonnez-vous de façon structurée (du général au particulier) ?
3. **La correction** : proposez-vous la bonne commande de correction ?
4. **La vérification** : vérifiez-vous que la correction a fonctionné ?

**Commandes utiles pour le troubleshooting :**

```ios
! Connectivité :
ping X.X.X.X
traceroute X.X.X.X

! Routage OSPF :
show ip ospf neighbor
show ip route ospf
show ip ospf interface

! HSRP :
show standby brief
show standby

! VPN IPsec :
show crypto isakmp sa
show crypto ipsec sa
show crypto map

! ACL :
show ip access-lists
show ip interface [interface]

! Général :
show running-config
show ip interface brief
```

---

### Phase 5 — Questions jury (5 min)

> Le jury peut poser des questions complémentaires sur votre infrastructure ou sur les thèmes du module U31.

---

## 📦 CE QUE VOUS DEVEZ APPORTER

| **Document / Fichier** | **Format** | **Obligatoire ?** |
|---|---|---|
| Fichier Packet Tracer `.pkt` | Clé USB ou dossier partagé | ✅ Obligatoire |
| Schéma réseau (topologie) | Papier imprimé ou dessiné | ✅ Obligatoire |
| Plan d'adressage | Tableau papier | ✅ Obligatoire |
| Fiche récapitulative HSRP | Papier (pour la démo) | ✅ Recommandé |
| Rapport de tests (S17) | Papier | ✅ Recommandé |
| Documentation supplémentaire | Au choix | ✅ Valorisé |

---

## 📊 CRITÈRES D'ÉVALUATION (résumé)

| **Critère** | **Points** |
|---|---|
| Qualité du schéma et de la présentation | /3 |
| Complétude et fonctionnalité de la topologie | /4 |
| Démonstration des technologies (T1–T8) | /5 |
| Défense des choix techniques | /2 |
| Troubleshooting live (méthode + résultat) | /4 |
| Expression orale et posture professionnelle | /2 |
| **TOTAL** | **/20** |

**Seuil de validation U31 : 10/20**

---

## 💡 CONSEILS DE PRÉPARATION

**La semaine avant :**
- [ ] Tester TOUTES les fonctionnalités de votre topologie (ping, show, bascule)
- [ ] Préparer le schéma réseau sur papier (pas seulement dans votre tête)
- [ ] Préparer vos justifications techniques (1 argument par technologie)
- [ ] S'entraîner à présenter à voix haute (chronométrer les 5 min)
- [ ] Simuler une panne et s'entraîner à diagnostiquer

**Le jour J :**
- [ ] Arriver 15 min en avance (copier le fichier .pkt sur le PC du jury)
- [ ] Vérifier que Packet Tracer s'ouvre correctement avant la soutenance
- [ ] Avoir votre schéma et vos documents sous la main
- [ ] Respirer : un troubleshooting que vous ne trouvez pas en 10 min mais que vous approchez avec méthode vaut plus qu'un silence de 10 min

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
