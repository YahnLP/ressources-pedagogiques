# 🎤 GUIDE DE SOUTENANCE — PROJET A2 · S20 · 2ᵉ ANNÉE · E31
## Présenter · Démontrer · Défendre ses choix techniques

---

> **Équipe** : ___________________________ · ___________________________
> **Durée** : 8 minutes de présentation + 4 minutes de questions
> **Support** : Slides (4 max) OU démonstration live sur PT OU les deux

---

## 🎯 Objectif de la soutenance

> Ce n'est pas une récitation du dossier. C'est une **démonstration de maîtrise**.
> Tu dois montrer que tu comprends ce que tu as construit — pas seulement que tu l'as fait.
> La question *"Pourquoi ?"* sera posée à chaque fonctionnalité.

---

## 📋 Plan des 8 minutes

### Slide 1 — Architecture (2 min)

```
Montrer : Le schéma logique du projet A2 (OSPF areas, VLANs, EtherChannel, VPN, QoS)

Dire :
  "DIGITEC a 3 sites : Siège, Agence B, et Datacenter."
  "Nous avons choisi OSPF multi-aires car..."
  "Le lien WAN est doublement sécurisé via..."
  "La VoIP est prioritarisée via..."

→ Durée : 2 min chrono
```

### Slide 2 — Démonstration live (3 min)

> Choisir UNE fonctionnalité à démontrer en direct sur Packet Tracer.
> Recommandations par niveau :

```
Niveau de base :
  Démontrer OSPF : show ip ospf neighbor → FULL sur R_SIEGE
  + show ip route sur R_AGENCE_B → routes O IA vers tous les sites

Niveau intermédiaire :
  Démontrer la haute disponibilité WAN :
  1. Ping continu PC_B1 → PC_Siege (ping 192.168.10.10 -n 100)
  2. Shutdown Se0/0/0 sur R_SIEGE
  3. Montrer que le ping reprend via WAN secours (show ip route)

Niveau avancé :
  Démontrer la QoS LLQ :
  show policy-map interface Se0/0/0
  → Expliquer les compteurs de la classe VOIX
```

### Slide 3 — Scénario de panne (2 min)

```
Choisir un scénario du PRA et le jouer :
"Si le WAN principal tombe... voici ce qui se passe..."
Montrer la résilience (route flottante, EtherChannel failover...)
```

### Slide 4 — Rétrospective (1 min)

```
"Ce qui aurait été différent avec plus de temps..."
"La difficulté principale rencontrée était..."
"Ce que nous ferions différemment..."
```

---

## ❓ Questions types posées par l'enseignant

> Prépare une réponse courte et précise (30s max) pour chacune :

```
Q1 : "Pourquoi avez-vous choisi LACP en mode active/active et pas mode on ?"
→ Ma réponse : _______________________________________________________________

Q2 : "Quelle est la distance administrative de votre route flottante ? Pourquoi 5 ?"
→ Ma réponse : _______________________________________________________________

Q3 : "Si R_DC tombe, les utilisateurs du Siège peuvent-ils encore accéder à l'Agence B ?"
→ Ma réponse : _______________________________________________________________

Q4 : "Comment avez-vous vérifié que votre QoS fonctionne vraiment ?"
→ Ma réponse : _______________________________________________________________

Q5 : "Quelle est la différence entre votre sauvegarde 'copy run start' et 'copy run tftp:' ?"
→ Ma réponse : _______________________________________________________________

Q6 : "Si votre dossier devait être lu par un technicien externe qui ne connaît pas DIGITEC,
      que manque-t-il pour qu'il puisse tout comprendre seul ?"
→ Ma réponse : _______________________________________________________________
```

---

## 📊 Grille d'évaluation de la soutenance — Enseignant

> À remplir pendant chaque soutenance

| Équipe : _________________________________ | Note : _____ / 10 |
|---|---|

| Critère | 0 | 1 | 2 | Commentaire |
|---|---|---|---|---|
| **Clarté de la présentation** | Incompréhensible | Partiellement clair | Clair et structuré | |
| **Maîtrise de l'architecture** | Ne comprend pas le schéma | Comprend partiellement | Explique les choix | |
| **Démonstration live** | Rien ne fonctionne | Fonctionne partiellement | Démonstration probante | |
| **Réponses aux questions** | Hors sujet ou silence | Approximatif | Précis et justifié | |
| **Gestion du temps** | Hors délai (+3 min) | Légèrement hors délai | 8 min respectées | |
| **TOTAL** | | | **/10** | |

**Points forts de l'équipe :**
```
___________________________________________________________________________
```

**Points à améliorer :**
```
___________________________________________________________________________
```

---

## 💬 Retour collectif post-soutenances (pour l'enseignant)

> À écrire au tableau pendant le bilan collectif :

```
ERREURS LES PLUS FRÉQUENTES DANS LES PROJETS A2 :
  1. ________________________________________________________________________
  2. ________________________________________________________________________
  3. ________________________________________________________________________

POINTS FORTS COLLECTIFS :
  → ________________________________________________________________________
  → ________________________________________________________________________

SÉANCES À RÉVISER EN PRIORITÉ (selon les soutenances) :
  → ________________________________________________________________________
```

---

*Guide de soutenance + Grille d'évaluation orale*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S20*
