# 🔍 ACTIVITÉ DE DÉCOUVERTE — S3 · 3ᵉ ANNÉE · E31
## « Le carnet d'adresses d'Internet » — Décoder BGP sans cours préalable

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche uniquement
> **Principe** : On te présente des sorties BGP réelles d'un routeur de FAI. Tu dois comprendre ce qui se passe avant tout cours.

---

## 🎯 Mise en situation

> Tu es **stagiaire chez un FAI régional** (AS 64512 — fictif).
> Ton responsable part en réunion et te laisse devant un terminal avec ces mots :
> *"Surveille les voisins BGP. Si quelque chose passe en rouge, appelle-moi."*
> Tu ne connais pas BGP. Tu dois comprendre ce que tu vois.

---

## 📋 Sortie 1 — `show bgp summary` sur le routeur de bordure

```
BGP router identifier 1.1.1.1, local AS number 64512
BGP table version is 47, main routing table version 47
14 network entries using 2016 bytes of memory
18 path entries using 1584 bytes of memory

Neighbor        V    AS     MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down  State/PfxRcd
10.0.12.2       4   200       1204      1198       47     0    0  05:23:11        3
10.0.34.1       4   300        891       897       47     0    0  02:11:44        8
172.16.1.1      4 64512        532       528       47     0    0  01:05:33        6
192.168.1.2     4 64512          0         0        0     0    0  never       Active
```

---

## 📋 Sortie 2 — `show bgp ipv4 unicast` (table BGP complète)

```
BGP table version is 47, local router ID is 1.1.1.1
Status codes: s suppressed, d damped, h history, * valid, > best, i internal
Origin codes: i - IGP, e - EGP, ? - incomplete

   Network          Next Hop        Metric  LocPrf  Weight  Path
*> 10.0.12.0/30     0.0.0.0              0          32768   i
*> 10.0.34.0/30     0.0.0.0              0          32768   i
*> 192.168.100.0/24 0.0.0.0              0          32768   i
*  203.0.113.0/24   10.0.34.1           20     100       0   300 i
*> 203.0.113.0/24   10.0.12.2            0     150       0   200 i
*> 198.51.100.0/24  10.0.34.1            0     100       0   300 100 i
   203.0.114.0/24   10.0.12.2                           0   200 i
```

---

## 🔍 PARTIE 1 — Comprendre les voisins (12 min)

**Question 1.1** — Dans `show bgp summary`, combien de voisins BGP ce routeur a-t-il ? Relève leur adresse IP et leur numéro d'AS :

| Adresse voisin | Numéro AS | Voisin dans le même AS ? |
|---|---|---|
| 10.0.12.2 | | ☐ Oui ☐ Non |
| 10.0.34.1 | | ☐ Oui ☐ Non |
| 172.16.1.1 | | ☐ Oui ☐ Non |
| 192.168.1.2 | | ☐ Oui ☐ Non |

> **Indice** : le routeur local est dans l'AS **64512** (voir la première ligne).

**Question 1.2** — La colonne `State/PfxRcd` affiche soit un nombre, soit un état texte. Qu'est-ce que ces valeurs indiquent selon toi ?

```
Voisin 10.0.12.2 → State/PfxRcd = 3      signifie : ____________________________
Voisin 10.0.34.1 → State/PfxRcd = 8      signifie : ____________________________
Voisin 172.16.1.1 → State/PfxRcd = 6     signifie : ____________________________
Voisin 192.168.1.2 → State/PfxRcd = Active signifie : ___________________________
```

**Question 1.3** — Le voisin 192.168.1.2 est dans l'AS 64512 (même AS que nous). Il est en état `Active`. C'est un problème ?

```
☐ Oui — il ne s'est jamais connecté (Up/Down = "never", State = "Active" = en tentative)
☐ Non — "Active" signifie qu'il est opérationnel
Que faudrait-il vérifier pour comprendre pourquoi il ne se connecte pas ?
___________________________________________________________________________
```

**Question 1.4** — Les voisins dans le **même AS** (AS 64512) forment une session BGP d'un type particulier. Les voisins dans un **AS différent** forment un autre type. Comment appellera-t-on ces deux types selon toi ?

```
Voisin dans AS différent → peering de type : ___________________________________
Voisin dans même AS      → peering de type : ___________________________________
```

---

## 🔍 PARTIE 2 — Lire la table BGP (13 min)

**Question 2.1** — Dans `show bgp ipv4 unicast`, deux symboles précèdent chaque route : `*` et `>`.
D'après le contexte, que signifient-ils ?

```
*  (astérisque) signifie probablement : _______________________________________
>  (chevron)    signifie probablement : _______________________________________
Une route marquée uniquement `*` sans `>` est-elle utilisée pour le routage ? ☐ Oui ☐ Non
```

**Question 2.2** — Le réseau `203.0.113.0/24` apparaît **deux fois** dans la table BGP :

```
*  203.0.113.0/24   10.0.34.1   Metric=20  LocPrf=100  via AS 300
*> 203.0.113.0/24   10.0.12.2   Metric=0   LocPrf=150  via AS 200
```

Le routeur a choisi le chemin via AS 200 (marqué `>`). En observant les colonnes `LocPrf`, quelle est la règle ?

```
Via AS 200 : LocPrf = _______
Via AS 300 : LocPrf = _______
Le chemin avec la valeur LocPrf la PLUS ______ est préféré.
Cette colonne s'appelle : ________________________
```

**Question 2.3** — La colonne `Path` contient des numéros d'AS. Pour `198.51.100.0/24` :

```
Path = "300 100 i"
Cela signifie que ce préfixe a été annoncé par AS _______,
qui l'a reçu de AS _______, qui l'a reçu d'un réseau originel annoté "i" (IGP).
Nombre d'AS traversés pour atteindre ce réseau depuis notre AS : _______
```

**Question 2.4** — La route `203.0.114.0/24` n'a pas de `*` ni de `>`. À quoi servent les lignes sans symboles ?

```
☐ Ce sont des routes désactivées (blackhole)
☐ Ce sont des routes invalides (next-hop inaccessible ou autre problème)
☐ Ce sont des routes en attente de validation
```

---

## 🔍 PARTIE 3 — Relier à la logique Internet (10 min)

**Question 3.1** — Dans OSPF, tous les routeurs d'une même aire ont la même LSDB. En BGP, est-ce la même chose ? Que contient la table BGP ?

```
Table OSPF (LSDB) contient : ________________________________________________
Table BGP contient : _________________________________________________________
```

**Question 3.2** — OSPF recalcule en ~40 secondes si un lien tombe. D'après la colonne `Up/Down` (temps depuis que la session est établie), que penses-tu de la stabilité des sessions BGP ?

```
Temps de session le plus long observé : _______________________________________
BGP semble être un protocole : ☐ qui reconverge vite ☐ qui privilégie la stabilité
Raison (pense à Internet) : ___________________________________________________
```

**Question 3.3** — Pourquoi, à ton avis, BGP utilise-t-il des **numéros d'AS** plutôt que des adresses IP de routeurs pour identifier les chemins ?

```
L'AS-path "200 300" signifie : passage par l'AS 200 puis l'AS 300
Si on utilisait des IPs de routeurs : ________________________________________
L'avantage du numéro d'AS : __________________________________________________
```

---

## 🏁 Bilan

```
BGP est utilisé pour : ______________________________________________________
Un AS (Système Autonome) est : ______________________________________________
eBGP = session entre AS ____________________
iBGP = session entre routeurs du même AS ___________________

Dans show bgp summary :
  Un chiffre dans State/PfxRcd → le voisin est ______________ et a reçu _______ préfixes
  "Active" dans State/PfxRcd  → le voisin est ______________ (problème de session)

Trois attributs influencent le choix du meilleur chemin BGP :
  1. _________________ (plus haut = préféré) → choix de sortie depuis l'AS
  2. _________________ (plus court = préféré) → compte les AS traversés
  3. _________________ (plus bas = préféré)  → suggestion d'entrée dans l'AS voisin
```

---

## 📎 Pour l'enseignant — Réponses

**1.1** : 10.0.12.2 → AS 200 (différent) · 10.0.34.1 → AS 300 (différent) · 172.16.1.1 → AS 64512 (même) · 192.168.1.2 → AS 64512 (même)

**1.2** : Chiffre = session Established, X préfixes reçus · Active = session en tentative de connexion TCP (problème de peering)

**1.3** : Problème — vérifier connectivité IP, config `neighbor`, AS correct

**1.4** : AS différent → eBGP · même AS → iBGP

**2.1** : `*` = route valide (next-hop joignable) · `>` = meilleure route (best path, installée dans la RIB) · route sans `>` = valide mais pas choisie comme best

**2.2** : LocPrf 150 > 100 → plus haut = préféré → Local-Preference

**2.3** : Path "300 100 i" → AS 300 a annoncé, qui l'avait reçu d'AS 100 · 2 AS traversés

**2.4** : Routes invalides (next-hop inaccessible ou autre problème de validation)

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S3*
*Compétences : S2.4 · S2.5 · C2.3*
