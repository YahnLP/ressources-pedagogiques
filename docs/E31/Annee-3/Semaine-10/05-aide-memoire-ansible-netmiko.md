{% raw %}
# 🗂️ AIDE-MÉMOIRE ANSIBLE / NETMIKO — À PLASTIFIER
## Automation Réseau · IaC · BAC PRO CIEL · E31 · 3ᵉ année S10

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 🤖 Ansible — Structure de base

```ini
# inventory.ini
[cisco_routeurs]
R1 ansible_host=192.168.1.1
R2 ansible_host=192.168.1.2

[cisco_routeurs:vars]
ansible_user=admin
ansible_password=Cisco123!
ansible_network_os=ios
ansible_connection=network_cli
ansible_become=yes
ansible_become_method=enable
ansible_become_password=Cisco123!
```

```yaml
# playbook.yml
---
- name: Description du play
  hosts: cisco_routeurs
  gather_facts: false

  vars:
    ma_variable: valeur

  tasks:
    - name: Configurer quelque chose
      cisco.ios.ios_config:
        lines:
          - commande IOS
      
    - name: Lire quelque chose
      cisco.ios.ios_command:
        commands:
          - show ip route
      register: sortie

    - name: Afficher
      debug:
        var: sortie.stdout_lines
```

---

## ⚙️ Modules ios essentiels

```
ios_config    → envoyer de la CONFIGURATION (mode config)
ios_command   → envoyer des commandes SHOW (mode exec)
ios_facts     → collecter des informations auto
debug         → afficher une variable
assert        → vérifier une condition (test)
```

---

## 🔑 Syntaxe YAML à connaître

```yaml
# Variable simple
nom: TECHPRO

# Liste (loop)
vlans:
  - { id: 10, nom: DATA }
  - { id: 20, nom: VOIX }

# Utiliser la variable dans une tâche
loop: "{{ vlans }}"
→ {{ item.id }}  {{ item.nom }}

# Capturer une sortie
register: ma_variable
→ Utiliser {{ ma_variable.stdout[0] }}

# Template Jinja2
"interface {{ inventory_hostname }}"
```

---

## 🐍 Netmiko — Template de base

```python
from netmiko import ConnectHandler

routeur = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "Cisco123!",
    "secret": "Cisco123!",
}

# Connexion
conn = ConnectHandler(**routeur)
conn.enable()           # Passer en mode exec privilégié

# Commandes show
sortie = conn.send_command("show ip route")

# Commandes de configuration
commandes = [
    "interface Gi0/0",
    "description WAN",
]
conn.send_config_set(commandes)

# Sauvegarder + déconnecter
conn.save_config()
conn.disconnect()
```

---

## 📋 Ansible vs Netmiko

```
Ansible   → YAML · Déclaratif · Idempotent · Config standard
Netmiko   → Python · Impératif · Flexible · Logique complexe

Idempotence = exécuter N fois = même résultat que 1 fois
ok      = déjà dans l'état correct (rien changé)
changed = quelque chose a été modifié
```

---

## ⌨️ Commandes Ansible essentielles

```bash
# Tester la connectivité
ansible R1 -i inventory.ini -m ping

# Exécuter un playbook
ansible-playbook -i inventory.ini playbook.yml

# Dry run (simulation sans appliquer)
ansible-playbook -i inventory.ini playbook.yml --check

# Verbose (voir les détails)
ansible-playbook -i inventory.ini playbook.yml -v
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| Masque au lieu de wildcard dans network OSPF | `/24 → wildcard 0.0.0.255` |
| `hosts: tous_les_routeurs` (groupe inexistant) | Vérifier le nom exact dans l'inventaire |
| Indentation YAML incorrecte | YAML = espaces (pas tabs) · chaque niveau = 2 espaces |
| `register` sans `debug` | Toujours afficher ce qu'on capture |
| Mot de passe enable manquant | Ajouter `ansible_become_password` dans les vars |

---

## 🔧 Cycle IaC (Configuration Réseau as Code)

```
Coder → Tester (--check) → Versionner (git) → Déployer → Vérifier
```

---

*Aide-Mémoire Ansible/Netmiko — À plastifier*
*BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S10*
*Compétences S7.1 · S7.2 · S7.3 · C2.2 · C3.1*

{% endraw %}
