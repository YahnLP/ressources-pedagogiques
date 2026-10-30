# 🎤 GUIDE PRÉPARATION SOUTENANCE — S19 · 2ᵉ ANNÉE · E2
## Démo Maquette · Présentation · Questions Jury

---

> **Distribuer aux apprenants 1 semaine avant la soutenance**

---

## ⏱️ Les 20 minutes de ta soutenance

```
0 – 5 min   → Tu présentes (sans interruption)
5 – 12 min  → Tu démontres en live
12 – 18 min → Tu réponds aux questions du jury
18 – 20 min → Tu conclus ("ce que j'améliorerais")
```

---

## ✅ CHECKLIST — Ce qui doit fonctionner le jour J

### Maquette et matériel

```
☐ ESP32 flashé avec le code final (pas une version de test)
☐ Connexion WiFi au réseau de la salle vérifiée (SSID + password corrects)
☐ Broker MQTT accessible (tester la veille)
☐ Node-RED démarré avec les flows chargés
☐ InfluxDB démarré avec des données déjà présentes
☐ Dashboard http://localhost:1880/ui ouvert dans le navigateur
☐ Câble USB de secours (si redémarrage nécessaire)
☐ PC chargé à ≥ 80% (ou branché secteur)
```

### Dossier technique (physique ou PDF ouvert)

```
☐ Schéma KiCad exporté en PDF — PROPRE, annoté, ERC = 0 erreur
☐ BOM avec prix et fournisseurs
☐ Architecture du système (schéma blocs ASCII ou dessin)
☐ Topics MQTT utilisés (tableau)
☐ PV de métrologie complet (calculs + décision de conformité)
☐ Captures dashboard (au moins 3 screenshots)
☐ Code Arduino commenté imprimé (ou PDF ouvert)
```

---

## 🗣️ Structure de ta présentation (5 min)

### Modèle en 4 temps

```
TEMPS 1 — Introduction (30 secondes)
"Mon projet est [nom]. Il s'agit de [décrire en 2 phrases].
Il mesure [grandeurs] et les affiche sur [dashboard]."

TEMPS 2 — Architecture (2 min)
Montrer le schéma blocs ou pointer les composants sur la maquette :
→ "L'ESP32 lit le DHT22 sur GPIO 4 toutes les [X] secondes..."
→ "Il publie en MQTT sur le topic [topic] via le broker [broker]..."
→ "Node-RED reçoit et affiche sur le dashboard..."
→ "Les données sont stockées dans InfluxDB pour l'historique..."

TEMPS 3 — Point fort technique (1 min)
Choisir 1 chose dont tu es fier :
→ "Ce qui m'a le plus appris : [X]"
→ "La difficulté principale était [Y], que j'ai résolue en faisant [Z]"

TEMPS 4 — Résultat métrologie (30 secondes)
"J'ai validé mon capteur DHT22 avec 10 mesures de comparaison.
Le biais est de [X]°C, l'incertitude élargie de [U]°C.
Mon capteur est [conforme / non conforme] à la spécification ±0,5°C."
```

---

## 🖥️ Démonstrations live à préparer (12 min)

### Les 5 démos incontournables

```
DÉMO 1 — ESP32 connecté (obligatoire) :
  Ouvrir le moniteur série Arduino IDE
  → Montrer "WiFi connecté ! IP : 192.168.X.X"
  → Montrer les messages MQTT publiés en temps réel
  
DÉMO 2 — Dashboard en temps réel (obligatoire) :
  Ouvrir http://localhost:1880/ui dans le navigateur
  → Montrer les jauges qui se mettent à jour toutes les Xs
  → Montrer le graphe qui s'allonge
  
DÉMO 3 — Déclencher une alerte (si configurée) :
  Approcher une source de chaleur du DHT22 (ou modifier un seuil)
  → Montrer l'alerte apparaître sur le dashboard

DÉMO 4 — Historique InfluxDB (si configuré) :
  Ouvrir l'onglet "Historique" du dashboard
  → Montrer que les données des 30 dernières minutes sont présentes
  
DÉMO 5 — Document PV métrologie (obligatoire) :
  Ouvrir le PV
  → Montrer le tableau de mesures rempli
  → Pointer le résultat : "conforme" ou "non conforme" avec justification
```

---

## ❓ Questions types — Prépare tes réponses

```
Q : "Quelle est l'adresse IP de votre ESP32 ?"
R : "En mode Station, l'ESP32 obtient l'IP [X] par DHCP depuis le routeur.
    Elle est visible dans le moniteur série à chaque connexion."

Q : "Pourquoi MQTT et pas un simple WebServer ?"
R : "MQTT est plus adapté à l'IoT car il est asynchrone et léger.
    Avec un WebServer, il faudrait que le client 'tire' les données.
    Avec MQTT, l'ESP32 'pousse' les données dès qu'elles sont disponibles.
    Cela permet à plusieurs abonnés de recevoir simultanément."

Q : "Que se passe-t-il si le WiFi se coupe ?"
R : "Mon code contient une fonction reconnectMQTT() qui vérifie la connexion
    dans loop() et tente de se reconnecter automatiquement.
    Le système reprend seul sans intervention humaine."

Q : "Vos résultats de métrologie — le capteur est-il bon ?"
R : "Oui / Non. J'ai mesuré un biais de [X]°C et une incertitude de [U]°C.
    L'erreur totale (biais + incertitude) est de [Y]°C, ce qui est
    [inférieur / supérieur] à la spécification de ±0,5°C.
    Mon capteur est donc [conforme / non conforme]."

Q : "Que changeriez-vous dans une version 2 ?"
R : "J'ajouterais [X] parce que [raison technique précise].
    J'aurais aussi voulu [Y] mais par manque de temps [Z]."
```

---

## 💬 Vocabulaire professionnel à utiliser

```
✓ "J'ai configuré un broker MQTT Mosquitto sur [IP]"
✓ "Les données sont publiées sur le topic [topic] avec un QoS [0/1]"
✓ "Le plan de masse sur B.Cu est continu pour minimiser les boucles de courant"
✓ "Le biais mesuré est de [X]°C, l'incertitude élargie de [U]°C (k=2, 95%)"
✓ "La fiabilité du système sur 1 an est de [R]% d'après la loi exponentielle"

✗ "J'ai mis un truc pour recevoir les données" → Trop vague
✗ "C'est le bidule qui envoie des messages" → Inacceptable en soutenance
✗ "Je sais pas trop comment ça marche" → Dire plutôt : "Je pense que..."
```

---

## 🚫 Ce qui fait perdre des points

```
❌ Lire ses notes intégralement (montre qu'on n'a pas compris)
❌ Dire "ça marche pas" sans expliquer pourquoi ni ce qu'on a essayé
❌ Ne pas regarder le jury (parler à l'écran)
❌ S'excuser en permanence ("c'est pas très bien mais...")
❌ Répondre "je sais pas" sans essayer de déduire
❌ Dépasser 6 minutes de présentation sans avoir montré la démo
```

## ✅ Ce qui fait gagner des points

```
✓ Schéma blocs dessiné à la main prêt (aide à expliquer sans PC)
✓ Moniteur série ouvert AVANT la démo (gain de temps précieux)
✓ Vocabulaire technique naturel et précis
✓ Mentionner une vraie difficulté rencontrée et comment résolue
✓ Lier le PV métrologie à une décision concrète
✓ Proposer une amélioration non demandée
✓ "Je ne suis pas sûr, mais le principe est..." (honnêteté valorisée)
```

---

*Guide Préparation Soutenance — BAC PRO CIEL | E2 Systèmes Électroniques | 2ᵉ année S19*
*Distribuer 1 semaine avant la soutenance*
