# 📖 FICHE COURS – S14 ANNÉE 2 – E2
## Maintenance Corrective : Diagnostic de Pannes, Procédures de Réparation

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Appliquer la démarche DECA pour diagnostiquer une panne
- ✅ Identifier les 8 catégories de pannes sur un système IoT ESP32
- ✅ Choisir l'instrument adapté à chaque type de symptôme
- ✅ Rédiger une fiche de maintenance standardisée
- ✅ Valider la réparation par des tests mesurables

---

## 1️⃣ LES 3 NIVEAUX DE MAINTENANCE

> La maintenance est l'ensemble des actions permettant de maintenir ou de rétablir un bien dans un état spécifié. On distingue trois niveaux :

| **Niveau** | **Définition** | **Exemple IoT ESP32** |
|---|---|---|
| **Préventive** | Avant la panne — éviter qu'elle arrive | Vérification mensuelle des connexions, mise à jour firmware, nettoyage contacts |
| **Corrective** | Après la panne — la réparer | Diagnostic + remplacement composant + recompilation code |
| **Évolutive** | Après réparation — améliorer | Ajouter un WDT, remplacer le régulateur LDO par un buck converter, passer IP44 → IP65 |

> **En BAC PRO CIEL**, la maintenance corrective est la compétence centrale de S14. Mais une bonne réparation intègre toujours une réflexion évolutive : "Comment éviter que ça revienne ?"

---

## 2️⃣ LA DÉMARCHE DECA

$$\boxed{D \rightarrow E \rightarrow C \rightarrow A}$$

### D — Décrire le problème

> Recueillir TOUS les symptômes avant de mesurer quoi que ce soit. Un diagnostic raté commence souvent par une mesure faite trop tôt, au mauvais endroit.

```
Questions à se poser :
  - Quand est apparue la panne ? (date, heure, contexte)
  - Quel est exactement le symptôme ? (ce qu'on voit, entend, mesure)
  - Qu'est-ce qui fonctionnait avant ? Qu'est-ce qui a changé ?
  - La panne est-elle permanente, intermittente, ou sous condition ?
  - Quels sont les derniers travaux effectués sur le système ?
```

### E — Éliminer des hypothèses

> Dressez la liste de TOUTES les causes possibles, puis éliminez les plus improbables logiquement, sans mesure.

```
Exemple : ESP32 ne publie plus sur MQTT

Causes possibles :
  H1 : Wi-Fi déconnecté
  H2 : IP broker incorrecte
  H3 : Certificat révoqué (AWS IoT)
  H4 : Topic incorrect
  H5 : Code en deadlock
  H6 : Alimentation insuffisante → reset en boucle

Élimination logique :
  - Si la LED Wi-Fi est allumée → H1 éliminée
  - Si le log série montre "MQTT connected" → H2, H3 éliminées
  - Si les valeurs JSON sont visibles dans le log → H5 partiellement éliminée
  → Reste H4 (topic) → à vérifier
```

### C — Cibler la cause

> Appliquer la **méthode de dichotomie** : couper le chemin de défaut en deux à chaque étape.

![Chemin d'un message MQTT et diagnostic par dichotomie](images/chemin-message-mqtt.png)

### A — Agir et valider

> Réparer la cause identifiée, puis **tester que la réparation fonctionne** et que rien d'autre n'a été cassé (test de régression).

```
1. Appliquer la correction
2. Test de fonctionnement : le symptôme a-t-il disparu ?
3. Test de régression : les autres fonctions marchent-elles toujours ?
4. Documenter dans la fiche de maintenance
5. Réflexion évolutive : comment éviter cette panne à l'avenir ?
```

---


---

## 3️⃣ LES 8 CATÉGORIES DE PANNES IoT

### Catégorie 1 — Alimentation

| **Symptôme** | **Cause probable** | **Outil de diagnostic** |
|---|---|---|
| Reset en boucle / brownout | Tension < 3,3V minimum ESP32 | Multimètre sur VCC |
| Pas de démarrage | Fusible grillé / régulateur mort | Multimètre continuité + tension |
| Consommation excessive | Court-circuit partiel | Ampèremètre en série |
| Chauffe anormale | Régulateur LDO surchargé | Thermocouple / thermomètre IR |

```
Seuils ESP32 DevKit :
  VCC nominal : 5V ± 5%  (4,75 – 5,25V)
  VCC min opérationnel : ~3,6V (via pin 3V3 directement)
  Courant max : 250 mA en Wi-Fi actif + 80 mA idle
```

### Catégorie 2 — Signal numérique

| **Symptôme** | **Cause probable** | **Outil** |
|---|---|---|
| I2C : NACK systématique sur l'adresse | Pull-up manquante / composant absent | Oscillo / analyseur logique |
| SPI : données incorrectes ou nulles | Mode SPI incorrect (CPOL/CPHA) | Analyseur logique |
| UART : garbage data | Vitesse baud incorrecte | Moniteur série à différents bauds |
| Signal déformé, fronts lents | Pull-up trop haute / capacité excessive | Oscillo (voir front de montée) |

### Catégorie 3 — Réseau et Connectivité

| **Symptôme** | **Cause probable** | **Outil** |
|---|---|---|
| Wi-Fi : connexion échoue | SSID/password incorrects | Moniteur série |
| Wi-Fi : déconnexions fréquentes | Signal faible (RSSI < -80 dBm) | `WiFi.RSSI()` dans le code |
| MQTT : connexion refusée | Broker IP incorrecte / pare-feu | Ping, moniteur série |
| MQTT : messages non reçus | Topic sensible à la casse | Comparer topics publisher/subscriber |

### Catégorie 4 — Logicielle / Firmware

| **Symptôme** | **Cause probable** | **Outil** |
|---|---|---|
| Guru Meditation Error | Déréférencement pointeur NULL / stack overflow | Moniteur série (message d'erreur) |
| Watchdog Timer reset (WDT) | `loop()` bloqué > 5 secondes | Moniteur série + analyse code |
| `malloc()` échoue (retourne NULL) | Heap plein (memory leak) | `ESP.getFreeHeap()` dans le code |
| Données incorrectes | Conversion int/float incorrecte | Log des valeurs brutes avant conversion |

```cpp
// Diagnostics logiciels utiles en Arduino ESP32 :
Serial.println(ESP.getFreeHeap());        // Mémoire heap disponible
Serial.println(ESP.getCpuFreqMHz());     // Fréquence CPU
Serial.println(WiFi.RSSI());              // Force signal Wi-Fi
Serial.println(mqtt.state());             // Code erreur PubSubClient
```

### Catégorie 5 — Capteurs

| **Symptôme** | **Cause probable** | **Outil** |
|---|---|---|
| Valeurs constantes | Capteur figé / broche DATA court-circuit | Oscillo sur DATA |
| Valeurs `NaN` ou `-127` | Capteur non alimenté / DATA déconnecté | Multimètre continuité + VCC |
| Valeurs aberrantes (ex: 99°C) | Capteur en dehors de sa plage opérationnelle | Comparer avec thermomètre de référence |
| Lectures intermittentes | Contact défectueux / condensation | Inspection visuelle + flex du câble |

### Catégorie 6 — Communication Protocole

| **Symptôme** | **Cause probable** | **Outil** |
|---|---|---|
| MQTT : publish retourne `false` | Déconnecté du broker ou payload trop long | Moniteur série + `mqtt.connected()` |
| AWS IoT : `MQTT_CONNECT_UNAUTHORIZED` | Certificat révoqué / policy trop restrictive | Console AWS → certificats |
| Données corrompues en JSON | Concaténation de chaînes incorrecte | Log le payload avant publish |
| Timeout fréquents | Réseau congestionné / QoS 2 trop lourd | Passer QoS 0 pour test |

### Catégorie 7 — Mécanique et Environnement

| **Symptôme** | **Cause probable** | **Outil** |
|---|---|---|
| Panne intermittente liée aux vibrations | Soudure froide / connecteur Dupont mal enfoncé | Inspection + flex cable à la main |
| Panne par temps humide | Condensation sur PCB / oxydation contact | Inspection visuelle + loupe |
| Composant grillé (brûlé) | Inversion polarité / surtension | Vue + odorat + multimètre continuité |
| Boîtier déformé | Surchauffe (PLA > 55°C) | Mesure thermique |

### Catégorie 8 — Sécurité / Authentification

| **Symptôme** | **Cause probable** | **Outil** |
|---|---|---|
| TLS : handshake timeout | Horloge système désynchronisée (NTP requis) | `time(nullptr)` dans le code |
| AWS IoT : connexion refusée | Policy IoT trop restrictive | Console AWS → Surveiller → MQTT |
| Hash de certificat incorrect | CA certificate incorrect (AmazonRootCA1 vs AmazonRootCA3) | Vérifier l'empreinte du certificat |

---

## 4️⃣ INSTRUMENTS DE DIAGNOSTIC : LEQUEL CHOISIR ?

```
Problème d'alimentation (tension, courant) → MULTIMÈTRE
Problème de signal analogique (forme d'onde, niveau, fréquence) → OSCILLOSCOPE
Problème de protocole numérique (I2C, SPI, UART) → ANALYSEUR LOGIQUE
Problème logiciel / réseau / connexion → MONITEUR SÉRIE + logs
Problème température → THERMOMÈTRE IR / thermocouple
Problème de continuité (fil coupé, soudure) → MULTIMÈTRE (mode bip)
Problème AWS IoT / certificats → CONSOLE AWS CLOUDWATCH
```

> **Règle d'or :** toujours commencer par ce qui ne nécessite pas d'instrument — le **moniteur série** et l'**inspection visuelle**. 80% des pannes IoT se diagnostiquent sans toucher un instrument.

---

## 5️⃣ LA FICHE DE MAINTENANCE

### Pourquoi documenter ?

> Un technicien passe souvent plus de temps à diagnostiquer une panne déjà résolue 3 mois plus tôt par un collègue qu'à en trouver une nouvelle. La fiche de maintenance transforme l'expérience individuelle en savoir collectif permanent.

### Structure standardisée

```
┌─────────────────────────────────────────────────────────────────────┐
│  FICHE DE MAINTENANCE CORRECTIVE                                    │
├─────────────────────────────────────────────────────────────────────┤
│  Équipement : esp32-station-météo-01    Date : 2026-03-15           │
│  Intervenant : Alice DUPONT             Durée intervention : 45 min │
├─────────────────────────────────────────────────────────────────────┤
│  1. SYMPTÔME(S)                                                     │
│  L'ESP32 ne publie plus sur AWS IoT depuis 14h00. LED Wi-Fi OK.    │
│  Moniteur série : "Erreur MQTT : -8" en boucle.                    │
├─────────────────────────────────────────────────────────────────────┤
│  2. DÉMARCHE DE DIAGNOSTIC                                          │
│  Étape 1 : Wi-Fi OK (LED + log "WiFi OK → 192.168.1.42")           │
│  Étape 2 : Ping broker OK → broker joignable                       │
│  Étape 3 : show crypto ipsec → certificat AWS désactivé ? Non.     │
│  Étape 4 : Console AWS → Surveiller → MQTT test → log erreur :     │
│           "Policy doesn't allow iot:Publish on this resource"       │
├─────────────────────────────────────────────────────────────────────┤
│  3. CAUSE IDENTIFIÉE                                                │
│  La Policy IoT AWS a été modifiée par erreur (suppression de        │
│  l'action iot:Publish lors d'une mise à jour de sécurité).          │
├─────────────────────────────────────────────────────────────────────┤
│  4. ACTION CORRECTIVE                                               │
│  Ajout de "iot:Publish" dans la Policy IoT via console AWS.         │
├─────────────────────────────────────────────────────────────────────┤
│  5. VALIDATION                                                      │
│  Messages visibles dans console AWS MQTT Test : ✅                  │
│  CloudWatch : nouvelles métriques température : ✅                  │
│  Durée sans incident depuis : > 24h ✅                               │
├─────────────────────────────────────────────────────────────────────┤
│  6. AMÉLIORATION PRÉVENTIVE                                         │
│  Créer une alarme CloudWatch sur l'absence de métriques > 15 min.  │
│  Ajouter politique de gestion des changements (validation avant     │
│  toute modification de Policy IoT en production).                   │
└─────────────────────────────────────────────────────────────────────┘
```

---


---

## 6️⃣ CODES D'ERREUR PUBSUBCLIENT — RÉFÉRENCE RAPIDE

| **Code** | **Constante** | **Signification** | **Première action** |
|---|---|---|---|
| **-4** | MQTT_CONNECT_BAD_PROTOCOL | Version MQTT rejetée | Vérifier compatibilité bibliothèque/broker |
| **-3** | MQTT_CONNECT_DISCONNECTED | Déconnecté du broker | Vérifier connectivité réseau |
| **-2** | MQTT_CONNECT_FAILED | Connexion TCP impossible | Vérifier IP broker + ping |
| **-1** | MQTT_DISCONNECTED | Client déconnecté (normal avant connect) | Appeler connect() |
| **0** | MQTT_CONNECTED | Connecté ✅ | — |
| **1** | MQTT_CONNECT_BAD_PROTOCOL | — | — |
| **5** | MQTT_CONNECT_UNAUTHORIZED | Auth refusée | Vérifier certificats ou user/pass |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais appliquer DECA : Décrire (symptôme) → Éliminer → Cibler → Agir
- [ ] Je distingue symptôme et cause (ex: "ne publie pas" ≠ "IP incorrecte")
- [ ] Je sais choisir l'instrument adapté à chaque catégorie de panne
- [ ] Je sais lire un code d'erreur PubSubClient et en déduire la nature du problème
- [ ] Je sais rédiger une fiche de maintenance avec les 6 champs obligatoires
- [ ] Je pense à la validation après réparation ET à la réflexion préventive

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **Maintenance corrective** | Actions effectuées après une panne pour rétablir le fonctionnement |
| **Démarche DECA** | Décrire, Éliminer, Cibler, Agir — méthode structurée de diagnostic |
| **Cause racine** | Cause première d'une panne — pas le symptôme visible mais l'origine |
| **Dichotomie** | Méthode consistant à couper le chemin de défaut en deux à chaque test |
| **Brownout** | Réinitialisation de l'ESP32 due à une tension d'alimentation insuffisante |
| **Guru Meditation Error** | Message d'erreur critique ESP32 (panic / crash noyau) |
| **WDT** | Watchdog Timer — chien de garde qui resette l'ESP32 si `loop()` est bloquée |
| **Soudure froide** | Soudure électriquement défectueuse (contact résistif ou intermittent) |
| **RSSI** | Received Signal Strength Indicator — force du signal Wi-Fi en dBm |
| **Fiche de maintenance** | Document traçant symptôme, diagnostic, cause, correction et validation |
| **Test de régression** | Vérification que la réparation n'a pas cassé ce qui fonctionnait avant |
| **Heap** | Mémoire dynamique de l'ESP32 (allouée par `malloc` / `new`) |

---

## 📌 POINTS-CLÉS À RETENIR

1. **80% des pannes IoT** sont logicielles ou de configuration — commencer par le moniteur série
2. **DECA** : Décrire → Éliminer → Cibler → Agir — ne jamais mesurer avant d'avoir décrit
3. Distinguer **symptôme** (ce qu'on voit) de **cause** (pourquoi ça arrive)
4. **Dichotomie** : couper le chemin de défaut en deux → O(log n) mesures pour trouver
5. `mqtt.state()` = premier code à lire quand MQTT ne fonctionne pas
6. `ESP.getFreeHeap()` = surveiller si l'ESP32 commence à manquer de mémoire
7. **Fiche de maintenance** = traçabilité obligatoire — symptôme + cause + correction + validation
8. Après réparation : toujours faire un **test de validation** puis un **test de régression**

---

**Document – BAC PRO CIEL – A2 – E2/U21 – Version 1.0 – 2026**
