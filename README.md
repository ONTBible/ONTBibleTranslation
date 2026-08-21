# La Bible ONT — le vault

La traduction elle-même. **Ontologie Nouvelle Traduction** : une restitution
française du corpus hébreu et araméen antique, fondée sur l'ontologie hébraïque
antique fonctionnelle.

Le principe tient en une phrase, et tout le reste en découle : **le cosmos
hébreu n'est pas une usine, c'est un Temple.** Une chose n'existe pas parce
qu'elle a une substance, mais parce qu'elle a une fonction assignée, un nom, un
rôle dans un système ordonné. *Bara* ne veut pas dire fabriquer.

Traduction et direction : **Gloire Bikouta**, avec Claude comme co-traducteur.

---

## Ce dépôt n'est pas de la documentation, c'est une **source**

Un vault Obsidian, et en même temps l'entrée d'une chaîne de construction. Le
pipeline de `../ONTBibleApp` le lit à chaque build et en tire les données que
l'app iOS et le site publient.

```
ONTBibleTranslation/     ce dépôt — le texte, les conventions, le glossaire
        │
        ▼
ONTBibleApp/pipeline     lit le vault et le CLAUDE.md → dist/*.json
        │
        ├──▶  l'app iOS   (le corpus est embarqué au build)
        └──▶  le site     (ONTBibleWebapp, embarqué à la compilation)
```

Conséquence directe : **une décision terminologique prise ici arrive dans la
liseuse au prochain build.** Elle n'est recopiée nulle part.

Et conséquence inverse, plus exigeante : une convention mal tenue dans un
fichier n'est pas une coquille de mise en forme, c'est une donnée fausse chez
le lecteur. D'où le contrôle du pipeline décrit plus bas.

---

## `CLAUDE.md` est le document de référence, et il est lu par une machine

85 Ko, treize sections. C'est à la fois le manuel du traducteur et un fichier
que le pipeline analyse :

| section | ce qu'elle fixe | ce que le pipeline en tire |
|---|---|---|
| §1 | ce qu'est l'ONT, les quatre modes, le périmètre du corpus | — |
| §2 | les conventions typographiques — **immuables** | la grammaire du parseur |
| §2.5 | les formes balisées des intraduisibles, et leur premier emploi | les entrées du glossaire |
| §2.6 | les noms des livres | les répertoires de noms |
| §3 | la terminologie fixée — hébreu, rendu ONT, champ sémantique | le contenu des fiches |
| §4 | les principes de traduction | — |
| §7 / §8 | ce qui exige l'auteur, ce qui se traite en autonomie | — |
| §10 | ce que l'ONT **n'est pas** — cinq lignes | la page la plus forte du site |
| §12 | le flux de validation, et les Fondations verrouillées | les deux arbres lus |
| §13 | les chantiers ouverts, relevés par le pipeline | — |

Le §13 est écrit **par la construction, pour l'auteur** : le pipeline contrôle
à chaque passage que tout terme balisé a bien son entrée, et dépose son relevé
complet dans `dist/report.md` du dépôt voisin.

---

## Les trois niveaux, et le quatrième marquage

C'est la raison d'être du projet, et la raison pour laquelle le texte s'écrit
dans ce dialecte de markdown et pas dans un autre. Un parseur générique
écraserait ces niveaux en gras et italiques indifférenciés.

| dans le `.md` | niveau | ce que ça veut dire |
|---|---|---|
| texte ordinaire | 1 | le corps de la traduction — ce que l'hébreu dit |
| `**chesed**` | 1 | **intraduisible** — le mot n'est pas traduit, il est posé |
| `==« Jour »==` | 1 | **accentuation** — on insiste, on ne promet rien |
| `*[glose]*` | 2 | l'implicite hébreu rendu explicite — la voix du projet |
| `(*chasdo* / חַסְדּוֹ)` | 3 | translittération **et** hébreu, toujours les deux |

**`**…**` est réservé, strictement.** Un gras posé pour insister déclare le mot
intraduisible : dans l'app il s'affiche en or et devient touchable, et le
lecteur ouvre une fiche vide. Sur la maquette Affinity, il déclenche à tort le
style « Transliteration ». C'est pour ça que `==…==` existe (§2.5 bis) —
l'or promet une fiche et la tient, le bordeaux marque sans rien promettre.

Onze balises ont déjà été converties de l'un vers l'autre le 12 août 2026
(§13.3) : ne pas les refaire.

---

## L'arborescence porte l'ordre canonique

```
locked/ · brouillons/ · in-writing/
   └── 1. kenesset (le Rassemblement)     ou  2. berit-hadashah
         └── 1. torah (la Fondation)      2. neviim · 3. ketouvim · 4. nistarot
               └── 01. bereshit (Genèse)
                     └── bereshit-1.md
```

Les préfixes numériques ne sont pas cosmétiques : **l'ordre canonique n'est
écrit nulle part ailleurs.** Le pipeline le lit dans les noms de dossiers, donc
ajouter un slot suffit à le voir apparaître dans l'app et sur le site. L'IDE
trie alphabétiquement ; les préfixes forcent l'ordre fonctionnel. Le tableau
complet des soixante-dix livres vit dans **`corpus-order.md`**.

Quatre modes, et ce ne sont pas des divisions canoniques mais des modes
d'engagement avec le réel : **Torah** institue, **Nevi'im** lit l'alliance dans
l'histoire, **Ketouvim** habite, **Nistarot** traverse l'architecture voilée.
Leurs initiales font *Kenesset* (כְּנֶסֶת), le nom du corpus dans l'ONT.

---

## Trois dossiers, un seul fait référence

| dossier | ce qu'il contient | distribué ? |
|---|---|---|
| `locked/` | les unités verrouillées — **la référence absolue** | oui |
| `brouillons/` | rédigé, en attente de la relecture de l'auteur | non |
| `in-writing/` | l'arborescence vide des 70 slots — le squelette | non |

`brouillons/` **miroite exactement** l'arborescence de `locked/` : valider, c'est
déplacer un fichier vers le chemin identique et passer son pied de « à valider »
à « Version X — verrouillée ». Rien à renommer, rien à déduire.

Le pipeline lit quand même les brouillons — sinon le rapport ne pourrait pas
dire où en est le corpus, et la liseuse d'atelier n'aurait rien à montrer. Il
les marque : **`brouillons/` l'emporte sur `locked/` pour une même unité**, et
chaque unité porte son `status`. La distribution publique ne doit embarquer que
les unités verrouillées.

`context/` ne voyage pas non plus.

---

## Le reste de la racine

| | |
|---|---|
| `corpus-order.md` | la numérotation globale 01-70, l'ordre par mode |
| `paratexte.md` | préface, note linguistique, glossaire imprimé — à construire |
| `context/` | l'auteur, les notes de travail d'un livre |
| `utilities/` | les fontes hébraïques |
| `sessions/` | les transcriptions de sessions de traduction |

**La maquette Affinity n'est pas dans le dépôt.** Le document de composition de
l'édition papier — 20,3 × 19,3 cm, double page, double colonne — vit sur le
disque de l'auteur, sous `af/`, ignoré par git. Douze méga de binaires opaques
que git ne sait ni différencier ni fusionner n'avaient rien à faire dans un
dépôt qui porte du texte : la mise en page est un aval du texte, pas une source.

**Les fontes sont versionnées, sauf une.** Ezra SIL, Frank Ruhl Libre et Taamey
Frank CLM sont sous licence libre et vivent dans le dépôt — c'est ce qui permet
à quiconque le clone de composer le texte tel qu'il est écrit. **SBL Hebrew est
sous EULA propriétaire : la committer serait la redistribuer.** Elle reste sur
le disque pour Affinity et ne quitte pas la machine ; `.gitignore` la retient.

Ezra SIL est la seule qui positionne correctement niqqud **et** te'amim
ensemble — c'est pour ça qu'elle est aussi la fonte hébraïque de l'app et du
site.

Les réglages du vault (`.obsidian/`) sont versionnés ; l'état de l'espace de
travail, non — il change à chaque ouverture de panneau.

---

## L'état du corpus

| | |
|---|---|
| Slots | **3 rédigés sur 70** — *Bereshit*, *Toledot Adam ve-Chavah*, *Sefar Gibbaraya* |
| Unités | 39 chapitres + 2 feuilles d'introduction — **781 versets** |
| Glossaire | **105 entrées**, dont 47 intraduisibles balisés |
| Index | 2 033 occurrences |

Relevé au dernier build du pipeline, jamais recopié à la main.

Ce que la ventilation des occurrences raconte : **mishpat** paraît 14 fois dans
le corps contre 40 dans les gloses — un terme encore en cours de fondation.
**gibbaraya** est à 47 contre 6 : acquis.

---

## Les chantiers ouverts (§13)

Neuf formes sont balisées `**…**` sans entrée de glossaire. Chacune demande une
décision de traducteur, pas une correction : **A** — c'est un vrai
intraduisible, on lui écrit son entrée au §2.5 et au §3 ; **B** — ce n'en est
pas un, il passe en `==…==`.

`tsadiqim` est le plus rentable : neuf occurrences, et le terme est déjà au
glossaire au singulier.

S'y ajoutent vingt-deux marqueurs `**` ouverts sans être refermés, tous dans les
pieds de page de *Bereshit* 15 à 19. Le pipeline les recolle en silence — un
`**…**` ne peut pas contenir une phrase entière — mais le rendu Affinity et
celui de l'app peuvent diverger tant que la coquille est là.

---

## Les dépôts voisins

| | |
|---|---|
| [`ONTBibleApp`](https://github.com/ONTBible/ONTBibleApp) | le pipeline, l'app iOS, le backend |
| [`ONTBibleWebapp`](https://github.com/ONTBible/ONTBibleWebapp) | `ontbible.com` |

Les trois portent le même ruleset : `main` protégée, passage par pull request,
**signatures exigées**, suppression de la branche après fusion.
