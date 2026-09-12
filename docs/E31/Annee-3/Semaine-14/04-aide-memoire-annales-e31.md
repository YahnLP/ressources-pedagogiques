# 🗂️ AIDE-MÉMOIRE ANNALES E31 — À PLASTIFIER
## Les Pièges · La Checklist · Les Points Gratuits · S14 · 3ᵉ année

---

> *La fiche à relire la veille de l'épreuve E31*

---

## ⏱️ Gestion des 4 heures

```
0h00-0h15  → Lire le sujet COMPLET + schéma brouillon
0h15-0h35  → Plan d'adressage (wildcards !)
0h35-2h50  → Configuration PT (L2 → L3 → Routage → Services)
2h50-3h15  → Documentation + schéma annoté
3h15-3h50  → Tests + vérifications
3h50-4h00  → copy run start × TOUS les équipements
```

---

## 📋 Checklist avant de rendre

```
☐ copy run start sur CHAQUE équipement
☐ show ip ospf neighbor → FULL sur tous les routeurs
☐ Ping E2E : PC le plus éloigné → PC le plus éloigné
☐ show etherchannel summary → Po(SU), ports en (P)
☐ Schéma avec toutes les adresses IP, VLANs, areas OSPF
☐ Tableau de tests rempli avec les vrais résultats
```

---

## 🎯 12 points "gratuits"

```
1.  Hostname sur chaque équipement
2.  no shutdown sur TOUTES les interfaces
3.  description sur les interfaces WAN
4.  copy run start après chaque bloc
5.  Loopback0 sur les routeurs OSPF
6.  passive-interface sur tous les LANs OSPF
7.  encapsulation dot1Q X AVANT l'adresse IP
8.  no shutdown sur l'interface PARENT des sous-interfaces
9.  Ping documenté dans le tableau de tests
10. Wildcard calculée correctement
11. Trunk allowed vlan explicite (pas juste "all")
12. show etherchannel summary noté dans la doc
```

---

## 🚨 8 pièges fatals

```
1. Masque OSPF → wildcard : /24=0.0.0.255 /30=0.0.0.3
2. ACL sans permit any → tout bloqué par le deny implicite
3. Tunnel GRE inversé → source/dest IDENTIQUES sur les deux routeurs
4. Interface parent down → sous-interfaces toutes down (no shutdown !)
5. EtherChannel trunk sur Gi au lieu de Port-channel
6. BGP : réseau non dans la table de routage → pas annoncé
7. ACL étendue côté destination → placer PRÈS de la SOURCE
8. copy run start oublié → config disparaît au reload
```

---

## 🔑 Wildcards à connaître par cœur

```
/24=0.0.0.255    /25=0.0.0.127    /26=0.0.0.63
/27=0.0.0.31     /28=0.0.0.15     /29=0.0.0.7
/30=0.0.0.3      /32=0.0.0.0      /20=0.0.15.255
/22=0.0.3.255    /16=0.255.255.255
```

---

## 📐 Ordre de configuration PT

```
1. Adressage IP (interfaces + Loopback + WAN)
2. VLANs + ports access
3. EtherChannel (avant les trunks !)
4. Trunks sur Port-channel
5. Sous-interfaces Inter-VLAN (parent no shutdown d'abord)
6. OSPF / BGP (avec wildcards !)
7. VPN / Tunnel GRE
8. ACL + QoS (EN DERNIER — risque de bloquer)
9. Tests + documentation
```

---

## 💡 Règles des 3 thèmes délicats

```
OSPF :
  network X 0.0.0.WILDCARD area N    ← wildcard PAS masque
  passive-interface sur TOUS les LANs

ACL :
  Standard → filtre SOURCE → placer PRÈS DESTINATION
  Étendue  → filtre src+dst+port → placer PRÈS SOURCE
  Toujours ajouter permit ip any any en fin

GRE :
  Sur Rx : source=IP WAN de Rx · destination=IP WAN de Ry
  Les deux côtés sont INVERSES l'un de l'autre
```

---

## 🏆 Ce qui fait la différence

```
BIEN     = Ça fonctionne
TRÈS BIEN = Ça fonctionne + c'est professionnel
  → passive-interface systématique
  → description sur les interfaces
  → vérifications show documentées
  → justifications précises (pas vagues)
  → schéma complet avec tous les labels
```

---

*Aide-Mémoire Annales E31 — À plastifier*
*BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S14*
