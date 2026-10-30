# 🔩 FICHE TECHNIQUE — CAPTEUR DHT11
## Document de référence apprenant · Version simplifiée

---

> *BAC PRO CIEL | Module E2 | S16*
> *À conserver dans le classeur et le portfolio — pièce justificative du choix technique*

---

## 📦 Identification du composant

| Champ | Valeur |
|---|---|
| **Référence** | DHT11 |
| **Fabricant** | AOSONG Electronics |
| **Type** | Capteur numérique de température et d'humidité |
| **Boîtier disponible** | TO-92 (4 broches) ou Module breakout (3 broches) |
| **Prix indicatif** | 1,50 € à 3,00 € HT (module breakout) |

---

## 📐 Caractéristiques électriques

| Paramètre | Valeur |
|---|---|
| **Tension d'alimentation (VCC)** | 3,3 V à 5,5 V |
| **Courant de fonctionnement** | 1 mA (mesure) — 0,15 mA (veille) |
| **Interface de communication** | Numérique série propriétaire (1-Wire simplifié) |
| **Longueur de câble max** | 20 m (avec résistance pull-up adaptée) |

---

## 🌡️ Caractéristiques de mesure

### Température

| Paramètre | Valeur |
|---|---|
| **Plage de mesure** | 0°C à 50°C |
| **Précision** | ±2°C |
| **Résolution** | 1°C (données entières) |
| **Temps de réponse** | 30 secondes (inertie thermique) |

### Humidité relative

| Paramètre | Valeur |
|---|---|
| **Plage de mesure** | 20% HR à 90% HR |
| **Précision** | ±5% HR |
| **Résolution** | 1% HR (données entières) |

> ⚠️ **Fréquence de lecture maximale** : **1 lecture toutes les 2 secondes**.
> Au-delà, le capteur retourne des valeurs invalides (NaN).

---

## 🔌 Description des broches

### Boîtier TO-92 nu (4 broches — vue de face)

![DHT11 : face avant et numérotation des broches](images/dht11-brochage.png)

| N° Broche | Nom | Fonction | Connexion Arduino |
|---|---|---|---|
| 1 | **VCC** | Alimentation + | 5V Arduino |
| 2 | **DATA** | Signal données (bidirectionnel) | Broche numérique + R pull-up 10kΩ vers VCC |
| 3 | **NC** | Non connectée | Laisser libre |
| 4 | **GND** | Masse | GND Arduino |

### Module breakout (3 broches)

| Broche | Fonction | Connexion Arduino |
|---|---|---|
| **VCC (+ ou S)** | Alimentation | 5V Arduino |
| **DATA (out)** | Signal données | Broche numérique (résistance déjà intégrée) |
| **GND (-)** | Masse | GND Arduino |

---

## ⚡ Circuit de câblage recommandé (boîtier nu)

![Câblage du DHT11 avec résistance pull-up de 10 kΩ](images/dht11-cablage.png)

**Valeur de la résistance pull-up selon la longueur du câble :**

| Longueur câble | Résistance pull-up |
|---|---|
| < 1 m | 10 kΩ (standard) |
| 1 m à 5 m | 4,7 kΩ |
| 5 m à 20 m | 2,2 kΩ |

---

## 💻 Code Arduino minimal

```cpp
#include <DHT.h>

#define BROCHE_DHT 2
#define TYPE_DHT   DHT11

DHT dht(BROCHE_DHT, TYPE_DHT);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  delay(2000);  // Attente obligatoire

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Erreur lecture !");
    return;
  }

  Serial.print("T=");  Serial.print(t); Serial.print("°C  ");
  Serial.print("HR="); Serial.print(h); Serial.println("%");
}
```

---

## 🔄 Comparaison avec le DHT22

| Critère | DHT11 | DHT22 |
|---|---|---|
| Prix | ~1,50 € | ~3,50 € |
| Plage T° | 0 à 50°C | −40 à 80°C |
| Précision T° | ±2°C | **±0,5°C** |
| Plage HR | 20 à 90% | 0 à 100% |
| Précision HR | ±5% | **±2%** |
| Résolution | 1°C / 1% | **0,1°C / 0,1%** |
| Fréquence lecture min | 1 mesure / 2s | 1 mesure / 2s |
| Code Arduino | Identique (changer `DHT11` → `DHT22`) | — |

> 💡 Pour un projet industriel ou médical exigeant une meilleure précision, **préférer le DHT22**.
> Pour un projet éducatif ou domotique simple, le **DHT11 suffit**.

---

## 🐛 Problèmes fréquents et solutions

| Problème | Cause | Solution |
|---|---|---|
| `Erreur lecture !` en boucle | Résistance pull-up manquante | Ajouter R 10kΩ entre VCC et DATA |
| Valeurs `0 / 0` constantes | Mauvaise broche dans le code | Vérifier `BROCHE_DHT` correspond au câblage réel |
| Valeurs aberrantes (ex : 255°C) | Lecture trop fréquente | Respecter `delay(2000)` minimum entre lectures |
| Bibliothèque introuvable | Dépendance manquante | Installer aussi `Adafruit Unified Sensor` |
| Valeurs qui ne changent pas | Capteur défectueux | Tester avec un autre DHT11 |

---

*Fiche Technique DHT11 — BAC PRO CIEL | Module E2 | S16*
*Document à intégrer dans la BOM et le dossier technique Portfolio E5*
