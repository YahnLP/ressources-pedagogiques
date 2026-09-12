{% raw %}
# 📘 FICHE DE COURS — S10 · 3ᵉ ANNÉE · E31
## Automation : Ansible Playbooks · Python Netmiko · Configuration Réseau as Code

---

> **Nom** : ___________________________
> **Date** : ___________________________
> **Compétences travaillées** : S7.1 · S7.2 · S7.3 · C2.2 · C3.1

---

## 🔑 Vocabulaire clé à maîtriser

| Terme | Définition |
|---|---|
| **Infrastructure as Code (IaC)** | Gestion de l'infrastructure (réseau, serveurs) via des fichiers de code versionnés |
| **Ansible** | Outil d'automatisation agentless (sans agent) basé sur des fichiers YAML et SSH |
| **Playbook** | Fichier YAML Ansible décrivant les tâches à exécuter sur les équipements |
| **Inventaire** | Fichier listant les équipements cibles et leurs paramètres de connexion |
| **Task (Tâche)** | Action élémentaire dans un playbook (configurer, lire, copier...) |
| **Module** | Plugin Ansible qui effectue une action spécifique (ios_config, ios_command...) |
| **Idempotence** | Propriété : exécuter N fois = même résultat que 1 fois · pas d'effet si déjà appliqué |
| **YAML** | Yet Another Markup Language — format de fichier lisible, basé sur l'indentation |
| **Netmiko** | Bibliothèque Python SSH multi-vendeur pour automatiser les équipements réseau |
| **ConnectHandler** | Classe Netmiko qui gère la connexion SSH à un équipement réseau |
| **send_config_set()** | Méthode Netmiko pour envoyer des commandes de configuration |
| **send_command()** | Méthode Netmiko pour envoyer une commande show et récupérer la sortie |
| **Agentless** | Sans agent — Ansible se connecte via SSH standard, aucun logiciel à installer sur les cibles |
| **Jinja2** | Moteur de templates Python utilisé dans Ansible pour les variables (`{{ variable }}`) |
| **Git** | Système de contrôle de version — permet de versionner les playbooks et scripts réseau |

---

## 1️⃣ — Pourquoi automatiser le réseau ?

### Le problème de la configuration manuelle

```
Entreprise avec 200 routeurs et une nouvelle règle de sécurité ACL à déployer :

APPROCHE MANUELLE :
  200 sessions SSH ouvertes une par une
  200 fois la même commande tapée
  Temps : ~1 heure · Risque d'erreur : élevé
  Vérification : manuelle, complexe
  Si erreur : identifier laquelle des 200 config est fausse

APPROCHE AUTOMATISÉE :
  1 fichier YAML de 15 lignes écrit une fois
  1 commande : ansible-playbook deploy_acl.yml
  Temps : 2 minutes · Risque d'erreur : quasi nul
  Vérification : intégrée dans le playbook (ios_command + assert)
  Si erreur : les logs indiquent exactement quel équipement et pourquoi
```

### Les 5 bénéfices de la "Configuration Réseau as Code"

```
1. REPRODUCTIBILITÉ
   → Le même playbook produit toujours le même résultat
   → Déploiement identique sur 1 ou 500 équipements

2. VERSIONNAGE (avec Git)
   → Historique complet de toutes les configurations
   → Rollback possible : "revenir à la version d'hier"
   → Qui a changé quoi, quand, pourquoi

3. DOCUMENTATION VIVANTE
   → Le playbook EST la documentation
   → Plus besoin de maintenir un fichier Word séparé

4. TEST ET VALIDATION
   → Tester en lab avant de déployer en prod
   → Playbooks de vérification automatiques

5. COLLABORATION
   → Plusieurs admins travaillent sur le même dépôt Git
   → Code review avant tout déploiement
```

---

**🖼️ ILLUSTRATION 1**
> *Légende* : Comparaison "Avant automation" vs "Avec automation". Gauche : administrateur stressé devant 5 terminaux SSH ouverts simultanément, chacun avec un routeur différent, horloge montrant 45 min, points rouges pour les erreurs potentielles. Droite : administrateur serein qui tape `ansible-playbook` dans un seul terminal, les 5 routeurs se configurent en parallèle représentés par des flèches vertes, horloge montrant 2 min, icône Git pour le versionnage. En bas : tableau 5 bénéfices.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 2️⃣ — Ansible : architecture et concepts

### Vue d'ensemble Ansible

```
MACHINE DE CONTRÔLE (Control Node)
  → Machine Linux où Ansible est installé
  → Lance les playbooks
  → Se connecte via SSH aux équipements cibles
  → PAS BESOIN d'installer quoi que ce soit sur les cibles !

ÉQUIPEMENTS CIBLES (Managed Nodes)
  → Routeurs, switches, serveurs
  → Seul prérequis : SSH actif et compte d'accès

INVENTAIRE (Inventory)
  → Fichier listant les équipements cibles
  → Groupes d'équipements
  → Variables de connexion

PLAYBOOK
  → Fichier YAML décrivant les tâches à exécuter
  → S'exécute contre les équipements de l'inventaire
```

### Structure d'un inventaire Ansible

```ini
# fichier: inventory.ini

[cisco_routeurs]           ← Nom du groupe
R1 ansible_host=192.168.1.1
R2 ansible_host=192.168.1.2
R3 ansible_host=192.168.1.3

[cisco_switches]
SW1 ansible_host=192.168.1.10
SW2 ansible_host=192.168.1.11

[tous_cisco:children]      ← Groupe qui contient d'autres groupes
cisco_routeurs
cisco_switches

[tous_cisco:vars]          ← Variables communes à tous les équipements Cisco
ansible_user=admin
ansible_password=Cisco123!
ansible_network_os=ios
ansible_connection=network_cli
ansible_become=yes
ansible_become_method=enable
ansible_become_password=Cisco123!
```

### Structure d'un playbook Ansible

```yaml
---                                        # Début d'un fichier YAML
- name: Description du play               # Nom de la séquence de tâches
  hosts: cisco_routeurs                    # Groupe cible de l'inventaire
  gather_facts: false                      # Désactiver la collecte auto (plus rapide)
  
  vars:                                    # Variables locales
    interface_wann: GigabitEthernet0/1
    description_wan: "Lien vers FAI"
  
  tasks:                                   # Liste des tâches
    
    - name: Configurer la description WAN  # Nom de la tâche (apparaît dans les logs)
      cisco.ios.ios_config:               # Module Ansible à utiliser
        lines:                            # Commandes IOS à envoyer
          - interface {{ interface_wan }}
          - description {{ description_wan }}
    
    - name: Vérifier la configuration     # Tâche de vérification
      cisco.ios.ios_command:
        commands:
          - show interfaces GigabitEthernet0/1 | include Description
      register: verification             # Sauvegarder le résultat dans une variable
    
    - name: Afficher le résultat
      debug:
        msg: "Résultat : {{ verification.stdout[0] }}"
```

---

**🖼️ ILLUSTRATION 2**
> *Légende* : Anatomie d'un playbook Ansible YAML avec 8 flèches colorées annotant chaque section. La structure YAML est affichée avec une indentation mise en évidence. Les flèches pointent vers : `---` (début de fichier YAML), `name:` (description du play), `hosts:` (groupe cible), `vars:` (variables), `tasks:` (liste de tâches), `cisco.ios.ios_config:` (module Ansible), `lines:` (commandes IOS), `register:` (capturer le résultat). À droite, le flux d'exécution : playbook → Ansible → SSH → routeur → résultat.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 3️⃣ — Les modules Ansible réseau essentiels

### Modules `cisco.ios` principaux

```yaml
# MODULE 1 : ios_config — Envoyer de la configuration
- name: Configurer OSPF
  cisco.ios.ios_config:
    lines:
      - router ospf 1
      - router-id 1.1.1.1
      - network 192.168.0.0 0.0.255.255 area 0
    parents: router ospf 1    # Contexte hiérarchique optionnel

# MODULE 2 : ios_command — Exécuter des commandes show
- name: Vérifier les voisins OSPF
  cisco.ios.ios_command:
    commands:
      - show ip ospf neighbor
      - show ip route
  register: sortie

# MODULE 3 : ios_facts — Collecter des informations sur l'équipement
- name: Collecter les facts
  cisco.ios.ios_facts:
    gather_subset:
      - all

# MODULE 4 : debug — Afficher des variables
- name: Afficher la version IOS
  debug:
    msg: "Version : {{ ansible_net_version }}"

# MODULE 5 : assert — Vérifier une condition
- name: Vérifier que OSPF est actif
  assert:
    that:
      - "'FULL' in sortie.stdout[0]"
    fail_msg: "OSPF n'est pas convergé !"
    success_msg: "OSPF est bien convergé"
```

### Variables Ansible automatiques pour les équipements réseau

```
{{ ansible_net_hostname }}   → Nom de l'équipement
{{ ansible_net_version }}    → Version du système d'exploitation
{{ ansible_net_interfaces }} → Dictionnaire des interfaces
{{ ansible_net_neighbors }}  → Voisins CDP/LLDP
{{ inventory_hostname }}     → Nom de l'hôte dans l'inventaire
```

---

## 4️⃣ — Playbook complet : exemple réel

### Déploiement de VLANs et configuration de trunks

```yaml
---
- name: Déploiement VLAN et Trunk - TECHPRO
  hosts: cisco_switches
  gather_facts: false

  vars:
    vlans:
      - { id: 10, nom: DATA }
      - { id: 20, nom: VOIX }
      - { id: 30, nom: GESTION }
    interface_trunk: GigabitEthernet0/1

  tasks:
    # ÉTAPE 1 : Créer les VLANs
    - name: Créer les VLANs
      cisco.ios.ios_config:
        lines:
          - vlan {{ item.id }}
          - name {{ item.nom }}
      loop: "{{ vlans }}"

    # ÉTAPE 2 : Configurer le trunk
    - name: Configurer l'interface trunk
      cisco.ios.ios_config:
        lines:
          - switchport mode trunk
          - switchport trunk allowed vlan 10,20,30
        parents:
          - interface {{ interface_trunk }}

    # ÉTAPE 3 : Vérifier
    - name: Vérifier les VLANs créés
      cisco.ios.ios_command:
        commands:
          - show vlan brief
      register: etat_vlans

    # ÉTAPE 4 : Afficher la vérification
    - name: Afficher les VLANs
      debug:
        var: etat_vlans.stdout_lines

    # ÉTAPE 5 : Sauvegarder
    - name: Sauvegarder la configuration
      cisco.ios.ios_config:
        save_when: always
```

---

**🖼️ ILLUSTRATION 3**
> *Légende* : Schéma d'exécution d'un playbook Ansible sur 3 switches simultanément. En haut, la machine de contrôle avec le playbook YAML. Des flèches SSH partent vers 3 switches (SW1, SW2, SW3) en parallèle. Chaque switch montre les 5 tâches s'exécutant dans l'ordre (barres de progression). La sortie Ansible dans le terminal montre "PLAY RECAP" avec les statuts ok/changed/failed pour chaque hôte. Un chronomètre compare "3 switches en parallèle = même temps que 1 switch".
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 5️⃣ — Python Netmiko : automatisation flexible

### Pourquoi Netmiko ?

```
Ansible → Déclaratif · Idempotent · Lisible · YAML
  ✓ Idéal pour la configuration répétitive et standardisée
  ✗ Moins flexible pour la logique conditionnelle complexe

Netmiko → Impératif · Contrôle total · Python
  ✓ Logique programmable (if/else, calculs, traitement de sortie)
  ✓ Intégration avec d'autres bibliothèques Python (pandas, matplotlib...)
  ✗ Plus verbeux que Ansible pour les cas simples
```

### Connexion de base avec Netmiko

```python
from netmiko import ConnectHandler

# Définir l'équipement cible
routeur = {
    "device_type": "cisco_ios",     # Type d'équipement
    "host": "192.168.1.1",          # Adresse IP
    "username": "admin",             # Nom d'utilisateur
    "password": "Cisco123!",         # Mot de passe SSH
    "secret": "Cisco123!",           # Mot de passe enable
}

# Se connecter
connexion = ConnectHandler(**routeur)
connexion.enable()                   # Passer en mode privilégié

# Envoyer une commande show
sortie = connexion.send_command("show ip route")
print(sortie)

# Envoyer de la configuration
commandes_config = [
    "interface GigabitEthernet0/0",
    "description Lien WAN - FAI1",
    "no shutdown",
]
connexion.send_config_set(commandes_config)

# Sauvegarder
connexion.save_config()

# Déconnexion
connexion.disconnect()
print("✓ Terminé !")
```

### Netmiko sur plusieurs équipements (pattern professionnel)

```python
from netmiko import ConnectHandler

# Inventaire (normalement lu depuis un fichier)
inventaire = [
    {"name": "R1", "host": "192.168.1.1"},
    {"name": "R2", "host": "192.168.1.2"},
    {"name": "R3", "host": "192.168.1.3"},
]

connexion_base = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "Cisco123!",
    "secret": "Cisco123!",
}

resultats = {}

for equipement in inventaire:
    nom = equipement["name"]
    print(f"[{nom}] Connexion...")
    
    try:
        # Connexion
        params = {**connexion_base, "host": equipement["host"]}
        conn = ConnectHandler(**params)
        conn.enable()
        
        # Collecter des informations
        version = conn.send_command("show version | include Version")
        voisins = conn.send_command("show ip ospf neighbor")
        
        # Stocker les résultats
        resultats[nom] = {
            "version": version,
            "voisins_ospf": voisins,
            "statut": "OK"
        }
        
        conn.disconnect()
        print(f"  ✓ [{nom}] Collecte réussie")
        
    except Exception as erreur:
        resultats[nom] = {"statut": f"ERREUR: {erreur}"}
        print(f"  ✗ [{nom}] Erreur : {erreur}")

# Rapport final
print("\n=== RAPPORT DE COLLECTE ===")
for nom, infos in resultats.items():
    print(f"\n{nom}: {infos['statut']}")
    if infos['statut'] == "OK":
        print(f"  Version: {infos['version'][:50]}...")
```

---

**🖼️ ILLUSTRATION 4**
> *Légende* : Comparaison côte à côte Ansible vs Netmiko pour la même tâche (configurer un hostname sur 3 routeurs). Colonne Ansible : 8 lignes de YAML, label "Déclaratif, Idempotent". Colonne Netmiko : 20 lignes de Python, label "Impératif, Flexible". Tableau de comparaison en dessous : Syntaxe/Idempotence/Flexibilité/Courbe apprentissage/Cas d'usage idéal. Des icônes représentent: YAML=document, Python=serpent logo.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 6️⃣ — Configuration Réseau as Code : concepts clés

### Idempotence

```
DÉFINITION : Exécuter une action N fois = même résultat que 1 fois

Exemple :
  ansible-playbook configure_vlans.yml
  # Résultat : VLAN 10 créé, VLAN 20 créé
  
  ansible-playbook configure_vlans.yml  ← exécuté une 2ème fois
  # Résultat : unchanged (VLANs déjà présents → rien ne change)

IMPORTANCE :
  → Déployer en toute sécurité sans vérifier "est-ce déjà configuré ?"
  → Re-déployer pour corriger une dérive de configuration
```

### Configuration Drift et Remediation

```
CONFIGURATION DRIFT = La configuration réelle diverge de la configuration souhaitée
  Cause : modification manuelle hors du playbook, bug, changement non documenté

DÉTECTION : ansible-playbook --check (dry run)
  → Montre ce qui changerait SANS appliquer les changements
  
REMÉDIATION : ansible-playbook configure_baseline.yml
  → Réapplique la configuration de référence sur TOUS les équipements
  → Corrige automatiquement les dérives
```

### Git pour les configurations réseau

```bash
# Initialiser un dépôt pour les playbooks
git init network-automation/
cd network-automation/

# Ajouter les fichiers
git add inventory.ini playbooks/

# Commiter un changement
git commit -m "Ajout ACL sécurité serveurs DMZ - ticket #1234"

# Voir l'historique
git log --oneline

# Revenir à une version précédente (rollback)
git checkout abc1234 -- playbooks/configure_acl.yml
ansible-playbook playbooks/configure_acl.yml  # Re-déployer l'ancienne version
```

---

**🖼️ ILLUSTRATION 5**
> *Légende* : Cycle de vie "Configuration Réseau as Code" sous forme de roue. Les 5 étapes en cercle : 1-Coder (écrire le playbook/script), 2-Tester (dry-run, tests unitaires), 3-Versionner (git commit), 4-Déployer (ansible-playbook), 5-Vérifier (playbook de vérification + assert). Au centre : "Configuration de référence". Une flèche externe représente la "dérive" et une flèche de retour montre la "remédiation". En bas, les outils : Ansible, Netmiko, Git, Python.
>
> > 🖼️ **Illustration à venir** — schéma en cours de production.

---

## 📌 Les essentiels à retenir pour l'examen

> ✅ **Ansible** : agentless · YAML · inventaire + playbook · modules `ios_config` et `ios_command`
> ✅ **Inventaire** : liste les équipements cibles + variables de connexion
> ✅ **Playbook** : fichier YAML avec `hosts:`, `vars:`, `tasks:` · s'exécute via `ansible-playbook`
> ✅ **ios_config** = envoyer de la **configuration** · **ios_command** = envoyer des commandes **show**
> ✅ **`register:`** = sauvegarder la sortie d'une tâche dans une variable
> ✅ **Idempotence** = exécuter N fois = même résultat que 1 fois
> ✅ **Netmiko** : bibliothèque Python · `ConnectHandler()` + `send_config_set()` + `send_command()`
> ✅ `ansible-playbook --check` = **dry run** (simulation sans appliquer)
> ✅ **Git** + playbooks = configuration versionnée + historique + rollback
> ✅ Ansible = déclaratif (YAML lisible) · Netmiko = impératif (Python flexible)

---

*Fiche de Cours — BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S10*
*Compétences : S7.1 · S7.2 · S7.3 · C2.2 · C3.1*

{% endraw %}
