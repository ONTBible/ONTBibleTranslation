# L'état des sources — ce qui est acquis, ce qui manque, à qui écrire

*Relevé du 10 septembre 2026, par six recherches menées en parallèle. Chaque
ligne porte sa source ; ce qui n'a pas été lu en source primaire est dit tel.*

> **Pourquoi ce fichier existe.** Ces résultats n'existaient que dans la
> conversation d'une session. Un redémarrage de la machine a purgé `/tmp` le
> matin même et emporté tous les fichiers de travail — ==une recherche qui vit
> dans un contexte de session est une recherche qu'on refera==. Elle est ici.

---

## Ce qui est acquis, et que personne n'avait relevé

### Toledot Adam ve-Chavah et Chazon Barukh — permission accordée

**Ken Penner a répondu le 2 septembre 2026** à la demande ouverte chez *Online
Critical Pseudepigrapha* (issue #34), et le dépôt a été re-licencié.

> *« You are very welcome to use and display both `AdamEve.xml` (Life of Adam
> and Eve) and `2Bar-Syr.xml` (2 Baruch) alongside your French translation in
> the ONT application and website. **We gladly grant permission** for this
> use. »*
>
> *« The text editions and TEI XML files in `static/docs/` are explicitly
> released under **Creative Commons Attribution 4.0 International**. »*

`github.com/OnlineCriticalPseudepigrapha/Online-Critical-Pseudepigrapha`

- **`AdamEve.xml`** — 387 Ko. Grec de l'*Apocalypse de Moïse* d'après Tischendorf
  1866 (domaine public), plus deux latins (Meyer, Mozley). ==Travailler sur les
  couches en langue source== : les couches anglaise et française ont été versées
  en masse et ne sont pas relues.
- **`2Bar-Syr.xml`** — 1,27 Mo, 40 655 caractères syriaques, apparat calé sur
  Dedering, Ceriani, Violet, Charles.

**Réserve** : la version syriaque de `2Bar.xml` nomme Daniel M. Gurtner, dont
l'édition critique de 2009 est sous copyright. La permission de Penner couvre le
fichier tel qu'il est publié ; c'est lui l'autorité éditoriale.

**Rien à écrire. Archiver les deux permaliens de l'issue** — c'est la pièce, au
même titre que le courriel de Ran HaCohen.

### Yovelim — le guèze existe, et c'est Ran HaCohen qui l'a transcrit

`BetaMasaheft/Works/1001-2000/LIT1697Jubilees.xml` — 716 Ko, **188 171
caractères de guèze**, TEI, 50 chapitres, un `<l>` par verset.

Licence lue dans l'en-tête TEI :

> `<licence target="http://creativecommons.org/licenses/by-sa/4.0/">` … *« The
> text transcription by **Ran HaCohen** … has also been made available under the
> same licence »*, et dans l'`editionStmt` : *« OCTATEUCHUS © Digitalizavit Ran
> HaCohen »*.

**C'est la personne qui a déjà donné son accord écrit le 1er septembre 2026**
pour le guèze de *Chanokh*, à condition d'être tenue informée du projet. ==Le bon
geste est de relancer ce fil==, pas d'ouvrir une démarche neuve.

**Une question à lui poser franchement** : sa transcription est faite de
l'édition **VanderKam 1989** (CSCO), qui est sous copyright, et Beta maṣāḥǝft la
publie en CC BY-SA. C'est la même tension qu'ailleurs — la poser plutôt que la
supposer. ==Et c'est aussi la réponse au silence de VanderKam.==

**Un piège** : `LPettay/ethiopian-bible` sert le même guèze en JSON par chapitre,
très commode, et ==n'a aucune licence== (`"license": null`). Prendre la source,
jamais le dérivé.

### Sefar Gibbaraya et Tsavaʾat Levi — un seul dépôt, une seule lettre

`github.com/ETCBC/dss` — les rouleaux de la mer Morte au format Text-Fabric,
d'après les données de **Martin Abegg**. Licence lue dans les données mêmes
(`tf/2.0/otype.tf`) :

    @license=Creative Commons Attribution-NonCommercial 4.0 International License
    @createdBy=Martin G. Abegg, Jr., James E. Bowley, and Edward M. Cook

Tous les témoins y sont, vérifiés dans `scroll.tf` (997 rouleaux) :

    Livre des Géants   1Q23 · 1Q24 · 2Q26 · 4Q203 · 4Q530 · 4Q531 · 4Q532 · 4Q533 · 6Q8
    Lévi araméen       1Q21 · 4Q213 · 4Q213a · 4Q213b · 4Q214 · 4Q214a · 4Q214b

Texte consonantique, langue étiquetée (`lang=a` pour l'araméen), lacunes et
reconstructions marquées, morphologie complète.

**La clause NC est à négocier**, et ce projet l'a déjà fait deux fois. Écrire à
Willem van Peursen, directeur de l'ETCBC — adresse lue sous forme obfusquée sur
`etcbc.nl/staff/`. Mentionner Jarod Jacobs et Dirk Roorda, qui ont mené la
conversion. ==La levée dépend en dernier ressort de Martin Abegg== (émérite,
Trinity Western University) : passer par l'ETCBC plutôt que de reconstruire une
adresse.

**Un avertissement d'usage** : ne pas lire ces fichiers avec un parseur
improvisé. Un extrait annoncé `4Q530` a rendu du Targoum de Job. Charger avec la
bibliothèque `text-fabric`, qui fait l'alignement rouleau → signes correctement.

### Chazon Avraham — un slavon numérique existe

Kamchatnov & Milkov, « Апокриф "Откровение Авраама" в составе Палеи Толковой »,
*Палеоросия* n° 3 (15), 2021, p. 227-265. DOI `10.47132/2618-9674_2021_3_227`.

Recension de la *Palaia Tolkovaia* d'après ГИМ, Барс. № 620 (XVe s.), avec
apparat sur six autres manuscrits, traduction russe et commentaire. ==Il complète
Box (Codex Sylvester) et Bonwetsch — il ne les remplace pas.==

**La couche texte du PDF est réelle**, vérifiée par extraction : le slavon sort
en cyrillique Unicode. Les lettres suscrites et les titla sortent en substituts
latins (`a`, `N`, `=`) — un encodage de police propriétaire qui demande une table
de correspondance. ==C'est mécanique, ce n'est pas de l'OCR.==

**Réserve de licence sérieuse** : CyberLeninka affiche un badge « CC BY » ==sans
numéro de version==, et le site de l'éditeur porte « Все права защищены ».
Contradiction non résolue — à confirmer par écrit auprès de la rédaction des
revues de la SPbDA.

**Rien ailleurs** : le Corpus Cyrillo-Methodianum n'a que sept textes canoniques,
TOROT et PROIEL n'ont pas l'*Apocalypse*, Zenodo et GitHub sont vides.

---

## Ce qui reste fermé, et pourquoi

### CATSS — l'alignement de référence, sous contrat

Les 46 fichiers `.par` de l'alignement mot à mot MT ↔ LXX répondent librement en
HTTP. **Ils sont pourtant inutilisables ici**, et c'est la déclaration
d'utilisateur qui le dit :

> *(1) Not to use or make available these materials for **commercial purposes**
> without first obtaining the written consent of the owners/encoders;*
>
> *(3) To control access to these materials and **require any other party to whom
> the recipient supplies any portion of this material** to observe these
> conditions and **to register a signed USER AGREEMENT form with CCAT**;*

La clause (3) est ==virale== : chaque destinataire doit s'enregistrer. Une app
distribuée ne peut pas tenir ça. Deux projets qui redistribuent CATSS l'ont
conclu indépendamment.

**Et une seconde couche de droits dessous** : l'hébreu vient de la BHS
(Deutsche Bibelgesellschaft), le grec de Rahlfs 1935 — *« with further
verification and adaptation towards conformity with the individual Göttingen
editions »*. ==Ce n'est donc ni Rahlfs ni Göttingen : c'est un état mouvant.==

**Contacts, si l'on décide d'écrire** : Robert Kraft, seul contact affiché par le
CATSS, ==est mort le 15 septembre 2023== et la page n'a jamais été mise à jour.
Les responsables vivants sont **Emanuel Tov** (Hebrew University, émérite), qui a
dirigé l'équipe qui a produit l'alignement, et **Frank Polak** (Tel Aviv,
émérite), qui a signé la révision de 2008. Leur README précise *« no fees are
involved »*.

### Rahlfs — un arrêt de la CJUE a déplacé la question

**CJUE, 19 mars 2026, aff. C-649/23**, ECLI:EU:C:2026:213. L'affaire porte sur
une édition critique de Cantemir, non sur la Bible. Le dispositif :

> *« the critical edition of a work which is in the public domain … **may be
> regarded as a work protected by copyright** … provided that it is an
> intellectual creation reflecting the author's personality »*

Ce que ça change : la question n'est plus *« le §70 allemand a-t-il expiré en
1960 ? »* — 25 ans après parution — mais *« l'édition de Rahlfs est-elle une
œuvre ? »*, ce qui ouvre **70 ans post mortem**.

Et son **§64** refuse de séparer le texte de l'apparat : ==la stratégie « je ne
prends que le texte » tombe==.

| couche | Allemagne / France | États-Unis |
|---|---|---|
| Rahlfs 1935 — texte, apparat, introduction | expiré **fin 2005** *si* œuvre ; jamais protégé sinon | **fin 2030** *si* restauré par l'URAA ; libre sinon |
| Rahlfs-Hanhart 2006 | Hanhart † **11 juillet 2025** → **fin 2095** | protégé |

==Le chiffre le plus lourd du dossier est la date de mort de Hanhart.==

**Ce qui reste vrai et sert** : la Deutsche Bibelgesellschaft ne revendique
publiquement que l'édition de **2006** — aucune de ses pages ne mentionne 1935.
Et le **§68** de l'arrêt laisse la porte ouverte : reconnaître un droit sur une
édition critique *« does not bring that work into the private domain »*.

**Et un point qui concerne directement ce projet** : le droit d'auteur interdit
la reproduction, **pas la consultation**. Se servir de Rahlfs comme témoin pour
établir une glose n'est pas reproduire son texte dans l'app.

*(Ces analyses ne sont pas un avis juridique. La branche URAA n'a été vérifiée
par aucune source : c'est un raisonnement appliqué à un texte de loi lu. Une
distribution aux États-Unis en dépend et mérite un avis de juriste américain.)*

---

## La morphologie de la Septante — le trou s'est refermé à moitié

**Une analyse complète existe depuis le 1er juin 2026** :
`github.com/OpenScriptorium/lxx-morph`, **CC BY 4.0**, 59 livres, la Septante
entière. Chaque mot porte son lemme, son analyse, sa bande de confiance et la
justification. ==L'annotation ne dérive pas de CATSS== — elle a été engendrée par
Perseus Morpheus puis relue.

**Mais son texte grec remonte à CATSS**, et la contradiction est écrite dans les
deux dépôts :

> **lxx-morph** : *« derived from the Eliran Wong **public-domain** digital
> edition of Rahlfs (1935) »*
>
> **eliranwong/LXX-Rahlfs-1935** : *« licensed under CC **Attribution-
> NonCommercial**-ShareAlike 4.0 […] A derivative work based on CCAT data »*

Aucune base juridique n'est citée. Et l'auteur déclare lui-même :

> *« the work of a **self-taught student of Koine, not a trained classicist** …
> **Verify against an authoritative edition before citing.** »*

**La seule chaîne irréprochable** : `UD_Ancient_Greek-PTNK`, CC BY-SA 4.0,
morphologie ==manuelle==, texte du **Codex Alexandrinus** — donc hors de toute la
question Rahlfs/CATSS. Couverture : ==Genèse et Ruth==, soit 7 % de la Septante —
et la totalité de ce que le vault a écrit dans la Torah.

**Le projet de James Tauber n'a jamais abouti** : dormant depuis 2017, et sa
méthode se calait de toute façon sur CATSS. **STEPBible TAGOT n'est pas sorti**,
et son README annonce une morphologie *« based on CCAT »*.

---

## Ce qui n'existe pas, et qu'il ne sert à rien de chercher

**Hatch & Redpath** — la concordance grec → hébreu de la Septante, 1897-1906,
domaine public. Les trois volumes sont sur archive.org, et ==l'OCR est
inutilisable== : zéro caractère hébreu dans les trois, mesuré. Le volume 2 rend
même le grec en lettres latines. Lisible par un humain, pas par une machine.
Aucune transcription sur GitHub.

Même constat pour **dos Santos**, *An Expanded Hebrew Index* — l'inverse exact du
pont, OCR également nul, et sous CC BY-NC-ND.

**Aucune annotation du Nouveau Testament grec pour ses tournures sémitiques n'a
jamais été publiée.** Zéro sur Zenodo, zéro sur HuggingFace, zéro sur GitHub. Les
travaux du domaine — Wilcox, Maloney, Black, Casey — restent des livres.
==C'est une absence documentée, pas une recherche incomplète.==

**Muraoka** et **LEH** sont deux livres en vente, sans édition libre. Écartés
sans regret possible.

---

## Les citations de l'AT dans le NT — prêtes à importer

`ubsicap/ubs-open-license`, fichier `parallel passages/ParallelPassages.xml`,
**CC BY-SA 4.0**, 336 250 octets, figé depuis juillet 2023.

**249 passages AT → NT**, alignés mot à mot. Ni namespace XML, ni entité, ASCII
pur hors BOM.

Trois choses que la documentation ne dit pas et qui décident de l'import :

- ==les valeurs vont de 0 à 5, pas de 0 à 2==. 3, 4 et 5 valent 0, 1 et 2 plus un
  saut de ligne d'affichage. **6,9 % des positions** en portent ; un parseur qui
  ne fait pas `valeur % 3` lit faux sans lever d'erreur ;
- ==les références sont massorétiques, les chiffres comptent des mots grecs==.
  Dans un passage mixte, `PSA 110:1` est bien le Ps 110 hébreu — mais sa chaîne
  compte les mots de la Septante. Les deux systèmes coexistent dans le même
  élément ;
- ==la longueur d'une chaîne ne garantit pas le compte de mots de votre texte==.
  Mesuré : 77,7 % de concordance sur l'AT contre le WLC, 89,7 % sur Matthieu. Il
  faut valider verset par verset et mettre les écarts en quarantaine, ==jamais
  indexer positionnellement à l'aveugle==.

Il n'existe **aucun attribut** pour distinguer les passages AT→NT : la marque est
le mélange des noms d'attributs `HEB` et `GRK` à l'intérieur d'un même
`<Passage>`. Sigles de livres : **USFM 3.0**, pas OSIS — `EZK` et non `Ezek`,
`JOL` et non `Joel`, `PHP` et non `Phil`, et `JUD` est Jude quand `JDG` est
*Shoftim*.

Attribution demandée : *UBS Parallel Passage Database, © 2023 United Bible
Societies*.

---

## Récapitulatif — à qui écrire, dans quel ordre

| livre | ressource | licence | action |
|---|---|---|---|
| Toledot | OCP `AdamEve.xml` | **CC BY 4.0 — accordé** | rien |
| Chazon Barukh | OCP `2Bar-Syr.xml` | **CC BY 4.0 — accordé** | rien |
| Yovelim | BM `LIT1697Jubilees.xml` | CC BY-SA 4.0 | **Ran HaCohen**, relance du fil |
| Sefar Gibbaraya | `ETCBC/dss` | CC BY-NC 4.0 | van Peursen → Abegg |
| Tsavaʾat Levi | `ETCBC/dss` | CC BY-NC 4.0 | ==la même lettre== |
| Chazon Avraham | Paleorosia 2021 | badge « CC BY » à confirmer | rédaction SPbDA |

**Deux livres sont acquis sans rien écrire. Une seule lettre en couvre deux
autres.**

Restent hors de portée, et il faut le savoir : l'arménien et le géorgien de
*Toledot* (Anderson & Stone, papier), et la Geniza du Caire pour *Tsavaʾat Levi*
(Cambridge sert des images, pas des transcriptions).
