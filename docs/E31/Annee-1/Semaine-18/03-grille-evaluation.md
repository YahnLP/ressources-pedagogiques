# GRILLE D'ÉVALUATION - PROJET FINAL U31
## Semaine 18 - Déploiement Infrastructure Réseau

---

**Binôme évalué :**

- Apprenti 1 : _________________________
- Apprenti 2 : _________________________

**Sujet :** _________________________________________________________________

**Date :** ___/___/______ **Formateur évaluateur :** _________________________

---

## 📊 BARÈME GLOBAL (100 points → /20)

| **Partie** | **Points obtenus** | **Points max** |
|------------|--------------------|----------------|
| **A - Compétences techniques** | ___/50 | 50 |
| **B - Documentation** | ___/20 | 20 |
| **C - Soutenance orale** | ___/20 | 20 |
| **D - Compétences transversales** | ___/10 | 10 |
| **TOTAL** | **___/100** | **100** |

**Note finale : ___/20**

**Appréciation globale :**

☐ Excellent (90-100 pts / 18-20)  
☐ Très bien (80-89 pts / 16-17.8)  
☐ Bien (70-79 pts / 14-15.8)  
☐ Satisfaisant (60-69 pts / 12-13.8)  
☐ Passable (50-59 pts / 10-11.8)  
☐ Insuffisant (<50 pts / <10)

---

## 🔧 PARTIE A : COMPÉTENCES TECHNIQUES (50 points)

### A1. Câblage structuré (5 points)

**Critères d'évaluation :**

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Nombre de câbles** | Minimum 6 câbles fabriqués | 1 pt | ___/1 |
| **Norme T568B** | Câbles respectent norme (ordre fils) | 1 pt | ___/1 |
| **Tests au testeur** | Tous câbles testés OK (8 LEDs vertes) | 2 pts | ___/2 |
| **Étiquetage** | Câbles étiquetés (VLAN, destination) | 1 pt | ___/1 |

**Commentaire :**
_________________________________________________________________________
_________________________________________________________________________

**Sous-total A1 : ___/5 points**

---

### A2. Configuration switch (10 points)

**Critères d'évaluation :**

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **VLANs créés** | 3 VLANs minimum avec noms descriptifs | 3 pts | ___/3 |
| **Ports affectés** | Ports en mode access, affectés aux bons VLANs | 3 pts | ___/3 |
| **Configuration sauvegardée** | `write memory` exécuté, résiste au reboot | 2 pts | ___/2 |
| **Commandes CLI** | Commandes correctes, syntaxe maîtrisée | 2 pts | ___/2 |

**Test de validation :**

```
Switch# show vlan brief
```

**Résultat :**

| **VLAN** | **Nom** | **Ports** | **Validé** |
|----------|---------|-----------|------------|
| VLAN 10 | __________ | __________ | ☐ OK ☐ KO |
| VLAN 20 | __________ | __________ | ☐ OK ☐ KO |
| VLAN 30 | __________ | __________ | ☐ OK ☐ KO |

**Commentaire :**
_________________________________________________________________________

**Sous-total A2 : ___/10 points**

---

### A3. Connectivité VLANs (8 points)

**Test 1 : Connectivité intra-VLAN** (4 points)

**Procédure :**

1. Connecter 2 PC au même VLAN (ex: VLAN 10)
2. Configurer IP statiques (ex: 192.168.10.10 et .20)
3. Ping entre les 2 PC

**Résultat :**

- ☐ **Ping réussit** (4/4 réponses) → **4 points**
- ☐ **Ping partiel** (1-3/4 réponses) → **2 points**
- ☐ **Ping échoue** (0/4 réponses) → **0 point**

**Points obtenus Test 1 : ___/4**

---

**Test 2 : Isolation inter-VLAN** (4 points)

**Procédure :**

1. Connecter 2 PC à des VLANs différents (ex: VLAN 10 et VLAN 20)
2. Configurer IP statiques (ex: 192.168.10.10 et 192.168.20.10)
3. Ping entre les 2 PC (sans routage inter-VLAN)

**Résultat attendu :** Ping doit **échouer** (isolation VLAN)

- ☐ **Ping échoue** (isolation OK) → **4 points** ✅
- ☐ **Ping réussit** (isolation KO) → **0 point** ❌

**Points obtenus Test 2 : ___/4**

**Commentaire :**
_________________________________________________________________________

**Sous-total A3 : ___/8 points**

---

### A4. Serveur DHCP (8 points)

**Critères d'évaluation :**

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Installation** | Serveur `isc-dhcp-server` installé | 1 pt | ___/1 |
| **Configuration pools** | 3 pools configurés (1 par VLAN) | 3 pts | ___/3 |
| **Service actif** | `systemctl status isc-dhcp-server` = active | 1 pt | ___/1 |
| **Test fonctionnel** | PC client obtient IP automatique | 3 pts | ___/3 |

**Test de validation :**

**PC client configuré en DHCP :**

```
C:\> ipconfig /all
```

**Résultat observé :**

| **Paramètre** | **Valeur** | **Conforme** |
|--------------|------------|--------------|
| IPv4 | _________________ | ☐ OK ☐ KO |
| Masque | _________________ | ☐ OK ☐ KO |
| Passerelle | _________________ | ☐ OK ☐ KO |
| Serveur DHCP | _________________ | ☐ OK ☐ KO |

**Commentaire :**
_________________________________________________________________________

**Sous-total A4 : ___/8 points**

---

### A5. Serveur Web (6 points)

**Critères d'évaluation :**

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Installation Apache** | `apache2` installé et actif | 1 pt | ___/1 |
| **Page HTML créée** | Contenu personnalisé, structure HTML5 | 2 pts | ___/2 |
| **Permissions** | Fichiers www-data, 644 | 1 pt | ___/1 |
| **Test accès** | Site accessible via navigateur | 2 pts | ___/2 |

**Test de validation :**

**URL testée :** http://_______________

**Résultat :**

- ☐ **Site s'affiche correctement** → 2 points
- ☐ **Site s'affiche avec erreurs** → 1 point
- ☐ **Erreur 404/403/500** → 0 point

**Capture d'écran du site :**

☐ Jointe au dossier

**Commentaire :**
_________________________________________________________________________

**Sous-total A5 : ___/6 points**

---

### A6. Routage inter-VLAN (optionnel - 5 points bonus)

**Critères d'évaluation :**

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Routeur configuré** | Routeur ou switch L3 avec IPs par VLAN | 2 pts | ___/2 |
| **Routage actif** | `ip forwarding` activé | 1 pt | ___/1 |
| **Test fonctionnel** | Ping inter-VLAN réussit | 2 pts | ___/2 |

**Note :** Cette partie est optionnelle. Les points bonus s'ajoutent au total.

**Sous-total A6 (bonus) : ___/5 points**

---

### A7. Diagnostic et dépannage (8 points)

**Panne introduite par le formateur :** ______________________________________

**Procédure de résolution :**

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Méthodologie** | Démarche structurée (tests, logs, etc.) | 2 pts | ___/2 |
| **Outils utilisés** | Ping, traceroute, logs consultés | 2 pts | ___/2 |
| **Temps de résolution** | Panne résolue en <10 minutes | 2 pts | ___/2 |
| **Explication** | Cause identifiée et expliquée | 2 pts | ___/2 |

**Chronométrage :**

- ☐ **<5 minutes** → 2 points
- ☐ **5-10 minutes** → 1 point
- ☐ **>10 minutes ou non résolu** → 0 point

**Commentaire :**
_________________________________________________________________________
_________________________________________________________________________

**Sous-total A7 : ___/8 points**

---

## **TOTAL PARTIE A : ___/50 points** (+ ___/5 bonus)

---

## 📄 PARTIE B : DOCUMENTATION TECHNIQUE (20 points)

### B1. Structure du dossier (4 points)

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Page de garde** | Titre, binôme, date présents | 1 pt | ___/1 |
| **Sommaire** | Numéroté, paginé | 1 pt | ___/1 |
| **Organisation** | Sections claires, logique | 1 pt | ___/1 |
| **Annexes** | Captures, configs regroupées | 1 pt | ___/1 |

**Commentaire :**
_________________________________________________________________________

**Sous-total B1 : ___/4 points**

---

### B2. Schémas réseau (6 points)

**Schéma physique (3 points) :**

| **Critère** | **Présent** | **Points** |
|-------------|------------|-----------|
| Topologie (bus/étoile/maillée) | ☐ Oui ☐ Non | 1 pt |
| Équipements (switch, routeur, serveur) | ☐ Oui ☐ Non | 1 pt |
| Connexions physiques (câbles) | ☐ Oui ☐ Non | 1 pt |

**Points obtenus schéma physique : ___/3**

---

**Schéma logique (3 points) :**

| **Critère** | **Présent** | **Points** |
|-------------|------------|-----------|
| VLANs représentés (avec noms) | ☐ Oui ☐ Non | 1 pt |
| Adressage IP (réseau, masque) | ☐ Oui ☐ Non | 1 pt |
| Services (DHCP, Web, DNS) | ☐ Oui ☐ Non | 1 pt |

**Points obtenus schéma logique : ___/3**

**Commentaire :**
_________________________________________________________________________

**Sous-total B2 : ___/6 points**

---

### B3. Plan d'adressage (4 points)

**Tableau présent dans le dossier :** ☐ Oui ☐ Non

**Contenu du tableau :**

| **Critère** | **Présent** | **Points** |
|-------------|------------|-----------|
| Réseaux (ex: 192.168.10.0/24) | ☐ Oui ☐ Non | 1 pt |
| Plages DHCP (ex: .100 - .150) | ☐ Oui ☐ Non | 1 pt |
| Passerelles (ex: .1) | ☐ Oui ☐ Non | 1 pt |
| DNS (ex: 8.8.8.8) | ☐ Oui ☐ Non | 1 pt |

**Commentaire :**
_________________________________________________________________________

**Sous-total B3 : ___/4 points**

---

### B4. Captures d'écran (3 points)

**Nombre de captures :** _____ (minimum 5 attendu)

| **Capture** | **Présente** | **Légendée** | **Points** |
|------------|--------------|--------------|------------|
| `show vlan brief` (switch) | ☐ Oui ☐ Non | ☐ Oui ☐ Non | 0.5 pt |
| `ipconfig /all` (PC DHCP) | ☐ Oui ☐ Non | ☐ Oui ☐ Non | 0.5 pt |
| Site web dans navigateur | ☐ Oui ☐ Non | ☐ Oui ☐ Non | 0.5 pt |
| Ping intra-VLAN | ☐ Oui ☐ Non | ☐ Oui ☐ Non | 0.5 pt |
| Logs Apache | ☐ Oui ☐ Non | ☐ Oui ☐ Non | 0.5 pt |
| Autres (préciser) | ☐ Oui ☐ Non | ☐ Oui ☐ Non | 0.5 pt |

**Total captures : ___/3 points**

**Commentaire :**
_________________________________________________________________________

**Sous-total B4 : ___/3 points**

---

### B5. Qualité rédaction (3 points)

| **Critère** | **Évaluation** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Orthographe/grammaire** | Peu de fautes (<5) | 1 pt | ___/1 |
| **Clarté** | Explications compréhensibles | 1 pt | ___/1 |
| **Présentation** | Mise en page soignée | 1 pt | ___/1 |

**Commentaire :**
_________________________________________________________________________

**Sous-total B5 : ___/3 points**

---

## **TOTAL PARTIE B : ___/20 points**

---

## 🎤 PARTIE C : SOUTENANCE ORALE (20 points)

### C1. Présentation générale (4 points)

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Introduction** | Présentation claire du contexte | 1 pt | ___/1 |
| **Structure** | Plan annoncé, transitions fluides | 1 pt | ___/1 |
| **Respect du temps** | 10 minutes respectées (±1 min) | 1 pt | ___/1 |
| **Conclusion** | Synthèse, bilan pertinent | 1 pt | ___/1 |

**Temps réel de présentation :** _____ minutes

**Commentaire :**
_________________________________________________________________________

**Sous-total C1 : ___/4 points**

---

### C2. Démonstration technique (6 points)

| **Test** | **Réussi** | **Points** | **Obtenu** |
|----------|-----------|-----------|-----------|
| **Ping intra-VLAN** | ☐ Oui ☐ Non | 1.5 pts | ___/1.5 |
| **Affichage IP DHCP** (ipconfig) | ☐ Oui ☐ Non | 1.5 pts | ___/1.5 |
| **Accès site web** (navigateur) | ☐ Oui ☐ Non | 1.5 pts | ___/1.5 |
| **Show vlan brief** (switch) | ☐ Oui ☐ Non | 1.5 pts | ___/1.5 |

**Commentaire :**
_________________________________________________________________________

**Sous-total C2 : ___/6 points**

---

### C3. Réponses aux questions (5 points)

**Questions posées par le formateur :**

**Question 1 :** _____________________________________________________________

**Réponse :** ☐ Correcte et argumentée ☐ Partiellement correcte ☐ Incorrecte

**Points : ___/1.5**

---

**Question 2 :** _____________________________________________________________

**Réponse :** ☐ Correcte et argumentée ☐ Partiellement correcte ☐ Incorrecte

**Points : ___/1.5**

---

**Question 3 :** _____________________________________________________________

**Réponse :** ☐ Correcte et argumentée ☐ Partiellement correcte ☐ Incorrecte

**Points : ___/2**

---

**Commentaire général :**
_________________________________________________________________________
_________________________________________________________________________

**Sous-total C3 : ___/5 points**

---

### C4. Communication orale (3 points)

| **Critère** | **Évaluation** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Expression** | Claire, audible, structurée | 1 pt | ___/1 |
| **Vocabulaire technique** | Termes appropriés (VLAN, DHCP, etc.) | 1 pt | ___/1 |
| **Posture** | Professionnelle, regard public | 1 pt | ___/1 |

**Commentaire :**
_________________________________________________________________________

**Sous-total C4 : ___/3 points**

---

### C5. Support visuel (2 points)

| **Critère** | **Présent** | **Points** | **Obtenu** |
|-------------|-----------|------------|------------|
| **Diaporama ou schémas** | ☐ Oui ☐ Non | 1 pt | ___/1 |
| **Lisibilité** | Police, couleurs adaptées | 1 pt | ___/1 |

**Note :** Le support visuel est optionnel mais valorisé.

**Sous-total C5 : ___/2 points**

---

## **TOTAL PARTIE C : ___/20 points**

---

## 🌟 PARTIE D : COMPÉTENCES TRANSVERSALES (10 points)

### D1. Travail en équipe (3 points)

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Répartition tâches** | Tâches clairement distribuées | 1 pt | ___/1 |
| **Collaboration** | Échanges, entraide visible | 1 pt | ___/1 |
| **Équilibre** | Les 2 apprentis ont contribué équitablement | 1 pt | ___/1 |

**Observation formateur :**
_________________________________________________________________________

**Sous-total D1 : ___/3 points**

---

### D2. Autonomie (3 points)

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Gestion temps** | Planning respecté, échéances tenues | 1 pt | ___/1 |
| **Résolution problèmes** | Cherche solutions avant de demander aide | 1 pt | ___/1 |
| **Initiative** | Propose améliorations, va au-delà du demandé | 1 pt | ___/1 |

**Observation formateur :**
_________________________________________________________________________

**Sous-total D2 : ___/3 points**

---

### D3. Rigueur (2 points)

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Vérifications** | Tests systématiques après chaque étape | 1 pt | ___/1 |
| **Sauvegardes** | Configs sauvegardées, docs régulières | 1 pt | ___/1 |

**Sous-total D3 : ___/2 points**

---

### D4. Esprit critique (2 points)

| **Critère** | **Indicateur** | **Points** | **Obtenu** |
|-------------|----------------|------------|------------|
| **Analyse choix** | Justifie les décisions techniques | 1 pt | ___/1 |
| **Recul** | Identifie points d'amélioration | 1 pt | ___/1 |

**Sous-total D4 : ___/2 points**

---

## **TOTAL PARTIE D : ___/10 points**

---

## 📊 SYNTHÈSE FINALE

### Récapitulatif des notes

| **Partie** | **Points obtenus** | **Points max** | **% Réussite** |
|------------|--------------------|----------------|----------------|
| A - Technique | ___/50 | 50 | ___% |
| B - Documentation | ___/20 | 20 | ___% |
| C - Soutenance | ___/20 | 20 | ___% |
| D - Transversal | ___/10 | 10 | ___% |
| **TOTAL** | **___/100** | **100** | **___%** |

### Conversion note sur 20

**Note finale : ___/100 × 0,2 = ___/20**

---

### Appréciation détaillée

**Points forts :**
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**Axes d'amélioration :**
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**Compétences validées :**

- ☐ C3.1 - Installer et configurer un réseau informatique local
- ☐ C3.2 - Maintenir et dépanner un réseau informatique
- ☐ C3.3 - Exploiter un réseau informatique
- ☐ C3.4 - Installer et configurer un service réseau
- ☐ C2.1 - Analyser et diagnostiquer
- ☐ C2.2 - Documenter
- ☐ C4.1 - Communiquer à l'oral

**Validation globale du projet :**

- ☐ **Validé** (≥ 50/100) - Compétences acquises
- ☐ **Non validé** (< 50/100) - Remédiation nécessaire

---

### Recommandations pour l'Année 2

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

**Signatures :**

**Formateur :** _________________________  **Date :** ___/___/______

**Apprenti 1 :** _________________________  **Date :** ___/___/______

**Apprenti 2 :** _________________________  **Date :** ___/___/______

---

**Ce document est à conserver dans le portfolio professionnel**

**Date de création :** 24/02/2026  
**Version :** 1.0  
**Auteur :** Équipe pédagogique CFA
