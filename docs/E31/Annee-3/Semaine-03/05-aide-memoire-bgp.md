# 🗂️ AIDE-MÉMOIRE BGP — À PLASTIFIER
## AS · eBGP vs iBGP · Attributs · Table BGP · BAC PRO CIEL · E31 · 3ᵉ année S3

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## 🌐 BGP en une ligne

```
BGP = protocole de routage ENTRE AS (organisations)
      fait tourner Internet · EGP (pas IGP comme OSPF)
      TCP port 179 · voisins déclarés MANUELLEMENT
```

---

## 🏢 AS et numéros

```
AS = groupe de réseaux sous une même politique de routage
ASN privés  : 64 512 – 65 534  (labs et TP)
ASN publics : 1 – 64 511       (Internet)
Exemples : Free=12322 · Orange=3215 · Google=15169 · CF=13335
```

---

## 🔄 eBGP vs iBGP

```
              eBGP                 iBGP
remote-as     ≠ local AS           = local AS
AS-path       modifié (AS ajouté)  inchangé
Next-hop      modifié              inchangé (⚠️)
Usage         Entre FAI/orgs       Dans un même AS
Session       Lien direct          Via Loopback souvent
```

---

## ⚙️ Configuration de base

```cisco
router bgp 100
 bgp router-id 1.1.1.1
 neighbor 10.0.12.2 remote-as 200     ← eBGP
 neighbor 172.16.1.1 remote-as 100    ← iBGP
 neighbor 172.16.1.1 update-source Loopback0
 network 192.168.1.0 mask 255.255.255.0
! ⚠️ Le réseau DOIT être dans la table de routage !
```

---

## 🎯 3 Attributs clés

```
LOCAL-PREF (défaut=100) :
  Plus HAUT = préféré
  Contrôle la SORTIE de l'AS
  Propagé en iBGP uniquement
  → "Je préfère sortir par FAI_1" (LocPrf=200)

AS-PATH :
  Plus COURT = préféré
  Liste des AS traversés
  Détecte les boucles (propre AS = rejeter)
  → "200 300" (2 AS) < "200 50 300" (3 AS)

MED (défaut=0) :
  Plus BAS = préféré
  Suggère l'ENTRÉE dans l'AS voisin
  Propagé vers l'AS voisin direct uniquement
  → "Entrez par mon lien principal (MED=10)"
```

---

## 📊 Algorithme de sélection BGP

```
1. Weight       (+ haut = préféré)  ← Cisco local
2. Local-Pref   (+ haut = préféré)  ← contrôle sortie
3. Locally originated
4. AS-path      (+ court = préféré) ← compter les AS
5. Origin       (IGP > EGP > ?)
6. MED          (+ bas = préféré)   ← suggestion entrée
7. eBGP > iBGP
8. IGP metric   (+ bas = préféré)
9. Router-ID    (+ bas = préféré)
```

---

## 🔍 Lire show bgp summary

```
Neighbor  V    AS   MsgRcvd  ...  Up/Down    State/PfxRcd
10.0.12.2 4   200     1204   ...  05:23:11       3   ← OK (3 préfixes)
10.0.23.1 4   300       12   ...  00:01:02       8   ← OK
172.16.1.1 4 64512     532   ...  01:05:33       6   ← iBGP (même AS)
10.0.99.2 4   400         0  ...  never       Active ← ❌ Session KO

Chiffre = Established ✓ (X préfixes reçus)
Active  = TCP en tentative ✗ (vérifier remote-as + connectivité IP)
OpenSent = OPEN envoyé, pas encore répondu
```

---

## 🔍 Lire show bgp ipv4 unicast

```
   Network        Next Hop  Metric  LocPrf  Weight  Path
*> 192.168.1.0/24 0.0.0.0       0          32768   i  ← local
*> 203.0.113.0/24 10.0.12.2    0     150       0   200 i  ← BEST
*  203.0.113.0/24 10.0.34.1   20     100       0   300 i  ← alternatif

* = valide (next-hop joignable)
> = best path (installé dans la table de routage)
i seul (sans >) = reçu via iBGP, non best
Next Hop 0.0.0.0 = réseau local
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| remote-as incorrect | Chaque côté déclare l'AS DE L'AUTRE |
| network non dans la table de routage | Vérifier show ip route d'abord |
| Oublier `update-source Lo0` pour iBGP | Ajouter si session via Loopback |
| Confondre eBGP / iBGP | eBGP = AS différents · iBGP = même AS |
| Local-Pref vs MED inversés | LocPrf = sortie + haut · MED = entrée + bas |

---

*Aide-Mémoire BGP — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S3*
*Compétences S2.4 · S2.5 · C2.2 · C2.3*
