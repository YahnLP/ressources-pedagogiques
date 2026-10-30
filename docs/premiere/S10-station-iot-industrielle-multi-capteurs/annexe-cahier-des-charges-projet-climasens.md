# 📋 CAHIER DES CHARGES — PROJET CLIMASENS
## Station IoT Industrielle Multi-Capteurs · S10 · 2ᵉ ANNÉE · E2

---

> **Nom / Groupe** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Date** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Encadrant** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Version CdC** : 1.0

---

## 🏭 Contexte industriel

> **CLIMASENS SAS** est un bureau d'ingénierie en automatisme industriel.
> Ils t'ont confié la réalisation d'un prototype de **station de surveillance d'atelier**.
> L'objectif est de surveiller les conditions environnementales d'un local industriel
> (température, humidité, qualité d'air) et d'alerter les opérateurs en cas de dépassement.

---

## 🎯 Fonctions du système

| Fonction | Description | Priorité |
|---|---|---|
| **FP1** | Mesurer la température toutes les 30 secondes | Principale |
| **FP2** | Mesurer l'humidité relative toutes les 30 secondes | Principale |
| **FP3** | Mesurer la qualité de l'air (fumée/gaz) | Principale |
| **FC1** | Transmettre les données via WiFi/MQTT | Contrainte |
| **FC2** | Afficher les données sur un dashboard temps réel | Contrainte |
| **FC3** | Stocker l'historique dans une base de données | Contrainte |
| **FC4** | Alerter si dépassement de seuil | Contrainte |
| **FC5** | Documenter le système (schéma, BOM, PV) | Contrainte |

---

## 📐 Spécifications techniques

### Capteurs requis

| Grandeur mesurée | Capteur | Plage | Précision requise |
|---|---|---|---|
| Température | DHT22 | -10 à +60°C | ± 1°C |
| Humidité relative | DHT22 | 0 à 100% | ± 3% |
| Qualité d'air / Fumée | MQ-2 | 0 à 100% relatif | Seuil détection |
| Luminosité (optionnel) | LDR | 0 à 100% relatif | Relative |

### Seuils d'alerte

```
TEMPÉRATURE :
  ≤ 5°C   → ❄️ ALERTE FROID (protection matériel)
  ≥ 40°C  → 🔥 ALERTE CHALEUR (risque incendie)

HUMIDITÉ :
  ≥ 80%   → 💧 ALERTE HUMIDITÉ ÉLEVÉE (condensation)
  ≤ 20%   → 🏜️ ALERTE HUMIDITÉ FAIBLE (risque électrostatique)

QUALITÉ AIR (MQ-2) :
  ≥ 60% de la plage → ⚠️ ALERTE FUMÉE / GAZ
```

### Architecture matérielle

```
                    ┌────────────────────────────────────┐
                    │        ESP32 DevKit v1              │
                    │                                     │
  DHT22 ────────── GPIO4 (DATA)                          │
  MQ-2  ────────── GPIO34 (ADC)                          │
  LDR   ────────── GPIO35 (ADC)                          │
  LED Status ───── GPIO2 (OUTPUT)                        │
                    │     WiFi 802.11 b/g/n               │
                    └───────────────────────────────────┘
                           │ MQTT/WiFi
                           ▼
                    [Broker MQTT]
                           │
                           ▼
                    [Node-RED] ──→ [Dashboard web]
                           │
                           ▼
                    [InfluxDB] ──→ [Historique]
```

### Topic MQTT

```
Structure : "climasens/[groupe]/[mesure]"

Topics publiés par l'ESP32 :
  climasens/grpXX/data    ← JSON complet {temp, hum, air, lum, timestamp}
  climasens/grpXX/status  ← "online" / "offline"

Topics subscriber Node-RED :
  climasens/grpXX/+       ← Tous les messages du groupe
  climasens/grpXX/alerte  ← Alertes pour tableau de bord
```

### Dashboard requis

```
Le dashboard Node-RED doit comporter :
  ☐ Onglet "Temps Réel" :
      Gauge Température (0-60°C, couleurs zones)
      Gauge Humidité (0-100%, couleurs zones)
      Indicateur Qualité Air (texte coloré)
      Voyant LED Status (vert = OK, rouge = alerte)
  
  ☐ Onglet "Historique" :
      Graphe température sur 30 min (Chart multi-points)
      Graphe humidité sur 30 min
      Tableau des 10 dernières alertes
  
  ☐ Onglet "Alertes" :
      Notification visuelle + texte d'alerte horodatée
      Bouton "Acquitter" (effacer l'alerte)
```

---

## 📁 Livrables attendus

```
Rendu en fin de séance (ou J+2 pour complétion) :

FICHIERS OBLIGATOIRES :
  ☐ schema_climasens_grpXX.kicad_sch    (schéma KiCad)
  ☐ schema_climasens_grpXX.pdf           (export PDF)
  ☐ bom_climasens_grpXX.csv             (nomenclature)
  ☐ code_esp32_climasens.ino            (programme Arduino)
  ☐ flow_nodered_climasens.json         (export flow Node-RED)
  ☐ pv_mesure_climasens_grpXX.pdf       (procès-verbal)
  ☐ capture_dashboard.png               (screenshot dashboard)

FICHIERS BONUS (pour mention Très Bien) :
  ☐ pcb_climasens_grpXX.kicad_pcb       (PCB si réalisé)
  ☐ gerber_climasens_grpXX.zip          (fichiers fabrication)
  ☐ rapport_climasens_grpXX.pdf         (rapport complet)
```

---

## 📊 Grille d'évaluation projet

| Critère | Pondération | Indicateurs |
|---|---|---|
| **Schéma KiCad** | 20% | Correct, annoté, ERC 0 erreur, PDF propre |
| **BOM** | 10% | Tous composants, prix renseignés, format tableur |
| **Code Arduino** | 20% | Compile, multi-capteurs, MQTT, commenté |
| **Dashboard Node-RED** | 20% | Fonctionnel, tous les widgets, alertes actives |
| **PV de mesure** | 15% | ≥ 10 mesures, analyse des écarts, conclusions |
| **Documentation générale** | 15% | Mise en forme pro, schéma blocs, captures |
| **TOTAL** | **100%** | |

---

*Cahier des charges — BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S10*
*Projet CLIMASENS — Station IoT Industrielle*
