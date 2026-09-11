# Les références `Bereshit C:V` — ce que chacune désigne

**Relevé, non passe.** Rien n'a été corrigé, rien n'a été commité. Plusieurs de
ces fichiers sont verrouillés, et changer une référence change ce qu'une glose
dit.

Périmètre : `locked/`, `brouillons/`, `in-writing/`, `lexique/`.
Date : 9 septembre 2026.

---

## 1. Le problème, et pourquoi il est petit

Le corpus emploie la notation `Bereshit C:V` sans dire si `C` est **le chapitre
biblique** ou **l'unité ONT**. Les unités de *Bereshit* recouvrent leur chapitre
homonyme sauf trois — 2, 8 et 9 —, donc seules les références `Bereshit 2:N`,
`Bereshit 8:N` et `Bereshit 9:N` peuvent être lues de deux façons.

| écrit | lecture biblique donne | lecture ONT donne |
|---|---|---|
| `Bereshit 2:N` | Gn 2:N | Gn 2:N+3 (N ≤ 8) · Gn 2:N+4 (N ≥ 9) |
| `Bereshit 8:N` | Gn 8:N | Gn 9:N |
| `Bereshit 9:N` | Gn 9:N | Gn 9:N+17 |

**67 occurrences relevées. 20 se tranchent seules** — N dépasse la taille de
l'unité ONT, seule la lecture biblique reste possible. **47 restent**, et c'est
l'objet de ce relevé.

### La carte de l'unité 2, établie et non supposée

L'unité 2 annonce `2:4-25`, soit **vingt-deux versets, et n'en porte que
vingt et un** (¹ à ²¹). Le verset ⁸ réunit **Gn 2:11 et 2:12** — il porte le
Pishon, Chavilah, *puis* l'or **tov**, le *bedolach* et la pierre de *shoham*,
qui sont le contenu de Gn 2:12. Vérifié dans le fichier, non déduit du décompte.

C'est de là que vient le décalage à deux pentes du tableau ci-dessus. Le
pipeline l'avait déjà relevé (`SYNCHRONISATION.md`, 25 août : *« deux ont été
réunis »*) sans dire lesquels.

**Conséquence directe :** `Bereshit 2:22` n'a **aucun référent ONT** — l'unité
s'arrête à ²¹. Les trois occurrences de cette forme sont tranchées par la borne,
pas par le contenu.

### Contrôle de l'instrument

`Bereshit 9:8` dans `bereshit-10.md` devait ressortir en lecture **ONT**. Il en
ressort — ligne 2 du tableau. Le compte 47 / 20 tombe exactement sur celui de la
commande. L'instrument est validé sur un cas dont la réponse était connue.

---

## 2. Le relevé — 47 lignes

Les fichiers de `locked/…/01. bereshit` et `brouillons/…/01. bereshit` sont
abrégés en `bereshit-N.md` ; ceux de *Toledot* en `toledot-N.md`.

| # | fichier | référence écrite | ce que la glose annonce | lecture biblique | lecture ONT | verdict | preuve |
|---|---|---|---|---|---|---|---|
| 1 | bereshit-10.md L18 | `Bereshit 2:10` | *vayipared* — le fleuve du Jardin se divise en quatre bras | Gn 2:10 — le fleuve, quatre bras | Gn 2:14 — le Chiddeqel et le Prat | **biblique** | la glose décrit littéralement Gn 2:10 |
| 2 | bereshit-10.md L22 | `Bereshit 9:8` | Kenaʿan frappé de dysfonctionnement par la prononciation de Noach | Gn 9:8 — « **ʾElohim** formula à Noach », ouverture de la **berith** | Gn 9:25 — « Kenaʿan est frappé de dysfonctionnement » | **ONT** | seule la lecture ONT porte l'*arur* ; la biblique ne dit rien de Kenaʿan |
| 3 | bereshit-10.md L24 | `Bereshit 2:11-12` | Chavilah — pays de l'or, du *bdellium*, de la pierre de *shoham* | Gn 2:11-12 — exactement ces trois | Gn 2:15-16 — le mandat, puis l'instruction | **biblique** | les trois matériaux sont nommés |
| 4 | bereshit-10.md L72 | `Bereshit 9:9` | « le programme de *YHWH Elohim Shem* » | Gn 9:9 — « me voici, j'établis mon **berith** » | Gn 9:26 — « Acclamé soit **YHWH**, **ʾElohim** de Shem » | **ONT** | la glose cite la formule mot pour mot ; elle n'est qu'en Gn 9:26 |
| 5 | bereshit-10.md L74 | `Bereshit 2:11-12` | la Chavilah du fleuve, distincte des deux de la table des nations | Gn 2:11-12 | Gn 2:15-16 | **biblique** | même preuve que #3 |
| 6 | bereshit-10.md L82 | `*Bereshit* 2:10` | *parad* au niphal — le fleuve d'Eden se divisant en quatre bras | Gn 2:10 | Gn 2:14 | **biblique** | même preuve que #1 |
| 7 | bereshit-10.md L91 | `Bereshit 2:10` | note de pied : *nifredou*, même racine que *vayipared* | Gn 2:10 | Gn 2:14 | **biblique** | même preuve que #1 |
| 8 | bereshit-11.md L15 | `Bereshit 2:22` | *banah* — la construction de l'**ʾIshah** | Gn 2:22 — « il édifia le flanc en une **ʾishah** » | *n'existe pas* — l'unité 2 s'arrête à ²¹ | **biblique** (borne) | la lecture ONT est hors plage |
| 9 | bereshit-15.md L34 | `Bereshit 2:21` | *tardemah* — le sommeil où le flanc est pris | Gn 2:21 — le sommeil profond | Gn 2:25 — nus, sans honte | **biblique** | la glose nomme la prise de la côte |
| 10 | bereshit-15.md L48 | `Bereshit 2:14` | le Prat / l'Euphrate, « déjà posé » | Gn 2:14 — le Prat | Gn 2:18 — « il ne fait pas bon que l'**ʾadam** soit seul » | **biblique** | seule Gn 2:14 nomme le Prat |
| 11 | bereshit-15.md L64 | `Bereshit 2:21` | note de pied : écho du sommeil de l'**ʾadam** | Gn 2:21 | Gn 2:25 | **biblique** | même preuve que #9 |
| 12 | bereshit-16.md L10 | `Bereshit 2:22` | *vayiven et-hatsela* — cité en hébreu | Gn 2:22 | *n'existe pas* | **biblique** (borne) | l'hébreu cité est celui de Gn 2:22 |
| 13 | bereshit-17.md L24 | `*Bereshit* 2:15` | *shamar* — la garde du Jardin | Gn 2:15 — « pour le servir et le garder » | Gn 2:19 — le façonnage des bêtes | **biblique** | seule Gn 2:15 porte *shamar* |
| 14 | bereshit-17.md L28 | `*Bereshit* 9:12` | *ot* — le signe de l'arc dans la nuée | Gn 9:12 — « Voici le signe de la **berith** » | Gn 9:29 — Noach mourut | **biblique** | seule la biblique porte le signe |
| 15 | bereshit-17.md L50 | `*Bereshit* 2:1-2` | *kalah* — les Cieux et la Terre atteignent leur plénitude, puis la cessation | Gn 2:1-2 — exactement cela | Gn 2:4-5 — les *toledot*, l'absence d'arbrisseau | **biblique** | Gn 2:1-3 relève de l'unité **1** ; en lecture ONT la référence eût été `Bereshit 1:32` |
| 16 | bereshit-18.md L62 | `*Bereshit* 2:7, 3:19` | *afar* — la poussière dont l'**ʾadam** est fait | Gn 2:7 — *ʿafar min ha-ʾadamah* | Gn 2:10 — le fleuve | **biblique** | l'appariement avec 3:19, biblique lui aussi, ferme la lecture |
| 17 | bereshit-6.md L19 | `Bereshit 2:9` | **raʿ** « déjà posé » | Gn 2:9 — l'arbre de la **daʿat tov varaʿ** | Gn 2:13 — le Gichon | **biblique** | le §2.5 fixe le premier emploi de **raʿ** en *Bereshit* 2:9 |
| 18 | toledot-1.md L8 | `*Bereshit* 2:8` | le Jardin planté *miqqedem*, à l'orient | Gn 2:8 — « planta un Jardin en Eden, à l'orient » | Gn 2:11 — le Pishon | **biblique** | *miqqedem* n'est qu'en Gn 2:8 |
| 19 | toledot-1.md L8 | `*Bereshit* 2:9` | « l'autre arbre du milieu du Jardin » | Gn 2:9 — les deux arbres | Gn 2:13 — le Gichon | **biblique** | seule Gn 2:9 nomme les arbres |
| 20 | toledot-1.md L8 | `*Bereshit* 2:16` | « donnait tout arbre du Jardin » | Gn 2:16 — « de tout arbre du Jardin, manger tu mangeras » | Gn 2:20 — le nommage des bêtes | **biblique** | la glose paraphrase Gn 2:16 |
| 21 | toledot-1.md L12 | `*Bereshit* 2:16` | citation entre guillemets de la formule | Gn 2:16 | Gn 2:20 | **biblique** | la glose **cite** le verset |
| 22 | toledot-1.md L12 | `*Bereshit* 2:7` | les narines où la **Neshamah** fut insufflée | Gn 2:7 | Gn 2:10 | **biblique** | la **Neshamah** n'est qu'en Gn 2:7 |
| 23 | toledot-3.md L8 | `*Bereshit* 2:9` | la **daʿat**, « celle de l'arbre » | Gn 2:9 | Gn 2:13 | **biblique** | même preuve que #19 |
| 24 | toledot-3.md L10 | `*Bereshit* 9:3` | la chair donnée en nourriture après le **mabbul** | Gn 9:3 — « tout rampant vivant vous servira de nourriture » | Gn 9:20 — Noach, l'**ʾIsh** de la *ʾadamah*, la vigne | **biblique** | la glose énonce le contenu de Gn 9:3 |
| 25 | toledot-3.md L10 | `*Bereshit* 2:15` | *avad* — « le mot même du mandat donné dans le Jardin » | Gn 2:15 | Gn 2:19 | **biblique** | même preuve que #13 |
| 26 | toledot-4.md L14 | `*Bereshit* 2:9` | l'arbre de la Vie | Gn 2:9 | Gn 2:13 | **biblique** | même preuve que #19 |
| 27 | toledot-5.md L8 | `*Bereshit* 2:19` | *vayave*, hiphil — les vivants amenés à l'**ʾadam** pour recevoir leur **Shem** | Gn 2:19 — exactement cela | Gn 2:23 — « os de mes os » | **biblique** | la glose cite *vayave* et sa forme |
| 28 | toledot-8.md L8 | `*Bereshit* 2:7` | la **Neshamah** soufflée bouche contre narines | Gn 2:7 | Gn 2:10 | **biblique** | même preuve que #22 |
| 29 | toledot-8.md L8 | `*Bereshit* 2:7` | *ʿafar min ha-ʾadamah*, cité en hébreu | Gn 2:7 | Gn 2:10 | **biblique** | l'hébreu cité est celui de Gn 2:7 |
| 30 | toledot-9.md L8 | `*Bereshit* 2:22` | *banah* — « le verbe de l'architecte » | Gn 2:22 | *n'existe pas* | **biblique** (borne) | la lecture ONT est hors plage |
| 31 | sefar-gibbaraya-1.md L8 | `*Bereshit* 2:15` | « servir et garder », les deux verbes du Jardin | Gn 2:15 | Gn 2:19 | **biblique** | même preuve que #13 |
| 32 | sefar-gibbaraya-1.md L18 | `*Bereshit* 8:1` | *zakar* — **ʾElohim** se souvient de Noach, un souffle passe, les eaux baissent | Gn 8:1 — exactement cela | Gn 9:1 — **ʾElohim** dote Noach | **biblique** | le souvenir et la baisse des eaux ne sont qu'en Gn 8:1 |
| 33 | sefar-gibbaraya-1.md L24 | `*Bereshit* 2:15` | « servir et garder », dans le même ordre | Gn 2:15 | Gn 2:19 | **biblique** | même preuve que #13 |
| 34 | sefar-gibbaraya-10.md L18 | `*Bereshit* 8:1` | la **Ruach** repasse sur les eaux, « écho de 1:2 » | Gn 8:1 | Gn 9:1 | **biblique** | l'écho de Gn 1:2 est en Gn 8:1 |
| 35 | sefar-gibbaraya-2.md L14 | `*Bereshit* 9:6` | le droit du sang : on ne verse pas le sang de l'**ʾadam**, représentant d'**ʾElohim** | Gn 9:6 — exactement cela | Gn 9:23 — Shem et Yafet, le manteau | **biblique** | l'argument est celui de Gn 9:6 |
| 36 | sefar-gibbaraya-6.md L14 | `*Bereshit* 2:8` | « **YHWH** **ʾElohim** planta un jardin en Eden » | Gn 2:8 | Gn 2:11 | **biblique** | la glose cite le verset |
| 37 | bereshit-13.md L34 | `Bereshit 2:9` | **raʿ** « déjà posé » | Gn 2:9 | Gn 2:13 | **biblique** | même preuve que #17 |
| 38 | bereshit-13.md L41 | `Bereshit 2:7` | *ʿafar min ha-ʾadamah*, cité en hébreu | Gn 2:7 | Gn 2:10 | **biblique** | même preuve que #29 |
| 39 | bereshit-19.md L18 | `*Bereshit* 2:9` | racine de **raʿ**, « posé en » | Gn 2:9 | Gn 2:13 | **biblique** | même preuve que #17 |
| 40 | bereshit-19.md L56 | `*Bereshit* 8:1` | *vayizkor Elohim et Noach*, cité en hébreu | Gn 8:1 | Gn 9:1 | **biblique** | l'hébreu cité est celui de Gn 8:1 |
| 41 | chazon-avraham-2.md L62 | `*Bereshit* 2:15` | *leʿovdah* — le mandat donné à l'**ʾadam** dans le Jardin | Gn 2:15 | Gn 2:19 | **biblique** | même preuve que #13 |
| 42 | chazon-avraham-2.md L99 | `*Bereshit* 2:15` | *leʿovdah uleshomrah*, cité en hébreu | Gn 2:15 | Gn 2:19 | **biblique** | l'hébreu cité est celui de Gn 2:15 |
| 43 | lexique/Chavilah.md L29 | `*Bereshit* 2:11-12` | « pour le pays du fleuve » | Gn 2:11-12 | Gn 2:15-16 | **biblique** | même preuve que #3 |
| 44 | lexique/YHWH Elohim.md L47 | `*Bereshit* 2:4 à 3:24` | « où la formule paraît vingt fois » | Gn 2:4-3:24 — les vingt emplois de **YHWH ʾElohim** | Gn 2:7-… — commencerait après le premier emploi | **biblique** | le compte de vingt ne tombe qu'à partir de Gn 2:4, où la formule paraît pour la première fois |
| 45 | lexique/gan.md L33 | `*Bereshit* 2:8-15` | du Jardin planté jusqu'aux verbes *avad* et *shamar* | Gn 2:8-15 — plantation → mandat, bornes exactes | Gn 2:11-19 — du Pishon au façonnage des bêtes | **biblique** | les deux bornes annoncées sont Gn 2:8 et Gn 2:15 |
| 46 | lexique/mut.md L15 | `*Bereshit* 2:17` | *mot tamut* — « mourir tu mourras » | Gn 2:17 — la formule | Gn 2:21 — le *tardemah* | **biblique** | *mot tamut* n'est qu'en Gn 2:17 |
| 47 | lexique/mut.md L31 | `*Bereshit* 2:17 et 3:4` | l'interdit et sa contre-parole | Gn 2:17 / Gn 3:4 | Gn 2:21 / Gn 3:4 | **biblique** | l'appariement avec 3:4, biblique, ferme la lecture |

---

## 3. Les chiffres

    lecture biblique      45
    lecture ONT            2   (#2 et #4, toutes deux dans bereshit-10.md)
    indifférent            0
                          ──
                          47

**Zéro indifférent.** La commande prévoyait le cas ; il ne s'est pas présenté.
Sur les 47, les deux candidats donnaient toujours un texte différent — parce que
le décalage est d'au moins trois versets sur l'unité 2 et de dix-sept sur
l'unité 9.

Trois des 45 (#8, #12, #30) sont tranchées **par la borne** et non par le
contenu : `Bereshit 2:22` n'a pas de référent ONT. Leur contenu allait dans le
même sens, mais la borne suffisait.

---

## 4. Le motif — et il n'est pas celui qu'on attendait

**La commande posait deux conventions en usage. Les mesures disent autre chose :
une seule convention, universelle, et deux glissements dans un seul fichier.**

### Ce qui ne varie pas

Aucun des découpages proposés ne sépare quoi que ce soit :

| axe | résultat |
|---|---|
| `locked/` vs `brouillons/` | aucun écart — les deux citent biblique |
| corps vs `lexique/` | aucun écart — les cinq fiches citent biblique |
| *Bereshit* vs *Toledot* vs *Sefar Gibbaraya* vs *Chazon Avraham* | aucun écart |
| unité 2 vs unité 8 vs unité 9 | aucun écart, hors les deux cas |

Répartition des 47 par forme, et verdict :

    Bereshit 2:N     39 occurrences     39 biblique,  0 ONT
    Bereshit 8:N      3 occurrences      3 biblique,  0 ONT
    Bereshit 9:N      5 occurrences      3 biblique,  2 ONT

Les 39 références de `Bereshit 2:N` sont biblique **sans exception**, et les
trois `Bereshit 8:N` aussi. Toute la divergence tient dans la forme
`Bereshit 9:N`, et dans un seul fichier.

### Ce qui varie, et où exactement

Les deux seules lectures ONT sont dans `bereshit-10.md`, et le même fichier
cite le **même passage** en biblique ailleurs :

    L22   « la prononciation de Noach tombe sur Kenaʿan seul (Bereshit 9:25) »   biblique
    L22   « frappé de dysfonctionnement … en Bereshit 9:8 »                       ONT
          ── les deux désignent Gn 9:25, sur la même ligne, notées autrement

    L12, L58, L102   « Bereshit 9:27 » pour yaft Elohim leYafet                   biblique
    L28              « Bereshit 9:20 » pour la vigne                              biblique
    L72              « Bereshit 9:9 » pour barukh YHWH Elohei Shem                ONT

Ce n'est donc pas une convention concurrente : c'est **une contamination locale**,
dans un fichier qui applique par ailleurs la convention biblique, y compris sur
les versets voisins.

### Le mécanisme, et sa trace

Ligne 58 de `bereshit-10.md` porte la forme hybride :

> *YHWH Elohim Shem* (Bereshit **9:27 v.9** : la première identification
> explicite de **YHWH** avec une lignée particulière)

`v.9` est l'exposant ⁹ de l'unité 9 — soit Gn 9:26, qui est bien le verset de
*barukh YHWH Elohei Shem*. La référence a donc été écrite **en lisant les
exposants du fichier ONT**, puis doublée d'une référence biblique approximative.
Quatorze lignes plus bas, le `v.` tombe et il ne reste que `Bereshit 9:9`.

**Le mécanisme se confirme hors du périmètre.** `CLAUDE.md` §4.16 tabule :

    akhol tokhel   Bereshit 2:12
    mot tamut      Bereshit 2:13

Ce sont exactement les labels ¹² et ¹³ de l'unité 2, soit Gn 2:16 et 2:17.
Tomber là **exige** de connaître la fusion de Gn 2:11-12 dans le verset ⁸ —
c'est-à-dire de recopier les exposants du fichier. Et `lexique/mut.md` écrit
`*Bereshit* 2:17` pour la même formule : **les deux documents se contredisent**.

*Aucune faute d'inattention ne produit ce profil.* Un chiffre glissé donnerait
un verset voisin ; ici l'on tombe **au verset exact**, à l'endroit exact où
l'exposant se trouve.

### La convention qui en découle

**Lecture biblique partout.** C'est ce que 45 références sur 47 appliquent, ce
que toutes les fiches de `lexique/` appliquent, et ce que le pipeline a déjà
implémenté. Les deux glissements sont des **corrections à programmer**, non un
usage à préserver.

---

## 5. Ce que ça change pour `ONTBibleApp` — à relayer

`SYNCHRONISATION.md`, entrée du 25 août 2026, dit que **218 renvois sont déjà
liés**, résolus selon la lecture biblique : *« Bereshit 9:27 » mène à
`bereshit-9?v=10`*.

Les deux glissements sont donc **un défaut de destination déjà en production** :

| écrit | où le lien mène aujourd'hui | où la glose voulait mener |
|---|---|---|
| `Bereshit 9:8` | unité 8, verset ⁸ — l'ouverture de la **berith** | unité 9, verset ⁸ — l'*arur* sur Kenaʿan |
| `Bereshit 9:9` | unité 8, verset ⁹ — « me voici » | unité 9, verset ⁹ — *barukh YHWH Elohei Shem* |

Le lecteur qui touche « Kenaʿan frappé de dysfonctionnement » arrive sur un
verset qui ne parle pas de Kenaʿan. C'est exactement le mode d'échec que le
§2.5 ter décrit pour la résolution morphologique : *une substitution silencieuse
vaut moins qu'un mot inerte*.

**La correction relève de l'auteur** : `bereshit-10.md` est verrouillé, et
changer une référence change ce qu'une glose dit.

---

## 6. Doutes, et ce que ce relevé ne prouve pas

1. **Intention contre désignation.** Les 47 verdicts disent ce que chaque
   référence *désigne*, établi sur le contenu de la phrase porteuse. Ils ne
   disent pas ce que l'auteur *voulait* écrire. Pour #2 et #4, les deux se
   rejoignent — la glose décrit le verset ONT et rien d'autre. Il reste possible
   que `9:8` ait été voulu comme `9:25` mal recopié ; la trace `9:27 v.9` de la
   ligne 58 rend cette hypothèse moins probable qu'une lecture d'exposants,
   mais elle ne l'exclut pas.

2. **Les 20 références « forcées » n'ont pas été auditées**, et l'une au moins
   est fautive : `Bereshit 9:27 v.9` (L58) donne `9:27` là où la formule citée
   est en Gn **9:26**. Le fait qu'une lecture soit forcée ne dit pas qu'elle
   soit juste. Un second relevé, hors périmètre de celui-ci, reste à faire.

3. **`CLAUDE.md` §4.16 est hors des quatre racines** et n'entre pas dans le
   compte. Sa contradiction avec `lexique/mut.md` est signalée, non tranchée.

4. **La fusion Gn 2:11-12 est établie par le contenu du verset ⁸**, non par une
   déclaration du fichier. Le décalage à deux pentes en dépend. Trois témoins
   indépendants le corroborent : le verset ⁹ porte le Gichon (Gn 2:13), le
   verset ¹⁰ le Chiddeqel (Gn 2:14), et le pipeline avait relevé le manque d'un
   verset sans l'expliquer.

5. **Les autres livres n'ont pas été balayés.** Ce relevé ne porte que sur
   `Bereshit 2:`, `8:` et `9:`. Une unité ONT d'un autre livre qui s'écarterait
   de son chapitre homonyme rouvrirait la même question — et rien ici ne dit
   qu'il n'y en a pas.
