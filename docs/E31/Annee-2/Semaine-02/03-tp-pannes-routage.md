# 🔬 TRAVAUX PRATIQUES — S2 · 2ᵉ ANNÉE · E31
## Mission : Résoudre 3 pannes de routage statique — Compte rendu d'intervention

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________ **Groupe** : ___________________________
> **Durée** : 80 minutes · **Fiche méthode autorisée** · **Packet Tracer**
> **Fichier .pkt** : `S2_E31_TP_Pannes_Routage.pkt` (fourni par l'enseignant)
> **Épreuve ciblée** : **E31** – Épreuve pratique infrastructure réseau

---

## 📌 Compétences travaillées

| Code | Compétence | Niveau attendu |
|---|---|---|
| **C2.2** | Configurer les équipements actifs | Corriger les routes statiques sous IOS |
| **C2.3** | Diagnostiquer un dysfonctionnement | Appliquer la méthode 5 étapes |
| **C3.1** | Rédiger un compte rendu d'intervention | Compléter le document au format professionnel |
| **S2.3** | Table de routage | Lire, interpréter, identifier les anomalies |

---

## 🗺️ Topologie du TP

```
           LAN1                     LAN4
      192.168.10.0/24          192.168.40.0/24
            │                        │
         Gi0/0                     Gi0/1
        ┌──────┐  10.1.2.0/30   ┌──────┐  10.2.3.0/30   ┌──────┐
        │  R1  ├─Gi0/1─── Gi0/0─┤  R2  ├─Gi0/1───Gi0/0─┤  R3  │
        └──────┘                └──────┘                 └──────┘
         PC1                                               PC4
     192.168.10.10                                   192.168.40.10

Adresses des interfaces :
  R1 Gi0/0 : 192.168.10.1/24    R1 Gi0/1 : 10.1.2.1/30
  R2 Gi0/0 : 10.1.2.2/30        R2 Gi0/1 : 10.2.3.1/30
  R3 Gi0/0 : 10.2.3.2/30        R3 Gi0/1 : 192.168.40.1/24
```

---

## 🎯 Mission

> Le réseau vient d'être livré par un prestataire mais **PC1 ne peut pas joindre PC4**.
> Le prestataire affirme avoir configuré toutes les routes statiques nécessaires.
> **Ta mission** : trouver les pannes, les corriger, et documenter chaque intervention.

---

## 🔵 ÉTAPE 1 — État initial : symptômes

**1.1** — Depuis PC1, effectue un `ping 192.168.40.10`. Résultat ?

```
Commande saisie : ping _______________________
Résultat : ☐ Succès (!!!)  ☐ Timeout (....)  ☐ Unreachable (U)
Interprétation : __________________________________________________________
```

**1.2** — Depuis PC1, effectue un `tracert 192.168.40.10`. Note les résultats :

```
Hop 1 : _____________ (temps : _____)  →  ☐ Réponse ☐ * * * (timeout)
Hop 2 : _____________ (temps : _____)  →  ☐ Réponse ☐ * * * (timeout)
Hop 3 : _____________ (temps : _____)  →  ☐ Réponse ☐ * * * (timeout)
Hop 4 : _____________ (temps : _____)  →  ☐ Réponse ☐ * * * (timeout)

Le paquet s'arrête après le hop n° : _______   à l'équipement : _____________
```

---

## 🔴 PANNE 1 — Route manquante

### Diagnostic

**1.3** — Sur R1, affiche la table de routage : `show ip route`

Recopie les lignes affichées :

```
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
_____________________________________________________________________________
```

**1.4** — Analyse : R1 a-t-il une route vers le réseau **192.168.40.0/24** (réseau de PC4) ?

```
☐ Oui — via : _______________
☐ Non — route ABSENTE

Type de panne : ________________________
```

**1.5** — Identifie également : R1 a-t-il une route vers le réseau **10.2.3.0/30** (WAN R2-R3) ?

```
☐ Oui ☐ Non — nécessaire ? ________________________
(Une route vers 10.2.3.0/30 est-elle obligatoire pour que R1 joigne PC4 ?)
```

### Correction

**1.6** — Écris et applique la commande pour corriger la panne sur R1 :

```
R1> enable
R1# configure terminal
R1(config)# ip route _________________ _________________ _________________
R1(config)# end
R1# show ip route
```

**1.7** — Vérifie que la route est bien présente dans la table après correction.
Recopie la ligne concernée :

```
_____________________________________________________________________________
```

---

## 🔴 PANNE 2 — Masque incorrect

### Diagnostic

**2.1** — Sur R2, affiche la table de routage et note les routes statiques configurées :

```
Routes statiques sur R2 :
S  _________________ [1/0] via _________________
S  _________________ [1/0] via _________________
```

**2.2** — Compare les masques des routes de R2 avec les masques réels des réseaux de la topologie.
Y a-t-il une incohérence ?

```
Route sur R2 vers 192.168.40.0 : masque = _______________
Masque réel du réseau 192.168.40.0 dans la topologie : _______________
Incohérence : ☐ Oui — le masque configuré est /_______ au lieu de /_______
              ☐ Non

Type de panne : ________________________
```

**2.3** — Quel est l'impact d'un masque trop large (ex: /16 au lieu de /24) ?

```
Avec le masque /16 : R2 croit connaître le réseau _______._______.0.0/16
Cela englobe tous les réseaux commençant par _______._______.
Problème concret : ___________________________________________________________
```

### Correction

**2.4** — Écris et applique les commandes pour corriger le masque sur R2 :

```
R2(config)# no ip route _________________ _________________ _________________
                          ← SUPPRIMER la mauvaise route d'abord

R2(config)# ip route _________________ _________________ _________________
                          ← AJOUTER la route corrigée
R2(config)# end
```

---

## 🔴 PANNE 3 — Next-hop injoignable

### Diagnostic

**3.1** — Sur R3, affiche la table de routage et note les routes statiques :

```
Routes statiques sur R3 :
S  _________________ [1/0] via _________________
S  _________________ [1/0] via _________________
```

**3.2** — Depuis R3, ping le next-hop configuré pour la route vers 192.168.10.0/24 :

```
Adresse du next-hop configuré : _________________
R3# ping _________________
Résultat : ☐ Succès  ☐ Timeout  ☐ Unreachable

Le next-hop est-il joignable ? ☐ Oui ☐ Non
```

**3.3** — Compare l'adresse next-hop configurée avec les adresses réelles des interfaces R3 et de ses voisins.

```
Next-hop configuré sur R3 pour LAN1 : _________________
Adresses réellement disponibles sur le lien WAN23 :
  R2 Gi0/1 : _________________
  R3 Gi0/0 : _________________
La bonne adresse de next-hop aurait dû être : _________________
Type de panne : ________________________
```

### Correction

**3.4** — Écris et applique les commandes pour corriger le next-hop sur R3 :

```
R3(config)# no ip route _________________ _________________ _________________
R3(config)# ip route _________________ _________________ _________________
R3(config)# end
```

---

## ✅ ÉTAPE 2 — Vérification globale

**Après correction des 3 pannes**, effectue les tests suivants et note les résultats :

| Test | Commande | Résultat attendu | Résultat obtenu |
|---|---|---|---|
| PC1 → PC4 | ping 192.168.40.10 | Succès !!!! | |
| PC4 → PC1 | ping 192.168.10.10 | Succès !!!! | |
| PC1 → R3 Gi0/1 | ping 192.168.40.1 | Succès !!!! | |
| R1 → PC4 | ping 192.168.40.10 source Gi0/0 | Succès !!!! | |
| Traceroute PC1 → PC4 | tracert 192.168.40.10 | 4 hops, pas de * | |

**La communication est-elle rétablie ?** ☐ Oui — TP réussi ✓   ☐ Non — chercher la panne restante

---

## 📄 COMPTE RENDU D'INTERVENTION

> **Rédige le compte rendu professionnel de ton intervention.
> Un technicien qui n'a pas participé au TP doit pouvoir comprendre ce qui s'est passé.**

---

```
┌─────────────────────────────────────────────────────────────────────────┐
│               COMPTE RENDU D'INTERVENTION RÉSEAU                       │
│               Réf. : S2-E31-CR-_______  Date : _______________         │
├─────────────────────────────────────────────────────────────────────────┤
│  Technicien : _______________________  Binôme : ______________________  │
│  Client fictif : Atelier Sud / Datacenter  Site : ____________________  │
├─────────────────────────────────────────────────────────────────────────┤
│  1. DESCRIPTION DU PROBLÈME INITIAL                                    │
│                                                                         │
│  _____________________________________________________________________ │
│  _____________________________________________________________________ │
│  _____________________________________________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  2. DIAGNOSTIC — MÉTHODE APPLIQUÉE                                     │
│                                                                         │
│  Commandes utilisées :                                                  │
│  _____________________________________________________________________ │
│  _____________________________________________________________________ │
│  Localisation du problème : ___________________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  3. PANNES IDENTIFIÉES ET CORRECTIONS APPLIQUÉES                       │
│                                                                         │
│  PANNE 1 — sur R___ :                                                  │
│  Nature : _____________________________________________________________ │
│  Commande appliquée : _________________________________________________ │
│                                                                         │
│  PANNE 2 — sur R___ :                                                  │
│  Nature : _____________________________________________________________ │
│  Commandes appliquées : _______________________________________________ │
│  _____________________________________________________________________ │
│                                                                         │
│  PANNE 3 — sur R___ :                                                  │
│  Nature : _____________________________________________________________ │
│  Commandes appliquées : _______________________________________________ │
│  _____________________________________________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  4. TESTS DE VALIDATION POST-CORRECTION                                │
│                                                                         │
│  PC1 → PC4 : ☐ OK    PC4 → PC1 : ☐ OK    Traceroute complet : ☐ OK   │
│                                                                         │
│  Commentaire : _________________________________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  5. RECOMMANDATIONS                                                     │
│  (Que faudrait-il mettre en place pour éviter ce type de panne ?)     │
│                                                                         │
│  _____________________________________________________________________ │
│  _____________________________________________________________________ │
├─────────────────────────────────────────────────────────────────────────┤
│  Visa technicien : ___________________   Visa enseignant : ____________ │
│  Durée d'intervention : _______ min      Date clôture : ______________ │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## ✅ Auto-évaluation

| Compétence | Maîtrisé | En cours | À revoir |
|---|---|---|---|
| Lire une table de routage IOS | ☐ | ☐ | ☐ |
| Identifier une route manquante | ☐ | ☐ | ☐ |
| Identifier un masque incorrect | ☐ | ☐ | ☐ |
| Identifier un next-hop injoignable | ☐ | ☐ | ☐ |
| Écrire la commande ip route correcte | ☐ | ☐ | ☐ |
| Utiliser ping / traceroute / show ip route | ☐ | ☐ | ☐ |
| Rédiger un compte rendu d'intervention | ☐ | ☐ | ☐ |

---

## ✍️ Validation enseignant

| Critère | /pts |
|---|---|
| Diagnostic Panne 1 correct + commande appliquée | /5 |
| Diagnostic Panne 2 correct + commandes appliquées | /5 |
| Diagnostic Panne 3 correct + commandes appliquées | /5 |
| Tests de validation ping réussis | /5 |
| Compte rendu complet et professionnel | /5 |
| **TOTAL** | **/25** |

---

---

# ✅ CORRECTION DU TP — Document enseignant uniquement

## Correction Panne 1 — Route manquante sur R1

```
Table de routage R1 initiale (défaillante) :
C    192.168.10.0/24 → connecté Gi0/0
C    10.1.2.0/30 → connecté Gi0/1
S    10.2.3.0/30 [1/0] via 10.1.2.2
← PAS de route vers 192.168.40.0/24 !

Correction :
R1(config)# ip route 192.168.40.0 255.255.255.0 10.1.2.2

NB : La route vers 10.2.3.0/30 n'est pas strictement nécessaire pour joindre 192.168.40.0/24
car R1 peut utiliser R2 comme next-hop intermédiaire sans connaître ce réseau.
```

## Correction Panne 2 — Masque incorrect sur R2

```
Route défaillante :
S    192.168.40.0/16 [1/0] via 10.2.3.2    ← masque /16 au lieu de /24

Correction :
R2(config)# no ip route 192.168.40.0 255.255.0.0 10.2.3.2
R2(config)# ip route 192.168.40.0 255.255.255.0 10.2.3.2

Impact d'un masque /16 : R2 croit connaître tout le réseau 192.168.0.0/16 mais
le calcul d'appartenance du paquet 192.168.40.10 se fait mal → comportement imprévisible
```

## Correction Panne 3 — Next-hop injoignable sur R3

```
Route défaillante :
S    192.168.10.0/24 [1/0] via 10.9.9.1    ← next-hop inexistant

Ping 10.9.9.1 depuis R3 → timeout (adresse inconnue sur ce réseau)

Correction :
R3(config)# no ip route 192.168.10.0 255.255.255.0 10.9.9.1
R3(config)# ip route 192.168.10.0 255.255.255.0 10.2.3.1    ← R2 Gi0/1

Vérification : show ip route → la route doit apparaître sans astérisque
```

## Table de routage complète attendue après corrections

```
R1 : C 192.168.10.0/24, C 10.1.2.0/30, S 192.168.40.0/24 via 10.1.2.2
R2 : C 10.1.2.0/30, C 10.2.3.0/30, S 192.168.10.0/24 via 10.1.2.1, S 192.168.40.0/24 via 10.2.3.2
R3 : C 10.2.3.0/30, C 192.168.40.0/24, S 192.168.10.0/24 via 10.2.3.1
```

## Éléments attendus dans le compte rendu

**Recommandations** : Mettre en place un protocole de routage dynamique (OSPF) pour éviter les erreurs de configuration manuelle et permettre la convergence automatique en cas de panne.

---

*TP Routage Statique + Correction — BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S2*
*Document Portfolio E31 — Compétences C2.2 · C2.3 · C3.1 · S2.3*
