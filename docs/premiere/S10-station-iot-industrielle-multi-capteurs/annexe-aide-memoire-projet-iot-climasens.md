# 🗂️ AIDE-MÉMOIRE PROJET IoT CLIMASENS — À PLASTIFIER
## BOM · PV Mesure · Checklist Dossier · BAC PRO CIEL · E2 · 2ᵉ année S10

---

> *Conserver pendant toute la séance projet*

---

## 📋 Checklist livrables (à cocher)

```
SCHÉMA KICAD :
  ☐ Tous les composants présents
  ☐ Tous les nets nommés
  ☐ ERC : 0 erreur
  ☐ Exporté en PDF

BOM :
  ☐ Réf · Désignation · Valeur · Boîtier
  ☐ Quantité · Fournisseur · Prix unitaire
  ☐ Total calculé

CODE ARDUINO :
  ☐ Compile sans erreur
  ☐ DHT22 + MQ-2 lus
  ☐ JSON publié sur MQTT
  ☐ Alertes configurées
  ☐ Code commenté

DASHBOARD :
  ☐ Gauge temp + hum
  ☐ Alerte si seuil
  ☐ Graphe historique
  ☐ InfluxDB fonctionnel

PV MESURE :
  ☐ ≥ 10 mesures
  ☐ Écarts calculés
  ☐ Analyse rédigée

CAPTURES :
  ☐ Dashboard temps réel
  ☐ Graphe historique
  ☐ Test alerte
```

---

## 🔌 Câblage ESP32 — Rappel rapide

```
GPIO 4  → DHT22 DATA (+ R 10kΩ → 3V3)
GPIO 34 → MQ-2 AO (INPUT ONLY)
GPIO 35 → LDR (pont diviseur) (INPUT ONLY)
GPIO 2  → LED + R 220Ω → GND
3V3     → VCC DHT22, LDR
5V (USB)→ VCC MQ-2 (chauffage !)
GND     → Commun
```

---

## 🚨 Seuils d'alerte CLIMASENS

```
T° ≤ 5°C  → ALERTE FROID
T° ≥ 40°C → ALERTE CHALEUR
Hum ≥ 80% → ALERTE HUMIDITÉ ÉLEVÉE
Hum ≤ 20% → ALERTE HUMIDITÉ FAIBLE
Air ≥ 60% → ALERTE FUMÉE/GAZ
```

---

## 📨 Topics MQTT

```
climasens/grpXX/data    ← JSON {temp, hum, air, lum}
climasens/grpXX/status  ← "online" / "offline"
climasens/grpXX/alerte  ← Message texte alerte
```

---

## 🔵 Nœud function "Parser" — squelette

```javascript
var data = msg.payload;
var msgT = { payload: parseFloat(data.temperature) };
var msgH = { payload: parseInt(data.humidite) };
var msgA = { payload: parseInt(data.air) };
var msgI = { payload: data };
return [msgT, msgH, msgA, msgI];
// ⚠️ Configurer 4 outputs dans les propriétés du nœud
```

---

## 🔴 Format InfluxDB

```javascript
msg.payload = [{
  measurement: "sonde_climasens",
  tags: { groupe: "grpXX" },
  fields: {
    temperature: parseFloat(data.temperature),
    humidite: parseInt(data.humidite),
    air: parseInt(data.air)
  }
}];
```

---

## ⚠️ Pièges courants

```
❌ MQ-2 sur 3V3 → chauffage insuffisant → valeurs fausses
❌ DHT22 lu < 2s → erreur lecture → isnan() !
❌ analogSetAttenuation() oublié → ADC tronqué à 1V
❌ Client ID MQTT dupliqué → déconnexion
❌ Function 4 outputs mais return de 3 → InfluxDB vide
❌ PV rempli sans démarrer le système → incohérences
```

---

*Aide-Mémoire Projet CLIMASENS — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S10*
*Compétences C4.1 · C4.3 · S5.1-5.6 · C3.1*
