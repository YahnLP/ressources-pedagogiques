# 🔬 ATELIER – S7 ANNÉE 3 – E2
## Rédaction DAT Électronique + PV de Validation + Inspection IPC-A-610

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

Titre           : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Référence DAT   : DAT-ELEC-NE555-\_\_\_
Version         : 1.0
Date            : 2026-\_\_\_-\_\_\_
Statut          : ☐ Brouillon  ☐ Pour validation  ☐ Validé
Auteur(s)       : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Client          : ELECTROPRO SAS

Historique des révisions :
| Version | Date | Auteur | Description |
|---|---|---|---|
| 0.1 | 2026-__-__ |  | Création initiale |
| 1.0 | 2026-__-__ |  | Version complète |

**Q1.1 *(1 pt)*** — Quel est l'objet et le périmètre de ce DAT en 2 phrases ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

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

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

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

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **Q3.1** — Exemple de réponse (à adapter à ta propre carte) :  
    - $R_3 = \dfrac{V_{cc} - V_{led}}{I_f} = \dfrac{5 - 2}{0{,}020} = 150\,\Omega$ ; valeur normalisée choisie : **150 Ω** (série E12).  
    - NE555 astable : $f = \dfrac{1{,}44}{(R_a + 2R_b)\,C}$ et $DC = \dfrac{R_a + R_b}{R_a + 2R_b}$. Exemple cohérent avec les mesures de la partie B : $R_a = 4{,}7\,\mathrm{k\Omega}$, $R_b = 68\,\mathrm{k\Omega}$, $C_3 = 10\,\mathrm{\mu F}$ → $f = \dfrac{1{,}44}{140{,}7 \times 10^{3} \times 10 \times 10^{-6}} \approx 1{,}02\,\mathrm{Hz}$ et $DC = \dfrac{72{,}7}{140{,}7} \approx 51{,}7\,\%$.  
    **Q3.2** — La **datasheet du NE555** (Texas Instruments / ST), qui donne la formule de la fréquence en mode astable.

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

??? success "Réponses"
    Valeurs types à confirmer avec les datasheets utilisées :  
    - Alimentation : nominale **12 V DC** ; minimum environ **7 V** (le 7805 a besoin d'environ 2 V de marge : en dessous, la sortie n'est plus régulée à 5 V) ; maximum absolu **35 V** à l'entrée du 7805 (au-delà : destruction) ; polarité **non protégée** sans diode série.  
    - Limites des composants : NE555 $V_{CC}$ max environ **16 V** ; 7805 $V_{in}$ max absolu **35 V** ; LED $I_f$ max **25 mA** (spécification de ce TP).

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

**Q6.2 *(1 pt)*** — La norme appliquée pour l'assemblage est IPC-A-610 Classe \_\_\_. Justifiez ce choix.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **Q6.1** — Fichiers générés par KiCad :
    
    | Fichier | Couche / Type | Rôle |
    |---|---|---|
    | .gbr (F.Cu) | Cuivre face avant | Pistes côté composants |
    | .gbr (B.Cu) | Cuivre face arrière | Pistes côté soudures |
    | .gbr (F.Mask) | Masque de soudure avant | Zones laissées libres pour souder |
    | .gbr (B.Mask) | Masque de soudure arrière | Zones laissées libres pour souder |
    | .gbr (F.SilkS) | Sérigraphie avant | Repères et contours des composants |
    | .gbr (B.SilkS) | Sérigraphie arrière | Textes côté arrière |
    | .gbr (Edge.Cuts) | Contour | Découpe de la carte |
    | .drl | Perçage | Position et diamètre des trous |
    
    **Q6.2** — Classe **2** : produits électroniques professionnels, pour lesquels un fonctionnement continu est attendu mais où une panne n'est pas dangereuse pour les personnes (classe 3 = haute fiabilité : médical, aéronautique).

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

**B1.1 *(2 pts)*** — Calculez la moyenne et $u_{A}$ :

$$\bar{V}_{out} = \frac{4,987 + 4,984 + 4,990 + 4,988 + 4,985}{5} = \frac{\_\_\_\_}{5} = \_\_\_\_ \text{ V}$$

| $V_{i}$ | $V_{i} - \bar{V}$ | $(V_{i} - \bar{V})^2$ |
|---|---|---|
| 4,987 | | |
| 4,984 | | |
| 4,990 | | |
| 4,988 | | |
| 4,985 | | |
| Somme | — | |

$$s = \sqrt{\frac{\sum(V_{i}-\bar{V})^2}{4}} = \_\_\_\_ \text{ V} \qquad u_{A} = \frac{s}{\sqrt{5}} = \_\_\_\_ \text{ V}$$

**B1.2 *(1 pt)*** — Calculez $u_{B}$ (résolution et classe Fluke 87V) :

$$u_{B,rés} = \frac{0,001}{2\sqrt{3}} = \_\_\_\_ \text{ V}$$

$$u_{B,cl} = \frac{0,5 \times \bar{V}}{100\sqrt{3}} = \_\_\_\_ \text{ V}$$

**B1.3 *(1 pt)*** — Incertitude combinée et élargie :

$$u_{c} = \sqrt{u_A^2 + u_{B,rés}^2 + u_{B,cl}^2} = \_\_\_\_ \text{ V}$$

$$U = 2 \times u_{c} = \_\_\_\_ \text{ V} \rightarrow U_{arrondi} = \_\_\_\_ \text{ V}$$

$$\boxed{V_{out} = (\_\_\_\_ \pm \_\_\_\_) \text{ V [95\%]}}$$

**B1.4 *(1 pt)*** — Spécification : 5V ±3% → [4,85 V ; 5,15 V]. La mesure est-elle conforme ?

```
Intervalle mesuré : [_____ - U ; _____ + U] = [_____ ; _____] V
Intervalle spec.  : [4,850 ; 5,150] V
Conforme ? ☐ Oui  ☐ Non  → Conclusion : _______________
```

??? success "Réponses"
    **B1.1** — $\sum V_i = 24{,}934$ ; $\bar{V}_{out} = \dfrac{24{,}934}{5} = 4{,}9868\,\mathrm{V}$.
    
    | $V_i$ | $V_i - \bar{V}$ | $(V_i - \bar{V})^2$ |
    |---|---|---|
    | 4,987 | +0,0002 | $0{,}04 \times 10^{-6}$ |
    | 4,984 | −0,0028 | $7{,}84 \times 10^{-6}$ |
    | 4,990 | +0,0032 | $10{,}24 \times 10^{-6}$ |
    | 4,988 | +0,0012 | $1{,}44 \times 10^{-6}$ |
    | 4,985 | −0,0018 | $3{,}24 \times 10^{-6}$ |
    | Somme | — | $22{,}8 \times 10^{-6}$ |
    
    $s = \sqrt{\dfrac{22{,}8 \times 10^{-6}}{4}} \approx 0{,}00239\,\mathrm{V}$ ; $u_A = \dfrac{0{,}00239}{\sqrt{5}} \approx 0{,}00107\,\mathrm{V}$.  
    **B1.2** — $u_{B,rés} = \dfrac{0{,}001}{2\sqrt{3}} \approx 0{,}00029\,\mathrm{V}$ ; $u_{B,cl} = \dfrac{0{,}5 \times 4{,}9868}{100\sqrt{3}} \approx 0{,}01440\,\mathrm{V}$.  
    **B1.3** — $u_c = \sqrt{0{,}00107^2 + 0{,}00029^2 + 0{,}0144^2} \approx 0{,}01444\,\mathrm{V}$ ; $U = 2 \times 0{,}01444 = 0{,}0289\,\mathrm{V}$, arrondi par excès à **0,029 V** (2 chiffres car elle commence par 2). $V_{out} = (4{,}987 \pm 0{,}029)\,\mathrm{V}$ [95 %].  
    **B1.4** — Intervalle mesuré : $[4{,}987 - 0{,}029\,;\,4{,}987 + 0{,}029] = [4{,}958\,;\,5{,}016]\,\mathrm{V}$, entièrement dans $[4{,}850\,;\,5{,}150]$ : **conforme**.

---

### TC-02 — Fréquence NE555 (à compléter par l'apprenti)

**B2 *(3 pts)*** — Calculez la moyenne, $u_{A}$, $u_{B}$, $u_{c}$, U et concluez sur la conformité à 1 Hz ±10% [0,9 ; 1,1] Hz :

```
(Calculs à développer)

Résultat : f = (_____ ± _____) Hz [95%]
Conforme à [0,9 ; 1,1] Hz ? ☐ Oui  ☐ Non
```

??? success "Réponses"
    $\bar{f} = 1{,}018\,\mathrm{Hz}$ ; $s \approx 0{,}0084\,\mathrm{Hz}$ ; $u_A = \dfrac{0{,}0084}{\sqrt{5}} \approx 0{,}0037\,\mathrm{Hz}$ ; $u_{B,rés} = \dfrac{0{,}01}{2\sqrt{3}} \approx 0{,}0029\,\mathrm{Hz}$ ; $u_{B,cl} = \dfrac{0{,}1 \times 1{,}018}{100\sqrt{3}} \approx 0{,}0006\,\mathrm{Hz}$.  
    $u_c = \sqrt{0{,}0037^2 + 0{,}0029^2 + 0{,}0006^2} \approx 0{,}0048\,\mathrm{Hz}$ ; $U = 2 u_c \approx 0{,}0095\,\mathrm{Hz}$, arrondi par excès à **0,01 Hz**.  
    Résultat : $f = (1{,}02 \pm 0{,}01)\,\mathrm{Hz}$ [95 %] ; intervalle $[1{,}01\,;\,1{,}03]$ dans $[0{,}9\,;\,1{,}1]$ : **conforme**.

---

### TC-03 — Courant LED (mesure unique)

**B3 *(2 pts)*** — Sans répétition, calculez $u_{B}$ uniquement. Spécification : If ≤ 25 mA.

Valeur  : 19,3 mA  |  Résolution : 0,1 mA  |  Classe Fluke : 0,5%  
$u_{B,\mathrm{rés}}$ = \_\_\_\_\_  |  $u_{B,\mathrm{cl}}$ = \_\_\_\_\_  |  $u_{c}$ = \_\_\_\_\_  |  U = \_\_\_\_\_  

$$I_{\mathrm{LED}} = (\underline{\hspace{2.5em}} \pm \underline{\hspace{2.5em}}) mA [95\,\mathrm{\%}]$$

Conforme (≤ 25 mA) ? ☐ Oui  ☐ Non  

??? success "Réponses"
    $u_{B,rés} = \dfrac{0{,}1}{2\sqrt{3}} \approx 0{,}029\,\mathrm{mA}$ ; $u_{B,cl} = \dfrac{0{,}5 \times 19{,}3}{100\sqrt{3}} \approx 0{,}056\,\mathrm{mA}$ ; $u_c = \sqrt{0{,}029^2 + 0{,}056^2} \approx 0{,}063\,\mathrm{mA}$ ; $U = 2 u_c \approx 0{,}1255$, arrondi par excès à **0,13 mA**.  
    $I_{LED} = (19{,}30 \pm 0{,}13)\,\mathrm{mA}$ [95 %] ; valeur maximale $19{,}43\,\mathrm{mA} \leq 25\,\mathrm{mA}$ : **conforme**.

---

### Tableau de synthèse PV

**B4 *(2 pts)*** — Remplissez le tableau de synthèse du PV :

| **TC#** | **Exigence** | **Résultat ± U** | **Conforme ?** |
|---|---|---|---|
| TC-01 | $V_{out} = 5\,\mathrm{V} \pm 3\,\mathrm{\%} = [4{,}85;5{,}15]V$ | | |
| TC-02 | $f = 1\,\mathrm{\mathrm{Hz}} \pm 10\,\mathrm{\%} = [0{,}9;1{,}1]\mathrm{Hz}$ | | |
| TC-03 | If ≤ 25 mA | | |
| TC-04 | DC ≈ 50% (observation) | À calculer | |

**B5 *(1 pt)*** — Rédigez la conclusion de conformité globale en 2 phrases :

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    | TC# | Exigence | Résultat ± U | Conforme ? |
    |---|---|---|---|
    | TC-01 | $V_{out} = 5\,\mathrm{V} \pm 3\,\%$ | $(4{,}987 \pm 0{,}029)\,\mathrm{V}$ | Oui |
    | TC-02 | $f = 1\,\mathrm{Hz} \pm 10\,\%$ | $(1{,}02 \pm 0{,}01)\,\mathrm{Hz}$ | Oui |
    | TC-03 | $I_f \leq 25\,\mathrm{mA}$ | $(19{,}30 \pm 0{,}13)\,\mathrm{mA}$ | Oui |
    | TC-04 | $DC \approx 50\,\%$ (observation) | $(51{,}8 \pm 0{,}17)\,\%$ | Observation : proche de 50 % |
    
    TC-04 : moyenne 51,8 % ; $s \approx 0{,}158$ ; $u_A \approx 0{,}071$ ; $u_{B,rés} \approx 0{,}029$ ; $u_{B,cl} \approx 0{,}030$ ; $u_c \approx 0{,}082$ ; $U \approx 0{,}164$ arrondi à 0,17 %. Un NE555 en astable donne toujours un rapport cyclique **supérieur à 50 %** : $DC = \dfrac{R_a + R_b}{R_a + 2R_b}$.  
    **B5** — Les trois exigences chiffrées (tension, fréquence, courant) sont respectées, même en tenant compte de l'incertitude élargie. La carte est déclarée **conforme** ; le rapport cyclique de 51,8 % est cohérent avec le montage.

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

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    | N° | Classe 2 | Justification |
    |---|---|---|
    | B1 | Conforme | Brasure brillante, angle de mouillage inférieur ou égal à 90° |
    | B2 | **Non conforme** | Pont de soudure = court-circuit entre deux pads |
    | B3 | Conforme | Remplissage supérieur ou égal à 75 % |
    | B4 | Non conforme par précaution, à retoucher | Une pointe de soudure peut réduire l'isolement entre broches ; critère exact à confirmer avec la norme utilisée en classe |
    | B5 | Conforme | Décalage latéral de 40 % : inférieur ou égal à 50 % de la largeur |
    
    **C1** — Norme appliquée : IPC-A-610 Classe 2. Défauts non conformes : B2 (pont de soudure) et B4 (pointe de soudure). Action : retoucher ces deux brasures puis refaire l'inspection.

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
