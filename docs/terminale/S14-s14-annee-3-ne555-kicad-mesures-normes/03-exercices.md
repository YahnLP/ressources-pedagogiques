# 📝 CAHIER D'EXERCICES — CONSOLIDATION FINALE E2
## S14 Année 3 — NE555, KiCad, Mesures, Normes, Synthèse

> **Mode d'emploi :** Traitez les blocs dans l'ordre indiqué par votre formateur. Dossier ressources E2 autorisé. Calculatrice autorisée. Montrez tous vos calculs — un résultat sans calcul ne donne aucun point.

---

# ═══════════════════════════════════════════
# BLOC A — MÉTROLOGIE ET INCERTITUDES (20 pts)
# ═══════════════════════════════════════════

## A1 — Calcul d'incertitude complet (12 pts)

> Un technicien mesure la résistance d'une résistance 4,7 kΩ avec un multimètre UNI-T UT61E (classe 1,0%, résolution 10 Ω, N°série UT-2026-447). Il réalise 5 mesures :

| **m** | 4 680 Ω | 4 710 Ω | 4 695 Ω | 4 725 Ω | 4 690 Ω |

**A1.1 *(1 pt)*** — Calculez la moyenne $\bar{x}$ :

$$\bar{x} = \frac{\_\_\_\_+\_\_\_\_+\_\_\_\_+\_\_\_\_+\_\_\_\_}{5} = \frac{\_\_\_\_\_}{5} = \_\_\_\_ \text{ Ω}$$

**A1.2 *(3 pts)*** — Calculez l'écart-type $s$ et l'incertitude type A $u_{A}$ :

| $x_{i}$ | $x_{i} - \bar{x}$ | $(x_{i} - \bar{x})^2$ |
|---|---|---|
| 4 680 | | |
| 4 710 | | |
| 4 695 | | |
| 4 725 | | |
| 4 690 | | |
| **Σ** | | |

$$s = \sqrt{\frac{\sum(x_{i}-\bar{x})^2}{n-1}} = \text{\_\_\_\_ Ω} \qquad u_{A} = \frac{s}{\sqrt{5}} = \text{\_\_\_\_ Ω}$$

**A1.3 *(3 pts)*** — Calculez les incertitudes type B :

$$u_{B,rés} = \frac{10}{2\sqrt{3}} = \text{\_\_\_\_ Ω}$$

$$u_{B,cl} = \frac{1,0 \times \bar{x}}{100\sqrt{3}} = \frac{1,0 \times \text{\_\_\_\_}}{173,2} = \text{\_\_\_\_ Ω}$$

**A1.4 *(3 pts)*** — Incertitude combinée et élargie :

$$u_{c} = \sqrt{u_A^2 + u_{B,rés}^2 + u_{B,cl}^2} = \text{\_\_\_\_ Ω}$$

$$U = 2 \times u_{c} = \text{\_\_\_\_ Ω} \quad \rightarrow \quad U_{arrondi} = \text{\_\_\_\_ Ω}$$

$$\boxed{R = (\text{\_\_\_\_ ± \_\_\_\_}) \text{ Ω} \quad [95\%]}$$

**A1.5 *(2 pts)*** — La spécification est 4,7 kΩ ±5% → [4 465 Ω ; 4 935 Ω].

```
Intervalle mesuré : [_____ ; _____] Ω
Conclusion : ☐ Conforme   ☐ Non conforme   ☐ Sous réserve
```

??? success "Réponses"
    **A1.1** — $\bar{x} = \dfrac{4680 + 4710 + 4695 + 4725 + 4690}{5} = \dfrac{23\,500}{5} = 4\,700\,\Omega$.  
    **A1.2** —
    
    | $x_i$ | $x_i - \bar{x}$ | $(x_i - \bar{x})^2$ |
    |---|---|---|
    | 4 680 | −20 | 400 |
    | 4 710 | +10 | 100 |
    | 4 695 | −5 | 25 |
    | 4 725 | +25 | 625 |
    | 4 690 | −10 | 100 |
    | **Σ** | 0 | 1 250 |
    
    $s = \sqrt{\dfrac{1250}{4}} \approx 17{,}7\,\Omega$ ; $u_A = \dfrac{17{,}7}{\sqrt{5}} \approx 7{,}9\,\Omega$.  
    **A1.3** — $u_{B,rés} = \dfrac{10}{2\sqrt{3}} \approx 2{,}9\,\Omega$ ; $u_{B,cl} = \dfrac{1{,}0 \times 4700}{173{,}2} \approx 27{,}1\,\Omega$.  
    **A1.4** — $u_c = \sqrt{7{,}9^2 + 2{,}9^2 + 27{,}1^2} \approx 28{,}4\,\Omega$ ; $U = 2 \times 28{,}4 \approx 56{,}8\,\Omega$, arrondi par excès à **60 Ω** (1 chiffre significatif). $R = (4\,700 \pm 60)\,\Omega$ [95 %].  
    **A1.5** — Intervalle mesuré : $[4\,640\,;\,4\,760]\,\Omega$, entièrement dans $[4\,465\,;\,4\,935]$ : **conforme**.

---

## A2 — Questions courtes métrologie (8 pts)

**A2.1 *(2 pts)*** — `[PIÈGE CLASSIQUE]` Un technicien calcule $u_{B,cl}$ avec la pleine échelle de son multimètre (10 kΩ) au lieu de la valeur mesurée (4 700 Ω). Quelle erreur cela produit-il sur l'incertitude finale ? Est-elle sur- ou sous-estimée ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**A2.2 *(2 pts)*** — Un PV de mesure indique : `R = 4 700 Ω — conforme`. Citez **3 éléments manquants** qui le rendent non professionnel :

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  3. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**A2.3 *(2 pts)*** — Expliquez pourquoi le certificat d'étalonnage d'un instrument a une date de validité (durée limitée). Que se passe-t-il si on utilise un instrument dont le certificat est périmé depuis 3 mois ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**A2.4 *(2 pts)*** — La chaîne de traçabilité métrologique doit être "ininterrompue". Que signifie ce terme et quelle est son importance dans un contexte industriel/légal ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **A2.1** — La classe porte sur la **valeur lue**, pas sur la pleine échelle : avec 10 kΩ on obtient $u_{B,cl} \approx 57{,}7\,\Omega$ au lieu de $27{,}1\,\Omega$, soit une incertitude **surestimée d'un facteur 2 environ**, donc un résultat trop pessimiste.  
    **A2.2** — Éléments manquants : l'**incertitude** (± U avec le niveau de confiance), l'**instrument** utilisé avec son numéro de série et son étalonnage, la **tolérance / critère** de conformité, la **date**, l'**opérateur**, les **conditions** de mesure.  
    **A2.3** — Un instrument **dérive** avec le temps et les chocs : le certificat n'est valable que pour une durée limitée. Utiliser un instrument hors validité rend les mesures **non garanties**, donc **sans valeur** dans un PV (non-conformité qualité, litige possible).  
    **A2.4** — « Ininterrompue » : chaque instrument est comparé à un étalon plus précis, **sans maillon manquant**, jusqu'à l'étalon national. Si un maillon est rompu, la mesure n'est plus **opposable** (audit, contrat, litige).

---

# ═══════════════════════════════════════════
# BLOC B — KPI, ALARMES, CODE ESP32 (20 pts)
# ═══════════════════════════════════════════

## B1 — Analyse de code : buffer circulaire et hystérésis (10 pts)

```cpp
// Extrait de firmware ESP32 — serre hydroponique
const int    N        = 5;
float        buf[N]   = {0};
int          idx      = 0;
bool         plein    = false;

const float  SH       = 38.0;   // Seuil alarme CRITIQUE
const float  SB       = 36.0;   // Seuil désactivation
const int    HYST_MS  = 15000;  // Anti-rebond 15 secondes

typedef enum { OK, CRITIQUE } Etat;
static Etat  etat     = OK;

static unsigned long t_debut   = 0;
static bool          debord    = false;

float moyenneMobile(float v) {
  buf[idx] = v;
  idx = (idx + 1) % N;
  if (idx == 0) plein = true;
  if (!plein) return v;
  float s = 0;
  for (int i = 0; i < N; i++) s += buf[i];
  return s / N;
}

void gererAlarme(float moy) {
  if (etat == OK) {
    if (moy >= SH) {
      if (!debord) { t_debut = millis(); debord = true; }
      else if (millis() - t_debut >= HYST_MS) { etat = CRITIQUE; debord = false; }
    } else { debord = false; }
  } else {
    if (moy <= SB) { etat = OK; }
  }
}
```

**B1.1 *(2 pts)*** — Si les mesures sont prises toutes les 5 secondes, après combien de temps la moyenne mobile sera-t-elle calculée sur N valeurs complètes ? Que renvoie `moyenneMobile()` avant ce délai ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**B1.2 *(2 pts)*** — Tracez l'état de l'alarme (OK ou CRITIQUE) pour la séquence de moyennes mobiles suivante. Supposez que l'anti-rebond est 0s pour simplifier (répondre uniquement avec la logique SH/SB) :

```
Séquence : 36,5 / 38,2 / 39,0 / 37,8 / 36,5 / 35,9 / 35,5

Etat : _____ / _____ / _____ / _____ / _____ / _____ / _____
```

**B1.3 *(2 pts)*** — Dans le code, l'anti-rebond de 15 secondes est implémenté avec `millis()`. Expliquez pourquoi `delay(15000)` serait une mauvaise alternative dans un firmware de supervision.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**B1.4 *(2 pts)*** — La variable `debord` est déclarée `static` dans la fonction. Qu'est-ce que `static` signifie ici et pourquoi est-ce indispensable pour l'anti-rebond ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**B1.5 *(2 pts)*** — Modifiez le seuil haut à SH = 40°C et la bande d'hystérésis à 3°C (SB = SH − 3). Réécrivez les deux lignes const :

```cpp
const float SH = _____ ;
const float SB = _____ ;
```

??? success "Réponses"
    **B1.1** — Après **5 mesures** (soit 25 s) le buffer est plein ; tant qu'il n'est pas plein, la fonction renvoie la **valeur brute** $v$ et non une moyenne.  
    **B1.2** — Seuils : montée à 38,0 ; descente à 36,0.  
    `OK / CRITIQUE / CRITIQUE / CRITIQUE / CRITIQUE / OK / OK`  
    (37,8 et 36,5 restent critiques : on est entre les deux seuils, l'alarme ne se coupe qu'en dessous de 36,0).  
    **B1.3** — `delay(15000)` **bloque tout le microcontrôleur** pendant 15 s : plus de mesure, de MQTT ni d'alarme. `millis()` mesure le temps sans bloquer.  
    **B1.4** — `static` : la variable **conserve sa valeur entre deux appels** de la fonction. Sans cela, `debord` serait remise à zéro à chaque appel et le chronomètre ne pourrait jamais atteindre 15 s.  
    **B1.5** — `const float SH = 40.0;` et `const float SB = 37.0;` ($40 - 3$).

---

## B2 — KPI et tendance (10 pts)

> La serre enregistre les données suivantes (moyennes mobiles sur 10 minutes) :

| **Heure** | **08h00** | **08h10** | **08h20** | **08h30** | **08h40** |
|---|---|---|---|---|---|
| T° (°C) | 24,2 | 25,8 | 27,4 | 29,0 | 30,6 |

**B2.1 *(2 pts)*** — Calculez la tendance en °C/heure :

Tendance = ($T_{\mathrm{finale}}$ - $T_{\mathrm{initiale}}$) / durée_en_heures  

$$= \dfrac{\underline{\hspace{2.5em}} - \underline{\hspace{2.5em}}}{40/60}$$

= \_\_\_\_\_ °C/heure  

**B2.2 *(2 pts)*** — Avec cette tendance, estimez l'heure à laquelle la température dépassera le seuil CRITIQUE de 38°C :

```
ΔT nécessaire = 38 - _____ = _____ °C
Durée = ΔT / (tendance/60) = _____ / _____ = _____ minutes
Heure estimée = 08h40 + _____ min = _____
```

**B2.3 *(2 pts)*** — Quelle est la valeur ajoutée d'une **alarme prédictive** basée sur la tendance par rapport à une alarme simple sur seuil ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**B2.4 *(2 pts)*** — Le taux d'alarme sur la dernière heure est 15% (9 mesures sur 60 en état CRITIQUE). Formulez une phrase de rapport de maintenance à partir de ce KPI :

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**B2.5 *(2 pts)*** — Rédigez la ligne JSON complète que l'ESP32 publierait sur MQTT avec toutes les informations calculées (valeur brute, moyenne mobile, tendance, alarme) :

```json
{
  "device" : "serre-hydro-01",
  "ts"     : 1710000000,
  "t_raw"  : _____,
  "t_moy"  : _____,
  "trend"  : _____,
  "alarme" : "_____"
}
```

??? success "Réponses"
    **B2.1** — Tendance $= \dfrac{30{,}6 - 24{,}2}{40/60} = \dfrac{6{,}4}{0{,}667} = 9{,}6\,°\mathrm{C/h}$.  
    **B2.2** — $\Delta T = 38 - 30{,}6 = 7{,}4\,°\mathrm{C}$ ; durée $= \dfrac{7{,}4}{9{,}6/60} = \dfrac{7{,}4}{0{,}16} \approx 46\,\mathrm{min}$ ; heure estimée : 08 h 40 + 46 min ≈ **09 h 26**.  
    **B2.3** — L'alarme prédictive **prévient avant** le dépassement : on a du temps pour agir. Une alarme sur seuil ne réagit qu'**après** le problème.  
    **B2.4** — Exemple : « Sur la dernière heure, l'équipement est resté en alarme critique 15 % du temps (9 mesures sur 60) : une vérification de la ventilation est recommandée. »  
    **B2.5** — Exemple cohérent : `"t_raw": 30.9, "t_moy": 30.6, "trend": 9.6, "alarme": "OK"`.

---

# ═══════════════════════════════════════════
# BLOC C — KICAD ET ANALYSE DE SCHÉMA (20 pts)
# ═══════════════════════════════════════════

## C1 — Lecture et identification d'erreurs (10 pts)

> Un apprenti a saisi le schéma suivant d'un filtre RC passe-bas avec indicateur LED. Il comporte **4 erreurs ou oublis**.

```
Schéma décrit :
  J1 (connecteur 2 broches) :
    pin1 → +5V
    pin2 → GND

  R1 (10kΩ) :
    pin1 → +5V
    pin2 → "noeud_RC"

  C1 (100nF CMS) :
    pin1 → "noeud_RC"
    pin2 → GND

  R2 (330Ω) :
    pin1 → "noeud_RC"
    pin2 → Anode LED1

  LED1 (rouge 5mm) :
    Anode → R2 pin2
    Cathode → GND

  Il n'y a qu'un seul PWR_FLAG, sur GND.
  LED1 est câblée avec Anode → GND et Cathode → R2 (à la place)
```

**C1.1 *(4 pts)*** — Identifiez les 4 erreurs/oublis et proposez la correction pour chacune :

| **#** | **Erreur** | **Correction** |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

**C1.2 *(2 pts)*** — Après correction de toutes les erreurs, combien d'erreurs l'ERC devrait-il retourner ? Citez-les.

```
Nombre d'erreurs ERC restantes : _____
Liste : _________________________________________________
```

**C1.3 *(2 pts)*** — La fréquence de coupure du filtre RC est $f_{c} = \frac{1}{2\pi R_{1} C_{1}}$. Calculez $f_{c}$ :

$$f_{c} = \frac{1}{2\pi \times 10000 \times 100\times10^{-9}} = \frac{1}{2\pi \times \_\_\_\_} = \_\_\_\_ \text{ Hz}$$

**C1.4 *(2 pts)*** — Quel est le courant qui circule dans LED1 si la tension à "noeud_RC" est 4,8V (après filtrage) avec Vled = 2V ?

```
If = (Vnoeud_RC - Vled) / R2 = (_____ - _____) / _____ = _____ mA
```

??? success "Réponses"
    **C1.1** — Erreurs certaines d'après l'énoncé :  
    | # | Erreur | Correction |
    |---|---|---|
    | 1 | LED câblée à l'envers (anode vers GND) | Anode côté R2, cathode vers GND |
    | 2 | Un seul PWR_FLAG (sur GND) | Ajouter un PWR_FLAG sur +5V |
    | 3 et 4 | L'énoncé ne permet pas de les identifier avec certitude | À compléter avec l'enseignant (pistes habituelles : empreintes non associées, références non annotées) |
    
    **C1.2** — Après correction complète : **0 erreur** ERC.  
    **C1.3** — $f_c = \dfrac{1}{2\pi \times 10\,000 \times 100 \times 10^{-9}} = \dfrac{1}{2\pi \times 10^{-3}} \approx 159\,\mathrm{Hz}$.  
    **C1.4** — $I_f = \dfrac{4{,}8 - 2}{330} \approx 8{,}5\,\mathrm{mA}$.

---

## C2 — Empreintes et netlist (10 pts)

**C2.1 *(4 pts)*** — Associez chaque composant à son empreinte KiCad correcte :

| **Composant** | **Package requis** | **Empreinte KiCad** |
|---|---|---|
| R1 (10kΩ) | CMS 0805 | |
| C1 (100nF) | CMS 0805 | |
| LED1 | THT 5mm | |
| J1 | THT 2.54mm 2 broches | |

**C2.2 *(3 pts)*** — Voici un extrait de netlist :

```
(net (name "+5V")
  (node (ref J1)  (pin 1))
  (node (ref R1)  (pin 1))
)
(net (name "noeud_RC")
  (node (ref R1)  (pin 2))
  (node (ref C1)  (pin 1))
  (node (ref R2)  (pin 1))
)
(net (name "GND")
  (node (ref J1)  (pin 2))
  (node (ref C1)  (pin 2))
  (node (ref LED1)(pin K))
)
```

**C2.2.1 *(1 pt)*** — Combien de nœuds électriques distincts cette netlist décrit-elle ?

\_\_\_\_\_\_\_\_\_

**C2.2.2 *(1 pt)*** — La cathode de LED1 (pin K) est connectée à GND. Est-ce correct pour une LED alimentée par pin 3 → R2 → Anode → Cathode → GND ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**C2.2.3 *(1 pt)*** — Le nœud `noeud_RC` regroupe 3 pins. Identifiez le problème si R2 pin2 n'est **pas** dans ce net mais que l'anode de LED1 y est rattachée.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**C2.3 *(3 pts)*** — Après routage, le DRC signale `Unrouted net : noeud_RC (1 ratsnest)`. Expliquez ce que cela signifie et comment le corriger.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **C2.1** — R1 : `Resistor_SMD:R_0805_2012Metric` ; C1 : `Capacitor_SMD:C_0805_2012Metric` ; LED1 : `LED_THT:LED_D5.0mm` ; J1 : `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`.  
    **C2.2.1** — **3 nœuds** : `+5V`, `noeud_RC`, `GND` (l'extrait ne montre pas le net entre R2 et l'anode).  
    **C2.2.2** — **Oui** : la cathode d'une LED va côté masse.  
    **C2.2.3** — La pin 2 de R2 resterait **en l'air** (non connectée) et l'anode serait reliée **directement** à `noeud_RC` : la LED n'est plus protégée par la résistance, **courant non limité** et risque de destruction.  
    **C2.3** — Un ratsnest non routé est une **liaison qui existe dans le schéma mais pas encore en piste** sur le PCB. Il faut **tracer la piste manquante** (ou changer de face avec un via), puis relancer le DRC.

---

# ═══════════════════════════════════════════
# BLOC D — NORMES, IPC ET DAT (16 pts)
# ═══════════════════════════════════════════

## D1 — IPC-A-610 Classe 2 (6 pts)

> Inspection d'une carte de prototypage ESP32 IoT. Classifiez chaque observation selon IPC-A-610 Classe 2 :

| **Observation** | **Classif. Cl.2** | **Justification** |
|---|---|---|
| CMS 0805 décalé de 28% de sa largeur | | |
| Pont de soudure entre deux pads R1-R2 adjacents | | |
| Remplissage PTH 7805 = 78% | | |
| Résidu de flux de colophane autour de U1 | | |
| LED THT : pointe de soudure (icicle) 1,2mm | | |
| Condensateur électrolytique C3 inversé | | |

??? success "Réponses"
    | Observation | Classe 2 | Justification |
    |---|---|---|
    | CMS décalé de 28 % | Conforme | Décalage inférieur ou égal à 50 % de la largeur |
    | Pont R1-R2 | **Non conforme** | Court-circuit |
    | Remplissage PTH 78 % | Conforme | Supérieur ou égal à 75 % |
    | Résidu de flux de colophane | Acceptable | Résidu non conducteur (nettoyage selon cahier des charges) |
    | Pointe de soudure de 1,2 mm | Non conforme par précaution | Peut réduire l'isolement ; critère exact à confirmer |
    | Condensateur C3 inversé | **Non conforme** | Polarité inversée : risque d'explosion |

---

## D2 — Normes : association (4 pts)

> Associez chaque norme à sa description (reliez par une flèche ou écrivez la lettre) :

| **Norme** | **Description** |
|---|---|
| IPC-A-610 | A. Acceptabilité des assemblages électroniques (brasures) |
| IPC-2221 | B. Tests environnementaux (chaleur, froid, humidité) |
| CEI 60068-2 | C. Sécurité des appareils électriques de mesure |
| CEI 61010-1 | D. Standard générique de conception PCB |
| ISO 9001 | E. Système de management de la qualité |

**D2.1 *(2 pts)*** — Quelle norme s'applique pour vérifier que les clearances de votre PCB KiCad (0,25 mm) sont conformes pour un produit industriel ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**D2.2 *(2 pts)*** — Une carte IoT pour serre agricole doit résister à 40°C / 85% d'humidité pendant 96 heures. Quelle norme définit cette condition de test ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    IPC-A-610 → **A** ; IPC-2221 → **D** ; CEI 60068-2 → **B** ; CEI 61010-1 → **C** ; ISO 9001 → **E**.  
    **D2.1** — **IPC-2221** (conception des PCB, classe B industrielle).  
    **D2.2** — **CEI 60068-2** (essai de chaleur humide : 40 °C / 85 % HR, 96 h, série 60068-2-78).

---

## D3 — DAT Électronique : sections manquantes (6 pts)

> Voici un DAT incomplet livré au client. Identifiez les sections manquantes et leur impact.

```
DAT-NE555-001 contient :
  ✅ Section 1 : Page de garde + historique révisions
  ✅ Section 3 : Schéma électronique + calculs
  ✅ Section 5 : BOM complète
  ❌ Section 2 : [manquante]
  ❌ Section 7 : [manquante]
  ❌ Section 8 : [manquante]
```

**D3.1 *(3 pts)*** — Pour chaque section manquante, indiquez son titre et son impact si elle est absente :

| **Section** | **Titre** | **Impact de son absence** |
|---|---|---|
| Section 2 | | |
| Section 7 | | |
| Section 8 | | |

**D3.2 *(3 pts)*** — Rédigez les 5 informations clés de la Section 7 (Contraintes de fonctionnement) pour la carte NE555/7805 (Vin=12V, serre à 0–60°C) :

```
7.1 Alimentation : Vin nominale = _____V, min = _____V, max = _____V
7.2 Températures : opérationnelle = _____°C à _____°C
7.3 IP carte nue : IP_____
7.4 NE555 VCC max : _____V
7.5 Courant LED max : _____ mA
```

??? success "Réponses"
    **D3.1** —
    
    | Section | Titre | Impact de son absence |
    |---|---|---|
    | 2 | Description fonctionnelle | On ne comprend pas le rôle de la carte ni ses interfaces |
    | 7 | Contraintes de fonctionnement | L'utilisateur peut dépasser les limites (tension, température) et détruire la carte |
    | 8 | Résultats de validation | Aucune preuve que la carte respecte les exigences |
    
    **D3.2** — Exemple : Vin nominale **12 V**, min environ **7 V**, max **35 V** (7805) ; température opérationnelle **0 à 60 °C** ; IP carte nue : **IP00** ; NE555 $V_{CC}$ max **16 V** ; courant LED max **25 mA**.

---

# ═══════════════════════════════════════════
# BLOC E — CAS INTÉGRATEUR (24 pts)
# ═══════════════════════════════════════════

> **AGRIMAX** commande un système de supervision de serre. La carte mesure la température (DHT22, pin 4) et contrôle une LED d'alarme (pin 2). Elle publie sur AWS IoT Core via MQTT TLS.

## E1 — Conception électronique (8 pts)

**E1.1 *(2 pts)*** — Le client demande une résistance de pull-up sur la ligne DATA du DHT22. Quelle est la valeur recommandée et entre quels points est-elle câblée ?

```
Valeur recommandée : _____ kΩ
Câblage : entre _____ et _____
```

**E1.2 *(3 pts)*** — Rédigez la description des composants manquants pour ce circuit (connecteur d'alimentation, régulateur, condensateurs) en complétant le tableau :

| **Réf.** | **Désignation** | **Valeur** | **Empreinte** |
|---|---|---|---|
| J1 | Connecteur 2P | — | PinHeader_1x02_P2.54mm |
| U1 | Régulateur 5V | 7805 | TO-220-3_Vertical |
| C1 | Cond. découplage Vin | | C_0805 |
| C2 | Cond. stabilité Vout | | CP_Radial_D5.0mm_P2.50mm |

**E1.3 *(3 pts)*** — Citez les 5 points de la checklist obligatoire avant de lancer l'impression 3D du boîtier :

1. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  2. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  3. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
4. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  5. \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **E1.1** — **10 kΩ** (4,7 à 10 kΩ), câblée entre la ligne **DATA** et **VCC**.  
    **E1.2** — C1 : **100 nF** ; C2 : **10 µF** (électrolytique).  
    **E1.3** — Proposition (à valider selon le cours) : **dimensions** de la carte et des trous de fixation ; **position des connecteurs** et accès ; **ventilation** et échauffement du régulateur ; **tolérances d'impression** et jeu ; **matériau adapté à la température** de la serre (le PLA ramollit vers 60 °C).

---

## E2 — Mesures et incertitudes (8 pts)

> La tension Vout est mesurée avec un Fluke 87V (classe 0,5%, résolution 0,001V). Trois mesures : 4,998V / 5,002V / 4,997V.

**E2.1 *(4 pts)*** — Calculez $\bar{V}$, $u_{A}$, $u_{B,cl}$, $u_{c}$, $U$ et exprimez le résultat :

(Montrez tous les calculs)  

$$V_{out} = (\underline{\hspace{2.5em}} \pm \underline{\hspace{2.5em}}) V [95\,\mathrm{\%}]$$

**E2.2 *(2 pts)*** — La fréquence NE555 mesurée à l'oscillo est 0,978 Hz. La spécification est 1 Hz ±10%.

```
[0,90 ; 1,10] Hz → f mesurée = 0,978 Hz → ☐ Conforme   ☐ Non conforme
Écart par rapport au nominal = _____  %
```

**E2.3 *(2 pts)*** — Lors de l'inspection, le remplissage des PTH du connecteur J1 est évalué à 72%. Quelle classification IPC-A-610 Classe 2 ? Quelle action ?

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

??? success "Réponses"
    **E2.1** — $\bar{V} = 4{,}999\,\mathrm{V}$ ; $s \approx 0{,}00265$ ; $u_A \approx 0{,}00153$ ; $u_{B,rés} \approx 0{,}00029$ ; $u_{B,cl} = \dfrac{0{,}5 \times 4{,}999}{100\sqrt{3}} \approx 0{,}01443$ ; $u_c \approx 0{,}01451$ ; $U \approx 0{,}0290$ → **0,029 V**. $V_{out} = (4{,}999 \pm 0{,}029)\,\mathrm{V}$ [95 %].  
    **E2.2** — $0{,}978 \in [0{,}90\,;\,1{,}10]$ : **conforme** ; écart $= \dfrac{0{,}978 - 1}{1} \times 100 = -2{,}2\,\%$.  
    **E2.3** — 72 % est **inférieur à 75 %** : **non conforme** en classe 2. Action : **retoucher** la brasure (refusion avec apport de soudure) puis contrôler à nouveau.

---

## E3 — Documentation et synthèse (8 pts)

**E3.1 *(3 pts)*** — Rédigez le tableau de résultats du PV de validation (TC-01 Vout, TC-02 fréquence, TC-03 inspection IPC) pour la carte AGRIMAX :

| TC# | Exigence | Résultat ± U | Conf. |
|---|---|---|---|
| TC-01 | $V_{out} = 5\,\mathrm{V} \pm 5\,\mathrm{\%} = [4{,}75;5{,}25]V$ |  |  |
| TC-02 | $f = 1\,\mathrm{\mathrm{Hz}} \pm 10\,\mathrm{\%} = [0{,}90;1{,}10]\mathrm{Hz}$ |  |  |
| TC-03 | Assemblage IPC-A-610 Cl.2 |  |  |

**E3.2 *(2 pts)*** — TC-03 est NON CONFORME (remplissage J1 = 72%). Rédigez la conclusion globale du PV :

```
☐ CONFORME   ☐ NON CONFORME   ☐ CONFORME AVEC RÉSERVE

Conclusion : _____________________________________________________________
```

**E3.3 *(3 pts)*** — Le client reçoit le dossier complet. Citez les 3 documents qui constituent le dossier de livraison et le rôle de chacun :

| **Document** | **Rôle** |
|---|---|
| | |
| | |
| | |

??? success "Réponses"
    **E3.1** —
    
    | TC# | Exigence | Résultat ± U | Conf. |
    |---|---|---|---|
    | TC-01 | $V_{out} = 5\,\mathrm{V} \pm 5\,\%$ | $(4{,}999 \pm 0{,}029)\,\mathrm{V}$ | Oui |
    | TC-02 | $f = 1\,\mathrm{Hz} \pm 10\,\%$ | $0{,}978\,\mathrm{Hz}$ (écart −2,2 %) | Oui |
    | TC-03 | Assemblage IPC-A-610 Cl. 2 | Remplissage J1 = 72 % | **Non** |
    
    **E3.2** — **NON CONFORME** tant que J1 n'est pas retouché. Conclusion : « Les mesures électriques sont conformes, mais le remplissage de la brasure de J1 (72 %) est inférieur au minimum de 75 % ; retouche et nouveau contrôle exigés avant livraison. »  
    **E3.3** — **DAT** (décrit la carte, ses calculs et ses contraintes), **PV de validation fonctionnelle** (preuves chiffrées de conformité), **fiche MES** (atteste l'installation et la remise au client).

---

## 📊 RÉCAPITULATIF BARÈME

| **Bloc** | **Points** |
|---|---|
| A — Métrologie | /20 |
| B — KPI / Alarmes | /20 |
| C — KiCad | /20 |
| D — Normes / DAT | /16 |
| E — Cas Intégrateur | /24 |
| **TOTAL** | **/100** |

> *Note /20 = score / 5*

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Consolidation Finale – Version 1.0 – 2026**
