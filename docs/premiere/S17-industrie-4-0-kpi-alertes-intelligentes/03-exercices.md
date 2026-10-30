# 🔬 EXERCICES PRATIQUES + PV MÉTROLOGIE — S17 · 2ᵉ ANNÉE · E2
## Industrie 4.0 : KPI · Alertes Multi-niveaux · Procès-Verbal de Métrologie

---

> **Nom** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ **Groupe** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Date** : \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
> **Durée** : 60 minutes · **Calculatrice obligatoire**

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **S5.5** | Requêtes InfluxDB statistiques (mean, min, max, stddev) |
| **C3.1** | Rédiger un PV de métrologie normalisé avec incertitudes |
| **C5.3** | Configurer des alertes multi-niveaux Node-RED |

---

## 🟢 EXERCICE 1 — Requêtes InfluxDB statistiques (15 min)

> Les données de la chaîne de production PROCIMEX sont dans InfluxDB.
> Écris les requêtes Flux pour chaque besoin.

**Q1.a** — Température **moyenne** des **30 dernières minutes** :

```javascript
from(bucket: "_____________")
  |> range(start: ________)
  |> filter(fn: (r) => r._measurement == "production_line")
  |> filter(fn: (r) => r._field == "_____________")
  |> mean()
```

**Q1.b** — Température **max** et **min** des **3 dernières heures** :

```javascript
// Requête max :
from(bucket: "procimex")
  |> range(start: ________)
  |> filter(fn: (r) => r._measurement == "production_line")
  |> filter(fn: (r) => r._field == "temperature")
  |> ______()

// Pour avoir max ET min dans un seul résultat :
from(bucket: "procimex")
  |> range(start: -3h)
  |> filter(fn: (r) => r._measurement == "production_line")
  |> filter(fn: (r) => r._field == "temperature")
  |> reduce(
       fn: (r, accumulator) => ({
         max: if r._value > accumulator.max then r._value else accumulator.max,
         min: if r._value < accumulator.min then r._value else accumulator.min
       }),
       identity: {max: -999.0, min: 999.0}
     )
```

**Q1.c** — **Moyenne par tranche de 10 minutes** sur la **dernière heure** (pour un graphe lissé) :

```javascript
from(bucket: "procimex")
  |> range(start: ________)
  |> filter(fn: (r) => r._measurement == "production_line")
  |> filter(fn: (r) => r._field == "temperature")
  |> aggregateWindow(every: ________, fn: ________, createEmpty: false)
```

**Q1.d** — Interprète ce résultat d'une requête `stddev()` sur la pression (résultat = 0,42 bar) :

```
La valeur 0,42 bar représente : ______________________________________________
Une valeur idéale serait : ☐ la plus grande possible ☐ la plus proche de 0
Pour une pression nominale de 4,8 bar, un σ = 0,42 bar signifie que 68% des mesures
se trouvent entre _______ et _______ bar (intervalle µ ± σ).
Est-ce acceptable pour une chaîne industrielle ? ☐ Oui ☐ Non · Raison : ___________
```

??? success "Réponses"
    **Q1.a** : bucket `procimex`, `range(start: -30m)`, champ `temperature`.  
    **Q1.b** : `range(start: -3h)` et la fonction `max()` (et `min()` pour le minimum).  
    **Q1.c** : `range(start: -1h)` et `aggregateWindow(every: 10m, fn: mean, createEmpty: false)`.  
    **Q1.d** : 0,42 bar est l'écart-type : la dispersion des mesures de pression autour de leur moyenne. Une valeur idéale serait la plus proche de 0. 68 % des mesures se trouvent entre 4,38 et 5,22 bar. Pour une chaîne industrielle, ce n'est pas acceptable : la dispersion représente près de 9 % de la pression nominale.

---

## 🟡 EXERCICE 2 — Logique d'alertes multi-niveaux (15 min)

> Complète le code du nœud function "Gestionnaire alertes température" avec 3 niveaux.

```javascript
// Entrée : msg.payload = valeur température (nombre)
// Sortie : 3 outputs (INFO, ATTENTION, CRITIQUE)

var temp = msg.payload;

// Seuils
var INFO_MAX   = 24, INFO_MIN   = 20;
var ATTN_MAX   = 26, ATTN_MIN   = 18;
var CRIT_MAX   = 30, CRIT_MIN   = 15;

var msgAlerte = {
    payload   : temp,
    timestamp : new Date().toISOString()
};

// CRITIQUE (priorité 1 — vérifier EN PREMIER)
if (temp > _______ || temp < _______) {
    msgAlerte.niveau  = "CRITIQUE";
    msgAlerte.couleur = "rouge";
    msgAlerte.texte   = "🔴 ARRÊT PRODUCTION : T° = " + temp + "°C";
    return [null, null, msgAlerte];
}

// ATTENTION (priorité 2)
if (temp > _______ || temp < _______) {
    msgAlerte.niveau  = "ATTENTION";
    msgAlerte.couleur = "orange";
    msgAlerte.texte   = "🟠 Surveillance requise : T° = " + temp + "°C";
    return [null, msgAlerte, null];
}

// INFO (priorité 3)
if (temp > _______ || temp < _______) {
    msgAlerte.niveau  = "INFO";
    msgAlerte.couleur = "jaune";
    msgAlerte.texte   = "🟡 Écart légèrement hors cible : T° = " + temp + "°C";
    return [_______, null, null];
}

// Normal — aucune alerte
return [null, null, null];
```

**Q2.a** — Pourquoi vérifie-t-on CRITIQUE avant ATTENTION avant INFO ?

```
___________________________________________________________________________
___________________________________________________________________________
```

**Q2.b** — Si `temp = 31°C`, quelles sorties du nœud function reçoivent un message ?

```
Output 1 (INFO)      : ☐ Reçoit un message ☐ null
Output 2 (ATTENTION) : ☐ Reçoit un message ☐ null
Output 3 (CRITIQUE)  : ☐ Reçoit un message ☐ null
```

??? success "Réponses"
    Seuils : CRITIQUE `temp > CRIT_MAX (30) || temp < CRIT_MIN (15)` ; ATTENTION `temp > ATTN_MAX (26) || temp < ATTN_MIN (18)` ; INFO `temp > INFO_MAX (24) || temp < INFO_MIN (20)` ; dans le test INFO : `return [msgAlerte, null, null];`  
    **Q2.a** : une température de 31 °C vérifie aussi les conditions ATTENTION et INFO. Le premier test vrai arrête la fonction (`return`) : on teste donc le niveau le plus grave en premier, pour ne pas le masquer par un niveau plus faible.  
    **Q2.b** : pour 31 °C, seule la sortie 3 (CRITIQUE) reçoit un message ; les sorties 1 et 2 reçoivent `null`.

---

## 🟠 EXERCICE 3 — Feux tricolores sur le dashboard (10 min)

> Un feu tricolore IoT sur le dashboard Node-RED s'implémente avec un nœud **text** (Dashboard)
> dont la couleur du fond change selon la valeur d'un message.

**Q3.a** — Complète le code du nœud function qui envoie la couleur correcte au feu tricolore :

```javascript
// Entrée : msg.payload.niveau = "INFO" | "ATTENTION" | "CRITIQUE" | "OK"
// Sortie : msg.payload = string HTML colorée pour le nœud text

var niveau = msg.payload.niveau || "OK";

var couleurs = {
    "OK"        : { bg: "#4CAF50", emoji: "🟢", label: "NORMAL" },
    "INFO"      : { _____________________________ },
    "ATTENTION" : { bg: "#FF9800", emoji: "🟠", label: "ATTENTION" },
    "CRITIQUE"  : { _____________________________ }
};

var c = couleurs[niveau] || couleurs["OK"];
msg.payload = "<div style='background:" + c.bg +
              ";color:white;padding:10px;text-align:center;font-size:20px'>" +
              c.emoji + " " + c.label + "</div>";
msg.style = { "background": c.bg };
return msg;
```

**Q3.b** — Quelle propriété du nœud **text** du dashboard permet d'injecter du HTML ?

```
Propriété à cocher/configurer : ______________________________________________
```

??? success "Réponses"
    **Q3.a** : `"INFO" : { bg: "#FFC107", emoji: "🟡", label: "INFO" }` et `"CRITIQUE" : { bg: "#F44336", emoji: "🔴", label: "CRITIQUE" }`.  
    **Q3.b** : l'option « Allow HTML » (autoriser le HTML) du nœud text.

---

## 🔴 EXERCICE 4 — PV de métrologie (20 min)

> **Contexte** : Tu dois valider le capteur de température DHT22 de la station CLIMASENS.
> Tu as effectué 10 mesures en comparaison avec un thermomètre de référence certifié.

### Tableau de mesures relevées

| N° | T° référence (°C) | T° DHT22 (°C) | Écart (°C) | Écart² |
|---|---|---|---|---|
| 1 | 22,0 | 22,3 | +0,3 | 0,09 |
| 2 | 22,0 | 21,8 | −0,2 | 0,04 |
| 3 | 22,0 | 22,5 | +0,5 | 0,25 |
| 4 | 22,0 | 22,1 | +0,1 | 0,01 |
| 5 | 22,0 | 22,4 | +0,4 | 0,16 |
| 6 | 22,0 | 21,9 | −0,1 | 0,01 |
| 7 | 22,0 | 22,6 | +0,6 | 0,36 |
| 8 | 22,0 | 22,2 | +0,2 | 0,04 |
| 9 | 22,0 | 22,0 | 0,0 | 0,00 |
| 10 | 22,0 | 22,3 | +0,3 | 0,09 |
| **Σ** | | | | |

**Q4.a** — Calcule la **somme des écarts** et la **somme des écarts²** :

```
Σ Écart = ___________________________________________________________________
Σ Écart² = __________________________________________________________________
```

**Q4.b** — Calcule l'**erreur systématique** (biais) = moyenne des écarts :

```
Biais = Σ Écart / n = _______ / 10 = _______ °C
Interprétation : le DHT22 surestime / sous-estime (entourer) la vraie valeur de _______ °C
```

**Q4.c** — Calcule l'**écart-type** des mesures :

Formule : σ = $\sqrt{ Σ(écart²}$ / (n−1) )  

$$\sigma  = \sqrt{ \underline{\hspace{2.5em}} / \underline{\hspace{2.5em}} } = \sqrt{ \underline{\hspace{2.5em}} } = \underline{\hspace{2.5em}} °C$$

**Q4.d** — Calcule l'**incertitude type** u et l'**incertitude élargie** U (k=2, confiance 95%) :

u = σ / $\sqrt{n}$ = \_\_\_\_\_\_\_ / $\sqrt{10}$ = \_\_\_\_\_\_\_ / \_\_\_\_\_\_\_ = \_\_\_\_\_\_\_ °C  

$$U = k \times u = 2 \times \underline{\hspace{2.5em}} = \underline{\hspace{2.5em}} °C$$

Résultat final : T_DHT22 = (22,3 ± \_\_\_\_\_\_\_ ) °C  [intervalle de confiance 95%]  

**Q4.e** — La spécification du DHT22 annonce une précision de ±0,5°C.
La tenue de cette spécification est-elle vérifiée ?

```
Biais mesuré : _______ °C · U élargie : _______ °C
Pire cas (biais + incertitude) : _______ + _______ = _______ °C

Comparaison avec spécification ±0,5°C :
  ☐ Conforme (pire cas < 0,5°C)
  ☐ Non conforme (pire cas > 0,5°C)
  
Conclusion : _________________________________________________________________
```

??? success "Réponses"
    **Q4.a** : Σ écart = 2,1 ; Σ écart² = 1,05.  
    **Q4.b** : biais = 2,1 / 10 = 0,21 °C : le DHT22 surestime la vraie valeur de 0,21 °C.  
    **Q4.c** (formule de l'énoncé) : $\sigma = \sqrt{\dfrac{1{,}05}{9}} = \sqrt{0{,}1167} \approx 0{,}34\,°\mathrm{C}$  
    **Q4.d** : $u = \dfrac{0{,}34}{\sqrt{10}} = \dfrac{0{,}34}{3{,}16} \approx 0{,}11\,°\mathrm{C}$ ; $U = 2 \times 0{,}11 = 0{,}22\,°\mathrm{C}$ ; $T_{DHT22} = (22{,}3 \pm 0{,}22)\,°\mathrm{C}$ [95 %].  
    **Q4.e** : biais 0,21 °C ; U = 0,22 °C ; pire cas 0,21 + 0,22 = 0,43 °C < 0,5 °C : conforme. Conclusion : la spécification ±0,5 °C est vérifiée, mais avec une marge faible (0,07 °C).

---
