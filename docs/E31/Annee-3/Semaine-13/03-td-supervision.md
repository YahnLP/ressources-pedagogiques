# 🎯 TD RÉVISIONS — SUPERVISION (Nagios)
## S13 Année 3 – E31

**Nom : ________________  Prénom : ________________**

---

## 📋 RAPPEL SYNTHÉTIQUE NAGIOS

### Architecture en 5 blocs

```
┌─────────────────────────────────────────────────────────────────┐
│  HÔTES (host)   → les équipements à surveiller                  │
│  SERVICES       → ce qu'on vérifie sur chaque hôte              │
│  COMMANDES      → comment exécuter un check (check_ping, etc.)  │
│  CONTACTS       → qui reçoit les alertes (email, SMS)           │
│  PÉRIODES       → quand envoyer les alertes (heures ouvrées...) │
└─────────────────────────────────────────────────────────────────┘
```

### Codes retour plugins

| **Code** | **État** | **Couleur** |
|---|---|---|
| 0 | **OK** | 🟢 |
| 1 | **WARNING** | 🟡 |
| 2 | **CRITICAL** | 🔴 |
| 3 | **UNKNOWN** | 🟠 |

### Timing Hard/Soft State

```
max_check_attempts = 3 (exemple)

1ère anomalie → Soft State (pas d'alerte encore)
2ème anomalie → Soft State (pas d'alerte encore)
3ème anomalie → HARD STATE → alerte envoyée ✅

Si OK entre les tentatives → retour à zéro
```

### Seuils et perf data

```bash
# Syntaxe plugin avec perf data :
check_disk -H 192.168.1.1 -w 75% -c 90%
# Sortie :
DISK OK - / 52% used | /=52%;75;90;0;100

# Règle : WARNING < CRITICAL (toujours)
```

---

## 🧪 TD-SUP1 — Architecture et Timing (5 pts)

### Contexte

> Le réseau ACME est supervisé par Nagios. Voici la configuration du service `check_http` sur le serveur web principal :

```nagios
define service {
    use                     generic-service
    host_name               SRV-WEB
    service_description     HTTP
    check_command           check_http
    normal_check_interval   5
    retry_check_interval    1
    max_check_attempts      4
    contact_groups          admins
    notification_options    w,c,r
    notification_interval   60
}
```

**SUP1.1 *(1 pt)*** — Le serveur web tombe à 14h00. Combien de minutes s'écoulent avant que la première alerte email soit envoyée ? Montrez votre calcul.

```
Tentative 1 (Soft) : 14h00 + _____ min = _______
Tentative 2 (Soft) : + _____ min = _______
Tentative 3 (Soft) : + _____ min = _______
Tentative 4 (Hard) : + _____ min = _______  ← ALERTE ENVOYÉE
Délai total avant alerte : _____ minutes
```

**SUP1.2 *(1 pt)*** — Le `notification_interval` est fixé à 60. Que se passe-t-il si le serveur reste en CRITICAL pendant 3 heures ? Combien d'alertes email l'admin reçoit-il au total ?

_________________________________________________________________________
_________________________________________________________________________

**SUP1.3 *(0,5 pt)*** — Que signifie `notification_options: w,c,r` ? Listez les trois événements déclencheurs.

_________________________________________________________________________

**SUP1.4 *(1 pt)*** — L'admin ajoute un deuxième admin `marie` dans les contacts. Mais Marie ne travaille que de 8h à 18h. Quel bloc Nagios faut-il configurer pour que Marie ne reçoive des alertes que pendant ses heures de travail ?

_________________________________________________________________________
_________________________________________________________________________

**SUP1.5 *(1,5 pt)*** — Voici la sortie `show nagios status` pour le service HTTP :

```
SRV-WEB / HTTP : CRITICAL (Hard)
  Last check: 14:23:45
  Next check: 14:28:45
  Attempt: 4/4
  Output: CRITICAL - Socket timeout after 10 seconds
```

Identifiez le problème probable. Proposez 2 actions de diagnostic.

_________________________________________________________________________
_________________________________________________________________________

---

## 🧪 TD-SUP2 — Lecture de Sortie Plugin (4 pts)

### Sortie brute d'un plugin personnalisé

```bash
$ /usr/lib/nagios/plugins/check_temp_salle -H 10.0.5.5 -w 28 -c 35
TEMPERATURE WARNING - 29.3°C | temp=29.3;28;35;0;50
$ echo $?
1
```

**SUP2.1 *(0,5 pt)*** — Quel est l'état retourné par ce plugin ?

_________________________________________________________________________

**SUP2.2 *(1 pt)*** — Décomposez la ligne de performance data `temp=29.3;28;35;0;50` champ par champ :

| **Champ** | **Valeur** | **Signification** |
|---|---|---|
| Métrique | `temp` | Nom de la métrique |
| Valeur actuelle | | |
| Seuil WARNING | | |
| Seuil CRITICAL | | |
| Min | | |
| Max | | |

**SUP2.3 *(1 pt)*** — La prochaine vérification retourne `exit 0` avec `temp=27.8`. Quel état affiche Nagios ? La règle Hold State s'applique-t-elle ici ?

_________________________________________________________________________
_________________________________________________________________________

**SUP2.4 *(1,5 pt)*** — Le plugin `check_temp_salle` retourne parfois `exit 3` avec le message `UNKNOWN - Cannot connect to sensor API`. Quelles sont les 3 causes possibles pour un code UNKNOWN (3) plutôt que CRITICAL (2) ?

1. _______________________________________________________________________
2. _______________________________________________________________________
3. _______________________________________________________________________

---

## 🧪 TD-SUP3 — Plugin Custom à Corriger (5 pts)

### Script à corriger

> Ce script est censé surveiller l'espace disque d'un appareil IoT via son API REST. Il contient **3 erreurs**. Trouvez-les et corrigez-les.

```bash
#!/bin/bash
# check_iot_disk.sh — Vérifier l'espace disque d'un IoT via API REST

HOST=$1
WARN=$2
CRIT=$3

# Appel API
DISK=$(curl -s "http://$HOST/api/disk" | grep -o '"used":[0-9]*' | grep -o '[0-9]*')

if [ -z "$DISK" ]; then
    echo "UNKNOWN - Cannot reach API on $HOST"
    exit 3
fi

# Vérification des seuils
if [ "$DISK" -ge "$CRIT" ]; then
    echo "DISK CRITICAL - Usage: ${DISK}%"
    exit 2
fi

if [ "$DISK" -ge "$WARN" ]; then
    echo "DISK WARNING - Usage: ${DISK}%"
    exit 2         # ERREUR 1
fi

echo "DISK OK - Usage: ${DISK}%"
exit 1             # ERREUR 2
                   # (ERREUR 3 : donnée de performance manquante)
```

**SUP3.1 *(1 pt)*** — Identifiez et corrigez l'ERREUR 1 :

_________________________________________________________________________

**SUP3.2 *(1 pt)*** — Identifiez et corrigez l'ERREUR 2 :

_________________________________________________________________________

**SUP3.3 *(2 pts)*** — Identifiez l'ERREUR 3 et réécrivez la ligne de sortie OK avec la performance data correcte (métrique `disk`, valeurs w=`$WARN`, c=`$CRIT`, min=0, max=100) :

```bash
# Ligne corrigée :
echo "_____________________________________________"
```

**SUP3.4 *(1 pt)*** — Quelle commande bash faut-il exécuter avant de tester ce plugin depuis Nagios pour qu'il soit exécutable ?

```bash
$ _____________________________________________
```

---

## 📊 BARÈME TD SUPERVISION

| **Section** | **Points** |
|---|---|
| TD-SUP1 | /5 |
| TD-SUP2 | /4 |
| TD-SUP3 | /5 |
| **TOTAL** | **/14** |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
