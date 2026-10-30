# 🔍 CHECK-LIST DIAGNOSTIC VISUEL PCB
## Fiche d'inspection — Maintenance N1 · Norme de référence IPC-A-610

---

> **Document élève — À utiliser à chaque intervention de maintenance**
> BAC Pro CIEL | S5 Module E2 | MFR de Pontonx

---

## 📌 Identification de l'intervention

| Champ | À remplir |
|---|---|
| **Technicien** | |
| **Date d'inspection** | |
| **Référence de la carte** | |
| **Provenance / Équipement d'origine** | |
| **Motif d'inspection** | ☐ Maintenance préventive planifiée ☐ Panne déclarée ☐ Contrôle qualité réception |
| **Conditions d'inspection** | ☐ Sous tension ☐ Hors tension (préciser si présence risque condensateurs chargés) |

---

## 🛡️ Vérification ESD avant intervention

*À effectuer AVANT tout contact avec la carte — ne jamais ignorer*

| Vérification | ☐ |
|---|---|
| Bracelet ESD mis au poignet | ☐ |
| Câble du bracelet raccordé au tapis | ☐ |
| Tapis raccordé à la prise de terre | ☐ |
| Carte posée sur le tapis (jamais sur bois, plastique, tissu) | ☐ |
| Composants sensibles rangés dans sachets antistatiques | ☐ |

---

## 🔬 Grille de diagnostic visuel — Les 9 critères

*Inspecter chaque critère avec la loupe ×5 sous éclairage rasant. Cocher le résultat.*

---

### Critère 1 — État général de propreté

| Observation | Résultat | Observations libres |
|---|---|---|
| Présence de poussière générale | ☐ OK ☐ NOK | |
| Corps étrangers visibles (métaux, débris) | ☐ Absent ☐ Présent | |
| Résidus de flux (traces jaunâtres, blanc laiteux) | ☐ Absent ☐ Présent | |
| Traces de condensation ou d'humidité | ☐ Absent ☐ Présent | |
| Taches de graisse ou d'huile | ☐ Absent ☐ Présent | |

**Conclusion critère 1 :** ☐ Conforme ☐ Nettoyage requis ☐ Anomalie grave

---

### Critère 2 — Position et intégrité des composants

| Observation | Résultat | Repères concernés |
|---|---|---|
| Composants droits et bien positionnés | ☐ OK ☐ NOK | |
| Aucun composant manquant (vs. BOM ou carte référence) | ☐ OK ☐ NOK | |
| Aucun composant fissuré ou fracturé | ☐ OK ☐ NOK | |
| Aucun composant déplacé ou mal fixé | ☐ OK ☐ NOK | |
| Composants CMS non décollés (si présents) | ☐ OK ☐ NOK | |

**Conclusion critère 2 :** ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave

---

### Critère 3 — Qualité des brasures (IPC-A-610)

| Observation | Résultat | Repères concernés |
|---|---|---|
| Brasures brillantes ou semi-brillantes (SAC305) | ☐ OK ☐ NOK | |
| Forme conique ou concave (pas de boule ronde) | ☐ OK ☐ NOK | |
| Aucun pont entre pads voisins | ☐ OK ☐ NOK | |
| Aucune brasure froide visible (aspect mat/granuleux) | ☐ OK ☐ NOK | |
| Aucun délaminage de pad | ☐ OK ☐ NOK | |

**Conclusion critère 3 :** ☐ Conforme ☐ Reprises nécessaires ☐ Défaut critique

---

### Critère 4 — État des condensateurs électrolytiques

| Observation | Résultat | Repères concernés |
|---|---|---|
| Sommet des condensateurs plat (pas de bombement) | ☐ OK ☐ NOK | |
| Corps cylindrique sans déformation | ☐ OK ☐ NOK | |
| Aucune fissure ou déchirure de l'enveloppe | ☐ OK ☐ NOK | |
| Aucune trace de fuite (liquide, dépôt blanchâtre à la base) | ☐ OK ☐ NOK | |

> ⚠️ **Condensateur bombé ou fissuré = NE PAS METTRE SOUS TENSION — risque d'explosion**

**Conclusion critère 4 :** ☐ Conforme ☐ Remplacement requis AVANT mise sous tension

---

### Critère 5 — État des pistes et du substrat PCB

| Observation | Résultat | Localisation |
|---|---|---|
| Pistes cuivre intactes (pas de coupure, pas de corrosion verte) | ☐ OK ☐ NOK | |
| Substrat FR4 intact (pas de cloquage, pas de brûlure) | ☐ OK ☐ NOK | |
| Vernissage de protection intact (couleur verte uniforme) | ☐ OK ☐ NOK | |
| Aucune piste grattée ou entaillée mécaniquement | ☐ OK ☐ NOK | |

**Conclusion critère 5 :** ☐ Conforme ☐ Anomalie mineure ☐ Dommage irréparable

---

### Critère 6 — État des connecteurs et interfaces

| Observation | Résultat | Référence connecteur |
|---|---|---|
| Contacts non oxydés (pas de vert-de-gris, pas de noircissement) | ☐ OK ☐ NOK | |
| Aucune broche tordue, pliée ou manquante | ☐ OK ☐ NOK | |
| Verrouillage / loquet en place (si applicable) | ☐ OK ☐ NOK | |
| Câbles associés non effilochés ni coupés | ☐ OK ☐ NOK | |

**Conclusion critère 6 :** ☐ Conforme ☐ Nettoyage contact requis ☐ Remplacement requis

---

### Critère 7 — Traces thermiques et traces de brûlures

| Observation | Résultat | Localisation |
|---|---|---|
| Aucun composant noirci ou carbonisé | ☐ OK ☐ NOK | |
| Aucune auréole brune sur le substrat (signe de surchauffe) | ☐ OK ☐ NOK | |
| Absence d'odeur de brûlé au moment de l'inspection | ☐ OK ☐ NOK | |
| Radiateurs / dissipateurs thermiques propres et bien fixés | ☐ OK ☐ NOK | |

**Conclusion critère 7 :** ☐ Conforme ☐ Dommage thermique passé (stable) ☐ Dommage actif — investigation requise

---

### Critère 8 — Intégrité des corps de composants

| Observation | Résultat | Repères concernés |
|---|---|---|
| Aucun boîtier plastique fissuré ou éclaté | ☐ OK ☐ NOK | |
| Résines de protection intactes (pas de décollement) | ☐ OK ☐ NOK | |
| Transformateurs : noyau ferrite intact, bobinage non dénudé | ☐ OK ☐ NOK | |
| Composants de puissance (transistors, régulateurs) : marquage lisible, boîtier intact | ☐ OK ☐ NOK | |

**Conclusion critère 8 :** ☐ Conforme ☐ Anomalie mineure ☐ Remplacement requis

---

### Critère 9 — Lisibilité des sérigraphies et repères

| Observation | Résultat |
|---|---|
| Références composants lisibles (R1, C2, U3...) | ☐ OK ☐ NOK |
| Repères de polarité visibles (+, −, triangle de sens) | ☐ OK ☐ NOK |
| Marquage tension / courant de la carte visible | ☐ OK ☐ NOK |
| Numéro de version ou de série lisible (si présent) | ☐ OK ☐ NOK |

**Conclusion critère 9 :** ☐ Conforme ☐ Usure normale ☐ Anomalie (signe de surchauffe ou d'usure sévère)

---

## 📊 Bilan du diagnostic visuel

| Critère | Résultat |
|---|---|
| 1 — Propreté | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 2 — Composants | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 3 — Brasures | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 4 — Condensateurs | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 5 — Pistes/Substrat | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 6 — Connecteurs | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 7 — Thermique | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 8 — Corps composants | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |
| 9 — Sérigraphies | ☐ Conforme ☐ Anomalie mineure ☐ Anomalie grave |

---

## 📋 Synthèse des anomalies trouvées

| N° | Anomalie | Critère | Gravité | Action recommandée | Niveau maintenance |
|---|---|---|---|---|---|
| 1 | | | ☐ Mineure ☐ Grave | | ☐ N1 ☐ N2 ☐ N3 |
| 2 | | | ☐ Mineure ☐ Grave | | ☐ N1 ☐ N2 ☐ N3 |
| 3 | | | ☐ Mineure ☐ Grave | | ☐ N1 ☐ N2 ☐ N3 |
| 4 | | | ☐ Mineure ☐ Grave | | ☐ N1 ☐ N2 ☐ N3 |

---

## 🏁 Conclusion de l'inspection

☐ **CARTE CONFORME** — Aucune anomalie. Peut être remise en service.

☐ **MAINTENANCE N1 REQUISE** — Anomalies mineures. Actions N1 à réaliser avant remise en service :
```
___________________________________________________________________
___________________________________________________________________
```

☐ **ESCALADE VERS N2 REQUISE** — Anomalies nécessitant remplacement de composants ou reprises de brasures.

☐ **CARTE HORS SERVICE — NE PAS METTRE SOUS TENSION** — Condensateur bombé / dommage thermique grave / délaminage.

---

## ✍️ Signatures

| Rôle | Nom | Signature | Date |
|---|---|---|---|
| **Technicien inspecteur** | | | |
| **Formateur validateur** | | | |

> 🏷️ **Indicateur Qualiopi** : Cette check-list constitue une **preuve de traçabilité de l'intervention de maintenance** (indicateur 6 et 7). Elle est conservée dans le dossier de suivi individuel et versée au portfolio E6.

---

*Check-list diagnostic visuel PCB — BAC Pro CIEL S5 Module E2 | MFR de Pontonx*
*Document inspiré de la norme IPC-A-610 et des procédures de maintenance industrielle de niveau 1*
