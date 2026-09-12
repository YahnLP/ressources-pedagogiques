# 📝 EXERCICES - S11 E31
## Active Directory - Pratique

**Nom : ________________  Prénom : ________________**

---

## EXERCICE 1 : Workgroup vs Domaine (6 pts)

**Complète le tableau :**

| **Critère** | **Workgroup** | **Domaine AD** | **(1 pt)** |
|------------|--------------|---------------|----------|
| Gestion users | _____________ | Centralisée | |
| Nb PC max conseillé | < 10 | _____________ | |
| Création user Bob | Sur chaque PC | _____________ | |
| Sécurité | Faible | _____________ | |
| Protocole auth | NTLM | _____________ | |
| Usage typique | Maison | _____________ | |

---

## EXERCICE 2 : Concepts AD (5 pts)

**Associe définition au terme :**

| **Définition** | **Terme** | **(1 pt)** |
|---------------|----------|----------|
| Serveur qui héberge AD | __________ | |
| Conteneur logique (service) | __________ | |
| Format identifiant (user@...) | __________ | |
| Protocole authentification | __________ | |
| Extension domaine test | __________ | |

**Termes :** DC, OU, UPN, Kerberos, .local

---

## EXERCICE 3 : Installation AD (4 pts)

**Ordonne les étapes (1-4) :**

☐ Promouvoir serveur en contrôleur domaine  
☐ Configurer IP fixe + DNS  
☐ Ajouter rôle AD DS  
☐ Redémarrer serveur  

---

## EXERCICE 4 : Cas Pratique PME (5 pts)

**Entreprise ABC (50 PC) veut passer en domaine AD.**

**Services :**
- Direction (5 PC)
- Comptabilité (10 PC)
- Production (30 PC)
- Logistique (5 PC)

**Questions :**

**Q1** (1 pt) : Quel nom domaine recommandé ?
_______________________________________________

**Q2** (2 pts) : Créer structure OUs (dessine arbre) :

```
globaltech.local
   ├─ ?
   ├─ ?
   ├─ ?
   └─ ?
```

**Q3** (1 pt) : Où créer user "alice.durand" (Compta) ?
_______________________________________________

**Q4** (1 pt) : Avantage AD vs workgroup pour ABC ?
_______________________________________________

---

## 📊 BARÈME

| **Exercice** | **Points** | **Note** |
|-------------|-----------|----------|
| Workgroup/Domaine | /6 | |
| Concepts AD | /5 | |
| Installation | /4 | |
| Cas pratique | /5 | |
| **TOTAL** | **/20** | |

---

**Document - Version 1.0 - Février 2026**
