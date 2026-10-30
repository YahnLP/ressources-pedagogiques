# 🖥️ CHECKLIST DÉMONSTRATION LIVE — S19 · 2ᵉ ANNÉE · E2
## Préparer la Maquette · Séquence de Démo · Auto-évaluation Technique

---

> **Nom** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Groupe** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Date de soutenance** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Heure de passage** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## ⏱️ J−1 : Préparer la démo (à faire la veille)

### Vérification du système complet

```
CODE ARDUINO ESP32 :
  ☐ La version finale du code compile sans erreur
  ☐ Le code lit correctement le DHT22 (pas de "nan" en Serial monitor)
  ☐ Le code lit correctement le MQ-2 (ADC analogique)
  ☐ Les données sont publiées toutes les 10s en JSON sur MQTT
  ☐ Les alertes se déclenchent si les seuils sont dépassés
  ☐ copy running → fichier .ino sauvegardé sur clé USB (backup)

NODE-RED :
  ☐ Node-RED démarre sans erreur (http://localhost:1880)
  ☐ Le flow MQTT → Node-RED fonctionne (messages dans debug)
  ☐ La jauge température affiche une valeur cohérente (20-25°C)
  ☐ La jauge humidité affiche une valeur cohérente (40-70%)
  ☐ Le graphe historique montre des données sur au moins 10 minutes
  ☐ Une alerte se déclenche si on met le doigt sur le DHT22 (T° monte)
  ☐ InfluxDB reçoit les données (vérifier dans l'interface web)
  ☐ Le flow est exporté en JSON (backup) : flow_climasens_final.json

DOSSIER TECHNIQUE :
  ☐ Schéma KiCad exporté en PDF propre
  ☐ BOM avec prix et fournisseurs
  ☐ Code Arduino commenté (format .pdf ou .ino)
  ☐ PV de métrologie signé (σ, biais, U calculés, décision conforme/non)
  ☐ Captures du dashboard (≥ 3 screenshots)
  ☐ Schéma d'architecture (ESP32 → MQTT → Node-RED → InfluxDB)
  ☐ Tout le dossier en PDF dans un classeur ou sur clé USB
```

---

## 🎤 Séquence de présentation (5 minutes chrono)

### Script type (à adapter)

```
INTRODUCTION (30 secondes) :
"Mon projet s'appelle CLIMASENS — c'est une station IoT de surveillance
environnementale. Elle mesure la température, l'humidité et la qualité de l'air,
et transmet ces données en temps réel vers un dashboard Node-RED."

ARCHITECTURE (1 minute 30) :
[Montrer le schéma d'architecture]
"L'ESP32 lit les capteurs toutes les 10 secondes.
Les données sont publiées via MQTT sur le broker [adresse].
Node-RED les reçoit, les affiche sur le dashboard et les stocke dans InfluxDB.
Si la température dépasse [seuil]°C, une alerte orange se déclenche."

PCB ET COMPOSANTS (1 minute) :
[Montrer le schéma KiCad ou la maquette]
"Le schéma électronique montre la connexion du DHT22 sur GPIO 4
avec sa résistance pull-up de 10kΩ. Le MQ-2 est alimenté en 5V
depuis l'USB — il ne peut pas fonctionner en 3,3V."

DÉMONSTRATION LIVE (2 minutes) :
→ Ouvrir le dashboard sur l'écran
→ Montrer la valeur de température en direct
→ Provoquer une variation (doigt sur le capteur)
→ Montrer l'historique qui se remplit
→ Provoquer une alerte si possible
→ Montrer une requête InfluxDB en temps réel

BILAN (30 secondes) :
"En résumé, le système répond aux fonctions FP1 à FP3 du cahier des charges.
Ce que j'améliorerais pour une version 2 : [une amélioration concrète]."
```

---

## 🎯 Les 5 démonstrations live incontournables

```
DÉMO 1 — Données en temps réel (obligatoire) :
  Montrer la jauge se mettre à jour toutes les 10 secondes
  Valeur attendue : T° = 20-25°C · Hum = 40-70%

DÉMO 2 — Provoquer une alerte (très impressionnant) :
  Mettre le doigt sur le DHT22 → T° monte → alerte orange/rouge
  Sur le dashboard : le voyant d'alerte change de couleur
  Dans Node-RED debug : message d'alerte visible

DÉMO 3 — Historique dans InfluxDB :
  Ouvrir l'interface InfluxDB (port 8086)
  Montrer les données enregistrées des 30 dernières minutes
  Ou : graphe "historique InfluxDB" dans le dashboard

DÉMO 4 — MQTT en temps réel :
  Ouvrir un terminal avec mosquitto_sub ou MQTT Explorer
  Montrer les messages qui arrivent toutes les 10 secondes
  Format JSON visible : {"temperature":23.4, "humidite":62, ...}

DÉMO 5 — Le PV de métrologie (document) :
  Ouvrir le PV signé
  Montrer le tableau de mesures et pointer le résultat :
  "Le biais est de +0,21°C et l'incertitude élargie de 0,22°C.
   Le pire cas est 0,43°C < 0,5°C → le capteur est conforme."
```

---

## ❓ Réponses préparées aux questions du jury

```
Q : "Que se passe-t-il si le WiFi est coupé ?"
R : "L'ESP32 tente de se reconnecter automatiquement (boucle de reconnexion
    dans le code). Le dashboard ne reçoit plus de données — la jauge reste
    sur la dernière valeur. Les données InfluxDB sont perdues pendant la coupure."

Q : "Pourquoi avoir choisi MQTT plutôt que HTTP direct ?"
R : "MQTT est plus adapté à l'IoT : plus léger (headers plus courts), la connexion
    est persistante, et le broker peut gérer plusieurs clients simultanément.
    HTTP nécessiterait de poller le serveur régulièrement."

Q : "Quel est le MTBF de votre système ?"
R : "Le DHT22 a un MTBF de 50 000 heures soit environ 5,7 ans.
    Avec l'ESP32 (100 000h) en série, le MTBFs ≈ 33 000h ≈ 3,8 ans."

Q : "Quelle est la principale limite CEM de votre maquette ?"
R : "La maquette est sur breadboard sans plan de masse. Les pistes longues
    du DHT22 et de la LDR peuvent capter des perturbations inductives.
    Pour un système de production, il faudrait un PCB avec plan de masse continu
    et des condensateurs de découplage au plus près de l'ESP32."

Q : "Votre capteur est-il conforme ?"
R : "Oui. Le PV de métrologie montre un biais de +0,21°C et une incertitude
    élargie U=0,22°C. Le pire cas est 0,43°C, inférieur à la spécification ±0,5°C."
```

---

## 📊 Auto-évaluation avant la soutenance

> Évalue-toi honnêtement — c'est pour cibler tes dernières révisions.

| Compétence | Confiant | Hésitant | À retravailler |
|---|---|---|---|
| Expliquer l'architecture ESP32→MQTT→Node-RED | ☐ | ☐ | ☐ |
| Montrer la démo live sans paniquer | ☐ | ☐ | ☐ |
| Expliquer le schéma KiCad | ☐ | ☐ | ☐ |
| Justifier le topic MQTT choisi | ☐ | ☐ | ☐ |
| Lire les résultats du PV métrologie | ☐ | ☐ | ☐ |
| Citer le MTBF du capteur principal | ☐ | ☐ | ☐ |
| Expliquer 1 violation CEM de la maquette | ☐ | ☐ | ☐ |
| Proposer 1 amélioration pour une v2 | ☐ | ☐ | ☐ |

---

## 💬 Ce qui fait la différence entre 12/20 et 17/20

```
À 12/20 : Le système fonctionne. La démo marche. Les réponses sont vagues.
  "J'ai mis un condensateur de découplage parce qu'il le faut."

À 17/20 : Le système fonctionne. La démo marche. Les réponses sont précises.
  "J'ai placé le condensateur 100nF à moins de 2mm des pins VCC/GND de l'ESP32
   parce qu'au-delà, l'inductance de la piste annule l'effet de filtrage HF."

La différence : l'apprenant qui COMPREND vs celui qui a REPRODUIT.
Deux questions du jury suffisent pour distinguer les deux.
```

---

*Checklist Démo Live + Préparation Soutenance — BAC PRO CIEL | E2 | 2ᵉ année S19*
*Document apprenant — À compléter la veille*
