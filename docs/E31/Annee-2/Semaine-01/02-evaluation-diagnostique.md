# 📋 ÉVALUATION DIAGNOSTIQUE – S1 ANNÉE 2 – E31
## Plan d'Adressage IP et Routage Statique

**Nom : ________________  Prénom : ________________  Date : ________________**

---

## 📋 CONSIGNES

| **Durée** | 60 minutes |
|---|---|
| **Documents** | Calculatrice autorisée. Aucun document. |
| **Barème** | /40 points |
| **Objectif** | Évaluation diagnostique — non notée pour le bulletin |

> ℹ️ **Cette évaluation permet d'adapter la révision de l'après-midi à vos besoins réels. Si vous ne savez plus, laissez blanc : c'est une information utile. Ne devinez pas.**

---

## EXERCICE 1 – Calcul d'adressage IP (10 pts)

> Pour chaque adresse IP avec son masque, complétez le tableau. Montrez vos calculs dans les cases "calcul".

### 1.1 – Tableau de calcul

| **Adresse IP / Masque** | **Adresse réseau** | **Adresse broadcast** | **1ère @ hôte** | **Dernière @ hôte** | **Nb d'hôtes** |
|---|---|---|---|---|---|
| 192.168.1.130 /25 | | | | | |
| 10.0.0.57 /27 | | | | | |
| 172.16.4.200 /28 | | | | | |
| 192.168.100.14 /30 | | | | | |
| 10.10.5.100 /26 | | | | | |

**Barème :** 2 pts par ligne (0,5 pt par case correcte sur 4 cases principales + 0,5 pt nb hôtes)

---

### 1.2 – Questions courtes (2 pts)

**Q1.a *(1 pt)*** : Un réseau est adressé en 172.16.0.0 /22. Combien d'hôtes peut-il contenir ?

```
Calcul :



Réponse : _______ hôtes
```

**Q1.b *(1 pt)*** : Vous devez créer un sous-réseau pour relier uniquement deux routeurs (liaison point-à-point). Quel préfixe CIDR choisissez-vous pour utiliser le minimum d'adresses ? Justifiez.

_________________________________________________________________________
_________________________________________________________________________

---

## EXERCICE 2 – Plan d'adressage (12 pts)

### Topologie

```
                        ┌─────────────┐
                        │  INTERNET   │
                        └──────┬──────┘
                               │
                          ┌────┴────┐
                          │   R1    │ (routeur FAI / bordure)
                          └────┬────┘
                    ┌──────────┴──────────┐
               ┌────┴────┐          ┌─────┴────┐
               │   R2    │          │    R3    │
               └────┬────┘          └─────┬────┘
             ┌──────┴──────┐    ┌─────────┴─────────┐
          [VLAN 10]    [VLAN 20] [VLAN 30]        [VLAN 40]
         (Direction) (Atelier) (Informatique)  (Production)
```

### Contraintes

| **Segment** | **Nb d'hôtes requis** | **Plage à utiliser** |
|---|---|---|
| VLAN 10 – Direction | 25 hôtes | 192.168.10.0/24 à découper |
| VLAN 20 – Atelier | 50 hôtes | 192.168.10.0/24 à découper |
| VLAN 30 – Informatique | 12 hôtes | 192.168.10.0/24 à découper |
| VLAN 40 – Production | 60 hôtes | 192.168.10.0/24 à découper |
| Liaison R1 – R2 (point à point) | 2 hôtes | 10.0.0.0/30 à 10.0.0.252/30 (choisir) |
| Liaison R1 – R3 (point à point) | 2 hôtes | 10.0.0.0/30 à 10.0.0.252/30 (choisir) |
| Liaison R2 – R3 (point à point) | 2 hôtes | 10.0.0.0/30 à 10.0.0.252/30 (choisir) |

---

### 2.1 – Découpage de 192.168.10.0/24 (6 pts)

> Attribuez un sous-réseau adapté à chaque VLAN. Justifiez le préfixe choisi (il doit correspondre au **plus petit sous-réseau** qui peut contenir le nombre d'hôtes requis).

| **VLAN** | **Nb hôtes req.** | **Préfixe choisi** | **Justification (2^n − 2 ≥ X)** | **Adresse réseau** | **Broadcast** | **Passerelle (1ère @)** |
|---|---|---|---|---|---|---|
| VLAN 10 – Direction | 25 | | | | | |
| VLAN 20 – Atelier | 50 | | | | | |
| VLAN 30 – Info | 12 | | | | | |
| VLAN 40 – Production | 60 | | | | | |

**Barème :** 1,5 pt par VLAN (0,5 pt préfixe + 0,5 pt réseau/broadcast + 0,5 pt justification)

---

### 2.2 – Liaisons point-à-point (3 pts)

> Attribuez un sous-réseau /30 à chaque liaison. Précisez l'adresse de chaque interface routeur.

| **Liaison** | **Réseau /30 choisi** | **IP interface R1 (ou Rx)** | **IP interface R2/R3** |
|---|---|---|---|
| R1 – R2 | | | |
| R1 – R3 | | | |
| R2 – R3 | | | |

**Barème :** 1 pt par liaison (0,5 pt réseau + 0,5 pt IPs)

---

### 2.3 – Plan d'adressage récapitulatif (3 pts)

> Complétez le tableau final récapitulatif.

| **Segment** | **Réseau** | **Masque** | **Passerelle / Interface routeur** |
|---|---|---|---|
| VLAN 10 – Direction | | | |
| VLAN 20 – Atelier | | | |
| VLAN 30 – Informatique | | | |
| VLAN 40 – Production | | | |
| Liaison R1–R2 | | | |
| Liaison R1–R3 | | | |
| Liaison R2–R3 | | | |

---

## EXERCICE 3 – Routage statique (12 pts)

### Topologie simplifiée

```
[PC-A]──────[R1]──────[R2]──────[PC-B]
          Gi0/0  Gi0/1  Gi0/0  Gi0/1
         .1    .1   .2    .1      .10

R1 : Gi0/0 : 192.168.1.1/24   (réseau PC-A : 192.168.1.0/24)
     Gi0/1 : 10.0.0.1/30      (liaison R1-R2 : 10.0.0.0/30)

R2 : Gi0/0 : 10.0.0.2/30      (liaison R1-R2 : 10.0.0.0/30)
     Gi0/1 : 192.168.2.1/24   (réseau PC-B : 192.168.2.0/24)

PC-A : 192.168.1.10/24  — passerelle : 192.168.1.1
PC-B : 192.168.2.10/24  — passerelle : 192.168.2.1
```

---

### 3.1 – Table de routage à compléter (6 pts)

> Complétez les tables de routage de R1 et R2 pour permettre la communication **bidirectionnelle** entre PC-A et PC-B.

**Table de routage R1 :**

| **Type** | **Réseau destination** | **Masque** | **Via (next-hop ou interface)** | **Interface sortie** |
|---|---|---|---|---|
| C | 192.168.1.0 | /24 | — (connecté) | Gi0/0 |
| C | 10.0.0.0 | /30 | — (connecté) | Gi0/1 |
| S | _____________ | _______ | _____________ | Gi0/1 |

**Table de routage R2 :**

| **Type** | **Réseau destination** | **Masque** | **Via (next-hop ou interface)** | **Interface sortie** |
|---|---|---|---|---|
| C | 10.0.0.0 | /30 | — (connecté) | Gi0/0 |
| C | 192.168.2.0 | /24 | — (connecté) | Gi0/1 |
| S | _____________ | _______ | _____________ | Gi0/0 |

**Barème :** 3 pts par table (1,5 pt réseau destination + 0,5 pt masque + 1 pt next-hop)

---

### 3.2 – Commandes IOS (4 pts)

> Écrivez les commandes IOS complètes à saisir sur R1 et R2 pour configurer les routes statiques ci-dessus.

**Sur R1 :**

```
R1(config)# _____________________________________________________
```

**Sur R2 :**

```
R2(config)# _____________________________________________________
```

**Barème :** 2 pts par commande (1 pt syntaxe correcte + 0,5 pt réseau + 0,5 pt next-hop)

---

### 3.3 – Route par défaut (2 pts)

> R1 est également connecté à Internet via son interface Gi0/2 (adresse IP fournie par le FAI). Écrivez la commande de route par défaut à configurer sur R1, avec next-hop 203.0.113.1.

```
R1(config)# _____________________________________________________
```

Que se passerait-il si cette route par défaut n'était pas configurée mais qu'un PC-A essaie de joindre un serveur sur Internet ?

_________________________________________________________________________
_________________________________________________________________________

---

## EXERCICE 4 – Débogage d'une configuration (6 pts)

### Situation

> Un technicien junior a configuré trois routeurs R1, R2 et R3. Des machines sur le réseau de R3 (192.168.3.0/24) n'arrivent pas à joindre les machines sur le réseau de R1 (192.168.1.0/24). En revanche, R1 → R2 fonctionne.

### Topologie

```
[Net-A]──[R1]──[R2]──[R3]──[Net-C]
192.168.1.0/24  10.0.0.0/30 10.0.0.4/30 192.168.3.0/24
```

### Configuration actuelle

**R1 :**
```
ip route 192.168.2.0 255.255.255.0 10.0.0.2
ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

**R2 :**
```
ip route 192.168.1.0 255.255.255.0 10.0.0.1
ip route 192.168.3.0 255.255.255.0 10.0.0.6
```

**R3 :**
```
ip route 192.168.1.0 255.255.255.0 10.0.0.5
ip route 0.0.0.0 0.0.0.0 10.0.0.5
```

---

**Q4.1 *(2 pts)*** : Analysez les tables de routage ci-dessus. Quelle route est manquante ou incorrecte pour que Net-C (192.168.3.0/24) puisse joindre Net-A (192.168.1.0/24) ? Identifiez **précisément le routeur et la route problématique**.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**Q4.2 *(2 pts)*** : Écrivez la commande de correction à saisir sur le routeur concerné.

```
RX(config)# _____________________________________________________
```

**Q4.3 *(2 pts)*** : Le technicien vous dit : *"Mais j'ai mis une route par défaut sur R3, ça devrait suffire pour tout joindre depuis Net-C !"* Expliquez pourquoi cette affirmation est **partiellement vraie et partiellement fausse**.

_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

---

## 📊 GRILLE DE AUTO-POSITIONNEMENT POST-DIAGNOSTIC

> *À remplir après correction collective*

| **Exercice** | **Points obtenus** | **Points max** | **Maîtrise** |
|---|---|---|---|
| Ex. 1 – Calcul d'adressage | | /10 | ✅ ⚠️ ❌ |
| Ex. 2 – Plan d'adressage | | /12 | ✅ ⚠️ ❌ |
| Ex. 3 – Routage statique | | /12 | ✅ ⚠️ ❌ |
| Ex. 4 – Débogage | | /6 | ✅ ⚠️ ❌ |
| **TOTAL** | | **/40** | |

**→ Mon profil de révision : A ☐ B ☐ C ☐ Expert ☐**

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
