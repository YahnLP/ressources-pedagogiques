# 🎲 ACTIVITÉ REMOBILISATION – S1 ANNÉE 2 – E31
## Retour en Piste : Adressage IP et Routage Statique

---

## 🎯 OBJECTIFS

- ✅ Réactiver les connaissances d'A1 sur l'adressage IP
- ✅ Repérer collectivement ce qui est encore acquis / à consolider
- ✅ Mettre les apprentis en **posture active** avant le diagnostic
- ✅ Créer un climat de confiance (diagnostic non punitif)

---

## ⏱️ DURÉE : 25 min

---

## ⚙️ MISE EN PLACE (2 min)

**Message du formateur :**

> *"Bienvenue en A2. Avant d'attaquer OSPF — qui est le protocole de routage dynamique que vous utiliserez dans la vraie vie professionnelle — je dois savoir où vous en êtes. On commence par réactiver ce qu'on a vu l'an dernier. C'est un retour en douceur, pas un interrogatoire. Les erreurs sont normales après les vacances d'été."*

---

## 🔥 PHASE 1 – Questions flash (10 min)

**Format : le formateur pose les questions à l'oral, les apprentis répondent sur une feuille ou ardoise. Correction immédiate après chaque question.**

---

### Bloc A – Adressage IP (5 questions)

**Q1.** Quelle est la différence entre une adresse IP et une adresse réseau ?

> **Réponse attendue :** L'adresse IP identifie un hôte précis. L'adresse réseau (tous les bits de la partie hôte à 0) identifie le réseau auquel appartient l'hôte.

---

**Q2.** Donnez le masque en décimale pointée correspondant à /27.

> **Réponse attendue :** 255.255.255.224 (car 3 bits hôtes : 256 − 32 = 224)

---

**Q3.** Combien d'hôtes peut-on adresser dans un réseau /28 ?

> **Réponse attendue :** 2⁴ − 2 = **14 hôtes** (16 adresses − réseau − broadcast)

---

**Q4.** Pour l'adresse 192.168.10.65/26 : quelle est l'adresse réseau ?

> **Réponse attendue :** /26 → incrément 64 → sous-réseaux : .0, .64, .128, .192 → .65 est dans le bloc .64 → **réseau : 192.168.10.64/26**

---

**Q5.** Qu'est-ce que l'adresse de broadcast d'un réseau ? Donnez-la pour 192.168.10.64/26.

> **Réponse attendue :** C'est la dernière adresse du réseau (bits hôtes tous à 1), utilisée pour envoyer à tous les hôtes du réseau. Pour .64/26 : .64 + 64 − 1 = **.127** → broadcast = **192.168.10.127**

---

### Bloc B – Routage statique (5 questions)

**Q6.** Quelle est la différence entre un switch et un routeur ?

> **Réponse attendue :** Le switch travaille en couche 2 (trames Ethernet, adresses MAC) et relie des hôtes dans un même réseau. Le routeur travaille en couche 3 (paquets IP) et interconnecte des réseaux différents.

---

**Q7.** Complétez la commande IOS suivante pour que le routeur R1 joigne le réseau 10.0.2.0/24 via le next-hop 10.0.1.2 :

```
R1(config)# ip route _____ _____ _____
```

> **Réponse attendue :** `ip route 10.0.2.0 255.255.255.0 10.0.1.2`

---

**Q8.** Qu'est-ce qu'une route par défaut ? Donnez sa syntaxe IOS.

> **Réponse attendue :** Une route qui s'applique à tout paquet dont la destination ne correspond à aucune route spécifique. Syntaxe : `ip route 0.0.0.0 0.0.0.0 <next-hop>`

---

**Q9.** Un routeur a deux interfaces : Gi0/0 (192.168.1.1/24) et Gi0/1 (10.0.0.1/30). Un PC sur le réseau 192.168.1.0/24 envoie un paquet vers 10.0.5.1. Quelle interface de sortie le routeur utilisera-t-il (si une route existe) ?

> **Réponse attendue :** Gi0/1 (car c'est l'interface qui donne accès au réseau 10.x.x.x, vers le prochain routeur)

---

**Q10.** Que signifie la lettre **S** au début d'une ligne dans la table de routage (`show ip route`) ?

> **Réponse attendue :** S = Static (route configurée manuellement par `ip route`). Les autres codes courants : C = Connected, R = RIP, O = OSPF, D = EIGRP.

---

## 📊 PHASE 2 – Auto-positionnement (8 min)

### Grille d'auto-positionnement individuelle

> **Complète honnêtement ce tableau. Ce n'est pas noté.**

| **Compétence** | **Je maîtrise** ✅ | **J'hésite** ⚠️ | **J'ai oublié** ❌ |
|---|---|---|---|
| Calculer l'adresse réseau depuis IP/masque | | | |
| Calculer l'adresse de broadcast | | | |
| Calculer le nombre d'hôtes utilisables | | | |
| Convertir CIDR ↔ masque décimal (/27, /28, /29, /30) | | | |
| Construire un plan d'adressage pour plusieurs réseaux | | | |
| Lire une table de routage (`show ip route`) | | | |
| Écrire une commande `ip route` | | | |
| Écrire une route par défaut | | | |
| Comprendre le concept de next-hop | | | |

### Question ouverte

**Selon toi, quel est le point de l'adressage/routage statique sur lequel tu te sens le moins à l'aise ?**

_________________________________________________________________________

_________________________________________________________________________

---

## 🎤 PHASE 3 – Bilan collectif (5 min)

**Le formateur demande à main levée :**

> - *"Qui s'est mis au moins 3 fois '❌ J'ai oublié' ?"* → Profil A probable
> - *"Qui hésite sur les calculs de masques mais se souvient du principe de routage ?"* → Profil B probable
> - *"Qui a surtout oublié la syntaxe exacte des commandes ?"* → Profil C probable
> - *"Qui pense avoir tout ?"* → Profil Expert

**Message de conclusion avant l'évaluation :**

> *"Parfait. Dans 5 minutes, vous allez faire le diagnostic. 60 minutes, en silence, calculatrice autorisée. Ce que vous ne savez plus, laissez blanc plutôt que d'inventer — ça m'aide à mieux calibrer la révision de cet après-midi. Allez."*

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
