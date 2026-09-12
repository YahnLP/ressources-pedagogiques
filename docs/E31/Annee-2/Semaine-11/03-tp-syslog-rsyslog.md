# 🔬 TRAVAUX PRATIQUES — S11 · 2ᵉ ANNÉE · E31
## Syslog centralisé : Installer rsyslog · Filtres · Rotation · Lien SIEM

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **Linux VM**
> **Infrastructure** : VM1 = log-server (192.168.50.10) · VM2 = web-server (192.168.50.20)
> **Épreuve ciblée** : **E31** – Administration des systèmes

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S5.2** | Installer et configurer rsyslog serveur + client |
| **S5.3** | Écrire des règles de filtrage rsyslog |
| **S5.4** | Configurer logrotate |
| **S5.5** | Vérifier le lien SIEM (forwarding JSON) |
| **C2.4** | Administrer un serveur Linux |

---

## 🟢 NIVEAU 1 — Préparer l'environnement (10 min)

### Sur les deux VMs

**1.1** — Vérifie la connectivité réseau :

```bash
# Sur web-server (VM2)
ping -c 3 192.168.50.10
```

```
Résultat : ☐ 3 paquets reçus — OK ☐ 0 paquets — problème réseau à corriger
```

**1.2** — Vérifie que rsyslog est installé et actif sur les deux VMs :

```bash
systemctl status rsyslog
rsyslogd -v
```

```
Version rsyslog sur log-server  : _______
Version rsyslog sur web-server  : _______
Status (active/inactive)        : _______
```

**1.3** — Envoie un message de test depuis web-server :

```bash
logger -p auth.info "TEST CONNEXION depuis web-server"
```

Vérifie qu'il apparaît localement sur web-server :

```bash
tail -5 /var/log/auth.log
```

```
Le message apparaît ? ☐ Oui — note la ligne : ______________________________
                      ☐ Non — vérifier le service rsyslog
```

---

## 🟡 NIVEAU 2 — Configurer le serveur rsyslog (20 min)

### Sur log-server (VM1)

**2.1** — Ouvre le fichier de configuration principal :

```bash
nano /etc/rsyslog.conf
```

Décommente (ou ajoute) les lignes suivantes pour activer l'écoute :

```bash
# Activer UDP
module(load="imudp")
input(type="imudp" port="514")

# Activer TCP (plus fiable)
module(load="imtcp")
input(type="imtcp" port="514")
```

**2.2** — Crée un fichier de configuration dédié aux logs distants :

```bash
nano /etc/rsyslog.d/10-remote.conf
```

Ajoute ce contenu :

```bash
# Template : un fichier par hostname source
template(name="RemoteLogs" type="string"
         string="/var/log/distant/%HOSTNAME%/%PROGRAMNAME%.log")

# Règle : tout message venant d'une machine distante → dans son propre fichier
if $FROMHOST-IP != "127.0.0.1" then {
    action(type="omfile" DynaFile="RemoteLogs" dirCreateMode="0755" FileCreateMode="0644")
    stop
}
```

**2.3** — Crée le répertoire de réception et redémarre rsyslog :

```bash
mkdir -p /var/log/distant
chmod 755 /var/log/distant
systemctl restart rsyslog

# Vérifie qu'rsyslog écoute bien sur le port 514
ss -ulnp | grep 514
ss -tlnp | grep 514
```

```
Port UDP 514 en écoute ? ☐ Oui ☐ Non
Port TCP 514 en écoute ? ☐ Oui ☐ Non
```

**2.4** — Vérifie la syntaxe du fichier de configuration :

```bash
rsyslogd -N1
```

```
Résultat : ☐ "End of config validation run" → OK
           ☐ Erreur de syntaxe : ______________________________________
```

---

## 🟠 NIVEAU 3 — Configurer le client (forwarding) (15 min)

### Sur web-server (VM2)

**3.1** — Crée le fichier de forwarding :

```bash
nano /etc/rsyslog.d/50-forwarding.conf
```

Ajoute :

```bash
# Envoyer TOUS les logs vers le serveur central (TCP)
*.* @@192.168.50.10:514
```

**3.2** — Redémarre rsyslog sur web-server :

```bash
systemctl restart rsyslog
```

**3.3** — Génère plusieurs messages de test depuis web-server :

```bash
logger -p auth.warning "ALERTE AUTH test depuis web-server"
logger -p daemon.info "Service nginx démarré (test)"
logger -p kern.crit "ERREUR CRITIQUE kernel (test)"
logger -p local7.notice "Application métier : utilisateur connecté"
```

**3.4** — Vérifie la réception sur log-server (VM1) :

```bash
# Sur log-server :
ls -la /var/log/distant/
ls -la /var/log/distant/web-server/
tail -20 /var/log/distant/web-server/logger.log
```

```
Le répertoire /var/log/distant/web-server/ a été créé ? ☐ Oui ☐ Non
Les messages de test sont présents ?
  auth.warning   : ☐ Oui ☐ Non
  daemon.info    : ☐ Oui ☐ Non
  kern.crit      : ☐ Oui ☐ Non
```

---

## 🔵 NIVEAU 4 — Écrire des règles de filtrage (25 min)

### Sur log-server (VM1)

**4.1** — Crée un fichier de règles de filtrage avancé :

```bash
nano /etc/rsyslog.d/20-filters.conf
```

**Règle 1** — Créer un fichier dédié aux échecs d'authentification :

```bash
if $msg contains "Failed password" or $msg contains "authentication failure" then {
    action(type="omfile" file="/var/log/distant/auth_failures.log")
}
```

**Règle 2** — Centraliser toutes les urgences (severity 0-2) dans un fichier critique :

```bash
if $syslogseverity <= 2 then {
    action(type="omfile" file="/var/log/distant/CRITICAL.log")
}
```

**Règle 3** — Ignorer les messages debug pour alléger le volume :

```bash
if $syslogseverity == 7 then stop
```

**4.2** — Redémarre rsyslog et recharge la config :

```bash
systemctl restart rsyslog
rsyslogd -N1
```

**4.3** — Teste les règles depuis web-server :

```bash
# Simuler un échec d'authentification
logger -p auth.warning "Failed password for root from 10.0.0.99 port 12345 ssh2"

# Simuler une urgence
logger -p kern.emerg "DISQUE DÉFAILLANT - panique immédiate"

# Simuler un message debug (doit être ignoré)
logger -p daemon.debug "Message debug à ignorer"
```

**4.4** — Vérifie sur log-server que les règles fonctionnent :

```bash
cat /var/log/distant/auth_failures.log
cat /var/log/distant/CRITICAL.log
# Le message debug NE doit PAS apparaître dans les logs distants
grep "debug à ignorer" /var/log/distant/web-server/*.log
```

```
auth_failures.log contient le message "Failed password" ? ☐ Oui ☐ Non
CRITICAL.log contient l'urgence kernel ? ☐ Oui ☐ Non
Message debug présent dans les logs distants ? ☐ Oui (problème) ☐ Non (correct)
```

---

## 🔴 NIVEAU 5 — Configurer logrotate et préparer le SIEM (10 min)

### Logrotate sur log-server

**5.1** — Crée la configuration de rotation pour les logs distants :

```bash
nano /etc/logrotate.d/rsyslog-distant
```

Ajoute :

```bash
/var/log/distant/*/*.log {
    daily
    missingok
    rotate 30
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

**5.2** — Teste la configuration logrotate :

```bash
logrotate --debug /etc/logrotate.d/rsyslog-distant
```

```
La config est valide ? ☐ Oui — message "rotating log" visible ☐ Non — erreur : _______
```

**5.3** — Force une rotation pour tester :

```bash
logrotate --force /etc/logrotate.d/rsyslog-distant
ls -la /var/log/distant/web-server/
```

```
Fichiers après rotation :
  *.log       (fichier actuel) : ☐ présent
  *.log.1     (non compressé)  : ☐ présent
  *.log.2.gz  (compressé)      : ☐ présent (si ≥ 2 rotations)
```

### Préparer le forwarding SIEM

**5.4** — Ajoute une règle pour envoyer les logs critiques vers le SIEM (IP fictive 192.168.50.100) :

```bash
# Dans /etc/rsyslog.d/30-siem.conf
nano /etc/rsyslog.d/30-siem.conf
```

```bash
# Envoyer les events d'auth et les critiques au SIEM
if ($syslogfacility-text == "auth" or $syslogseverity <= 3) then {
    action(type="omfwd" target="192.168.50.100" port="5514" protocol="tcp")
}
```

**5.5** — Réponds aux questions de synthèse :

```
Pourquoi utiliser TCP (@@) plutôt que UDP (@) pour le forwarding en production ?
______________________________________________________________________________

Si le serveur rsyslog est indisponible, que se passe-t-il avec les logs du client ?
(Cherche la directive "ActionQueueType" dans la doc rsyslog)
______________________________________________________________________________

Quelle commande surveille les logs en temps réel sur le serveur central ?
______________________________________________________________________________

Comment vérifier que le port 514 est bien ouvert dans le pare-feu ?
______________________________________________________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Configurer rsyslog en mode serveur (UDP+TCP 514) | ☐ | ☐ | ☐ |
| Configurer rsyslog en mode client (forwarding) | ☐ | ☐ | ☐ |
| Créer un template de fichier par hostname | ☐ | ☐ | ☐ |
| Écrire une règle `if $msg contains` | ☐ | ☐ | ☐ |
| Filtrer par severity (≤ 2, == 7) | ☐ | ☐ | ☐ |
| Configurer logrotate (daily/rotate/compress) | ☐ | ☐ | ☐ |
| Tester avec `logger` et vérifier la réception | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.2 — rsyslog serveur écoute UDP+TCP 514 | /5 |
| Niv.3 — Forwarding client fonctionnel, logs reçus | /5 |
| Niv.4 — Règles de filtrage correctes + tests probants | /8 |
| Niv.5 — logrotate configuré + réponses synthèse | /7 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 3

```
Le fichier /var/log/distant/web-server/logger.log reçoit les messages générés par la commande
`logger` (programme = "logger"). Les 4 messages doivent apparaître sauf si les filtres de
niveau 7 ont déjà été mis en place.
```

## Correction Niveau 4

```
Règle 3 (stop sur debug) : le message "daemon.debug" ayant severity=7 est arrêté
avant d'être transmis au réseau. La commande grep ne doit donc rien trouver.
Si le grep trouve le message → la règle 3 n'est pas dans le bon ordre (le "stop"
doit précéder les règles d'envoi réseau) ou il y a une erreur de syntaxe.
```

## Correction Niveau 5

```
5.5 Réponses :
- TCP (@@) : accusé de réception, pas de perte de paquets vs UDP
- Si serveur indisponible : ActionQueueType=LinkedList permet de mettre en file
  d'attente les messages jusqu'à 100 000 entrées → envoi dès que le serveur revient
- Surveillance temps réel : tail -f /var/log/distant/web-server/sshd.log
                             ou multitail /var/log/distant/*/*
- Vérifier le pare-feu : ufw status | grep 514
                          ou iptables -L -n | grep 514
                          ou ss -ulnp | grep 514
```

---

*TP Syslog + Correction — BAC PRO CIEL | E31 Administration Systèmes | 2ᵉ année S11*
*Document Portfolio E31 — Compétences S5.2 · S5.3 · S5.4 · S5.5 · C2.4*
