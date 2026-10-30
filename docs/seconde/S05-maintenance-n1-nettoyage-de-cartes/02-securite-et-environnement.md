# 🦺 Sécurité, électricité et environnement : les bons réflexes

## 🤔 À ton avis ?

Tu travailles sur une carte alimentée en **5 V**. Faut-il quand même prendre des précautions ? Et que fais-tu d'une carte électronique qui ne fonctionne plus ?

??? question "Réponse"
    Oui : même sans danger électrique, il y a la **chaleur** (fer à souder), les **fumées**, l'**électricité statique** qui détruit les composants, et les **déchets** qui ne vont pas à la poubelle ordinaire.

## 1. Basse tension et habilitation électrique

| Type de tension | Limite de la basse tension (TBT) |
|---|---|
| Alternatif (AC) | jusqu'à **50 V** |
| Continu (DC) | jusqu'à **120 V** |

> [!TIP] 💡 En clair
> Nos montages (5 V, 12 V) sont en **très basse tension** : ils ne présentent pas de risque d'électrisation. Au-delà de **50 V alternatif ou 120 V continu**, on intervient seulement avec une **habilitation électrique** (par exemple **BR**, pour les interventions de dépannage en basse tension). Sans habilitation, on ne touche pas.

### Vérifie

1. Une alimentation de 12 V continu nécessite-t-elle une habilitation ?
2. Tu dois intervenir sur un appareil branché au secteur (230 V). Quelle est la première chose à demander ?

??? success "Réponses"

    1. **Non** : 12 V est très inférieur à la limite de 120 V continu.
    2. Si tu as l'habilitation et l'autorisation, **couper et consigner** l'alimentation. Sans habilitation, tu **ne fais pas** l'intervention : tu préviens ton responsable.

## 2. L'électricité statique (ESD)

Une étincelle invisible suffit à **détruire un circuit intégré** sans que tu le sentes. On se protège :

- **bracelet antistatique** relié à la terre ;
- **tapis antistatique** sur le poste ;
- composants **rangés dans leurs sachets** antistatiques (argentés ou noirs) ;
- on **touche les cartes par les bords**, jamais par les composants.

## 3. Équipements de protection et soudure

- **Lunettes** pour la découpe de pattes (les bouts de fil partent vite) ;
- fer à souder **toujours reposé sur son support** ;
- **aspiration des fumées** de flux ;
- étain **sans plomb** (conforme à la directive européenne RoHS).

## 4. Environnement : que faire d'une carte hors service ?

Une carte électronique est un **déchet d'équipement électrique et électronique (DEEE)** : elle contient des métaux précieux et des substances polluantes. Elle ne va **ni à la poubelle ordinaire ni dans la nature**, mais dans un **bac de collecte DEEE**.

- **RoHS** : directive qui limite les substances dangereuses (plomb, mercure…) dans les produits neufs.
- **Piles et batteries** (surtout LiPo) : collecte séparée, jamais écrasées ni percées (risque d'incendie).

### Vérifie

1. Que signifie DEEE ?
2. Peut-on jeter une batterie LiPo gonflée à la poubelle ?

??? success "Réponses"

    1. **Déchets d'équipements électriques et électroniques.**
    2. **Non** : bac de collecte spécifique ; une batterie gonflée est dangereuse (risque d'incendie), on la met à l'écart dans un récipient non inflammable.

> [!SUCCESS] 🧠 À retenir
> - Limite de la TBT : **50 V AC / 120 V DC** ; au-delà, **habilitation** obligatoire.
> - ESD : bracelet, tapis, sachets antistatiques.
> - Carte ou batterie hors service : filière **DEEE**, jamais à la poubelle ordinaire.
