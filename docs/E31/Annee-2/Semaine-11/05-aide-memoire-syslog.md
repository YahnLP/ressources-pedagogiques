# 🗂️ AIDE-MÉMOIRE SYSLOG / RSYSLOG — À PLASTIFIER
## Centralisation logs · Filtres · logrotate · SIEM · BAC PRO CIEL · E31 · 2ᵉ année S11

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 📋 Format d'un message Syslog

```
Jan 15 03:12:44  web-server  sshd[1234]: Failed password for root
   │                │             │              │
   └─ Horodatage    └─ Hostname   └─ Prog[PID]  └─ Message
```

---

## 🔢 Facility & Severity — Les plus importants

```
FACILITY (qui génère) :       SEVERITY (gravité) :
  0 = kern   (noyau)            0 = emerg   🔴 système inutilisable
  1 = user                      1 = alert   🔴 action immédiate
  2 = mail                      2 = crit    🟠 condition critique
  3 = daemon (services)         3 = err     🟠 erreur
  4 = auth   ← authentif.       4 = warning 🟡 avertissement
 16 = local0  ← usage libre     5 = notice  🔵 notable
 …                              6 = info    ⚪ information
 23 = local7                    7 = debug   ⚪ débogage

PRI = (Facility × 8) + Severity
```

---

## ⚙️ Configurer le serveur rsyslog

```bash
# /etc/rsyslog.d/10-server.conf
module(load="imudp")
input(type="imudp" port="514")
module(load="imtcp")
input(type="imtcp" port="514")

template(name="RemoteLogs" type="string"
  string="/var/log/distant/%HOSTNAME%/%PROGRAMNAME%.log")

if $FROMHOST-IP != "127.0.0.1" then {
    action(type="omfile" DynaFile="RemoteLogs"
           dirCreateMode="0755" FileCreateMode="0644")
    stop
}
```

---

## 📡 Configurer le client (forwarding)

```bash
# /etc/rsyslog.d/50-forwarding.conf
*.* @@192.168.50.10:514   # TCP (@@) = fiable
*.* @192.168.50.10:514    # UDP (@)  = rapide mais avec perte possible
```

---

## 🎯 Règles de filtrage

```bash
# Par contenu du message
if $msg contains "Failed password" then {
    action(type="omfile" file="/var/log/ssh_attacks.log")
}

# Par severity (critique = ≤ 2)
if $syslogseverity <= 2 then {
    action(type="omfile" file="/var/log/CRITICAL.log")
}

# Ignorer debug
if $syslogseverity == 7 then stop

# Par programme
if $programname == "nginx" then {
    action(type="omfile" file="/var/log/nginx.log")
}

# Selector classique
auth.warning    /var/log/auth_warn.log
*.emerg         @192.168.50.10:514
mail.none        /var/log/messages
```

---

## 🔄 logrotate — Template

```bash
/var/log/distant/*/*.log {
    daily          # ou weekly
    rotate 30      # nombre de fichiers à conserver
    compress       # gzip les anciens fichiers
    delaycompress  # ne pas compresser le dernier (.1)
    missingok      # ne pas échouer si absent
    notifempty     # ne pas tourner si vide
    postrotate
        /usr/lib/rsyslog/rsyslog-rotate
    endscript
}
```

---

## 🧰 Commandes essentielles

```bash
# Vérifier la syntaxe
rsyslogd -N1

# Tester l'envoi d'un message
logger -p auth.warning "Test depuis $(hostname)"

# Voir les logs en temps réel
tail -f /var/log/distant/web-server/sshd.log

# Redémarrer rsyslog
systemctl restart rsyslog

# Vérifier l'écoute réseau
ss -ulnp | grep 514
ss -tlnp | grep 514

# Tester logrotate
logrotate --debug /etc/logrotate.d/rsyslog-distant
logrotate --force /etc/logrotate.d/rsyslog-distant
```

---

## 🔗 Chaîne vers le SIEM

```
Machine → rsyslog local → Serveur rsyslog central → SIEM
              (UDP/TCP 514)        (Forwarding/Beats)

SIEM fait :
  1. Parsing (facility, severity, IP, prog…)
  2. Corrélation (5 Failed password en 10s → alerte)
  3. Alerte automatique
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| Port 514 fermé sur le pare-feu | `ufw allow 514/tcp` et `514/udp` |
| `stop` avant l'action → message perdu | Placer `stop` APRÈS les `action()` |
| Pas de `mkdir /var/log/distant` | Créer le répertoire avant de tester |
| UDP = perte possible | Utiliser `@@` (TCP) en production |
| Pas de logrotate → disque plein | Toujours configurer logrotate sur un serveur de logs |

---

*Aide-Mémoire Syslog/rsyslog — À plastifier*
*BAC PRO CIEL | E31 Administration Systèmes | 2ᵉ année S11*
*Compétences S5.1 · S5.2 · S5.3 · S5.4 · S5.5 · C2.4*
