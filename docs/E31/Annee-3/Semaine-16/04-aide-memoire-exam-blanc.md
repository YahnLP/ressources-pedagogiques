# 🗂️ AIDE-MÉMOIRE EXAMEN BLANC E31 — À PLASTIFIER
## Simulation CCF · Checklist · Oral · BAC PRO CIEL · E31 · 3ᵉ année S16

---

> *Lire pendant la préparation de l'oral (15 min)*

---

## ⏱️ Gestion des 3h pratique

```
0h00-0h15  → Lire le sujet COMPLET + brouillon
0h15-0h35  → Plan d'adressage (wildcards !)
0h35-2h20  → Config PT : L2 → L3 → OSPF → Services
2h20-2h50  → Documentation + schéma
2h50-3h00  → Checklist finale + copy run start
```

---

## ✅ Checklist AVANT de rendre

```
☐ copy run start sur CHAQUE équipement
☐ show ip ospf neighbor → FULL
☐ Ping E2E : PC le + éloigné → PC le + éloigné
☐ show etherchannel summary → Po(SU), (P)
☐ Schéma avec VLANs, areas OSPF, adresses IP
☐ Tableau de tests rempli avec vrais résultats
☐ Justifications rédigées (pas laissées vides)
```

---

## 🎤 Structure oral (5 min)

```
30s → Introduction (contexte client + besoin)
2min → Architecture (schéma + choix technos justifiés)
2min → Démonstration live (show ospf + ping + show EC)
30s → Réflexion critique (ce qu'on améliorerait)
```

## 3 démos incontournables

```
R_LYON# show ip ospf neighbor → FULL ✓
PC_DIR> ping [IP PC_Marseille] → Succès ✓
SW# show etherchannel summary → Po1(SU) ✓
```

---

## ❓ Réponses types (3 questions clés)

```
"Pourquoi OSPF multi-aires ?"
→ Limite la propagation LSA · Area 0 backbone · scalabilité

"Pourquoi passive-interface ?"
→ Pas de Hello vers les PCs · sécurité · économie CPU

"Que se passe-t-il si le WAN tombe ?"
→ OSPF détecte en 40s · routes O IA disparaissent de R_MRS
→ Amélioration : lien de secours + route flottante
```

---

## 🔑 Wildcards express

```
/25=0.0.0.127   /26=0.0.0.63    /27=0.0.0.31
/28=0.0.0.15    /30=0.0.0.3     /32=0.0.0.0
```

## 🚨 5 pièges fatals E31

```
1. Masque dans OSPF → wildcard !
2. no shutdown interface parent avant sous-interfaces
3. Trunk sur Port-channel (pas sur Gi membres)
4. ACL sans permit any → tout bloqué
5. copy run start oublié → config disparaît
```

---

## 💬 Phrases à connaître

```
Choix : "J'ai utilisé [X] car [raison précise]."
Lacune : "Je n'ai pas eu le temps de [X], j'aurais fait [Y]."
Difficulté : "Le principe est [X], même si je ne suis pas sûr des détails."
```

---

*Aide-Mémoire Examen Blanc E31 — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S16*
