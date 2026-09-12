# 🎓 GUIDE DE POURSUITE D'ÉTUDES
## BTS CIEL / BTS SIO — Ce qui vous Attend, Ce que Vous Savez Déjà, Comment Préparer l'Été

**Nom : ________________  Prénom : ________________**

---

> *Ce guide est votre feuille de route pour la période entre la fin du BAC PRO et le début du BTS. Gardez-le.*

---

## PARTIE 1 — LE PAYSAGE DES FILIÈRES

### Vue d'ensemble

```
BAC PRO CIEL
    │
    ├──► BTS CIEL (Cybersécurité, Informatique et réseaux Électronique et communication)
    │       Spécialités : IR (Informatique et Réseaux) / EC / ER
    │
    ├──► BTS SIO (Services Informatiques aux Organisations)
    │       Options : SISR (Systèmes et réseaux) / SLAM (Développement)
    │
    ├──► LP Informatique / Réseaux (Université — après BTS de préférence)
    │
    ├──► Bachelor Informatique (Écoles — 3 ans post-BAC)
    │
    └──► Entrée directe en entreprise (alternance, contrat pro)
```

---

## PARTIE 2 — BTS CIEL : CE QUI VOUS ATTEND

### Vue d'ensemble

| **Critère** | **BAC PRO CIEL** | **BTS CIEL** |
|---|---|---|
| Durée | 3 ans (dont stages) | **2 ans** (dont stages = 10–12 semaines) |
| Niveau | Bac (Niveau 4) | **Bac+2 (Niveau 5)** |
| Rythme | Alterné (apprentissage) | Scolaire ou apprentissage |
| Dominante | Pratique guidée | **Conception + autonomie** |
| Projet | Mini-projets | **Projet annuel structurant** |
| Examen | Épreuve pratique + oral | Épreuves écrites + E6 (rapport de stage) |

---

### Matières E31 → BTS CIEL : Ce que vous avez déjà

| **Compétence BTS CIEL IR** | **Vous avez déjà en E31** | **Ce qui est nouveau** |
|---|---|---|
| Routage avancé (OSPF, BGP, EIGRP) | OSPF v2/v3, multi-area ✅ | BGP (inter-AS), EIGRP, redistribution |
| Haute disponibilité réseau | HSRP, VRRP, STP ✅ | GLBP, VSS, chassis stacking |
| VPN et tunneling | IPsec site-à-site, DMVPN ✅ | SSL VPN, MPLS L3VPN |
| Supervision | Nagios, plugins, SNMP notions ✅ | Zabbix, Prometheus, Grafana, ELK |
| Sécurité périmétrique | ACL étendues ✅ | Firewall stateful, IDS/IPS, WAF |
| Infrastructure cloud | AWS VPC, Azure vNET ✅ | Terraform, Ansible, CI/CD réseau |
| IPv6 | EUI-64, DHCPv6, OSPFv3 ✅ | Segments de migration complexes |
| Virtualisation réseau | VXLAN, SD-WAN concepts ✅ | NSX, ACI, OpenStack Neutron |

> **Estimation de votre avance :** Un bachelier CIEL E31 maîtrisé correspond à environ **30–40% du programme réseau BTS CIEL IR**. Vous démarrez avec 6 mois d'avance sur vos camarades venant d'autres BAC PRO.

---

### Les matières nouvelles en BTS CIEL

| **Matière** | **Ce que vous y verrez** | **Lien avec E31** |
|---|---|---|
| **Mathématiques** | Algèbre de Boole, logique combinatoire, notions de cryptographie | Bases pour comprendre AES, RSA |
| **Anglais technique** | Documentation Cisco en anglais, RFC, certifications | Vous avez déjà lu des RFC en cours |
| **Gestion de projet** | Méthode Agile/Scrum, planification, livrables | Le "plan de test" de S17-A2 était déjà ça |
| **Cybersécurité** | Pentest bases, OWASP, SIEM, analyse de logs | Lien direct avec ACL et supervision |
| **BGP** | Protocole inter-AS, attributs, politiques de routage | Extension d'OSPF — même logique SPF |
| **Scripting / Automatisation** | Python Netmiko/Paramiko, Ansible, API REST | check_temp.sh de Nagios → Python |

---

## PARTIE 3 — BTS SIO : OPTIONS SISR ET SLAM

### Option SISR (Systèmes et Réseaux)

> C'est l'option la plus proche d'E31. Elle forme des techniciens capables de déployer, administrer et sécuriser des infrastructures informatiques complètes.

| **Compétence SISR** | **Déjà acquis en E31** | **Nouveau** |
|---|---|---|
| Administration systèmes (Linux/Windows Server) | Nagios sur Linux ✅ | Active Directory, DNS/DHCP serveur, GPO |
| Réseau (commutation, routage, VPN) | Tout OSPF, HSRP, VPN ✅ | Équipements HP/Juniper, firewall Palo Alto |
| Supervision | Nagios ✅ | Zabbix, PRTG, SIEM |
| Virtualisation | Notions cloud ✅ | VMware, Hyper-V, Proxmox |
| Sécurité | ACL, VPN, Wi-Fi WPA2/WPA3 ✅ | Hardening, SIEM, incident response |

### Option SLAM (Solutions Logicielles et Applications Métiers)

> Moins axée réseau, davantage développement. Pertinent si vous avez de la curiosité pour le scripting ou le développement.

| **Ce que vous apporterez** | **Ce qui sera très nouveau** |
|---|---|
| Logique de réseau (APIs REST utilisées dans les plugins Nagios) | Développement web, bases de données |
| Scripts bash (Nagios plugins) | Python, Java, SQL, frameworks |
| Méthode de test (plans de test S17-A2) | Tests unitaires, CI/CD |

---

### BTS SIO vs BTS CIEL — Que choisir ?

| **Si vous...** | **Choisissez** |
|---|---|
| Adorez configurer des routeurs et des switches | BTS CIEL IR |
| Voulez une formation plus large (réseau + systèmes + sécurité) | BTS SIO SISR |
| Avez une curiosité pour le développement en plus du réseau | BTS SIO SLAM ou BTS CIEL avec ouverture |
| Visez une poursuite en LP ou école d'ingénieur réseau | BTS CIEL IR puis LP |
| Voulez le plus d'employabilité possible | BTS SIO SISR (spectre très large) |

---

## PARTIE 4 — TD : CE QUE VOUS SAVEZ DÉJÀ POUR LE BTS

> Pour chaque thème BTS, évaluez votre niveau et identifiez ce qui est nouveau.

### TD "Mapping E31 → BTS"

**Sujet 1 — Routage BGP (BTS CIEL A1)**

> Le professeur de BTS vous dit : "BGP est le protocole de routage inter-domaines. Il fonctionne entre Autonomous Systems (AS) distincts — par exemple entre un opérateur télécom et une entreprise cliente."

**Q1.** En quoi BGP ressemble-t-il à OSPF dans son principe de base (échange d'informations de routage) ? En quoi est-il fondamentalement différent (ce qu'il optimise) ?

_________________________________________________________________________
_________________________________________________________________________

**Q2.** Dans E31, vous avez utilisé OSPF pour annoncer des routes entre vos routeurs. En BTS, BGP sera utilisé pour annoncer des préfixes IP entre opérateurs. Le même principe de "table de routage" s'applique. Quelles commandes IOS de vérification vous semblent transposables ?

_________________________________________________________________________

---

**Sujet 2 — Ansible (BTS SIO/CIEL A2)**

> En BTS, vous configurerez des équipements via Ansible plutôt qu'en tapant les commandes manuellement. Un playbook Ansible pour configurer OSPF ressemble à ceci :

```yaml
- hosts: routers
  tasks:
    - name: Configure OSPF
      ios_config:
        lines:
          - router ospf 1
          - router-id 1.1.1.1
          - network 10.0.0.0 0.0.0.255 area 0
```

**Q3.** Vous reconnaissez les commandes IOS dans ce playbook. Que fait ce code par rapport à ce que vous feriez manuellement en SSH ?

_________________________________________________________________________

**Q4.** Quel avantage voit-on immédiatement pour une infrastructure de 50 routeurs à configurer ?

_________________________________________________________________________

---

**Sujet 3 — Zabbix vs Nagios (BTS SIO SISR)**

> En BTS, vous utiliserez Zabbix (ou Grafana/Prometheus) plutôt que Nagios. Voici une comparaison :

| **Critère** | **Nagios (connu)** | **Zabbix (BTS)** |
|---|---|---|
| Config | Fichiers .cfg texte | Interface web graphique |
| Agents | Plugins scripts | Agents Zabbix sur les hôtes |
| Alertes | Email/SMS via scripts | Email/SMS/Slack/Teams natif |
| Dashboards | Limité | Graphes et dashboards avancés |
| SNMP | Via plugin | Natif et intégré |

**Q5.** Les concepts que vous connaissez (host, service, seuils WARNING/CRITICAL, Hard State) existent-ils en Zabbix ? Quel est leur équivalent ?

_________________________________________________________________________
_________________________________________________________________________

**Q6.** Le principe des plugins Nagios (`exit 0/1/2/3` + perf data) se retrouve-t-il dans Zabbix ? Sous quelle forme ?

_________________________________________________________________________

---

**Sujet 4 — Active Directory (BTS SIO SISR A1)**

> Le premier trimestre de BTS SIO SISR introduit Windows Server et Active Directory. Un réseau AD ajoute des services que vous n'avez pas vus en E31 : DNS interne, DHCP centralisé, authentification centralisée (Kerberos), stratégies de groupe (GPO).

**Q7.** En E31, vous avez vu la supervision Wi-Fi avec 802.1X et RADIUS (S8-A2). Quel lien existe-t-il entre RADIUS et Active Directory dans une infrastructure d'entreprise réelle ?

_________________________________________________________________________
_________________________________________________________________________

---

**Sujet 5 — Cybersécurité — Pentest (BTS CIEL A2)**

> En BTS, vous réaliserez des audits de sécurité basiques (scan de ports, détection de vulnérabilités). Voici un exemple d'output Nmap :

```
PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   open   http
443/tcp  open   https
3306/tcp open   mysql
3389/tcp closed rdp
```

**Q8.** Avec votre connaissance des ACL E31, identifiez deux ports qui devraient être bloqués en entrée depuis Internet dans une politique de filtrage standard. Justifiez.

Port 1 : _________ Raison : _____________________________________________
Port 2 : _________ Raison : _____________________________________________

**Q9.** Si un firewall avait une ACL similaire à celle que vous avez appris (permit HTTPS depuis Internet, deny tout le reste), quel port ci-dessus resterait ouvert ? Est-ce intentionnel ou une erreur ?

_________________________________________________________________________

---

## PARTIE 5 — COMMENT PRÉPARER L'ÉTÉ

### Le plan optimal : 3 phases sur 8 semaines

**Phase 1 — Consolidation (Semaines 1–3)**

> Objectif : ne pas oublier ce que vous avez appris.

```
□ Refaire 1 lab Packet Tracer complet par semaine (topologie simple)
  → Semaine 1 : OSPF + HSRP
  → Semaine 2 : VPN IPsec + ACL
  → Semaine 3 : Nagios + IPv6

□ Lire les RFC fondamentales (15 min/jour)
  → RFC 2328 (OSPF) → Parcourir l'intro seulement
  → RFC 5798 (VRRP) → 2 pages
  → RFC 4862 (SLAAC) → Section 5

□ Pratiquer l'anglais technique
  → Lire la documentation Cisco en anglais (cisco.com/c/en/us/td/...)
  → Regarder des vidéos CBT Nuggets ou NetworkChuck sur YouTube
```

**Phase 2 — Découverte BTS (Semaines 4–6)**

> Objectif : ne pas arriver en terra incognita.

```
□ BGP en autodidacte (8h)
  → Regarder : "BGP for Beginners" — David Bombal (YouTube)
  → Lire : RFC 4271 intro (4 pages)
  → Exercice : topologie PT avec 2 AS et BGP entre eux

□ Python réseau (6h)
  → Installer Python 3
  → Faire les 20 premiers exercices de "Automate the Boring Stuff"
  → Tenter un script qui ping une liste d'IPs et log le résultat

□ Scripting Ansible (4h)
  → Installer Ansible sur Linux (ou WSL2)
  → Suivre le tutoriel officiel "Getting started with Ansible"
  → Écrire un playbook qui configure 2 routeurs PT via Netmiko

□ Linux admin (4h)
  → OverTheWire : Bandit (niveaux 0–10)
  → Commandes : grep, awk, sed, find, chmod, crontab
```

**Phase 3 — Projets personnels (Semaines 7–8)**

> Objectif : avoir quelque chose à montrer lors du premier cours BTS.

```
□ Option A — Lab home avec GNS3/EVE-NG
  → Monter une infrastructure virtuelle : 3 routeurs + OSPF + HSRP + VPN
  → Documenter avec un schéma réseau professionnel

□ Option B — Certifications débutantes (gratuites ou peu coûteuses)
  → Cisco NetAcad : "Introduction to Networks" (CCNA 1 — gratuit)
  → NDG Linux Essentials (gratuit sur NetAcad)
  → Google IT Support Certificate (Coursera — bases systèmes)

□ Option C — Projet Raspberry Pi réseau
  → Pi-hole (DNS filtrant sur le réseau domestique)
  → WireGuard VPN personnel (alternative moderne à IPsec)
  → Superviser avec Grafana + Prometheus
```

---

## PARTIE 6 — RESSOURCES RECOMMANDÉES

### Pour renforcer le niveau E31

| **Ressource** | **Type** | **Coût** | **Pour quoi** |
|---|---|---|---|
| Packet Tracer (Cisco NetAcad) | Logiciel + cours | Gratuit | Pratiquer OSPF, HSRP, VPN |
| GNS3 + images IOS | Logiciel | Gratuit | Lab plus réaliste |
| David Bombal (YouTube) | Vidéo | Gratuit | Cisco, Python réseau, SD-WAN |
| NetworkChuck (YouTube) | Vidéo | Gratuit | Linux, Docker, Wi-Fi |
| Jeremy's IT Lab (YouTube) | Vidéo | Gratuit | CCNA complet, très pédagogique |

### Pour préparer le BTS

| **Ressource** | **Type** | **Coût** | **Pour quoi** |
|---|---|---|---|
| Cisco NetAcad CCNA 1–3 | Cours en ligne | Gratuit | BGP, OSPF avancé, sécurité |
| TryHackMe | Plateforme gamifiée | Gratuit/Payant | Cybersécurité pratique |
| Automate the Boring Stuff (Python) | Livre/Web | Gratuit | Python pour débutants |
| Ansible Documentation | Doc officielle | Gratuit | Automatisation réseau |
| OverTheWire : Bandit | CTF | Gratuit | Linux et scripting |
| Zabbix Documentation | Doc officielle | Gratuit | Supervision avancée |

### Certifications accessibles après le BAC PRO CIEL

| **Certification** | **Niveau** | **Valeur** | **Conseil** |
|---|---|---|---|
| **Cisco CCNA** | Intermédiaire | ⭐⭐⭐⭐⭐ | La référence industrie — visez après 6 mois de BTS |
| **CompTIA Network+** | Débutant | ⭐⭐⭐ | Bonne base, moins reconnu que CCNA en France |
| **CompTIA Security+** | Débutant-inter | ⭐⭐⭐⭐ | Si cybersécurité vous attire |
| **AWS Cloud Practitioner** | Débutant | ⭐⭐⭐ | Si cloud vous attire — examen 1h |
| **Fortinet NSE 1–3** | Débutant | ⭐⭐ | Gratuit, rapide, bon complément |

---

**Document – BAC PRO CIEL – A3 – E31/U31 – Version 1.0 – 2026**
