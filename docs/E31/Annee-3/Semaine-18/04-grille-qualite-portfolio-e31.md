# 📊 GRILLE QUALITÉ DOSSIER E31 + CHECKLIST PORTFOLIO — S18 · 3ᵉ ANNÉE
## Évaluer son dossier avant remise · Portfolio numérique E31

---

> **Nom** : ___________________________
> **Date d'auto-évaluation** : ___________________________
> **Infrastructure documentée** : ☐ NEXALINK (S16) ☐ Projet A2 (S16-2A) ☐ Autre : ___

---

## 🏅 GRILLE D'AUTO-ÉVALUATION DU DOSSIER E31

> Utilise cette grille AVANT de remettre ton dossier.
> Chaque critère manquant = points perdus sur C3.1.

### A — Mise en forme et structure (/20 pts)

| Critère | 0 | 1 | 2 | Notes |
|---|---|---|---|---|
| Page de garde complète (titre, référence, version, date, auteur, statut) | | | | |
| Table des matières avec numéros de pages | | | | |
| Pagination (numéros de pages sur toutes les pages) | | | | |
| En-tête ou pied de page (nom du projet + version) | | | | |
| Police cohérente (1-2 polices max, tailles hiérarchisées) | | | | |
| Titres de sections numérotés (1, 1.1, 1.2...) | | | | |
| Glossaire des acronymes présent | | | | |
| Registre des modifications présent | | | | |
| Document exporté en PDF (format final) | | | | |
| Orthographe vérifiée (aucune faute grossière) | | | | |
| **Sous-total mise en forme** | | | | **/20** |

### B — Contenu technique (/40 pts)

| Critère | 0 | 1 | 2 | Notes |
|---|---|---|---|---|
| **Contexte** : entreprise et besoin clairement décrits | | | | |
| **Objectifs** : listés avec indicateurs de réussite | | | | |
| **Schéma logique** : équipements nommés + VLANs colorés | | | | |
| **Schéma logique** : areas OSPF délimitées + adresses IP | | | | |
| **Schéma physique** : modèles, ports, types câbles | | | | |
| **Plan adressage** : en tableau (pas en texte) | | | | |
| **Plan adressage** : masques CIDR + wildcard OSPF | | | | |
| **Configs commentées** : chaque ligne clé expliquée | | | | |
| **Configs commentées** : passive-interface justifié | | | | |
| **Configs commentées** : wildcard OSPF correcte + commentée | | | | |
| **Justifications** : OSPF multi-aire justifié | | | | |
| **Justifications** : EtherChannel justifié | | | | |
| **Justifications** : QoS justifiée | | | | |
| **Justifications** : passive-interface justifié | | | | |
| **Tests** : tableau avec ≥ 8 tests documentés | | | | |
| **Tests** : résultats réels (pas supposés) + commandes | | | | |
| **Procédures** : ≥ 2 procédures au format professionnel | | | | |
| **Procédures** : chaque procédure contient un rollback | | | | |
| **PRA** : ≥ 2 scénarios de panne | | | | |
| **PRA** : RTO/RPO chiffrés pour chaque scénario | | | | |
| **Sous-total contenu technique** | | | | **/40** |

### C — Qualité rédactionnelle (/10 pts)

| Critère | 0 | 1 | 2 | Notes |
|---|---|---|---|---|
| Justifications précises (termes techniques exacts) | | | | |
| Pas de formulations vagues ("ça marche", "c'est utile") | | | | |
| Langue professionnelle (pas de "on a fait", "j'ai mis") | | | | |
| Cohérence entre schéma, tableau et configuration | | | | |
| Longueur appropriée (8-12 pages, ni trop court ni inutilement long) | | | | |
| **Sous-total rédactionnel** | | | | **/10** |

### TOTAL

| Section | /pts | Score |
|---|---|---|
| A — Mise en forme | /20 | |
| B — Contenu technique | /40 | |
| C — Rédactionnel | /10 | |
| **TOTAL** | **/70** | |

**Conversion sur 20** : Score × 20/70 ≈ **___/20**

---

## 📌 Les 5 erreurs qui font descendre d'une note

```
ERREUR 1 : Plan d'adressage en texte libre
  "R_LYON a l'adresse 10.20.1.1 sur son interface vers le VLAN 100..."
  → Doit TOUJOURS être un tableau

ERREUR 2 : Configuration collée sans un seul commentaire
  router ospf 1
  router-id 10.20.255.1
  network 10.20.1.0 0.0.0.127 area 0
  → Chaque ligne doit avoir une explication à côté (! commentaire IOS)

ERREUR 3 : Justifications vagues
  "J'ai utilisé OSPF parce que c'est un bon protocole de routage"
  → Doit mentionner : dynamique, convergence, multi-aire, scalabilité...

ERREUR 4 : Tableau de tests avec résultats fictifs
  T3 : show ip ospf neighbor → FULL ← "résultat obtenu" copié sans vérifier
  → Copier la vraie sortie PT (ou noter "KO, problème identifié : ...")

ERREUR 5 : PRA sans RTO chiffré
  "En cas de panne WAN, rétablir rapidement le service"
  → Doit dire : "RTO = 30 minutes. Si non résolu : escalade opérateur"
```

---

## 🗂️ CHECKLIST PORTFOLIO NUMÉRIQUE E31

> Avant de clore le portfolio, vérifier que tous les documents requis sont présents.

### Documents à inclure dans le portfolio E31

```
INFRASTRUCTURE (production S16-2A / S16-3A) :
  ☐ Fichier PT de l'infrastructure complète (.pkt)
  ☐ DAT complet en PDF (≥ 8 pages)
  ☐ Schéma logique en PNG/PDF haute résolution
  ☐ Schéma physique en PNG/PDF
  ☐ Plan d'adressage en tableau (extrait du DAT ou fichier séparé)

PROCÉDURES (production S18-2A / S18-3A) :
  ☐ Procédure de sauvegarde (PROC-001)
  ☐ Procédure de modification en production (PROC-002)
  ☐ Procédure de rétablissement WAN (PROC-003)
  ☐ PRA avec 2 scénarios minimum

PREUVES DE COMPÉTENCES :
  ☐ Capture show ip ospf neighbor (FULL) → C2.2
  ☐ Capture show etherchannel summary → C2.2
  ☐ Capture ping E2E réussi → C2.3
  ☐ Capture show ip access-lists (si ACL configurée) → C2.2
  ☐ Grille de compétences E31 signée (S20-2A) → bilan

BONUS (valorisé mais non obligatoire) :
  ☐ Script Ansible ou Netmiko utilisé (S10-3A)
  ☐ Captures Wireshark annotées
  ☐ Rapport de test de charge ou performance
```

### Organisation des fichiers du portfolio

```
portfolio_E31_[NOM_PRENOM]/
├── 01_DAT/
│   ├── DAT_NEXALINK_v1.0.pdf
│   ├── Schema_Logique_v1.0.png
│   └── Schema_Physique_v1.0.png
├── 02_Configurations/
│   ├── R_LYON_running_2024-05-10.cfg
│   ├── R_MARSEILLE_running_2024-05-10.cfg
│   ├── SW_CORE_LYON_running_2024-05-10.cfg
│   └── SW_ACC_LYON_running_2024-05-10.cfg
├── 03_Procedures/
│   ├── PROC-001_Sauvegarde.pdf
│   ├── PROC-002_Modification_Production.pdf
│   └── PROC-003_PRA_Panne_WAN.pdf
├── 04_Preuves_Competences/
│   ├── show_ospf_neighbor_FULL.png
│   ├── show_etherchannel_summary.png
│   ├── ping_E2E_reussi.png
│   └── show_policy_map_QoS.png
└── 05_Bilan/
    └── Grille_Competences_E31_signee.pdf
```

---

## 💡 Conseils finaux pour un dossier E31 remarquable

```
1. LE SCHÉMA PARLE EN PREMIER
   Avant de lire un seul mot, l'examinateur regarde le schéma.
   Un schéma clair avec VLANs colorés et areas annotées = première impression positive.

2. LES TABLEAUX RASSURENT
   Plan d'adressage en tableau = "cet apprenant est organisé et rigoureux".
   Texte libre = "cet apprenant ne sait pas présenter de l'information technique".

3. LES COMMENTAIRES DISTINGUENT
   Une config commentée montre que tu comprends ce que tu as fait.
   Une config brute montre que tu l'as peut-être copiée sans comprendre.

4. LE PRA MONTRE LA MATURITÉ
   Penser aux pannes et aux procédures de reprise = vision professionnelle.
   Beaucoup d'apprenants l'oublient ou le bâclent → différenciation immédiate.

5. LA COHÉRENCE RASSURE
   Même adresses IP dans le schéma, le tableau et la configuration.
   Des incohérences (IP différentes dans le schéma et la config) = perte de crédibilité.
```

---

*Grille Qualité + Checklist Portfolio — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S18*
*Compétences : C3.1 · C3.2 · C2.3 · Portfolio E31*
