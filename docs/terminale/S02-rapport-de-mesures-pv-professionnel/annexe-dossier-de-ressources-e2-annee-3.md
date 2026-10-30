# 📚 DOSSIER DE RESSOURCES E2 — ANNÉE 3
## Métrologie, IPC-A-610, Outils, Références Normatives

**Ce document est le guide de navigation de votre dossier de ressources E2 A3.**
**Il est à conserver et à enrichir tout au long de l'année.**

---

## 🗂️ STRUCTURE DU DOSSIER DE RESSOURCES

```
Ressources_E2_A3_[VotreNom]/
│
├── 00_NAVIGATION.md (ce fichier)
│
├── R01_METROLOGIE/
│   ├── Formules_incertitudes.pdf
│   ├── Exemple_PV_reference.pdf
│   ├── Modele_PV_vierge.odt
│   └── Fiche_codes_multimetre.pdf
│
├── R02_NORME_IPC/
│   ├── IPC-A-610_resume_classes.pdf
│   ├── Photos_defauts_brasures.zip
│   ├── Grille_inspection_IPC.xlsx
│   └── Lexique_IPC.md
│
├── R03_ELECTRONIQUE/
│   ├── Datasheet_ESP32_WROOM32D.pdf
│   ├── Datasheet_ADXL345.pdf
│   ├── Datasheet_DHT22.pdf
│   ├── Datasheet_AMS1117.pdf
│   └── Codage_couleurs_resistances.pdf
│
├── R04_OUTILS_LOGICIELS/
│   ├── Raccourcis_KiCad8.md
│   ├── Raccourcis_FreeCAD.md
│   ├── Templates_Drawio/
│   ├── ArduinoIDE_shortcuts.md
│   └── Saleae_LogicAnalyzer_tips.md
│
├── R05_AWS_IOT/
│   ├── Checklist_connexion_AWS.md
│   ├── Codes_erreur_MQTT.md
│   ├── Modele_Policy_IoT.json
│   └── Règle_SQL_examples.md
│
├── R06_FORMULES/
│   ├── Formules_incertitudes_type_A_B.md  (ce document)
│   ├── Formules_electronique.md
│   └── Calculs_thermiques_boitier.md
│
└── R07_PROJETS/
    ├── DAT_template_vierge.odt
    ├── BOM_template.xlsx
    ├── Plan_de_tests_template.xlsx
    └── Fiche_maintenance_template.odt
```

---

## 📐 R06 — AIDE-MÉMOIRE FORMULES ESSENTIELLES

### Métrologie et incertitudes

$$u_A = \frac{s}{\sqrt{n}} \quad \text{avec} \quad s = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n-1}}$$

$$u_{B,résolution} = \frac{\text{résolution}}{2\sqrt{3}}$$

$$u_{B,classe} = \frac{\text{classe\%} \times \text{valeur}}{100\sqrt{3}}$$

$$u_c = \sqrt{u_A^2 + u_{B1}^2 + u_{B2}^2 + \ldots}$$

$$U = k \cdot u_c \quad (k=2 \text{ pour 95\%})$$

$$\text{Expression : } \boxed{X = (\bar{x} \pm U) \text{ unité [95\%]}}$$

### Électronique

$$V = R \times I \quad [\text{V} = \Omega \times \text{A}]$$

$$P = V \times I = \frac{V^2}{R} = R \times I^2 \quad [\text{W}]$$

$$\text{Diviseur de tension : } V_{out} = V_{in} \times \frac{R_2}{R_1 + R_2}$$

$$\text{Filtre RC : } f_c = \frac{1}{2\pi RC}$$

$$\text{Thermique : } \Delta T = \frac{P}{k \times S} \quad (k \approx 5 \text{ W/m²·K convection naturelle})$$

---

## 🔑 R04 — RACCOURCIS KICAD 8 — RÉFÉRENCE RAPIDE

| **Action** | **Raccourci** |
|---|---|
| Ajouter symbole | `A` |
| Ajouter fil | `W` |
| Ajouter label réseau | `L` |
| Ajouter alimentation | `P` |
| Propriétés composant | `E` |
| Déplacer (avec connexions) | `G` |
| Annoter schéma | Tools → Annotate Schematic |
| ERC | Inspect → Electrical Rules Checker |
| Générer netlist | File → Export → Netlist |
| Zoom ajusté | `Ctrl+Shift+H` |
| Supprimer | `Del` |
| Annuler | `Ctrl+Z` |

---

## 🌐 R05 — CODES ERREUR MQTT (PubSubClient)

| **Code** | **Constante** | **Cause** | **Action** |
|---|---|---|---|
| **-4** | BAD_PROTOCOL | Version MQTT incompatible | Vérifier bibliothèque |
| **-3** | DISCONNECTED | Déconnecté | Vérifier réseau |
| **-2** | CONNECT_FAILED | TCP impossible | Vérifier IP broker |
| **-1** | DISCONNECTED | Avant connect() | Appeler connect() |
| **0** | CONNECTED | ✅ Connecté | — |
| **5** | UNAUTHORIZED | Auth refusée | Vérifier certificats ou PSK |
| **-8** | UNAUTHORIZED | Policy trop restrictive | Console AWS → Policy |

---

## 📋 R01 — MODÈLE PV VIERGE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PROCÈS-VERBAL DE MESURE  |  Réf : PV-[AAAA]-[PROJET]-[NNN]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Date           :            Lieu           :
Donneur d'ordre:            Objet          :

EUT (Équipement Sous Test) :
  Désignation : _______ Référence : _______ N°Série : _______

Instrument de mesure :
  Appareil    : _______ Marque : _______ Modèle : _______
  N° série    : _______ Classe : _______ %
  Certificat  : _______ Date étalonnage : _______ Validité : _______

Conditions de mesure :
  Température : ___°C  Hygrométrie : ___% HR

Résultats :
┌──────────────┬──────────────┬────────────┬──────────────────────────┐
│  Grandeur    │ Valeur mesurée│ Incertitude│ Résultat [95%]           │
├──────────────┼──────────────┼────────────┼──────────────────────────┤
│              │              │            │                          │
│              │              │            │                          │
│              │              │            │                          │
└──────────────┴──────────────┴────────────┴──────────────────────────┘

Spécification appliquée :
Conformité : ☐ Conforme  ☐ Non conforme  ☐ Sous réserve de :

Remarques :

Mesureur : ________________   Responsable qualité : ________________
Date     :                    Signature :
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📋 R02 — GRILLE D'INSPECTION IPC-A-610 RAPIDE

| **Défaut** | **Cl.1** | **Cl.2** | **Cl.3** |
|---|---|---|---|
| Décalage CMS < 25% largeur | Acc. | Acc. | NC |
| Décalage CMS 25–50% | Acc. | NC | NC |
| Pont de soudure (bridging) | Acc. | NC | NC |
| Pointe soudure (icicle) | Acc. | NC | NC |
| Remplissage PTH < 50% | Acc. | NC | NC |
| Remplissage PTH 50–75% | Acc. | NC | NC |
| Remplissage PTH ≥ 75% | ✅ | ✅ | ✅ |
| Void brasure > 25% | Acc. | NC | NC |
| Résidu flux (colophane) | ✅ | Acc. | Acc. |
| Composant manquant | NC | NC | NC |

**Légende :** ✅ Conforme (target) / Acc. = Acceptable / NC = Non conforme

---

## 🔗 RESSOURCES EN LIGNE (vérifiées 2026)

| **Ressource** | **URL** | **Usage** |
|---|---|---|
| IPC-A-610 description officielle | ipc.org | Référence normative |
| LNE métrologie | lne.fr | Traçabilité française |
| COFRAC accréditations | cofrac.fr | Trouver un labo étalonneur |
| KiCad documentation | docs.kicad.org | Aide KiCad 8 |
| AWS IoT docs | docs.aws.amazon.com/iot | AWS IoT Core |
| Mouser (composants) | fr.mouser.com | BOM et datasheets |
| RS Components | fr.rs-online.com | BOM et datasheets |

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Dossier Ressources – Version 1.0 – 2026**
