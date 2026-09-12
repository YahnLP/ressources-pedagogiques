# 🔬 TRAVAUX PRATIQUES — S18 · 2ᵉ ANNÉE · E31
## Sauvegardes TFTP · Procédures d'exploitation · PRA — Projet A2 DIGITEC

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 75 minutes · **Fiche de cours autorisée** · **Packet Tracer + éditeur texte**
> **Fichier .pkt** : Le fichier A2 complet de votre équipe (S16)
> **Épreuve ciblée** : **E31** – Administration systèmes

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **C2.6** | Sauvegarder et restaurer une configuration IOS |
| **C3.1** | Rédiger des procédures d'exploitation professionnelles |
| **C3.2** | Planifier la maintenance et rédiger un PRA |
| **S5.2** | Configurer et utiliser un serveur TFTP |

---

## 🗺️ Rappel de la topologie DIGITEC (Projet A2)

```
SIÈGE (Lyon)            WAN Principal          AGENCE B (Grenoble)
R_SIEGE ─────────── 10.1.2.0/30 ─────────── R_AGENCE_B
    │                                              │
R_SIEGE_BACKUP ─── 10.1.3.0/30 (secours) ────────┘
    │
10.1.4.0/30
    │
R_DC ── SRV_Web (192.168.200.10)
        SRV_VoIP (192.168.200.20)

Serveur TFTP : 192.168.10.100 (dans le LAN Siège VLAN 10)
```

---

## 🟢 PARTIE 1 — Configurer le serveur TFTP (10 min)

### Sur le serveur TFTP (PT Generic Server)

**1.1** — Sur le Serveur TFTP dans Packet Tracer, active le service TFTP :

```
Services → TFTP → On
```

**1.2** — Note l'adresse IP du serveur TFTP :

```
Adresse IP du serveur TFTP : _______________________
Est-il dans le bon VLAN pour être joignable depuis R_SIEGE ? ☐ Oui ☐ Non
```

**1.3** — Teste la connectivité depuis R_SIEGE :

```cisco
R_SIEGE# ping 192.168.10.100
```

```
Résultat : ☐ Succès !!!!! ☐ Échec
Si échec → vérifier l'inter-VLAN routing et la sous-interface Gi0/0.10
```

---

## 🟡 PARTIE 2 — Sauvegarder toutes les configurations (25 min)

> Tu vas sauvegarder les configurations des **5 équipements principaux** du projet A2.
> Convention de nommage imposée : `[HOSTNAME]_running_[ta_date]_0800.cfg`

### Procédure pour chaque équipement

**2.1** — Sur R_SIEGE, exécute et note les résultats :

```cisco
R_SIEGE# show version | include IOS
```

```
Version IOS actuelle : _______________________________________________________
```

```cisco
R_SIEGE# copy running-config tftp:
Address or name of remote host []? _______________
Destination filename [r_siege-confg]? _______________
```

```
Résultat : ☐ [OK] !!!!! copié  ☐ Erreur : _______________________________
```

**2.2** — Répète l'opération pour les 4 autres équipements. Complète le tableau :

| Équipement | Commande tapée | Nom du fichier sur TFTP | Résultat |
|---|---|---|---|
| R_AGENCE_B | `copy running-config tftp:` | | ☐ OK ☐ KO |
| R_DC | `copy running-config tftp:` | | ☐ OK ☐ KO |
| SW_CORE_A | `copy running-config tftp:` | | ☐ OK ☐ KO |
| R_SIEGE_BACKUP | `copy running-config tftp:` | | ☐ OK ☐ KO |

**2.3** — Vérifie sur le serveur TFTP que les fichiers sont présents :

```
Services → TFTP → lister les fichiers
```

```
Fichiers présents sur le serveur TFTP :
1. ____________________________________________
2. ____________________________________________
3. ____________________________________________
4. ____________________________________________
5. ____________________________________________
```

---

## 🟠 PARTIE 3 — Simuler une mauvaise configuration et restaurer (20 min)

### Simulation d'incident

**3.1** — Sur SW_CORE_A, **supprime le VLAN 20** (VoIP) intentionnellement :

```cisco
SW_CORE_A# configure terminal
SW_CORE_A(config)# no vlan 20
SW_CORE_A(config)# end
```

**3.2** — Vérifie l'impact :

```cisco
SW_CORE_A# show vlan brief
```

```
VLAN 20 (VoIP) encore présent ? ☐ Oui ☐ Non
Quel est l'impact sur les téléphones IP ? ___________________________________
```

**3.3** — Tente un ping depuis un téléphone IP vers SRV_VoIP :

```
ping 192.168.200.20 depuis IP_Phone_Siege → ☐ Succès ☐ Échec
```

### Procédure de restauration

**3.4** — Applique la procédure de rollback depuis TFTP :

```cisco
SW_CORE_A# copy tftp: running-config
Address or name of remote host []? 192.168.10.100
Source filename []? [nom_de_ton_fichier_sauvegardé]
```

**3.5** — Vérifie la restauration :

```cisco
SW_CORE_A# show vlan brief
```

```
VLAN 20 (VoIP) restauré ? ☐ Oui ☐ Non
Temps total de l'incident à la restauration : _______ minutes
```

**3.6** — Teste à nouveau le téléphone IP :

```
ping 192.168.200.20 depuis IP_Phone_Siege → ☐ Succès ☐ Échec
```

**3.7** — Réflexion : si le switch n'avait pas eu de sauvegarde TFTP externe, que se serait-il passé ?

```
Sans sauvegarde TFTP : ________________________________________________________
Temps de restauration estimé (reconfiguration manuelle) : ______________________
```

---

## 🔵 PARTIE 4 — Rédiger les procédures d'exploitation (20 min)

> Rédige 2 procédures d'exploitation pour l'infrastructure DIGITEC.
> Utilise le format professionnel vu en cours.

### Procédure 1 — Sauvegarde quotidienne des configurations

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PROCÉDURE : SAUVEGARDE QUOTIDIENNE DES CONFIGURATIONS                 │
│  Auteur : _____________________ Date : _______________ Version : _____  │
│  Validé par : __________________                                        │
├─────────────────────────────────────────────────────────────────────────┤
│  CONDITIONS PRÉALABLES :                                                │
│  • Serveur TFTP accessible à l'adresse : _______________________________ │
│  • Aucune fenêtre de maintenance requise (opération non impactante)     │
│  • Fréquence : ______________________ (heure recommandée : __________)  │
├─────────────────────────────────────────────────────────────────────────┤
│  ÉTAPES D'EXÉCUTION :                                                   │
│  1. Se connecter à _________________ via SSH/console                   │
│  2. Vérifier la connectivité TFTP :                                     │
│     ___________________________________________________________________ │
│  3. Sauvegarder la running-config :                                     │
│     ___________________________________________________________________ │
│     Nom du fichier : ___________________________________________________  │
│  4. Répéter les étapes 1-3 pour : ______________________________________ │
│     ___________________________________________________________________  │
│  5. Vérifier la présence des fichiers sur le serveur TFTP               │
├─────────────────────────────────────────────────────────────────────────┤
│  VALIDATION :                                                           │
│  ☐ Tous les fichiers présents sur le serveur TFTP                      │
│  ☐ Tailles des fichiers cohérentes (non nuls)                          │
│  ☐ Convention de nommage respectée                                      │
├─────────────────────────────────────────────────────────────────────────┤
│  ROLLBACK : N/A (opération de lecture seule — aucun rollback requis)   │
├─────────────────────────────────────────────────────────────────────────┤
│  DURÉE ESTIMÉE : _______ minutes        IMPACT UTILISATEURS : Aucun    │
└─────────────────────────────────────────────────────────────────────────┘
```

### Procédure 2 — Modification d'une configuration en production

```
┌─────────────────────────────────────────────────────────────────────────┐
│  PROCÉDURE : MODIFICATION DE CONFIGURATION EN PRODUCTION               │
│  Auteur : _____________________ Date : _______________ Version : _____  │
│  Validé par : __________________                                        │
├─────────────────────────────────────────────────────────────────────────┤
│  CONDITIONS PRÉALABLES :                                                │
│  • Fenêtre de maintenance requise : ☐ Oui → Plage horaire : __________ │
│  • Approbation du responsable réseau : _______________________________ │
│  • Sauvegarde préalable obligatoire : ________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  ÉTAPES D'EXÉCUTION :                                                   │
│  Étape 0 — SAUVEGARDE PRÉALABLE (obligatoire) :                        │
│    copy running-config tftp:                                            │
│    Fichier : ____________________________________________________________ │
│    ☐ Fichier reçu et vérifié sur le serveur TFTP                       │
│  Étape 1 — Effectuer la modification :                                 │
│    _____________________________________________________________________│
│  Étape 2 — Tests de validation :                                       │
│    _____________________________________________________________________│
│    _____________________________________________________________________│
│  Étape 3 — Si tests OK : copy running-config startup-config            │
│  Étape 4 — Documenter le changement                                    │
├─────────────────────────────────────────────────────────────────────────┤
│  ROLLBACK (si tests KO) :                                              │
│  1. ___________________________________________________________________ │
│  2. ___________________________________________________________________ │
│  3. Notifier l'équipe et ouvrir un ticket d'incident                  │
├─────────────────────────────────────────────────────────────────────────┤
│  RTO EN CAS DE ROLLBACK : _______ minutes                              │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Configurer un serveur TFTP + tester la connectivité | ☐ | ☐ | ☐ |
| Sauvegarder une running-config vers TFTP | ☐ | ☐ | ☐ |
| Appliquer la convention de nommage horodatée | ☐ | ☐ | ☐ |
| Restaurer une config depuis TFTP (rollback) | ☐ | ☐ | ☐ |
| Rédiger une procédure au format professionnel | ☐ | ☐ | ☐ |
| Identifier les 5 règles d'or des procédures | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Partie 2 — 5 sauvegardes TFTP réussies avec bon nommage | /8 |
| Partie 3 — Incident simulé + restauration réussie | /7 |
| Partie 4 — 2 procédures rédigées au format professionnel | /10 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Partie 2 — Sauvegardes

Les fichiers attendus sur le serveur TFTP :
```
R_SIEGE_running_[date]_0800.cfg
R_AGENCE_B_running_[date]_0800.cfg
R_DC_running_[date]_0800.cfg
SW_CORE_A_running_[date]_0800.cfg
R_SIEGE_BACKUP_running_[date]_0800.cfg
```

## Partie 3 — Restauration

```
Après `no vlan 20` sur SW_CORE_A :
- show vlan brief → VLAN 20 absent
- ping IP_Phone → SRV_VoIP → timeout

Rollback :
copy tftp: running-config
→ Merge : le VLAN 20 revient dans la config
→ show vlan brief → VLAN 20 présent
→ ping IP_Phone → SRV_VoIP → succès

RTO observé : < 5 minutes avec la procédure de rollback préparée
Sans sauvegarde : reconfiguration manuelle = 30-60 min minimum
```

## Partie 4 — Procédures

Éléments obligatoires dans Proc.1 :
- Fréquence quotidienne, heure hors heures de bureau (23h recommandé)
- Ping TFTP avant la sauvegarde (étape de vérification)
- Tous les équipements listés nominativement
- Convention de nommage présente

Éléments obligatoires dans Proc.2 :
- Étape 0 sauvegarde préalable EN PREMIER (avant toute modification)
- Fenêtre de maintenance cochée
- Tests de validation précis (pas juste "vérifier que ça marche")
- Rollback avec commandes exactes (`copy tftp: running-config`)

---

*TP Procédures d'exploitation + Correction — BAC PRO CIEL | E31 | 2ᵉ année S18*
*Compétences C2.6 · C3.1 · C3.2 · S5.2*
