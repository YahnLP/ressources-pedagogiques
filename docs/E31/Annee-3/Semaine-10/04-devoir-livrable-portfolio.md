{% raw %}
# 📝 DEVOIR & LIVRABLE PORTFOLIO — S10 · 3ᵉ ANNÉE · E31
## Automation : Ansible · Python Netmiko · Configuration Réseau as Code

---

> **Module** : E31 – Administration Systèmes — Automation réseau
> **Épreuve visée** : **E31** · CCNA DevNet (optionnel)
> **Durée totale** : Partie A en classe (45 min) + Partie B en autonomie (≈ 50 min)

---

## 📌 Compétences évaluées

| Code | Compétence | Barème |
|---|---|---|
| **S7.1** | Ansible — inventaire, playbook, modules ios | /35 |
| **S7.2** | Python Netmiko — connexion, commandes | /30 |
| **S7.3** | IaC — idempotence, versionnage, drift | /20 |
| **C3.1** | Documenter et commenter le code | /15 |
| | **TOTAL** | **/100** |

---

## 🎯 Mise en situation

> **Tu es automaticien réseau** chez MULTICORP (50 agences, 200 routeurs).
> Ton manager te donne 3 missions à accomplir avant la fin de la journée.

---

## 🅰️ PARTIE A — En classe (45 min)

### 🤖 Exercice 1 — Analyser et corriger un playbook (/35)

> Ton collègue a écrit ce playbook mais il contient **3 erreurs**. Trouve-les et corrige.

```yaml
---
- name: Configuration OSPF sur routeurs MULTICORP
  hosts: tous_les_routeurs          # Erreur potentielle 1
  gather_facts: false

  vars:
    ospf_process: 1
    ospf_area: 0

  tasks:
    - name: Activer OSPF
      cisco.ios.ios_config:
        lines:
          - router ospf {{ ospf_process }}
          - router-id {{ inventory_hostname }}.1.1    # Erreur potentielle 2
          - network 192.168.0.0 255.255.0.0 area 0   # Erreur potentielle 3

    - name: Vérifier OSPF
      cisco.ios.ios_command:
        commands:
          - show ip ospf
```

**1.a** — Identifie et explique les 3 erreurs : *(15 pts)*

```
Erreur 1 (ligne hosts:) :
  Problème : _________________________________________________________________
  Correction : _______________________________________________________________

Erreur 2 (router-id) :
  Problème : _________________________________________________________________
  Correction : _______________________________________________________________

Erreur 3 (network) :
  Problème : _________________________________________________________________
  Correction : _______________________________________________________________
```

**1.b** — Réécris le playbook corrigé et complet, avec des commentaires : *(20 pts)*

```yaml
---
# Playbook : Configuration OSPF - MULTICORP
# Auteur   : _____________________
# Date     : _____________________

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
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

---

## 🅱️ PARTIE B — En autonomie (/65)

### 📋 Exercice 2 — Écrire un inventaire et un playbook (/30)

> MULTICORP a 3 sites avec ces équipements :

```
Site Paris (VLAN 10 = 192.168.10.0/24, VLAN 20 = 192.168.20.0/24)
  R_PARIS   : 10.0.1.1   (routeur de bordure)
  SW_PARIS  : 10.0.1.10  (switch de distribution)

Site Lyon (VLAN 10 = 192.168.30.0/24, VLAN 20 = 192.168.40.0/24)
  R_LYON    : 10.0.2.1
  SW_LYON   : 10.0.2.10

Credentials : admin / Cisco123! (enable aussi)
```

**2.a** — Écris l'inventaire Ansible complet avec des groupes logiques : *(10 pts)*

```ini
# inventaires/multicorp.ini
# Inventaire Ansible - MULTICORP
# Auteur : ___________________

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
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
___________________________________________________________________________
```

**2.b** — Écris un playbook qui configure les VLANs sur les switches avec une boucle : *(20 pts)*

```yaml
# playbooks/deploiement_vlans.yml
# Mission : Déployer VLAN 10 (DATA) et VLAN 20 (VOIP) sur tous les switches

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
___________________________________________________________________________
___________________________________________________________________________
```

---

### 🐍 Exercice 3 — Script Python Netmiko (/20)

> Écris un script Python qui se connecte à R_PARIS et R_LYON, récupère leur table de routage, et signale si une route OSPF est présente.

```python
# scripts/audit_routage.py
# Mission : Vérifier que OSPF est actif et des routes O existent
# Auteur  : ___________________

from netmiko import ConnectHandler

# Définir les routeurs à auditer
routeurs = [
    _____________________________________________________________________,
    _____________________________________________________________________,
]

# Paramètres communs de connexion
connexion_base = {
    _____________________________________________________________________
    _____________________________________________________________________
    _____________________________________________________________________
    _____________________________________________________________________
}

print("AUDIT ROUTAGE MULTICORP")
print("=" * 40)

for routeur in routeurs:
    print(f"\n[{routeur['name']}] Audit en cours...")
    
    try:
        # Connexion SSH
        params = {**connexion_base, "host": _________________________}
        conn = ConnectHandler(**params)
        _____________________________        # Passer en mode enable
        
        # Récupérer la table de routage
        table_routage = conn.send_command("_____________________________")
        
        # Vérifier si des routes OSPF existent
        if "O" in table_routage:
            print(f"  ✅ Routes OSPF présentes")
        else:
            print(f"  ❌ Aucune route OSPF !")
            
        # Compter le nombre de routes
        lignes_O = [l for l in table_routage.split('\n') if l.startswith('O')]
        print(f"  Nombre de routes O : {len(lignes_O)}")
        
        # Fermer proprement
        _____________________________
        
    except Exception as e:
        print(f"  ❌ Erreur : {e}")

print("\nAudit terminé.")
```

**Complète les 7 blancs dans le script.**

---

### 💡 Exercice 4 — Questions conceptuelles IaC (/15)

**4.a** — Explique l'idempotence avec un exemple concret dans le contexte réseau : *(5 pts)*

```
Définition : __________________________________________________________________
Exemple réseau : si tu lances un playbook qui crée le VLAN 10 sur un switch
  Première exécution → Ansible dit : ____________ (VLAN créé)
  Deuxième exécution → Ansible dit : ____________ (VLAN déjà présent)
  Impact sur le réseau : ☐ le VLAN est supprimé et recréé ☐ rien ne change
```

**4.b** — Ton manager te demande de déployer une nouvelle ACL sur 200 routeurs.
Décris la démarche "réseau as code" en 5 étapes : *(10 pts)*

```
Étape 1 (Coder) : _____________________________________________________________
Étape 2 (Tester) : ____________________________________________________________
Étape 3 (Versionner) : ________________________________________________________
Étape 4 (Déployer) : __________________________________________________________
Étape 5 (Vérifier) : __________________________________________________________
```

---

## 🏅 Barème global

| Exercice | Compétences | Barème | Seuil |
|---|---|---|---|
| Ex. 1 — Analyser et corriger playbook | S7.1 | /35 | ≥ 20 |
| Ex. 2 — Inventaire + playbook | S7.1 + C3.1 | /30 | ≥ 17 |
| Ex. 3 — Script Netmiko | S7.2 | /20 | ≥ 11 |
| Ex. 4 — IaC concepts | S7.3 | /15 | ≥ 8 |
| **TOTAL** | | **/100** | **≥ 55** |

---

---

# ✅ CORRECTION ATTENDUE — Document Enseignant uniquement

## Correction Exercice 1

**Erreur 1 — `hosts: tous_les_routeurs`** : Ce groupe n'existe probablement pas dans l'inventaire. Si on veut tous les équipements, utiliser `all` ou créer le groupe dans l'inventaire. Correction : `hosts: cisco_routeurs` (ou `hosts: all` si voulu)

**Erreur 2 — `router-id {{ inventory_hostname }}.1.1`** : `inventory_hostname` est le nom symbolique (R1) pas une adresse IP. Un router-id doit être au format `X.X.X.X`. Correction : utiliser une variable dédiée comme `router_id: "1.1.1.1"` dans les variables host ou group.

**Erreur 3 — `network 192.168.0.0 255.255.0.0 area 0`** : La commande OSPF utilise le **wildcard mask** pas le masque réseau. `255.255.0.0` est le masque, pas le wildcard. Wildcard de /16 = `0.0.255.255`. Correction : `network 192.168.0.0 0.0.255.255 area 0`

**1.b Playbook corrigé** :
```yaml
---
# Playbook : Configuration OSPF - MULTICORP
- name: Configuration OSPF sur routeurs MULTICORP
  hosts: cisco_routeurs
  gather_facts: false

  vars:
    ospf_process: 1
    ospf_area: 0
    # router_id défini par hôte dans l'inventaire : host_vars/R1.yml → router_id: 1.1.1.1

  tasks:
    - name: Activer OSPF avec router-id correct
      cisco.ios.ios_config:
        lines:
          - router ospf {{ ospf_process }}
          - router-id {{ router_id }}             # Variable définie par hôte
          - network 192.168.0.0 0.0.255.255 area {{ ospf_area }}  # Wildcard !
          - passive-interface default
          - no passive-interface GigabitEthernet0/1

    - name: Vérifier OSPF
      cisco.ios.ios_command:
        commands:
          - show ip ospf neighbor
      register: voisins_ospf

    - name: Afficher les voisins
      debug:
        var: voisins_ospf.stdout_lines
```

## Correction Exercice 2

**Inventaire** :
```ini
[routeurs_paris]
R_PARIS ansible_host=10.0.1.1

[switches_paris]
SW_PARIS ansible_host=10.0.1.10

[routeurs_lyon]
R_LYON ansible_host=10.0.2.1

[switches_lyon]
SW_LYON ansible_host=10.0.2.10

[tous_routeurs:children]
routeurs_paris
routeurs_lyon

[tous_switches:children]
switches_paris
switches_lyon

[tous_cisco:children]
tous_routeurs
tous_switches

[tous_cisco:vars]
ansible_user=admin
ansible_password=Cisco123!
ansible_network_os=ios
ansible_connection=network_cli
ansible_become=yes
ansible_become_method=enable
ansible_become_password=Cisco123!
```

**Playbook VLANs** :
```yaml
---
- name: Déploiement VLANs MULTICORP
  hosts: tous_switches
  gather_facts: false

  vars:
    vlans:
      - { id: 10, nom: DATA }
      - { id: 20, nom: VOIP }

  tasks:
    - name: Créer les VLANs
      cisco.ios.ios_config:
        lines:
          - vlan {{ item.id }}
          - name {{ item.nom }}
      loop: "{{ vlans }}"

    - name: Vérifier
      cisco.ios.ios_command:
        commands:
          - show vlan brief
      register: vlans_etat

    - name: Afficher
      debug:
        var: vlans_etat.stdout_lines

    - name: Sauvegarder
      cisco.ios.ios_config:
        save_when: always
```

## Correction Exercice 3

```python
routeurs = [
    {"name": "R_PARIS", "host": "10.0.1.1"},
    {"name": "R_LYON", "host": "10.0.2.1"},
]

connexion_base = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "Cisco123!",
    "secret": "Cisco123!",
}

# Dans la boucle :
params = {**connexion_base, "host": routeur["host"]}
conn.enable()
table_routage = conn.send_command("show ip route")
conn.disconnect()
```

---

*Devoir + Correction — BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S10*
*Épreuve E31 | Compétences S7.1 · S7.2 · S7.3 · C2.2 · C3.1*

{% endraw %}
