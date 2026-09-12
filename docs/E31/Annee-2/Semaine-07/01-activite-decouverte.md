# 🎲 ACTIVITÉ DÉCOUVERTE – S7 ANNÉE 2 – E31
## « La Valise Diplomatique » : Pourquoi Chiffrer les Communications Réseau

---

## 🎯 OBJECTIFS

- ✅ Faire émerger le **besoin de confidentialité** des communications inter-sites via Internet
- ✅ Comprendre que chiffrer ne suffit pas : il faut aussi **authentifier** et garantir l'**intégrité**
- ✅ Introduire les trois propriétés de sécurité d'IPsec : confidentialité, intégrité, authenticité
- ✅ Poser le problème de la gestion des clés (comment R-PARIS et R-LYON se mettent d'accord sans qu'un attaquant les intercepte ?)

---

## ⏱️ DURÉE : 30 min

---

## ⚙️ MISE EN PLACE (2 min)

**Le formateur pose l'accroche :**

> *"En S6, on a mis en place le NAT — les machines internes communiquent avec Internet. Mais qu'est-ce qui protège les données qui transitent ? Si je transfère le dossier de paie de Paris à Lyon via Internet… qui peut le lire en chemin ?"*

---

## 🔬 PHASE 1 – L'Interception (8 min)

**Le formateur dessine la situation au tableau :**

```
[PARIS: 192.168.1.0/24]            [LYON: 192.168.2.0/24]
        │                                   │
    [R-PARIS]── Internet (public) ──[R-LYON]
                       │
                [🕵️ Attaquant]
              "Je vois tout !"
```

**Questions au groupe :**

| **Q** | **Réponse attendue** |
|---|---|
| "Que peut faire un attaquant qui intercepte les paquets ?" | Lire le contenu (sniffing), modifier les données (MITM), rejouer d'anciens paquets (replay) |
| "Si je chiffre les données, que voit l'attaquant ?" | Une suite de caractères illisibles — mais il sait toujours que Paris parle à Lyon |
| "Si l'attaquant modifie des bits dans le flux chiffré, comment le détecter ?" | Besoin d'un code d'intégrité (HMAC) — sans ça, la modification peut passer inaperçue |
| "Comment Paris et Lyon se mettent-ils d'accord sur la clé de chiffrement sans que l'attaquant la capte ?" | C'est le problème de l'échange de clés — c'est ce que DH (Diffie-Hellman) résout ! |

---

## 📦 PHASE 2 – L'Analogie de la Valise Diplomatique (10 min)

> *"La valise diplomatique est un mécanisme utilisé par les ambassades. Elle voyage librement entre pays, personne ne peut l'ouvrir, et son contenu est légalement protégé. IPsec fait la même chose pour vos paquets réseau."*

**Tableau d'analogie :**

| **Valise Diplomatique** | **VPN IPsec** |
|---|---|
| Valise fermée à clé | Paquet chiffré (AES) |
| Scellée avec un cachet officiel | Code d'intégrité (HMAC-SHA) |
| Identité du porteur vérifiée | Authentification du routeur (PSK ou certificat) |
| Envoyée dans un conteneur opaque | Mode tunnel : IP interne cachée dans IP externe |
| Durée de validité du visa | Durée de vie de la SA (lifetime) |
| Valises séparées Paris→Lyon et Lyon→Paris | SA unidirectionnelles (une pour chaque sens) |

**Questions :**

**Q1.** Pourquoi la valise voyage-t-elle dans un "conteneur externe" (le camion de l'ambassade) ? À quoi cela correspond-il en IPsec ?

_________________________________________________________________________
_________________________________________________________________________

**Q2.** Si l'attaquant capture la valise et la rouvre 30 minutes après (attaque de rejeu), qu'est-ce qui empêche ça en IPsec ?

_________________________________________________________________________

**Q3.** Pourquoi a-t-on besoin de deux valises séparées (une Paris→Lyon, une Lyon→Paris) ? Pourquoi pas une seule valise qui va dans les deux sens ?

_________________________________________________________________________
_________________________________________________________________________

---

## 🤔 PHASE 3 – Le Problème de la Négociation (8 min)

> *"Avant d'envoyer la valise, Paris et Lyon doivent s'entendre sur la serrure à utiliser, le cachet, et le mot de passe. Mais comment faire ça de façon sécurisée si l'attaquant écoute tout ?"*

**Le formateur présente le problème de l'échange de clés :**

```
Paris                           Lyon
  │                               │
  │── "Utilisons AES-256 ?" ──►   │   → Attaquant écoute tout
  │◄── "OK, SHA-256 aussi." ───   │
  │                               │
  │    [Comment partager la       │
  │     clé secrète sans          │
  │     que l'attaquant           │
  │     la connaisse ?]           │
```

**Brainstorming :**

> *"Proposez une façon d'établir un secret commun entre Paris et Lyon même si l'attaquant voit tous les échanges intermédiaires."*

| **Idée** | **Fonctionne ?** |
|---|---|
| Se téléphoner pour s'accorder sur la clé | Possible mais pas scalable (hors bande) |
| Envoyer la clé par e-mail chiffré | ♾️ Problème circulaire (comment chiffrer si on n'a pas encore de clé ?) |
| Utiliser les mathématiques pour créer un secret partagé sans jamais l'envoyer | ✅ C'est **Diffie-Hellman** ! |

**Le formateur révèle :**

> *"Diffie-Hellman permet à Paris et Lyon de créer un secret commun en échangeant uniquement des valeurs publiques — même si l'attaquant voit tout l'échange, il ne peut pas en déduire le secret. C'est la magie des mathématiques (nombres premiers, puissances modulaires). IKEv2 utilise DH pour exactement ça."*

---

## ✍️ PHASE 4 – Synthèse (2 min)

**À noter :**

```
┌────────────────────────────────────────────────────────────────────┐
│  IPsec = suite de protocoles pour sécuriser les communications IP  │
│                                                                    │
│  Les 3 propriétés garanties :                                      │
│  1. CONFIDENTIALITÉ : chiffrement AES                              │
│  2. INTÉGRITÉ       : code HMAC-SHA (détecte les modifications)    │
│  3. AUTHENTICITÉ    : clé pré-partagée (PSK) ou certificat         │
│                                                                    │
│  IKEv2 = protocole de négociation                                  │
│  Phase 1 → établit un canal sécurisé pour négocier                 │
│  Phase 2 → négocie les paramètres du vrai tunnel de données        │
│                                                                    │
│  SA = Security Association = contrat de sécurité UNIDIRECTIONNEL  │
│  → Une SA Paris→Lyon + une SA Lyon→Paris                           │
└────────────────────────────────────────────────────────────────────┘
```

---

## ✅ VALIDATION DE L'ACTIVITÉ

**L'activité est réussie si :**

- ✅ Les apprentis identifient les 3 propriétés de sécurité (confidentialité, intégrité, authenticité)
- ✅ Ils comprennent pourquoi il faut 2 SA (une par sens)
- ✅ Ils formulent le problème de l'échange de clés sans canal sécurisé préalable
- ✅ Ils ont entendu les mots IKEv2, DH, Phase 1/2, PSK

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
