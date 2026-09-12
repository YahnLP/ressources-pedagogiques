# 📝 EXERCICES - S3 E31
## Modèle OSI - Pratique

**Nom : ________________  Prénom : ________________**

---

## EXERCICE 1 : Ordre des couches (4 pts)

**Complète les 7 couches (de bas en haut) :**

| **Numéro** | **Nom couche** | **(0,5 pt)** |
|-----------|---------------|-------------|
| C1 | ________________ | |
| C2 | ________________ | |
| C3 | ________________ | |
| C4 | ________________ | |
| C5 | ________________ | |
| C6 | ________________ | |
| C7 | ________________ | |

**Aide :** Pierre Le Rat...

---

## EXERCICE 2 : Protocoles (6 pts)

**À quelle couche appartient chaque protocole ?**

| **Protocole** | **Couche (1-7)** | **(1 pt)** |
|--------------|----------------|----------|
| **HTTP** | C____ | |
| **TCP** | C____ | |
| **IP** | C____ | |
| **Ethernet** | C____ | |
| **UDP** | C____ | |
| **FTP** | C____ | |

---

## EXERCICE 3 : Équipements (4 pts)

**Associe équipement à sa couche :**

| **Équipement** | **Couche** | **(1 pt)** |
|---------------|-----------|----------|
| Câble RJ45 | C____ | |
| Switch | C____ | |
| Routeur | C____ | |
| Hub | C____ | |

---

## EXERCICE 4 : TCP vs UDP (3 pts)

**Coche les bonnes cases :**

| **Caractéristique** | **TCP** | **UDP** |
|--------------------|---------|---------|
| Fiable (accusés réception) | ☐ | ☐ |
| Rapide | ☐ | ☐ |
| Utilisé pour le web (HTTP) | ☐ | ☐ |
| Utilisé pour streaming vidéo | ☐ | ☐ |
| Avec connexion | ☐ | ☐ |
| Sans connexion | ☐ | ☐ |

**Barème :** 0,5 pt par case correcte

---

## EXERCICE 5 : Encapsulation (3 pts)

**Schématise l'encapsulation d'un message :**

```
Message : "Bonjour"

C7 ajoute HTTP :
[_______][Message]

C4 ajoute TCP :
[_______][HTTP][Message]

C3 ajoute IP :
[_______][TCP][HTTP][Message]

C2 ajoute Ethernet :
[_______][IP][TCP][HTTP][Message]
```

**Complète les en-têtes ajoutés.**

**Barème :** 0,75 pt par en-tête

---

## 📊 BARÈME

| **Exercice** | **Points** | **Note** |
|-------------|-----------|----------|
| Ordre couches | /4 | |
| Protocoles | /6 | |
| Équipements | /4 | |
| TCP vs UDP | /3 | |
| Encapsulation | /3 | |
| **TOTAL** | **/20** | |

---

**Document - Version 1.0 - Février 2026**
