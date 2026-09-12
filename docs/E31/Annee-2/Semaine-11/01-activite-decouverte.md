# 🔍 ACTIVITÉ DE DÉCOUVERTE — S11 · 2ᵉ ANNÉE · E31
## « Retrouver l'intrus » — Lire des logs système sans formation préalable

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement (pas d'ordinateur)
> **Principe** : Tu reçois un extrait de logs système d'un serveur Linux. Sans jamais avoir étudié Syslog, tu dois reconstituer ce qui s'est passé la nuit dernière.

---

## 🎯 Mise en situation

> Il est 9h du matin. Tu arrives au bureau et ton responsable t'accueille :
> *"Notre serveur web a été compromis cette nuit. L'attaquant a effacé les logs locaux MAIS
> nos logs sont centralisés sur un serveur séparé qu'il n'a pas pu atteindre.
> Voici l'extrait du serveur de logs. Dis-moi ce qui s'est passé."*

---

## 📋 Extrait des logs (serveur centralisé)

```
Jan 15 02:58:11 web-server sshd[1201]: Server listening on 0.0.0.0 port 22
Jan 15 03:12:31 web-server sshd[1234]: Invalid user admin from 185.220.101.45 port 52337
Jan 15 03:12:44 web-server sshd[1234]: Failed password for root from 185.220.101.45 port 52341 ssh2
Jan 15 03:12:46 web-server sshd[1234]: Failed password for root from 185.220.101.45 port 52342 ssh2
Jan 15 03:12:48 web-server sshd[1234]: Failed password for root from 185.220.101.45 port 52343 ssh2
Jan 15 03:12:49 web-server sshd[1234]: Failed password for admin from 185.220.101.45 port 52344 ssh2
Jan 15 03:12:50 web-server sshd[1234]: Failed password for admin from 185.220.101.45 port 52345 ssh2
Jan 15 03:12:52 web-server sshd[1234]: Failed password for deploy from 185.220.101.45 port 52347 ssh2
Jan 15 03:13:05 web-server sshd[1235]: Accepted password for deploy from 185.220.101.45 port 52350 ssh2
Jan 15 03:13:07 web-server sudo[2341]: deploy : TTY=pts/0 ; PWD=/home/deploy ; USER=root ; COMMAND=/bin/bash
Jan 15 03:13:09 web-server sudo[2342]: pam_unix(sudo:session): session opened for user root
Jan 15 03:14:22 web-server useradd[2356]: new user: name=backdoor, UID=0, GID=0, home=/root
Jan 15 03:14:55 web-server kernel: [UFW BLOCK] IN=eth0 SRC=10.0.0.5 DST=185.220.101.45 LEN=1420
Jan 15 03:15:00 web-server sshd[1235]: Disconnected from user deploy 185.220.101.45 port 52350
Jan 15 03:15:01 web-server sshd[2400]: Connection closed by 185.220.101.45 port 52351
Jan 15 07:45:02 web-server CRON[3001]: (root) CMD (find /var/log -name "*.log" -delete)
Jan 15 07:45:03 web-server syslog: rsyslogd: action 'action-3-builtin:omfile' lost 847 messages
Jan 15 08:01:11 web-server sshd[3100]: Accepted publickey for backdoor from 91.108.4.30 port 44221
```

---

## 🔍 PARTIE 1 — Comprendre le format (8 min)

**Question 1.1** — Chaque ligne a la même structure. Décompose la ligne suivante en identifiant chaque élément :

```
Jan 15 03:12:44   web-server   sshd[1234]   Failed password for root from 185.220.101.45 port 52341 ssh2
   │                │               │                   │
   └─ ?              └─ ?            └─ ?                └─ ?
```

```
"Jan 15 03:12:44" = ___________________________________________________________
"web-server"      = ___________________________________________________________
"sshd[1234]"      = ___________________________________________________________
"Failed password…" = __________________________________________________________
```

**Question 1.2** — À quel moment précis cette séquence de logs a-t-elle eu lieu ? Est-ce un horaire de travail normal ?

```
Heure des événements suspects : entre _______h et _______h
Un opérateur humain était-il vraisemblablement présent ? ☐ Oui ☐ Non
Pourquoi cet horaire est-il stratégiquement choisi par un attaquant ? ____________
```

---

## 🔍 PARTIE 2 — Reconstituer l'attaque chronologiquement (15 min)

**Question 2.1** — Ligne par ligne, que fait l'attaquant depuis l'IP `185.220.101.45` ?

| Heure | Ligne | Ce qui se passe concrètement |
|---|---|---|
| 03:12:31 | Invalid user admin | |
| 03:12:44 à 03:12:52 | Failed password (×7) | |
| 03:13:05 | **Accepted password for deploy** | |
| 03:13:07 | sudo COMMAND=/bin/bash | |
| 03:14:22 | new user: name=backdoor, UID=0 | |
| 03:15:00 | Disconnected | |

**Question 2.2** — À 03:14:22, un utilisateur "backdoor" est créé avec `UID=0` et `GID=0`.
Que signifie UID=0 sous Linux ?

```
UID=0 correspond à l'utilisateur : _______________________________
Conséquence : le compte "backdoor" a les mêmes droits que ________
C'est une technique d'attaque appelée : ___________________________
```

**Question 2.3** — À 07:45:02, une tâche CRON s'exécute : `find /var/log -name "*.log" -delete`
Que fait cette commande ? Qui l'a probablement programmée ?

```
Effet de la commande : _______________________________________________
Programmée par : _____________________________________________________
Objectif de l'attaquant : ____________________________________________
```

**Question 2.4** — À 07:45:03 : `rsyslogd: action lost 847 messages`. Qu'est-ce que ça révèle ?

```
Cela signifie que 847 messages de logs ont été : _________________________
Pourquoi rsyslog le signale-t-il sur le serveur CENTRALISÉ ?
___________________________________________________________________________
Conclusion : l'attaquant a effacé les logs locaux MAIS ______________________
___________________________________________________________________________
```

**Question 2.5** — À 08:01:11 : connexion SSH avec `publickey for backdoor from 91.108.4.30`
Quelle est la différence avec la première connexion ? Pourquoi c'est plus inquiétant ?

```
Première connexion : mot de passe (brute force)
Deuxième connexion : __________________ → cela signifie que l'attaquant a _______
___________________________________________________________________________
L'adresse IP est différente : ____________ vs ____________ → l'attaquant utilise
___________________________________________________________________________
```

---

## 🔍 PARTIE 3 — Ce que révèle la centralisation (7 min)

**Question 3.1** — Si les logs n'avaient PAS été centralisés, aurait-on pu reconstituer cette attaque ?

```
☐ Oui — car ________________________________________________________________
☐ Non — car ________________________________________________________________
```

**Question 3.2** — Cite **3 informations cruciales** que seul le serveur de logs centralisé a permis de récupérer :

```
Information 1 : _______________________________________________________________
Information 2 : _______________________________________________________________
Information 3 : _______________________________________________________________
```

**Question 3.3** — Comment aurait-on pu **détecter** cette attaque AVANT qu'elle réussisse ?

```
Indice : ligne 03:12:44 à 03:12:52 — 7 échecs d'authentification en 8 secondes
Règle d'alerte à créer : ______________________________________________________
Outil qui peut créer cette alerte automatiquement : ____________________________
```

---

## 🏁 Bilan

```
Un message de log syslog contient toujours :
  - La date et l'heure : ________________
  - Le nom de la machine : ______________
  - Le programme source : _______________
  - Le message : ______________________

La centralisation des logs est indispensable car :
  1. ________________________________________________________________________
  2. ________________________________________________________________________

Le serveur qui centralise les logs s'appelle sous Linux : _______________________
```

> ✅ Tu viens d'analyser une vraie attaque depuis des logs bruts.
> Le cours va maintenant te montrer comment configurer le serveur qui aurait collecté ces logs automatiquement.

---

## 📎 Pour l'enseignant — Réponses

**2.2** : UID=0 = root → compte backdoor avec droits root complets = "rootkit via useradd"

**2.3** : Supprime tous les fichiers .log de /var/log → programmé par l'attaquant via crontab → effacement des preuves sur la machine locale

**2.4** : 847 messages perdus (les logs supprimés) → rsyslog local ne peut plus écrire → MAIS les 847 messages avaient DÉJÀ été envoyés au serveur central → preuve préservée

**2.5** : Clé publique SSH = l'attaquant a installé sa clé publique dans ~/.ssh/authorized_keys sur le compte backdoor → accès persistant sans mot de passe + depuis une IP différente (proxy/Tor relay)

**3.3** : Règle : "plus de 5 Failed password depuis la même IP en moins de 30 secondes → alerte" · Outil : SIEM (Wazuh, Splunk, ELK) ou Fail2ban

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Administration Systèmes | 2ᵉ année S11*
*Compétences : S5.1 · S5.5 · C2.3*
