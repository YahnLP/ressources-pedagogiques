# 🔍 ANALYSE D'ERREURS + PARCOURS DE REMÉDIATION — S16-A3 E2
## Séance Finale : Cibler, Comprendre, Corriger

---

## ÉTAPE 1 — MON BILAN PERSONNEL (10 min, individuel)

### 🤔 À ton avis ?

À quelques semaines de l'épreuve, **où perds-tu le plus de points** ? Sais-tu vraiment ce que tu dois retravailler en priorité ?

??? question "Voir une réponse possible"
    Cette séance t'aide à **cibler** tes lacunes (bilan personnel), à **comprendre** tes erreurs (erreurs types) puis à les **corriger** par des ateliers. Mieux vaut **travailler 2 points précis** que tout reprendre au hasard.


> En vous aidant de vos copies corrigées (S9-A3 et S14-A3), identifiez vos lacunes.

### Mes résultats

| **Compétence** | **Score S9-A3** | **Score S14-A3** | **Tendance** |
|---|---|---|---|
| Métrologie / PV | /20 | /20 | ↑ / → / ↓ |
| KPI / Alarmes embarquées | /20 | /20 | |
| KiCad / Schéma | /16 | /20 | |
| Normes / DAT | /12 | /16 | |
| Synthèse intégrée | /12 | /24 | |

### Mes 3 lacunes prioritaires (à compléter après l'entretien formateur)

```
Lacune 1 : ___________________________________________________________
           Ce que j'ai fait de faux : __________________________________
           Ce que je dois faire à la place : ___________________________

Lacune 2 : ___________________________________________________________
           Ce que j'ai fait de faux : __________________________________
           Ce que je dois faire à la place : ___________________________

Lacune 3 : ___________________________________________________________
           Ce que j'ai fait de faux : __________________________________
           Ce que je dois faire à la place : ___________________________
```

> **→ Choisissez votre parcours de remédiation :**
> - Métrologie fragile → **Parcours 1**
> - KiCad fragile → **Parcours 2**
> - Synthèse/PV fragile → **Parcours 3**
> - Score global < 50% → Commencer par P1 puis aller en P3


> [!TIP] 💡 En clair : comment trouver ses lacunes
> Une lacune se repère à la **catégorie d'erreur**, pas au nombre de points perdus. Dans tes copies, **classe chaque erreur** : **oubli** (unité, tolérance, signature), **calcul** (formule, arrondi), **méthode** (mauvais ordre, mauvaise valeur utilisée), **connaissance** (notion non comprise). Les **oublis** se corrigent par des **réflexes** ; les **connaissances** par une **relecture** puis un exercice.

??? tip "💡 Aide : comment remplir ton bilan"
    - Si ton score est **inférieur à 50 %** dans une catégorie, c'est une **priorité**.
    - **Une tendance en baisse** entre les deux copies indique souvent un **oubli de méthode** plutôt qu'un manque de connaissance.
    - Choisis **trois lacunes seulement** : les corriger vaut mieux qu'en lister dix.

---

## ÉTAPE 2 — ANALYSE DES ERREURS TYPES (15 min, collectif)

> [!TIP] 💡 En clair
> Une **erreur type** revient chez plusieurs élèves : oubli d'unité, arrondi trop tôt, mauvaise conversion, schéma sans PWR_FLAG… Repérer **tes** erreurs types t'évite de les refaire le jour de l'épreuve.

> [!SUCCESS] 🧠 À retenir
> - Noter ses erreurs types = ne plus les refaire.


> Le formateur présente les 5 erreurs les plus fréquentes. Notez ci-dessous la règle correcte pour chaque erreur que vous avez commise.

### Erreur #1 — Calcul $u_{B,\mathrm{cl}}$

```
❌ Ce que j'ai fait : u_B,cl = (classe% × _______________) / (100√3)
✅ Ce qu'il faut faire : u_B,cl = (classe% × _______________) / (100√3)
Différence : _______________________________________________________
```

### Erreur #2 — Tracé alarme hystérésis

```
Règle : L'alarme se DÉSACTIVE seulement quand la valeur descend SOUS ___
        (= le seuil BAS, pas le seuil haut)
Exemple : SH=35, SB=33 → à 34°C, l'alarme est ☐ Active ☐ Inactive
```

### Erreur #3 — NE555 pin 4

$$Pin 4 = \underline{\hspace{2.5em}}$$

Doit être connectée à : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Si non connectée : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  

### Erreur #4 — Seuil IPC Classe 2

```
Décalage CMS : non conforme si > _____ %   (Classe 2)
Remplissage PTH : non conforme si < _____ %  (Classe 2)
```

### Erreur #5 — Conclusion PV

```
Les 3 formulations acceptées :
  1. La carte est _________________________________________________
  2. La carte est _________________________________________________
  3. La carte est _________________________________________________
```


??? tip "💡 Aides pour les cinq erreurs types (sans les réponses)"
    - **Erreur n° 1 (classe de l'instrument)** : dans ce cours, la classe s'applique à la **valeur mesurée** $\bar{x}$, **pas à la pleine échelle** de l'instrument. Vérifie quelle grandeur figure au numérateur de ta formule.
    - **Erreur n° 2 (hystérésis)** : repère **quel seuil** s'applique quand l'alarme est **active** et quand elle est **inactive**. Entre les deux seuils, l'état **ne change pas**.
    - **Erreur n° 3 (broche 4 du NE555)** : c'est l'entrée de **remise à zéro** (RESET) : elle est **active à l'état bas**. Elle doit donc être **forcée au niveau haut** pour que le circuit oscille.
    - **Erreur n° 4 (IPC)** : les seuils sont des **pourcentages** : un **décalage maximum** pour les CMS et un **remplissage minimum** pour les trous métallisés. Retrouve les valeurs de ton cours.
    - **Erreur n° 5 (conclusion du PV)** : la conclusion a **trois formes** possibles ; chacune doit reposer sur un **chiffre** (intervalle de mesure, tolérance).

---

# ═══════════════════════════════════════════
# PARCOURS 1 — MÉTROLOGIE INTENSIVE
# Durée : 90 min
# ═══════════════════════════════════════════

> *Si votre lacune principale est les incertitudes de mesure et la rédaction de PV*

## P1.1 — Refaire le calcul complet de A à Z (20 min)

> Cinq mesures de la tension de sortie d'un régulateur 3,3V avec un multimètre classe 0,5%, résolution 0,01V : **3,28 / 3,32 / 3,30 / 3,27 / 3,31 V**

**P1.1.1** — Calculez $\bar{x}$, $s$, $u_{A}$ :

$$\bar{x} = \_\_\_\_ \text{ V} \qquad s = \_\_\_\_ \text{ V} \qquad u_{A} = \frac{s}{\sqrt{5}} = \_\_\_\_ \text{ V}$$

**P1.1.2** — Calculez les deux composantes $u_{B}$ :

$$u_{B,rés} = \frac{0,01}{2\sqrt{3}} = \_\_\_\_ \text{ V}$$

$$u_{B,cl} = \frac{0,5 \times \bar{x}}{100\sqrt{3}} = \_\_\_\_ \text{ V}$$

*(Attention : utilisez $\bar{x}$, PAS la pleine échelle de l'instrument)*

**P1.1.3** — Calculez $u_{c}$ et $U$ :

$$u_{c} = \sqrt{u_A^2 + u_{B,rés}^2 + u_{B,cl}^2} = \_\_\_\_ \text{ V}$$

$$U = 2 \times u_{c} = \_\_\_\_ \text{ V} \rightarrow U_{arrondi} = \_\_\_\_ \text{ V}$$

$$\boxed{V = (\_\_\_\_ \pm \_\_\_\_) \text{ V} \quad [95\%]}$$

**P1.1.4** — Spécification 3,3V ±2% = [3,234 ; 3,366] V. Concluez :

```
Intervalle : [_____ ; _____] V  vs  [3,234 ; 3,366] V → _______________
```


> [!TIP] 💡 En clair : la méthode en sept lignes
> **1** Moyenne · **2** écart-type · **3** $u_A$ · **4** $u_{B,rés}$ · **5** $u_{B,cl}$ calculée avec la **moyenne** · **6** $u_c$ en racine carrée de la somme des carrés · **7** $U = 2u_c$, **arrondi par excès**, puis la valeur centrale **arrondie au même rang**.

??? tip "💡 Aide : ordres de grandeur pour vérifier ton calcul"
    - Pour cinq mesures d'un régulateur 3,3 V qui varient de **quelques centièmes de volt**, l'écart-type est de l'ordre de **0,01 à 0,03 V**.
    - $u_A$ est **plus petit** que l'écart-type (on divise par $\sqrt{5}$).
    - $u_{B,rés}$ est de l'ordre de **quelques millivolts** (au plus **0,003 V** pour une résolution de 0,01 V).
    - La **classe 0,5 %** donne, pour 3,3 V, une composante de l'ordre de **0,01 V**.
    - $U$ est de l'ordre de **0,02 à 0,05 V** : si tu trouves **plusieurs volts**, tu as oublié une division ou une racine.

---

## P1.2 — Les 3 cas limites (20 min)

> Ces 3 cas piégent régulièrement. Traitez-les.

**Cas 1 — Mesure unique (pas de répétition)**

> Une seule mesure : 4,97V (classe 0,5%, résolution 0,001V). Calculez U.

$u_{A}$ = 0  (pas de répétition → $u_{A}$ est nul)  
$u_{B,\mathrm{rés}}$ = \_\_\_\_\_  |  $u_{B,\mathrm{cl}}$ = \_\_\_\_\_  
$u_{c}$ = \_\_\_\_\_  |  U = \_\_\_\_\_  |  $U_{\mathrm{arrondi}}$ = \_\_\_\_\_  

$$V = (\underline{\hspace{2.5em}} \pm \underline{\hspace{2.5em}}) V [95\,\mathrm{\%}]$$

**Cas 2 — Quand U vaut plus que la tolérance**

> Mesure = 5,10V, U = 0,08V → intervalle [5,02 ; 5,18]. Spécification = 5V ±3% = [4,85 ; 5,15]. La borne haute 5,18 dépasse 5,15. Quelle conclusion ?

```
[5,02 ; 5,18] vs [4,85 ; 5,15]
5,18 > 5,15 → L'intervalle de mesure N'EST PAS entièrement dans la spécification
Conclusion : ☐ Conforme  ☐ Non conforme  ☐ Sous réserve
Justification : _________________________________________________
```

**Cas 3 — Arrondi de U**

> $u_{c}$ = 0,0143 V. Quel est $U_{arrondi}$ ?

$$U = 2 \times 0{,}0143 = 0{,}0286\,\mathrm{V}$$

1er chiffre significatif de U = \_\_\_  → règle : arrondir par excès à 1 chiffre sig  

$$U_{\mathrm{arrondi}} = \underline{\hspace{2.5em}} V$$

Valeur centrale arrondie au même rang : \_\_\_\_\_ V  


??? tip "💡 Aide : les trois cas limites"
    - **Mesure unique** : $u_A = 0$, mais les deux composantes de **type B** restent. Ne conclus pas « incertitude nulle ».
    - **$U$ plus grand que la marge** : si la plage « mesure ± U » **dépasse** la tolérance, même d'un seul côté, la conformité n'est **pas garantie** : choisis la conclusion **sous réserve** ou **non conforme** et **justifie** avec les chiffres.
    - **Arrondi** : on garde **un chiffre significatif** pour $U$ (par excès) puis on arrondit la valeur centrale **au même rang**. Exemple d'arrondi par excès : 0,0286 → **0,03**.

---

## P1.3 — Rédiger un PV partiel de qualité (25 min)

> Contexte : Vous venez de mesurer Vout = (4,99 ± 0,04) V [95%]. La spécification est 5V ±5% = [4,75 ; 5,25] V. L'inspection IPC-A-610 Cl.2 a révélé un pont de soudure sur C1.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROCÈS-VERBAL DE VALIDATION — EXERCICE P1
Réf. : PVF-REMEDIATION-\_\_\_  |  Date : 2026-\_\_\_-\_\_\_
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Produit : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Ref. : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Instrument : \_\_\_\_\_\_\_\_\_\_\_\_\_ Cl.\_\_\_% Rés.\_\_\_V N°:\_\_\_\_\_\_\_\_\_ Cert.:\_\_\_\_\_

RÉSULTATS :
| TC# | Exigence | Résultat ± U | Conf. |
|---|---|---|---|
| TC-01 | $V_{out} = 5\,\mathrm{V} \pm 5\,\mathrm{\%}$ |  |  |
| TC-02 | Assemblage IPC-A-610 Cl.2 | Pont soudure C1 |  |

CONCLUSION :
☐ CONFORME     ☐ NON CONFORME     ☐ CONFORME AVEC RÉSERVE

Justification : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Mesureur : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  Date : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**P1.3.1** — Pourquoi la conclusion est-elle NON CONFORME et pas CONFORME AVEC RÉSERVE ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


??? tip "💡 Aide : rédiger le PV"
    - Écris **d'abord** le tableau (exigence, résultat ± U, conformité), **puis** la décision.
    - La décision doit rester **cohérente** avec les lignes du tableau : **un seul non-conforme** suffit à **refuser** la carte.
    - Le **motif** compte **au moins deux lignes**, avec des **valeurs chiffrées**.
    - N'oublie pas **instrument** (classe, résolution, numéro, certificat) et **signature**.

---

## P1.4 — Entraînement vitesse (25 min)

> 4 mini-calculs rapides (3 min chacun, sans détail) :

Calc 1 : classe 1,0%, valeur = 12,3V, résolution = 0,1V  

$$u_{\mathrm{B,cl}} = \underline{\hspace{2.5em}} u_{\mathrm{B,rés}} = \underline{\hspace{2.5em}}$$

Calc 2 : 3 mesures : 22,3 / 22,7 / 22,5°C, classe 0,5%, rés. 0,1°C  

$$x̄ = \underline{\hspace{2.5em}} s = \underline{\hspace{2.5em}} u_{\mathrm{A}} = \underline{\hspace{2.5em}}$$

Calc 3 : $u_{c}$ = $\sqrt{0,0124² + 0,0058² + 0,0289²}$ = \_\_\_\_\_  

Calc 4 : U = 2 × 0,0314 = \_\_\_\_\_ → $U_{\mathrm{arrondi}}$ = \_\_\_\_\_  
si x̄ = 22,53°C : T = (\_\_\_\_\_ ± \_\_\_\_\_) °C [95%]  

---

# ═══════════════════════════════════════════
# PARCOURS 2 — KICAD ET ANALYSE DE SCHÉMA
# Durée : 90 min
# ═══════════════════════════════════════════

> *Si votre lacune principale est la conception de schéma, l'ERC, les empreintes ou la netlist*

## P2.1 — Les 8 règles absolues KiCad (15 min)

> Complétez et mémorisez ces 8 règles. Elles couvrent 90% des erreurs KiCad d'examen.

```
Règle 1 : PWR_FLAG : il en faut _____ (un sur _____ et un sur _____)
Règle 2 : ERC doit être à _____ erreur avant de passer au PCB
Règle 3 : NE555 pin 4 (RESET) doit être connectée à _____
Règle 4 : NE555 pin 5 (CTRL) doit avoir un condensateur _____ vers GND
Règle 5 : Condensateur électrolytique = symbole _____ (polarisé)
Règle 6 : 7805 condensateur d'ENTRÉE = _____ nF / condensateur SORTIE = _____ µF
Règle 7 : Empreinte NE555 traversant = _____________________
Règle 8 : Pour annoter : Tools → ___________________
```


> [!TIP] 💡 En clair : une règle, une raison
> Pour **mémoriser** les huit règles, associe chacune à la **conséquence** de son oubli : *« si j'oublie X, l'ERC me dit Y »*. C'est plus efficace que d'apprendre une liste.

---

## P2.2 — Corriger un schéma NE555 en 12 min (15 min)

> Voici le schéma décrit. Trouvez et corrigez toutes les erreurs (il y en a exactement 4).

```
Composants et câblage :
  J1 (2 broches) : pin1→+12V, pin2→GND
  U1 (7805) : Vin=+12V, GND=GND, Vout=+5V
  C1 (100nF CMS) : pin1→+12V, pin2→GND             ← Correct
  C2 (10µF élec.) : pin1→+5V, pin2→GND             ← Correct
  U2 (NE555) : pin8=+5V, pin1=GND, pin4=GND         ← Cherchez ici
  R1 (4k7) : pin1→+5V, pin2→pin7
  R2 (47k) : pin1→pin7, pin2→"noeud_t"
  C3 (10µF) : pin1→"noeud_t", pin2→GND              ← Cherchez ici
  C4 (100nF) : pin1→+5V, pin2→GND                   ← Cherchez ici
  R3 (150Ω) : pin1→pin3, pin2→Anode(LED1)
  LED1 : Anode→R3, Cathode→GND                      ← Correct
  (NE555 pin6 et pin2 non connectés entre eux)       ← Cherchez ici
  PWR_FLAG : 1 seul sur +5V
```

| **Erreur #** | **Composant/Pin** | **Problème** | **Correction** |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |


??? tip "💡 Aide : où chercher les quatre erreurs du schéma NE555"
    Parcours le schéma **broche par broche** (1 à 8) en te demandant : *à quoi est-elle reliée ? est-ce attendu ?* Les erreurs se trouvent généralement dans la **liste suivante** : une broche de **commande** (RESET, CONTROL) laissée **flottante**, une **alimentation** non repérée, un **condensateur de découplage** manquant, une **polarité** de composant inversée.

---

## P2.3 — Empreintes express (10 min)

> Sans notes, citez l'empreinte KiCad correcte :

| **Composant** | **Package** | **Empreinte KiCad** |
|---|---|---|
| NE555 | DIP-8 traversant | |
| 7805 | TO-220 vertical | |
| Résistance CMS | 0805 | |
| Condensateur élec. | Radial Ø5mm P2.5mm | |
| LED | THT 5mm | |
| Connecteur 2P | THT 2.54mm | |

---

## P2.4 — Analyse de netlist (20 min)

> Extrait de netlist d'un circuit NE555 astable :

```
(net (name "+5V")
  (node (ref U1) (pin 3))
  (node (ref U2) (pin 8))
  (node (ref R1) (pin 1))
  (node (ref U2) (pin 4))
)

(net (name "NOEUD_T")
  (node (ref R1) (pin 2))
  (node (ref R2) (pin 1))
  (node (ref U2) (pin 6))
  (node (ref U2) (pin 2))
  (node (ref C3) (pin 1))
)
```

**P2.4.1** — Combien de composants sont connectés à `+5V` ? Lesquels ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**P2.4.2** — Le net `NOEUD_T` regroupe pin6 et pin2 du NE555. En mode astable, pourquoi est-il correct de les connecter ensemble ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**P2.4.3** — U2 pin4 (RESET) est dans le net `+5V`. Est-ce correct ? Quelle erreur aurait l'ERC si ce nœud était absent ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


> [!TIP] 💡 En clair : lire une netlist
> Un **net** est un **ensemble de broches reliées** (par exemple tout ce qui est à +5 V). Pour compter ce qui est relié à un net, **compte les broches** listées dans ce net, puis regroupe par **composant**. Deux broches dans le **même net** sont **au même potentiel**.

---

## P2.5 — DRC et routage (30 min)

**P2.5.1** — Citez **3 erreurs DRC courantes** et leur correction :

| **Erreur DRC** | **Cause** | **Correction** |
|---|---|---|
| Clearance violation | | |
| Unconnected net | | |
| Board edge clearance | | |

**P2.5.2** — Vous devez router un PCB 80×60mm en simple face. Le net GND a 8 pastilles. Le DRC signale "4 ratsnest non routés sur GND". Proposez la solution la plus efficace (1 phrase) :

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**P2.5.3** — Quelles sont les 7 couches Gerber à exporter et leur rôle ?

| **Couche** | **Rôle** |
|---|---|
| F.Cu | |
| B.Cu | |
| F.Silkscreen | |
| F.Mask | |
| Edge.Cuts | |
| F.Paste | |
| PTH.drl | |


??? tip "💡 Aide : DRC, routage et Gerber"
    - **Erreurs DRC courantes** : **espacement insuffisant** (*clearance*), **piste trop étroite**, **pastille/piste non reliée**, **court-circuit** entre deux nets.
    - **Ratsnest non routés** : ce sont des **connexions oubliées** ; pour le GND en simple face, **réorganise le placement** ou ajoute un **strap** ; en double face, utilise un **via** ou un **plan de masse**.
    - **Couches Gerber** : pense à **cuivre**, **masque de soudure**, **sérigraphie**, **contour** (pour un simple face, le cuivre et le contour sont **indispensables**) + le fichier de **perçage**.

---

# ═══════════════════════════════════════════
# PARCOURS 3 — SYNTHÈSE ET PV PROFESSIONNEL
# Durée : 90 min
# ═══════════════════════════════════════════

> *Si votre lacune principale est la capacité à croiser les documents et produire une conclusion complète*

## P3.1 — Les normes : association rapide (15 min)

> Sans notes, reliez chaque norme à sa définition en 1 ligne et donnez un exemple concret :

```
IPC-A-610  →  Domaine : ___________________________
              Exemple  : ___________________________

IPC-2221   →  Domaine : ___________________________
              Exemple  : ___________________________

CEI 60068-2 → Domaine : ___________________________
              Exemple  : ___________________________

ISO 9001   →  Domaine : ___________________________
              Exemple  : ___________________________
```

**P3.1.1** — Quelle norme impose que "tout résultat de validation doit être documenté et traçable" ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## P3.2 — IPC-A-610 : 10 cas à classer en 15 min (20 min)

> Classifiez chaque cas selon IPC-A-610 Classe 2 : Conforme (C) / Acceptable (A) / Non conforme (NC)

| **#** | **Observation** | **Cl.2** |
|---|---|---|
| 1 | CMS 0805 décalé 18% de la largeur | |
| 2 | CMS 0805 décalé 30% | |
| 3 | Pont de soudure entre 2 pads | |
| 4 | Remplissage PTH = 80% | |
| 5 | Remplissage PTH = 70% | |
| 6 | Icicle (pointe soudure) sur TO-220 | |
| 7 | Résidu de flux colophane sur R1 | |
| 8 | Brasure brillante, angle < 90° | |
| 9 | Composant CMS décalé 60% (hors pastille) | |
| 10 | Condensateur électrolytique inversé | |


??? tip "💡 Aide : classer un cas IPC rapidement"
    1. Un **court-circuit**, une **polarité inversée** ou une **brasure absente** sont **toujours non conformes**.
    2. Compare ensuite les **pourcentages** aux seuils du cours (décalage CMS, remplissage PTH).
    3. Un **résidu non conducteur** ou un défaut **esthétique** est en général **acceptable**.
    4. En cas de doute, **nomme le critère** que tu utilises : c'est ce qui rapporte des points.

---

## P3.3 — DAT : sections clés à rédiger en 25 min (30 min)

> Rédigez les éléments suivants pour la carte NE555/7805 (Vin=12V, serre 0–60°C) :

**Section 7 complète (Contraintes de fonctionnement) :**

7.1 Alimentation :  
Vin nominale  = \_\_\_\_\_V DC  
Vin minimum   = \_\_\_\_\_V (sous ce seuil : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)  
Vin maximum absolu = \_\_\_\_\_V (au-delà : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_)  
Polarité inversée : ☐ Protégée   ☐ Non protégée  

7.2 Températures :  
Opérationnelle = \_\_\_\_\_°C à \_\_\_\_\_°C  
Stockage       = \_\_\_\_\_°C à \_\_\_\_\_°C  
Composant limitant : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ (Tmax = \_\_\_\_\_°C)  

7.3 IP carte nue : IP\_\_\_\_\_  
Recommandation boîtier : IP\_\_\_\_\_  

7.4 Tensions absolues max :  

$$NE555 V_{cc} max = \underline{\hspace{2.5em}}V$$

$$7805 V_{in} max = \underline{\hspace{2.5em}}V$$

$$LED I_{\mathrm{F}} max = \underline{\hspace{2.5em}} mA$$

**P3.3.1** — Pourquoi la section 7 est-elle juridiquement cruciale dans un DAT livré au client ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


??? tip "💡 Aide : rédiger les sections du DAT"
    - Chaque section répond à **une question** : *qu'est-ce que c'est ? comment c'est configuré ? comment l'installer ? que faire en panne ? quelles sont les limites ?*
    - Pour la **section des limites de responsabilité**, indique **ce qui est garanti** (plage de température, tension d'entrée) et **ce qui ne l'est pas**.
    - **Vin = 12 V, serre de 0 à 60 °C** : cite ces valeurs **chiffrées** dans tes réponses.

---

## P3.4 — Cas intégrateur croisé (25 min)

> Voici les résultats de 3 tests sur une carte :

```
TC-01 : Vout 7805 = (4,97 ± 0,04) V  |  Spéc. = 5V ±5% = [4,75;5,25]V
TC-02 : Fréquence  = (1,04 ± 0,02) Hz |  Spéc. = 1Hz ±10% = [0,90;1,10]Hz
TC-03 : Inspection IPC Cl.2 :
         • R1 CMS décalé 22%
         • C2 électrolytique : remplissage PTH 73%
         • LED1 : icicle 0,5mm sur cathode
```

**P3.4.1** — Complétez le tableau de résultats et la conclusion :

| **TC#** | **Exigence** | **Résultat ± U** | **Conforme ?** |
|---|---|---|---|
| TC-01 | [4,75 ; 5,25] V | (4,97 ± 0,04) V | |
| TC-02 | [0,90 ; 1,10] Hz | (1,04 ± 0,02) Hz | |
| TC-03 | IPC-A-610 Cl.2 | 3 observations | |

**P3.4.2** — Rédigez la conclusion globale du PV :

```
☐ CONFORME   ☐ NON CONFORME   ☐ CONFORME AVEC RÉSERVE

Conclusion : ___________________________________________________________
_______________________________________________________________________
Actions requises : _____________________________________________________
```

**P3.4.3** — Le client insiste pour recevoir la carte maintenant (urgence production). Que répondez-vous professionnellement ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_


??? tip "💡 Aide : le cas intégrateur"
    - Remplis d'abord le **tableau** (test, exigence, résultat, verdict) **sans interpréter**.
    - Ensuite, déduis la **décision globale** : **un test non conforme** suffit à **refuser** (ou à accepter **sous réserve** si le cahier des charges le permet et que tu le **justifies**).
    - Face à une **urgence client**, reste **factuel** : propose une **solution** (retouche et re-test) et **n'accepte pas** de modifier le verdict.

---

## ÉTAPE 3 — MINI-VALIDATION (20 min, individuel)

> 5 questions flash — notez votre réponse en 2 lignes max.

**V1** — Classe 0,5%, valeur mesurée = 5,023V, résolution = 0,001V. Calculez $u_{B,cl}$ :

$$u_{B,cl} = \frac{0,5 \times \_\_\_\_}{100 \times \sqrt{3}} = \_\_\_\_ \text{ V}$$

**V2** — SH=35, SB=33. Séquence moyennes : 34,2 → 35,4 → 34,8 → 32,9. Tracez l'état :

```
34,2 : ___  35,4 : ___  34,8 : ___  32,9 : ___
```

**V3** — Empreinte KiCad pour NE555 traversant DIP-8 :

\_\_\_\_\_\_\_\_\_

**V4** — CMS décalé 30% : classification IPC-A-610 Classe 2 ?

\_\_\_\_\_\_\_\_\_

**V5** — TC-01 conforme (Vout) + TC-02 non conforme (icicle IPC). Conclusion PV ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Remédiation Ultime – Version 1.0 – 2026**
