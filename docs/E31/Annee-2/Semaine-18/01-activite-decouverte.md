# 🔍 ACTIVITÉ DE DÉCOUVERTE — S18 · 2ᵉ ANNÉE · E31
## « L'audit des procédures » — Repérer ce qui manque avant le cours

---

> **Durée** : 30 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement
> **Principe** : Avant tout cours sur les procédures d'exploitation, tu analyses 3 procédures réelles. Certaines sont bonnes, d'autres sont dangereuses. Tu dois identifier pourquoi.

---

## 🎯 Mise en situation

> L'entreprise DIGITEC vient de subir **deux incidents** la même semaine :
>
> **Incident 1** — Mardi 14h : un technicien a mis à jour le firmware du routeur principal
> du Siège sans prévenir. Le routeur a redémarré pendant 4 minutes.
> 40 salariés ont été coupés d'Internet. Le directeur a appelé.
>
> **Incident 2** — Jeudi 09h : un stagiaire a modifié la config d'un switch "pour tester".
> Le VLAN VoIP a disparu. Il a voulu revenir en arrière mais il n'avait pas de sauvegarde.
> Les téléphones IP sont restés muets pendant 2 heures.
>
> **Ta mission** : analyser les 3 procédures laissées par différents techniciens
> et identifier celles qui auraient empêché ces incidents.

---

## 📄 Procédure A — Rédigée par le technicien Marc

```
┌─────────────────────────────────────────────────────────────────────┐
│  PROCÉDURE : MISE À JOUR IOS SUR ROUTEUR CISCO                     │
│  Rédigée par : Marc D.  |  Version : 1.0                           │
├─────────────────────────────────────────────────────────────────────┤
│  1. Télécharger le fichier IOS depuis le site Cisco                │
│  2. Copier le fichier sur le routeur via TFTP                      │
│     copy tftp: flash:                                               │
│  3. Modifier le registre de démarrage                              │
│     boot system flash: [nom_du_fichier]                             │
│  4. Redémarrer le routeur                                          │
│     reload                                                          │
│  5. Vérifier la version après redémarrage                          │
│     show version                                                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📄 Procédure B — Rédigée par la technicienne Sophie

```
┌─────────────────────────────────────────────────────────────────────┐
│  PROCÉDURE : MODIFICATION DE CONFIGURATION SWITCH                  │
│  Rédigée par : Sophie L.  |  Version : 2.1  |  Date : 2024-01-10  │
├─────────────────────────────────────────────────────────────────────┤
│  CONDITIONS PRÉALABLES :                                           │
│    → Fenêtre de maintenance approuvée (samedi 22h-06h)             │
│    → Sauvegarde de la config actuelle effectuée AVANT              │
│    → Responsable réseau informé par email                          │
│    → Procédure de rollback préparée (étapes 6-8)                   │
│                                                                     │
│  ÉTAPES D'EXÉCUTION :                                              │
│  1. Sauvegarder la configuration courante :                        │
│     copy running-config tftp:                                       │
│     → Fichier : SW_CORE_A_running_2024-01-13_2200.cfg              │
│  2. Effectuer la modification                                      │
│  3. Tester : ping depuis PC_Siege_1 → PC_Agence_B                 │
│  4. Si tests OK : copy running-config startup-config               │
│  5. Documenter le changement dans le registre des modifications    │
│                                                                     │
│  ROLLBACK (si tests KO) :                                          │
│  6. copy tftp: running-config                                       │
│     → Restaurer SW_CORE_A_running_2024-01-13_2200.cfg              │
│  7. Vérifier la restauration (show running-config)                 │
│  8. Notifier l'équipe + ouvrir un ticket d'incident                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📄 Procédure C — Rédigée par le stagiaire Kevin

```
┌─────────────────────────────────────────────────────────────────────┐
│  PROCÉDURE : SAUVEGARDE CONFIG ROUTEUR                             │
│  Kevin K. — Stagiaire                                              │
├─────────────────────────────────────────────────────────────────────┤
│  Pour sauvegarder un routeur, taper :                              │
│  copy running-config startup-config                                 │
│                                                                     │
│  Ça sauvegarde la config.                                          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 PARTIE 1 — Évaluer chaque procédure (15 min)

**Question 1.1** — Pour chaque procédure, coche les éléments présents ou absents :

| Élément | Proc. A (Marc) | Proc. B (Sophie) | Proc. C (Kevin) |
|---|---|---|---|
| Auteur identifié | ☐ Oui ☐ Non | ☐ Oui ☐ Non | ☐ Oui ☐ Non |
| Date / version | ☐ Oui ☐ Non | ☐ Oui ☐ Non | ☐ Oui ☐ Non |
| Sauvegarde AVANT l'intervention | ☐ Oui ☐ Non | ☐ Oui ☐ Non | ☐ Oui ☐ Non |
| Fenêtre de maintenance | ☐ Oui ☐ Non | ☐ Oui ☐ Non | ☐ Oui ☐ Non |
| Tests de validation après | ☐ Oui ☐ Non | ☐ Oui ☐ Non | ☐ Oui ☐ Non |
| Procédure de rollback | ☐ Oui ☐ Non | ☐ Oui ☐ Non | ☐ Oui ☐ Non |
| Notification des équipes | ☐ Oui ☐ Non | ☐ Oui ☐ Non | ☐ Oui ☐ Non |

**Question 1.2** — Quelle procédure qualifies-tu de **professionnelle** ? Laquelle est **dangereuse** ?

```
Procédure professionnelle : _______ — Justification : _________________________
Procédure dangereuse : _______ — Car : ________________________________________
```

---

## 🔍 PARTIE 2 — Relier aux incidents de DIGITEC (10 min)

**Question 2.1** — **Incident 1** (redémarrage pendant les heures de bureau) :
Quelle erreur de la Procédure A a provoqué cet incident ?

```
Erreur identifiée : ____________________________________________________________
Élément manquant qui aurait évité l'incident : __________________________________
```

**Question 2.2** — **Incident 2** (VLAN VoIP disparu sans possibilité de rollback) :
La Procédure C est-elle suffisante pour permettre un rollback ? Pourquoi ?

```
La Procédure C sauvegarde-t-elle la config sur un serveur externe ? ☐ Oui ☐ Non
Que fait réellement `copy running-config startup-config` ?
→ Elle copie la config courante vers ___________________________________________
→ En cas de mauvaise modification, peut-on revenir en arrière avec ça ? ________
Ce qui manque dans la Procédure C : ___________________________________________
```

**Question 2.3** — La Procédure B aurait-elle évité les deux incidents ? Explique pour chacun.

```
Incident 1 (redémarrage intempestif) :
  Procédure B aurait évité ? ☐ Oui ☐ Non — car : ______________________________

Incident 2 (pas de rollback possible) :
  Procédure B aurait évité ? ☐ Oui ☐ Non — car : ______________________________
```

---

## 🔍 PARTIE 3 — Améliorer la Procédure A (5 min)

**Question 3.1** — Liste les **4 éléments manquants** dans la Procédure A de Marc :

```
Manque 1 : ____________________________________________________________________
Manque 2 : ____________________________________________________________________
Manque 3 : ____________________________________________________________________
Manque 4 : ____________________________________________________________________
```

**Question 3.2** — À quel moment précis de la Procédure A faut-il insérer la sauvegarde ? Ajoute l'étape 0 :

```
Étape 0 (À AJOUTER EN PREMIER) :
Action : _____________________________________________________________________
Commande IOS : _______________________________________________________________
Convention de nommage du fichier : ____________________________________________
```

---

## 🏁 Bilan

```
Les 5 règles d'or d'une procédure d'exploitation :
1. ___________________________________________________________________________
2. ___________________________________________________________________________
3. ___________________________________________________________________________
4. ___________________________________________________________________________
5. ___________________________________________________________________________

La différence entre `copy run start` et `copy run tftp:` :
  copy run start → sauvegarde ______________ (sur le même équipement)
  copy run tftp: → sauvegarde ______________ (sur un serveur externe)
  Laquelle permet un rollback en cas de sinistre physique ? ___________________
```

> ✅ Tu viens d'identifier tous les principes des procédures d'exploitation professionnelles.
> Le cours va maintenant te donner les commandes précises et le format standard.

---

## 📎 Pour l'enseignant — Réponses

**1.2** : Professionnelle = B · Dangereuse = C (ne sauvegarde que localement, pas externe)

**2.1** : Marc n'a pas de fenêtre de maintenance → a redémarré en pleine journée de travail

**2.2** : `copy run start` = sauvegarde locale sur le même équipement → si la config est mauvaise, la startup-config l'est aussi → pas de rollback possible. Il manque la sauvegarde vers un serveur TFTP externe.

**3.1** : Manque 1 : sauvegarde préalable vers TFTP · Manque 2 : fenêtre de maintenance · Manque 3 : procédure de rollback · Manque 4 : tests de validation après reload

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Administration Systèmes | 2ᵉ année S18*
*Compétences : C3.1 · C3.2 · C2.6*
