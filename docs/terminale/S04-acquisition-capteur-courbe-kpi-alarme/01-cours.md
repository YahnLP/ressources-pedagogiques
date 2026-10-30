# 📖 FICHE COURS – S4 ANNÉE 3 – E2
## Acquisition Capteur → Courbe → KPI → Alarme Embarquée

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Calculer des KPI embarqués (moyenne mobile, min/max glissants, tendance)
- ✅ Implémenter des seuils d'alerte avec hystérésis et anti-rebond
- ✅ Générer une courbe de tendance depuis les données acquises
- ✅ Rédiger une fiche de mise en service complète et signée

---

## 1️⃣ DU CLOUD À L'EMBARQUÉ : POURQUOI ?

### L'architecture A2 et ses limites

> En A2, la logique d'alarme était dans le cloud (règle CloudWatch). Si le réseau Wi-Fi est coupé pendant 30 minutes, aucune alarme n'est envoyée — même si la machine dépasse son seuil critique.

### L'intelligence embarquée : décision locale

```
Architecture A3 :

 [Capteur] ──► [ESP32]
                  │
                  ├── Calcul KPI (moyenne, tendance...)
                  ├── Comparaison aux seuils
                  ├── Si alarme → LED rouge / buzzer / relais (LOCAL)
                  │                    ↓ immédiat, sans réseau
                  └── Si réseau OK → publication JSON sur MQTT/AWS
                                         ↓ dashboard CloudWatch

Avantage : réaction < 1 seconde, même sans Wi-Fi
```

---

## 2️⃣ LES KPI EMBARQUÉS

### Définition

> Un **KPI** (Key Performance Indicator) est un indicateur chiffré qui résume en une valeur l'état d'un système. En IoT embarqué, les KPI sont calculés en temps réel dans le firmware.

### KPI 1 — Moyenne Mobile (lissage du bruit)

> La moyenne mobile calcule la **moyenne des N dernières mesures**. Elle élimine les pics ponctuels (bruit électronique, vibration passagère) et donne une valeur représentative.

$$\bar{x}_{mobile}(t) = \frac{1}{N} \sum_{i=0}^{N-1} x_{t-i}$$

```cpp
// Implémentation : buffer circulaire de taille N
const int N = 10;              // Taille de la fenêtre
float buffer[N] = {0};
int   index = 0;
bool  buffer_plein = false;

float ajouterEtMoyenner(float nouvelle_valeur) {
  buffer[index] = nouvelle_valeur;
  index = (index + 1) % N;       // Avance circulairement
  if (index == 0) buffer_plein = true;

  if (!buffer_plein) return nouvelle_valeur; // Pas encore N valeurs

  float somme = 0;
  for (int i = 0; i < N; i++) somme += buffer[i];
  return somme / N;
}
```

**Effets de la taille N :**

| **N petit (ex: 3)** | **N grand (ex: 20)** |
|---|---|
| Réactif aux changements rapides | Très lissé, insensible au bruit |
| Peut encore être bruité | Répond lentement aux vraies variations |
| Bon pour détections rapides | Bon pour tendances lentes |

---

### KPI 2 — Min et Max Glissants

```cpp
const int FENETRE = 60;   // Nombre de mesures (ex: 60 × 5s = 5 min)
float buf_minmax[FENETRE];
int   idx_mm = 0;

void majMinMax(float val) {
  buf_minmax[idx_mm] = val;
  idx_mm = (idx_mm + 1) % FENETRE;
}

float calculerMin() {
  float mini = buf_minmax[0];
  for (int i = 1; i < FENETRE; i++) if (buf_minmax[i] < mini) mini = buf_minmax[i];
  return mini;
}

float calculerMax() {
  float maxi = buf_minmax[0];
  for (int i = 1; i < FENETRE; i++) if (buf_minmax[i] > maxi) maxi = buf_minmax[i];
  return maxi;
}

float calculerAmplitude() { return calculerMax() - calculerMin(); }
```

**Usage :** Si l'amplitude (max−min) dépasse un seuil, c'est signe d'instabilité ou de vibration anormale.

---

### KPI 3 — Taux d'Alarme

> Sur les N dernières minutes, quelle proportion du temps l'équipement était-il en alarme ?

```cpp
unsigned int nb_alarmes_fenetre = 0;   // Compteur glissant
unsigned int nb_mesures_fenetre = 0;

float tauxAlarme() {
  if (nb_mesures_fenetre == 0) return 0;
  return 100.0 * nb_alarmes_fenetre / nb_mesures_fenetre;  // en %
}
```

---

### KPI 4 — Tendance (pente)

> La tendance indique si la grandeur **monte, descend ou reste stable** sur une fenêtre temporelle.

$$\text{tendance} = \frac{x_{dernier} - x_{premier}}{(N-1) \times \Delta t} \quad [\text{unité/heure}]$$

```cpp
float calculerTendance(float* buf, int taille, float dt_secondes) {
  // buf[0] = la plus ancienne valeur, buf[taille-1] = la plus récente
  float pente = (buf[taille-1] - buf[0]) / ((taille-1) * dt_secondes / 3600.0);
  return pente;   // en [unité/heure]
}
// pente > +0.5 °C/h → température monte → alarme prédictive possible
// pente ≈ 0 → stable
// pente < -0.5 °C/h → température descend
```

---

## 3️⃣ SEUILS D'ALERTE : PROBLÈMES ET SOLUTIONS

### Le problème des seuils simples : le battement

```
Seuil = 35°C, sans hystérésis :

Mesure : 34,9 / 35,1 / 34,8 / 35,2 / 34,9 / 35,0 / 35,1 / 34,7

Alarme :  OFF  / ON  / OFF / ON  / OFF / OFF / ON  / OFF
         ← Battement ON/OFF permanent →
```

> Ce comportement génère des fausses alarmes en rafale. Il est inacceptable en production (usure des relais, notifications intempestives, perte de confiance dans le système).

---

### Solution 1 — L'Hystérésis

> L'hystérésis crée une **bande morte** : l'alarme s'active à `SEUIL_HAUT` et ne se désactive qu'à `SEUIL_BAS` (avec `SEUIL_BAS < SEUIL_HAUT`).

```
SEUIL_HAUT = 35°C   (activation alarme)
SEUIL_BAS  = 33°C   (désactivation alarme)
Hystérésis = 2°C

Mesure : 33,5 / 34,2 / 35,1 / 36,0 / 34,8 / 33,9 / 32,5

Alarme :  OFF / OFF / ON  / ON  / ON  / ON  / OFF
          ← L'alarme reste ON jusqu'à 32,5 < 33°C →
```

```cpp
const float SEUIL_HAUT = 35.0;    // Activation alarme
const float SEUIL_BAS  = 33.0;    // Désactivation alarme (hystérésis 2°C)
bool alarme_active = false;

void mettreAJourAlarme(float valeur) {
  if (!alarme_active && valeur >= SEUIL_HAUT) {
    alarme_active = true;
    Serial.println("ALARME ACTIVÉE : " + String(valeur) + "°C");
  } else if (alarme_active && valeur <= SEUIL_BAS) {
    alarme_active = false;
    Serial.println("Alarme désactivée : " + String(valeur) + "°C");
  }
}
```

---

### Solution 2 — L'Anti-rebond Temporel

> L'alarme n'est confirmée que si le dépassement dure plus de `DELAI_MS` millisecondes en continu. Cela filtre les pics fugaces (bruit, vibration de 50ms).

```cpp
const unsigned long DELAI_CONFIRMATION_MS = 5000;  // 5 secondes
static unsigned long debut_depassement = 0;
static bool          en_depassement    = false;
bool                 alarme_confirmee  = false;

void antiRebond(float valeur) {
  if (valeur >= SEUIL_HAUT) {
    if (!en_depassement) {
      debut_depassement = millis();
      en_depassement = true;
    } else if (millis() - debut_depassement >= DELAI_CONFIRMATION_MS) {
      alarme_confirmee = true;   // Confirmé après 5 secondes
    }
  } else {
    en_depassement = false;
    if (valeur <= SEUIL_BAS) alarme_confirmee = false;  // + hystérésis
  }
}
```

> **⚠️ Ne jamais utiliser `delay()` pour l'anti-rebond** — cela bloque tout le firmware. Toujours utiliser `millis()`.

---

### Les 3 niveaux d'alarme

> En supervision industrielle, on distingue généralement 3 niveaux croissants :

```
Niveau 1 : NORMAL    → Valeur dans la plage verte
           Action : Aucune

Niveau 2 : WARNING   → Seuil orange dépassé
           Action : LED orange, log, notification basse priorité

Niveau 3 : CRITICAL  → Seuil rouge dépassé
           Action : LED rouge + buzzer, arrêt préventif, notification urgente
```

```cpp
// Exemple pour température :
const float T_WARNING  = 32.0;    // °C — surveillance renforcée
const float T_CRITICAL = 38.0;    // °C — arrêt préventif
const float T_HYST     = 1.5;     // °C — hystérésis commune

typedef enum { NORMAL, WARNING, CRITICAL } NiveauAlarme;
NiveauAlarme niveauCourant = NORMAL;

NiveauAlarme evaluerNiveau(float temp) {
  switch (niveauCourant) {
    case NORMAL:
      if (temp >= T_CRITICAL)     return CRITICAL;
      if (temp >= T_WARNING)      return WARNING;
      return NORMAL;
    case WARNING:
      if (temp >= T_CRITICAL)     return CRITICAL;
      if (temp < T_WARNING - T_HYST) return NORMAL;
      return WARNING;
    case CRITICAL:
      if (temp < T_CRITICAL - T_HYST) return WARNING;
      return CRITICAL;
  }
  return NORMAL;
}
```

---

![Alarme avec hystérésis : seuil haut 30 °C, seuil bas 28 °C, plus de clignotement autour du seuil.](images/hysteresis-alerte.png)

---

## 4️⃣ COURBE DE TENDANCE

### Stocker les données pour la courbe

```cpp
// Buffer horodaté pour la courbe
struct DataPoint {
  unsigned long timestamp_s;   // secondes depuis démarrage
  float valeur;
  float moyenne_mobile;
  NiveauAlarme alarme;
};

const int TAILLE_HISTORIQUE = 120;  // 10 min × 12 points/min
DataPoint historique[TAILLE_HISTORIQUE];
int idx_hist = 0;

void enregistrerPoint(float valeur, float moy_mobile, NiveauAlarme alarme) {
  historique[idx_hist] = {millis()/1000, valeur, moy_mobile, alarme};
  idx_hist = (idx_hist + 1) % TAILLE_HISTORIQUE;
}
```

### Publication JSON enrichie pour dashboard

```json
{
  "device": "agro-serre-01",
  "ts": 1710000000,
  "temp_raw": 34.2,
  "temp_moy5": 33.8,
  "temp_min10": 31.5,
  "temp_max10": 34.9,
  "tendance_ch": 1.8,
  "taux_alarme_pct": 12.5,
  "alarme": "WARNING",
  "uptime_s": 3620
}
```

---

## 5️⃣ FICHE DE MISE EN SERVICE (MES)

### Qu'est-ce qu'une fiche MES ?

> La **fiche de mise en service** (MES, aussi appelée "fiche de recette" ou "PV de mise en service") est le document officiel remis au client attestant que :
> 1. Le système a été **installé** selon les spécifications
> 2. Il a été **configuré** avec les paramètres définis
> 3. Il a été **testé** avec résultats mesurables
> 4. Il est **remis opérationnel** au client

> C'est le document qui **transfère la responsabilité** du prestataire au client. Après signature, le client atteste avoir reçu un système fonctionnel.

### Structure d'une fiche MES

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  FICHE DE MISE EN SERVICE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. IDENTIFICATION
   Référence MES   : MES-2026-AGRO-001
   Client          : Coopérative AGROSMART – M. LEROUX
   Site            : Serre n°3 – Zone Tomates
   Date            : 2026-03-22
   Intervenant(s)  : A. DUPONT, B. MARTIN — CFA [Ville]

2. MATÉRIELS INSTALLÉS
   Réf.  │ Désignation          │ N° Série     │ Firmware
   ──────┼──────────────────────┼──────────────┼──────────────
   U1    │ ESP32 DevKit v1      │ ESP-2026-043 │ v2.1.0
   U2    │ DHT22 Temp+Hum       │ —            │ —
   U3    │ LED d'alarme Ø5mm    │ —            │ —

3. PARAMÈTRES CONFIGURÉS
   SSID Wi-Fi           : AGRO_PRO_WIFI [réseau interne]
   Broker MQTT          : AWS IoT Core eu-west-1
   Topic publication    : agro/serre3/capteurs
   Fréquence pub.       : 10 secondes
   T° seuil WARNING     : 32°C (hystérésis 1,5°C)
   T° seuil CRITICAL    : 38°C (hystérésis 1,5°C)
   Anti-rebond alarme   : 30 secondes
   Moyenne mobile       : N = 6 points (1 min)
   Notification SMS     : +33 6 XX XX XX XX (M. LEROUX)

4. TESTS DE VALIDATION
   ┌───────────────────────────────────────────────────────────┐
   │ Test TC-001 : Connexion Wi-Fi et publication MQTT        │
   │ Résultat : Premier message reçu en 8,3 s    → ✅ PASS   │
   ├───────────────────────────────────────────────────────────┤
   │ Test TC-002 : Lecture capteur DHT22                       │
   │ T° = 24,3°C / HR = 58% — cohérent avec sonde de réf.    │
   │                                                  → ✅ PASS│
   ├───────────────────────────────────────────────────────────┤
   │ Test TC-003 : Déclenchement alarme WARNING (T° simulée)  │
   │ Résultat : LED orange + SMS reçu en 38s     → ✅ PASS   │
   ├───────────────────────────────────────────────────────────┤
   │ Test TC-004 : Dashboard CloudWatch en temps réel         │
   │ Résultat : Courbe visible, KPI affichés      → ✅ PASS  │
   ├───────────────────────────────────────────────────────────┤
   │ Test TC-005 : Fonctionnement hors réseau                 │
   │ Résultat : LED d'alarme locale active          → ✅ PASS │
   └───────────────────────────────────────────────────────────┘

5. OBSERVATIONS ET RÉSERVES
   Aucune réserve.
   Prochaine vérification recommandée : dans 6 mois.

6. DÉCLARATION DE MISE EN SERVICE
   L'équipement décrit ci-dessus est déclaré :
   ☑ OPÉRATIONNEL — conforme aux spécifications définies

7. SIGNATURES
   Installateur : ___________  Date : __________
   Client       : ___________  Date : __________
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---


---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais implémenter un buffer circulaire pour la moyenne mobile
- [ ] Je comprends pourquoi le flag `buffer_plein` est nécessaire
- [ ] Je sais configurer l'hystérésis (SEUIL_HAUT ≠ SEUIL_BAS)
- [ ] Je sais utiliser `millis()` pour l'anti-rebond (pas `delay()`)
- [ ] Je sais calculer la tendance en unité/heure depuis un buffer
- [ ] Je connais les 3 niveaux d'alarme (NORMAL / WARNING / CRITICAL)
- [ ] Je sais rédiger une fiche MES avec les 7 sections obligatoires
- [ ] Je sais que la fiche MES transfère la responsabilité au client

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **KPI** | Key Performance Indicator — indicateur chiffré résumant l'état d'un système |
| **Moyenne mobile** | Moyenne des N dernières mesures — lisse le bruit de mesure |
| **Buffer circulaire** | Tableau de taille fixe dont les données sont écrasées cycliquement |
| **Hystérésis** | Bande morte entre le seuil d'activation et de désactivation d'une alarme |
| **Anti-rebond** | Confirmation d'un état après un délai pour filtrer les transitoires |
| **Tendance** | Pente de la courbe sur une fenêtre temporelle (unité/heure) |
| **Battement** | Oscillation rapide ON/OFF d'une alarme autour du seuil — à éviter |
| **millis()** | Fonction Arduino retournant le temps écoulé en ms — base du timing non-bloquant |
| **Fiche MES** | Fiche de Mise en Service — document certifiant l'installation et les tests |
| **SCADA** | Supervisory Control And Data Acquisition — système de supervision industrielle |

---

## 📌 POINTS-CLÉS À RETENIR

1. **Intelligence embarquée** = alarmes locales sans dépendre du réseau → meilleure résilience
2. **Buffer circulaire** = structure de données fondamentale pour les KPI glissants
3. **Jamais `delay()`** pour l'anti-rebond → utiliser `millis() - t_debut >= DELAI`
4. **Hystérésis** = SEUIL_HAUT pour activer, SEUIL_BAS pour désactiver — **toujours 2 seuils**
5. **Tendance** = (dernière − première valeur) / (durée en heures) → unité/heure
6. **Fiche MES** = 7 sections, test de validation obligatoire, **double signature** client + installateur
7. La fiche MES est le document qui **transfère la responsabilité** — sans elle, c'est "non livré"

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Version 1.0 – 2026**
