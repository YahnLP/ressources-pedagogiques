# 📖 FICHE COURS – S10 ANNÉE 2 – E31
## Nagios : Plugins & Checks, Alertes Mail/SMS, Supervision du Projet IoT

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS DE LA SÉANCE

- ✅ Comprendre l'architecture Nagios (serveur, plugins, NRPE)
- ✅ Configurer des hôtes et services dans Nagios (.cfg)
- ✅ Tester et utiliser les plugins standards
- ✅ Configurer les alertes par mail et SMS
- ✅ Superviser un équipement IoT (Raspberry Pi, capteur)

---

## 1️⃣ ARCHITECTURE NAGIOS

### Qu'est-ce que Nagios ?

> **Nagios** est un système de surveillance réseau open source qui vérifie **activement et périodiquement** l'état des équipements et services. Il alerte les administrateurs en cas de problème.

### Les composants

| **Composant** | **Rôle** |
|---|---|
| **Serveur Nagios** | Le cœur — orchestre tous les checks, stocke les états, envoie les alertes |
| **Plugins** | Scripts/programmes qui testent un service et retournent un code (OK/WARNING/CRITICAL) |
| **NRPE** | Nagios Remote Plugin Executor — exécute des plugins sur des machines distantes |
| **Interface Web** | Tableau de bord graphique pour visualiser les états en temps réel |
| **Fichiers .cfg** | Configuration des hôtes, services, contacts, commandes |

---

📷 **[ILLUSTRATION 1]**
*Schéma d'architecture Nagios. Au centre : le serveur Nagios (rectangle bleu avec l'engrenage Nagios). Autour, des équipements supervisés reliés par des flèches : un routeur (check_ping), un serveur web (check_http), un serveur Linux avec NRPE (check_disk, check_load via NRPE), un Raspberry Pi IoT (check_custom_iot). À droite du serveur Nagios : interface web (navigateur) et notifications (icônes mail + SMS). Style diagramme réseau technique, fond blanc, couleurs distinctes par composant.*

> **Légende :** Le serveur Nagios exécute périodiquement des plugins pour vérifier chaque équipement. Pour les équipements locaux (réseau), les plugins s'exécutent directement sur le serveur Nagios. Pour les équipements Linux distants, NRPE permet d'exécuter les plugins localement sur la machine distante et de renvoyer le résultat à Nagios.

---

### Checks actifs vs checks passifs

| **Type** | **Qui initie ?** | **Quand ?** | **Usage** |
|---|---|---|---|
| **Check actif** | Nagios interroge l'équipement | Périodique (ex : toutes les 5 min) | Standard — ping, HTTP, SSH, disque |
| **Check passif** | L'équipement envoie à Nagios (NSCA) | À l'événement | Équipements qui ne peuvent pas être interrogés de l'extérieur |

> En pratique : on utilise les **checks actifs** dans 95% des cas. Les checks passifs servent pour des équipements derrière NAT strict ou pour les résultats de scripts cron.

---

## 2️⃣ LES PLUGINS NAGIOS

### Principe d'un plugin

> Un plugin Nagios est un programme (bash, Python, Perl, C…) qui :
> 1. Effectue un test (ping, requête HTTP, lecture d'un fichier…)
> 2. Compare le résultat à des seuils WARNING et CRITICAL
> 3. Affiche un message sur stdout
> 4. Retourne un **code de sortie** (0, 1, 2, ou 3)

### Les codes de retour — à connaître par cœur

| **Code** | **État** | **Couleur** | **Signification** |
|---|---|---|---|
| **0** | **OK** | 🟢 Vert | Service fonctionnel |
| **1** | **WARNING** | 🟡 Jaune | Seuil d'avertissement dépassé |
| **2** | **CRITICAL** | 🔴 Rouge | Seuil critique dépassé — alerte immédiate |
| **3** | **UNKNOWN** | 🟠 Orange | Impossible de tester (erreur plugin, timeout) |

> ⚠️ **RÈGLE ABSOLUE :** Seuil WARNING < seuil CRITICAL. Exemple : `-w 75 -c 90` pour le disque.

---

### Tester un plugin depuis le CLI

> On peut (et doit !) tester les plugins manuellement **avant** de les configurer dans Nagios :

```bash
# Tester check_ping
/usr/lib/nagios/plugins/check_ping -H 192.168.1.1 -w 100,10% -c 500,50%

# Tester check_http
/usr/lib/nagios/plugins/check_http -H www.google.com -p 80

# Tester check_disk
/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /

# Tester check_ssh
/usr/lib/nagios/plugins/check_ssh -H 192.168.1.10

# Lire le code de retour du dernier plugin :
echo $?    # Affiche 0 (OK), 1 (WARNING), 2 (CRITICAL), 3 (UNKNOWN)
```

---

### Plugins standards à connaître

| **Plugin** | **Ce qu'il vérifie** | **Paramètres clés** |
|---|---|---|
| `check_ping` | Disponibilité et latence (ICMP) | `-H <ip> -w <latence>,<perte%> -c <latence>,<perte%>` |
| `check_http` | Réponse HTTP d'un serveur web | `-H <host> -p <port> -u <url>` |
| `check_https` | Réponse HTTPS + validité certificat | `-H <host> --ssl` |
| `check_ssh` | Disponibilité du service SSH | `-H <ip>` |
| `check_disk` | Espace disque disponible | `-w <warn%> -c <crit%> -p <partition>` |
| `check_load` | Charge CPU (load average) | `-w <w1>,<w5>,<w15> -c <c1>,<c5>,<c15>` |
| `check_procs` | Nombre de processus | `-w <warn> -c <crit> -C <nom_processus>` |
| `check_tcp` | Disponibilité d'un port TCP | `-H <ip> -p <port>` |
| `check_nrpe` | Exécuter un plugin sur machine distante | `-H <ip> -c <commande_nrpe>` |

---

📷 **[ILLUSTRATION 2]**
*Schéma montrant un plugin Nagios comme une "boîte noire" avec des entrées et sorties. Entrée : paramètres de la ligne de commande (-H, -w, -c, -p). À l'intérieur : le test (flèche vers l'équipement et retour). Sortie : un message texte sur stdout ("OK - Ping to 192.168.1.1: 12ms") et un code retour (0). Exemple concret avec check_disk : partitions mesurées, seuils comparés, résultat affiché. Style diagramme boîte noire pédagogique, fond blanc.*

> **Légende :** Tous les plugins Nagios suivent le même modèle : ils reçoivent des paramètres (hôte à tester, seuils), effectuent le test, affichent un message lisible par un humain sur stdout, et retournent un code 0/1/2/3. Ce format standardisé permet à Nagios d'interpréter n'importe quel plugin de la même façon.

---

## 3️⃣ CONFIGURATION NAGIOS — FICHIERS .CFG

### Organisation des fichiers de configuration

```
/etc/nagios/
├── nagios.cfg                    ← Config principale (pointeurs vers les autres)
├── objects/
│   ├── hosts.cfg                 ← Définition des équipements supervisés
│   ├── services.cfg              ← Définition des services à vérifier
│   ├── contacts.cfg              ← Définition des contacts (admins à alerter)
│   ├── commands.cfg              ← Définition des commandes/plugins
│   └── templates.cfg             ← Templates réutilisables (linux-server, etc.)
└── conf.d/
    ├── mon-routeur.cfg           ← Config spécifique d'un équipement
    └── pi-iot.cfg                ← Config du Raspberry Pi IoT
```

---

### Définir un hôte (hosts.cfg)

```nagios
define host {
    use                  linux-server        ; Template prédéfini
    host_name            PI-ATELIER          ; Nom unique dans Nagios
    alias                Raspberry Pi Atelier ; Nom affiché dans le dashboard
    address              192.168.1.50        ; Adresse IP à superviser
    max_check_attempts   3                   ; 3 échecs avant de passer HARD
    check_interval       5                   ; Vérifier toutes les 5 minutes
    retry_interval       1                   ; Réessayer toutes les 1 min si échec
    check_command        check-host-alive    ; Plugin pour vérifier la dispo
    notification_options d,u,r              ; Alertes si: Down, Unreachable, Recovery
    contacts             admin-ciel          ; Qui alerter
}
```

**Options `notification_options` pour les hôtes :**

| **Code** | **Signification** |
|---|---|
| `d` | Down (hôte non joignable) |
| `u` | Unreachable (inaccessible, hôte parent down) |
| `r` | Recovery (retour en ligne) |
| `f` | Flapping (état instable) |
| `n` | Never (désactiver toutes les notifs) |

---

### Définir un service (services.cfg)

```nagios
define service {
    use                  generic-service     ; Template prédéfini
    host_name            PI-ATELIER          ; Hôte auquel appartient ce service
    service_description  Vérification SSH    ; Nom affiché dans le dashboard
    check_command        check_ssh           ; Plugin à utiliser
    check_interval       5                   ; Vérifier toutes les 5 minutes
    retry_interval       1
    max_check_attempts   3
    notification_options w,u,c,r            ; WARNING, UNKNOWN, CRITICAL, Recovery
    contacts             admin-ciel
}
```

**Service avec seuils (exemple check_disk) :**

```nagios
define service {
    use                  generic-service
    host_name            PI-ATELIER
    service_description  Espace disque SD
    check_command        check_disk!20%!10%  ; !<warn>!<crit> = arguments
    check_interval       10
    max_check_attempts   2
    contacts             admin-ciel
}
```

---

### Définir les commandes (commands.cfg)

> Les commandes définissent comment invoquer les plugins. La plupart sont pré-définies dans le fichier commands.cfg standard.

```nagios
# Exemple de commande custom pour check IoT
define command {
    command_name    check_iot_temperature
    command_line    /usr/lib/nagios/plugins/check_iot_temp.sh -H $HOSTADDRESS$ -w $ARG1$ -c $ARG2$
}
# $HOSTADDRESS$ = adresse IP de l'hôte (automatique)
# $ARG1$, $ARG2$ = arguments passés avec ! dans la définition du service
```

---

## 4️⃣ CONTACTS ET NOTIFICATIONS

### Définir un contact (contacts.cfg)

```nagios
define contact {
    contact_name                admin-ciel
    alias                       Administrateur CIEL
    email                       admin@ciel-lycee.fr
    service_notification_period 24x7
    host_notification_period    24x7
    service_notification_options w,u,c,r,f
    host_notification_options   d,u,r,f
    service_notification_commands notify-service-by-email
    host_notification_commands  notify-host-by-email
}
```

---

### Configurer les alertes par e-mail

> Nagios utilise la commande `mail` (ou `sendmail`) du système pour envoyer les alertes. La commande de notification est définie dans commands.cfg.

**Commande de notification e-mail standard :**

```nagios
define command {
    command_name    notify-service-by-email
    command_line    /usr/bin/printf "%b" "***** Nagios *****\n\nNotification Type: $NOTIFICATIONTYPE$\n\nService: $SERVICEDESC$\nHost: $HOSTALIAS$\nAddress: $HOSTADDRESS$\nState: $SERVICESTATE$\n\nDate/Time: $LONGDATETIME$\n\nAdditional Info:\n\n$SERVICEOUTPUT$" | /usr/bin/mail -s "** $NOTIFICATIONTYPE$ Service Alert: $HOSTALIAS$/$SERVICEDESC$ is $SERVICESTATE$ **" $CONTACTEMAIL$
}
```

**Variables Nagios dans les notifications :**

| **Variable** | **Contenu** |
|---|---|
| `$NOTIFICATIONTYPE$` | Type : PROBLEM, RECOVERY, ACKNOWLEDGEMENT |
| `$HOSTALIAS$` | Nom de l'hôte |
| `$HOSTADDRESS$` | Adresse IP de l'hôte |
| `$SERVICESTATE$` | WARNING, CRITICAL, OK, UNKNOWN |
| `$SERVICEDESC$` | Description du service |
| `$SERVICEOUTPUT$` | Message du plugin (ex : "CRITICAL - Disk /: 95% used") |
| `$CONTACTEMAIL$` | E-mail du contact |
| `$LONGDATETIME$` | Date et heure complètes |

---

### Configurer les alertes par SMS

**Option 1 — Gammu (modem GSM branché sur le serveur) :**

```nagios
define command {
    command_name    notify-service-by-sms
    command_line    echo "$NOTIFICATIONTYPE$ - $HOSTALIAS$/$SERVICEDESC$ est $SERVICESTATE$" | gammu --sendsms TEXT $CONTACTPAGER$
}
```

**Option 2 — API Twilio (SMS via Internet, sans modem GSM) :**

```bash
#!/bin/bash
# Script notify-by-twilio.sh
curl -X POST https://api.twilio.com/2010-04-01/Accounts/$TWILIO_SID/Messages.json \
  --data-urlencode "Body=$1" \
  --data-urlencode "From=+33XXXXXXXXXX" \
  --data-urlencode "To=$2" \
  -u "$TWILIO_SID:$TWILIO_TOKEN"
```

**Option 3 — Pushover / Pushbullet (notification push smartphone) :**

> Solution légère sans modem GSM, via API HTTP. Un script bash appelle l'API Pushover et envoie une notification push sur le smartphone de l'admin.

---

## 5️⃣ SUPERVISION DU PROJET IOT

### Stratégie de supervision IoT

> Un projet IoT (Raspberry Pi + capteurs) nécessite de superviser plusieurs couches :

| **Couche** | **Ce qu'on supervise** | **Plugin/méthode** |
|---|---|---|
| **Disponibilité matérielle** | Le Pi répond-il au ping ? | `check_ping` |
| **Système** | Espace disque, charge CPU, température CPU | `check_disk`, `check_load`, script custom |
| **Services** | SSH dispo, API REST répond, broker MQTT actif | `check_ssh`, `check_http`, `check_tcp` |
| **Données capteurs** | Valeur du capteur dans les plages normales | Script custom → API REST ou fichier |
| **Connectivité IoT** | Topic MQTT reçu, données fraîches (horodatage) | Plugin Python custom |

---

### Créer un plugin custom pour un capteur de température IoT

> Le capteur de température du projet IoT expose ses données sur une API REST : `http://192.168.1.50:8080/api/temperature`

**Script plugin `/usr/lib/nagios/plugins/check_iot_temp.sh` :**

```bash
#!/bin/bash
# check_iot_temp.sh - Nagios plugin pour superviser la température IoT
# Usage: ./check_iot_temp.sh -H <host> -w <warn> -c <crit>

HOST=$2
WARN=$4
CRIT=$6

# Appel de l'API REST du capteur
TEMP=$(curl -s --max-time 5 "http://${HOST}:8080/api/temperature" | python3 -c "import sys,json; print(json.load(sys.stdin)['value'])" 2>/dev/null)

# Vérifier que la valeur a été obtenue
if [ -z "$TEMP" ]; then
    echo "UNKNOWN - Impossible de contacter l'API IoT (http://${HOST}:8080)"
    exit 3
fi

# Comparer aux seuils
if (( $(echo "$TEMP > $CRIT" | bc -l) )); then
    echo "CRITICAL - Température : ${TEMP}°C (seuil : ${CRIT}°C)"
    exit 2
elif (( $(echo "$TEMP > $WARN" | bc -l) )); then
    echo "WARNING - Température : ${TEMP}°C (seuil : ${WARN}°C)"
    exit 1
else
    echo "OK - Température : ${TEMP}°C | temperature=${TEMP};${WARN};${CRIT}"
    exit 0
fi
```

> 💡 La partie après `|` dans le message OK (`temperature=${TEMP};${WARN};${CRIT}`) est la **donnée de performance** — elle permet à des outils comme Nagiosgraph ou Grafana de tracer des courbes historiques.

---

**Déclaration dans Nagios :**

```nagios
# commands.cfg
define command {
    command_name    check_iot_temp
    command_line    /usr/lib/nagios/plugins/check_iot_temp.sh -H $HOSTADDRESS$ -w $ARG1$ -c $ARG2$
}

# services.cfg
define service {
    use                  generic-service
    host_name            PI-ATELIER
    service_description  Temperature Capteur 1
    check_command        check_iot_temp!28!35    ; WARNING à 28°C, CRITICAL à 35°C
    check_interval       2
    max_check_attempts   2
    contacts             admin-ciel
}
```

---

### Supervision MQTT (broker Mosquitto)

```bash
# Vérifier que le broker MQTT est accessible (port 1883)
/usr/lib/nagios/plugins/check_tcp -H 192.168.1.50 -p 1883

# Plugin custom : vérifier qu'un topic MQTT a été mis à jour récemment
#!/bin/bash
# Récupérer le dernier message d'un topic et vérifier son horodatage
LAST_MSG=$(mosquitto_sub -h $HOST -t "iot/capteur1/temperature" -C 1 --quiet 2>/dev/null)
if [ -z "$LAST_MSG" ]; then
    echo "CRITICAL - Aucun message reçu sur le topic MQTT"
    exit 2
fi
echo "OK - Valeur MQTT reçue : $LAST_MSG"
exit 0
```

---

## 6️⃣ WORKFLOW NAGIOS — DU CHECK À L'ALERTE

```
Nagios Core
    │
    │ [Toutes les check_interval minutes]
    ▼
Plugin exécuté ────────────────────────► Équipement testé
    │
    │ Code retour : 0/1/2/3 + message
    ▼
État actuel comparé à l'état précédent
    │
    ├─ Même état → Mise à jour du dernier check OK
    │
    └─ Changement d'état → Soft State (compteur)
              │
              │ [après max_check_attempts]
              ▼
           Hard State → NOTIFICATION envoyée
              │
              ├─ notify-by-email → mail à l'admin
              └─ notify-by-sms   → SMS à l'admin
```

### États Soft vs Hard

| **État** | **Signification** | **Notification ?** |
|---|---|---|
| **Soft State** | Nouvel état détecté, mais pas encore confirmé (max_check_attempts pas atteint) | ❌ Non |
| **Hard State** | État confirmé après max_check_attempts échecs consécutifs | ✅ Oui |

> 💡 Avec `max_check_attempts = 3` : Nagios attend 3 checks consécutifs en échec avant d'envoyer l'alerte. Cela évite les faux positifs sur des timeouts transitoires.

---

## 7️⃣ COMMANDES D'ADMINISTRATION NAGIOS

```bash
# ── Validation de la configuration (OBLIGATOIRE avant chaque reload) ──
sudo nagios -v /etc/nagios/nagios.cfg

# ── Recharger la configuration ──
sudo systemctl reload nagios

# ── Redémarrer Nagios ──
sudo systemctl restart nagios

# ── Vérifier l'état du service ──
sudo systemctl status nagios

# ── Suivre les logs en temps réel ──
sudo tail -f /var/log/nagios/nagios.log

# ── Tester l'envoi d'un mail ──
echo "Test Nagios" | mail -s "Test alerte" admin@ciel-lycee.fr

# ── Tester un plugin manuellement ──
/usr/lib/nagios/plugins/check_ping -H 8.8.8.8 -w 100,10% -c 500,50%
```

---

## ✅ AUTO-ÉVALUATION

- [ ] Je connais les 4 états Nagios et leurs codes (0=OK, 1=WARN, 2=CRIT, 3=UNK)
- [ ] Je sais tester un plugin Nagios depuis la ligne de commande
- [ ] Je sais écrire un bloc `define host {}` minimal
- [ ] Je sais écrire un bloc `define service {}` avec check_command et seuils
- [ ] Je sais écrire un bloc `define contact {}` avec notification par e-mail
- [ ] Je comprends la différence check actif / passif
- [ ] Je comprends Soft State vs Hard State (max_check_attempts)
- [ ] Je sais créer un plugin custom shell qui retourne le bon code de sortie
- [ ] Je sais superviser une API REST IoT avec un script Nagios

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **Nagios Core** | Moteur de supervision open source — orchestre les checks et les alertes |
| **Plugin** | Programme qui teste un service et retourne un code 0/1/2/3 |
| **Check actif** | Nagios interroge l'équipement périodiquement |
| **Check passif** | L'équipement envoie son état à Nagios (NSCA) |
| **NRPE** | Agent Nagios pour exécuter des plugins sur machines distantes |
| **Hard State** | État confirmé après max_check_attempts échecs — déclenche l'alerte |
| **Soft State** | État transitoire — Nagios réessaie avant de confirmer |
| **Flapping** | Service qui oscille rapidement entre OK et CRITICAL — état instable |
| **Perf data** | Données de performance dans le message du plugin (pour tracer des graphes) |
| **check_interval** | Fréquence des vérifications en minutes (ex : 5 = toutes les 5 min) |
| **max_check_attempts** | Nombre d'échecs consécutifs avant alerte Hard State |
| **contact** | Personne à notifier lors des alertes (email, SMS) |
| **notification_options** | Événements déclenchant une notification (w, c, r, d, u, f) |

---

## 📌 POINTS-CLÉS À RETENIR

1. Nagios teste **activement** et **périodiquement** — il n'attend pas qu'on lui signale un problème
2. Codes retour : **0=OK**, **1=WARNING**, **2=CRITICAL**, **3=UNKNOWN**
3. Seuil WARNING **toujours inférieur** au seuil CRITICAL (`-w 75 -c 90`)
4. **Toujours valider** avec `nagios -v nagios.cfg` avant de recharger
5. **Soft State** = transitoire (max_check_attempts pas atteint, pas d'alerte) ; **Hard State** = confirmé (alerte envoyée)
6. Un plugin = un script qui retourne `exit 0/1/2/3` + affiche un message
7. Pour l'IoT : superviser disponibilité + système + données capteur + connectivité MQTT

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
