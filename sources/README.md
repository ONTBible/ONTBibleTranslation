# `sources/` — les textes en langue source

Ce que le lecteur voit quand il appuie longuement sur un verset : le texte
**dans sa langue**, hébreu ou grec, avec son analyse morphologique.

Rien ici n'est de l'ONT. Ce sont trois éditions critiques extérieures,
reprises telles quelles, et c'est tout leur intérêt : la couche fonctionnelle
de l'ONT se lit **contre** un texte qu'elle n'a pas choisi.

---

## Les cinq témoins

| dossier | témoin | texte | analyse |
|---|---|---|---|
| `he-wlc/` | Westminster Leningrad Codex | domaine public | **OSHB** — CC BY 4.0 |
| `grc-sblgnt/` | SBL Greek New Testament | CC BY 4.0 | **MorphGNT** — CC BY-SA 3.0 |
| `grc-byz/` | Robinson-Pierpont, RP2018 | domaine public | domaine public |
| `gez-dillmann/` | Dillmann 1851 — guèze | domaine public | *(aucune)* |
| `lat-vulgata/` | Vulgate clémentine 1592 — latin | domaine public | *(aucune)* |

Le guèze et le latin ne sont pas des langues du corpus : voir plus bas.

Les deux témoins grecs sont **côte à côte, sans marquage des divergences** —
décision de l'auteur du 30 août 2026. L'un est éclectique, l'autre byzantin ;
l'ONT ne tranche pas entre eux et ne les aligne pas mot à mot.

`MANIFEST.json` porte, par source : la licence, l'attribution exacte, le
commit amont d'où l'import a été tiré, et le compte de chaque livre.

## L'apparat du SBLGNT — et ce qu'il n'est pas

`sources/grc-sblgnt/<livre>-apparat.jsonl` — **6 934 entrées**, même licence
CC BY que le texte.

**Il ne compare pas des manuscrits.** Il compare ==quatre éditions imprimées
modernes== : Westcott-Hort 1881, Tregelles 1857, Nestle-Aland 2012 et
Robinson-Pierpont. Une entrée dit « ici, WH porte ceci et NA28 porte cela ».
Elle ne dira ==jamais== ce que porte un codex ancien.

C'est un piège de vocabulaire, et le lecteur doit en être protégé : « apparat
critique » évoque des manuscrits, et celui-ci n'en montre aucun. Le libellé de
la liseuse doit tenir cette différence.

**Un quart est déjà à l'écran** : Robinson-Pierpont est l'une des quatre
éditions comparées, et l'ONT l'affiche comme second témoin grec. Le lecteur
*voit* cette divergence-là au lieu de lire qu'elle existe.

**Les doubles crochets sont conservés.** `⟦WH⟧` ne veut pas dire « WH » : il
veut dire ==WH imprime le passage mais le tient pour douteux==. Les endroits où
la notation paraît ne sont pas quelconques — la sueur de sang de *Luc* 22:43-44,
le « Père, pardonne-leur » de *Luc* 23:34, la finale longue de *Marc* 16:9-20,
la péricope de la femme adultère. Le champ `crochets` les porte ; les jeter
aurait fait dire à Westcott-Hort qu'ils tenaient pour sûr ce qu'ils ont
précisément voulu mettre en doute.

**Et le `;` grec est un point d'interrogation**, non un séparateur. Le
découpage des variantes ne coupe qu'après un sigle d'édition — couper sur tous
les `;` briserait chaque variante contenant une question, et le ferait en
silence puisque les morceaux resteraient du grec bien formé.

## L'attribution voyage avec la source

Elle est dans `MANIFEST.json`, à côté des données qu'elle couvre — jamais
dans un écran « à propos » tenu ailleurs. Un écran séparé se désynchronise le
jour où une source est ajoutée, et personne ne le voit.

Robinson-Pierpont n'exige rien. Le SBLGNT et OSHB exigent d'être crédités, et
le SBLGNT interdit d'être **vendu seul** — ce que l'ONT ne fait pas.

## `mgnt` est un îlot fermé, et une machine le tient

MorphGNT est en **CC BY-SA** : une clause de copyleft, donc contagieuse. Ses
étiquettes vivent dans le seul champ `mgnt`, et ==rien de la couche
fonctionnelle de l'ONT ne doit y entrer==. Un schéma qui les fusionne ne se
défusionne pas, et la clause mordrait alors sur le travail de l'auteur.

C'est la seule contrainte de ce chantier qui ne se rattrape pas après coup.
Elle n'est donc pas confiée à l'attention de qui écrira ensuite :
`scripts/eprouver-les-sources.py` refuse tout champ non déclaré à l'intérieur
de `mgnt`.

Le même cloisonnement est appliqué à l'hébreu (`oshb`) alors que CC BY ne
l'exige pas — une seule règle vaut mieux que deux.

---

## La forme, et ce qu'elle ne décide pas

Un fichier **JSONL par livre-source**, une ligne par verset :

    {"ref":"Gen.1.1","c":1,"v":1,"w":[{"t":"בְּרֵאשִׁ֖ית","oshb":{"lem":"7225","morph":"HR/Ncfsa","id":"…"}}]}

Le classement est **par référence biblique**, qui est la clé native des trois
sources. Ce dossier ==ne connaît ni les **parashiot** ni la numérotation
interne des unités ONT== (§2.2) : la jointure unité → référence est au
pipeline.

C'est délibéré, et c'est le bon joint. `dist/` n'est pas arrêté — `schema.rs`
est encore en discussion. Et surtout : la correspondance « unité ONT ↔ versets
bibliques » vit dans le sous-titre de chaque unité, et elle bougera encore ;
les données sources, elles, ne bougeront jamais.

`MANIFEST.json` porte quand même la correspondance livre-source → numéro ONT,
en **un seul endroit déclaratif** que l'auteur peut corriger sans toucher aux
93 fichiers de données.

L'ONT réunit ce que les éditions séparent — *Shemuel*, *Melakhim*,
*Ezra-Nehemyah*, *Divrei Hayamim* — d'où plusieurs livres-sources sur un même
numéro. Les références restent distinctes (`1Sam.1.1` et `2Sam.1.1`).

## Ce que le byzantin a demandé de coudre

Robinson-Pierpont est publié en deux jeux disjoints, et aucun ne suffit :
l'un porte les accents et la ponctuation mais aucune analyse, l'autre le
Strong et l'analyse mais un texte tout en minuscules et **sans accents**.

Prendre le second seul aurait donné un byzantin nu affiché à côté d'un SBLGNT
accentué — deux témoins qu'on présente côte à côte et qui n'auraient pas eu la
même mise. Les deux sont donc recousus mot à mot, et la couture est
**vérifiée** plutôt que supposée : l'import s'arrête net si un verset dément
l'alignement. Il tient sur les 7 953 versets.

---

## Le guèze, et pourquoi il est à part

*1 Chanokh* ne nous est parvenu ni en hébreu ni en grec. Le seul témoin complet
est en **guèze**, l'éthiopien classique — et le guèze traduit le grec, qui
traduisait l'araméen. ==C'est un témoin de second degré, et le dire fait partie
de l'honnêteté de la couche== : partout où l'araméen de Qumrân subsiste, c'est
lui qui prime, parce que c'est la langue dans laquelle le livre a été pensé.

L'assise est **Dillmann, Leipzig 1851**, la première édition critique, dans le
domaine public. Elle a un prix qu'il faut nommer : ==Dillmann n'a pas vu
Qumrân==, ayant établi son texte un siècle avant le premier fragment.

**La saisie appartient à quelqu'un, et il a dit oui.** Le texte informatique
vient de Michal Jerabek (1995), converti en Unicode par **Ran HaCohen** (2011),
université de Tel-Aviv. Sa notice n'autorisait que l'usage non commercial ; il a
donné son accord explicite le 1er septembre 2026, ==à une condition qui
n'expire pas== : être tenu informé du projet. L'épreuve refuse d'ailleurs toute
saisie sous clause non commerciale dont la permission n'est pas déclarée.

**Le découpage en versets est déduit, non donné.** Les pages ne portent qu'un
numéro de chapitre ; les frontières viennent du `።` et de 14 corrections
vérifiées. Le détail, et ce qui reste ouvert, sont dans l'en-tête de
`scripts/importer-le-gueze-de-chanokh.py`.

## Le latin, et une censure médiévale qu'on ne masque pas

Le *Chazon Ezra* n'est conservé dans aucune langue sémitique. Son témoin
principal est le latin, par lequel il a traversé le Moyen Âge glissé en
appendice de la Vulgate. Comme le guèze, ==c'est un témoin de second degré== :
le latin traduit un grec perdu, qui traduisait un hébreu perdu.

L'assise est la **Vulgate clémentine de 1592**, domaine public ; Wikisource n'en
est que le transporteur. On n'importe que les **chapitres 3 à 14** : les
chapitres 1-2 et 15-16 sont des additions chrétiennes hellénisées, que le
critère d'inclusion de l'ONT écarte.

**Soixante-dix versets manquent, et ce n'est pas un accident.** Le passage
7:36-105 porte sur l'intercession pour les morts, et il a été ==retranché des
manuscrits latins au Moyen Âge== parce qu'il la refusait. Robert Bensly l'a
retrouvé en 1875 dans un manuscrit du IXᵉ siècle d'Amiens qui avait échappé au
couteau — mais son édition n'existe qu'en fac-similé, et son OCR est illisible.
Le syriaque, lui, n'a jamais subi cette censure : c'est par là que la lacune se
comblera.

**Et la numérotation est celle de la norme, parce qu'un numéro de verset est un
système de renvoi.** « Chazon Ezra 7:120 » doit désigner la même chose ici et
partout ailleurs.

La Clémentine, elle, numérote son chapitre 7 de 1 à 69 sans trou : chez elle la
lacune tombe **entre** 7:35 et 7:36. Le décalage a d'abord paru invérifiable —
69 + 70 = 139, quand la norme va à 140. Un verset d'écart, sans témoin pour
dire d'où il venait.

==Il venait du texte lui-même.== Le dernier verset clémentin fait 171 signes
quand les autres du chapitre en font 96, et il porte deux propositions : la
Clémentine **fusionne ses deux derniers versets**. Le décalage de +70 a ensuite
tenu sur quatre ancres — 7:36, 44, 50 et 68 tombant sur 7:106, 114, 120 et 138.

    clémentine 7:1-35    →  7:1-35            inchangé
    clémentine 7:36-68   →  7:106-138         décalé de +70
    clémentine 7:69      →  7:139 + 7:140     défusionné

Les versets 36 à 105 n'existent donc pas dans ce fichier, et c'est la vérité :
ils manquent au témoin latin.

L'épreuve garde la règle qui va avec : une source qui déclare une lacune doit
dire ce que sa numérotation en fait.

## Ce que cette couche ne couvre pas

**64 livres ONT sur 70.** Les six qui restent sont le corpus étendu — ceux dont
aucun témoin exploitable et librement réutilisable n'a encore été obtenu :

    06  Yovelim                    39  Chazon Avraham
    36  Toledot Adam ve-Chavah     40  Tsava'at Levi
    37  Sefar Gibbaraya            43  Chazon Barukh

Ils survivent en guèze, en slavon, en syriaque ou par fragments araméens. Pour
le *Chazon Avraham*, ==il n'existe aucune édition slavonne ouverte et lisible
par machine== : un appui long sur un de ses versets n'aura rien à montrer, et
c'est précisément le livre en cours d'écriture.

Ce n'est pas un manque de l'import : c'est l'état du corpus. Le dire ici vaut
mieux que de le laisser découvrir à l'usage.

## `pont-septante/` — un outil de travail, jamais un témoin

Décision de l'auteur du 9 septembre 2026 : **le pont n'est pas déclaré au
`MANIFEST.json`**, donc le lecteur ne le voit pas. Le manifeste est le seul
interrupteur — `sources.rs` n'émet que les clés qu'il y trouve, et un dossier
non déclaré ne produit rien.

**Ce que c'est.** Pour chaque morphème hébreu du Westminster Leningrad Codex,
le mot grec que la Septante lui oppose et son numéro de Strong. 319 783
appariements, 39 livres, ==69 % de couverture==. La donnée vient de MACULA
Hebrew (Biblica, CC BY 4.0).

**Ce que ce n'est pas — et ses auteurs le disent avant nous.** La documentation
de MACULA écrit : *« a tentative alignment to the Septuagint […] This data has
never been manually checked and is released as a starting point for further
work. »* Pris mot à mot, il se trompe — en *Daniel* 7 il apparie *chelem*, le
songe, à κεφαλή, la tête.

**C'est pourquoi on compte au lieu de lire.** Une erreur isolée est du bruit
dans un dénombrement, décisive dans une lecture. Quand 2 146 occurrences
d'*asah* sur 2 269 tombent sur ποιέω, aucune poignée d'appariements faux ne
fabrique ce chiffre. ==Faible au mot, fort à l'agrégat== — et l'ONT ne lui
demande que l'agrégat.

**Trois limites à connaître avant de s'en servir :**

- ==un seul sens==. Il n'existe aucun identifiant de mot grec : on va de
  l'hébreu vers le grec, jamais l'inverse. Les *plus* de la Septante — ce
  qu'elle ajoute et que l'hébreu n'a pas — sont invisibles ;
- ==l'araméen est écarté==. L'appariement de *Daniel* 2:4-7:28 et d'*Ezra* 4-7
  est manifestement faux ; 7 529 morphèmes sont retirés plutôt que comptés de
  travers ;
- ==l'édition grecque n'est nommée nulle part==. Ni le dépôt ni sa
  documentation ne disent si le grec vient de Rahlfs ou de Göttingen. On ne le
  devine pas : le pont n'énonce que des **numéros de Strong**, qui sont de 1890
  et libres de droits.

### L'interversion χ / ξ, et pourquoi on ne la répare pas

Les formes grecques portent un défaut d'encodage systématique — `ἀρξῇ` pour
ἀρχῇ, `ξόρτου` pour χόρτου, `ψυξὴν` pour ψυχήν. Il est signalé chez MACULA
(issue #81), déclaré résolu, et ==il est toujours dans les données livrées==.

Il paraît réparable par un simple échange des deux lettres. **Mesuré, il ne
l'est pas.** Sur les 1 474 formes distinctes concernées, contrôlées contre le
lemme Strong de chacune :

    l'inversion répare        1 048
    la forme était déjà juste    55      ← ἔβρεχεν · ἕχει · ἐλέγχει
    indécidable                 371

Un échange en masse casserait les cinquante-cinq, ==et rien ne le dirait==. On
s'en tient donc aux numéros, sains, et les formes ne servent qu'à illustrer.

## L'attribution du pont

    MACULA Hebrew Linguistic Datasets, available at
    https://github.com/Clear-Bible/macula-hebrew/
    © 2022-2024 Biblica, Inc — CC BY 4.0

Les colonnes SDBH et MARBLE du même dépôt (`sdbh`, `lexdomain`, `coredomain`)
sont « used with permission » et ==non couvertes par le CC BY== — une issue
ouverte chez eux pose exactement cette question, sans réponse. **On ne les lit
pas**, et l'importateur ne les extrait pas.

Le dictionnaire qui rend les numéros grecs lisibles est le Strong de 1890,
domaine public, par la transcription de MorphGNT. Aucune définition n'en est
reprise — seulement le lemme.

## Refaire l'import

    ./scripts/importer-les-textes-sources.py --depots <dossier> --cloner
    ./scripts/importer-le-gueze-de-chanokh.py
    ./scripts/importer-le-latin-de-chazon-ezra.py
    ./scripts/importer-l-apparat-du-sblgnt.py
    ./scripts/eprouver-les-sources.py

Les trois premiers écrivent chacun leur part de `MANIFEST.json` **sans toucher à
celle de l'autre** — écrire le fichier en entier effacerait l'autre source sans
un mot, et un `sources/` amputé reste bien formé, donc invisible. Le troisième
refuse un `sources/` qui s'écarterait de ce qu'il déclare.

Le pont de la Septante se refait à part, et il demande le clone de MACULA :

    GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/Clear-Bible/macula-hebrew
    ./scripts/importer-le-pont-septante.py --macula <clone> --sortie sources/pont-septante
    ./scripts/etablir-le-pont-septante.py --strong <strongsgreek.xml> --sortie <rapport.md>

`GIT_LFS_SKIP_SMUDGE` évite les 84 Mo de la TSV, que l'import n'emploie pas :
il lit les XML `WLC/lowfat/`, qui sont des fichiers ordinaires.
