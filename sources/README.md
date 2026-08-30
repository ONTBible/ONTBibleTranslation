# `sources/` — les textes en langue source

Ce que le lecteur voit quand il appuie longuement sur un verset : le texte
**dans sa langue**, hébreu ou grec, avec son analyse morphologique.

Rien ici n'est de l'ONT. Ce sont trois éditions critiques extérieures,
reprises telles quelles, et c'est tout leur intérêt : la couche fonctionnelle
de l'ONT se lit **contre** un texte qu'elle n'a pas choisi.

---

## Les trois témoins

| dossier | témoin | texte | analyse |
|---|---|---|---|
| `he-wlc/` | Westminster Leningrad Codex | domaine public | **OSHB** — CC BY 4.0 |
| `grc-sblgnt/` | SBL Greek New Testament | CC BY 4.0 | **MorphGNT** — CC BY-SA 3.0 |
| `grc-byz/` | Robinson-Pierpont, RP2018 | domaine public | domaine public |

Les deux témoins grecs sont **côte à côte, sans marquage des divergences** —
décision de l'auteur du 30 août 2026. L'un est éclectique, l'autre byzantin ;
l'ONT ne tranche pas entre eux et ne les aligne pas mot à mot.

`MANIFEST.json` porte, par source : la licence, l'attribution exacte, le
commit amont d'où l'import a été tiré, et le compte de chaque livre.

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

## Ce que cette couche ne couvre pas

**62 livres ONT sur 70.** Les huit qui restent sont exactement le corpus
étendu — ceux qui ne nous sont pas parvenus en hébreu ni en grec :

    06  Yovelim                    38  1 Chanokh
    36  Toledot Adam ve-Chavah     39  Chazon Avraham
    37  Sefar Gibbaraya            40  Tsava'at Levi
                                   42  Chazon Ezra
                                   43  Chazon Barukh

Ils survivent en guèze, en slavon, en syriaque, ou par fragments araméens de
Qumrân — et aucune de ces traditions n'est dans les trois témoins importés
ici. ==Un appui long sur un verset du *Chazon Avraham* n'aura donc rien à
montrer==, et c'est précisément le livre en cours d'écriture.

Ce n'est pas un manque de l'import : c'est l'état du corpus. Le dire ici vaut
mieux que de le laisser découvrir à l'usage.

## Refaire l'import

    ./scripts/importer-les-textes-sources.py --depots <dossier> --cloner
    ./scripts/eprouver-les-sources.py

Le premier cloue le commit amont dans `MANIFEST.json` ; le second refuse un
`sources/` qui s'écarterait de ce qu'il déclare.
