# Audit de la base de connaissances et de son graphe

*Relevé du 18 septembre 2026, sur `main` @ `68c7849`. Demandé par l'auteur :
un audit complet et exhaustif de la KB et du KG. Ce fichier ne voyage pas —
`knowledge/` n'entre dans aucun livre, et le §12 du `CLAUDE.md` le range avec
`context/` et `scripts/`.*

---

## 1. Ce qui a été mesuré

| dimension | état |
|---|---|
| fichiers · sous-commandes · notices | 17 · 15 · **73** — 0 erreur, `valide: true` |
| domaines | grammaire 25 · concepts 12 · méthodes 12 · sources 10 · histoire 6 · interprétations 4 · décisions 4 |
| statuts | synthèse documentaire 49 · renvoi au document 24 |
| ancres internes | **24/24 retrouvées**, 0 perdue |
| sources externes | **30/30 complètes** — titre, url, `consulte_le`, attribution, limite |
| graphe | **1778 nœuds · 5216 relations** |
| — ses types | FormeDeclaree 758 · Fiche 438 · NumeroDeclare 389 · Notice 73 · Unite 58 · SourceWeb 30 · SectionDocumentaire 23 · Domaine 7 · TermeSansFiche 2 |
| cascade de résolution | nom_de_fiche 1362 · puce_du_2_5 92 · graphie_normalisée 33 · forme_déclarée 25 · **irrésolu 2** |
| les 15 commandes | toutes OK, de **0,07 s à 0,56 s** |
| le hook | **8101 car. en 0,30 s** sur une tâche réelle · **0 car. en 0,05 s** sur « ok » |
| épreuves | 31 `knowledge` + 9 `kb-prototype` = **40** — vertes *(42 après ce travail)* |

## 2. Ce qui tient, et tient vraiment

`verifier()` n'est pas décoratif, et il faut le dire avant de dire ce qu'il
rate. Il refuse une synthèse vide ; il **refuse un renvoi qui recopie sa
source**, ce qui tient mécaniquement la promesse « ne copie rien » au lieu de
la confier à la discipline ; il exige `https` et les cinq champs de provenance ;
et `section_source()` refuse une ancre **absente ou ambiguë** — pas seulement
absente, ce qui est le cas difficile.

Le hook fait exactement ce qu'il annonce : il se tait sur un accusé de
réception et verse 8 Ko sur une vraie tâche.

## 3. Le défaut de tête — établi par un test, non déduit

Sur une copie du vault dont le témoin était propre, le contenu d'une section a
été **entièrement réécrit sous un titre inchangé** :

    copie intacte                              valide: True   0 erreur
    contenu ENTIÈREMENT réécrit sous le titre  valide: True   0 erreur

L'ancre se retrouve toujours — c'est le titre, et le titre n'a pas bougé. Rien
n'enregistrait **ce que la section disait** quand la notice a été écrite, donc
la notice continuait d'affirmer ce que la section ne dit plus, et **aucun
contrôle ne pouvait le voir**.

Ce n'est pas théorique. **Onze notices citent `CLAUDE.md`**, dont le dernier
commit est du jour même — et plusieurs de ses §-sections ont été réécrites dans
la journée, par la session qui menait cet audit.

## 4. L'asymétrie qui l'explique

    source externe (registre data.sources)   titre · url · consulte_le · attribution · limite
    source locale  (dans la notice)          source · fichier · ancre

La moitié qui déclarait sa fraîcheur — consultée du 14 au 17 septembre, 30 sur
30 — est **celle qui ne bouge pas**. Celle qui bouge tous les jours n'en
déclarait **aucune**.

La session des langues sources a relevé le même renversement sur son terrain, et
sa formule vaut mieux que la mienne : *on instrumente ce qui est stable parce
que c'est là que l'instrument est facile à écrire*, pas là où il sert. Ses cinq
témoins sont figés — Leningrad, SBLGNT, Dillmann 1851, la Clémentine de 1592 —
et ce sont eux qui portent commit amont, licence et comptes par livre.

## 5. Ce qui a été implémenté

Une **empreinte de la section citée**, posée à la rédaction et recalculée à la
vérification, avec la date et **le commit du vault** :

    "fichier": "CLAUDE.md",
    "ancre": "3.4 Les formes verbales hébraïques (*binyanim*)",
    "empreinte": "6901e3afb45e8090",
    "empreinte_le": "2026-09-18",
    "commit": "68c78491f357"

**Le commit est l'apport de la session des langues sources**, et il change ce
que le signal peut dire :

    empreinte_le    dit QUAND on a regardé
    empreinte       dit QUE ça a changé
    commit          dit CE QUI a changé

parce qu'il rend le diff calculable. *« KB-0027 cite une section qui a bougé »*
est vrai et inexploitable ; le même signal qui imprime
`git diff 68c78491f357..HEAD -- CLAUDE.md` se traite en trente secondes. La
forme est reprise du `MANIFEST.json` des témoins, qui stampe le commit amont de
chaque import pour cette raison exacte.

**Trois choix, et leurs motifs.**

- **Signal, non bloquant.** Une notice périmée n'est pas cassée, elle est *à
  relire*. C'est la distinction que `controles()` porte déjà — `shem_sans_fiche`
  est un signal, `terme_inatteignable` est bloquant. Et un contrôle qui barre
  sur une remise en forme se fait contourner, donc cesse de servir.
- **On empreinte le texte exact, sans normaliser.** Un instrument indulgent ne
  rend pas un verdict approximatif, il rend un verdict faux et toujours dans le
  sens qui arrange — c'est le 98,1 % du §2.5 ter. Le prix est qu'un reflow fait
  rougir ; c'est le bon sens de l'erreur. L'empreinte et la vérification sortent
  du **même `extrait()`**, donc du même tampon : le piège d'`ONT_PRETTY` — un
  fichier indenté publié sous une empreinte calculée en compact — ne mord pas
  ici.

  *(Ce piège était crédité ci-dessus à la session des langues sources, et
  c'était faux : elle me l'avait relayé, non trouvé. Relevé par la session
  macOS, qui a refusé le crédit que je lui prêtais au passage. Le journal de
  l'app tranche sans nous deux — « la mesure vient du vault ». Une attribution
  fausse voyage comme une preuve fausse : elle se relit comme vérifiée.)*
- **`empreinte_le`, et non `revu_le`.** Le champ dit l'acte réellement accompli.
  Personne n'a relu ces vingt-quatre sections aujourd'hui ; on en a pris
  l'empreinte. Nommer autrement ferait exactement ce que cet audit reproche.

**La commande.** `empreinter` pose ce qui manque et **ne rafraîchit jamais une
empreinte périmée toute seule** — le faire effacerait le signal au lieu de le
traiter. Il faut nommer la notice : `--relue KB-0008`, l'acte de celui qui vient
de la relire. C'est la règle de `poser.py` sur les crochets : on pose ce qui
manque, on ne remplace jamais ce qui diverge sans qu'on l'ait demandé.

**La migration** a posé 24 empreintes, rafraîchi 0, laissé 0 périmée.

## 6. Ce que la migration ne certifie pas — et il faut le lire

Poser une empreinte **n'affirme rien sur la justesse des notices**. Elle fixe un
point de départ : à partir d'aujourd'hui, une dérive devient visible.

Le cas gênant est connu et il est nommé ici pour qu'il ne se perde pas : **les
onze notices qui citent `CLAUDE.md` peuvent déjà être périmées**, puisque ce
fichier a été réécrit le jour même du stampage. Les empreinter aujourd'hui gèle
cet état comme référence. **Une relecture de ces onze notices contre leurs
sections reste à faire** — c'est un travail de lecture, pas de code, et il n'a
pas été fait.

## 7. Ce qu'aucun contrôle ne voit encore

- **la justesse d'une synthèse** au regard de sa source. `verifier()` contrôle
  la forme, la provenance et désormais la fraîcheur ; il ne lit pas ;
- **les 2 nœuds `TermeSansFiche` et les 2 résolutions irrésolues** de la
  cascade — signalés, non traités ;
- **cinq occurrences du Voyant sont hors d'atteinte, et la cause est dans le
  témoin.** L'OSHB annote `d/7200` les cinq des Chroniques — *2 Chr* 16:7 et
  16:10, *1 Chr* 9:22, 26:28 et 29:29 — là où il annote `d/7203 a` les cinq de
  *1 Samuel* 9. Même mot, même office, analyse morphologique différente : les
  cinq `7203 a` sont tous des participes (`Vqrmsa`), et les cinq seuls emplois
  de 7200 étiquetés `Ncmsa` sont précisément les cinq Voyants. La table prend
  donc les deux colonnes à l'envers — le numéro du nom là où elle lit un
  participe, celui du verbe là où elle lit un nom —, alors qu'un numéro de
  Strong indexe un lexème et non une analyse de forme.
  Ni la fiche ni la liseuse ne peuvent les atteindre : le hé de l'article est
  une consonne, donc `הָרֹאֶה` ne vaut jamais `רֹאֶה` à aucun étage de
  normalisation. **Le témoin n'est pas retouché** — le `MANIFEST.json` déclare
  l'OSHB avec son commit amont, et modifier un lemme ferait de notre copie
  autre chose que ce qu'elle annonce : ce ne serait plus une inexactitude, ce
  serait une attribution fausse. Déclaré en limite dans `sources/README.md`,
  question portée en amont. Mécanisme établi par épreuve côté liseuse
  (`ce_que_la_garde_fait_des_trois_graphies_de_roeh`), relevé du témoin
  contre-vérifié ici ;
- **le compteur d'usage ne dit encore rien.** `2 lancements · 1 démarrage`. Il a
  été posé le jour même : c'est une mesure de lui-même, pas de l'usage. À relire
  dans une semaine, et à ne citer d'ici là dans aucun arbitrage.

## 8. Les fautes de cet audit, et elles sont du même genre

Trois mesures fausses ont été produites en le menant, toutes par l'instrument et
non par le corpus :

1. `corps` au lieu de `texte` — « 73 notices sans champ » annoncé, faux ;
2. une copie de travail **contaminée** (`sources/` manquant) : refaite en
   comparant les *ensembles* d'erreurs entre copie pristine et copie modifiée.
   C'est pourquoi le test du §3 établit d'abord son témoin ;
3. **« le hook rend 0 caractère »** — le JSON de test n'avait pas
   `hook_event_name`. Le hook allait très bien ; c'est la mesure qui était
   muette, et elle a été annoncée avant d'être vérifiée.

Chaque fois : *un instrument qui répond bien à la mauvaise question*. C'est le
motif que le journal du 25 août a nommé — **le format de sortie survit à
l'absence de mesure** —, et un audit n'en est pas exempté par son objet.

La parade appliquée au §3 est celle que le journal donne déjà : **un instrument
se valide sur un cas dont on connaît la réponse**, jamais sur celui qu'on
étudie. Le témoin propre a été exigé *avant* la réécriture, et c'est lui qui
rend le second chiffre lisible.

---

## 9. Ce que la recherche rate — mesuré, puis corrigé

*Ajouté le 18 septembre 2026, sur demande de l'auteur.*

La KB ne compose pas de phrases : elle retrouve des passages écrits par
quelqu'un. Son README le déclare — *« recherche lexicale dans les documents et
notices ; aucun modèle d'embeddings »*. Restait à savoir ce que ça coûte.

**Le banc.** `knowledge/banc-recherche.py` — douze questions en français, et
pour chacune la source qui y répond, **relevée dans les documents avant tout
lancement**. C'est ce qui le rend utile : une amélioration jugée à l'impression
n'est pas une amélioration.

    départ                          5 trouvées sur 12
    rang moyen quand trouvé         1,2 sur 8 rendus

**Les deux causes des sept ratées, mesurées et non supposées.**

| cause | mesure |
|---|---|
| la **taille de la section** | médiane des ratées **16 094** caractères, des trouvées **3 500** — cinq pour un |
| une **population homogène** | « Prononciation » paraît dans **437** fiches : la source qui fait autorité concourt contre 437 quasi-jumelles |

Les trois plus grosses sections du `CLAUDE.md` — §2.5 (47 605), §3.2 (32 817),
§2.5 ter (16 094) — étaient trois des cibles ratées. Le classement BM25 pénalise
la longueur : **la section qui fait autorité est celle qui perd**.

**Ce que la mesure a corrigé dans la recommandation.** J'allais conseiller des
embeddings. Ils n'auraient pas réparé la cause 1 — ils l'auraient aggravée :
encoder 47 605 caractères en un vecteur produit un vecteur qui ne dit rien. Le
remède est mécanique, non sémantique. *Le gros levier proposé avant mesure,
une fois de plus.*

**Le correctif.** `knowledge/decouper.py` engendre des passages à partir des
sections au-delà de 4 000 caractères — 14 sections, 65 passages, médiane
2 482 caractères. Les sources ne sont pas touchées, et c'est nécessaire : le
`CLAUDE.md` **interdit** de poser un sous-titre dans son §2.5, qui fermerait la
section et rendrait invisibles les formes déclarées dessous. Les sections les
plus grosses sont exactement celles qu'on ne peut pas couper sur place.

    5/12  →  11/12

**Et la mesure a été contrôlée, parce qu'un +6 qui suit une retouche de
l'instrument a la forme suspecte.** Le critère du banc a dû changer — il
exigeait `CLAUDE.md` comme fichier porteur, donc il aurait compté ✗ une bonne
réponse remontée depuis un passage, c'est-à-dire qu'il aurait mesuré
l'emplacement au lieu de la trouvaille. Le contrôle sépare les deux causes :

    nouveau critère, SANS les passages     5/12   ← identique au départ
    nouveau critère, AVEC les passages    11/12

Le changement de critère apporte **zéro**. Le gain vient entièrement du
découpage.

**Un passage n'est pas une seconde source.** Il est engendré, jamais édité, et
il déclare l'empreinte de la section dont il sort. `decouper.py --verifier`
refuse la dérive — éprouvé sur quatre cas dont on connaît la réponse : intact 0,
retouché 1, supprimé 1, régénéré 0. Le pas est dans la CI, et il **échoue** au
lieu de régénérer, comme celui de l'index des décisions : régénérer en silence
ferait diverger le dépôt de ce qui a été relu.

C'est ce qui répond à la crainte de l'auteur — *« il faudra maintenir les
découpes et le CLAUDE en même temps »*. Non : on édite la source, on relance une
commande, et le contrôle se souvient à notre place.

**La ratée qui reste** est la question du qof — la cause 2, que le découpage ne
traite pas. Une pondération par autorité (`CLAUDE.md` est la norme, une fiche en
est une illustration) est le levier suivant, et il se mesurera sur le même banc.
