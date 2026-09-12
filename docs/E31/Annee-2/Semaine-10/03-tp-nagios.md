# 🔬 TP LINUX – S10 ANNÉE 2 – E31
## Nagios : Configuration Plugins, Checks et Alertes — Supervision du Projet IoT

**Nom : ________________  Prénom : ________________  Date : ________________**
**Binôme : ________________**

---

## 🎯 OBJECTIFS DU TP

- ✅ Configurer des hôtes et services Nagios dans des fichiers .cfg
- ✅ Tester des plugins Nagios depuis la ligne de commande
- ✅ Configurer un contact avec notification par e-mail
- ✅ Créer et intégrer un check custom pour superviser le Raspberry Pi IoT
- ✅ Interpréter le tableau de bord Nagios (états, historique)

---

## ⏱️ DURÉE : 70 min

---

## 📋 ENVIRONNEMENT

| **Équipement** | **IP** | **Rôle** |
|---|---|---|
| Serveur Nagios (VM Debian/Ubuntu) | 192.168.100.10 | Moteur de supervision |
| Routeur-LAN | 192.168.1.1 | Équipement réseau à superviser |
| Serveur-Web (Apache) | 192.168.1.20 | Service HTTP à superviser |
| PI-ATELIER (Raspberry Pi) | 192.168.1.50 | Équipement IoT à superviser |
| Votre poste | 192.168.100.X | Connexion SSH au serveur Nagios |

> **Connexion :** `ssh nagiosadmin@192.168.100.10`
> **Interface web :** `http://192.168.100.10/nagios` (admin / nagios)

---

## ⚠️ RÈGLES IMPORTANTES

> 🔴 Toujours valider la config avant de recharger : `sudo nagios -v /etc/nagios/nagios.cfg`
> 🔴 Toujours recharger après modification : `sudo systemctl reload nagios`
> 🔴 En cas de doute sur la syntaxe : consulter la fiche cours ou `man nagios`

---

## 🧪 PARTIE 1 – Tests manuels de plugins (10 min)

### 1.1 – Tester check_ping

```bash
/usr/lib/nagios/plugins/check_ping -H 192.168.1.1 -w 100,20% -c 500,60%
```

**Résultat obtenu :**

```
___________________________________________________________________________
```

**Code de retour :**

```bash
echo $?   →  _______
```

**Q1.** Quel état correspond à ce code ? ___________

---

### 1.2 – Tester check_http

```bash
/usr/lib/nagios/plugins/check_http -H 192.168.1.20 -p 80
```

**Résultat :** ___________________________________________

**Q2.** Modifiez la commande pour vérifier que la page répond en moins de 2 secondes (option `-t 2`). Écrivez la commande et son résultat :

```bash
_____________________________________________
```

---

### 1.3 – Tester check_disk

```bash
/usr/lib/nagios/plugins/check_disk -w 20% -c 10% -p /
```

**Résultat :** ___________________________________________

**Q3.** Quel est le pourcentage d'espace utilisé sur la partition `/` ? ___________

---

### 1.4 – Tester check_load

```bash
/usr/lib/nagios/plugins/check_load -w 3,2,1 -c 6,4,2
```

**Résultat :** ___________________________________________

**Q4.** À quoi correspondent les trois valeurs `-w 3,2,1` dans ce check ?

_________________________________________________________________________

---

## 🔬 PARTIE 2 – Configuration des hôtes (15 min)

### 2.1 – Créer le fichier de configuration

```bash
sudo nano /etc/nagios/conf.d/projet-ciel.cfg
```

### 2.2 – Ajouter le Routeur-LAN

**Copiez et complétez la définition suivante :**

```nagios
define host {
    use                  generic-host
    host_name            ____________
    alias                Routeur principal LAN
    address              ____________
    max_check_attempts   3
    check_interval       5
    retry_interval       1
    check_command        check-host-alive
    notification_options d,r
    contacts             nagiosadmin
}
```

### 2.3 – Ajouter le Serveur-Web

```nagios
define host {
    use                  linux-server
    host_name            ____________
    alias                Serveur Web Atelier
    address              ____________
    max_check_attempts   ______
    check_interval       ______
    retry_interval       1
    check_command        check-host-alive
    notification_options d,u,r
    contacts             nagiosadmin
}
```

### 2.4 – Ajouter le PI-ATELIER (Raspberry Pi)

```nagios
define host {
    use                  linux-server
    host_name            PI-ATELIER
    alias                ____________
    address              ____________
    max_check_attempts   3
    check_interval       2
    retry_interval       1
    check_command        check-host-alive
    notification_options d,u,r
    contacts             nagiosadmin
}
```

### 2.5 – Valider et recharger

```bash
sudo nagios -v /etc/nagios/nagios.cfg
```

**Résultat validation :**

```
Total Warnings: _______
Total Errors:   _______
```

**Si erreurs → corriger avant de continuer.**

```bash
sudo systemctl reload nagios
```

---

## ✅ PARTIE 3 – Configuration des services (15 min)

### 3.1 – Ajouter les services au même fichier projet-ciel.cfg

**Service HTTP sur Serveur-Web :**

```nagios
define service {
    use                  generic-service
    host_name            SERVEUR-WEB
    service_description  ____________
    check_command        check_http
    check_interval       5
    max_check_attempts   3
    contacts             nagiosadmin
}
```

**Service SSH sur PI-ATELIER :**

```nagios
define service {
    use                  generic-service
    host_name            PI-ATELIER
    service_description  ____________
    check_command        check_ssh
    check_interval       5
    max_check_attempts   3
    contacts             nagiosadmin
}
```

**Service Espace Disque sur PI-ATELIER (seuil WARNING 75%, CRITICAL 90%) :**

```nagios
define service {
    use                  generic-service
    host_name            PI-ATELIER
    service_description  Espace Disque SD
    check_command        check_disk!______!______
    check_interval       10
    max_check_attempts   2
    contacts             nagiosadmin
}
```

**Service Charge CPU sur PI-ATELIER :**

```nagios
define service {
    use                  generic-service
    host_name            PI-ATELIER
    service_description  Charge CPU
    check_command        check_load!3,2,1!6,4,2
    check_interval       5
    max_check_attempts   3
    contacts             nagiosadmin
}
```

### 3.2 – Valider et recharger

```bash
sudo nagios -v /etc/nagios/nagios.cfg && sudo systemctl reload nagios
```

---

## 🔔 PARTIE 4 – Configuration des alertes mail (10 min)

### 4.1 – Tester l'envoi d'e-mail depuis le serveur

```bash
echo "Test alerte Nagios" | mail -s "Test S10" votre.email@domaine.fr
```

**L'e-mail a-t-il été reçu ? _______ (Si non, appeler le formateur)**

---

### 4.2 – Vérifier la configuration du contact nagiosadmin

```bash
grep -A 15 "define contact {" /etc/nagios/objects/contacts.cfg
```

**Relevez l'e-mail actuellement configuré :** ___________

---

### 4.3 – Modifier l'adresse e-mail du contact nagiosadmin

```bash
sudo nano /etc/nagios/objects/contacts.cfg
```

Changez la ligne `email` pour votre adresse ou celle du formateur.

**Vérifier :**

```bash
grep "email" /etc/nagios/objects/contacts.cfg
```

---

### 4.4 – Simuler une panne et observer la notification

> Pour simuler une panne, arrêtez momentanément le service Apache sur Serveur-Web :

```bash
# Depuis le Serveur-Web (si accessible) :
sudo systemctl stop apache2

# Attendre 2 check_intervals (2×5 = 10 min) puis vérifier le dashboard Nagios
# Puis redémarrer :
sudo systemctl start apache2
```

**Q5.** Après la panne simulée, quel état apparaît dans le dashboard ? ___________

**Q6.** Après le redémarrage d'Apache, quel est l'état final et quel type de notification est envoyé ?

_________________________________________________________________________

---

## 🤖 PARTIE 5 – Check custom IoT (15 min)

### 5.1 – Créer le plugin custom

```bash
sudo nano /usr/lib/nagios/plugins/check_iot_temp.sh
```

**Contenu du script (à recopier et adapter) :**

```bash
#!/bin/bash
# Plugin Nagios : supervision température IoT via API REST
# Usage: check_iot_temp.sh <host> <warn> <crit>

HOST=$1
WARN=$2
CRIT=$3

# Appel API REST (adapter l'URL à votre projet)
TEMP=$(curl -s --max-time 5 "http://${HOST}:8080/api/temperature" \
       | python3 -c "import sys,json; print(json.load(sys.stdin)['value'])" 2>/dev/null)

if [ -z "$TEMP" ]; then
    echo "UNKNOWN - API IoT non joignable (http://${HOST}:8080)"
    exit 3
fi

if (( $(echo "$TEMP > $CRIT" | bc -l) )); then
    echo "CRITICAL - Temperature: ${TEMP}C (seuil critical: ${CRIT}C)"
    exit 2
elif (( $(echo "$TEMP > $WARN" | bc -l) )); then
    echo "WARNING - Temperature: ${TEMP}C (seuil warning: ${WARN}C)"
    exit 1
else
    echo "OK - Temperature: ${TEMP}C | temperature=${TEMP};${WARN};${CRIT}"
    exit 0
fi
```

### 5.2 – Rendre le plugin exécutable et tester

```bash
sudo chmod +x /usr/lib/nagios/plugins/check_iot_temp.sh

# Test manuel :
/usr/lib/nagios/plugins/check_iot_temp.sh 192.168.1.50 28 35
```

**Résultat du test :** ___________________________________________

**Code de retour (echo $?) :** ___________

---

### 5.3 – Déclarer la commande dans Nagios

```bash
sudo nano /etc/nagios/objects/commands.cfg
```

**Ajouter à la fin du fichier :**

```nagios
define command {
    command_name    check_iot_temp
    command_line    /usr/lib/nagios/plugins/check_iot_temp.sh $HOSTADDRESS$ $ARG1$ $ARG2$
}
```

---

### 5.4 – Ajouter le service IoT dans projet-ciel.cfg

```nagios
define service {
    use                  generic-service
    host_name            PI-ATELIER
    service_description  Temperature Capteur IoT
    check_command        check_iot_temp!28!35
    check_interval       2
    max_check_attempts   2
    contacts             nagiosadmin
}
```

### 5.5 – Valider, recharger et vérifier dans le dashboard

```bash
sudo nagios -v /etc/nagios/nagios.cfg && sudo systemctl reload nagios
```

**État dans le dashboard :** ___________

---

## 📊 PARTIE 6 – Lecture du tableau de bord (5 min)

### Capturez ou notez l'état de votre supervision

| **Hôte** | **État** | **Services supervisés** | **Dernier check** |
|---|---|---|---|
| ROUTEUR-LAN | | | |
| SERVEUR-WEB | | | |
| PI-ATELIER | | | |

**Q7.** Dans le dashboard, quelle information vous permet de savoir si une alerte a déjà été envoyée (Hard State vs Soft State) ?

_________________________________________________________________________

**Q8.** Un hôte est en état `DOWN/SOFT (1/3)`. Qu'est-ce que cela signifie ? Nagios a-t-il déjà envoyé une alerte ?

_________________________________________________________________________
_________________________________________________________________________

**Q9.** Vous observez un service en état `UNKNOWN`. Quelle est la première action à effectuer pour diagnostiquer ?

_________________________________________________________________________

---

## 📊 BARÈME DU TP

| **Section** | **Critère** | **Points** |
|---|---|---|
| Partie 1 | 4 tests plugins + Q1–Q4 | /4 |
| Partie 2 | 3 hôtes configurés, validation sans erreur | /4 |
| Partie 3 | 4 services configurés correctement | /4 |
| Partie 4 | Contact mail + simulation panne + Q5–Q6 | /3 |
| Partie 5 | Plugin IoT créé + testé + intégré | /4 |
| Partie 6 | Tableau de bord + Q7–Q9 | /2 |
| Présentation / Clarté | — | /1 |
| **TOTAL** | | **/22** |

> *Ramené à /20 : score × 0,91*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
