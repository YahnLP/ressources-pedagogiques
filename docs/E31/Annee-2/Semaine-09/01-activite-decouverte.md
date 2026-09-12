# 🔍 ACTIVITÉ DE DÉCOUVERTE — S9 · 2ᵉ ANNÉE · E32
## « Qui êtes-vous vraiment ? » — Décoder un échange 802.1X sans cours préalable

---

> **Durée** : 35 minutes
> **Format** : Binômes
> **Matériel** : Cette fiche · Stylo
> **Principe** : On te présente une capture d'un échange d'authentification WiFi réel. Tu dois identifier les acteurs, leur rôle et le résultat — avant tout cours.

---

## 🎯 Mise en situation

> Tu es **technicien cybersécurité** dans une entreprise.
> Un nouvel employé arrive et tente de se connecter au WiFi de l'entreprise.
>
> Ton collègue a capturé les échanges réseau. Voici ce qu'il a vu, dans l'ordre chronologique.
> **Ta mission** : comprendre ce qui se passe, sans manuel.

---

## 📡 La capture réseau simplifiée

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Heure    De              Vers            Message                       │
├─────────────────────────────────────────────────────────────────────────┤
│  09:00:01 Laptop-Alice    Borne WiFi      "Je veux me connecter"        │
│  09:00:02 Borne WiFi      Laptop-Alice    "Prouve qui tu es"            │
│  09:00:03 Laptop-Alice    Borne WiFi      "Je m'appelle alice@corp.fr"  │
│  09:00:03 Borne WiFi      Serveur Auth    "Alice veut se connecter"     │
│  09:00:04 Serveur Auth    Borne WiFi      "Demande-lui son certificat"  │
│  09:00:04 Borne WiFi      Laptop-Alice    "Montre ton certificat"       │
│  09:00:05 Laptop-Alice    Borne WiFi      [Certificat numérique d'Alice]│
│  09:00:05 Borne WiFi      Serveur Auth    [Transmet le certificat]      │
│  09:00:06 Serveur Auth    Borne WiFi      "Certificat VALIDE ✓"         │
│  09:00:07 Serveur Auth    Borne WiFi      "Alice est autorisée — VLAN10"│
│  09:00:07 Borne WiFi      Laptop-Alice    "Connexion autorisée ✓"       │
│  09:00:08 Laptop-Alice    Réseau Corp     [Trafic normal VLAN 10]       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 PARTIE 1 — Identifier les acteurs (8 min)

**Question 1.1** — Combien y a-t-il d'entités distinctes qui participent à cet échange ?

```
Entité 1 : ___________________________________________________________________
Entité 2 : ___________________________________________________________________
Entité 3 : ___________________________________________________________________
```

**Question 1.2** — Quel est le rôle de chacune ? Associe chaque entité à sa description :

| Entité | Rôle probable |
|---|---|
| Laptop-Alice | ☐ Demande l'accès au réseau ☐ Vérifie l'identité ☐ Filtre le trafic |
| Borne WiFi | ☐ Demande l'accès au réseau ☐ Intermédiaire / garde-barrière ☐ Accorde l'accès |
| Serveur Auth | ☐ Décide d'autoriser ou refuser ☐ Transmet des paquets ☐ Chiffre le trafic |

**Question 1.3** — La borne WiFi prend-elle elle-même la décision d'autoriser Alice ?

```
☐ Oui — la borne décide seule
☐ Non — la borne transmet à _____________ qui prend la décision
Preuve dans la capture : ligne _______ ("_______________________________________")
```

---

## 🔍 PARTIE 2 — Le rôle du certificat (10 min)

**Question 2.1** — À la ligne 09:00:05, Alice envoie un "certificat numérique". D'après le contexte, à quoi sert ce certificat ?

```
Un certificat numérique sert à prouver : _______________________________________
C'est l'équivalent numérique d'une : ☐ clé USB ☐ carte d'identité ☐ adresse IP
```

**Question 2.2** — Le serveur d'authentification vérifie ce certificat. Pour être valide, que doit vérifier ce serveur d'après toi ?

```
Vérification 1 : _______________________________________________________________
Vérification 2 : _______________________________________________________________
Vérification 3 : _______________________________________________________________
```

**Question 2.3** — Compare cette méthode avec un WiFi classique à mot de passe partagé (PSK). Quelle est la différence fondamentale si Alice quitte l'entreprise ?

```
WiFi PSK : pour bloquer Alice après son départ, il faut ________________________
            Impact sur les autres employés : ___________________________________

WiFi 802.1X : pour bloquer Alice, il suffit de _________________________________
              Impact sur les autres employés : _________________________________
```

**Question 2.4** — À la ligne 09:00:07 le serveur répond "Alice est autorisée — VLAN10". Il assigne Alice à un VLAN spécifique. D'après toi, pourquoi ne pas mettre tout le monde dans le même VLAN ?

```
Avantage de mettre Alice dans VLAN10 plutôt que VLAN0 (tout le monde) :
___________________________________________________________________________
___________________________________________________________________________
```

---

## ❌ PARTIE 3 — Scénario de refus (10 min)

> Le lendemain, Bob tente de se connecter. Voici sa capture :

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Heure    De              Vers            Message                       │
├─────────────────────────────────────────────────────────────────────────┤
│  10:15:01 Laptop-Bob      Borne WiFi      "Je veux me connecter"        │
│  10:15:02 Borne WiFi      Laptop-Bob      "Prouve qui tu es"            │
│  10:15:03 Laptop-Bob      Borne WiFi      "Je m'appelle bob@corp.fr"    │
│  10:15:03 Borne WiFi      Serveur Auth    "Bob veut se connecter"       │
│  10:15:04 Serveur Auth    Borne WiFi      "Demande-lui son certificat"  │
│  10:15:04 Borne WiFi      Laptop-Bob      "Montre ton certificat"       │
│  10:15:05 Laptop-Bob      Borne WiFi      [Certificat numérique de Bob] │
│  10:15:05 Borne WiFi      Serveur Auth    [Transmet le certificat]      │
│  10:15:06 Serveur Auth    Borne WiFi      "Certificat EXPIRÉ ✗"         │
│  10:15:06 Borne WiFi      Laptop-Bob      "Connexion REFUSÉE ✗"         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Question 3.1** — Pourquoi la connexion de Bob est-elle refusée ?

```
Raison : _____________________________________________________________________
```

**Question 3.2** — Compare la capture de Bob avec celle d'Alice. Le refus est-il décidé par la borne WiFi ou par le serveur d'authentification ?

```
Décision prise par : _______________________  à la ligne : _______
```

**Question 3.3** — Que doit faire le technicien réseau pour que Bob puisse se reconnecter ?

```
Action 1 (immédiate) : _________________________________________________________
Action 2 (pour l'avenir) : _____________________________________________________
```

**Question 3.4** — Troisième scénario : Eve (une attaquante extérieure) tente de se connecter. Elle ne possède pas de certificat valide. Dérouler le scénario :

```
Eve envoie sa demande de connexion
→ La borne demande : ___________________________________________________________
→ Eve répond avec : ____________________________________________________________
→ Le serveur vérifie et répond : _______________________________________________
→ Résultat : ☐ Eve se connecte ☐ Eve est refusée
→ Eve peut-elle deviner le certificat d'Alice ? ☐ Oui ☐ Non — car _______________
```

---

## 🏁 PARTIE 4 — Bilan (7 min)

**Complète avec tes propres mots :**

```
Dans un WiFi 802.1X, il y a 3 acteurs :
  1. Le _______________ (supplicant) : appareil qui demande l'accès
  2. L'_______________ (authenticator) : borne WiFi, filtre le trafic
  3. Le _______________ (authentication server) : décide d'autoriser ou refuser

Le protocole utilisé entre la borne et le serveur s'appelle : ___________________

Le moyen de prouver son identité utilisé ici est : un _________________________

Avantage principal par rapport au WiFi PSK : __________________________________
______________________________________________________________________________
```

> ✅ Tu viens de comprendre l'essence de 802.1X — le cours va maintenant te donner
> les noms techniques précis, les protocoles sous-jacents et les commandes de configuration.

---

## 📎 Pour l'enseignant — Réponses

**1.1** : Laptop-Alice (supplicant) · Borne WiFi (authenticator) · Serveur Auth (RADIUS)
**1.3** : Non — la borne transmet au Serveur Auth qui décide (ligne 09:00:06-07)
**2.3** : PSK → changer le mot de passe pour tous / 802.1X → révoquer le certificat ou désactiver le compte Alice uniquement
**3.2** : Décision prise par le Serveur Auth à la ligne 10:15:06
**3.3** : Renouveler le certificat de Bob (via la PKI) + vérifier la date d'expiration
**3.4** : Eve est refusée — le certificat est cryptographiquement signé par une CA, impossible à deviner ou forger sans la clé privée

---

*Activité de Découverte — Fiche apprenant*
*BAC PRO CIEL | E32 Cybersécurité | 2ᵉ année S9*
*Compétences : S4.1 · S4.2 · S4.3*
