# 🔧 FICHE DE CONFIGURATION MODULE HC-05
## Document de référence technique — à remplir lors du TP

---

> **Nom de l'apprenant** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
> **Binôme** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
> **Date** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
> **N° de matériel** : Module HC-05 n° \_\_\_\_\_  / Arduino n° \_\_\_\_\_

---

## 📋 Section 1 — Identification du module

| Champ | Valeur relevée |
|---|---|
| Version firmware (`AT+VERSION?`) | |
| Adresse MAC (`AT+ADDR?`) | |
| Rôle initial (`AT+ROLE?`) | ☐ Master (1) &nbsp; ☐ Slave (0) |
| Baudrate initial (`AT+UART?`) | |
| Nom initial (`AT+NAME?`) | |
| PIN initial (`AT+PSWD?`) | |

---

## ⚙️ Section 2 — Paramètres configurés

| Paramètre | Valeur choisie | Commande AT utilisée | Résultat obtenu |
|---|---|---|---|
| Nouveau nom | | `AT+NAME=` | ☐ OK &nbsp; ☐ Erreur |
| Nouveau PIN | | `AT+PSWD=` | ☐ OK &nbsp; ☐ Erreur |
| Baudrate défini | | `AT+UART=` | ☐ OK &nbsp; ☐ Erreur |
| Rôle défini | | `AT+ROLE=` | ☐ OK &nbsp; ☐ Erreur |

---

## 🔌 Section 3 — Câblage réalisé

| Broche Arduino | Connexion | Broche HC-05 | Couleur du fil |
|---|---|---|---|
| | | VCC | |
| | | GND | |
| | Pont diviseur ☐ Oui ☐ Non | RXD | |
| | Direct | TXD | |

**Valeurs du pont diviseur utilisé :**  
R1 = \_\_\_\_\_\_\_\_\_\_ Ω  |  R2 = \_\_\_\_\_\_\_\_\_\_ Ω  |  Tension calculée = \_\_\_\_\_\_\_\_\_\_ V

**Schéma de câblage** *(croquis ou capture Fritzing à coller ici)* :

```
[ Zone de schéma — coller votre capture d'écran ou dessiner ici ]
```

---

## 📡 Section 4 — Tests de communication effectués

| N° | Test réalisé | Résultat attendu | Résultat obtenu | ☐ OK / ☐ KO |
|---|---|---|---|---|
| 1 | Commande `AT` en mode AT | `OK` | | |
| 2 | Lecture du nom `AT+NAME?` | Nom configuré | | |
| 3 | Modification du nom | `OK` | | |
| 4 | Lecture du PIN | PIN configuré | | |
| 5 | Appairage smartphone | Connexion établie | | |
| 6 | Envoi `1` depuis smartphone | LED allumée + message reçu | | |
| 7 | Envoi `0` depuis smartphone | LED éteinte + message reçu | | |
| 8 | Envoi texte depuis moniteur PC | Message reçu sur smartphone | | |

---

## 📏 Section 5 — Test de portée

| Distance testée | Communication maintenue ? | Observations |
|---|---|---|
| 1 m | ☐ Oui ☐ Non | |
| 3 m | ☐ Oui ☐ Non | |
| 5 m | ☐ Oui ☐ Non | |
| 10 m | ☐ Oui ☐ Non | |
| > 10 m | ☐ Oui ☐ Non | |

**Portée maximale mesurée** : \_\_\_\_\_\_\_\_\_\_ m

---

## 🧠 Section 6 — Analyse et conclusions

**1. Pourquoi faut-il un pont diviseur de tension sur la broche RXD ?**

```
Réponse :
```

**2. Quelle est la différence entre le mode AT et le mode communication ?**

```
Réponse :
```

**3. Que signifie le clignotement rapide de la LED du HC-05 ?**

```
Réponse :
```

**4. Cite un problème rencontré et comment tu l'as résolu :**

```
Problème :
Solution :
```

---

## ✅ Validation enseignant

| Critère | Note /5 | Commentaire |
|---|---|---|
| Câblage correct et fonctionnel | | |
| Commandes AT maîtrisées | | |
| Appairage réussi | | |
| Communication bidirectionnelle testée | | |
| Fiche complète et lisible | | |
| **TOTAL** | **/25** | |

**Signature enseignant** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Date** : \_\_\_\_\_\_\_\_\_\_\_

---

*Fiche de Configuration HC-05 — BAC PRO CIEL | Module E2 | S14*  
*Document à conserver dans le Portfolio de l'apprenant (Épreuve E5)*
