# 🗂️ AIDE-MÉMOIRE DOCUMENTATION E31 — À PLASTIFIER
## DAT · Schémas · Procédures · Portfolio · BAC PRO CIEL · E31 · 3ᵉ année S18

---

> *Référence pour produire un dossier E31 professionnel*

---

## 📄 Structure du DAT (8 sections)

```
1. Page de garde (titre, réf, version, date, auteur)
2. Contexte et objectifs
3. Architecture (schéma logique + physique)
4. Plan d'adressage (TABLEAU obligatoire)
5. Configurations commentées
6. Tableau de tests
7. Procédures d'exploitation (≥ 2)
8. PRA (≥ 2 scénarios + RTO chiffrés)
[Annexes + Glossaire + Changelog]
```

---

## 🖼️ Schéma logique — éléments obligatoires

```
✓ Équipements nommés (R_LYON, SW_CORE...)
✓ VLANs avec couleurs distinctes (n° + nom)
✓ Areas OSPF délimitées en pointillés
✓ Adresses IP sur chaque interface
✓ EtherChannel représenté (double lien)
✓ Légende des symboles et couleurs
```

---

## 📐 Plan d'adressage — format tableau

```
| Équipement | Interface | IP | CIDR | Rôle |
|------------|-----------|-----|------|------|
| R_LYON     | Gi0/0.100 | ... | /25  | GW VLAN 100 |
                    ↑
         JAMAIS en texte libre
```

---

## ⚙️ Configuration commentée — exemple

```cisco
! Loopback = Router-ID stable (ne change pas si interface tombe)
interface Loopback0
 ip address 10.20.255.1 255.255.255.255

! OSPF : wildcard = inverse du masque
! /25 → masque 255.255.255.128 → wildcard 0.0.0.127
network 10.20.1.0 0.0.0.127 area 0
```

---

## 📋 Procédure — format obligatoire

```
1. TITRE + Référence + Version + Date + Auteur
2. OBJECTIF (2-3 lignes)
3. PRÉREQUIS (qui peut l'exécuter, outils, fenêtre maint.)
4. ÉTAPES NUMÉROTÉES (1 action = 1 étape = 1 commande)
5. VALIDATION (tests + résultats attendus)
6. ROLLBACK (que faire si ça échoue)
```

---

## 🔴 PRA — 2 scénarios minimum

```
Pour chaque scénario :
  Symptômes observables
  Détection (commandes de diagnostic)
  Actions avec délais
  RTO chiffré (ex: "RTO = 30 minutes")
  Validation du retour à la normale
```

---

## 🚫 5 erreurs qui font descendre la note

```
1. Plan adressage en texte → tableau !
2. Config sans commentaires → expliquer chaque ligne clé
3. "J'ai utilisé OSPF car c'est bien" → justification précise
4. Tests avec résultats supposés → copier la vraie sortie PT
5. PRA sans RTO chiffré → "30 min" pas "rapidement"
```

---

## 🗂️ Checklist portfolio E31

```
☐ DAT en PDF (≥ 8 pages)
☐ Schéma logique (PNG/PDF)
☐ Fichier PT complet (.pkt)
☐ 3 procédures au format pro
☐ Preuves : show ospf neighbor + ping E2E
☐ Grille compétences signée
```

---

*Aide-Mémoire Documentation E31 — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S18*
*Compétences C3.1 · C3.2 · C2.3*
