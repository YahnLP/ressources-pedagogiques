# 🎓 FICHE DE PRÉPARATION CANDIDAT — SOUTENANCE U31 A2
## Ce que vous devez savoir faire et dire le jour J

**Nom : ________________  Prénom : ________________**

---

> *Cette fiche est votre guide de révision final. Pour chaque technologie, préparez une démonstration ET une justification orale. Cochez chaque case quand vous êtes prêt(e).*

---

## VOTRE PLAN DE SOUTENANCE (20 min)

### ⏱️ Phase 1 — Présentation topologie (5 min)

**Script recommandé :**

> *"Mon infrastructure CIEL-Corp comporte deux sites : Paris et Lyon. Côté Paris, j'ai [décrire]. Le routage inter-sites est assuré par [OSPF]. La redondance de passerelle est gérée par [HSRP]. La sécurité des communications inter-sites est assurée par [VPN IPsec]. Voici mon plan d'adressage..."*

**Ce que vous devez pouvoir montrer sur papier :**

| **Élément** | **Valeur dans votre infra** | **Prêt ?** |
|---|---|---|
| LAN Paris | ____________ / ____ | ☐ |
| IP virtuelle HSRP Paris | ____________ | ☐ |
| Priorité R-PARIS-A / R-PARIS-B | _____ / _____ | ☐ |
| Liaison WAN Paris-Lyon | ____________ / ____ | ☐ |
| LAN Lyon | ____________ / ____ | ☐ |
| PSK VPN | ____________ (à ne pas afficher publiquement) | ☐ |

---

### ⏱️ Phase 2 — Démonstration (10 min)

**Préparez vos commandes dans cet ordre :**

```
Étape 1 — Connectivité de base (1 min)
  PC-PARIS# ping [IP_LAN_PARIS_GW]        → must be ✅
  PC-PARIS# ping [IP_LAN_LYON_PC]         → must be ✅

Étape 2 — OSPF (2 min)
  R-PARIS-A# show ip ospf neighbor        → FULL attendu
  R-PARIS-A# show ip route ospf           → routes Lyon visibles

Étape 3 — HSRP état initial (2 min)
  R-PARIS-A# show standby brief           → Active + Virtual IP
  R-PARIS-B# show standby brief           → Standby
  (annoncer la bascule avant de la faire)

Étape 4 — Bascule HSRP (2 min)
  R-PARIS-A(config-if)# shutdown          → simuler panne
  R-PARIS-B# show standby brief           → maintenant Active
  PC-PARIS# ping [IP_Internet]            → fonctionne encore ?
  R-PARIS-A(config-if)# no shutdown       → retour
  R-PARIS-A# show standby brief           → reprend Active (preempt)

Étape 5 — VPN IPsec (2 min)
  R-PARIS-A# show crypto isakmp sa        → QM_IDLE
  R-PARIS-A# show crypto ipsec sa         → pkts encrypt > 0
  (si 0 → faire un ping LAN-LAN pour déclencher le trafic intéressant)

Étape 6 — ACL (1 min)
  R-PARIS-A# show ip access-lists         → matches visibles
```

---

### ⏱️ Phase 3 — Défense des choix (5 min)

**Préparez ces 6 réponses :**

**1. Pourquoi OSPF et pas du routage statique ?**

Votre réponse :
_________________________________________________________________________
_________________________________________________________________________

**Réponse attendue :** OSPF converge automatiquement en cas de panne de lien WAN. Avec du routage statique, si le lien tombe, les routes ne sont pas mises à jour automatiquement — il faudrait intervenir manuellement. OSPF gère la convergence en quelques secondes.

---

**2. Pourquoi ces priorités HSRP (ex: 120/100) ?**

Votre réponse :
_________________________________________________________________________
_________________________________________________________________________

**Réponse attendue :** J'ai choisi une valeur supérieure au défaut (100) pour R-PARIS-A afin qu'il soit clairement désigné comme routeur préférentiel. L'écart de 20 points entre les deux routeurs garantit une élection sans ambiguïté.

---

**3. Comment avez-vous calculé le décrement de tracking ?**

Votre réponse :
_________________________________________________________________________

**Réponse attendue :** Décrement doit satisfaire : prio_A - décrement < prio_B. Donc décrement > prio_A - prio_B = 120 - 100 = 20. J'ai choisi 30 pour avoir une marge.

---

**4. Pourquoi l'ACL est-elle placée sur cette interface et dans cette direction ?**

Votre réponse :
_________________________________________________________________________
_________________________________________________________________________

**Réponse attendue :** ACL étendue → proche de la source → interface LAN, direction `in`. Cela filtre le trafic dès son entrée dans le routeur, évitant qu'il traverse inutilement le réseau.

---

**5. Pourquoi l'ACL crypto de Lyon est-elle différente de celle de Paris ?**

Votre réponse :
_________________________________________________________________________
_________________________________________________________________________

**Réponse attendue :** L'ACL crypto définit le trafic à chiffrer. Sur Paris, le trafic intéressant va de Paris (source) vers Lyon (destination). Sur Lyon, c'est l'inverse. Si les deux ACL étaient identiques, Lyon ne reconnaîtrait pas le trafic venant de Paris comme étant à déchiffrer.

---

**6. Que se passe-t-il si le `permit ip any any` final de l'ACL est absent ?**

Votre réponse :
_________________________________________________________________________
_________________________________________________________________________

**Réponse attendue :** Toute règle Cisco se termine par un `deny any any` implicite. Sans `permit ip any any` explicite à la fin, tout le trafic non couvert par les règles précédentes serait bloqué — isolant complètement le LAN.

---

### ⏱️ Phase 4 — Troubleshooting Live (10 min)

**Votre méthode en cas de panne inconnue :**

```
STEP 1 — Tester la connectivité (ne pas regarder la config d'abord !)
  ping vers LAN local → si OK : problème au-delà du routeur
  ping vers WAN → si KO : problème réseau ou routage
  ping vers VPN → si KO : VPN ou routage inter-sites

STEP 2 — Identifier la couche du problème
  show ip ospf neighbor  → OSPF ok ?
  show standby brief     → HSRP ok ?
  show crypto isakmp sa  → VPN Phase 1 ok ?
  show ip access-lists   → ACL bloque quelque chose ?

STEP 3 — Cibler le composant fautif
  show run | section [protocole_suspect]
  Comparer avec ce que vous attendez

STEP 4 — Corriger et vérifier
  Saisir la commande de correction
  Retester la connectivité pour confirmer
```

**Dites à voix haute tout ce que vous pensez.** Le jury évalue votre méthode, pas seulement votre résultat.

---

## CHECKLIST FINALE — LA VEILLE

### Vérification de la topologie Packet Tracer

- [ ] Tous les pings LAN-LAN fonctionnent
- [ ] `show ip ospf neighbor` = FULL sur tous les routeurs
- [ ] `show standby brief` = Active + Standby avec la bonne IP virtuelle
- [ ] `show crypto isakmp sa` = QM_IDLE (après un ping inter-sites pour déclencher le VPN)
- [ ] `show crypto ipsec sa` = pkts encrypt > 0
- [ ] `show ip access-lists` = règles visibles avec matches > 0
- [ ] Bascule HSRP testée et fonctionnelle (en moins de 5 secondes)
- [ ] Retour preempt testé et fonctionnel
- [ ] Nagios : au moins 1 plugin testé depuis le CLI

### Documents à préparer

- [ ] Schéma réseau imprimé (A4 ou A3)
- [ ] Tableau plan d'adressage imprimé
- [ ] Fichier .pkt sauvegardé sur clé USB + copie de sauvegarde
- [ ] Fiche de défense (vos réponses aux 6 questions ci-dessus)

---

## 🗓️ PROGRAMME TYPE DU JOUR J

| **Heure** | **Action** |
|---|---|
| -15 min | Arriver, copier le fichier .pkt sur le PC jury, vérifier l'ouverture |
| 0h00 | Début de la soutenance |
| 0h05 | Phase 1 : Présentation topologie (avec schéma papier) |
| 0h15 | Phase 2 : Démonstration Packet Tracer |
| 0h25 | Phase 3 : Défense des choix (questions jury) |
| 0h30 | Phase 4 : Troubleshooting live |
| 0h40 | Phase 5 : Questions complémentaires jury |
| 0h45 | Fin — sortie de la salle, délibération jury |

---

## 💬 LEXIQUE D'URGENCE

> Si vous avez un trou de mémoire pendant la soutenance :

| **Symptôme** | **Commande réflexe** |
|---|---|
| "Ça ne ping pas" | `show ip route` + `show ip ospf neighbor` |
| "Le VPN est mort" | `show crypto isakmp sa` puis `show crypto ipsec sa` |
| "HSRP ne bascule pas" | `show standby` (chercher priorité et preempt) |
| "L'ACL bloque trop" | `show ip access-lists` (compteur deny élevé ?) |
| "OSPF ne voit pas le voisin" | `show ip ospf interface` (area ? network ?) |

---

**Document – BAC PRO CIEL – A2 – E31/U31 – Version 1.0 – 2026**
