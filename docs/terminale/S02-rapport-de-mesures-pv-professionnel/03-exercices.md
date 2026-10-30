# 🔬 ATELIER — S2 ANNÉE 3 – E2
## Rédaction du PV de Mesure + Calcul des Incertitudes + Rapport IPC

---

## 🎯 OBJECTIFS DE L'ATELIER

- ✅ Rédiger un PV de mesure professionnel complet en 10 sections
- ✅ Calculer les incertitudes de type A (statistique), B (résolution + classe)
- ✅ Exprimer les résultats au format normé : valeur ± U unité [95%]
- ✅ Rédiger un rapport de conformité IPC-A-610 Classe 2

---

## 📋 CONTEXTE DE MESURE

> Vous intervenez pour INDUSTECH SAS. On vous demande de **vérifier les résistances de pull-up I2C** (R1 et R2, spécification nominale : 4,7 kΩ ±5%) et **la tension d'alimentation 3,3V** de la carte ESP32 IoT avant mise en production. Vous disposez d'un **Fluke 87V** (N° série 7435280, classe 0,5%, étalonné le 2026-01-15, valide jusqu'au 2027-01-14, certificat COFRAC N° LAB-2026-0047).

---

## PARTIE A — Mesures de Résistance (Pull-up I2C)

### A1 — Données brutes (5 mesures répétées)

> Voici les 5 mesures relevées sur R1 (résistance de pull-up SDA) avec le Fluke 87V en mode Ω :

| **Mesure** | **Valeur (Ω)** |
|---|---|
| m1 | 4 718 |
| m2 | 4 711 |
| m3 | 4 725 |
| m4 | 4 709 |
| m5 | 4 717 |

**A1.1 *(1 pt)*** — Calculez la moyenne $\bar{x}$ :

$$\bar{x} = \frac{4718 + 4711 + 4725 + 4709 + 4717}{5} = \frac{\_\_\_\_\_}{5} = \_\_\_\_ \text{ Ω}$$

**A1.2 *(2 pts)*** — Calculez l'écart-type s et l'incertitude de type A :

| $m_{i}$ | $m_{i} - \bar{x}$ | $(m_{i} - \bar{x})^2$ |
|---|---|---|
| 4718 | | |
| 4711 | | |
| 4725 | | |
| 4709 | | |
| 4717 | | |
| **Somme** | — | |

$$s = \sqrt{\frac{\sum(m_{i} - \bar{x})^2}{n-1}} = \sqrt{\frac{\_\_\_\_\_}{4}} = \_\_\_\_ \text{ Ω}$$

$$u_{A} = \frac{s}{\sqrt{n}} = \frac{\_\_\_\_}{\sqrt{5}} = \_\_\_\_ \text{ Ω}$$

---

**A1.3 *(2 pts)*** — Calculez l'incertitude de type B (résolution + classe) :

Résolution Fluke 87V en gamme 6 kΩ : **1 Ω**

$$u_{B,rés} = \frac{\text{résolution}}{2\sqrt{3}} = \frac{1}{2 \times 1,732} = \frac{1}{\_\_\_\_} = \_\_\_\_ \text{ Ω}$$

Classe 0,5% sur la valeur mesurée :

$$u_{B,classe} = \frac{0,5 \times \bar{x}}{100 \times \sqrt{3}} = \frac{0,5 \times \_\_\_\_}{100 \times 1,732} = \frac{\_\_\_\_}{\_\_\_\_} = \_\_\_\_ \text{ Ω}$$

---

**A1.4 *(2 pts)*** — Calculez l'incertitude combinée et élargie :

$$u_{c} = \sqrt{u_A^2 + u_{B,rés}^2 + u_{B,classe}^2} = \sqrt{(\_\_\_)^2 + (\_\_\_)^2 + (\_\_\_)^2} = \_\_\_\_ \text{ Ω}$$

$$U = 2 \times u_{c} = 2 \times \_\_\_\_ = \_\_\_\_ \text{ Ω}$$

**Arrondir U par excès à 1 chiffre significatif :**

$$U_{arrondi} = \_\_\_\_ \text{ Ω}$$

**Expression finale du résultat R1 :**

$$\boxed{R_1 = (\text{\_\_\_\_ ± \_\_\_\_}) \text{ Ω } [95\%]}$$

---

**A1.5 *(1 pt)*** — La spécification est 4,7 kΩ ±5% (soit 4 465 Ω à 4 935 Ω). La mesure est-elle dans la tolérance ?

```
Valeur mesurée    : _____ Ω
Intervalle       : [4 465 ; 4 935] Ω
Conclusion : ☐ Conforme   ☐ Non conforme
```

---

### A2 — Mesure de R2 (pull-up SCL)

> La mesure unique de R2 donne : **4 831 Ω** (une seule mesure, pas de répétition).

**A2.1 *(2 pts)*** — Sans répétition possible ($u_{A}$ = 0), calculez l'incertitude élargie de R2 avec seulement $u_{B}$ résolution et $u_{B}$ classe :

$$u_{\mathrm{B,rés}} = \underline{\hspace{2.5em}} \Omega$$

$$u_{\mathrm{B,classe}} = \underline{\hspace{2.5em}} \Omega$$

$$u_{\mathrm{c}} = \underline{\hspace{2.5em}} \Omega$$

U = \_\_\_\_\_ Ω → arrondi → \_\_\_\_\_ Ω  

$$R₂ = (\underline{\hspace{2.5em}} \pm \underline{\hspace{2.5em}}) \Omega [95\,\mathrm{\%}]$$

**A2.2 *(1 pt)*** — Même spécification ±5%. R2 est-elle conforme ?

```
Conclusion : ☐ Conforme   ☐ Non conforme   ☐ Sous réserve
```

---

## PARTIE B — Mesure de Tension 3,3V

### Données

> Le Fluke 87V en mode VDC mesure la tension d'alimentation 3,3V de la carte.
> Mesure unique : **3,287 V**. Résolution : 0,001 V. Classe : 0,5%.
> Spécification : 3,3V ±3% (soit [3,201 V ; 3,399 V]).

**B1 *(2 pts)*** — Calculez l'incertitude élargie sur cette mesure de tension :

$$u_{\mathrm{B,rés}} = \dfrac{0{,}001}{2 \times \sqrt{3}} = \underline{\hspace{2.5em}} V$$

$$u_{\mathrm{B,classe}} = 0{,}5 \times \dfrac{3{,}287}{100 \times \sqrt{3}} = \underline{\hspace{2.5em}} V$$

$$u_{\mathrm{c}} = \sqrt{u_{\mathrm{B,rés}}^2 + u_{\mathrm{B,classe}}^2} = \underline{\hspace{2.5em}} V$$

U = 2 × \_\_\_\_\_ = \_\_\_\_\_ V → arrondi → \_\_\_\_\_ V  

$$V = (\underline{\hspace{2.5em}} \pm \underline{\hspace{2.5em}}) V [95\,\mathrm{\%}]$$

**B2 *(1 pt)*** — Avec l'incertitude, l'intervalle de confiance couvre-t-il la valeur nominale de 3,3V ?

```
Intervalle de la mesure : [3,287 - U ; 3,287 + U] = [_____ ; _____] V
3,3 V est dans cet intervalle ? ☐ Oui   ☐ Non
Conclusion conformité : ☐ Conforme   ☐ Non conforme
```

---

## PARTIE C — Rapport de Conformité IPC-A-610

### Données d'inspection visuelle

> Inspection de la carte ESP32 après soudage des composants (Classe 2, industriel).

**Observations relevées :**

| **Zone** | **Observation** | **Ref. IPC** |
|---|---|---|
| C1 (100nF CMS) | Composant décalé de 30% de sa largeur | 8.3.4 |
| R1 (4k7 CMS) | Brasure brillante, mouillage excellent | — |
| U1 (ESP32 module) | Pointe de soudure (icicle) sur pin 12 | 8.3.3 |
| J1 (connecteur USB) | Remplissage trou = 72% | 8.2.2 |
| J2 (connecteur alimentation) | Résidu de flux visible autour de la brasure | 8.4 |

**C1 *(3 pts)*** — Pour chaque observation, indiquez la classification IPC-A-610 Classe 2 (Conforme / Acceptable / Non conforme) et justifiez :

| **Zone** | **Classif. IPC Cl.2** | **Justification** |
|---|---|---|
| C1 (décalé 30%) | | |
| R1 (brasure OK) | | |
| U1 (icicle pin 12) | | |
| J1 (remplissage 72%) | | |
| J2 (résidu flux) | | |

**C2 *(1 pt)*** — Rédigez la conclusion de conformité globale de cette carte en 2 phrases :

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## PARTIE D — Rédaction du PV Complet

> En vous appuyant sur les résultats des Parties A et B, rédigez le PV de mesure complet en utilisant le modèle de la fiche cours. Toutes les sections doivent être présentes. Ce PV sera évalué sur la complétude, la clarté et la rigueur métrologique.

**Checklist du PV avant remise :**

```
☐ En-tête avec référence unique (PV-2026-ESP32-XXX)
☐ Date et lieu
☐ Équipement sous test identifié (EUT)
☐ Instrument identifié : marque, modèle, N° série, certificat, classe, validité
☐ Conditions de mesure (T°, HR)
☐ Tableau de résultats avec incertitudes (format : valeur ± U unité [95%])
☐ Conclusion de conformité (conforme / non conforme / sous réserve)
☐ Remarques et observations
☐ Signature et date
```

---

## 📊 BARÈME DE L'ATELIER

| **Section** | **Points** |
|---|---|
| A1 — Mesures R1 (moyenne, $u_{A}$, $u_{B}$, $u_{c}$, U, conformité) | /10 |
| A2 — Mesure R2 ($u_{B}$, conformité) | /3 |
| B — Tension 3,3V (incertitude + conformité) | /3 |
| C — Rapport conformité IPC (classifications + conclusion) | /4 |
| D — PV complet rédigé | /10 |
| **TOTAL** | **/30** |

> *Ramené à /20 : score × 0,67*

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Version 1.0 – 2026**
