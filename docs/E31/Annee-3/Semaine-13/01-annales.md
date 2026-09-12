# 📄 ANNALES COMMENTÉES — S13 ANNÉE 3 – E31
## Supervision + Haute Disponibilité : 3 Sujets Types avec Analyse des Pièges

**Nom : ________________  Prénom : ________________**

---

> **Mode d'utilisation :** Chaque annale est d'abord traitée en conditions d'examen (20–25 min), puis corrigée collectivement avec l'analyse des pièges. Les annotations `[PIÈGE]`, `[CLASSIQUE]` et `[EXPERT]` signalent les points d'attention.

---

# ═══════════════════════════════════════════
# ANNALE 1 — SUPERVISION NAGIOS
# ═══════════════════════════════════════════

**⏱️ Durée suggérée : 20 min — Barème : 20 pts**

---

## Contexte

> Vous êtes administrateur réseau chez **MédiaGroup**, un groupe de presse avec 3 serveurs à superviser. Nagios est installé sur `SRV-NAGIOS (192.168.1.50)`. Les paramètres généraux sont : `max_check_attempts=3`, `normal_check_interval=5`, `retry_check_interval=1`.

---

## Partie 1 — Connaissances Nagios (8 pts)

**1.1 *(1 pt)*** — Expliquez la différence entre un état **Soft State** et un état **Hard State** dans Nagios.

_________________________________________________________________________
_________________________________________________________________________

**1.2 *(2 pts)*** — Un service tombe à **09h00**. Combien de minutes s'écoulent avant que la première alerte soit envoyée ? Montrez le déroulement étape par étape.

```
09h00 : Check → _______ → état : Soft  (Tentative 1/3)
+___min : Check → _______ → état : Soft  (Tentative 2/3)
+___min : Check → _______ → état : HARD → Alerte envoyée ✅ (Tentative 3/3)
Heure de la 1ère alerte : _______
Délai total : _____ minutes
```

**1.3 *(1 pt)*** — `[PIÈGE]` Un stagiaire dit : "J'ai mis `exit 2` dans mon plugin pour signaler un problème mineur — les utilisateurs appelleront si c'est grave." Qu'est-ce qui ne va pas dans ce raisonnement ?

_________________________________________________________________________
_________________________________________________________________________

**1.4 *(2 pts)*** — Décrivez le contenu minimal d'un bloc `define host {}` valide dans Nagios. Citez au moins 5 directives avec leur rôle.

| **Directive** | **Rôle** |
|---|---|
| | |
| | |
| | |
| | |
| | |

**1.5 *(2 pts)*** — `[CLASSIQUE]` Vous exécutez manuellement un plugin :

```bash
$ /usr/lib/nagios/plugins/check_http -H 192.168.1.10 -p 80
CRITICAL - Unable to open TCP socket
$ echo $?
2
```

Mais dans le dashboard Nagios, le service HTTP est affiché **OK**. Citez 2 explications possibles.

1. _______________________________________________________________________
2. _______________________________________________________________________

---

## Partie 2 — Configuration Nagios (7 pts)

### Contexte additionnel

> MédiaGroup supervise `SRV-PROD (192.168.1.10)` avec les services suivants : ping de disponibilité, vérification SSH (port 22), et espace disque (avertissement à 75%, critique à 90%).

**2.1 *(2 pts)*** — Rédigez la définition complète du host `SRV-PROD` :

```nagios
define host {
    use                  _______________
    host_name            _______________
    alias                _______________
    address              _______________
    max_check_attempts   _______________
    check_interval       _______________
    contacts             _______________
    notification_options _______________
}
```

**2.2 *(2 pts)*** — Rédigez la définition du service de vérification SSH (port 22) sur `SRV-PROD` :

```nagios
define service {
    use                  _______________
    host_name            _______________
    service_description  _______________
    check_command        _______________
    check_interval       _______________
    contacts             _______________
}
```

**2.3 *(1 pt)*** — Quelle commande Nagios vérifie l'espace disque ? Écrivez-la avec les seuils 75%/90% :

```bash
check_command  check_disk!_______________!_______________
```

**2.4 *(1 pt)*** — Après avoir modifié la configuration, quelles sont les **deux étapes obligatoires** avant que Nagios prenne en compte les changements ?

1. _______________________________________________________________________
2. _______________________________________________________________________

**2.5 *(1 pt)*** — `[PIÈGE]` La directive `check_command check_ssh` retourne UNKNOWN avec le message "Could not connect to 192.168.1.10 on port 22". Nagios envoie une alerte UNKNOWN. Quelle vérification simple permet de déterminer si c'est un problème Nagios ou un problème réseau ?

_________________________________________________________________________

---

## Partie 3 — Supervision IoT (5 pts)

### Plugin custom pour capteur IoT

> Le capteur IoT `192.168.5.20` expose une API REST : `GET /api/humidity` → JSON `{"humidity": 68.5}`. Seuil WARNING : 70%, CRITICAL : 85%.

**3.1 *(3 pts)*** — Rédigez le script bash `check_humidity.sh` complet, avec les codes retour corrects et la ligne de performance data :

```bash
#!/bin/bash
# Usage : check_humidity.sh <host> <warning> <critical>

HOST=$1
WARN=$2
CRIT=$3

HUMIDITY=$(curl -s "http://$HOST/api/humidity" | grep -o '"humidity":[0-9.]*' | grep -o '[0-9.]*')

if [ -z "$HUMIDITY" ]; then
    echo "_______________________________________________"
    exit ___
fi

# Vérifier les seuils (entiers : utiliser awk pour la comparaison float)
if awk "BEGIN {exit !($HUMIDITY >= $CRIT)}"; then
    echo "HUMIDITY _______ - ${HUMIDITY}% | _______________"
    exit ___
elif awk "BEGIN {exit !($HUMIDITY >= $WARN)}"; then
    echo "HUMIDITY _______ - ${HUMIDITY}% | _______________"
    exit ___
else
    echo "HUMIDITY OK - ${HUMIDITY}% | _______________"
    exit ___
fi
```

**3.2 *(1 pt)*** — Indiquez quelle entrée `define command {}` dans Nagios permet d'utiliser ce plugin avec 3 arguments :

```nagios
define command {
    command_name  check_humidity
    command_line  $_______________ -H $HOSTADDRESS$ -w $_______________ -c $_______________
}
```

**3.3 *(1 pt)*** — `[EXPERT]` Si ce plugin retourne parfois UNKNOWN alors que le capteur est fonctionnel, quel paramètre Nagios peut limiter les fausses alertes liées aux timeouts réseau ponctuels ?

_________________________________________________________________________

---

# ═══════════════════════════════════════════
# ANNALE 2 — HAUTE DISPONIBILITÉ
# ═══════════════════════════════════════════

**⏱️ Durée suggérée : 20 min — Barème : 20 pts**

---

## Contexte

> **GlobalTrans** est une société logistique avec un siège à Nantes et une agence à Rennes. Le LAN Nantes est `10.50.1.0/25`. Deux routeurs assurent la redondance : `R-N1 (prio 120)` et `R-N2 (prio 90)`. IP virtuelle HSRP : `10.50.1.126`. Le WAN de R-N1 est tracké avec décrement 35.

---

## Partie 1 — HSRP : États et Bascule (10 pts)

**1.1 *(1 pt)*** — Qui est routeur Active au démarrage ? Comment le vérifier en une commande ?

_________________________________________________________________________

**1.2 *(2 pts)*** — `[CLASSIQUE]` Voici la sortie `show standby` sur R-N1 lors d'un audit :

```
GigabitEthernet0/0 - Group 1
  State is Active
  Virtual IP address is 10.50.1.126
  Active virtual MAC address is 0000.0c07.ac01
  Hello time 3 sec, hold time 10 sec
  Preemption disabled
  Active router is local
  Standby router is 10.50.1.2, priority 90
  Priority 120 (configured 120)
    Track interface GigabitEthernet0/1 state Up decrement 35
```

Identifiez **deux problèmes de configuration** dans cette sortie et expliquez leurs conséquences :

Problème 1 : _______________________________________________________________
Conséquence : ______________________________________________________________

Problème 2 : _______________________________________________________________
Conséquence : ______________________________________________________________

**1.3 *(2 pts)*** — `[PIÈGE]` R-N1 subit une panne électrique complète à 15h00. Les timers sont ceux affichés ci-dessus (Hello=3s, Hold=10s). Combien de secondes R-N2 met-il pour détecter la panne et prendre le rôle Active ? Expliquez le mécanisme précis.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**1.4 *(2 pts)*** — `[CLASSIQUE]` Le responsable IT vous demande de réduire le délai de bascule à maximum 2 secondes. Proposez des timers qui respectent la règle `Hold ≥ 3 × Hello` et écrivez la commande IOS correspondante. Mentionnez le risque.

```
Hello = _____ ms, Hold = _____ ms  (règle : _____ ≥ 3 × _____ = _____ ✅)
```

```ios
R-N1(config-if)# _____________________________________________
R-N2(config-if)# _____________________________________________
```

Risque : ________________________________________________________________

**1.5 *(1 pt)*** — `[PIÈGE]` Après la panne de R-N1, R-N2 est devenu Active. R-N1 revient 30 minutes plus tard. Que se passe-t-il selon la configuration actuelle (preemption disabled) ?

_________________________________________________________________________
_________________________________________________________________________

**1.6 *(2 pts)*** — Corrigez la configuration de R-N1 pour résoudre les deux problèmes identifiés en 1.2 :

```ios
R-N1(config)# interface GigabitEthernet0/0
R-N1(config-if)# _____________________________________________   ! Correction problème 1
R-N1(config-if)# _____________________________________________   ! Résultat attendu : preempt + timers optimisés
```

---

## Partie 2 — VRRP et Interopérabilité (4 pts)

**2.1 *(1 pt)*** — GlobalTrans achète un routeur Fortinet pour remplacer R-N2. HSRP fonctionne-t-il entre R-N1 (Cisco) et le nouveau Fortinet ? Quelle alternative recommandez-vous ?

_________________________________________________________________________
_________________________________________________________________________

**2.2 *(1 pt)*** — Dans VRRP, le routeur prioritaire s'appelle **Master** (et non Active comme en HSRP). Donnez l'équivalent VRRP des deux commandes HSRP suivantes :

| **HSRP** | **VRRP** |
|---|---|
| `standby 1 ip 10.50.1.126` | |
| `standby 1 priority 120` | |

**2.3 *(2 pts)*** — `[EXPERT]` En VRRP, la préemption est activée par défaut. Expliquez une situation où il serait préférable de la **désactiver** sur un routeur nouvellement ajouté.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

## Partie 3 — Bilan Architecture HA (6 pts)

**3.1 *(2 pts)*** — GlobalTrans envisage d'installer HSRP sur ses routeurs WAN (vers Internet) en plus du LAN. Expliquez pourquoi cela serait différent du HSRP LAN et quels mécanismes complémentaires seraient nécessaires.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**3.2 *(2 pts)*** — `[CLASSIQUE]` Vous vérifiez la table ARP du switch SW-CORE après une bascule HSRP. L'entrée pour l'IP virtuelle `10.50.1.126` pointe encore vers le MAC de R-N1. Quel mécanisme HSRP met à jour cette entrée automatiquement ? Quel problème survient si ce mécanisme échoue ?

_________________________________________________________________________
_________________________________________________________________________

**3.3 *(2 pts)*** — `[INTÉGRATION]` Vous devez superviser la bascule HSRP avec Nagios. Proposez une approche concrète : quel check configurer pour détecter si le routeur Active prévu (`R-N1`) n'est plus Active ?

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

# ═══════════════════════════════════════════
# ANNALE 3 — CAS INTÉGRÉ : SUPERVISION + HA
# ═══════════════════════════════════════════

**⏱️ Durée suggérée : 20 min — Barème : 20 pts**

---

## Contexte

> **AirLogix** est un opérateur de fret aérien. Son infrastructure réseau est critique : une interruption de service peut bloquer des opérations aéroportuaires. Vous intervenez en audit post-incident.

---

## Incident Report

```
Date       : Jeudi 12 mars à 02h47
Durée      : 23 minutes de coupure totale
Symptômes  : Toutes les agences ont perdu l'accès au serveur central
             Nagios n'a pas envoyé d'alerte
Impact     : 4 vols retardés, perte estimée 80 000€
```

```
Logs Nagios (extrait) :
[1710208020] SERVICE ALERT: R-CORE1;Ping;CRITICAL;SOFT;1;...
[1710208080] SERVICE ALERT: R-CORE1;Ping;CRITICAL;SOFT;2;...
[1710208140] SERVICE ALERT: R-CORE1;Ping;CRITICAL;SOFT;3;...
[1710208200] SERVICE ALERT: R-CORE1;Ping;CRITICAL;HARD;3;...
[1710208200] SERVICE NOTIFICATION: admin-on-call;...EMAIL SENT
```

```
show standby brief (relevé à 03h00, panne déjà résolue) :
Interface  Grp  Pri P State   Active         Standby   Virtual IP
Gi0/0      1    80  P Standby 10.0.1.2       local     10.0.1.254

show standby (R-CORE1) :
  Priority 80 (configured 120)
    Track interface GigabitEthernet0/1 state Down decrement 40
```

---

## Questions

**INT1 *(3 pts)*** — À partir des logs Nagios, calculez l'heure exacte à laquelle la première alerte email a été envoyée. Les timestamps sont en UNIX (secondes depuis 1970/01/01). Montrez votre raisonnement.

```
1er check CRITICAL : 1710208020 → 02h47:00
2ème check : + _____ s → _______
3ème check : + _____ s → _______
Hard State + email : 1710208200 → _______
Délai entre incident et alerte : _____ minutes
```

**INT2 *(2 pts)*** — Nagios a bien envoyé une alerte à 03h10. Pourtant l'incident a duré 23 minutes sans intervention. Proposez 2 explications pour ce délai entre l'alerte et la résolution.

1. _______________________________________________________________________
2. _______________________________________________________________________

**INT3 *(3 pts)*** — `[INTÉGRATION]` Analysez l'état HSRP de R-CORE1 (priorité 80, interface WAN Down, decrement 40). Reconstituez la chronologie de la bascule HSRP :

```
Priorité R-CORE1 configurée : _____
Décrement appliqué : _____
Priorité après panne WAN : _____
Priorité R-CORE2 (déduite) : > _____ → _____ semble être _____

Bascule : R-CORE1 (prio _____) → R-CORE2 Active ? OUI/NON
Preempt sur R-CORE1 : OUI (P visible) → R-CORE1 reprendra Active si WAN revient ? OUI/NON
```

**INT4 *(3 pts)*** — `[PIÈGE]` L'admin dit : "Nagios a fonctionné puisqu'il a envoyé l'alerte. Le problème c'est HSRP." Le RSSI dit : "HSRP a fonctionné puisque R-CORE2 a pris le relais. Le problème c'est Nagios." Qui a raison ? Quelle est la vraie cause de l'interruption de 23 minutes ?

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**INT5 *(3 pts)*** — Pour éviter la répétition de cet incident, proposez 3 améliorations concrètes avec la technologie/commande associée :

| **Amélioration** | **Technologie / Commande** |
|---|---|
| Réduire le délai d'alerte Nagios de 3 min à < 1 min | |
| Réduire le délai de bascule HSRP de 10s à < 3s | |
| Alerter si R-CORE1 n'est plus Active HSRP (et non juste si le ping échoue) | |

**INT6 *(3 pts)*** — `[EXPERT]` Rédigez le check Nagios custom qui détecte si R-CORE1 est en état Standby (alors qu'il devrait être Active). Le check doit se connecter en SSH à R-CORE1, exécuter `show standby brief`, et retourner CRITICAL si R-CORE1 n'est pas Active.

```bash
#!/bin/bash
# check_hsrp_state.sh

HOST=$1
EXPECTED_STATE="Active"

RESULT=$(ssh -o StrictHostKeyChecking=no nagios@$HOST \
         "show standby brief" 2>/dev/null | grep "Gi0/0" | awk '{print $5}')

if [ -z "$RESULT" ]; then
    echo "UNKNOWN - Cannot connect or parse HSRP state"
    exit ___
fi

if [ "$RESULT" = "$EXPECTED_STATE" ]; then
    echo "HSRP OK - R-CORE1 is $_______________ (expected)"
    exit ___
else
    echo "HSRP CRITICAL - R-CORE1 is $_______________ (expected: _______________)"
    exit ___
fi
```

**INT7 *(3 pts)*** — `[SYNTHÈSE]` Rédigez une recommandation de 4 phrases destinée au RSSI d'AirLogix expliquant la relation entre supervision et haute disponibilité, et pourquoi les deux sont nécessaires même si chacune fonctionne individuellement.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
