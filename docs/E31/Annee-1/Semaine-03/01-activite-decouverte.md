# 🎲 ACTIVITÉ - S3 E31
## "Enveloppes Gigognes" : Encapsulation OSI

---

## 🎯 OBJECTIFS

- ✅ Visualiser l'encapsulation (emboîtement)
- ✅ Comprendre rôle de chaque couche
- ✅ Expérimenter ajout d'en-têtes

---

## ⏱️ DURÉE : 40 min

---

## 🧩 MATÉRIEL

- 7 enveloppes tailles décroissantes
- Message original
- 7 fiches en-têtes (HTTP, TCP, IP, Ethernet...)
- 14 badges "Couches 1-7"

---

## 🎮 DÉROULEMENT

### **PHASE 1 : ENCAPSULATION (15 min)**

**7 groupes = 7 couches OSI**

**Processus :**

**C7 Application :**
- Message : "Salut Bob, RDV 14h?"
- Ajouter fiche "HTTP"
- Placer dans enveloppe A4

**C6 Présentation :**
- Recevoir enveloppe C7
- Ajouter fiche "SSL/TLS"
- Placer dans enveloppe A5

**C5 Session :**
- Recevoir C6
- Ajouter fiche "Session ID"
- Placer dans enveloppe moyenne

**C4 Transport :**
- Recevoir C5
- Ajouter fiche "TCP ports"
- Placer dans enveloppe bleue

**C3 Réseau :**
- Recevoir C4
- Ajouter fiche "IP source/dest"
- Placer dans enveloppe orange

**C2 Liaison :**
- Recevoir C3
- Ajouter fiche "MAC source/dest"
- Placer dans petite enveloppe

**C1 Physique :**
- Recevoir C2
- Montrer câble RJ45 (S2)
- Transmettre au récepteur

---

### **PHASE 2 : DÉSENCAPSULATION (10 min)**

**Processus inverse :**

C1 → C2 → C3 → C4 → C5 → C6 → C7

Chaque couche :
1. Ouvre enveloppe
2. Lit son en-tête
3. Retire en-tête
4. Passe enveloppe suivante

**Résultat C7 :** Message original intact !

---

### **PHASE 3 : DÉBRIEFING (15 min)**

**Lien jeu ↔ OSI :**

| **Jeu** | **OSI** |
|---------|---------|
| Enveloppes | En-têtes |
| Emboîtement | Encapsulation |
| Message original | Données utilisateur |
| Retrait enveloppes | Désencapsulation |
| Câble RJ45 | Couche 1 Physique (S2) |

**Schéma encapsulation :**

```
Message
   ↓ + HTTP
[HTTP][Message]
   ↓ + TCP
[TCP][HTTP][Message]
   ↓ + IP
[IP][TCP][HTTP][Message]
   ↓ + Ethernet
[Ethernet][IP][TCP][HTTP][Message]
   ↓ Bits
010101... (câble RJ45 S2)
```

---

## ✅ VALIDATION

- 100% participent
- 80% comprennent encapsulation
- 70% expliquent 3 couches
- 60% font lien S2 (câble)

---

**Document - Version 1.0 - Février 2026**
