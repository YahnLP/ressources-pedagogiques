# Semaine 6 (S6) - BLOC 2
## "Commutation, Cisco CLI et Linux : Commandes de Base"

---

## 🖥️ TP GUIDÉ CISCO PACKET TRACER
### "Configuration de Base d'un Switch SW_BUREAU_01"

---

### Objectif

Créer une topologie simple, accéder à la CLI d'un switch, le configurer entièrement (hostname, banner, passwords, save) et vérifier la configuration.

---

### Topologie à Réaliser

```
PC-Alice (192.168.10.10/24)─Fa0/1─┐
                                  │
PC-Bob   (192.168.10.20/24)─Fa0/2─┤  [SW_BUREAU_01]
                                  │
PC-Clara (192.168.10.30/24)─Fa0/3─┘
```

---

### Étape 1 : Créer la Topologie (5 min)

1. Ouvrir **Packet Tracer** → Nouveau fichier
2. Ajouter :
   - 1 **Switch Cisco 2960** (dans Network Devices → Switches)
   - 3 **PC** (dans End Devices)
3. Câbler : PC-Alice → Fa0/1, PC-Bob → Fa0/2, PC-Clara → Fa0/3 (câbles droits)
4. Configurer les IP des PC (onglet Desktop → IP Configuration) :
   - PC-Alice : `192.168.10.10` / `255.255.255.0`
   - PC-Bob : `192.168.10.20` / `255.255.255.0`
   - PC-Clara : `192.168.10.30` / `255.255.255.0`

✅ **Validation :** Les voyants des ports passent au vert (après quelques secondes).

---

### Étape 2 : Accéder à la CLI du Switch (2 min)

1. **Clic sur SW_BUREAU_01**
2. Onglet **CLI**
3. Appuyer sur **Entrée**
4. Si demande "Initial configuration dialog?" → taper **`no`** puis Entrée

```
Would you like to enter the initial configuration dialog? [yes/no]: no
Press RETURN to get started!
Switch>
```

✅ **Vous êtes en mode User EXEC (prompt `Switch>`)**

---

### Étape 3 : Explorer les Modes (5 min)

```cisco
Switch> ?                        ! Afficher les commandes disponibles en User EXEC

Switch> show version             ! Afficher les informations système

Switch> enable                   ! Passer en mode Privileged EXEC
Switch# ?                        ! Plus de commandes disponibles

Switch# show running-config      ! Afficher la config actuelle (vide pour l'instant)

Switch# configure terminal       ! Passer en mode Global Config
Switch(config)# ?                ! Commandes de configuration

Switch(config)# exit             ! Revenir en Privileged EXEC
Switch#
```

📝 **À noter :** Quelles nouvelles commandes apparaissent en mode Privileged par rapport à User ?

---

### Étape 4 : Configurer le Hostname (3 min)

```cisco
Switch# configure terminal
Switch(config)# hostname SW_BUREAU_01
SW_BUREAU_01(config)#            ! Le prompt a changé !
```

✅ **Validation :** Le prompt affiche maintenant `SW_BUREAU_01`.

---

### Étape 5 : Désactiver la Résolution DNS (1 min)

```cisco
SW_BUREAU_01(config)# no ip domain-lookup
```

💡 **Pourquoi ?** Sans cette commande, si vous faites une faute de frappe, Cisco essaie de résoudre le mot comme un nom DNS → attente de 30 secondes à chaque erreur !

---

### Étape 6 : Configurer le Banner MOTD (5 min)

```cisco
SW_BUREAU_01(config)# banner motd #
Entrez votre message. Terminez avec le caractère '#'.

=========================================
 ACCÈS RÉSERVÉ AU PERSONNEL AUTORISÉ
 Cabinet TechPro SARL - Service Informatique
 Toute connexion non autorisée est illégale.
 Contact DSI : +33 01 23 45 67 89
=========================================
#
SW_BUREAU_01(config)#
```

✅ **Validation :** Taper `end` puis `exit` pour se déconnecter, puis reconnecter → Le banner apparaît.

---

### Étape 7 : Sécuriser le Mode Privilégié (2 min)

```cisco
SW_BUREAU_01(config)# enable secret Cisco@2024
```

✅ **Validation :**
- Taper `end` pour revenir en Privileged
- Taper `disable` pour revenir en User EXEC
- Taper `enable` → le mot de passe est maintenant demandé !

```
SW_BUREAU_01> enable
Password: [taper Cisco@2024 - ne s'affiche pas]
SW_BUREAU_01#
```

---

### Étape 8 : Sécuriser la Ligne Console (5 min)

```cisco
SW_BUREAU_01# configure terminal
SW_BUREAU_01(config)# line console 0
SW_BUREAU_01(config-line)# password Console@2024
SW_BUREAU_01(config-line)# login
SW_BUREAU_01(config-line)# exec-timeout 5 0
SW_BUREAU_01(config-line)# exit
```

---

### Étape 9 : Sécuriser les Lignes VTY (5 min)

```cisco
SW_BUREAU_01(config)# line vty 0 15
SW_BUREAU_01(config-line)# password Vty@2024
SW_BUREAU_01(config-line)# login
SW_BUREAU_01(config-line)# exec-timeout 5 0
SW_BUREAU_01(config-line)# exit
```

---

### Étape 10 : Chiffrer Tous les Mots de Passe (2 min)

```cisco
SW_BUREAU_01(config)# service password-encryption
SW_BUREAU_01(config)# end
```

---

### Étape 11 : Vérification Complète (10 min)

```cisco
SW_BUREAU_01# show running-config
```

**Vérifier ligne par ligne :**

| **Ce qu'on doit voir** | **Trouvé ? ✅/❌** |
|------------------------|-------------------|
| `hostname SW_BUREAU_01` | |
| `no ip domain-lookup` | |
| Message du banner (entre `^C`) | |
| `enable secret 5 $1$...` (hash MD5) | |
| `line con 0` avec `password 7 ...` et `login` | |
| `line vty 0 4` avec `password 7 ...` et `login` | |
| `exec-timeout 5 0` sur con et vty | |

---

### Étape 12 : Observer la Table MAC (5 min)

```cisco
SW_BUREAU_01# show mac address-table
```

📝 La table est peut-être vide. Pour la remplir :

1. Aller sur **PC-Alice** → Desktop → Command Prompt
2. Taper : `ping 192.168.10.20` (vers PC-Bob)
3. Revenir sur le switch, retaper : `show mac address-table`

**Résultat attendu :**
```
          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
   1    0001.xxxx.xxxx    DYNAMIC     Fa0/1
   1    0002.xxxx.xxxx    DYNAMIC     Fa0/2
Total Mac Addresses for this criterion: 2
```

📝 **Questions :**
- Combien d'entrées ? Pourquoi pas PC-Clara ?
- Quel type (DYNAMIC/STATIC) ?
- Après quel délai les entrées disparaîtront-elles ?

---

### Étape 13 : SAUVEGARDER ! (2 min)

```cisco
SW_BUREAU_01# copy running-config startup-config
Destination filename [startup-config]?
Building configuration...
[OK]
```

**Vérification :**
```cisco
SW_BUREAU_01# show startup-config
```
→ La configuration doit être identique à `show running-config`.

---

### Étape 14 : Sauvegarde du Fichier Packet Tracer

1. Menu **File** → **Save As**
2. Nom : `NOM_Prenom_S6_TP_Switch_Config.pkt`
3. Sauvegarder dans votre dossier de travail.

