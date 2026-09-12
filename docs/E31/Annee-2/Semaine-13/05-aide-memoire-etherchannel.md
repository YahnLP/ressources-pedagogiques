# 🗂️ AIDE-MÉMOIRE ETHERCHANNEL LACP — À PLASTIFIER
## Agrégation de liens · Load balancing · Redondance · Dépannage · BAC PRO CIEL · E31 · S13

---

> *Conserver sur le poste de travail pendant toute la séance et les évaluations*

---

## ⚡ Pourquoi EtherChannel ?

```
Sans EC : STP bloque les liens redondants → 1 lien actif
Avec EC : tous les liens actifs simultanément → 4 Gbps + redondance

3 bénéfices :
  1. Bande passante × N (N = nombre de liens membres)
  2. Redondance sans reconvergence STP (failover < 1s)
  3. STP voit le port-channel comme 1 seul port
```

---

## 🔄 Modes LACP et compatibilité

```
active  + active   → ✓ EC formé  (RECOMMANDÉ)
active  + passive  → ✓ EC formé
passive + passive  → ✗ Personne n'initie
on      + on       → ✓ Static (sans négociation)
active  + on       → ✗ INCOMPATIBLE
```

---

## ⚙️ Configuration — 3 étapes

```cisco
! 1. Membres → assigner au groupe
interface range GigabitEthernet0/1-4
  channel-group 1 mode active

! 2. Port-channel → configurer trunk/VLAN
interface port-channel 1
  switchport mode trunk
  switchport trunk allowed vlan all

! 3. Load balancing (global)
port-channel load-balance src-dst-ip
```

> ⚠️ Config VLAN/trunk → sur Po1, pas sur Gi0/x individuel

---

## 📊 Load balancing

```
src-dst-ip ← recommandé (environnement mixte L3)
src-mac    ← réseau L2 avec beaucoup de clients
dst-mac    ← beaucoup de serveurs distincts

Vérifier : show etherchannel load-balance
```

---

## 🔍 Décoder show etherchannel summary

```
Group  Port-channel  Protocol    Ports
1      Po1(SU)       LACP        Gi0/1(P)  Gi0/2(P)  Gi0/3(D)  Gi0/4(I)
         │ ││                      │          │         │          │
         │ └─ U=actif              P=OK ✓     P=OK ✓   D=Down ✗   I=Stand-alone ✗
         └─ S=Layer2

Codes :
  (P) Bundled ✓  → membre actif
  (I) Stand-alone → incompatibilité (vitesse/VLAN/mode)
  (D) Down        → câble déconnecté ou shutdown
  (s) Suspended   → config VLAN différente entre membres
  (U) Port-channel actif ✓
  (S) Layer 2
```

---

## 🔴 4 Pannes fréquentes → Corrections

| Panne | Symptôme | Fix |
|---|---|---|
| Modes incompatibles | Po1(SD) | `channel-group 1 mode active` des 2 côtés |
| Vitesse différente | Gi0/x(I) | `speed auto` sur le port forcé |
| Trunk absent sur Po1 | VLAN ne passe pas | `switchport mode trunk` sur Po1 |
| Config VLAN sur membre physique | Gi0/x(s) | Supprimer config sur Gi0/x, la mettre sur Po1 |

---

## ✅ Commandes essentielles

```cisco
show etherchannel summary          ← vue d'ensemble
show etherchannel 1 detail         ← détail groupe 1
show interfaces port-channel 1     ← état du Po1
show interfaces port-channel 1 trunk ← config trunk
show lacp 1 internal               ← info LACP local
show lacp 1 neighbor               ← info LACP voisin
show etherchannel load-balance     ← méthode LB active
```

---

## 🔑 Les 3 conditions pour qu'un port rejoigne le bundle

```
1. Même vitesse (ex: tous à 1 Gbps)
2. Même duplex (full-duplex)
3. Même config VLAN/trunk (tout trunk ou même access VLAN)
```

---

## ⚠️ Erreurs fréquentes

| ❌ Erreur | ✅ Correction |
|---|---|
| active d'un côté + on de l'autre | active + active des deux côtés |
| Config trunk sur Gi0/1 (membre) | Mettre sur Po1 uniquement |
| Oublier le trunk sur Po1 | `switchport mode trunk` sur Po1 |
| Interfaces à vitesses différentes | `speed auto` sur tous les membres |

---

*Aide-Mémoire EtherChannel — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 2ᵉ année S13*
*Compétences S2.1 · S2.2 · S2.3 · C2.2 · C2.3*
