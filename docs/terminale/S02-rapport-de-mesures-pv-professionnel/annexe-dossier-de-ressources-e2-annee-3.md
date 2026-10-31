# 📚 DOSSIER DE RESSOURCES E2 — ANNÉE 3
## Métrologie, IPC-A-610, Outils, Références Normatives

**Ce document est le guide de navigation de votre dossier de ressources E2 A3.**
**Il est à conserver et à enrichir tout au long de l'année.**

---

## 🗂️ STRUCTURE DU DOSSIER DE RESSOURCES

![Arborescence du dossier de ressources E2 année 3 (R01 à R07)](images/arbre-ressources-a3.png)

---

## 📐 R06 — AIDE-MÉMOIRE FORMULES ESSENTIELLES

### Métrologie et incertitudes

$$u_{A} = \frac{s}{\sqrt{n}} \quad \text{avec} \quad s = \sqrt{\frac{\sum(x_{i} - \bar{x})^2}{n-1}}$$

$$u_{B,résolution} = \frac{\text{résolution}}{2\sqrt{3}}$$

$$u_{B,classe} = \frac{\text{classe\%} \times \text{valeur}}{100\sqrt{3}}$$

$$u_{c} = \sqrt{u_A^2 + u_{B1}^2 + u_{B2}^2 + \ldots}$$

$$U = k \cdot u_{c} \quad (k=2 \text{ pour 95\%})$$

$$\text{Expression : } \boxed{X = (\bar{x} \pm U) \text{ unité [95\%]}}$$

### Électronique

$$U = R \times I \quad [\text{V} = \Omega \times \text{A}]$$

$$P = U \times I = \frac{U^2}{R} = R \times I^2 \quad [\text{W}]$$

$$\text{Diviseur de tension : } U_{out} = U_{in} \times \frac{R_2}{R_1 + R_{2}}$$

$$\text{Filtre RC : } f_{c} = \frac{1}{2\pi RC}$$

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROCÈS-VERBAL DE MESURE  |  Réf : PV-[AAAA]-[PROJET]-[NNN]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Date           :            Lieu           :
Donneur d'ordre:            Objet          :

EUT (Équipement Sous Test) :
Désignation : \_\_\_\_\_\_\_ Référence : \_\_\_\_\_\_\_ N°Série : \_\_\_\_\_\_\_

Instrument de mesure :
Appareil    : \_\_\_\_\_\_\_ Marque : \_\_\_\_\_\_\_ Modèle : \_\_\_\_\_\_\_
N° série    : \_\_\_\_\_\_\_ Classe : \_\_\_\_\_\_\_ %
Certificat  : \_\_\_\_\_\_\_ Date étalonnage : \_\_\_\_\_\_\_ Validité : \_\_\_\_\_\_\_

Conditions de mesure :
Température : \_\_\_°C  Hygrométrie : \_\_\_% HR

Résultats :
| Grandeur | Valeur mesurée | Incertitude | Résultat [95%] |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Spécification appliquée :
Conformité : ☐ Conforme  ☐ Non conforme  ☐ Sous réserve de :

Remarques :

Mesureur : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   Responsable qualité : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
Date     :                    Signature :
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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
