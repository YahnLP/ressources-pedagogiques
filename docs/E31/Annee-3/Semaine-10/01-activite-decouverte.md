{% raw %}
# 🔍 ACTIVITÉ DE DÉCOUVERTE — S10 · 3ᵉ ANNÉE · E31
## « Déchiffrer le code réseau » — Lire Ansible et Python Netmiko sans cours

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement
> **Principe** : On te présente deux outils d'automatisation réseau. Tu dois comprendre ce qu'ils font avant tout cours — comme tu lirais un mode d'emploi étranger.

---

## 🎯 Mise en situation

> **Contexte** : Tu rejoins une équipe réseau qui automatise déjà tout.
> Un collègue t'a laissé ces deux fichiers avant de partir en congés.
> Il t'a juste dit : *"Lance le playbook Ansible et le script Python sur les routeurs.
> Tu comprendras ce qu'ils font en les lisant."*

---

## 📋 Document 1 — Playbook Ansible

```yaml
# fichier: configure_vlans.yml
---
- name: Déploiement VLANs sur les switches TECHPRO
  hosts: cisco_switches
  gather_facts: false
  
  vars:
    vlans_a_creer:
      - id: 10
        name: DATA
      - id: 20
        name: VOIX
      - id: 30
        name: GESTION

  tasks:
    - name: Créer les VLANs sur chaque switch
      cisco.ios.ios_config:
        lines:
          - vlan {{ item.id }}
          - name {{ item.name }}
      loop: "{{ vlans_a_creer }}"
      
    - name: Vérifier que les VLANs sont présents
      cisco.ios.ios_command:
        commands:
          - show vlan brief
      register: resultat_vlan
      
    - name: Afficher le résultat
      debug:
        var: resultat_vlan.stdout_lines
```

---

## 📋 Document 2 — Script Python Netmiko

```python
# fichier: configure_ospf.py
from netmiko import ConnectHandler

# Liste des routeurs à configurer
routeurs = [
    {"host": "192.168.1.1", "nom": "R1", "router_id": "1.1.1.1"},
    {"host": "192.168.1.2", "nom": "R2", "router_id": "2.2.2.2"},
    {"host": "192.168.1.3", "nom": "R3", "router_id": "3.3.3.3"},
]

# Paramètres de connexion communs
connexion_base = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "Cisco123!",
    "secret": "Cisco123!",
}

for routeur in routeurs:
    print(f"→ Configuration de {routeur['nom']}...")
    
    # Fusionner les paramètres spécifiques au routeur
    params = {**connexion_base, "host": routeur["host"]}
    
    # Se connecter via SSH
    connexion = ConnectHandler(**params)
    connexion.enable()
    
    # Commandes de configuration OSPF
    commandes = [
        "router ospf 1",
        f"router-id {routeur['router_id']}",
        "network 192.168.0.0 0.0.255.255 area 0",
        "passive-interface default",
        "no passive-interface GigabitEthernet0/1",
    ]
    
    # Envoyer la configuration
    sortie = connexion.send_config_set(commandes)
    print(f"  ✓ Résultat : {sortie[:80]}...")
    
    # Sauvegarder la configuration
    connexion.save_config()
    
    # Fermer la connexion
    connexion.disconnect()
    
    print(f"  ✓ {routeur['nom']} configuré et sauvegardé.")

print("\n✅ Tous les routeurs ont été configurés avec OSPF.")
```

---

## 🔍 PARTIE 1 — Analyser le playbook Ansible (12 min)

**Question 1.1** — La première ligne `hosts: cisco_switches` signifie que ce playbook s'applique à un groupe d'équipements. Où cette liste d'équipements est-elle définie ?

```
☐ Directement dans le fichier YAML
☐ Dans un fichier séparé appelé "inventaire" ou "inventory"
☐ Dans le code Python
```

**Question 1.2** — La section `vars:` définit une liste `vlans_a_creer` avec 3 entrées. Que contiendrait chaque entrée selon toi ?

```
L'entrée 1 a : id = _______ et name = ___________
L'entrée 2 a : id = _______ et name = ___________
L'entrée 3 a : id = _______ et name = ___________
```

**Question 1.3** — La tâche "Créer les VLANs" utilise `loop: "{{ vlans_a_creer }}"`. D'après le contexte, que fait `loop` ?

```
Loop signifie que la tâche va s'exécuter : ☐ une fois ☐ autant de fois qu'il y a d'éléments dans la liste
Pour ce playbook, la tâche de création de VLAN va s'exécuter : _______ fois
Chaque fois, `{{ item.id }}` sera remplacé par : _______, _______, _______
```

**Question 1.4** — La commande `cisco.ios.ios_config` envoie des configurations. La commande `cisco.ios.ios_command` envoie des commandes différentes. D'après le contenu, quelle est la différence ?

```
ios_config  → envoie des commandes de type : ☐ show ☐ configuration (mode config)
ios_command → envoie des commandes de type : ☐ show ☐ configuration (mode exec)
```

**Question 1.5** — Si ce playbook est lancé une seconde fois sans rien changer, que va-t-il se passer sur les switches ?

```
☐ Une erreur : les VLANs existent déjà
☐ Les VLANs seront recréés (aucun impact car identiques)
☐ Les VLANs seront supprimés puis recréés

Cette propriété s'appelle en automatisation : ______________________________
(créer 2 fois la même chose = même résultat que 1 fois)
```

---

## 🔍 PARTIE 2 — Analyser le script Python Netmiko (12 min)

**Question 2.1** — Le script importe `ConnectHandler` depuis `netmiko`. À quoi sert cet objet ?

```
ConnectHandler sert à : ________________________________________________________
La connexion utilisée est : ☐ Telnet ☐ SSH ☐ HTTP
```

**Question 2.2** — La liste `routeurs` contient 3 dictionnaires. Chaque dictionnaire représente :

```
Un dictionnaire = _______________________________________________________________
Les champs de chaque routeur : host (______), nom (______), router_id (______)
```

**Question 2.3** — Dans la boucle `for routeur in routeurs:`, le script fait la même chose pour chaque routeur. Liste les 4 actions dans l'ordre :

```
Action 1 : ___________________________________________________________________
Action 2 : ___________________________________________________________________
Action 3 : ___________________________________________________________________
Action 4 : ___________________________________________________________________
```

**Question 2.4** — La liste `commandes` contient des commandes Cisco IOS. Qu'est-ce qu'elles configurent ?

```
"router ospf 1"              → _____________________________________________
f"router-id {routeur['router_id']}" → _____________________________________________
"network 192.168.0.0 ..."    → _____________________________________________
"passive-interface default"  → _____________________________________________
"no passive-interface Gi0/1" → _____________________________________________
```

**Question 2.5** — Quelle est la différence principale entre l'approche Ansible et l'approche Python Netmiko ?

```
Ansible utilise des fichiers : ____________ (langage lisible par des non-programmeurs)
Python Netmiko utilise du : ____________ (plus de flexibilité, logique de programmation)

Pour configurer les mêmes 200 routeurs en entreprise :
  Ansible serait préféré si : ________________________________________________
  Python Netmiko serait préféré si : ________________________________________
```

---

## 🏁 Bilan

```
L'automatisation réseau permet de :
1. _______________________________________________________________ (temps)
2. _______________________________________________________________ (erreurs)
3. _______________________________________________________________ (reproductibilité)

Ansible utilise des fichiers _______ (YAML/Python/JSON)
Les équipements cibles sont listés dans un fichier ___________________________
Les instructions sont dans des fichiers appelés _______________________________

Python Netmiko :
  Bibliothèque Python qui gère la connexion : ____________ aux équipements réseau
  La méthode pour envoyer de la configuration est : ___________________________
  La méthode pour envoyer des commandes show est : ____________________________

L'idempotence = exécuter N fois = même résultat que _____ fois
```

---

## 📎 Pour l'enseignant — Réponses

**1.1** : Fichier inventaire séparé

**1.3** : loop → s'exécute 3 fois · {{ item.id }} → 10, 20, 30

**1.4** : ios_config = configuration · ios_command = show (lecture)

**1.5** : Recréés sans impact · Idempotence

**2.3** : 1. Se connecter via SSH (ConnectHandler) · 2. enable() · 3. send_config_set() · 4. save_config() + disconnect()

**2.4** : OSPF process 1 · Router-ID · Annonce réseau 192.168.0.0/16 · passive toutes interfaces · active Gi0/1

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Administration Systèmes | 3ᵉ année S10*
*Compétences : S7.1 · S7.2 · S7.3*

{% endraw %}
