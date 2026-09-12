{% raw %}
# 🔬 TRAVAUX PRATIQUES — S10 · 3ᵉ ANNÉE · E31
## Automation : Ansible Playbooks · Python Netmiko · Configuration Réseau

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche de cours autorisée** · **VM Linux + GNS3/PT**
> **Répertoire de travail** : `~/automation-reseau/`
> **Épreuve ciblée** : **E31** – Administration systèmes

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S7.1** | Créer un inventaire et un playbook Ansible |
| **S7.2** | Écrire et exécuter un script Python Netmiko |
| **S7.3** | Appliquer les concepts IaC (idempotence, vérification) |
| **C2.2** | Automatiser la configuration réseau |
| **C3.1** | Commenter les scripts pour la documentation |

---

## 🗺️ Infrastructure du TP

```
VM Linux (machine de contrôle Ansible)
  IP : 192.168.100.50
  
  ├── Ansible installé
  ├── Python 3 + netmiko installés
  └── Répertoire ~/automation-reseau/

Équipements cibles (GNS3 ou PT) :
  R1 : 192.168.100.1  (Cisco IOS, SSH configuré)
  R2 : 192.168.100.2  (Cisco IOS, SSH configuré)
  SW1: 192.168.100.10 (Cisco IOS Switch)

Tous les équipements :
  Username : admin  Password : Cisco123!  Enable : Cisco123!
```

---

## 🟢 NIVEAU 1 — Préparer l'environnement (10 min)

**1.1** — Crée le répertoire de travail et les sous-dossiers :

```bash
mkdir -p ~/automation-reseau/{playbooks,scripts,inventaires}
cd ~/automation-reseau/
```

**1.2** — Crée le fichier d'inventaire :

```bash
nano inventaires/inventory.ini
```

Contenu :

```ini
[cisco_routeurs]
R1 ansible_host=192.168.100.1
R2 ansible_host=192.168.100.2

[cisco_switches]
SW1 ansible_host=192.168.100.10

[tous_cisco:children]
cisco_routeurs
cisco_switches

[tous_cisco:vars]
ansible_user=admin
ansible_password=Cisco123!
ansible_network_os=ios
ansible_connection=network_cli
ansible_become=yes
ansible_become_method=enable
ansible_become_password=Cisco123!
```

**1.3** — Teste la connectivité Ansible vers R1 :

```bash
ansible R1 -i inventaires/inventory.ini -m ping
```

```
Résultat attendu : R1 | SUCCESS → { "ping": "pong" }
Résultat obtenu : ☐ SUCCESS ☐ FAILED → Erreur : ________________________
```

---

## 🟡 NIVEAU 2 — Premier playbook Ansible (20 min)

**2.1** — Crée un playbook pour collecter des informations :

```bash
nano playbooks/01_collecte_info.yml
```

Contenu :

```yaml
---
- name: Collecte d'informations - Routeurs TECHPRO
  hosts: cisco_routeurs
  gather_facts: false

  tasks:
    - name: Récupérer la version IOS
      cisco.ios.ios_command:
        commands:
          - show version | include Version
      register: version_ios

    - name: Récupérer la table de routage
      cisco.ios.ios_command:
        commands:
          - show ip route
      register: table_routage

    - name: Afficher la version
      debug:
        msg: "{{ inventory_hostname }} - {{ version_ios.stdout[0] }}"

    - name: Afficher un résumé de la table de routage
      debug:
        msg: "{{ table_routage.stdout_lines[0][:5] }}"
```

**2.2** — Exécute le playbook :

```bash
cd ~/automation-reseau
ansible-playbook -i inventaires/inventory.ini playbooks/01_collecte_info.yml
```

**2.3** — Observe la sortie et réponds :

```
Nombre de tâches exécutées : _______
Résultat pour R1 : ☐ ok ☐ changed ☐ failed
Résultat pour R2 : ☐ ok ☐ changed ☐ failed
Version IOS affichée pour R1 : _______________________________________________
```

**2.4** — Exécute le playbook une 2ème fois sans rien changer :

```bash
ansible-playbook -i inventaires/inventory.ini playbooks/01_collecte_info.yml
```

```
Le résultat est-il différent ? ☐ Oui ☐ Non
C'est le principe de : ___________________________________
```

---

## 🟠 NIVEAU 3 — Playbook de configuration (25 min)

**3.1** — Crée un playbook pour configurer les interfaces :

```bash
nano playbooks/02_config_interfaces.yml
```

```yaml
---
- name: Configuration des interfaces WAN
  hosts: cisco_routeurs
  gather_facts: false

  vars:
    interfaces:
      R1:
        nom: GigabitEthernet0/0
        description: "Lien vers ISP - Fibre 1G"
        ip: 192.168.100.1
        masque: 255.255.255.0
      R2:
        nom: GigabitEthernet0/0
        description: "Lien vers HQ - MPLS"
        ip: 192.168.100.2
        masque: 255.255.255.0

  tasks:
    - name: Configurer l'interface
      cisco.ios.ios_config:
        lines:
          - description {{ interfaces[inventory_hostname].description }}
          - ip address {{ interfaces[inventory_hostname].ip }} {{ interfaces[inventory_hostname].masque }}
          - no shutdown
        parents:
          - interface {{ interfaces[inventory_hostname].nom }}

    - name: Vérifier la configuration de l'interface
      cisco.ios.ios_command:
        commands:
          - "show interfaces {{ interfaces[inventory_hostname].nom }} | include Description"
      register: verif_interface

    - name: Afficher le résultat
      debug:
        var: verif_interface.stdout_lines

    - name: Sauvegarder la configuration
      cisco.ios.ios_config:
        save_when: always
```

**3.2** — Exécute le playbook et observe :

```bash
ansible-playbook -i inventaires/inventory.ini playbooks/02_config_interfaces.yml
```

```
Tâches avec statut "changed" : _________________________________________________
(changed = quelque chose a réellement été modifié sur l'équipement)
Tâches avec statut "ok" : ______________________________________________________
(ok = déjà dans l'état correct, rien à faire)
```

**3.3** — Exécute le playbook une 2ème fois :

```bash
ansible-playbook -i inventaires/inventory.ini playbooks/02_config_interfaces.yml
```

```
Combien de "changed" au 2ème lancement ? _______
Pourquoi ? ___________________________________________________________________
Ce comportement illustre : ___________________________________________________
```

**3.4** — Utilise le dry-run pour voir ce qui changerait sans appliquer :

```bash
ansible-playbook -i inventaires/inventory.ini playbooks/02_config_interfaces.yml --check
```

```
Qu'affiche Ansible en mode --check ? ________________________________________
Quel est l'intérêt de ce mode avant un déploiement en production ? ______________
```

---

## 🔵 NIVEAU 4 — Script Python Netmiko (20 min)

**4.1** — Crée un script Python pour vérifier l'état OSPF de tous les routeurs :

```bash
nano scripts/verifier_ospf.py
```

```python
#!/usr/bin/env python3
"""
Script : vérification état OSPF
Auteur : ___________________
Date   : ___________________
"""

from netmiko import ConnectHandler

# Inventaire des routeurs
routeurs = [
    {"name": "R1", "host": "192.168.100.1"},
    {"name": "R2", "host": "192.168.100.2"},
]

# Paramètres de connexion
connexion_base = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "Cisco123!",
    "secret": "Cisco123!",
}

# Rapport final
print("=" * 50)
print("VÉRIFICATION OSPF - RÉSEAU TECHPRO")
print("=" * 50)

for routeur in routeurs:
    print(f"\n[{routeur['name']}] Connexion sur {routeur['host']}...")
    
    try:
        # COMPLÉTER : Créer la connexion
        params = {**connexion_base, "host": _______________}
        conn = ConnectHandler(**params)
        conn.enable()
        
        # COMPLÉTER : Récupérer les voisins OSPF
        voisins = conn.send_command("_____________________________")
        
        # Analyser si OSPF est convergé
        if "FULL" in voisins:
            print(f"  ✅ OSPF convergé (adjacences FULL présentes)")
        elif voisins.strip() == "":
            print(f"  ❌ Aucun voisin OSPF détecté !")
        else:
            print(f"  ⚠️  OSPF en cours de convergence")
            
        print(f"  Sortie : {voisins[:100]}...")
        
        # COMPLÉTER : Fermer la connexion
        conn._______________()
        
    except Exception as e:
        print(f"  ❌ Erreur de connexion : {e}")

print("\n" + "=" * 50)
print("Vérification terminée.")
```

**4.2** — Complète les 3 parties marquées `_______________` dans le script.

**4.3** — Exécute le script :

```bash
python3 scripts/verifier_ospf.py
```

```
Résultat pour R1 : ☐ ✅ Convergé ☐ ❌ Aucun voisin ☐ ⚠️ En cours ☐ Erreur connexion
Résultat pour R2 : ___________________________________________________________
```

**4.4** — Ajoute une fonctionnalité : sauvegarder le résultat dans un fichier texte.
Ajoute ces lignes AVANT le `for routeur in routeurs:` :

```python
import datetime
horodatage = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
fichier_log = f"rapport_ospf_{horodatage}.txt"
```

Et ajoute à l'intérieur de la boucle :

```python
with open(fichier_log, "a") as f:
    f.write(f"[{routeur['name']}] {voisins}\n")
```

```bash
python3 scripts/verifier_ospf.py
ls -la *.txt       # Vérifier que le fichier de log est créé
cat rapport_ospf_*.txt
```

---

## 🔴 NIVEAU 5 — Versionner avec Git et bilan (5 min)

**5.1** — Initialise un dépôt Git pour tes playbooks :

```bash
cd ~/automation-reseau
git init
echo "# Réseau TECHPRO - Automation" > README.md
git add .
git commit -m "Init : inventaire + playbooks collecte et interfaces + script OSPF"
git log --oneline
```

**5.2** — Simule une modification et un rollback :

```bash
# Modifier une description dans le playbook
sed -i 's/Lien vers ISP/Lien vers ISP MODIFIE/' playbooks/02_config_interfaces.yml
git diff  # Voir la modification

# Annuler la modification (rollback)
git checkout -- playbooks/02_config_interfaces.yml
cat playbooks/02_config_interfaces.yml | grep description
# Vérifier que la description originale est restaurée
```

```
Après le rollback git, la description est : _____________________________________
C'est exactement ce qu'on ferait pour restaurer une configuration réseau
qui aurait causé un incident en production.
```

**5.3** — Réflexion finale :

```
En quoi Ansible est-il "agentless" (sans agent) ?
___________________________________________________________________________

Quelle est la différence entre "ok" et "changed" dans la sortie Ansible ?
  ok      = _________________________________________________________________
  changed = _________________________________________________________________

Cite un scénario réel où python Netmiko serait préféré à Ansible :
___________________________________________________________________________
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Créer un inventaire Ansible | ☐ | ☐ | ☐ |
| Écrire un playbook avec ios_config et ios_command | ☐ | ☐ | ☐ |
| Comprendre et utiliser `register:` et `debug:` | ☐ | ☐ | ☐ |
| Expliquer l'idempotence (changed vs ok) | ☐ | ☐ | ☐ |
| Écrire un script Python Netmiko avec boucle | ☐ | ☐ | ☐ |
| Utiliser git pour versionner les playbooks | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Niv.1-2 — Inventaire créé + playbook collecte fonctionnel | /5 |
| Niv.3 — Playbook config avec changed/ok + dry-run | /7 |
| Niv.4 — Script Netmiko complété et exécuté | /8 |
| Niv.5 — Git init + commit + rollback compris | /5 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Niveau 4 — Blancs à compléter

```python
# Ligne 1 : Paramètre host
params = {**connexion_base, "host": routeur["host"]}

# Ligne 2 : Commande OSPF
voisins = conn.send_command("show ip ospf neighbor")

# Ligne 3 : Fermer la connexion
conn.disconnect()
```

## Correction Niveau 5 — Questions

```
Agentless : Ansible se connecte via SSH standard, aucun logiciel n'est installé 
sur les équipements cibles. Il suffit que SSH soit actif.

ok = la tâche a vérifié l'état et il correspond déjà à ce qui est demandé → rien changé
changed = la tâche a dû modifier quelque chose pour atteindre l'état désiré

Netmiko préférable quand :
- Logique conditionnelle complexe (ex: si la version < 15.6 alors faire X sinon faire Y)
- Traitement et analyse de sorties de commandes (regex, parsing)
- Intégration avec une base de données ou une API externe
- Tâches qui ne sont pas idempotentes par nature
```

---

*TP Ansible Netmiko + Correction — BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S10*
*Document Portfolio E31 — Compétences S7.1 · S7.2 · S7.3 · C2.2 · C3.1*

{% endraw %}
