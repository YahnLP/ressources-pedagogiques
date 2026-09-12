# 🔍 ACTIVITÉ DE DÉCOUVERTE — S2 · 2ᵉ ANNÉE · E31
## « L'appel SOS » — Diagnostiquer une panne de routage sans toucher aux équipements

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche · Stylo
> **Principe** : Tu as accès aux sorties de commandes des routeurs, mais PAS aux équipements en direct. Tu dois identifier les pannes uniquement par l'analyse des tables de routage.

---

## 🎯 Mise en situation

> Il est 18h30. Tu reçois un appel du responsable de production d'une usine :
> *"Nos machines de l'atelier Sud ne communiquent plus avec le serveur ERP dans le datacenter.
> Les techniciens partent dans 30 minutes. Tu peux diagnostiquer à distance ?"*
>
> Tu as accès à la console des 3 routeurs via SSH.
> Tu relèves les tables de routage. Les voici.

---

## 🗺️ Topologie du réseau

```
         LAN Atelier Sud          LAN Datacenter
         192.168.20.0/24          192.168.99.0/24
               │                        │
            Gi0/0                     Gi0/0
           ┌──────┐  10.0.12.0/30  ┌──────┐  10.0.23.0/30  ┌──────┐
           │  R1  ├─ Gi0/1──Gi0/0 ─┤  R2  ├─ Gi0/1──Gi0/0 ─┤  R3  │
           └──────┘                └──────┘                 └──────┘

Adresses :
  R1 Gi0/0 : 192.168.20.1    R1 Gi0/1 : 10.0.12.1
  R2 Gi0/0 : 10.0.12.2       R2 Gi0/1 : 10.0.23.1
  R3 Gi0/0 : 10.0.23.2       R3 Gi0/1 : 192.168.99.1
  Machine atelier : 192.168.20.50   Serveur ERP : 192.168.99.10
```

---

## 📋 Tables de routage relevées à distance

### R1 — `show ip route`

```
Codes: C - connected, S - static, O - OSPF

C    192.168.20.0/24 is directly connected, GigabitEthernet0/0
C    10.0.12.0/30 is directly connected, GigabitEthernet0/1
S    10.0.23.0/30 [1/0] via 10.0.12.2
```

---

### R2 — `show ip route`

```
Codes: C - connected, S - static, O - OSPF

C    10.0.12.0/30 is directly connected, GigabitEthernet0/0
C    10.0.23.0/30 is directly connected, GigabitEthernet0/1
S    192.168.20.0/24 [1/0] via 10.0.12.1
S    192.168.99.0/16 [1/0] via 10.0.23.2
```

---

### R3 — `show ip route`

```
Codes: C - connected, S - static, O - OSPF

C    10.0.23.0/30 is directly connected, GigabitEthernet0/0
C    192.168.99.0/24 is directly connected, GigabitEthernet0/1
S    10.0.12.0/30 [1/0] via 10.0.23.1
S    192.168.20.0/24 [1/0] via 10.1.99.1
```

---

## 🔍 PARTIE 1 — Je lis les tables de routage (10 min)

**Question 1.1** — Sur R1, combien y a-t-il de routes ? Donne le type de chacune.

```
Nombre de routes : _______

Route 1 : type ___  réseau ___________________  source _______________
Route 2 : type ___  réseau ___________________  source _______________
Route 3 : type ___  réseau ___________________  source _______________
```

**Question 1.2** — R1 a-t-il une route vers le **réseau du datacenter** (192.168.99.0/24) ?

```
☐ Oui — via : _______________
☐ Non — cette route est ABSENTE de la table
```

**Question 1.3** — Que se passe-t-il quand R1 reçoit un paquet destiné à 192.168.99.10 (le serveur ERP) ?

```
R1 cherche dans sa table une route vers : _______________________
Il trouve : ☐ Une route correspondante ☐ Aucune route
Action de R1 : _______________________________________________________________
```

**Question 1.4** — Sur R2, la route vers 192.168.99.0 a le masque `/16`. Le réseau réel du datacenter est en `/24`.
Est-ce une erreur ? Quel impact cela a-t-il ?

```
Route inscrite : 192.168.99.0 / _______   Route correcte : 192.168.99.0 / _______
Erreur détectée : ☐ Oui ☐ Non
Impact : ___________________________________________________________________
```

---

## 🔍 PARTIE 2 — Je détecte les pannes (15 min)

**Question 2.1** — Sur R3, la route vers 192.168.20.0/24 pointe vers le next-hop `10.1.99.1`.
Regarde la topologie. Cette adresse existe-t-elle sur un des équipements du réseau ?

```
Interfaces de R3 : Gi0/0 = 10.0.23.2   Gi0/1 = 192.168.99.1
Next-hop configuré sur R3 : 10.1.99.1
Cette adresse appartient au réseau 10.0.23.0/30 ? ☐ Oui ☐ Non
Cette adresse est-elle joignable depuis R3 ? ☐ Oui ☐ Non
Type de panne : _____________________________________________________________
```

**Question 2.2** — Récapitule les pannes identifiées dans le tableau suivant :

| Routeur | Panne | Type de panne | Route concernée |
|---|---|---|---|
| **R1** | | | |
| **R2** | | | |
| **R3** | | | |

**Question 2.3** — Sans aucune correction, quel est le chemin qu'un paquet de `192.168.20.50` vers `192.168.99.10` essaie d'emprunter ? À quelle étape est-il perdu ?

```
192.168.20.50 → R1 → ??? 
Paquet perdu à : R1 ☐   R2 ☐   R3 ☐
Car : ______________________________________________________________________
```

---

## 🔧 PARTIE 3 — Je corrige les commandes (10 min)

> Pour chaque panne identifiée, écris la commande IOS à exécuter pour la corriger.
> Format : `ip route [réseau] [masque] [next-hop]`
> Supprimer une route : `no ip route [réseau] [masque] [next-hop]`

**Correction panne R1 :**

```
R1(config)# ip route _________________ _________________ _________________
```

**Correction panne R2 :**

*(deux étapes : supprimer la mauvaise route, ajouter la bonne)*

```
R2(config)# no ip route _________________ _________________ _________________
R2(config)# ip route _________________ _________________ _________________
```

**Correction panne R3 :**

```
R3(config)# no ip route _________________ _________________ _________________
R3(config)# ip route _________________ _________________ _________________
```

---

## 🏁 Bilan de l'atelier

**Complète avec tes propres mots :**

```
Les 4 types de pannes de routage les plus fréquentes sont :
1. ______________________________________________________________________
2. ______________________________________________________________________
3. ______________________________________________________________________
4. ______________________________________________________________________

Pour diagnostiquer une panne de routage, la première commande à taper est :
→ _______________________________________________________________________

La route par défaut s'écrit : ip route _______ _______ [next-hop]
```

> ✅ Tu viens de résoudre 3 pannes de routage réelles en lisant uniquement les tables.
> Le TP va maintenant te permettre de corriger ces pannes directement sur les routeurs
> et de vérifier avec `ping` et `traceroute` que la communication est rétablie.

---

## 📎 Pour l'enseignant — Réponses

**Pannes :**
1. R1 : **Route manquante** vers 192.168.99.0/24 → `ip route 192.168.99.0 255.255.255.0 10.0.12.2`
2. R2 : **Masque incorrect** 192.168.99.0**/16** → `no ip route 192.168.99.0 255.255.0.0 10.0.23.2` puis `ip route 192.168.99.0 255.255.255.0 10.0.23.2`
3. R3 : **Next-hop injoignable** 10.1.99.1 n'existe pas → `no ip route 192.168.20.0 255.255.255.0 10.1.99.1` puis `ip route 192.168.20.0 255.255.255.0 10.0.23.1`

**Question 2.3** : Le paquet est perdu dès **R1** (aucune route vers 192.168.99.0/24 → drop immédiat)

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S2*
*Compétences : C2.3 · S2.3*
