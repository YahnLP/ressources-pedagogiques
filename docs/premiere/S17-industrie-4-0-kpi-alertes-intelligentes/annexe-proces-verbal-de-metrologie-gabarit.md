# 📄 PROCÈS-VERBAL DE MÉTROLOGIE — GABARIT PROFESSIONNEL
## Vérification d'un Capteur IoT · S17 · 2ᵉ ANNÉE · E2

---

> **Instructions** : Complète ce PV avec tes mesures réelles ou simulées.
> Ce document est un livrable du portfolio E2.
> Il doit être exporté en PDF final (mise en page soignée obligatoire).

---

## ══════════════════════════════════════════════
## PAGE DE GARDE
## ══════════════════════════════════════════════

```
  PROCÈS-VERBAL DE MÉTROLOGIE

  Référence document  : PV-MET-[AAAA]-[NNN]
  Version             : 1.0
  Date d'établissement: [JJ/MM/AAAA]
  Opérateur           : [Nom Prénom]
  Groupe              : [Groupe]
  Établissement       : [Nom de l'établissement]

  Équipement contrôlé :
    Désignation    : Capteur de température DHT22
    N° de série    : ESP32_STATION_01
    Localisation   : Laboratoire E2
    Projet         : CLIMASENS — Station IoT Industrielle

  Étalon de référence :
    Désignation    : Thermomètre numérique de référence
    Modèle / Marque: ___________________________
    N° de série    : ___________________________
    Date étalonnage: ___________________________
    Traçabilité    : ☐ Certifié laboratoire accrédité ☐ Étalon interne

  Statut final       : ☐ CONFORME ☐ NON CONFORME ☐ CONFORME SOUS RÉSERVE

  Validé par         : ___________________________  Date : _______________
```

---

## SECTION 1 — OBJET ET DOMAINE D'APPLICATION

```
1.1 Objet du contrôle :
    Ce procès-verbal a pour objet de vérifier la conformité du capteur
    de température DHT22, utilisé dans la station IoT CLIMASENS, par rapport
    aux spécifications du fabricant.

1.2 Spécifications du DHT22 (extrait datasheet) :
    ┌────────────────────────────────────────────────────────────────┐
    │ Grandeur mesurée   : Température                               │
    │ Plage de mesure    : −40°C à +80°C                            │
    │ Précision déclarée : ± 0,5°C                                  │
    │ Résolution         : 0,1°C                                    │
    │ Temps de réponse   : < 5 secondes (63% de la variation)       │
    │ Alimentation       : 3,3V ou 5V (± 5%)                        │
    └────────────────────────────────────────────────────────────────┘

1.3 Critère de conformité retenu :
    Le capteur est déclaré CONFORME si :
    │Biais│ + U élargie (k=2) ≤ 0,5°C (spécification constructeur)
```

---

## SECTION 2 — CONDITIONS DE MESURE

```
2.1 Environnement de mesure :
    Date et heure    : ___________________________
    Lieu             : ___________________________
    Température ambiante de la pièce : _______ °C
    Humidité relative de la pièce    : _______ %
    Pression atmosphérique           : _______ hPa
    Stabilité thermique              : ☐ Stable (±0,2°C sur 10 min) ☐ Variable

2.2 Montage de mesure :
    ┌──────────────────────────────────────────────────────────────┐
    │  [Thermomètre étalon] ──┐                                    │
    │                          ├── [Point de mesure commun]        │
    │  [DHT22 sur ESP32]    ──┘                                    │
    │                                                              │
    │  [ESP32] ── MQTT ── [Node-RED] ── [Tableau de relevés]       │
    └──────────────────────────────────────────────────────────────┘
    Distance étalon / DHT22 : _______ cm
    Temps de stabilisation avant première mesure : _______ minutes

2.3 Fréquence d'acquisition :
    Une mesure toutes les : _______ secondes
    Nombre de mesures : _______ (minimum 10 requis)
```

---

## SECTION 3 — TABLEAU DE MESURES

> Relever alternativement : étalon puis DHT22 (même instant), noter les deux valeurs.

| N° | Heure | T° Étalon (°C) | T° DHT22 (°C) | Écart ei (°C) | Écart² (°$C^{2}$) |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |
| 8 | | | | | |
| 9 | | | | | |
| 10 | | | | | |
| 11 | | | | | |
| 12 | | | | | |
| **Σ** | | | | $Σei = \underline{\hspace{2.5em}}$ | $Σei^2 = \underline{\hspace{2.5em}}$ |

---

## SECTION 4 — CALCULS STATISTIQUES

### 4.1 Biais (erreur systématique)

```
Formule : e̅ = Σei / n

e̅ = _______ / _______ = _______ °C

Interprétation :
  → Si e̅ > 0 : le DHT22 surestime la vraie valeur de _______ °C
  → Si e̅ < 0 : le DHT22 sous-estime la vraie valeur de _______ °C
  → Si e̅ ≈ 0 : pas d'erreur systématique détectable
```

### 4.2 Écart-type expérimental (fidélité)

Formule : σ = √[ Σei² / (n−1) ]  

σ = √[ \_\_\_\_\_\_\_ / \_\_\_\_\_\_\_ ]  
= √[ \_\_\_\_\_\_\_ ]  

$$= \underline{\hspace{2.5em}} °C$$

Interprétation :  
→ σ représente la dispersion aléatoire des mesures du DHT22  
→ 68% des mesures sont dans l'intervalle [e̅ − σ ; e̅ + σ]  

### 4.3 Incertitude de répétabilité

```
Formule : u = σ / √n

u = _______ / √_______ = _______ / _______ = _______ °C

Cette incertitude reflète l'instabilité résiduelle sur la moyenne.
```

### 4.4 Incertitude élargie (intervalle de confiance 95%)

Formule : U = k × u    avec k = 2 (facteur d'élargissement, loi normale, 95%)  

$$U = 2 \times \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} °C$$

RÉSULTAT FINAL DE LA MESURE :  

T_DHT22 = \_\_\_\_\_\_\_ ± \_\_\_\_\_\_\_ °C     (k = 2, intervalle de confiance 95%)  

---

## SECTION 5 — ANALYSE ET CONCLUSIONS

### 5.1 Tableau de synthèse

```
┌─────────────────────────────────────────────────────────────────────┐
│  Grandeur         │ Valeur calculée │ Spécification │ Statut        │
├─────────────────────────────────────────────────────────────────────┤
│  Biais │e̅│         │ _______ °C      │               │               │
│  Écart-type σ     │ _______ °C      │               │               │
│  Incertitude U    │ _______ °C      │               │               │
│  ERREUR TOTALE    │ _______ °C      │   ≤ 0,5°C     │ ☐ OK  ☐ FAIL  │
│  (│e̅│ + U)        │                 │               │               │
└─────────────────────────────────────────────────────────────────────┘
Erreur totale = │e̅│ + U = _______ + _______ = _______ °C
```

### 5.2 Décision de conformité

```
Critère : Erreur totale ≤ 0,5°C (spécification constructeur)

Erreur totale calculée : _______ °C

DÉCISION : ☐ CONFORME     ← Erreur totale ≤ 0,5°C
           ☐ NON CONFORME ← Erreur totale > 0,5°C
           ☐ CONFORME SOUS RÉSERVE ← Erreur totale proche de la limite
```

### 5.3 Analyse des causes (si non conforme ou valeurs élevées)

```
Causes possibles identifiées :
  ☐ Dérive thermique de la pièce pendant les mesures
  ☐ Distance trop grande entre étalon et DHT22
  ☐ Influence du flux d'air (courants d'air parasites)
  ☐ Chauffage du capteur par le courant du circuit (auto-échauffement)
  ☐ Défaut du capteur spécifique à cet exemplaire

Autre : ____________________________________________________________________
```

### 5.4 Recommandations

```
☐ Utiliser ce capteur en production sans restriction
☐ Appliquer une correction de biais de _______ °C dans le logiciel (Node-RED)
☐ Remplacer le capteur (non conforme)
☐ Répéter les mesures dans de meilleures conditions d'environnement

Commentaires libres :
_____________________________________________________________________________
_____________________________________________________________________________
```

---

## SECTION 6 — SIGNATURE ET ARCHIVAGE

```
Ce document a été établi par :

Opérateur    : ___________________________   Signature : _______________
Vérificateur : ___________________________   Signature : _______________

Date d'archivage : ___________________________
Durée de conservation : 5 ans (règle interne qualité)

Référence système de gestion documentaire :
  Classeur physique : ☐ Oui ☐ Non
  Archive numérique : portfolio_E2/PV_metrologie/[Nom_Prénom]/
  Format de dépôt   : ☐ PDF (obligatoire) ☐ Fichier source conservé
```

---

## ANNEXE A — Graphique des écarts

> Tracer ici (ou insérer capture tableur) le graphe des écarts ei en fonction du numéro de mesure.
> Y ajouter : la ligne biais e̅, les lignes ±2σ, la ligne de spécification ±0,5°C.

```
[INSÉRER LE GRAPHIQUE DES ÉCARTS ICI]

Le graphique doit montrer :
  ─── Biais moyen e̅  (ligne horizontale centrale)
  ─ ─ Limites ±2σ   (bandes de dispersion)
  ─ · ─ Spécification ±0,5°C (limites constructeur)
  ● ● Points de mesure individuels
```

---

## ANNEXE B — Calculs de vérification (brouillon)

```
[ESPACE POUR LES CALCULS INTERMÉDIAIRES]
```

---

*PV de Métrologie — Gabarit Professionnel*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S17*
*Portfolio E2 · Compétence C3.1*
