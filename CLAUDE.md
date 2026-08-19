# ONT — ONTOLOGIE NOUVELLE TRADUCTION
## DOCUMENT DE RÉFÉRENCE COMPLET POUR LA TRADUCTION AUTONOME

> ## À faire à la fin de **chaque** travail, sans exception
>
> Ce dépôt est l'un des **trois** d'un même projet — avec `ONTBibleApp` (le
> pipeline, la liseuse iOS, le backend) et `ONTBibleWebapp` (`ontbible.com`).
> Ils sont côte à côte : `~/ONTBible/<dépôt>`.
>
> Avant de dire qu'un travail est fini, **lire [`SYNCHRONISATION.md`](SYNCHRONISATION.md)
> et appliquer sa règle** : demander ce que ce travail change pour les deux
> autres dépôts, le porter chez eux dans la même session, et inscrire la ligne
> au journal.
>
> Ce dépôt est **la source de tout le reste**. Le pipeline de `ONTBibleApp` lit
> le vault et en écrit `dist/`, que la liseuse embarque et que le site compile.
> Renommer un livre, changer une structure de fichier ou une convention de
> balisage se répercute donc jusqu'à l'App Store — et rien ici ne le signale.

---

## 1. QU'EST-CE QUE L'ONT ?

L'ONT est une traduction et reconstruction françaises du **corpus hébreu et araméen antique** fondées sur **l'ontologie hébraïque antique fonctionnelle**. Elle a été fondée et est dirigée par son auteur — **Sha'eliel** (שָׁאַל + אֵל : celui qui interroge Elohim jusqu'à ce que le réel rende ce qu'il cache) — en collaboration avec Claude comme co-traducteur. Voir `context/auteur.md`.

**Le principe fondamental :** Dans le monde hébreu antique, une chose n'existe pas parce qu'elle a une substance matérielle, mais parce qu'elle a une **fonction assignée, un nom, un rôle dans un système ordonné**. Créer ne signifie pas fabriquer de la matière — cela signifie ordonner, nommer, attribuer un rôle, inaugurer un espace fonctionnel. Le cosmos hébreu n'est pas une usine, c'est un Temple.

**Architecture du corpus — la Kenesset (כְּנֶסֶת) :**

Le corpus hébreu et araméen de l'ONT est nommé **Kenesset** (כְּנֶסֶת) — "le rassemblement, l'assemblée." Acronyme des quatre modes : **כ** (Ketouvim) + **נ** (Nevi'im) + **ס** (Nistarot — racine *satar* סָתַר) + **ת** (Torah) = כְּנֶסֶת. Remplace "Tanakh" comme nom du corpus dans l'ONT : Tanakh désignait les trois modes canoniques (Torah/Nevi'im/Ketouvim) ; Kenesset désigne les quatre modes fonctionnels incluant les Nistarot. Distinct de la *Berit Hadashah* qui est son propre corpus.

Le corpus est structuré en quatre catégories fonctionnelles. Ce ne sont pas des divisions canoniques — ce sont des modes distincts d'engagement avec le réel. Le critère est ontologique : si la distinction fonctionnelle est réelle, elle mérite un nom (*qara*).

| Catégorie | Mode ontologique | Fonction |
|---|---|---|
| **Torah** | *Institution* | La Torah constitue le réel — *bara*, *qara*, *natan*. Le cosmos passe du *tohu vavohu* à l'ordre fonctionnel. La Torah est l'acte par lequel le réel devient réel. |
| **Nevi'im** | *Lecture dans l'histoire* | Le navi lit l'alliance dans le temps visible et prononce le *mishpat* — discernement de l'alignement ou désalignement covenantal. Problème toujours national : Israël ↔ alliance ↔ terre ↔ roi ↔ Temple. |
| **Ketouvim** | *Habitation intérieure* | Là où le cosmos constitué (Torah) et lu (Nevi'im) rencontre l'être humain dans son expérience concrète. Job souffre, les Tehilim crient, Qohelet interroge, Ruth agit. Mode d'intériorité et de réponse vécue. |
| **Nistarot** | *Traversée architecturale* | De *satar* (סָתַר) : structurellement voilé. *Devarim* 29:28 : *hanistarot laYHWH Eloheinu* — les choses cachées appartiennent à YHWH. Les Nistarot révèlent les structures invisibles derrière l'histoire : hiérarchies célestes, conseil divin, temps comme structure cosmique, puissances derrière les empires. Mode vertical — l'architecture du réel que le regard ordinaire ne traverse pas. |

**Textes-charnières Nevi'im / Nistarot :** Yehezqel (merkavah ch. 1, Temple cosmique ch. 40-48), Zekharyah 1-8 (visions nocturnes avec médiateur angélique), Yeshayahu 24-27 (jugement cosmique), Daniel 7-12 (visions architecturales, *qetz*). Ces textes restent dans les Nevi'im — ils sont des portes, pas des résidents des Nistarot.

**Nistarot — jamais "Giluyim"** : *Giluy* / *galah* (גָּלָה) est un calque rabbinique tardif du grec *apokalupsis* — rejeté. Le terme natif est *nistarot* (Devarim 29:28), utilisé par la communauté de Qumrân elle-même pour désigner les réalités voilées révélées aux *maskilim*.

**Périmètre du corpus :** L'ONT ne se limite pas à la Bible canonique — le "canon" est une construction tardive (IVe siècle et après) qui n'existait pas à l'époque de la rédaction des textes. Le projet travaille sur l'ensemble de la bibliothèque d'un Juif lettré du Second Temple : textes canoniques ET pseudépigraphiques. **Critère d'inclusion :** tout texte en hébreu ou araméen antique qui illumine le cosmos hébreu depuis l'intérieur. **Critère d'exclusion :** tout texte qui a absorbé des catégories hellénistiques (grecques), même s'il est d'auteur juif — Philon d'Alexandrie, *Sagesse de Salomon*, 4 Maccabées. Le filtre n'est pas canonique, il est ontologique : est-ce que le texte pense en hébreu ou en grec ? La distinction canon/apocryphe n'existe pas dans l'ONT.

**Répartition du corpus étendu dans les quatre catégories :**

*Ketouvim* (mode d'habitation intérieure) : *Tehilim*, *Mishlei*, *Iyov*, *Shir Hashirim*, *Ruth*, *Qohelet*, *Esther*, *Ezra-Nehemyah*, *Divrei Hayamim*, *Toledot Adam ve-Chavah* (Vie d'Adam et Ève — mode narratif/expérientiel dominant ; cas limite à réévaluer), *Sefar Gibbaraya* (Livre des Géants — les *gibbaraya* pris dans le drame cosmique cherchant à interpréter leurs rêves ; même structure que Iyov : mode expérientiel, pas architectural).

*Torah* (mode d'institution) — corpus étendu : *Yovelim* (Jubilés) — retelling normatif et législatif de Bereshit-Shemot ; les tablettes célestes et le médiateur angélique sont des dispositifs d'autorité Torah-niveau, non un contenu de traversée architecturale. Yovelim institue et ordonne — il emprunte l'épistémologie Nistarot sans en être.

*Nistarot* (mode de traversée architecturale) : *Daniel*, *1 Khanokh*, *Chazon Avraham* (Apocalypse d'Abraham), *Chazon Ezra* (2 Ezra — ch. 3-14 uniquement ; ch. 1-2 et 15-16 sont des additions chrétiennes hellénisées exclues), *Chazon Barukh* (Apocalypse de Baruch — syriaque, original hébreu probable), *Tsava'at Lévi* (Testament de Lévi araméen de Qumrân — pas les Testaments des 12 Patriarches dans leur ensemble, trop christianisés).

**Terminologie ONT pour les textes de vision :** *chazon* (חָזוֹן — vision prophétique reçue, terme natif du Second Temple : Daniel 7:1, 8:1 ; titres de Yeshayahu, Ovadyah, Nahum, Havaquq) pour tous les textes de vision SAUF le *Machazeh Yohanan* qui garde *machazeh* (מַחֲזֵה) — décision délibérée pour créer l'écho avec *Bereshit* 15:1 (*bamachazeh*) : la vision inaugurale de la *berith* et la vision finale du cosmos racheté dans la même modalité. Ne pas utiliser *giluy* (hébreu rabbinique tardif, calque du grec *apokalypsis*) — le terme natif est *chazon*.

**Extension *Berit Hadashah* :** L'ONT inclut également la *Berit Hadashah* (בְּרִית חֲדָשָׁה) — titre tiré de *Yirmeyahu* 31:31, non pas le "Nouveau Testament" de la tradition latine tardive. Le même critère ontologique s'applique : lus à travers le prisme de l'ontologie hébraïque antique fonctionnelle, ces textes font apparaître la même structure cosmique hébraïque — *davar* performatif, *berith*, *tsedaqah*, *ruach*, *kavod*.

**Structure fonctionnelle de la *Berit Hadashah* — quatre modes parallèles à la Kenesset :**

| Mode | Corpus *Berit Hadashah* | Fonction parallèle |
|---|---|---|
| **Besorot** (la Fondation — Évangiles) | **Besorot** (בְּשׂוֹרוֹת) — *besorah* : annonce royale d'un acte accompli. Subdivisées en *Eduyot* (*Marqus*, *Matityahu*, *Luqas* — trois témoins au sens de *Devarim* 19:15) et *Bereshit ha-Yohanan* (séparée — *besorah* cosmique-inaugurale, écho de *Bereshit* 1) | Institue qui est Yeshua — fondation cosmique, *davar* inaugurale |
| **Nevi'im** | **Igerot** (אִגְּרוֹת) — lettres adressées, *devarim* fonctionnels | Confrontation covenantale depuis la position du *mishpat* — lecture de l'alignement/désalignement des communautés dans la *berith* |
| **Ketouvim** | **Gevurot ha-Neviim** (גְּבוּרוֹת הַנְּבִיאִים) — les *gevurot* de **YHWH** accomplies *à travers* ses *neviim* | Chronique narrative des actes de puissance de **YHWH** dans l'histoire — mode expérientiel et testimonial |
| **Nistarot** | **Machazeh Yohanan** (מַחֲזֵה יוֹחָנָן) — même terme qu'en *Bereshit* 15:1, dans la lignée de Yehezqel, Daniel et 1 Khanokh | Traversée architecturale — les structures invisibles derrière l'histoire, le cosmos racheté |

**Note terminologique — *navi* / *shaliach* : une seule réalité fonctionnelle.** Tout *navi* authentique est structurellement un *shaliach* et tout *shaliach* accomplit la fonction du *navi* — ils ne sont pas deux catégories analytiquement distinctes. La décomposition *navi* / *shaliach* / *evangeliste* / *pasteur* / *enseignant* (Éphésiens 4:11) est une décompression grecque d'une réalité hébraïque unifiée. Ne jamais traiter ces termes comme des fonctions mutuellement exclusives dans l'ONT.

**Pourquoi *Gevurot ha-Neviim* et non *Ma'asim HaShlichim*.** *Gevurot* (de *gavar* גָּבַר — être puissant, l'emporter) : les actes de puissance de **YHWH** — **YHWH** est le sujet grammatical, les *neviim* sont l'instrument. *Ma'asim* (de *asah* — faire) avec *ha-shlichim* (les envoyés) : les actes des *shlichim* — les humains comme sujets grammaticaux. La première formulation est hébraïque-fonctionnelle (*gevurot* appartient au vocabulaire de la puissance divine dans les *Tehilim* et les *Nevi'im*) ; la seconde importe la catégorie grecque de l'*apostolos* comme agent autonome.

**Référence académique principale :** John H. Walton — *The Lost World of Genesis One*. L'approche fonctionnelle-ontologique de l'hébreu biblique. Le paradigme du Temple cosmique proche-oriental.

---

## 2. CONVENTIONS TYPOGRAPHIQUES FIXES

Ces conventions sont **immuables** et s'appliquent à tout l'ONT sans exception.

### 2.1 Les trois niveaux du texte

**Niveau 1 — Corps de la traduction** : texte normal. Ce que l'hébreu dit directement.

**Niveau 2 — Gloses** : *[entre crochets en italique]*. Ce que le champ sémantique du mot hébreu porte implicitement pour le lecteur hébreu, rendu explicite pour le lecteur français. Ces gloses sont **indispensables** — elles explicitent l'implicite hébreu, elles n'inventent pas.

**Niveau 3 — Termes hébreux** : (translittération / הָעִבְרִית). Toujours les deux — la translittération ET l'hébreu, séparés par une barre oblique.

### 2.2 Numérotation des versets

Exposants : ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ¹⁰ ¹¹ ¹² ¹³ ¹⁴ ¹⁵ ¹⁶ ¹⁷ ¹⁸ ¹⁹ ²⁰ ²¹ ²² ²³ ²⁴ ²⁵ ²⁶ ²⁷ ²⁸ ²⁹ ³⁰ ³¹ ³² ³³ ³⁴

**Règle absolue — numérotation interne :** Chaque unité ONT (Bereshit N, Shemot N, etc.) repart toujours de ¹, quel que soit le numéro de verset biblique auquel elle commence. Si une unité ONT couvre Genèse 9:18-29, ses versets sont numérotés ¹ à ¹² — jamais ¹⁸ à ²⁹. De même, si un nouveau chapitre biblique commence au milieu d'une unité ONT, sa numérotation repart de ¹ à ce moment-là. Les numéros de versets bibliques ne sont jamais transposés dans l'ONT — ils figurent uniquement dans le sous-titre de référence *(Genèse / בְּרֵאשִׁית X:X-X)*.

### 2.3 Structure des chapitres

Les chapitres de l'ONT sont des **unités fonctionnelles** — un bloc se clôt quand une fonction cosmique est accomplie, pas quand un numéro de chapitre biblique change. Les numérotations de chapitres bibliques (introduites par le cardinal Stephen Langton au XIIIe siècle) sont des divisions administratives médiévales — souvent arbitraires. L'ONT les ignore au profit de la cohérence fonctionnelle.

**Exemple appliqué :** *Bereshit* 2:1-3 appartient fonctionnellement à la Fondation 1 (*Bereshit* 1) — c'est le couronnement du récit d'orchestration cosmique, pas le début d'un nouveau récit.

### 2.4 Formules fixes

**Formule d'accomplissement :** "Et il advint, et demeura conformément à ce qui avait été formulé" (*vayehi khen* / וַיְהִי-כֵן)

**Formule d'évaluation divine :** "Et Elohim examina et constata que c'était **tov**" (*vayar / ki tov* / וַיַּרְא כִּי-טוֹב)

**Formule du soir et du matin :** "Il y eut un soir (*erev* / עֶרֶב), puis un matin (*boqer* / בֹּקֶר) — ce fut le [N]e jour (*yom* / יוֹם)"

**Exception Jour Un :** "ce fut le Jour Un (*yom echad* / יוֹם אֶחָד)" — avec majuscules, car *echad* est le cardinal "un" pas l'ordinal "premier".

### 2.5 Marquage des termes intraduisibles — convention Affinity Publisher

**Règle absolue :** Tout terme intraduisible doit être entouré de `**...**` dans les fichiers .md. Ces marqueurs permettent à Affinity Publisher de détecter automatiquement ces termes et d'appliquer le style typographique "Transliteration" lors du copier-coller.

**Cette règle s'applique partout** : corps de la traduction (niveau 1), gloses (niveau 2), et notes de bas de section. Elle ne s'applique PAS à l'intérieur des translittérations de niveau 3 `(*terme* / הֵבְרִי)` — le terme y est déjà balisé.

**Liste complète des termes à baliser :**
- `**Elohim**` / `**elohim**`
- `**YHWH**`
- `**Ruach**` / `**ruach**`
- `**Nefesh**` / `**nefesh**`
- `**Neshamah**` / `**neshamah**`
- `**ishah**` / `**Ishah**` et formes dérivées : `**ishto**`, `**eshet**`, `**neshei**`
- `**ish**` / `**Ish**` et formes dérivées : `**anashim**` (pluriel absolu), `**anshei**` (pluriel construit) — **RÈGLE DE DÉDUCTION : toute forme dérivée d'un terme intraduisible est elle-même intraduisible. Ne jamais rendre *anashim* par "hommes".**
- `**Shem**` quand c'est le concept — lowercase `**shem**` toujours ; uppercase `**Shem**` quand précédé de "le / son / leur / du / des / ce / un" ou suivi d'une translittération minuscule
- `**kavod**` / `**Kavod**`
- `**Tahor**` / `**tahor**` / `**lo tahor**`
- `**Olah**` / `**olah**` / `**Olot**` / `**olot**`
- `**L'Être façonné du sol**` / `**l'Être façonné du sol**` (Bereshit 1-7 ; et tout récit en régime antédiluvien, avant le **mabbul** — ex. *Sefar Gibbaraya*). **Ne vise que le générique** *ha-adam* / *benei ha-adam* (l'humanité). Le **nom propre** Adam d'un individu (le personnage, ex. *Toledot Adam ve-Chavah*) reste un **nom propre** (§4.12) — ni traduit, ni balisé.
- `**adam**` (Bereshit 8 et suivants)
- `**mabbul**` — terme technique du déluge de Noach, utilisé sans traduction française dans le corps du texte à partir de Bereshit 8
- `**nacham**`. Premier emploi *Bereshit* 5:29.
- `**Adonai**` — s'écrit seul ou combiné : `**Adonai** **YHWH**`. Premier emploi *Bereshit* 15:2.
- `**El Elyon**` — deux mots, les deux en gras. Combiné : `**YHWH** **El Elyon**`. Premier emploi *Bereshit* 14.
- `**El Roï**` — deux mots, les deux en gras. Premier emploi *Bereshit* 16:13.
- `**Kohen**` / `**kohen**` / `**kohanim**` / `**kohen gadol**`. Premier emploi *Bereshit* 14:18.
- `**mal'akh**` / `**mal'akhim**` — combiné : `**mal'akh** **YHWH**`. Premier emploi *Bereshit* 16:7.
- `**shaliach**` / `**shlichim**`
- `**emunah**` / `**Emunah**` (nom) — forme verbale : `**emuna**` (sans h — délibéré, ne pas corriger). Premier emploi *Bereshit* 15:6.
- `**tsedaqah**`. Premier emploi *Bereshit* 15:6.
- `**tsadiq**`. Premier emploi *Bereshit* 6:9.
- `**rasha**` / `**resha'im**`. Premier emploi *Bereshit* 18:23.
- `**chesed**`. Premier emploi *Bereshit* 19:19 ; traitement définitif (plus ample) réservé à son locus central — *Shemot* 34:6-7 et *Ruth*.
- `**tov**` / `**tov me'od**`. Premier emploi *Bereshit* 1:4.
- `**ra**` / `**ra'at**` / `**ra'im**`. Premier emploi *Bereshit* 2:9.
- `**davar**` / `**devarim**` — combiné : "le **davar** de **YHWH**". Premier emploi *Bereshit* 11:1.
- `**'irin**` — araméen : les éveillés, les gardiens (עִירִין). Jamais "Veilleurs". Pluriel uniquement dans les textes araméens (*Sefar Gibbaraya*, 1 *Khanokh*).
- `**gibbaraya**` — araméen : les puissants, les démesurés (גבריא). Jamais "géants". Lien lexical avec les **gibborim** de *Bereshit* 6:4.
- `**El Shaddai**` — deux mots, les deux en gras. Même traitement qu'**El Elyon** et **El Roï**. Premier emploi *Bereshit* 17:1.
- `**milah**`. Premier emploi *Bereshit* 17.
- `**goy**` / `**goyim**` — forme construite : *goyei* → toujours **goyim**, jamais "nations"
- `**orlah**` / `**arel**`
- `**mishpat**` / `**mishpatim**`. Premier emploi *Bereshit* 18.
- `**shofet**` / `**shoftim**`. Premier emploi *Bereshit* 18:25.
- `**olam**` — intraduisible : de la racine "caché, dissimulé" — la limite temporelle que le regard humain ne peut pas discerner. **Règle de rendu en corps de texte : translittérer le construit en entier** — `**berith-olam**`, `**akhuzat-olam**`, `**ledorot-olam**`, `**ad-olam**`, `**le'olam**`, `**me'olam**`. Premier emploi *Bereshit* 3:22 (*vechai le'olam*).
- `**She'ol**` — intraduisible : le domaine des morts dans l'attente (שְׁאוֹל). Jamais « enfer » ni « séjour des morts » édulcoré. Le gras porte l'apostrophe de l'aleph, comme la translittération. Premier emploi *Toledot Adam ve-Chavah*.
- `**teshuvah**` — intraduisible : le retour, le réalignement vers la présence quittée (תְּשׁוּבָה). Jamais « repentance » ni « pénitence ». Premier emploi *Toledot Adam ve-Chavah*.
- `**ha-satan**` — intraduisible : l'accusateur, la *fonction* d'accusation du Conseil Divin (הַשָּׂטָן). L'article « ha- » marque la fonction — jamais un nom propre ni un dieu rival. Traitement définitif à *Iyov*. Premier emploi *Toledot Adam ve-Chavah*.
- `**tevilah**` — intraduisible : l'immersion de retour, passer par les eaux pour se retourner vers la source (טְבִילָה). Non « baptême » ni simple « bain ». Premier emploi *Toledot Adam ve-Chavah*.
- `**merkavah**` — intraduisible : le trône-char de **YHWH** **Elohim** vu en vision (מֶרְכָּבָה). Non « chariot » ordinaire. Premier emploi en corps de texte : *Toledot Adam ve-Chavah*.

**Appliquer dès la rédaction** — ne pas attendre une passe séparée.

**`**...**` est EXCLUSIVEMENT réservé aux intraduisibles** — jamais pour l'emphase (mettre en valeur une phrase, un mot ordinaire ou un titre), **y compris dans les feuilles d'introduction et les notes** : le gras déclencherait à tort le style « Transliteration » d'Affinity au copier-coller, et l'app afficherait le mot en or, touchable, ouvrant une fiche de lexique vide. Pour l'emphase ordinaire, utiliser l'italique `*...*` ; pour un **terme important**, voir §2.5 bis.

**Polices hébraïques — dossier `utilities/`.** Les polices pour composer le script hébreu (niveau 3) et le rendre dans Affinity Publisher vivent dans `utilities/` à la racine du dépôt : **SBL Hebrew** (`SBL_Hbrw.ttf`) et **Ezra SIL** (`EzraSIL2.51/`) — hébreu biblique avec voyelles et cantillation (*te'amim*) ; **Taamey Frank CLM** (projet Culmus) — hébreu avec *te'amim* ; **Frank Ruhl Libre** — hébreu moderne (fonte variable + statiques). **Attention aux licences** : Ezra SIL et Frank Ruhl Libre sont sous OFL, donc redistribuables — ce sont les deux que La Bible ONT embarque. SBL Hebrew relève d'un EULA propriétaire et Taamey Frank CLM d'une GPL dont l'exception ne couvre que les documents composés, pas un binaire : ces deux-là restent réservées à la composition Affinity et ne doivent jamais entrer dans une app ni dans un site. Ce sont les **assets typographiques** du projet, suivis dans le dépôt pour la composition — non distribués au lecteur (cf. principe de distribution : seuls l'intro et les chapitres du slot voyagent).

### 2.5 bis Marquage des termes importants — `==...==`

**Règle :** un mot qu'on veut mettre en relief **sans en faire un intraduisible** s'écrit `==mot==`.

C'est le surlignage natif d'Obsidian : il se voit en écrivant, et il n'était employé nulle part ailleurs dans le vault.

**Pourquoi cette troisième marque existe.** Le gras était détourné pour insister — `**« Jour »**`, `**Candidat intraduisible**`, `**Sarah**`. Or `**...**` veut dire « intraduisible », et rien d'autre. Le pipeline allait alors chercher une fiche de glossaire qui n'existait pas, et l'app affichait ces mots en or et touchables, promettant une explication qu'elle n'avait pas. L'intention était juste ; il lui manquait sa propre marque.

**Ce que chaque marque produit dans La Bible ONT :**

| écriture | rendu dans l'app | touchable |
|---|---|---|
| texte nu | encre | non |
| `==mot==` | **bordeaux clair `#862742`**, semi-gras | non |
| `**mot**` | **or**, semi-gras | **oui** → fiche de lexique |
| `*mot*` | italique | non |

**Quand employer `==...==` :**

- un mot français que le texte nomme solennellement — `==« Jour »==`, `==« Nuit »==`, `==« Cieux »==` ;
- un nom propre dont le verset explique l'étymologie — `==Chavah==`, `==Noach==`, `==Sarah==` (§4.12 interdit de les baliser comme intraduisibles) ;
- une métadonnée d'apparat critique — `==premier emploi dans l'ONT==`, `==Candidat intraduisible==`.

**Quand ne PAS l'employer :** pour un vrai terme hébreu. Celui-là mérite une entrée de glossaire (§2.5 / §3) et donc `**...**`. Le marquer `==...==` reviendrait à priver le lecteur de sa fiche.

**Côté Affinity :** `==...==` ne déclenche aucun style au copier-coller. Un style de caractère dédié reste à créer si l'édition imprimée doit distinguer ce niveau.


### 2.6 Les noms des livres bibliques

**Règle pour le texte ONT et les noms de fichiers :** Les noms des livres bibliques sont toujours donnés dans leur forme hébraïque translittérée. Ces noms sont intraduisibles : leur titre hébreu est le vrai titre, souvent issu du premier mot du livre. Cette règle vaut aussi pour les noms de fichiers (ex. `bereshit-1.md`, pas `genese-1.md`).

**Format des titres de section ONT :**
- Titre principal : `# Bereshit 1` — le nom hébreu translittéré est le vrai titre, suivi du numéro de section ONT
- Sous-titre : `*(Genèse / בְּרֵאשִׁית 1:1 — 2:3)*` — le nom français comme pont de navigation pour le lecteur occidental, suivi du script hébreu et de la référence de verset

**Format dans le corps du texte et les renvois :** *Bereshit* 7:2 — toujours la translittération

**Logique :** Le nom hébreu est le nom réel de la section. Le nom français (Genèse, Exode...) sert uniquement de repère pour que le lecteur occidental s'y retrouve dans sa Bible traditionnelle — il apparaît en sous-titre, jamais comme désignation principale.

**Répertoire des noms hébraïques — Torah :**
| Nom français | Nom hébreu | Translittération | Hébreu |
|---|---|---|---|
| Genèse | *Bereshit* | Bereshit | בְּרֵאשִׁית |
| Exode | *Shemot* | Shemot | שְׁמוֹת |
| Lévitique | *Vayiqra* | Vayiqra | וַיִּקְרָא |
| Nombres | *Bemidbar* | Bemidbar | בְּמִדְבַּר |
| Deutéronome | *Devarim* | Devarim | דְּבָרִים |

**Répertoire des noms hébraïques — Nevi'im (Prophètes) :**
| Nom français | Translittération | Hébreu |
|---|---|---|
| Josué | *Yehoshua* | יְהוֹשֻׁעַ |
| Juges | *Shoftim* | שֹׁפְטִים |
| Samuel (1-2) | *Shemuel* | שְׁמוּאֵל |
| Rois (1-2) | *Melakhim* | מְלָכִים |
| Ésaïe | *Yeshayahu* | יְשַׁעְיָהוּ |
| Jérémie | *Yirmeyahu* | יִרְמְיָהוּ |
| Lamentations | *Ekha* | אֵיכָה | Décision ONT : placé en Nevi'im après *Yirmeyahu* (lien fonctionnel et historique direct), et non dans les Ketouvim — le regroupement des Megillot est rabbinique post-70 CE, pas Second Temple |
| Ézéchiel | *Yehezqel* | יְחֶזְקֵאל |
| Osée | *Hoshea* | הוֹשֵׁעַ |
| Joël | *Yoel* | יוֹאֵל |
| Amos | *Amos* | עָמוֹס |
| Abdias | *Ovadyah* | עֹבַדְיָה |
| Jonas | *Yonah* | יוֹנָה |
| Michée | *Mikhah* | מִיכָה |
| Nahoum | *Nahum* | נַחוּם |
| Habacuc | *Havaquq* | חֲבַקּוּק |
| Sophonie | *Tsefanyah* | צְפַנְיָה |
| Aggée | *Haggai* | חַגַּי |
| Zacharie | *Zekharyah* | זְכַרְיָה |
| Malachie | *Malakhi* | מַלְאָכִי |

**Répertoire des noms hébraïques — Ketouvim (Écrits) :**
| Nom français | Translittération | Hébreu |
|---|---|---|
| Psaumes | *Tehilim* | תְּהִלִּים |
| Proverbes | *Mishlei* | מִשְׁלֵי |
| Job | *Iyov* | אִיּוֹב |
| Cantique | *Shir Hashirim* | שִׁיר הַשִּׁירִים |
| Ruth | *Ruth* | רוּת |
| Ecclésiaste | *Qohelet* | קֹהֶלֶת |
| Esther | *Esther* | אֶסְתֵּר |
| Daniel | *Daniel* | דָּנִיֵּאל |
| Esdras | *Ezra* | עֶזְרָא |
| Néhémie | *Nehemyah* | נְחֶמְיָה |
| Chroniques (1-2) | *Divrei Hayamim* | דִּבְרֵי הַיָּמִים |

**Répertoire des noms — Besorot (Évangiles) :**
| Nom français | Translittération ONT | Hébreu | Notes |
|---|---|---|---|
| Marc | *Marqus* | מַרְקוּס | Première *besorah* rédigée — dans les *Eduyot*. Nom complet : *Yohanan Marqus* (יוֹחָנָן מַרְקוּס — *Gevurot* 12:12) |
| Matthieu | *Matityahu* | מַתִּתְיָהוּ | "don de YHWH" — dans les *Eduyot* |
| Luc | *Luqas* | לוּקָס | Nom grec translittéré — dans les *Eduyot* |
| Jean | *Bereshit ha-Yohanan* | בְּרֵאשִׁית הַיּוֹחָנָן | *Bereshit* de Yohanan — *besorah* cosmique-inaugurale, écho de *Bereshit* 1:1, séparée des *Eduyot* |

**Répertoire des noms — Gevurot ha-Neviim et Machazeh :**
| Nom français | Translittération ONT | Hébreu | Notes |
|---|---|---|---|
| Actes des apôtres | *Gevurot ha-Neviim* | גְּבוּרוֹת הַנְּבִיאִים | "les *gevurot* (actes de puissance) de **YHWH** à travers ses *neviim*" — de *gavar* (גָּבַר) : être puissant, l'emporter. **YHWH** sujet grammatical, *neviim* instrument. Jamais *Ma'asim HaShlichim* (importait la catégorie grecque *apostolos* comme agent autonome). |
| Apocalypse | *Machazeh Yohanan* | מַחֲזֵה יוֹחָנָן | *machazeh* = vision intérieure — même terme qu'en *Bereshit* 15:1 |

**Répertoire des noms — Igerot (Lettres) :**
| Nom français | Translittération ONT | Hébreu | Notes |
|---|---|---|---|
| Romains | *El HaRomiyim* | אֶל הָרוֹמִיִּים | Igerot de Shaul |
| 1-2 Corinthiens | *El HaQorintiyim* | אֶל הַקּוֹרִינְתִּיִּים | Igerot de Shaul |
| Galates | *El HaGalatiyim* | אֶל הַגָּלָטִיִּים | Igerot de Shaul |
| Éphésiens | *El HaEfesiyim* | אֶל הָאֶפֶסִיִּים | Igerot de Shaul |
| Philippiens | *El HaFilipiyim* | אֶל הַפִּילִיפִּיִּים | Igerot de Shaul |
| Colossiens | *El HaQolossiyim* | אֶל הַקּוֹלוֹסִּיִּים | Igerot de Shaul |
| 1-2 Thessaloniciens | *El HaTessaloniqiyim* | אֶל הַתֶּסָּלוֹנִיקִיִּים | Igerot de Shaul |
| 1-2 Timothée | *El Timotiyos* | אֶל טִימוֹתִיּוֹס | Igerot de Shaul |
| Tite | *El Titos* | אֶל טִיטוֹס | Igerot de Shaul |
| Philémon | *El Filemon* | אֶל פִּילֵמוֹן | Igerot de Shaul |
| Hébreux | *Igeret HaIvrim* | אִגֶּרֶת הָעִבְרִים | Anonyme — ancrée dans *Vayiqra* |
| Jacques | *Igeret Ya'aqov* | יַעֲקֹב | "talon / il supplante" |
| 1-2 Pierre | *Igerot Kefa* | כֵּיפָא | Araméen : "roc" |
| 1-3 Jean | *Igerot Yohanan* | יוֹחָנָן | |
| Jude | *Igeret Yehudah* | יְהוּדָה | "celui qui est loué" |

### 2.7 La feuille d'introduction

Chaque livre s'ouvre par une **feuille d'introduction** qui porte, une fois en amont, tout le cadre (situation, question du livre, comment lire, motifs, plan) — au lieu de le répéter en gloses page après page. L'introduction est la voix du projet (dense) ; le corps garde la voix vécue et ses gloses restent légères. Sections types : **Titre & Shem · Régime d'auteur · Thème · Date d'émergence · Date de consignation · Contexte historique · But · Comment lire · Vue d'ensemble · Caractéristiques particulières · Échos dans la Berit Hadashah · Plan · Repères.** Fichier `*-0-intro.md` à côté du livre. Inaugurée avec *Toledot Adam ve-Chavah*.

### 2.8 Les use cases d'annotation

Opérationnalise §2.1 : chaque terme du glossaire reçoit **un** use case — une combinaison fixe des trois niveaux, appliquée mécaniquement.

| UC | Type | Niveau 3 (hébreu) |
|---|---|---|
| **UC0** | Noms divins — hébreu/gras, jamais traduits ; glose fondatrice une fois dans tout le corpus | généreux |
| **UC1** | Intraduisible — le mot reste hébreu (gras) | 1re occ. |
| **UC2** | Noyau *(traduit, hébreu persistant)* — *shamayim*/Cieux, *eretz*/Terre, *adamah*/sol concret… | **≥ 1×/chapitre** (régime b) |
| **UC3** | Traduit standard *(le défaut)* — *chata*/dévier, *tselem*/représentant fonctionnel… | 1re occ., puis nu |
| **UC4** | Nom propre | 1re occ. + identification sur 5 occ. (§4.12) |
| **UC5** | Glose seule — structure (mérisme, chiasme, ambiguïté, silence) | — |
| **UC6** | Français simple — mot ordinaire hors glossaire | — |

Règle : le gras **est** la translittération exacte (apostrophes comprises : **She'ol**, **mal'akh**), jamais une francisation.

---

## 3. TERMINOLOGIE FIXÉE — GLOSSAIRE COMPLET

Ce glossaire est **immuable**. Chaque terme hébreu a sa traduction française fixe pour tout l'ONT. Ne jamais dévier de ces choix sans décision explicite de l'auteur.

### 3.1 Verbes fondamentaux

| Terme hébreu | Translittération | Traduction ONT | Ce qu'il signifie |
|---|---|---|---|
| בָּרָא | *bara* | orchestrer | Inaugurer dans l'existence fonctionnelle. Sujet exclusif : Elohim. Jamais de matière première mentionnée. |
| עָשָׂה | *asah* | mettre en place / accomplir | Réaliser concrètement. Dimension structurelle de la parole divine. |
| יָצַר | *yatsar* | façonner | Verbe du potier. Acte matériel et artisanal. Toujours suivi d'une matière première. |
| אָמַר | *amar/vayomer* | formuler | Parole performative — qui en s'énonçant accomplit ce qu'elle énonce. |
| דִּבֶּר | *dibber/vayedabber* | parla (distinct de *vayomer*) | De la même racine que **davar**. Communication relationnelle directe, adressée à quelqu'un. Non pas la parole cosmique performative de *vayomer* — la parole dans sa dimension d'adresse personnelle. Rendu "parla" pour maintenir la distinction avec "formula" (*vayomer*). |
| רָאָה | *ra'ah/vayar* | examiner | Regard évaluateur du maître d'œuvre — inspection fonctionnelle. |
| בָּדַל | *badal/vayavdel* | distinguer | Séparer, différencier. Même racine que la *havdalah* juive. |
| קָרָא | *qara/vayiqra* | nommer | Acte souverain — faire entrer dans l'existence fonctionnelle. |
| נָתַן | *natan/vayiten* | installer / attribuer | Donner, placer, attribuer. Acte de placement précis et intentionnel. |
| בָּרַךְ | *barakh/vayevarekh* | doter | Transmission d'une capacité fonctionnelle active. Jamais "bénir". |
| קָדַשׁ | *qadash/vayeqadesh* | consacrer | Mettre à part fonctionnellement, séparer pour le domaine divin. |
| שָׁבַת | *shavat/vayishbot* | marquer une cessation | Cesser souverainement parce que l'œuvre est accomplie. Pas "se reposer". |
| כָּלָה | *kalah/vayekhullu* | atteindre leur plénitude | Être achevé dans sa totalité. Pas "être terminé". |
| רָדָה | *radah* | gouverner | Gouvernance d'un représentant royal — autorité déléguée. |
| כָּבַשׁ | *kavash* | prendre en charge | Prise en charge responsable d'un territoire. Pas "exploiter". |
| מָשַׁל | *mashal* | gouverner | Gouvernance fonctionnelle sur un domaine temporel. |
| עָבַד | *avad* | servir | Service sacerdotal — les lévites *avad* le Tabernacle, les prêtres *avad* le Temple. L'adam dans le Jardin est un prêtre, pas un agriculteur. |
| בָּנָה | *banah* | édifia | Bâtir, construire — terme de l'architecte. Distinct de *yatsar* (potier). La femme est érigée comme on construit un temple ou une ville. |
| חָטָא | *chata* | dévier | L'acte de déviation fonctionnelle — étymologiquement rater sa cible, manquer sa marque. Distinct de *ra* (état dysfonctionnel) : *chata* est l'acte, *ra* est l'état. |

### 3.2 Noms et concepts fondamentaux

| Terme hébreu | Translittération | Traduction ONT | Ce qu'il signifie |
|---|---|---|---|
| אֱלֹהִים | *Elohim* | Elohim | Laissé en hébreu — intraduisible sans perte. Pluriel hébreu avec accord grammatical singulier. Même traitement que Ruach, Nefesh, Neshamah. |
| אוֹר | *or* | Lumière | Non pas la lumière physique — l'Ordre lui-même. Ce qui rend toute distinction possible. |
| חֹשֶׁךְ | *choshekh* | Ténèbres | L'absence de toute lumière — donc l'impossibilité de distinguer quoi que ce soit. |
| תֹהוּ וָבֹהוּ | *tohu vavohu* | sans ordre ni fonction ni habitant | Un espace non nommé, non délimité, non assigné — présent matériellement mais inexistant fonctionnellement. |
| תְהוֹם | *tehom* | eaux primordiales | L'océan sans fond, sans limite, sans bord — les eaux d'avant toute ordination. Apparenté à Tiamat. |
| רוּחַ | *ruach* | Ruach | Intraduisible : souffle, vent, esprit — trois dimensions inséparables. Toujours laissé en hébreu. |
| רָקִיעַ | *raqia* | Voûte | Surface délimitante tendue entre les eaux d'en haut et d'en bas. |
| שָׁמַיִם | *shamayim* | Cieux | Ce qu'on voit au-dessus de nous. Étymologiquement "là où sont les eaux". |
| אֶרֶץ | *eretz* | Terre | Le domaine terrestre habitable — avec majuscule une fois nommé. |
| אֲדָמָה | *adamah* | sol concret | La glaise, la terre cultivable dans sa dimension physique. Même racine qu'Adam. |
| אָדָם | *adam* | l'Être façonné du sol (Bereshit 1-7) / **adam** intraduisible (Bereshit 8+) | Bereshit 1-7 : traduit "l'Être façonné du sol" pour rendre visible l'étymologie adamah/adam. Bereshit 8+ : intraduisible — laissé en hébreu en gras. Dans les contextes légaux et covenantaux de Gn 9, ha-adam désigne l'humanité dans son universalité ; la périphrase complète brise les chiasmes et alourdit la formulation du droit divin. Décision actée en Bereshit 8, v.5. Extension : le critère est l'ère, non le livre — dans un récit hors *Bereshit* mais en régime antédiluvien (avant le **mabbul**, ex. *Sefar Gibbaraya*), la périphrase "l'Être façonné du sol" vaut également, car c'est l'ère de *Bereshit* 1-7. **Distinction essentielle** : la périphrase rend le **générique** *ha-adam* / *benei ha-adam* (l'humanité, l'espèce). Le **nom propre** Adam d'un personnage individuel (ex. *Toledot Adam ve-Chavah*, où Adam et Chavah sont des personnes nommées) demeure un **nom propre** (§4.12) — ni traduit, ni balisé, glosé à la première occurrence. |
| אִשָּׁה / אִישׁ | *ishah* / *ish* | Ishah / Ish | Intraduisible. Non pas "femme/homme" au sens social. L'ishah est édifiée (banah) pour faire face à l'ish — "os de mes os, chair de ma chair." Le lien ish/ishah est une alliance de l'être même. *Ishto* = sa ishah (forme possessive). *Eshet* = ishah de (forme construite). *Neshei* = pluriel construit. Laissé en hébreu comme Ruach et Nefesh. **RÈGLE ABSOLUE — accord du possessif : toujours "ta/sa/ma ishah", jamais "ton/son/mon ishah" même devant voyelle. Le hiatus est délibéré — il rend le genre féminin visible. Erreur récurrente à ne jamais reproduire.** |
| נֶפֶשׁ | *nefesh* | Nefesh | Intraduisible. Non pas "l'âme" grecque — le principe vital concret et incarné. Toujours laissé en hébreu. |
| צֶלֶם | *tselem* | représentant fonctionnel | Statue représentative d'un roi. L'être humain est le tselem d'Elohim sur la Terre. |
| דְּמוּת | *demut* | modelé sur | Conformité au caractère et à la manière d'être d'Elohim. Renforce *tselem*. |
| שֵׁם | *shem* | Shem | Intraduisible. Non pas "le nom" au sens français — l'acte d'existence fonctionnelle lui-même. Nommer c'est faire entrer dans l'ordre. Laisser en hébreu comme Ruach et Nefesh. |
| טוֹב | *tov* | **tov** | Intraduisible. Non pas "beau" ou "moralement bien" : ce qui est pleinement ajusté à sa destination dans l'ordre cosmique, ce qui accomplit sa fonction. Opposé : **ra**. |
| טוֹב מְאֹד | *tov me'od* | **tov me'od** | Intraduisible. **Tov** + *me'od* (l'intensificateur de plénitude totale). Utilisé une seule fois dans Bereshit 1 — pour le cosmos entier dans sa totalité intégrée. |
| רַע | *ra* | **ra** | Intraduisible. Opposé fonctionnel de **tov** — ce qui rate sa destination, ce qui s'écarte de l'ordre cosmique. Non pas "le Mal" au sens moral grec. Formes : *ra* (adjectif/nom), *ra'at* (construit : "le ra de"), *ra'im* (pluriel). |
| מְלַאכָה | *melakhah* | œuvre architecturale | Travail qualifié de l'architecte. Même mot pour la construction du Tabernacle. |
| קָדוֹשׁ | *qadosh* | consacré / sacré | Mis à part fonctionnellement pour le domaine divin. Non pas "moralement pur". |
| בְּרִית | *berith* | alliance | Structure fonctionnelle d'engagement. Développé en Bereshit 8 : ici unilatérale — Elohim seul s'engage, Noach n'est pas invité à promettre. Non pas un contrat bilatéral mais une déclaration souveraine de fidélité permanente. Meqim (qum : faire se tenir) et non karat (couper) — l'alliance se tient debout par la parole d'Elohim seul. |
| חֶסֶד | *chesed* | **chesed** | Intraduisible. La fidélité loyale envers celui à qui l'on est lié par une **berith** : tenir parole et agir pour son bien, dans la durée. Non pas "bonté" (trop faible — rate la loyauté engagée), ni "grâce" (catégorie théologique tardive de la faveur imméritée — importée, §4.7), ni "miséricorde" (le **chesed** est *dû* à l'intérieur d'un lien, non simple pitié). S'étend de la fidélité de **YHWH** envers les siens (*chasdo* — qui « dure **le'olam** », *Tehilim* 136) jusqu'à la loyauté entre humains liés (Ruth envers Naomi). Premier emploi en *Bereshit* 19:19 — le **chesed** qui garde le **Nefesh** de Lot. Même logique relationnelle qu'**emunah** : une posture de fidélité, non un sentiment. Traitement définitif (plus ample) réservé à son locus central — *Shemot* 34:6-7 (*rav chesed*) et *Ruth*. Laissé en hébreu. |
| עוֹלָם | *olam* | **olam** | Intraduisible. De la racine "caché, dissimulé" : la limite temporelle que le regard humain ne peut pas discerner — l'horizon qui se dérobe. Non pas l'éternité abstraite des Grecs (*aeternitas*), mais ce qui est au-delà du visible. **Règle de rendu en corps de texte : translittérer le construit en entier.** *Berit olam* → **berith-olam**. *Akhuzat olam* → **akhuzat-olam**. *Ledorot olam* → **ledorot-olam**. *Ad-olam* → **ad-olam**. *Le'olam* → **le'olam**. *Me'olam* → **me'olam**. Premier emploi *Bereshit* 3:22 (*vechai le'olam*). |
| פָּנִים | *panim* | face | Non pas une surface neutre — une surface orientée vers, en relation avec. |
| מוֹעֵד | *mo'ed* | temps fixé | Le rendez-vous sacré, l'assemblée convoquée. Non pas "saison". |
| חַטָּאת | *chattah* | la déviation | Forme nominale de *chata* — l'acte de déviation lui-même, personnifié en *Bereshit* 4:7 comme une présence qui rôde. Jamais "le péché" (catégorie morale grecque). |
| מִנְחָה | *minchah* | tribut | Geste du vassal vers son suzerain — non pas encore un terme sacrificiel technique. Apporter un tribut c'est reconnaître une autorité supérieure. |
| אָרוּר | *arur* | frappé de dysfonctionnement | Opposé de *barakh* (doter) — non pas l'absence de dotation, mais sa perversion. La dotation demeure mais devient dysfonctionnelle. Le serpent continue de se mouvoir, l'adamah continue de produire, Qayin continue de vivre : mais tout cela est atteint dans sa fonction. |
| קַלֵּל | *qallel* | retirer de sa kavod | De *qalal* — alléger, réduire le poids fonctionnel. Non pas supprimer totalement : l'adamah conserve de la kavod après *Bereshit* 3, elle fonctionne encore. *Qallel* allège — il ne vide pas. Opposé exact de *barakh* (doter, alourdir de capacité). Première occurrence *Bereshit* 8:21 — YHWH promet de ne plus en retirer davantage. |
| כָּבוֹד | *kavod* | kavod | Intraduisible. De *kaved* (כָּבֵד) — être lourd, peser. La pesanteur fonctionnelle d'une réalité dans l'ordre cosmique : sa substance, son poids d'existence, sa densité dans l'ordre divin. Opposé de *qalal* (légèreté, vide). S'étend de la kavod d'une réalité créée jusqu'à la kavod de YHWH lui-même — la même racine, la même logique de pesanteur fonctionnelle. Laissé en hébreu. |
| טָהוֹר / לֹא טָהוֹר | *tahor* / *lo tahor* | Tahor / lo tahor | Intraduisible. Non pas "pur/impur" au sens moral ou hygiénique — pureté fonctionnelle rituelle : ce qui peut entrer en contact avec le domaine sacré sans le perturber, et ce qui ne le peut pas. Première occurrence en *Bereshit* 7:2 — catégorie déjà opératoire avant Sinaï. Laissé en hébreu dans le corps du texte, expliqué dans les gloses. |
| עֹלָה | *olah* | Olah | Intraduisible. De *alah* (עָלָה) — monter, s'élever. L'offrande qui monte vers Elohim dans la fumée. Jamais "holocauste" (terme grec chargé d'histoire moderne) ni "burnt offering" (catégorie rituelle chrétienne). Premier emploi en *Bereshit* 8:20 — acte inaugural après la re-création. Laissé en hébreu dans le corps du texte, expliqué dans les gloses. |
| מִזְבֵּחַ | *mizbeach* | autel | De *zavach* — égorger, sacrifier. Littéralement "le lieu d'égorgement". Traduit "autel" avec niveau 3 obligatoire à chaque première occurrence dans une Fondation : **autel** (*mizbeach* / מִזְבֵּחַ). |
| כֹּהֵן | *kohen* | Kohen | Intraduisible. Non pas "prêtre" (catégorie romaine/catholique anachronique qui réduit le terme à la fonction sacrificielle). Le **kohen** hébreu est l'intermédiaire fonctionnel qui maintient l'interface entre le domaine humain et le domaine divin — il tient les deux côtés ouverts l'un à l'autre. Pluriel : **kohanim**. Forme construite : *kohen* de/de l'alliance. Premier emploi en *Bereshit* 14:18 — Malki-tsedeq, **kohen** de **El Elyon**. Central dans tout Vayiqra. Laissé en hébreu. |
| צֶדֶק | *tsedeq* | tsedeq | Intraduisible. L'ordre juste cosmique, la conformité structurelle au bon fonctionnement de la réalité. Non pas "justice" au sens moral grec (*dikaiosyne*). Trois formes intraduisibles issues de cette racine : **tsedeq** (le concept), **tsadiq** (l'adjectif : celui qui est dans l'ordre juste — premier emploi Bereshit 6:9), **tsedaqah** (la forme nominale : l'état ou l'acte de juste-ordre — premier emploi Bereshit 15:6). |
| רָשָׁע | *rasha* | **rasha** | Intraduisible. L'opposé fonctionnel de **tsadiq** : celui dont l'existence est structurellement déviée de l'ordre cosmique. Non pas "méchant" au sens moral subjectif — celui qui est de travers dans l'ordre fonctionnel. La paire **tsadiq**/**rasha** est constitutive du droit divin hébraïque et de tout le corpus des Nevi'im. Pluriel : **resha'im**. Premier emploi en *Bereshit* 18:23. |
| אֲדֹנָי | *Adonai* | Adonai | Intraduisible. De *adon* (אָדוֹן) : le maître, le seigneur — *Adonai* = "mon seigneur/maître". Titre de maîtrise souveraine absolue adressé à **YHWH**. Distinct d'**Elohim** et de **YHWH**. Dans l'usage liturgique hébreu, *Adonai* deviendra la substitution prononcée pour **YHWH**. S'écrit seul ou combiné : **Adonai** **YHWH**. Premier emploi en *Bereshit* 15:2. |
| אֵל עֶלְיוֹן | *El Elyon* | El Elyon | Intraduisible. *Elyon* de *alah* (עָלָה) : monter, s'élever — El le Souverain élevé, l'El au sommet de l'ordre cosmique. Titre du dieu suprême dans les cosmologies proche-orientales voisines. En *Bereshit* 14, Malki-tsedeq l'emploie, Avram l'identifie à **YHWH** : **YHWH El Elyon**. Laissé en hébreu. |
| אֵל רֳאִי | *El Roï* | El Roï | Intraduisible. De *El* (אֵל) + *ro'i* (רֳאִי) de *ra'ah* (voir) : "El qui me voit", "El de la vision de moi". Nom divin unique dans toute la Bible — donné une seule fois, par Hagar, une servante égyptienne en fuite dans le désert. Première et unique occurrence en *Bereshit* 16:13. Laissé en hébreu. |
| אֵל שַׁדַּי | *El Shaddai* | El Shaddai | Intraduisible. Étymologie débattue : *shadad* (שָׁדַד) : puissance absolue ; ou akkadien *šadu* : montagne ; ou *she-dai* (שֶׁ-דַּי) : "Celui-qui-suffit". Ce nom accompagne les moments où **YHWH** accomplit l'impossible humain. Premier emploi en *Bereshit* 17:1. Laissé en hébreu. |
| מַלְאַךְ | *mal'akh* | mal'akh | Intraduisible. Non pas "ange" (catégorie grecque anachronique). L'envoyé-fonctionnaire de **YHWH** — de la racine *la'akh* (envoyer, déléguer) : celui que **YHWH** mandate pour accomplir un acte dans le monde humain. Il n'est pas défini par sa nature mais par sa mission. Ambiguïté délibérée du texte : le **mal'akh** **YHWH** parle parfois en son propre nom, parfois comme **YHWH** lui-même. Pluriel : **mal'akhim**. Forme combinée : **mal'akh** **YHWH**. Premier emploi en *Bereshit* 16:7. **Mal'akhim nommés** : quand un envoyé céleste porte un nom (Mikha'el — premier de l'ONT, *Toledot Adam ve-Chavah* ; Rafa'el — *Sefar Gibbaraya*), c'est un **nom propre** (sans gras, niveau 3 + glose à la première occurrence, §4.12), non un intraduisible — il garde la fonction de **mal'akh**. Tout nouvel être céleste nommé se décide avec l'auteur (règle des termes chargés). |
| קָנָה | *qanah* | fonder et maîtriser | Double dimension inséparable dans l'hébreu antique : créer/fonder ET acquérir/posséder. *Qoneh shamayim va'arets* = "fondateur et maître des Cieux et de la Terre" — formule du dieu suprême dans les textes proche-orientaux. |
| שָׁלִיחַ | *shaliach* | **shaliach** | Intraduisible. De *shalach* (שָׁלַח) — envoyer, mandater. L'envoyé-mandaté : celui qui porte l'autorité de celui qui l'envoie et agit en son nom. Équivalent hébreu exact du grec *apostolos* — jamais "apôtre" dans l'ONT. Le *shaliach* est défini par sa mission, pas par son statut. Pluriel : *shlichim* (שְׁלִיחִים). Même logique fonctionnelle que *mal'akh* : défini par l'envoi, pas par la nature. |
| דָּבָר | *davar* | **davar** | Intraduisible. La parole ET la chose simultanément — en hébreu antique, la parole et la réalité qu'elle désigne sont le même mot. La distinction française parole/chose n'existe pas : **davar** est à la fois l'événement et la parole qui le nomme. Pluriel : **devarim**. *Devar YHWH* = le **davar** de **YHWH**. Premier emploi en *Bereshit* 11:1 (*devarim ahadim*). |
| מִילָה | *milah* | **milah** | Intraduisible. De *mul* (מוּל) : circoncire. L'acte par lequel le signe de la **berith** est incisé dans la chair. Non pas "circoncision" — le terme latin réduit l'acte à sa dimension physique et perd la dimension covenantale de l'inscription. Premier emploi en *Bereshit* 17. |
| גּוֹי / גּוֹיִם | *goy* / *goyim* | **goy** / **goyim** | Intraduisible. Le peuple-nation dans sa réalité territoriale, ethnique et politique constituée. Non pas "les nations" (abstraction) ni "les gentils" (catégorie religieuse tardive). Présent dès *Bereshit* 10 dans la table des nations ; terme actif de la promesse à Avraham en *Bereshit* 17:4 (*av hamon goyim* : père d'une multitude de **goyim**). |
| עָרְלָה / עָרֵל | *orlah* / *arel* | **orlah** / **arel** | Intraduisible. De *aral* (עָרַל) : être couvert, non ouvert. La chair de l'**orlah** est le lieu du signe de la **berith** ; mais le terme s'étend métaphoriquement : **orlah** du cœur (*Devarim* 10:16), **orlah** des lèvres (*Shemot* 6:12), **orlah** du fruit (*Vayiqra* 19:23). **Arel** : celui qui a encore son **orlah**, dont la chair n'a pas reçu le signe. Premier emploi en *Bereshit* 17:11. |
| מִשְׁפָּט | *mishpat* | **mishpat** | Intraduisible. De *shaphat* (שָׁפַט) : juger, rendre une décision. L'acte de jugement rendu dans l'ordre cosmique — la décision qui discerne et ordonne correctement les parties. Non pas "justice" au sens abstrait grec (*dikaiosyne*) : le **mishpat** est concret, situationnel. Inséparable de **tsedaqah** dans tout le corpus : *tsedaqah umishpat* — l'ordre-juste et le jugement-juste sont le couple constitutif du droit divin hébraïque. Pluriel : **mishpatim**. Premier emploi en *Bereshit* 18. |
| נָחַם | *nacham* | **nacham** | Intraduisible. Deux dimensions indissociables : être saisi au fond des entrailles — une émotion viscérale qui ébranle la totalité de l'être — ET reconsidérer depuis cet endroit affecté. Non pas un simple chagrin ni un simple changement d'avis. Même racine : le **shem** de Noach (*Bereshit* 5:29 — *yenachameinu* : "il nous **nacham**era") et la consolation prophétique (*Yeshayahu* 40:1 — *nachamu nachamu ami*). Appliqué à **YHWH** en *Bereshit* 6:6 — le texte ne l'atténue pas. Premier emploi *Bereshit* 5:29. |
| שֹׁפֵט | *shofet* | **shofet** | Intraduisible. De *shaphat* (שָׁפַט) — même racine que **mishpat**. Celui qui exerce le **mishpat** dans une situation concrète : non pas le magistrat de tribunal (catégorie juridique moderne), mais celui qui rétablit l'ordre fonctionnel, qui discerne et ordonne. *Shofet kol ha'arets* ("le **shofet** de toute la Terre") — titre de souveraineté cosmique universelle de **YHWH** en *Bereshit* 18:25. Le titre du livre *Shoftim* résonne directement : les **shoftim** d'Israël sont ceux qui exercent le **mishpat** de **YHWH** dans l'histoire concrète. Pluriel : **shoftim**. Premier emploi en *Bereshit* 18:25. |
| שְׁאוֹל | *She'ol* | **She'ol** | Intraduisible. Le domaine bas où descendent les morts — non pas « l'enfer » (lieu de tourment, catégorie grecque/chrétienne tardive) ni « le séjour des morts » édulcoré. Le lieu du silence et de l'attente sous la Terre, où descend tout mort — **tsadiq** comme **rasha** — dans la cosmologie hébraïque (§6). Opposé structurel de la montée de l'âme grecque : on descend au **She'ol**, on ne s'envole pas. Premier emploi dans l'ONT en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| תְּשׁוּבָה | *teshuvah* | **teshuvah** | Intraduisible. De *shuv* (שׁוּב) : se retourner, revenir. Le mouvement de retour vers **YHWH** **Elohim** — se réorienter vers la présence quittée. Non pas « repentance » (culpabilité subjective, §4.7) ni « pénitence » (mérite/satisfaction). Même logique fonctionnelle qu'**emunah** — une posture relationnelle, non un sentiment. Premier emploi dans l'ONT en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| הַשָּׂטָן | *ha-satan* | **ha-satan** | Intraduisible. De *satan* (שָׂטָן) : accuser, s'opposer. **Ha-satan** = *l'*accusateur, une **fonction** du Conseil Divin (*Iyov* 1-2 ; *Zekharyah* 3) — non un nom propre : l'article défini « ha- » l'atteste. Non le « Satan » dualiste (dieu rival, principe métaphysique du mal), ni le serpent d'Eden (qui reste le *nachash* fonctionnel). Sa capacité à se transfigurer en lumière est corroborée par Shaul (2 Co 11:14). Traitement définitif réservé à *Iyov* ; introduit provisoirement en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| טְבִילָה | *tevilah* | **tevilah** | Intraduisible. De *taval* (טָבַל) : plonger, immerger. L'immersion de retour — passer par les eaux pour se retourner vers **YHWH** **Elohim** : le mouvement de la **teshuvah** rendu par le corps. Non « baptême » (catégorie chrétienne tardive) ni « pénitence » (mérite). Le mikveh du Second Temple ; l'immersion de Yohanan « pour la teshuvah » (Mc 1:4). Premier emploi dans l'ONT en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| מֶרְכָּבָה | *merkavah* | **merkavah** | Intraduisible. De *rakhav* (רָכַב) : monter (un char). Le **trône-char** de **YHWH** **Elohim**, contemplé en vision — Yehezqel (Ez 1), mode de la traversée architecturale (Nistarot) ; Shaul ravi au troisième ciel (2 Co 12). Non un « chariot » ordinaire. Premier emploi en corps de texte en *Toledot Adam ve-Chavah*. Laissé en hébreu. |

### 3.3 Créatures et catégories vivantes

| Terme hébreu | Translittération | Traduction ONT | Ce qu'il signifie |
|---|---|---|---|
| תַּנִּינִם | *tanninim* | dragons des eaux | Dans les cosmologies voisines : divinités chaotiques primordiales. Ici : Nefesh vivants parmi d'autres. |
| שֶׁרֶץ | *sherets* | qui grouillent | Catégorie fonctionnelle propre au milieu aquatique — le grouillement dense et foisonnant. |
| עוֹף | *of* | créatures ailées | Étymologiquement "ce qui vole". |
| כָּנָף | *kanaf* | aile | Ce qui permet d'habiter le domaine aérien. |
| בְּהֵמָה | *behemah* | grands quadrupèdes | Les animaux de l'espace proche de l'homme — domestiques et domesticables. |
| רֶמֶשׂ | *remes* | rampants | De *ramas* — se mouvoir au ras du sol. |
| חַיָּה | *chayah* | bêtes sauvages | La vitalité brute, la force animale non domestiquée. |

### 3.4 Les formes verbales hébraïques (*binyanim*)

L'hébreu biblique construit ses verbes sur sept formes (*binyanim*) qui modifient le sens d'une même racine. Ces formes apparaissent dans les gloses pour préciser comment un mot est construit et pourquoi son sens diffère de la racine simple. Référence pour le lecteur non-hébraïsant :

| Forme | Fonction | Exemple dans l'ONT |
|---|---|---|
| **Qal** | Forme simple active — l'action dans sa forme de base | *bara* (orchestrer) — Qal de ב-ר-א |
| **Niphal** | Forme passive ou réflexive — être fait / se laisser faire | *vayera* (se laissa voir) — Niphal de *ra'ah* |
| **Piel** | Forme intensive active — action répétée, accomplie avec intensité | *dibber* (parla, adressé à) — Piel de *davar* |
| **Pual** | Forme intensive passive | — |
| **Hiphil** | Forme causative active — faire en sorte que / déclarer comme / traiter comme | *he'emin* (emuna) — Hiphil de *aman* |
| **Hophal** | Forme causative passive | — |
| **Hitpael** | Forme réflexive-intensive — agir sur soi-même / marcher avec | *hithalekh* (marchait avec) — Hitpael de *halakh* |

Quand une glose écrit "hiphil de *aman*", elle dit : c'est la forme causative de la racine *aman* (être ferme) — soit "traiter comme ferme, s'appuyer sur". Quand elle écrit "niphal de *ra'ah*", elle dit : c'est la forme passive-réflexive de *ra'ah* (voir) — soit "se laisser voir, se révéler".

---

## 4. PRINCIPES DE TRADUCTION

### 4.1 Les gloses

Le lecteur occidental ne possède pas les réalités hébraïques en tête. Les gloses sont là pour expliciter ce que le lecteur hébreu comprenait implicitement par sa langue, sa culture et son vécu quotidien. Ce n'est pas de l'invention — c'est de la médiation culturelle nécessaire, dans la tradition des Targoums.

**Règle absolue :** On n'invente jamais — on explicite seulement dans les gloses.

### 4.2 La traduction vs le commentaire

Le corps du texte contient uniquement ce que l'hébreu dit directement. Les gloses contiennent l'explicitation du champ sémantique. Les deux sont distincts visuellement et fonctionnellement.

### 4.3 La démythologisation

Le texte hébreu démythologise systématiquement les cosmologies voisines (babylonienne, ougaritique, cananéenne, égyptienne). Chaque fois qu'un mot ou une réalité renvoie à une divinité ou un mythe des nations environnantes, le texte hébreu le réduit à un instrument fonctionnel dans le système cosmique d'Elohim. Cette démythologisation doit toujours être signalée dans les gloses.

**Exemples déjà traités :**
- Les grands dragons des eaux (*tanninim*) — verset 21
- Les luminaires non nommés (soleil/lune) — verset 16
- Les étoiles mentionnées en parenthèse — verset 16

### 4.4 Les mots intraduisibles

Certains mots hébreux sont trop riches pour être traduits en français sans perte majeure. Ils sont laissés en hébreu dans le corps du texte, en **gras**, et expliqués dans les gloses. Liste complète des formes à baliser → section 2.5. Définitions complètes → section 3.

### 4.5 Le mérisme

Figure hébraïque qui exprime la totalité en nommant les deux extrémités d'un spectre. Toujours signaler dans les gloses.
- "Les Cieux et la Terre" = la totalité du cosmos
- "Les jours et les années" = la totalité du temps

### 4.6 La parole performative

La parole divine (*vayomer* / וַיֹּאמֶר) n'est jamais descriptive — elle est performative. Elle accomplit ce qu'elle énonce. Toujours formulé avec "Elohim formula" — jamais "Elohim dit".

### 4.7 Règle fondamentale — Aucune influence extérieure

**Règle absolue pour tout l'ONT :** Les gloses ne doivent jamais importer de catégories théologiques, philosophiques ou culturelles extérieures à l'ontologie hébraïque antique fonctionnelle. Sont strictement interdits dans les gloses :
- Les catégories théologiques protestantes (grâce non-méritée, mérite, prédestination, substitution pénale, etc.)
- Les catégories théologiques catholiques (mérite, satisfaction, infusion de grâce, etc.)
- Les catégories philosophiques grecques (âme/corps, essence/accident, universel/particulier, etc.)
- Les catégories morales modernes (culpabilité subjective, innocence, justice punitive, etc.)

Chaque glose doit se fonder **exclusivement** sur : la sémantique hébraïque du mot, le contexte du Proche-Orient ancien, la logique fonctionnelle du cosmos hébreu. Si une explication exige une catégorie extérieure, c'est un signal que l'explication est fausse.

**Exemple de faute :** *chen* rendu comme "faveur non méritée" — importe la catégorie protestante de la grâce. *Chen* dit uniquement que l'initiative appartient au donneur, non au receveur. Le mérite n'est pas une catégorie hébraïque antique.

### 4.8 Les échos structurels (chiasme et reprises lexicales)

Quand un passage reprend délibérément le vocabulaire d'un passage antérieur pour créer un écho structurel, le signaler dans les gloses pour le lecteur français qui ne perçoit pas l'hébreu. Formule type : *[écho délibéré de Gn 1:2 — même formulation hébraïque]*.

**Exemple appliqué :** En *Bereshit* 8, le *ruach* d'Elohim sur les eaux (v.1) reprend mot pour mot *Bereshit* 1:2 — c'est la signature littéraire de la re-création. Ce chiasme décréation/re-création (les eaux montent → tout périt ; les eaux descendent → la Terre réapparaît) doit être rendu visible dans les gloses à chaque reprise lexicale significative.

### 4.9 Le silence narratif délibéré

Quand le texte hébreu lui-même ne commente pas une scène, les gloses doivent respecter ce silence. Ne pas surcharger de gloses ce que le texte a voulu sobre.

**Exemple appliqué :** Le corbeau et la colombe (*Bereshit* 8:6-12) — deux envois d'oiseaux, aucun commentaire du narrateur. Le silence est le message. Les gloses restent minimales : on identifie les animaux (*orev* / עֹרֵב ; *yonah* / יוֹנָה) et on laisse le texte parler seul.

### 4.10 Les chiffres fonctionnels hébraïques

Certains nombres hébreux sont des **unités fonctionnelles**, non des durées physiques exactes. Signaler dans les gloses leur valeur fonctionnelle à leur première occurrence dans chaque contexte.

- **40** (*arba'im* / אַרְבָּעִים) — unité de transformation : la durée qu'il faut pour qu'une réalité se transforme fondamentalement. 40 jours de pluie (Gn 7), 40 ans au désert, 40 jours de Moïse sur la montagne. Signaler : *[quarante — unité fonctionnelle hébraïque de la période de transformation]*.
- **7** (*sheva* / שֶׁבַע) — unité de plénitude et d'accomplissement.

### 4.11 Restituer les ambiguïtés — ne pas résoudre ce que le texte ne résout pas

**Règle absolue :** Quand une construction hébraïque est structurellement ambiguë, l'ambiguïté est une information — elle doit être restituée, pas effacée. L'ONT restitue, il ne commente pas et ne tranche pas.

**Dans le corps du texte :** choisir une formulation française qui ne ferme pas l'ambiguïté quand c'est possible, ou qui la laisse suffisamment ouverte.

**Dans les gloses :** présenter explicitement toutes les lectures disponibles dans l'hébreu sans en choisir une. Formuler : "Le texte ne tranche pas", "L'hébreu laisse les deux lectures disponibles", "L'ambiguïté est dans la structure même de la phrase."

**Exemple appliqué :** *ahi Yafet haggadol* (*Bereshit* 10:21) — haggadol peut qualifier Yaphet ("le frère de Yaphet-l'aîné") ou qualifier ahi ("le frère aîné de Yaphet"). Le texte ne résout pas l'ordre de naissance — la glose présente les deux lectures sans trancher.

### 4.12 Les noms propres

**Règle absolue pour tout l'ONT :** Les prénoms et noms propres hébreux sont conservés dans leur forme hébraïque originale — jamais dans leur forme latine ou française traditionnelle.

- Qayin (jamais Caïn), Hevel (jamais Abel), Chavah (jamais Ève), Noach (jamais Noé), Avraham (jamais Abraham), etc.
- **Cette règle s'applique aussi aux noms géographiques :** Sedom (jamais Sodome), Amorah (jamais Gomorrhe), Yarden (jamais Jourdain), Hevron (jamais Hébron), Mitsrayim (jamais Égypte dans les renvois géographiques), Kena'an (jamais Canaan), etc. **Ethnonymes de même** : *Mitsri* (masc.) / *Mitsrit* (fém.) / *Mitsrim* (pl.) — jamais « Égyptien(ne) » (ex. « Hagar la Mitsrit », *Bereshit* 16 ; « les Mitsrim », *Bereshit* 12). Pour l'emploi **adjectival** (langue, culture, architecture d'un peuple), utiliser « de Mitsrayim » (ex. « fortifications de Mitsrayim », « titre royal de Mitsrayim »).
- **La règle vaut dans le corps du texte ET dans les gloses** — ne jamais écrire la forme française même dans une glose d'explication.
- Raison : les noms hébreux sont sémantiquement chargés — leur étymologie est partie intégrante du texte. Traduire le nom en efface le sens.
- **Règle absolue — niveau 2 ET niveau 3 obligatoires :** À la première occurrence de chaque nom propre dans chaque unité ONT, le nom doit porter à la fois son niveau 3 (translittération / הָעִבְרִית) ET sa glose (expliquant l'étymologie et la signification fonctionnelle du Shem). Exemple : Yaphet (*Yaphet* / יֶפֶת) *[de pata : étendre, élargir — son Shem porte la dotation que Noach lui formulera]*. Les occurrences suivantes du même nom dans la même unité n'ont pas besoin de répéter la glose — le nom seul suffit.
- **Règle des cinq premières occurrences — lieux ET personnages :** Pour tout nom propre (lieu, ville, région, mais aussi personnage) apparaissant pour la première fois dans l'ONT, maintenir une brève glose d'identification dans les cinq premières occurrences à travers tout l'ONT (pas seulement dans l'unité). Pour un lieu : identifier le contexte géographique. Pour un personnage : rappeler brièvement qui il est et son rôle fonctionnel. Passé les cinq occurrences, le nom seul suffit — le lecteur connaît. Exemple appliqué pour les lieux : Bereshit 10. Exemple appliqué pour les personnages : Nimrod identifié à chaque réapparition dans ses cinq premières occurrences comme *[Nimrod — le *gibor* de Bereshit 10, fondateur de Bavel et Nineve]*.

### 4.13 Les orientations cardinales — registre littéraire classique

**Règle absolue pour tout l'ONT :** Les directions cardinales sont toujours exprimées dans leur forme littéraire classique française — jamais dans les termes modernes courants.

| Terme moderne | Forme ONT |
|---|---|
| nord | septentrion |
| sud | midi |
| est | orient |
| ouest | occident |
| nord-ouest | nord-occident |
| nord-est | nord-orient |
| sud-ouest | midi-occident |
| sud-est | midi-orient |
| septentrional(e) | septentrional(e) |
| méridional(e) | méridional(e) |

**Cette règle s'applique** : au corps du texte (niveau 1), aux gloses (niveau 2), et aux notes de bas de section. Elle vaut pour les expressions prépositionnelles ("au septentrion de", "à l'orient de", "à l'occident de") comme pour les emplois nominaux ("le septentrion", "le midi", "vers l'orient").

**Raison :** Nord/sud/est/ouest sont des termes modernes qui jettent une note anachronique dans le registre de l'ONT. Septentrion/midi/orient/occident sont les formes littéraires classiques, cohérentes avec la gravité et l'ancienneté du texte.

### 4.14 La datation à plusieurs niveaux

Dater un texte par son seul manuscrit est l'erreur de l'historien moderne. L'ONT est une histoire **ontologico-fonctionnelle** : elle distingue **trois dates**.
- **Date d'émergence** — quand la *réalité* est entrée dans le monde. Datable depuis l'intérieur du réel (p. ex. « dès le Jardin d'Eden »), non une métaphore.
- **Date de transmission** — quand la vérité circulait, vivante et courante à une époque, avant sa fixation.
- **Date de consignation** — quand le témoin que nous tenons a été mis par écrit.

Les trois découlent du modèle **déclin → recouvrement** : la réalité est ancienne, l'écrit est tardif — un fragment recouvré. Le moderne colle tout sur la consignation et croit avoir daté le texte.

### 4.15 Le régime d'auteur

La notion antique d'auteur est **fonctionnelle**, non moderne-individuelle. Deux régimes :
- **Auteur attesté et de sa main** — identifiable, il a réellement produit le texte (ex. les *Igerot* de Shaul).
- **Auteur qui restitue** — le nom marque la *provenance et l'autorité* d'une vérité, non le scribe physique. Ce n'est pas une fraude : écrire sous un nom révéré déclare que la vérité appartient à ce courant.

Ainsi la Torah est mosaïque par **autorité**, non par chaque trait de plume : *Devarim* 34 raconte la mort de Moshe, et *Bava Batra* 14b-15a le reconnaît depuis toujours (Yehoshua écrivit les derniers versets). Le régime d'auteur nomme *à qui la vérité appartient*, pas seulement *quelle main a tenu le calame*.

---

## 5. CE QUI DISTINGUE L'ÊTRE HUMAIN DE L'ANIMAL

Point capital pour tout le reste de la Bible :

- **Le Nefesh** (*nefesh chayah*) — commun à l'être humain ET à tous les animaux. Ce n'est pas ce qui distingue l'homme.
- **Le Tselem** (*tselem elohim*) — exclusif à l'être humain. C'est le mandat de représentant fonctionnel d'Elohim sur la Terre. Ce qui distingue l'homme de l'animal n'est pas son âme (catégorie grecque) mais sa **fonction cosmique de vice-roi**.

---

## 6. LA STRUCTURE COSMOLOGIQUE HÉBRAÏQUE

Pour comprendre et traduire correctement tout le texte :

**En bas** — la Terre (*eretz*) — le sol habitable, posé sur les eaux primordiales souterraines (*tehom*). Plus bas encore, le **She'ol** — le domaine des morts dans le silence et l'attente, où descend tout mort (introduit en *Toledot Adam ve-Chavah*).

**Au milieu** — l'espace habitable — l'atmosphère dans laquelle vivent les hommes et les créatures ailées.

**Au-dessus** — la Voûte (*raqia*) / les Cieux (*shamayim*) — surface solide qui sépare l'espace habitable des eaux supérieures. Dans la Voûte sont enchâssés les luminaires comme des lampes dans un plafond.

**Au-dessus de la Voûte** — les eaux supérieures — l'océan céleste retenu par la Voûte. Quand il pleut, ce sont ses écluses qui s'ouvrent (*Bereshit* 7:11).

**Structure de gouvernance cosmique :**
- Les luminaires (*me'orot*) gouvernent le temps — les domaines temporels
- L'être humain (*adam*) gouverne le vivant — les domaines vivants
- Ensemble ils couvrent la totalité de la gouvernance cosmique déléguée par Elohim

---

## 7. PASSAGES À TRAITER OBLIGATOIREMENT AVEC L'AUTEUR

Ces passages introduisent des concepts nouveaux majeurs ou des décisions qui engagent tout le projet. Claude Code ne doit pas les traiter en autonomie.

### PRIORITÉ ABSOLUE

***Bereshit* 2:4-25** — Le second récit de création
- Introduction de *YHWH Elohim* — décision capitale sur le Nom divin
- *Yatsar* vs *bara* — la création matérielle de l'homme
- L'Eden comme Temple cosmique
- La femme — *isha* et *ish*, *ezer kenegdo*
- Le premier mariage comme union fonctionnelle

***Bereshit* 3** — La rupture fonctionnelle
- Le serpent — *nachash*
- La Chute comme dysfonction cosmique, pas comme péché moral
- Les malédictions comme réorganisations fonctionnelles

***Shemot* 3:1-15** — Le Nom divin YHWH
- *Ehyeh asher ehyeh* — "Je suis ce que je suis / Je serai ce que je serai"
- Décision sur comment rendre YHWH dans tout l'ONT — **décision la plus importante du projet après Elohim**

***Shemot* 20 / *Devarim* 5** — Les Dix Paroles
- *Dibrot* — non pas "commandements" mais "paroles/déclarations"
- Chaque parole dans son contexte fonctionnel

***Tehilim*** — Registre poétique
- Le parallélisme hébraïque — règles de traduction spécifiques
- Le *lament* (*qinah*) — structure poétique de lamentation
- Premier Psaume à traiter ensemble pour établir les conventions poétiques

***Yeshayahu* 40-55** — Le Deutéro-Yeshayahu
- *Eved YHWH* — le Serviteur d'Elohim
- *Go'el* — le Rédempteur fonctionnel

***Iyov*** — Le problème de la souffrance
- Le Conseil Divin (*ha-satan* comme fonction, pas comme nom propre)
- Le tourbillon — réponse d'Elohim

### PRIORITÉ HAUTE

***Bereshit* 6-9** — Le déluge
- *Berith* — l'alliance comme structure fonctionnelle
- *Nephilim* — décision de traduction
- La géographie fonctionnelle du déluge

***Bereshit* 12, 15, 17** — Avraham
- *Berith* — développement de l'alliance
- *Emunah* — la foi comme fidélité fonctionnelle (non pas croyance intellectuelle)

***Vayiqra*** — Le système sacrificiel
- Tout le vocabulaire du sacrifice comme système fonctionnel
- *Kaphar* — l'expiation fonctionnelle

### BRIT HADASHAH — PRIORITÉ ABSOLUE

***Yohanan* 1:1-18** — Le Prologue
- *En archē ēn ho Logos* : lire *Logos* comme **davar** (Bereshit 1), non comme le *Logos* de Philon d'Alexandrie — décision terminologique capitale pour tout Yohanan

***Gevurot ha-Neviim* 2** — La Pentecôte
- Le *ruach* sur les disciples : écho direct de *Bereshit* 1:2 et 2:7 — décision terminologique sur la continuité cosmique

**Les *Igerot* de Shaul** — *Tsedaqah* et *emunah*
- Toutes les traductions existantes rendent *tsedaqah* par "justice" ou "justification" (catégorie grecque *dikaiosyne*) — l'ONT maintient **tsedaqah** intraduisible. Décision terminologique à confirmer systématiquement.

***Igeret HaIvrim*** — Lettre aux Hébreux
- Entièrement construite sur le système de *Vayiqra* — ne pas traiter avant que *Vayiqra* soit fondé
- *Kaphar* / *kippurim* — l'expiation fonctionnelle au centre de l'argumentation

***Machazeh Yohanan*** — Apocalypse
- Dense en références à Yehezqel, Daniel et 1 Khanokh — ne pas traiter avant que ces textes soient au moins partiellement fondés dans l'ONT
- Le Conseil Divin, les quatre vivants (*chayot*), la *kavod* de YHWH — vocabulaire déjà posé mais à réactiver dans ce registre

---

## 8. PASSAGES QUE CLAUDE CODE PEUT TRAITER EN AUTONOMIE

Ces passages utilisent le vocabulaire déjà fixé dans des contextes déjà traités.

### AUTONOMIE COMPLÈTE

- **Les généalogies** (*Bereshit* 5, 10, 11, 36, etc.) — formules répétitives, vocabulaire fixé
- **Les récits narratifs post-*Bereshit* 3** qui réutilisent le vocabulaire déjà posé
- **Les formules de bénédiction** (*barakh*) — vocabulaire fixé
- **Les formules d'alliance répétitives** une fois *berith* traité avec l'auteur
- **Les récits de déplacement et d'installation** — *va'yiqra*, *va'yelekh*, etc.

### AUTONOMIE AVEC PRUDENCE

Traiter en autonomie mais signaler à l'auteur tout mot nouveau ou décision conceptuelle rencontrée :
- ***Mishlei*** — sagesse fonctionnelle, une fois le registre établi
- ***Ruth* et *Esther*** — récits narratifs avec vocabulaire connu
- **Les récits des *Melakhim*** — narratifs, mais signaler tout nouveau terme royal ou institutionnel

---

## 9. MARCHE À SUIVRE POUR CHAQUE VERSET

### Étape 1 — Identifier les mots clés
Repérer dans le texte hébreu :
- Les mots du glossaire fixé (section 3)
- Les mots nouveaux non encore traités
- Les figures de style hébraïques (mérisme, parallélisme, chiasme, ellipse)

### Étape 2 — Vérifier le contexte
- Est-ce que ce passage renvoie à une cosmologie voisine à démythologiser ?
- Est-ce qu'un mot nouveau est porteur d'un concept fondamental ?
- Y a-t-il un changement de verbe significatif (*bara* vs *asah* vs *yatsar*) ?

### Étape 3 — Forger la traduction
- Corps du texte : fidèle à l'hébreu, sobre, sans interpolation
- Gloses : explicitation de l'implicite hébreu — jamais d'invention
- Termes hébreux : (translittération / הָעִבְרִית)

### Étape 4 — Vérifier la cohérence
- La traduction est-elle cohérente avec le glossaire ?
- Les formules fixes sont-elles respectées ?
- Le lecteur occidental comprend-il sans connaître l'hébreu ?

---

## 10. CE QUE L'ONT N'EST PAS

- Ce n'est pas une traduction littéraliste mot à mot
- Ce n'est pas une paraphrase libre
- Ce n'est pas une traduction confessionnelle (ni protestante, ni catholique, ni juive)
- Ce n'est pas une réfutation d'autres traductions — l'ONT affirme, il ne polémique pas
- Ce n'est pas une imposition de théologie moderne sur le texte ancien

L'ONT est une restitution de ce que le texte hébreu disait à ses lecteurs originaux — en rendant visible pour le lecteur français ce qui était invisible parce qu'implicite.

---

## 11. ORDRE CANONIQUE DES LIVRES DANS CHAQUE MODE

→ Voir **`corpus-order.md`** à la racine du projet : numérotation globale 01-70, ordre détaillé par mode, structure des Igerot (fracture du Ḥurban), note sur *Tsava'at Lévi*.

---

## 12. FONDATIONS DE RÉFÉRENCE

Les Fondations verrouillées sont la référence stylistique et terminologique absolue de l'ONT. Consulter ces fichiers pour vérifier la cohérence de toute nouvelle traduction.

**Deux états, deux dossiers — le flux de validation.** Un texte vit d'abord dans `brouillons/` tant qu'il porte la mention « à valider » (rédigé, en attente de la relecture de l'auteur — voir §7). `brouillons/` **miroite exactement** l'arborescence de `locked/` (même chemin *Kenesset → mode → livre*), afin qu'une validation soit un simple déplacement vers le chemin identique. Quand l'auteur valide, le fichier **passe de `brouillons/` au chemin identique dans `locked/`**, et son pied passe de « à valider » à « Version X — verrouillée ». Seuls les fichiers de `locked/` font référence ; `brouillons/` **ne voyage pas** dans la distribution (comme `context/` — seuls l'intro et les chapitres verrouillés d'un slot sont distribués).

**Chapitres actuellement en `brouillons/`** (non encore verrouillés — pour ceux-ci, lire `brouillons/…` et non `locked/…`, malgré les chemins de la liste ci-dessous) : *Bereshit* 1, 2, 7, 13, 14 (en révision ; *Bereshit* 2 et 7 attendent le traitement §7 de la *Neshamah*) et *Bereshit* 19 (à valider).

- **Bereshit 1** (Genèse 1:1 — 2:3) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-1.md` — référence fondatrice : toutes les conventions typographiques, le glossaire en action, les formules fixes. Toute traduction doit être cohérente avec elle.
- **Bereshit 2** (Genèse 2:4-25) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-2.md` — introduction de YHWH Elohim, *yatsar*, l'Eden comme Temple, *isha* / *ish*, *ezer kenegdo*, la *neshamah*.
- **Bereshit 3** (Genèse 3) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-3.md` — la rupture fonctionnelle, le *nachash*, les réorganisations cosmiques, *itsavon*, *arur*.
- **Bereshit 4** (Genèse 4) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-4.md` — Qayin et Hevel, *minchah*, *chattah*, *arur*, la ligne de Qayin.
- **Bereshit 5** (Genèse 5) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-5.md` — généalogie d'Adam à Noach, *toledot*, *hithalekh*, Khanokh.
- **Bereshit 6** (Genèse 6) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-6.md` — les Nephilim, la *berith* inaugurale, l'arche (*tevah*).
- **Bereshit 7** (Genèse 7-8) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-7.md` — le déluge, décréation et re-création, *tahor/lo tahor*, *olah*, *qallel*, *kavod*.
- **Bereshit 8** (Genèse 9:1-17) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-8.md` — la re-création après le *mabbul*, la *berith* noachide, *adam* intraduisible à partir d'ici, *olam*. (L'*olah* de Noach, Gn 8:20, est traitée en Bereshit 7, qui couvre Gn 7-8.)
- **Bereshit 9** (Genèse 9:18-29) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-9.md` — l'incident de la vigne, *ish ha'adamah*, *galah*, *arur* sur Kena'an, dotations de Shem et Yaphet, *shakan* (ambiguïté du sujet maintenue).
- **Bereshit 10** (Genèse 10:1-32) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-10.md` — table des nations, *toledot* des fils de Noach, Nimrod (*gibor*, écho des Nephilim), *mamlakhah*, *lifnei YHWH* (ambiguïté maintenue), Ever / *ivri*, Peleg / *palag*.
- **Bereshit 11** (Genèse 11:1-32) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-11.md` — tour de Bavel, *safah* / *balal* / Bavel (polémique étymologique contre Bab-ilim), *hadal* vs *shavat*, toledot de Shem jusqu'à Terah, *aqarah* (stérilité de Sarai), Haran personne / Haran ville (homonymie délibérée).
- **Bereshit 12** (Genèse 12:1-20) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-12.md` — *lekh-lekha* (ambiguïté maintenue), promesse à Avraham, *vayera* (mode de la révélation aux patriarches), *zera* (premier emploi dans la promesse), *niverekhu* (passif ou réflexif — ambiguïté maintenue), descente en Égypte, *nega'im* (écho de Shemot).
- **Bereshit 13** (Genèse 13:1-18) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-13.md` — retour au Négev et à Bet-El, séparation d'Avram et Lot, *riv* (conflit pastoral), *kikar* (bassin du Yarden), *miqqedem* (mouvement vers l'orient comme éloignement fonctionnel), renouvellement de la promesse aux quatre horizons, *hithalekh ba'arets*, Hevron comme premier ancrage durable.
- **Bereshit 14** (Genèse 14:1-24) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-14.md` — guerre des rois, capture et délivrance de Lot, Malki-tsedeq roi-**kohen** de Shalem, **El Elyon** (premier emploi — intraduisible), **kohen** (intraduisible dès ici), *tsedeq* (l'ordre juste), *qoneh shamayim va'arets*, *ha-ivri* (double étymologie maintenue), *ba'alei berit*, *ma'aser* (ambiguïté du sujet maintenue), identification **YHWH**-**El Elyon** par Avram (v.22).
- **Bereshit 15** (Genèse 15:1-21) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-15.md` — *berith bein habetarim*, **emunah** (intraduisible — verbe *he'emin* rendu "**emuna**"), **tsedaqah** (premier emploi — forme nominale de *tsedeq*), **tsadiq** (déjà posé en Bereshit 6:9), *machazeh* (vision intérieure, distinct de *vayera*), *tardemah* (écho délibéré de Bereshit 2:21), *ger* (premier emploi — étranger résident sans droits), *avon* (premier emploi — torsion structurelle, distinct de *chata* et *ra*), *berith* unilatérale confirmée (seul **YHWH** passe entre les morceaux), prophétie de l'exil et ambiguïté 400 ans / quatrième génération maintenue.
- **Bereshit 16** (Genèse 16:1-16) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-16.md` — **mal'akh** **YHWH** (premier emploi — intraduisible, ambiguïté délibérée entre le **mal'akh** et **YHWH** maintenue), **El Roï** (premier emploi — unique dans toute la Bible, donné par Hagar), Hagar (*ger* sans droits — première occurrence d'un personnage non-hébreu central), Ishma'el ("El entend"), Beer-lachai-roi, *shiphchah* vs *amah*, ambiguïté de *acharei ro'i* (v.13b — trois lectures maintenues sans résolution).
- **Bereshit 17** (Genèse 17:1-27) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-17.md` — **El Shaddai** (premier emploi — accompagne les moments où **YHWH** accomplit l'impossible humain), **milah** (premier emploi — l'inscription covenantale dans la chair), **orlah** / **arel** (premier emploi — portée métaphorique large : cœur, lèvres, fruit), **goyim** / **goy** (actif dans la promesse : *av hamon goyim*), Avram → Avraham / Sarai → Sarah (reformulation des **Shem** covenantaux : possessif particulier → souverain universel), *tamim* = "intègre" (cohérence avec Noach en *Bereshit* 6:9), *karet* (retranchement du peuple — sanction la plus grave du droit divin), formule covenantale *lihyot lekha l'Elohim* (v.7 — le nom cosmique comme engagement de relation personnelle).
- **Bereshit 18** (Genèse 18:1-33) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-18.md` — **mishpat** / **mishpatim** (premier emploi — l'acte de jugement concret dans l'ordre cosmique ; *tsedaqah umishpat* posé en v.19), **rasha** / **resha'im** (premier emploi — opposé fonctionnel de **tsadiq**, paire constitutive du droit divin hébraïque), **shofet** / **shoftim** (premier emploi — même racine que **mishpat** ; *shofet kol ha'arets* titre de souveraineté cosmique universelle ; écho vers le livre *Shoftim*), ambiguïté des trois **ish** maintenue (jamais nommés **mal'akhim** dans ce texte — titre donné seulement en *Bereshit* 19:1), *ze'aqah* (cri judiciaire de l'opprimé — déclenche la descente du **mishpat**), intercession 50→10 (Avraham demande un **mishpat** complet, non sa suspension).

---

## 13. CHANTIERS OUVERTS — À TRANCHER PAR L'AUTEUR

*Relevé par le pipeline de La Bible ONT (`/Users/gloiiire_/ONTBible/ONTBibleApp`), qui contrôle à chaque construction que tout `**terme**` a bien son entrée de glossaire. Le rapport complet vit dans `dist/report.md` de ce dépôt.*

### 13.1 Neuf termes balisés sans entrée de glossaire

Chacun est actuellement écrit `**...**`, donc **déclaré intraduisible** — mais absent du §3. Conséquence dans l'app : le mot s'affiche en or, le lecteur le touche, et il n'y a pas de fiche.

Pour chacun, **deux issues et deux seulement** :

- **A —** c'est un vrai intraduisible : lui écrire une entrée au §2.5 et au §3, il garde `**...**` ;
- **B —** ce n'est pas un intraduisible : le passer en `==...==` (§2.5 bis), il devient un *terme important*.

| terme | occurrences | premier emploi | remarque |
|---|---|---|---|
| `tsadiqim` | 9 | *Bereshit* 18:24 | pluriel de **tsadiq**, déjà au §3 — sans doute une forme dérivée à rattacher |
| `tsedaqah umishpat` | 1 | *Bereshit* 18:19 | construit de deux termes déjà au §3 |
| `chata'ah` | 1 | *Bereshit* 18:20 | proche de *chattah* (Bereshit 4) |
| `nashim` | 1 | *Bereshit* 6:2 | pluriel d'*ishah* |
| `shiphchah` | 1 | *Bereshit* 16 | déjà discuté dans la note de Bereshit 16, jamais fixé au §3 |
| `Tov vara` | 1 | *Bereshit* 2:6 | **tov** est au §3, *ra* non |
| `gibborim` | 1 | *Sefar Gibbaraya* 8:2 | pluriel de `gibor` |
| `gibor` | 1 | *Sefar Gibbaraya* 3:36 | singulier — une seule entrée pour les deux |
| `shaliachim` | 2 | *Sefar Gibbaraya* intro | **le §2.5 donne `shlichim`** — deux orthographes du même mot dans le corpus |

`tsadiqim` est le plus rentable : neuf occurrences, et le terme est déjà au glossaire au singulier.

### 13.2 Vingt-deux marqueurs déséquilibrés

Des `**` ouverts sans être refermés, dans les pieds de page de *Bereshit* 15 à 19. Le pipeline les recolle silencieusement, mais le rendu Affinity et le rendu de l'app peuvent diverger. `dist/report.md` les localise à la ligne.

### 13.3 Déjà fait — ne pas refaire

Onze balises `**...**` posées pour insister, et non pour déclarer un intraduisible, ont été converties en `==...==` le 12 août 2026 : `« Jour »`, `« Nuit »`, `« Cieux »`, `« Mers »`, `« Terre »` (*Bereshit* 1), `Chavah` (3:20), `Noach` (5:29), `Sarah` (17:15), et trois métadonnées d'apparat dans *Bereshit* 19.
