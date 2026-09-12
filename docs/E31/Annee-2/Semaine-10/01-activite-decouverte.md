# 🎲 ACTIVITÉ DÉCOUVERTE – S10 ANNÉE 2 – E31
## « La Panne Silencieuse » : Pourquoi Superviser Activement le Réseau ?

---

## 🎯 OBJECTIFS

- ✅ Faire émerger le besoin de **détection proactive** des pannes (vs réactive)
- ✅ Comprendre la différence entre **supervision passive** (attendre les logs) et **active** (tester régulièrement)
- ✅ Poser la question des **seuils d'alerte** : WARNING vs CRITICAL
- ✅ Faire formuler les besoins d'un système de supervision : quoi superviser, comment alerter

---

## ⏱️ DURÉE : 30 min

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur pose la question d'accroche :**

> *"En S9, on a vu SNMP et Syslog — les équipements envoient des messages quand quelque chose se passe. Mais s'ils ne savent pas qu'ils ont un problème ? Et si le problème n'est pas une panne totale, mais une dégradation progressive ?"*

---

## 🏥 PHASE 1 – Le Scénario de l'Hôpital (10 min)

**Le formateur décrit la situation :**

> *"Imaginez un hôpital. La salle de soins intensifs est reliée au serveur d'imagerie médicale par un réseau IP. Un lundi matin, le scanner IRM ne répond plus. Les infirmières pensent que le scanner est en panne — elles appellent le fabricant. 4 heures plus tard, l'ingénieur du fabricant arrive et constate... que c'est un câble réseau mal branché qui s'est desserré progressivement. Le scanner était parfait, mais il n'avait plus de réseau depuis 3 heures."*

**Questions au groupe :**

| **Question** | **Réponse attendue** |
|---|---|
| "Les équipements réseau ont-ils envoyé une alerte quand le câble s'est desserré ?" | Non — un câble qui se desserre ne génère pas de log automatique |
| "Comment aurait-on pu détecter le problème avant les infirmières ?" | En testant régulièrement la connectivité du scanner |
| "Quelle est la différence entre 'attendre un message d'alerte' et 'tester régulièrement' ?" | Passif vs actif : supervision passive attend ; supervision active interroge |
| "Quel délai acceptable entre la panne et sa détection en milieu hospitalier ?" | 1–5 minutes maximum — chaque minute compte |

**Le formateur conclut :**

> *"C'est exactement la philosophie de Nagios : toutes les X minutes, Nagios teste lui-même si chaque service est OK. Si ça ne répond pas → alerte immédiate. Sans attendre que quelqu'un s'en plaigne."*

---

## 📊 PHASE 2 – Brainstorming : Qu'est-ce qu'on supervise ? (8 min)

**Groupes de 4 — Pour votre projet IoT (capteurs, Raspberry Pi, réseau de l'atelier), listez :**

| **Quoi superviser ?** | **Seuil d'alerte raisonnable** | **Impact si non détecté** |
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

**Réponses typiques attendues :**

| **Élément supervisé** | **Seuil WARNING** | **Seuil CRITICAL** | **Impact** |
|---|---|---|---|
| Disponibilité du Raspberry Pi (ping) | Latence > 200 ms | Pas de réponse | Plus de données remontées |
| Espace disque de la carte SD | > 75% | > 90% | Perte de données capteurs |
| Température CPU du Pi | > 65°C | > 80°C | Arrêt thermique du Pi |
| Disponibilité de l'API REST du capteur | Réponse > 2 s | Pas de réponse | Applications sans données |
| Connexion MQTT broker | — | Broker non joignable | Rupture de la chaîne IoT |
| Niveau de batterie (si Pi nomade) | < 30% | < 10% | Perte du nœud IoT |

---

## 🎯 PHASE 3 – Le Problème des Seuils (8 min)

**Le formateur pose la situation :**

> *"Votre Raspberry Pi Pi-Atelier reçoit normalement les données de 10 capteurs de température. Aujourd'hui, il en reçoit 7. C'est une panne ? Une dégradation ? Une urgence ?"*

**Discussion :**

> → 7/10 capteurs = **WARNING** (dégradation à investiguer, mais le système tourne encore)
> → 0/10 capteurs = **CRITICAL** (panne totale, intervention immédiate)
> → 10/10 capteurs mais données incohérentes = **UNKNOWN** (le plugin ne sait pas si c'est bon ou mauvais)

**Formalisation :**

```
┌─────────────────────────────────────────────────────────────────────┐
│  Les 4 états Nagios :                                               │
│                                                                     │
│  🟢 OK       (code 0) : tout va bien                               │
│  🟡 WARNING  (code 1) : seuil d'alerte bas dépassé → surveiller    │
│  🔴 CRITICAL (code 2) : seuil critique dépassé → agir maintenant   │
│  🟠 UNKNOWN  (code 3) : le check n'a pas pu s'exécuter             │
│                                                                     │
│  Règle : seuil WARNING < seuil CRITICAL                             │
│  Exemple disque : WARNING à 75%, CRITICAL à 90%                     │
│  Exemple ping : WARNING à 200ms, CRITICAL à 500ms                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## ✍️ PHASE 4 – Démonstration live (5 min) + Synthèse

**Si disponible : le formateur affiche un tableau de bord Nagios déjà configuré :**

> *"Voilà ce que vous allez configurer aujourd'hui. Chaque ligne = un service supervisé. Vert = tout va bien. Rouge = problème. Et quand ça passe au rouge, un mail ou un SMS est envoyé automatiquement à l'admin."*

**Ce qu'on retiendra :**

```
Nagios = surveillance ACTIVE et PÉRIODIQUE des services réseau

  Nagios --[toutes les 5 min]--> check_ping 192.168.1.10
         --[toutes les 5 min]--> check_http www.monsite.com
         --[toutes les 5 min]--> check_disk /dev/sda1

  Si réponse = CRITICAL → envoi mail + SMS à l'admin
  Si retour à OK → envoi mail "retour à la normale"
```

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
