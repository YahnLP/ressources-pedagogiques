# 🔬 ATELIER – S7 ANNÉE 3 – E2
## Rédaction DAT Électronique + PV de Validation + Inspection IPC-A-610

**Nom : ________________  Prénom : ________________  Date : ________________**

---

## 🎯 OBJECTIFS

- ✅ Rédiger le DAT électronique complet de la carte NE555/7805 (S6-A3)
- ✅ Rédiger le PV de validation fonctionnelle avec mesures réelles
- ✅ Réaliser l'inspection IPC-A-610 Classe 2 sur photos de brasures
- ✅ Constituer le dossier de livraison complet

---

## ⏱️ SÉQUENÇAGE : 3 parties × 45 min + 15 min peer review

---

# PARTIE A — DAT ÉLECTRONIQUE (45 min)

> Rédigez le DAT électronique de la carte conçue en S6-A3 (NE555/7805). Utilisez la structure en 10 sections du cours.

---

### SECTION 1 — IDENTIFICATION ET GESTION

Titre           : _____________________________________________
Référence DAT   : DAT-ELEC-NE555-___
Version         : 1.0
Date            : 2026-___-___
Statut          : ☐ Brouillon  ☐ Pour validation  ☐ Validé
Auteur(s)       : _____________________________________________
Client          : ELECTROPRO SAS

Historique des révisions :
| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-__-__ |  | Création initiale |
| 1.0 | 2026-__-__ |  | Version complète |


**Q1.1 *(1 pt)*** — Quel est l'objet et le périmètre de ce DAT en 2 phrases ?

_________________________________________________________________________
_________________________________________________________________________

---

### SECTION 2 — DESCRIPTION FONCTIONNELLE

**Schéma bloc fonctionnel (à dessiner ci-dessous) :**

```
Dessinez les 3 blocs principaux et leurs liaisons :
  - Alimentation (entrée 12V → sortie 5V)
  - Oscillateur (NE555)
  - Indicateur (LED clignotante)

[Zone de dessin 10 × 6 cm]


```

**Q2.1 *(1 pt)*** — Décrivez la fonction générale de la carte en 1 phrase :

_________________________________________________________________________

**Q2.2 *(1 pt)*** — Listez les signaux et connecteurs d'interface :

| **Connecteur/Signal** | **Direction** | **Description** |
|---|---|---|
| J1 pin 1 | Entrée | |
| J1 pin 2 | — | |
| LED1 | Sortie optique | |

---

### SECTION 3 — SCHÉMA ÉLECTRONIQUE ET CALCULS

**Q3.1 *(2 pts)*** — Résumez les calculs de dimensionnement en complétant :

```
CALCUL RÉSISTANCE LED :
  Exigence  : If = 20 mA, Vled = 2V, Vcc = 5V
  Formule   : R3 = (Vcc - Vled) / If = _____
  Valeur choisie : _____ Ω

CALCUL OSCILLATEUR NE555 :
  Exigence : f = 1 Hz ±10%
  Ra = _____ Ω  |  Rb = _____ Ω  |  C3 = _____ µF
  Fréquence calculée : f = _____ Hz
  Rapport cyclique   : DC = _____ %
```

**Q3.2 *(1 pt)*** — Quel document de référence cite-t-on dans la section 3 pour justifier les calculs du NE555 ?

_________________________________________________________________________

---

### SECTION 5 — BOM (issue de S6-A3)

> Copiez votre BOM complète de l'exercice S6-A3 ici, ou référencez le fichier :

```
Référence fichier BOM : BOM_NE555_7805_[VotreNom].csv
Nombre de lignes      : _____ (composants distincts)
Coût total estimé     : _____ € HT
```

---

### SECTION 7 — CONTRAINTES DE FONCTIONNEMENT

**Remplissez le tableau pour la carte NE555/7805 :**

```
7.1 ALIMENTATION
    Tension nominale     : _____ V DC
    Tension minimum      : _____ V (sous ce seuil : _________________)
    Tension maximum abs. : _____ V (au-delà : ________________________)
    Polarité             : ☐ Protégée  ☐ Non protégée

7.2 TEMPÉRATURES
    Opérationnelle       : ___°C à ___°C
    Stockage             : ___°C à ___°C
    Composant le plus limitant : _______________ (Tmax = ___°C)

7.3 INDICE DE PROTECTION
    Carte nue            : IP___
    Recommandation boîtier: IP___

7.4 TENSIONS ABSOLUES MAXIMALES
    NE555 VCC max        : _____ V
    7805 Vin max absolu  : _____ V
    LED If max           : _____ mA
```

---

### SECTION 6 — FICHIERS DE FABRICATION

**Q6.1 *(2 pts)*** — Listez les 8 fichiers de fabrication générés par KiCad et leur rôle :

| **Fichier** | **Couche/Type** | **Rôle** |
|---|---|---|
| .gbr (F.Cu) | Face avant cuivre | Pistes côté composants |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |
| .drl | Drill | |

**Q6.2 *(1 pt)*** — La norme appliquée pour l'assemblage est IPC-A-610 Classe ___. Justifiez ce choix.

_________________________________________________________________________

---

# PARTIE B — PV DE VALIDATION FONCTIONNELLE (45 min)

> Des mesures ont été réalisées sur la carte assemblée. Utilisez ces données pour rédiger le PV complet.

### Données de mesures brutes (fournies)

| **TC#** | **Paramètre mesuré** | **Instrument** | **Valeurs brutes (5 mesures)** |
|---|---|---|---|
| TC-01 | Vout 7805 (V) | Fluke 87V, Cl.0,5%, Rés. 0,001V | 4,987 / 4,984 / 4,990 / 4,988 / 4,985 |
| TC-02 | Fréquence NE555 (Hz) | Rigol DS1054Z, Cl.0,1%, Rés. 0,01Hz | 1,02 / 1,01 / 1,03 / 1,02 / 1,01 |
| TC-03 | Courant LED (mA) | Fluke 87V, Cl.0,5%, Rés. 0,1mA | Mesure unique : 19,3 mA |
| TC-04 | Rapport cyclique (%) | Rigol DS1054Z, Cl.0,1%, Rés. 0,1% | 51,8 / 52,0 / 51,7 / 51,9 / 51,6 |

### TC-01 — Vout 7805 : calcul d'incertitude complet

**B1.1 *(2 pts)*** — Calculez la moyenne et u_A :

$$\bar{V}_{out} = \frac{4,987 + 4,984 + 4,990 + 4,988 + 4,985}{5} = \frac{\_\_\_\_}{5} = \_\_\_\_ \text{ V}$$

| $V_i$ | $V_i - \bar{V}$ | $(V_i - \bar{V})^2$ |
|---|---|---|
| 4,987 | | |
| 4,984 | | |
| 4,990 | | |
| 4,988 | | |
| 4,985 | | |
| Somme | — | |

$$s = \sqrt{\frac{\sum(V_i-\bar{V})^2}{4}} = \_\_\_\_ \text{ V} \qquad u_A = \frac{s}{\sqrt{5}} = \_\_\_\_ \text{ V}$$

**B1.2 *(1 pt)*** — Calculez u_B (résolution et classe Fluke 87V) :

$$u_{B,rés} = \frac{0,001}{2\sqrt{3}} = \_\_\_\_ \text{ V}$$

$$u_{B,cl} = \frac{0,5 \times \bar{V}}{100\sqrt{3}} = \_\_\_\_ \text{ V}$$

**B1.3 *(1 pt)*** — Incertitude combinée et élargie :

$$u_c = \sqrt{u_A^2 + u_{B,rés}^2 + u_{B,cl}^2} = \_\_\_\_ \text{ V}$$

$$U = 2 \times u_c = \_\_\_\_ \text{ V} \rightarrow U_{arrondi} = \_\_\_\_ \text{ V}$$

$$\boxed{V_{out} = (\_\_\_\_ \pm \_\_\_\_) \text{ V [95\%]}}$$

**B1.4 *(1 pt)*** — Spécification : 5V ±3% → [4,85 V ; 5,15 V]. La mesure est-elle conforme ?

```
Intervalle mesuré : [_____ - U ; _____ + U] = [_____ ; _____] V
Intervalle spec.  : [4,850 ; 5,150] V
Conforme ? ☐ Oui  ☐ Non  → Conclusion : _______________
```

---

### TC-02 — Fréquence NE555 (à compléter par l'apprenti)

**B2 *(3 pts)*** — Calculez la moyenne, u_A, u_B, u_c, U et concluez sur la conformité à 1 Hz ±10% [0,9 ; 1,1] Hz :

```
(Calculs à développer)


Résultat : f = (_____ ± _____) Hz [95%]
Conforme à [0,9 ; 1,1] Hz ? ☐ Oui  ☐ Non
```

---

### TC-03 — Courant LED (mesure unique)

**B3 *(2 pts)*** — Sans répétition, calculez u_B uniquement. Spécification : If ≤ 25 mA.

Valeur  : 19,3 mA  |  Résolution : 0,1 mA  |  Classe Fluke : 0,5%  
u_B,rés = _____  |  u_B,cl = _____  |  u_c = _____  |  U = _____  

$$I_{\mathrm{LED}} = (\underline{\hspace{2.5em}} \pm \underline{\hspace{2.5em}}) mA [95\,\mathrm{\%}]$$

Conforme (≤ 25 mA) ? ☐ Oui  ☐ Non  

---

### Tableau de synthèse PV

**B4 *(2 pts)*** — Remplissez le tableau de synthèse du PV :

| **TC#** | **Exigence** | **Résultat ± U** | **Conforme ?** |
|---|---|---|---|
| TC-01 | Vout = 5V ±3% = [4,85;5,15]V | | |
| TC-02 | f = 1Hz ±10% = [0,9;1,1]Hz | | |
| TC-03 | If ≤ 25 mA | | |
| TC-04 | DC ≈ 50% (observation) | À calculer | |

**B5 *(1 pt)*** — Rédigez la conclusion de conformité globale en 2 phrases :

_________________________________________________________________________
_________________________________________________________________________

---

# PARTIE C — INSPECTION IPC-A-610 (30 min)

> Inspection de 5 brasures de la carte. Pour chaque photo décrite, appliquez IPC-A-610 Classe 2.

### Observations

| **N°** | **Description de la brasure** | **Classe 2** | **Justification** |
|---|---|---|---|
| B1 | CMS 0805 : brasure brillante, angle de contact 75°, bonne extension | | |
| B2 | CMS 0805 : pont de soudure entre deux pads R1 et R2 adjacents | | |
| B3 | LED THT : remplissage du trou 81%, pas de pointe de soudure | | |
| B4 | TO-220 : pointe de soudure (icicle) de 0,8mm sur pin 3 | | |
| B5 | CMS résistance : composant décalé de 40% de la largeur, brasure OK | | |

**C1 *(2 pts)*** — Rédigez le rapport d'inspection IPC-A-610 en 3 lignes :

```
Norme appliquée : IPC-A-610 Classe 2
Défauts non conformes : _____________________________________________
Conclusion : ☐ Carte CONFORME  ☐ Carte NON CONFORME — action : ______
```

**C2 *(1 pt)*** — Quelle est la différence entre "conforme (target)" et "acceptable" dans la terminologie IPC ?

_________________________________________________________________________

---

## 📊 BARÈME DE L'ATELIER

| **Partie** | **Points** |
|---|---|
| A — DAT : Q1.1 à Q6.2 | /12 |
| B1 — Incertitude TC-01 complète | /5 |
| B2 — TC-02 calcul autonome | /3 |
| B3 — TC-03 mesure unique | /2 |
| B4 — Tableau synthèse + B5 conclusion | /3 |
| C — Inspection IPC + C1 rapport + C2 | /5 |
| **TOTAL** | **/30** |

> *Ramené à /20 : score × 0,67*

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Version 1.0 – 2026**
