# ONT — ONTOLOGIE NOUVELLE TRADUCTION
## DOCUMENT DE RÉFÉRENCE COMPLET POUR LA TRADUCTION AUTONOME

> ## À faire à la fin de **chaque** travail, sans exception
>
> Ce dépôt est l'un de ceux d'un même projet, rangés côte à côte sous
> `~/ONTBible/` — avec `ONTBibleApp` (le pipeline, la liseuse iOS, le backend)
> et `ONTBibleWebapp` (`ontbible.com`). La racine porte son propre
> `CLAUDE.md`, qui se charge aussi ici : **ouvrir les sessions depuis
> `~/ONTBible/`**, les voisins sont alors visibles.
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

L'ONT est une traduction et reconstruction françaises du **corpus hébreu et araméen antique** fondées sur **l'ontologie hébraïque antique fonctionnelle**. Elle a été fondée et est dirigée par son auteur — **Shaʾeliel** (שָׁאַל + אֵל : celui qui interroge Elohim jusqu'à ce que le réel rende ce qu'il cache) — en collaboration avec Claude comme co-traducteur. Voir `context/auteur.md`.

**Le principe fondamental :** Dans le monde hébreu antique, une chose n'existe pas parce qu'elle a une substance matérielle, mais parce qu'elle a une **fonction assignée, un nom, un rôle dans un système ordonné**. Créer ne signifie pas fabriquer de la matière — cela signifie ordonner, nommer, attribuer un rôle, inaugurer un espace fonctionnel. Le cosmos hébreu n'est pas une usine, c'est un Temple.

**Architecture du corpus — la Kenesset (כְּנֶסֶת) :**

Le corpus hébreu et araméen de l'ONT est nommé **Kenesset** (כְּנֶסֶת) — "le rassemblement, l'assemblée." Acronyme des quatre modes : **כ** (Ketouvim) + **נ** (Neviʾim) + **ס** (Nistarot — racine *satar* סָתַר) + **ת** (Torah) = כְּנֶסֶת. Remplace "Tanakh" comme nom du corpus dans l'ONT : Tanakh désignait les trois modes canoniques (Torah/Neviʾim/Ketouvim) ; Kenesset désigne les quatre modes fonctionnels incluant les Nistarot. Distinct de la *Berit Hadashah* qui est son propre corpus.

Le corpus est structuré en quatre catégories fonctionnelles. Ce ne sont pas des divisions canoniques — ce sont des modes distincts d'engagement avec le réel. Le critère est ontologique : si la distinction fonctionnelle est réelle, elle mérite un nom (*qara*).

| Catégorie | Mode ontologique | Fonction |
|---|---|---|
| **Torah** | *Institution* | La Torah constitue le réel — *bara*, *qara*, *natan*. Le cosmos passe du *tohu vavohu* à l'ordre fonctionnel. La Torah est l'acte par lequel le réel devient réel. |
| **Neviʾim** | *Lecture dans l'histoire* | Le navi lit l'alliance dans le temps visible et prononce le *mishpat* — discernement de l'alignement ou désalignement covenantal. Problème toujours national : Israël ↔ alliance ↔ terre ↔ roi ↔ Temple. |
| **Ketouvim** | *Habitation intérieure* | Là où le cosmos constitué (Torah) et lu (Neviʾim) rencontre l'être humain dans son expérience concrète. Job souffre, les Tehilim crient, Qohelet interroge, Ruth agit. Mode d'intériorité et de réponse vécue. |
| **Nistarot** | *Traversée architecturale* | De *satar* (סָתַר) : structurellement voilé. *Deutéronome* 29:28 : *hanistarot laYHWH Eloheinu* — les choses cachées appartiennent à YHWH. Les Nistarot révèlent les structures invisibles derrière l'histoire : hiérarchies célestes, conseil divin, temps comme structure cosmique, puissances derrière les empires. Mode vertical — l'architecture du réel que le regard ordinaire ne traverse pas. |

**Textes-charnières Neviʾim / Nistarot :** Yehezqel (merkavah ch. 1, Temple cosmique ch. 40-48), Zekharyah 1-8 (visions nocturnes avec médiateur angélique), Yeshayahu 24-27 (jugement cosmique), Daniel 7-12 (visions architecturales, *qetz*). Ces textes restent dans les Neviʾim — ils sont des portes, pas des résidents des Nistarot.

**Nistarot — jamais "Giluyim"** : *Giluy* / *galah* (גָּלָה) est un calque rabbinique tardif du grec *apokalupsis* — rejeté. Le terme natif est *nistarot* (Deutéronome 29:28), utilisé par la communauté de Qumrân elle-même pour désigner les réalités voilées révélées aux *maskilim*.

**Périmètre du corpus :** L'ONT ne se limite pas à la Bible canonique — le "canon" est une construction tardive (IVe siècle et après) qui n'existait pas à l'époque de la rédaction des textes. Le projet travaille sur l'ensemble de la bibliothèque d'un Juif lettré du Second Temple : textes canoniques ET pseudépigraphiques. **Critère d'inclusion :** tout texte en hébreu ou araméen antique qui illumine le cosmos hébreu depuis l'intérieur. **Critère d'exclusion :** tout texte qui a absorbé des catégories hellénistiques (grecques), même s'il est d'auteur juif — Philon d'Alexandrie, *Sagesse de Salomon*, 4 Maccabées. Le filtre n'est pas canonique, il est ontologique : est-ce que le texte pense en hébreu ou en grec ? La distinction canon/apocryphe n'existe pas dans l'ONT.

**Répartition du corpus étendu dans les quatre catégories :**

*Ketouvim* (mode d'habitation intérieure) : *Tehilim*, *Mishlei*, *Iyov*, *Shir Hashirim*, *Ruth*, *Qohelet*, *Esther*, *Ezra-Nehemyah*, *Divrei Hayamim*, *Toledot Adam ve-Chavah* (Vie d'Adam et Ève — mode narratif/expérientiel dominant ; cas limite à réévaluer), *Sefar Gibbaraya* (Livre des Géants — les *gibbaraya* pris dans le drame cosmique cherchant à interpréter leurs rêves ; même structure que Iyov : mode expérientiel, pas architectural).

*Torah* (mode d'institution) — corpus étendu : *Yovelim* (Jubilés) — retelling normatif et législatif de Bereshit-Shemot ; les tablettes célestes et le médiateur angélique sont des dispositifs d'autorité Torah-niveau, non un contenu de traversée architecturale. Yovelim institue et ordonne — il emprunte l'épistémologie Nistarot sans en être.

*Nistarot* (mode de traversée architecturale) : *Daniel*, *1 Chanokh*, *Chazon Avraham* (Apocalypse d'Abraham), *Chazon Ezra* (2 Ezra — ch. 3-14 uniquement ; ch. 1-2 et 15-16 sont des additions chrétiennes hellénisées exclues), *Chazon Barukh* (Apocalypse de Baruch — syriaque, original hébreu probable), *Tsavaʾat Lévi* (Testament de Lévi araméen de Qumrân — pas les Testaments des 12 Patriarches dans leur ensemble, trop christianisés).

**Terminologie ONT pour les textes de vision :** *chazon* (חָזוֹן — vision prophétique reçue, terme natif du Second Temple : Daniel 7:1, 8:1 ; titres de Yeshayahu, Ovadyah, Nahum, Havaquq) pour tous les textes de vision SAUF le *Machazeh Yohanan* qui garde *machazeh* (מַחֲזֵה) — décision délibérée pour créer l'écho avec *Genèse* 15:1 (*bamachazeh*) : la vision inaugurale de la *berith* et la vision finale du cosmos racheté dans la même modalité. Ne pas utiliser *giluy* (hébreu rabbinique tardif, calque du grec *apokalypsis*) — le terme natif est *chazon*.

**Extension *Berit Hadashah* :** L'ONT inclut également la *Berit Hadashah* (בְּרִית חֲדָשָׁה) — titre tiré de *Jérémie* 31:31, non pas le "Nouveau Testament" de la tradition latine tardive. Le même critère ontologique s'applique : lus à travers le prisme de l'ontologie hébraïque antique fonctionnelle, ces textes font apparaître la même structure cosmique hébraïque — *davar* performatif, *berith*, *tsedaqah*, *ruach*, *kavod*.

**Structure fonctionnelle de la *Berit Hadashah* — quatre modes parallèles à la Kenesset :**

| Mode | Corpus *Berit Hadashah* | Fonction parallèle |
|---|---|---|
| **Besorot** (la Fondation — Évangiles) | **Besorot** (בְּשׂוֹרוֹת) — *besorah* : annonce royale d'un acte accompli. Subdivisées en *Eduyot* (*Marqus*, *Matityahu*, *Luqas* — trois témoins au sens de *Deutéronome* 19:15) et *Bereshit ha-Yohanan* (séparée — *besorah* cosmique-inaugurale, écho de *Bereshit* 1) | Institue qui est Yeshua — fondation cosmique, *davar* inaugurale |
| **Neviʾim** | **Igerot** (אִגְּרוֹת) — lettres adressées, *devarim* fonctionnels | Confrontation covenantale depuis la position du *mishpat* — lecture de l'alignement/désalignement des communautés dans la *berith* |
| **Ketouvim** | **Gevurot ha-Neviʾim** (גְּבוּרוֹת הַנְּבִיאִים) — les *gevurot* de **YHWH** accomplies *à travers* ses *neviʾim* | Chronique narrative des actes de puissance de **YHWH** dans l'histoire — mode expérientiel et testimonial |
| **Nistarot** | **Machazeh Yohanan** (מַחֲזֵה יוֹחָנָן) — même terme qu'en *Genèse* 15:1, dans la lignée de Yehezqel, Daniel et 1 Chanokh | Traversée architecturale — les structures invisibles derrière l'histoire, le cosmos racheté |

**Note terminologique — *navi* / *shaliach* : une seule réalité fonctionnelle.** Tout *navi* authentique est structurellement un *shaliach* et tout *shaliach* accomplit la fonction du *navi* — ils ne sont pas deux catégories analytiquement distinctes. La décomposition *navi* / *shaliach* / *evangeliste* / *pasteur* / *enseignant* (Éphésiens 4:11) est une décompression grecque d'une réalité hébraïque unifiée. Ne jamais traiter ces termes comme des fonctions mutuellement exclusives dans l'ONT.

**Pourquoi *Gevurot ha-Neviʾim* et non *Maʿasim HaShlichim*.** *Gevurot* (de *gavar* גָּבַר — être puissant, l'emporter) : les actes de puissance de **YHWH** — **YHWH** est le sujet grammatical, les *neviʾim* sont l'instrument. *Maʿasim* (de *asah* — faire) avec *ha-shlichim* (les envoyés) : les actes des *shlichim* — les humains comme sujets grammaticaux. La première formulation est hébraïque-fonctionnelle (*gevurot* appartient au vocabulaire de la puissance divine dans les *Tehilim* et les *Neviʾim*) ; la seconde importe la catégorie grecque de l'*apostolos* comme agent autonome.

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

**Règle absolue — numérotation interne :** Chaque **parashah** (Bereshit N, Shemot N, etc.) repart toujours de ¹, quel que soit le numéro de verset biblique auquel elle commence. Si une **parashah** couvre Genèse 9:18-29, ses versets sont numérotés ¹ à ¹² — jamais ¹⁸ à ²⁹. De même, si un nouveau chapitre biblique commence au milieu d'une **parashah**, sa numérotation repart de ¹ à ce moment-là. Les numéros de versets bibliques ne sont jamais transposés dans l'ONT — ils figurent uniquement dans le sous-titre de référence *(Genèse / בְּרֵאשִׁית X:X-X)*.

### 2.3 Structure des chapitres

Les chapitres de l'ONT sont des **unités fonctionnelles** — un bloc se clôt quand une fonction cosmique est accomplie, pas quand un numéro de chapitre biblique change. Les numérotations de chapitres bibliques (introduites par le cardinal Stephen Langton au XIIIe siècle) sont des divisions administratives médiévales — souvent arbitraires. L'ONT les ignore au profit de la cohérence fonctionnelle.

**Exemple appliqué :** *Genèse* 2:1-3 appartient fonctionnellement à la Fondation 1 (*Bereshit* 1) — c'est le couronnement du récit d'orchestration cosmique, pas le début d'un nouveau récit.

**Le mot « chapitre » devient faux, et c'est pourquoi les liseuses offrent les deux registres.** Décision de l'auteur du 25 août 2026 : *quand une **parashah** ne recouvre pas les mêmes chapitres que les traductions habituelles, c'est « **parashah** » le mot juste.* Nommer « Chapitre 7 » une unité qui couvre *Bereshit* 7 et 8 n'est pas une approximation de confort — c'est un intitulé qui ment sur ce que le lecteur a sous les yeux, et qui l'enverra chercher dans sa Bible un découpage que l'ONT n'a pas.

Le réglage *Chapitre* / *Parashah* de l'app et du site n'est donc pas une préférence de registre. C'est une **béquille** : « Chapitre » permet d'avancer avant de savoir, et cesse d'être exact dès que l'unité s'écarte du découpage reçu. La fiche `lexique/parashah.md` porte l'explication que le lecteur reçoit ; la présente règle porte celle qui engage le traducteur.

### 2.4 Formules fixes

**Formule d'accomplissement :** "Et il advint, et demeura conformément à ce qui avait été formulé" (*vayehi khen* / וַיְהִי-כֵן)

**Formule d'évaluation divine :** "Et Elohim examina et constata que c'était **tov**" (*vayar / ki tov* / וַיַּרְא כִּי-טוֹב)

**Formule du soir et du matin :** "Il y eut un soir (*ʿerev* / עֶרֶב), puis un matin (*boqer* / בֹּקֶר) — ce fut le [N]e jour (*yom* / יוֹם)"

**Exception Jour Un :** "ce fut le Jour Un (*yom ʾechad* / יוֹם אֶחָד)" — avec majuscules, car *echad* est le cardinal "un" pas l'ordinal "premier".

### 2.5 Marquage des termes intraduisibles — convention Affinity Publisher

**Règle absolue :** Tout terme intraduisible doit être entouré de `**...**` dans les fichiers .md. Ces marqueurs permettent à Affinity Publisher de détecter automatiquement ces termes et d'appliquer le style typographique "Transliteration" lors du copier-coller.

**Cette règle s'applique partout** : corps de la traduction (niveau 1), gloses (niveau 2), et notes de bas de section. Elle ne s'applique PAS à l'intérieur des translittérations de niveau 3 `(*terme* / הֵבְרִי)` — le terme y est déjà balisé.

**Liste complète des termes à baliser :**
- `**ʾElohim**` / `**ʾelohim**`
- `**YHWH**`
- `**Ruach**` / `**ruach**`
- `**Nefesh**` / `**nefesh**`
- `**Neshamah**` / `**neshamah**`
- `**ʾishah**` / `**ʾIshah**` et formes dérivées : `**ʾishto**`, `**ʾeshet**`, `**neshei**` (pluriel construit), `**nashim**` (pluriel absolu)
- `**ʾish**` / `**ʾIsh**` et formes dérivées : `**ʾanashim**` (pluriel absolu), `**ʾanshei**` (pluriel construit) — **RÈGLE DE DÉDUCTION : toute forme dérivée d'un terme intraduisible est elle-même intraduisible. Ne jamais rendre *anashim* par "hommes".**
- `**Shem**` / `**Shemot**` (pluriel) quand c'est le concept — lowercase `**shem**` toujours ; uppercase `**Shem**` quand précédé de "le / son / leur / du / des / ce / un / ton / mon" ou suivi d'une translittération minuscule
- `**kavod**` / `**Kavod**`
- `**Tahor**` / `**tahor**` / `**lo tahor**`
- `**ʿOlah**` / `**ʿolah**` / `**ʿOlot**` / `**ʿolot**`
- `**L'Être façonné du sol**` / `**l'Être façonné du sol**` (Bereshit 1-7 ; et tout récit en régime antédiluvien, avant le **mabbul** — ex. *Sefar Gibbaraya*). ==Ne vise que le générique== *ha-adam* / *benei ha-adam* (l'humanité). Le ==nom propre== Adam d'un individu (le personnage, ex. *Toledot Adam ve-Chavah*) reste un ==nom propre== (§4.12) — ni traduit, ni balisé.
- `**ʾadam**` (Bereshit 8 et suivants)
- `**mabbul**` — terme technique du déluge de Noach, utilisé sans traduction française dans le corps du texte à partir de Bereshit 8
- `**nacham**`. Premier emploi *Genèse* 5:29.
- `**ʾAdonai**` — s'écrit seul ou combiné : `**ʾAdonai** **YHWH**`. Premier emploi *Genèse* 15:2.
- `**ʾEl**` — intraduisible depuis le 31 août 2026 : le nom du dieu au sommet de l'ordre (אֵל), au singulier. **Se balise aussi dans les gloses qui expliquent un Shem théophore** — « **ʾEl** entend » pour Yishmaʿel, « qui est comme **ʾEl** ? » pour Mikhaʾel, « **ʾEl** guérit » pour Rafaʾel : c'est le même **ʾEl**, et le lecteur doit pouvoir le toucher là où il le rencontre. ==Ne pas baliser== la particule à l'intérieur d'une translittération de niveau 3 — `(*ʾel* / אֵל)` la porte déjà —, ni les composés qui ont leur propre entrée : `**ʾEl ʿElyon**`, `**ʾEl Roï**`, `**ʾEl Shaddai**`.
- `**YHWH Elohim**` — deux mots, les deux en gras. La formule de *Bereshit* 2-3,
  où elle paraît vingt fois de suite puis presque plus jamais dans la Torah : celui
  qui a ordonné le cosmos est celui qui parle à cet homme-là. ==Ne pas anticiper le
  traitement de **YHWH**==, que le §7 réserve à *Exode* 3:1-15.
- `**ʾEl ʿElyon**` — deux mots, les deux en gras. Combiné : `**YHWH** **ʾEl ʿElyon**`. Premier emploi *Bereshit* 14.
- `**ʾEl Roï**` — deux mots, les deux en gras. Premier emploi *Genèse* 16:13.
- `**Kohen**` / `**kohen**` / `**kohanim**` / `**kohen gadol**`. Premier emploi *Genèse* 14:18.
- `**malʾakh**` / `**malʾakhim**` — combiné : `**malʾakh** **YHWH**`. Premier emploi *Genèse* 16:7.
- `**shaliach**` / `**shlichim**`
- `**shifchah**` / `**shefachot**` (pluriel) — la servante attachée à la sphère d'une **ʾishah**, distincte de l'*amah* (servante d'un **ʾish**). Premier emploi *Genèse* 16:1.
- `**ʾemunah**` / `**ʾEmunah**` (nom) — forme verbale : `**ʾemuna**` (sans h — délibéré, ne pas corriger). Premier emploi *Genèse* 15:6.
- `**tsedaqah**` / `**tsedaqah umishpat**` — le construit apparié, couple constitutif du droit divin, déclaré ici comme **yirat YHWH** l'est sous **yirah**. Premier emploi *Genèse* 15:6.
- `**berith**` / `**Berith**` — intraduisible depuis le 8 septembre 2026 : la structure d'engagement (בְּרִית). Non « alliance », qui suggère un contrat entre égaux : la **berith** de *Bereshit* 15 est ==unilatérale== — **YHWH** seul passe entre les morceaux, et Avraham dort. Elle ne se conclut pas, elle se ==fait tenir debout== (*meqim*, de *qum*), et c'est pourquoi elle ne dépend pas de la fidélité de celui qui la reçoit. ==La pratique avait déjà tranché== : le corpus l'écrivait en gras 65 fois pour 59 « alliance », et le §3.2 disait encore l'inverse.
- `**tsedeq**` — intraduisible : l'ordre juste cosmique (צֶדֶק). Le §3.2 le déclarait déjà, ==sans que le §2.5 le liste== — donc le pipeline ne savait pas le résoudre et il sortait en or sans fiche. Oubli de liste corrigé le 8 septembre 2026. Ses trois dérivés y étaient, eux : **tsadiq**, **tsedaqah**, et le rendu du couple **tsedaqah umishpat**.
- `**tsadiq**` / `**tsadiqim**`. Premier emploi *Genèse* 6:9.
- `**rashaʿ**` / `**reshaʿim**`. Premier emploi *Genèse* 18:23.
- `**chesed**`. Premier emploi *Genèse* 19:19 ; traitement définitif (plus ample) réservé à son locus central — *Exode* 34:6-7 et *Ruth*.
- `**tov**` / `**tov meʾod**` / `**tov varaʿ**` / `**Tov varaʿ**` — le construit de l'arbre (*etz hadaʿat tov vara*, *Genèse* 2:9) : les deux graphies, car il ouvre parfois la phrase. Premier emploi *Genèse* 1:4.
- `**raʿ**` / `**raʿat**` / `**raʿim**`. Premier emploi *Genèse* 2:9.
- `**chataʾ**` — rater sa cible, manquer sa marque. ==Le premier verbe intraduisible de l'ONT== : décision du 25 août 2026, prise en connaissance du précédent qu'elle ouvre. Pendant exact de **raʿ** — **chataʾ** est l'acte, **raʿ** est l'état. Premier emploi *Genèse* 4:7.
- `**chattat**` / `**chataʾah**` / `**chataʾim**` — les formes nominales de **chataʾ** : le manquement devenu une chose qu'on peut nommer, et qui en *Genèse* 4:7 se tapit à la porte. Premier emploi *Genèse* 4:7.
- `**davar**` / `**devarim**` — combiné : "le **davar** de **YHWH**". Premier emploi *Genèse* 11:1.
- `**ʿirin**` — araméen : les éveillés, les gardiens (עִירִין). Jamais "Veilleurs". Pluriel uniquement dans les textes araméens (*Sefar Gibbaraya*, 1 *Chanokh*).
- `**gibbarayaʾ**` — araméen : les puissants, les démesurés (גבריא). Jamais "géants". Lien lexical avec les **gibborim** de *Genèse* 6:4.
- `**parashah**` / `**parashiot**` — intraduisible : la division native du texte hébreu (פָּרָשָׁה), faite d'un ==blanc== laissé par le scribe et non d'un numéro. De *parash* (פרש) — rendre distinct. La *petuhah* ouvre sur une ligne neuve, la *setumah* laisse neuf espaces au milieu de la ligne. Attestée dans les rouleaux de la mer Morte, donc ==mille ans avant== les chapitres de Stephen Langton (XIIIᵉ s.), qui sont posés *sur* le texte quand la **parashah** est *dans* le texte. C'est le nom ONT d'une unité — elle se ferme quand une fonction s'accomplit, comme un blanc de scribe. Jamais « chapitre » : voir §2.3.
- `**basar**` — intraduisible : la chair en tant qu'==existence incarnée, fragile et partagée== (בָּשָׂר). Non « chair » au sens moral que le français a pris — ce n'est ni le contraire de l'esprit ni le siège du désir : c'est ==ce par quoi on est un vivant parmi les vivants==, ce qui meurt et ce qui peut ressusciter. C'est ce qu'un **malʾakh** n'a pas, et c'est pourquoi il ne peut ni mourir ni transformer ce qui meurt. Premier emploi *Genèse* 2:23 (*basar mibesari*).
- `**qahal**` / `**Qahal**` — intraduisible : l'assemblée ==convoquée par une autorité== (קָהָל). De *qahal* — rassembler, convoquer. Non « assemblée » ni « communauté », qui laissent croire à une réunion qu'on décide : au **qahal** on ==est appelé==. C'est le mot du jour du [[Sinai]] (*Deutéronome* 9:10, *yom ha-qahal*), et c'est celui que le grec rendra par *ekklesia*.
- `**ʾechad**` — intraduisible : l'unité qui ==compose== (אֶחָד). Non « un » au sens du compte, et surtout pas l'unité qui exclut, qui se dirait *yachid* (יָחִיד). C'est le mot de *basar echad* en *Genèse* 2:24 — deux qui deviennent un sans cesser d'être deux — et c'est celui du *Shema*. Un fleuve unique dont les eaux coulent en plusieurs canaux : les canaux ne multiplient pas le fleuve. Premier emploi *Genèse* 1:5 (*yom echad*).
- `**kli**` / `**Kli**` / `**kelim**` — intraduisible : ==ce qui est apte à recevoir== (כְּלִי). De la racine כלה — contenir, mener à complétion. Non « vase » ni « récipient », qui disent un contenant passif qu'on remplit : un **kli** est ==constitué pour==, et son aptitude décide de ce qu'il peut recevoir. C'est le mot des ustensiles du Mishkan — *klei ha-qodesh*, mis à part non par leur matière mais par leur destination. Il commande toute la question de l'**ʿolam** : ce qui change le régime de perceptibilité n'est pas la chose regardée, c'est ==le **kli** qui regarde==. La **Ruach** ne se pose jamais sans lui — un **naviʾ**, une tente, un sol, un **qahal**. Pluriel `**kelim**`. Locus définitif *Shemot* 25-31, les **kelim** du Mishkan.
- `**chuqqah**` / `**Chuqqah**` / `**chuqqot**` — intraduisible : ==l'ordonnance permanente== (חֻקָּה). De *chaqaq* (חָקַק) — ==graver, inciser dans la pierre==. Non « loi » ni « décret » : ce qui est gravé ==tient de soi-même==, on ne le rediscute pas, et le reste s'y appuie. À distinguer du masculin *choq* (חֹק), qui est la prescription ==ponctuelle== — l'hébreu apparie souvent les deux. C'est le nom ONT des énoncés permanents du corpus, et le pluriel donne son nom au dossier.
  ==Un mot qui nomme le texte qu'on lit ne se balise pas.== *« la première
  chuqqah »*, *« cette chuqqah dit »* restent nus : le mot y désigne ==le genre
  du texte sous les yeux==, non le concept. Le gras est une promesse — *ce mot
  cache quelque chose que le français rate* —, et il n'y a rien à apprendre en
  touchant le nom de ce qu'on est en train de lire. ==Une marque qui promet sans
  tenir s'use.== Même principe que le §2.10 : *le niveau 3 ne double pas la
  marque*, parce que le contexte porte déjà la chose. On balise donc `**chuqqah**`
  ==là où il désigne la chose elle-même== — la feuille d'introduction, une fiche,
  un passage qui l'explique —, et nulle part ailleurs.
- `**tevel**` — intraduisible : la terre ==en tant qu'elle est habitée et
  productive== (תֵּבֵל). Non « le monde », qui importe le *kosmos* grec — un tout
  ordonné qu'on contemple du dehors —, ni « l'univers ». Le mot ==ne prend jamais
  l'article== : il fonctionne comme un nom propre, et l'hébreu l'apparie à
  *ʾeretz* dans le parallélisme poétique sans que les deux se confondent. C'est
  ==la troisième terre== du corpus : l'**ʾeretz** est le domaine, l'*ʾadamah* est
  le sol qu'on travaille, le **tevel** est l'étendue en tant qu'elle porte des
  vivants. Les rendre tous trois par « terre » ferait disparaître deux
  distinctions que la langue tient. Premier emploi *1 Samuel* 2:8.
- `**seter**` — intraduisible : ==le couvert, l'endroit d'où l'on n'est pas vu==
  (סֵתֶר). De *satar* (סָתַר) — se dérober à la perception. Non « secret », qui en
  français désigne ==un contenu qu'on retient== : le **seter** n'est pas une
  information, c'est ==une position==. On est *ba-seter*, à couvert — et c'est de
  là que **YHWH** parle à Mosheh, comme c'est de là que le méchant tend son
  embuscade : ==le mot ne juge pas ce qui s'y tient==. Premier emploi *Devarim*
  13:7.
- `**nistar**` / `**nistarot**` / `**Nistarot**` — intraduisible : ==ce qui est
  structurellement voilé== (נִסְתָּר). Niphal de *satar* : non pas ce qu'on a
  caché, mais ==ce qui se dérobe de soi-même== — la forme passive ne désigne
  aucun acte de dissimulation. Non « les mystères » (catégorie des cultes
  hellénistiques : un savoir réservé à des initiés) ni « les choses secrètes »
  (qui suggère un contenu qu'on pourrait divulguer). Le §1 emploie déjà la
  majuscule pour ==le quatrième mode de la Kenesset==, d'après *Deutéronome* 29:28 —
  *hanistarot laYHWH ʾEloheinu* : ce qui est voilé appartient à **YHWH**, et
  ==cela reste vrai après qu'on l'a vu==. La forme minuscule vaut pour le concept
  partout ailleurs.
- `**maqom**` / `**Maqom**` / `**ha-Maqom**` — intraduisible : ==le lieu où une chose tient debout== (מָקוֹם). De *qum* (קוּם) — se lever, prendre position ; c'est la racine du relèvement. Non « lieu » au sens d'un emplacement, ni *topos* au sens grec d'un contenant ==indifférent à ce qu'il contient== : le **maqom** est ==actif==, il maintient debout ce qui s'y trouve. Composé `**ha-Maqom**` — ==le Lieu== —, titre divin : **YHWH** est le **maqom** du monde, et le monde n'est pas son **maqom**.
- `**chozeh**` / `**Chozeh**` — intraduisible : ==celui qui contemple ce qui reste voilé== (חֹזֶה). De *chazah* (חָזָה) — contempler, percevoir dans la vision. ==Distinct de `**roʿeh**`==, et c'est toute la question : le grec a fondu les deux en un seul mot, effaçant ==la gradation de profondeur== dans l'accès visionnaire. Le **roʿeh** voit ; le **chozeh** ==pénètre==. Écrire « hozeh » mettrait un `h` là où le §2.9 veut `ch`.
- `**roʿeh**` / `**Roʿeh**` — intraduisible : ==celui qui conduit parce qu'il voit== (רֹאֶה). Un seul mot pour ==deux verbes== que l'hébreu écrit pareil — *raʾah* (רָאָה) voir, et *raʾah* (רָעָה) paître. Ce n'est pas un hasard de la langue : le berger ==voit le chemin avant que le troupeau n'y marche==. Non « pasteur », qui ne garde que la conduite : un « pasteur » qui ne voit rien n'est pas un **roʿeh**, c'est un gestionnaire.
- `**mevaser**` / `**Mevaser**` — intraduisible : ==celui qui porte l'annonce d'une chose déjà accomplie== (מְבַשֵּׂר). De *basar* (בָּשַׂר) — annoncer une bonne nouvelle ; même racine que **basar**, la chair, ==ce qui suggère une annonce portée par un corps qui court==. Non « évangéliste » (métier tardif) : le **mevaser** est le crieur qui apporte ==la victoire déjà remportée== à ceux qui ne la savent pas encore.
- `**moreh**` / `**Moreh**` — intraduisible : ==celui qui pointe du doigt la direction== (מוֹרֶה). De *yarah* (יָרָה) — indiquer, viser. ==Même racine que *Torah*==, et c'est ce qui la découvre : la *Torah* n'est pas d'abord un code, c'est ==une direction indiquée==. Non « docteur » ni « enseignant » (savoir transmis) : le **moreh** enseigne depuis la **daʿat**, ==il a visité le territoire dont il donne la carte==.
- `**laqach**` / `**Laqach**` — intraduisible : ==la saisie souveraine== (לָקַח). Prendre, saisir, emmener. Non « appeler » ni « choisir », qui laissent au saisi une part d'initiative : le **laqach** ==ne se négocie pas==. C'est le mode de constitution du **naviʾ** — il n'est pas quelqu'un qui décide de prophétiser, il est ==celui sur qui la main s'est posée==. Écrire « lakach » manquerait deux lettres : le ==qof== veut `q`, et la finale est un ==het==.

- `**ʾEl Shaddai**` — deux mots, les deux en gras. Même traitement qu'**ʾEl ʿElyon** et **ʾEl Roï**. Premier emploi *Genèse* 17:1.
- `**milah**`. Premier emploi *Bereshit* 17.
- `**goy**` / `**goyim**` — forme construite : *goyei* → toujours **goyim**, jamais "nations"
- `**ʿorlah**` / `**ʿarel**`
- `**mishpat**` / `**mishpatim**`. Premier emploi *Bereshit* 18.
- `**shofet**` / `**shoftim**`. Premier emploi *Genèse* 18:25.
- `**ʿolam**` — intraduisible : de la racine "caché, dissimulé" — la limite temporelle que le regard humain ne peut pas discerner. **Règle de rendu en corps de texte : translittérer le construit en entier** — `**berith-olam**`, `**ʾachuzat-ʿolam**`, `**ledorot-olam**`, `**ʿad-ʿolam**`, `**leʿolam**`, `**meʿolam**`. Premier emploi *Genèse* 3:22 (*vechai leʿolam*).
- `**Sheʾol**` — intraduisible : le domaine des morts dans l'attente (שְׁאוֹל). Jamais « enfer » ni « séjour des morts » édulcoré. Le gras porte l'apostrophe de l'alef, comme la translittération. Premier emploi *Toledot Adam ve-Chavah*.
- `**teshuvah**` — intraduisible : le retour, le réalignement vers la présence quittée (תְּשׁוּבָה). Jamais « repentance » ni « pénitence ». Premier emploi *Toledot Adam ve-Chavah*.
- `**ha-satan**` — intraduisible : l'accusateur, la *fonction* d'accusation du Conseil Divin (הַשָּׂטָן). L'article « ha- » marque la fonction — jamais un nom propre ni un dieu rival. Traitement définitif à *Iyov*. Premier emploi *Toledot Adam ve-Chavah*.
- `**tevilah**` — intraduisible : l'immersion de retour, passer par les eaux pour se retourner vers la source (טְבִילָה). Non « baptême » ni simple « bain ». Premier emploi *Toledot Adam ve-Chavah*.
- `**merkavah**` — intraduisible : le trône-char de **YHWH** **ʾElohim** vu en vision (מֶרְכָּבָה). Non « chariot » ordinaire. Premier emploi en corps de texte : *Toledot Adam ve-Chavah*.
- `**Nefilim**` — intraduisible : les êtres nés du franchissement des domaines (נְפִילִים). De *napal* (נָפַל) : tomber. ==L'ambiguïté est maintenue== — ceux qui sont tombés, ceux qui font tomber, les êtres de la chute : le texte ne tranche pas, la traduction non plus. Jamais « géants » (la Septante a lu *gigantes*, et vingt siècles d'imagerie ont suivi ; le mot ne dit pas la taille). La majuscule est celle d'une catégorie d'êtres, non d'un peuple : c'est un pluriel sans singulier attesté dans le corpus. Premier emploi *Genèse* 6:4.
- `**gibbor**` / `**gibborim**` — intraduisible : le puissant, celui dont la force brute fait le poids (גִּבֹּר). De *gabar* (גָּבַר) : l'emporter, prévaloir. Non « héros » (catégorie grecque de l'excellence) ni « vaillant » (vertu morale) : le **gibbor** pèse par sa capacité de contrainte, jamais par la sagesse ni par la fidélité. Le corpus écrit aussi `**gibor**` — deux orthographes du même mot, les deux retombent sur cette entrée. Équivalent araméen : **gibbarayaʾ**, qui donne son titre au *Sefar Gibbaraya*. Premier emploi *Genèse* 6:4.

- `**naviʾ**` / `**neviʾim**` / `**Neviʾim**` — intraduisible : celui que **YHWH** envoie porter son **davar** dans le temps visible (נָבִיא). Jamais « prophète » au sens courant — devin, annonceur d'avenir : le **naviʾ** ne prédit pas d'abord, il ==lit l'alliance dans l'histoire== et prononce le **mishpat** sur ce qu'il y voit. Sa fonction est celle du **shaliach** (§2.6, note terminologique) : une seule réalité, que le grec a décomposée. Pluriel **neviʾim** ; forme construite dans *Gevurot ha-Neviʾim*, nom ONT du n° 44.
- `**qodesh**` — intraduisible : l'état d'être mis à part pour un office (קֹדֶשׁ). Jamais « sainteté » — l'hébreu ne nomme pas une perfection morale mais une ==assignation==. Forme adjectivale déjà fixée au §3 : **qadosh**.
- `**Ruach ha-Qodesh**` — intraduisible : la **Ruach** en tant qu'elle met à part (רוּחַ הַקֹּדֶשׁ). Jamais « le Saint-Esprit » (§4.7). ==Capitalisée comme Ruach, Nefesh et Neshamah== — les intraduisibles majeurs portent la majuscule, et le composé la garde sur ses deux termes pleins : `Ruach ha-Qodesh`, jamais `ruach ha-qodesh`. Les trois mots en gras d'un seul tenant, l'article compris. C'est elle qui repose sur le roi promis en *Ésaïe* 11:2 et qui y porte les six capacités ci-dessous.

**Les six ruachim de *Ésaïe* 11:2-3.** *(Pas de titre `####` ici : le
pipeline découpe le document à chaque titre, et un sous-titre fermerait le §2.5
— les formes déclarées en dessous deviendraient invisibles à la jointure, sans
que rien ne le signale. `gevurot` l'a été.)*

Le passage pose une **ruach** unique — celle de **YHWH** — et six capacités
qu'elle porte, appariées trois par trois : `**chokhmah**` et `**binah**`,
`**ʿetsah**` et `**gevurah**`, `**daʿat**` et `**yirat YHWH**`. Les six sont
intraduisibles, décision de l'auteur du 20 août 2026, et se balisent partout où
elles paraissent — y compris hors de *Yeshayahu*.

**Six, et non sept.** Le compte de sept vient de la Septante, qui a dédoublé
*yirat YHWH* en *eusebeia* et *phobos* — la piété et la crainte —, et la Vulgate
a suivi. L'hébreu n'a pas ce septième. L'ONT s'en tient à ce que le texte porte.

**Ne pas rendre le couple par une paire de synonymes français.** « Sagesse et
intelligence », « conseil et force » : chaque paire hébraïque oppose deux
opérations distinctes, et les synonymes français les écrasent en une seule.

- `**chokhmah**` — intraduisible : la compétence qui fait aboutir (חָכְמָה). Non « sagesse » (contemplation, catégorie grecque) : la **chokhmah** est ==opératoire==. C'est elle dont Betsalel est rempli pour bâtir le Mishkan, elle qu'ont le tisserand, le marin, le forgeron. Elle ajuste une chose à sa destination — l'opération dont **tov** est le résultat. Locus définitif *Ésaïe* 11:2.
- `**binah**` — intraduisible : le discernement qui ==sépare entre== (בִּינָה). De *bin*, apparenté à *bein* (בֵּין) — « entre ». Non « intelligence » ni « compréhension » : la **binah** ne saisit pas un contenu, elle trace une frontière — le geste même par lequel **ʾElohim** sépare en *Bereshit* 1. Elle est à la **chokhmah** ce que distinguer est à réussir. Locus définitif *Ésaïe* 11:2.
- `**ʿetsah**` — intraduisible : le dessein arrêté (עֵצָה). De *yaʿats* (יָעַץ) — délibérer, résoudre. Non « conseil » au sens d'un avis qu'on donne et qu'on peut ne pas suivre : l'**ʿetsah** est le plan qu'on a ==résolu== de tenir. C'est le terme du Conseil Divin. Locus définitif *Ésaïe* 11:2.
- `**gevurah**` / `**gevurot**` — intraduisible : la capacité d'accomplir (גְּבוּרָה). De *gabar* (גָּבַר) — l'emporter, prévaloir ; même racine que **gibbor**, et c'est la distinction à tenir : le **gibbor** est celui qui pèse, la **gevurah** est le pouvoir de faire aboutir. Non « force » (physique) ni « puissance » (domination). Pluriel `**gevurot**` : les actes où elle se manifeste — d'où *Gevurot ha-Neviʾim*, le nom ONT du n° 44. Locus définitif *Ésaïe* 11:2.
- `**daʿat**` — intraduisible : le connaître par participation (דַּעַת). De *yada* (יָדַע). Non « connaissance » (un regard extérieur posé sur un objet) : la **daʿat** suppose d'être ==à l'intérieur== de ce que l'on connaît — d'où son emploi pour l'union conjugale en *Genèse* 4:1. C'est la **daʿat** de l'arbre de *Genèse* 2:9 (*etz hadaʿat tov vara*). Locus définitif *Ésaïe* 11:2.
- `**yirah**` / `**yirat YHWH**` — intraduisible : la reconnaissance de sa place devant ce qui dépasse (יִרְאָה). De *yare* (יָרֵא). Non « crainte » ni « peur » — ce n'est pas un affect, c'est une ==posture== : se tenir au rang qui est le sien devant **YHWH**. Même logique fonctionnelle qu'**ʾemunah** et **teshuvah**. *Ésaïe* 11:3 la scelle par un jeu de racines que la traduction perd : *vaharicho* (וַהֲרִיחוֹ) — « il respirera » — vient de רו״ח, les consonnes mêmes de **ruach**. Les six capacités se referment sur le souffle qui les portait. Locus définitif *Ésaïe* 11:3.

**Appliquer dès la rédaction** — ne pas attendre une passe séparée.

**`**...**` est EXCLUSIVEMENT réservé aux intraduisibles** — jamais pour l'emphase (mettre en valeur une phrase, un mot ordinaire ou un titre), **y compris dans les feuilles d'introduction et les notes** : le gras déclencherait à tort le style « Transliteration » d'Affinity au copier-coller, et l'app afficherait le mot en or, touchable, ouvrant une fiche de lexique vide. Pour l'emphase ordinaire, utiliser l'italique `*...*` ; pour une **accentuation**, voir §2.5 bis.

**Jusqu'où porte cet interdit — écrit le 8 septembre 2026, parce qu'il ne
l'était pas.** La règle vaut pour ==ce qui est distribué== : le corps des
traductions, les gloses, les notes de bas de section, les feuilles
d'introduction, et les fiches de `lexique/`. Elle ne vaut pas pour les documents
de travail du dépôt — ce `CLAUDE.md`, `SYNCHRONISATION.md`, les plans, les
rapports —, où le gras d'insistance reste permis.

Le motif n'est pas une tolérance, c'est ==la raison d'être de l'interdit==. Les
deux dégâts qu'il prévient sont mécaniques : Affinity applique son style au
copier-coller, et l'app affiche le mot en or et le rend touchable. ==Un fichier
qui ne passe ni dans l'un ni dans l'autre ne peut produire ni l'un ni l'autre.==

**Une exception, et elle est le vrai périmètre.** Ce qui compte n'est pas le
fichier, c'est ==ce qui fabrique un lemme==. Les entrées de glossaire de ce
document sont lues par le pipeline et émises vers `dist/` : un gras d'insistance
posé ==à l'intérieur d'une entrée== y devient un terme émis, donc un mot d'or
sans fiche. Dix-neuf l'ont été et ont été convertis le 25 août 2026 — c'est le
seul endroit de ce fichier où la règle mord, et elle y mord entièrement.

==Mesuré, et non déduit.== Deux témoins plantés le 8 septembre 2026, un dans une
puce du §2.5 et un dans une case du §3, puis une construction :

- celui du §2.5 ==est devenu un lemme==. La puce d'un terme devient sa note de
  balisage dans `glossary.json`, et cette note est découpée en nœuds : le gras y
  ressort en nœud `term`, avec son propre `lemma`, et le rapport l'a signalé en
  lien mort ;
- celui du §3 ==n'a rien produit==. Le §2.5 a la préséance sur le §3 pour la
  définition (`reference.rs`), et le terme témoin avait déjà sa puce : sa case du
  §3 n'était pas lue.

Le §3 mord donc lui aussi, mais ==seulement pour les termes qui n'ont pas de
puce au §2.5== — ceux dont il fournit la définition. La prudence est de traiter
les deux, ce que la passe du 25 août avait fait.

**Pourquoi il fallait l'écrire.** Le document portait 337 gras d'insistance, et
==la phrase qui interdit le gras d'insistance en emploie trois==, dont un sur le
mot « accentuation », dans la clause même qui renvoie à `==…==`. Une règle que
son propre porteur viole à chaque page n'est pas violée : elle a ==un périmètre
que personne n'a écrit==. C'est exactement la forme du §2.9 — une pratique non
écrite ne se compare à rien, donc elle ne peut pas diverger visiblement. Elle est
écrite maintenant.

**Polices hébraïques — dossier `utilities/`.** Les polices pour composer le script hébreu (niveau 3) et le rendre dans Affinity Publisher vivent dans `utilities/` à la racine du dépôt : **SBL Hebrew** (`SBL_Hbrw.ttf`) et **Ezra SIL** (`EzraSIL2.51/`) — hébreu biblique avec voyelles et cantillation (*teʿamim*) ; **Taamey Frank CLM** (projet Culmus) — hébreu avec *teʿamim* ; **Frank Ruhl Libre** — hébreu moderne (fonte variable + statiques). **Attention aux licences** : Ezra SIL et Frank Ruhl Libre sont sous OFL, donc redistribuables — ce sont les deux que La Bible ONT embarque. SBL Hebrew relève d'un EULA propriétaire et Taamey Frank CLM d'une GPL dont l'exception ne couvre que les documents composés, pas un binaire : ces deux-là restent réservées à la composition Affinity et ne doivent jamais entrer dans une app ni dans un site. Ce sont les **assets typographiques** du projet, suivis dans le dépôt pour la composition — non distribués au lecteur (cf. principe de distribution : seuls l'intro et les chapitres du slot voyagent).

### 2.5 bis Marquage des accentuations — `==...==`

**Règle :** un mot qu'on veut mettre en relief **sans en faire un intraduisible** s'écrit `==mot==`.

C'est le surlignage natif d'Obsidian : il se voit en écrivant, et il n'était employé nulle part ailleurs dans le vault.

**Pourquoi cette troisième marque existe.** Le gras était détourné pour insister — `**« Jour »**`, `**Candidat intraduisible**`, `**Sarah**`. Or `**...**` veut dire « intraduisible », et rien d'autre. Le pipeline allait alors chercher une fiche de glossaire qui n'existait pas, et l'app affichait ces mots en or et touchables, promettant une explication qu'elle n'avait pas. L'intention était juste ; il lui manquait sa propre marque.

**Ce que chaque marque produit dans La Bible ONT :**

| écriture | rendu dans l'app | touchable |
|---|---|---|
| texte nu | encre | non |
| `==mot==` | **bordeaux clair `#862742`**, semi-gras | non |
| `[[Nom]]` | **terre brûlée `#603518`**, semi-gras — §2.10 | **oui** → fiche de **Shem** |
| `**mot**` | **ʾor**, semi-gras | **oui** → fiche de lexique |
| `*mot*` | italique | non |

**Quand employer `==...==` :**

- ~~tout nom propre~~ — **plus depuis le 29 août 2026** : les noms propres relèvent du §2.10, la couche des **Shemot**, et s'écrivent `[[Nom]]` ;
- un mot français que le texte nomme solennellement — `==« Jour »==`, `==« Nuit »==`, `==« Cieux »==` ;
- une métadonnée d'apparat critique — `==premier emploi dans l'ONT==`, `==Candidat intraduisible==`.

#### Les noms propres ont quitté cette marque — 29 août 2026

**Ils relèvent désormais du §2.10**, la couche des **Shemot**, et s'écrivent
`[[Nom]]` en terre brûlée. Ce qui suit est l'histoire de la règle, gardée parce
qu'elle explique pourquoi la couche existe.

Le 19 août, la règle avait été généralisée : de « un nom propre dont le verset
explique l'étymologie » à **tout nom propre, partout, à toutes ses
occurrences**. Le motif tenait : un lecteur qui arrive sans rien savoir ne
distingue pas Mitsrayim d'un mot ordinaire, et le §4.12 lui refuse la forme
française. Sans marque, le texte se lit comme une suite de mots opaques dont
rien ne dit lesquels sont des personnes et des lieux.

**Ce qui manquait, et que le 29 août a corrigé.** La couleur disait « ceci est
une personne, un lieu » — et s'arrêtait là. Le lecteur voyait qu'il y avait
quelque chose, sans pouvoir l'atteindre. Or un **Shem** *porte* : ==Avraham==
est « père d'une multitude », ==Peleg== le partage. La marque signalait un sens
sans jamais le donner.

**Deux noms lui échappaient, et ils échappent encore à la nouvelle couche.**
`Shem` et `Adam` sont tantôt noms propres, tantôt intraduisibles — le fils de
Noach et l'acte d'existence ; le personnage de *Toledot* et le générique de
*Bereshit* 8+. La casse ne les sépare pas. C'est un arbitrage verset par verset,
réservé à l'auteur.

**Un effet à connaître, qui vaut pour la couche des Shemot.** Sur un chapitre
patriarcal, « Avraham » paraît jusqu'à 186 fois : la page devient très colorée.
C'est un choix assumé — la lisibilité pour qui découvre passe avant la sobriété
de la page.

**Quand ne PAS l'employer :** pour un vrai terme hébreu. Celui-là mérite une entrée de glossaire (§2.5 / §3) et donc `**...**`. Le marquer `==...==` reviendrait à priver le lecteur de sa fiche.

**Côté Affinity :** `==...==` ne déclenche aucun style au copier-coller. Un style de caractère dédié reste à créer si l'édition imprimée doit distinguer ce niveau.


### 2.5 ter Les fiches de lexique — `lexique/<lemme>.md`

**Règle :** l'explication qu'un lecteur reçoit en touchant un mot d'or ne
s'écrit pas ici, mais dans `lexique/`, un fichier par terme, nommé par son
lemme — `lexique/chesed.md`.

**Pourquoi une seconde source.** Ce document est écrit *pour le traducteur* :
ses entrées consignent un arbitrage — pourquoi **ʾElohim** reste en hébreu, ce
que « grâce » raterait de **chesed**. Le lecteur du 21ᵉ siècle qui touche le mot
n'a pas cette question. Il en a une autre, à laquelle rien ne répondait : ce que
le mot voulait dire pour qui l'écrivait. La fiche d'**ʾElohim** tenait en deux
phrases, celle de **YHWH** était la plus courte des cent cinq.

Ce n'est pas une source de vérité dédoublée : **une seule source par *fait***.
Le §3 garde l'hébreu, les formes, le rendu fixé et la règle de balisage ;
`lexique/` ne porte que l'explication, et remplace la définition quand elle
existe.

**La forme : les titres intermédiaires sont permis depuis le 30 août 2026.** Le
titre `# Elohim` sert de repère dans Obsidian, le pipeline l'ignore ; les lignes
vides séparent les paragraphes. Une fiche peut porter des sous-titres `##`, des
listes, des citations et des filets — `BlocDeFiche.swift` les rend tous, et il
est partagé par la feuille d'un intraduisible et celle d'un **Shem**.

**Ce que la règle disait avant, et pourquoi elle a changé.** Elle imposait
« des paragraphes et rien d'autre », parce que la feuille ne rendait en effet
que les paragraphes et **laissait tomber le reste sans rien dire**. Le pipeline
jetait les titres avant même de les émettre : deux silences en série, et celui
qui écrivait la fiche ne pouvait pas savoir lequel des deux l'avait mangée.

Les deux sont réparés côté app. La contrainte tombe donc, et elle devait
tomber : une fiche porte trois mouvements — la racine dans les six ==ruachim==,
le porteur, les renvois —, et sans leurs titres ils arrivent collés en un seul
flot.

Ce qui ne change pas : une fiche faite de blocs de texte voyage par la mise à
jour réseau du corpus et atteint les apps **déjà installées**, sans compilation
ni revue Apple.

**Une fiche déclare les formes qui lui appartiennent.** Décision de l'auteur du
8 septembre 2026. Après le corps, une section ==Formes== liste les formes
fléchies que le corpus emploie et qui doivent mener ici.

    ## Formes
    vayomer · vayomru · amarti · vaʾomar

**Pourquoi dans la fiche, et pas au §2.5.** Le §2.5 est une liste
d'==intraduisibles== : y déclarer `vayomer` ferait d'`amar` un intraduisible, et
lui ferait perdre son rendu « formuler » que le §3.1 fixe. ==Les deux registres
doivent rester séparés== — ce qui se traduit, et ce qui se touche.

La fiche, elle, ==sait mieux que quiconque quelles formes lui appartiennent==.
L'information y vit avec le mot, se relit et se corrige comme le reste, et
n'engage aucun statut.

**Ce que ça produit.** Le lecteur touche `vayomer` dans une translittération de
niveau 3 et arrive sur la fiche d'`amar`. Sans cette déclaration il ne touche
rien — le mot reste lisible et ==inerte==.

**Et ce qu'on ne fait pas, délibérément.** ==Aucune résolution morphologique.==
Le pipeline ne devine pas une racine à partir d'une forme, et la raison n'est
pas la difficulté mais ==le mode d'échec== : une règle qui se trompe ne rend pas
le mot inerte, elle le rend ==touchable vers la mauvaise fiche==. Le lecteur
arrive ailleurs sans que rien ne le lui dise. Une déclaration exacte est un gain
permanent ; une devinette est une substitution silencieuse.

**Une fiche déclare aussi ce qui l'identifie.** Décision de l'auteur du
11 septembre 2026. Après les ==Formes==, une section ==Source== porte deux
choses, et rien d'autre :

    ## Source

    559 · אָמַר

À gauche le ==numéro de Strong== du lemme, nu. À droite ==sa forme absolue en
hébreu==, celle du dictionnaire — non une forme fléchie, que les Formes portent
déjà.

**Ce qu'est un numéro de Strong.** L'identifiant qu'une concordance de 1890 a
attribué à chaque mot du vocabulaire hébreu, araméen et grec de la Bible — un
par lemme, 1 à 8674 pour l'hébreu. Ton témoin le porte déjà : `sources/he-wlc/`
écrit `lem=1254 a` sous בָּרָא et `lem=430` sous אֱלֹהִים.

==Il dit quel mot c'est. Il ne dit pas ce qu'il veut dire.== Le sens reste au §3
et à la fiche ; le numéro n'est qu'une clé. L'abus classique — *« Strong dit que
ce mot signifie X »* — confond un index avec une autorité, et l'ONT ne l'emploie
jamais ainsi.

**Pourquoi la fiche, et non le §3.** Parce que le §3 est un glossaire
d'==arbitrages de traduction== : il porte les intraduisibles et les rendus
fixés, et il n'a aucune raison de grossir de huit cents entrées pour accueillir
le vocabulaire ordinaire du corpus. Mesuré le 11 septembre : ==133 fiches sur
357== ont une entrée de glossaire. Les 224 autres seraient restées hors
d'atteinte.

La fiche, elle, ==existe pour chaque mot qui en mérite une==, et elle sait ce
qui l'identifie. C'est le même raisonnement qui avait placé les Formes ici
plutôt qu'au §2.5.

**Ce que ça change, et c'est le point.** Sans le numéro, la liseuse doit
==deviner== quel mot du verset hébreu ouvre quelle fiche : elle ôte les voyelles
et compare les consonnes. Or ==deux mots peuvent avoir le même squelette==, et
une devinette fausse ne rend pas le mot inerte — elle le rend ==touchable vers
la mauvaise fiche==, ce que le paragraphe précédent interdit déjà pour la
morphologie.

    un squelette qui se trompe est silencieux
    un Strong qui se trompe est contredit par le témoin

**Le cas qui l'a montré, et il est du jour même.** Le même וַיִּקַּח — qof à
dagesh forte — s'écrit `vayiqach` dans un fichier verrouillé et `vayiqqach`
dans un brouillon. Une jointure par squelette ==ne verra jamais cette
divergence== : les voyelles ôtées, les deux donnent ויקח. Le Strong la voit,
avec une donnée que le témoin porte déjà.

**Garder la lettre des homographes.** Strong avait fondu des mots que l'érudition
a séparés depuis, et les éditions modernes les distinguent par une lettre :
`1254 a` n'est pas `1254 b`. ==C'est une distinction réelle, elle se garde.==

**Toute fiche ouvre par sa prononciation.** ==Avant le titre de section
suivant, avant la scène, avant tout le reste== — parce que c'est la première
chose qu'un lecteur veut savoir d'un mot qu'il ne sait pas dire, et parce que la
translittération ne la lui donne pas (§2.12).

La section porte quatre choses, et pas davantage :

- ==le mot découpé en syllabes, accent marqué== — `cha-NOKH`, la majuscule
  portant l'accent tonique ;
- ==chaque lettre que le français ne fait pas==, expliquée par ==le geste qui la
  produit== et non par son seul symbole. « Serre le fond de la gorge et souffle »
  vaut mieux que « pharyngal sourd », qui ne dit à personne quoi faire de sa
  bouche ;
- ==la faute probable==, quand elle existe. Un francophone lit `ch` comme
  « chat » et `q` comme « que » : le dire épargne des années de prononciation
  fausse, et l'auteur en est le témoin ;
- ==rien d'autre==. Ni histoire de la langue, ni variantes régionales : la fiche
  a le reste de sa place pour cela.

==Une fiche de **Shem** la porte aussi==, et pour la même raison — un nom qu'on
ne sait pas dire est un nom qu'on ne dit pas.

**Le critère : la fiche doit agir dans les six ruachim.** Ce n'est ni
l'exactitude ni la densité qui font une fiche — c'est qu'elle opère selon les
six capacités de *Ésaïe* 11:2-3, qui sont aussi bien la règle d'écriture que
l'objet du corpus.

| | ce que la fiche doit faire |
|---|---|
| **chokhmah** | **aboutir**. Elle est opératoire : de l'érudition qui ne produit pas de compréhension a raté son office. |
| **binah** | **séparer entre**. Trancher ce que le mot français confond — « sagesse » d'avec habileté, « crainte » d'avec posture. |
| **ʿetsah** | tenir un **dessein arrêté**. Une fiche va quelque part ; ce n'est pas un commentaire qui vagabonde. |
| **gevurah** | **mener jusqu'au bout**. Pas de demi-explication laissée au lecteur. |
| **daʿat** | **faire connaître du dedans** — la centrale. |
| **yirah** | **se tenir à son rang**. Ne pas inventer, ne pas dépasser ce que le texte porte. |

**La daʿat commande tout le reste.** Elle est le connaître par participation,
qui suppose d'être *à l'intérieur* de ce que l'on connaît — et c'est exactement
ce qu'une fiche doit produire : faire **voyager le lecteur à l'intérieur de
l'époque**, non lui décrire l'époque du dehors. Une fiche qui explique depuis
notre monde — « l'hébreu ne dit pas X mais Y » — le laisse spectateur : elle
donne de l'information, pas de la connaissance.

En pratique : **écrire la scène plutôt que la proposition.** Mettre le lecteur
là où l'on se tenait — l'atelier du Mishkan, la porte de la ville, le poids
d'une pierre dans la main. Le contraste avec le français vient *ensuite* et sert
la scène ; il ne la remplace pas. Ne jamais écrire « dans l'ontologie hébraïque,
exister c'est occuper une fonction » : montrer une chose qui n'existe pas encore
faute d'emploi, et laisser le lecteur le voir.

**Le balisage y vaut comme partout ailleurs** : `**terme**` pour un
intraduisible — il devient un lien vers sa fiche, et c'est ainsi que les fiches
se tiennent entre elles —, `==...==` pour l'accentuation, `*italique*` pour une
translittération. Le gras d'insistance reste interdit ici comme dans le corps :
il promettrait une fiche qui n'existe pas.

**Ce qui n'est pas trouvé est dit.** Une fiche dont le nom ne retombe sur aucun
lemme n'atteint aucun lecteur. Le pipeline la signale dans son rapport, section
« Fiches sans entrée de glossaire », plutôt que de la laisser tomber.

### 2.6 Les noms des livres bibliques

**Règle pour le texte ONT et les noms de fichiers :** Les noms des livres bibliques sont toujours donnés dans leur forme hébraïque translittérée. Ces noms sont intraduisibles : leur titre hébreu est le vrai titre, souvent issu du premier mot du livre. Cette règle vaut aussi pour les noms de fichiers (ex. `bereshit-1.md`, pas `genese-1.md`).

**Format des titres de section ONT :**
- Titre principal : `# Bereshit 1` — le nom hébreu translittéré est le vrai titre, suivi du numéro de section ONT
- Sous-titre : `*(Genèse / בְּרֵאשִׁית 1:1 — 2:3)*` — le nom français comme pont de navigation pour le lecteur occidental, suivi du script hébreu et de la référence de verset

**Format dans le corps du texte :** *Bereshit* — toujours la translittération.

**L'article défini s'écrit `ha-`, minuscule et lié.** *El ha-Qolossiyim*,
*Igeret ha-Ivrim*, *Gevurot ha-Neviʾim*, *Bereshit ha-Yohanan*, *Ruach
ha-Qodesh*, *ha-satan*, *benei ha-adam*. Jamais `Ha` collé en majuscule, jamais
`ha` collé sans trait d'union.

**Pourquoi la règle est écrite ici plutôt que sue.** Elle ne l'était pas, et le
corpus a porté trois conventions à la fois jusqu'au 25 août 2026 : `ha-` partout
où l'ONT forge un nom, `Ha` collé pour les seules *Igerot* — la forme même de
*Maʿasim HaShlichim*, que le §2.6 cite pour la rejeter —, et `ha` collé pour les
conteneurs du Ḥurban. Personne ne l'avait vu parce que chaque liste était
cohérente avec elle-même.

L'article n'est pas une partie du nom : c'est un morphème qui s'y attache. Le
trait d'union le montre, la majuscule le déguise en syllabe. Et la minuscule
tient l'ordre de lecture : le regard trouve d'abord *Qolossiyim*, le nom, et non
un *HaQolossiyim* qui n'existe dans aucune langue.

**La règle vaut pour les identifiants aussi** — dossiers, fichiers, slugs :
`el-ha-qolossiyim`, `igeret-ha-ivrim`, `igerot-lifnei-ha-hurban`. Ce sont eux
que les URL du site et les positions de lecture porteront ; les aligner coûtait
un renommage tant que les livres étaient vides, et deviendra une rupture le jour
où ils seront écrits.

**Logique :** Le nom hébreu est le nom réel de la section. Le nom français (Genèse, Exode...) sert uniquement de repère pour que le lecteur occidental s'y retrouve dans sa Bible traditionnelle — il apparaît en sous-titre, jamais comme désignation principale.

**Répertoire des noms hébraïques — Torah :**
| Nom français | Nom hébreu | Translittération | Hébreu |
|---|---|---|---|
| Genèse | *Bereshit* | Bereshit | בְּרֵאשִׁית |
| Exode | *Shemot* | Shemot | שְׁמוֹת |
| Lévitique | *Vayiqra* | Vayiqra | וַיִּקְרָא |
| Nombres | *Bemidbar* | Bemidbar | בְּמִדְבַּר |
| Deutéronome | *Devarim* | Devarim | דְּבָרִים |

**Répertoire des noms hébraïques — Neviʾim (Prophètes) :**
| Nom français | Translittération | Hébreu |
|---|---|---|
| Josué | *Yehoshua* | יְהוֹשֻׁעַ |
| Juges | *Shoftim* | שֹׁפְטִים |
| Samuel (1-2) | *Shemuel* | שְׁמוּאֵל |
| Rois (1-2) | *Melakhim* | מְלָכִים |
| Ésaïe | *Yeshayahu* | יְשַׁעְיָהוּ |
| Jérémie | *Yirmeyahu* | יִרְמְיָהוּ |
| Lamentations | *Ekha* | אֵיכָה | Décision ONT : placé en Neviʾim après *Yirmeyahu* (lien fonctionnel et historique direct), et non dans les Ketouvim — le regroupement des Megillot est rabbinique post-70 CE, pas Second Temple |
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
| Malachie | *Malʾakhi* | מַלְאָכִי |

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
| Esdras-Néhémie | *Ezra Nehemyah* | עֶזְרָא נְחֶמְיָה |
| Jubilés | *Yovelim* | יוֹבְלִים |
| 1 Hénoch | *Chanokh* | חֲנוֹךְ |
| Testament de Lévi | *Tsavaʾat Levi* | צַוָּאַת לֵוִי |
| 2 Ezra | *Chazon Ezra* | חֲזוֹן עֶזְרָא |
| Apocalypse de Baruch | *Chazon Barukh* | חֲזוֹן בָּרוּךְ |

**Répertoire des noms — Besorot (Évangiles) :**
| Nom français | Translittération ONT | Hébreu | Notes |
|---|---|---|---|
| Marc | *Marqus* | מַרְקוּס | Première *besorah* rédigée — dans les *Eduyot*. Nom complet : *Yohanan Marqus* (יוֹחָנָן מַרְקוּס — *Gevurot* 12:12) |
| Matthieu | *Matityahu* | מַתִּתְיָהוּ | "don de YHWH" — dans les *Eduyot* |
| Luc | *Luqas* | לוּקָס | Nom grec translittéré — dans les *Eduyot* |
| Jean | *Bereshit ha-Yohanan* | בְּרֵאשִׁית הַיּוֹחָנָן | *Bereshit* de Yohanan — *besorah* cosmique-inaugurale, écho de *Genèse* 1:1, séparée des *Eduyot* |

**Répertoire des noms — Gevurot ha-Neviʾim et Machazeh :**
| Nom français | Translittération ONT | Hébreu | Notes |
|---|---|---|---|
| Actes des apôtres | *Gevurot ha-Neviʾim* | גְּבוּרוֹת הַנְּבִיאִים | "les *gevurot* (actes de puissance) de **YHWH** à travers ses *neviʾim*" — de *gavar* (גָּבַר) : être puissant, l'emporter. **YHWH** sujet grammatical, *neviʾim* instrument. Jamais *Maʿasim HaShlichim* (importait la catégorie grecque *apostolos* comme agent autonome). |
| Apocalypse | *Machazeh Yohanan* | מַחֲזֵה יוֹחָנָן | *machazeh* = vision intérieure — même terme qu'en *Genèse* 15:1 |

**Répertoire des noms — Igerot (Lettres) :**
| Nom français | Translittération ONT | Hébreu | Notes |
|---|---|---|---|
| Romains | *El ha-Romiyim* | אֶל הָרוֹמִיִּים | Igerot de Shaul |
| 1-2 Corinthiens | *El ha-Qorintiyim* | אֶל הַקּוֹרִינְתִּיִּים | Igerot de Shaul |
| Galates | *El ha-Galatiyim* | אֶל הַגָּלָטִיִּים | Igerot de Shaul |
| Éphésiens | *El ha-Efesiyim* | אֶל הָאֶפֶסִיִּים | Igerot de Shaul |
| Philippiens | *El ha-Filipiyim* | אֶל הַפִּילִיפִּיִּים | Igerot de Shaul |
| Colossiens | *El ha-Qolossiyim* | אֶל הַקּוֹלוֹסִּיִּים | Igerot de Shaul |
| 1-2 Thessaloniciens | *El ha-Tessaloniqiyim* | אֶל הַתֶּסָּלוֹנִיקִיִּים | Igerot de Shaul |
| 1-2 Timothée | *El Timotiyos* | אֶל טִימוֹתִיּוֹס | Igerot de Shaul |
| Tite | *El Titos* | אֶל טִיטוֹס | Igerot de Shaul |
| Philémon | *El Filemon* | אֶל פִּילֵמוֹן | Igerot de Shaul |
| Hébreux | *Igeret ha-Ivrim* | אִגֶּרֶת הָעִבְרִים | Anonyme — ancrée dans *Vayiqra* |
| Jacques | *Igeret Yaʿaqov* | אִגֶּרֶת יַעֲקֹב | *Yaʿaqov* (יַעֲקֹב) — "talon / il supplante" |
| 1-2 Pierre | *Igeret Kefa* | אִגֶּרֶת כֵּיפָא | *Kefa* (כֵּיפָא) — araméen : "roc". Le rang se déduit : א׳, ב׳ |
| 1-3 Jean | *Igeret Yohanan* | אִגֶּרֶת יוֹחָנָן | *Yohanan* (יוֹחָנָן). Le rang se déduit : א׳, ב׳, ג׳ |
| Jude | *Igeret Yehudah* | אִגֶּרֶת יְהוּדָה | *Yehudah* (יְהוּדָה) — "celui qui est loué" |

#### Le nom porte la numérotation — 10 septembre 2026

**Décision de l'auteur.** Deux systèmes de numérotation coexistent dans l'ONT, et
==c'est le nom du livre qui dit lequel on emploie== :

    Bereshit 9:8      le verset ⁸ de l'unité ONT n° 9
    Genèse 9:25       le verset 25 du chapitre 9 de la Genèse reçue

Ce sont ==le même verset==, et la forme double est permise — recommandée même,
quand les deux servent le lecteur :

    Bereshit 9:8 / Genèse 9:25

**Pourquoi le nom, et pas une marque.** Parce qu'il n'y a alors ==rien à
deviner==. Une notation qui repose sur le contexte se lit juste tant que le
lecteur connaît le contexte ; un nom se lit seul. La règle ne signale pas
l'exception, ==elle supprime le cas d'exception==.

**Ce n'est pas une invention : c'est déjà la pratique du projet**, partout où les
deux systèmes se croisent —

- le **sous-titre** d'une unité : `*(Genèse / בְּרֵאשִׁית 15:1-21)*` ;
- le **pied de page** qui annonce la suite : `*Bereshit 9 : Genèse 9:18-29* ;
- le **§12** de ce document : `**Bereshit 8** (Genèse 9:1-17)`.

Les seules occurrences de `Genèse C:V` du corpus étaient déjà exactement cette
forme. ==Il n'y avait que les gloses pour l'ignorer==, et c'est là que les deux
fautes sont nées.

**Le rôle du nom français ne change pas** — le §2.6 lui assigne d'être ==le pont
de navigation vers la Bible que le lecteur connaît==. Une référence en
numérotation reçue est exactement cet office : elle ne désigne pas une unité de
l'ONT, elle dit où retrouver le passage ailleurs.

**Le piège, nommé pour qu'il ne se reproduise pas.** ==Ne jamais écrire un nom
ONT devant un numéro biblique.== C'est ce qui a produit les deux seules
références fautives du corpus, et le mécanisme est instructif : elles ont été
écrites ==en comptant les exposants affichés sur la page== au lieu de lire le
renvoi du sous-titre. Le comptage était juste — c'est le système qui était le
mauvais.

Et il faut le dire parce que la phrase qui précédait cette section l'y invitait :
elle disait *« Format dans le corps du texte **et les renvois** : *Bereshit* 7:2
— toujours la translittération »*. Écrite pour les ==noms== de livres, elle se
lisait comme couvrant les ==renvois chiffrés==. ==Une règle juste sur son propre
objet peut en fabriquer une fausse sur le terrain voisin.==

**La règle a une limite, et elle est structurelle.** Quatre livres portent ==le
même nom dans les deux langues== : `Amos`, `Ruth`, `Esther`, `Daniel`. Pour
eux, le nom ne peut rien distinguer — `Daniel 7:1` est la même chaîne dans les
deux systèmes.

Vingt-six références du corpus les visent, et ==aucune n'est ambiguë
aujourd'hui== : ces quatre livres n'ont pas d'unité ONT écrite, donc pas de
numérotation propre à confondre.

Le jour où l'un d'eux sera traduit, il faudra ==une marque explicite== pour ses
renvois internes — la forme `Daniel 7, v.1` du §2.6, ou la forme double. C'est
écrit ici pour qu'on le sache ==avant== d'écrire le livre, et non après.

**Une réserve, pour ne pas la découvrir trop tard.** Certains noms français
portent des catégories que l'ONT ==refuse explicitement== : « Apocalypse » est le
calque que le §1 rejette, « Actes des apôtres » réintroduit l'*apostolos* que le
§2.6 écarte au profit du **shaliach**, « Jean » perd l'écho de *Bereshit* 1 qui
fait tout le nom de *Bereshit ha-Yohanan*.

La règle ne mord pas encore sur eux : ==ces livres ne sont pas écrits==, donc ils
n'ont aucune unité ONT, donc aucune ambiguïté n'est possible. Le jour où ils le
seront, il faudra trancher entre garder le nom hébreu seul, forger un français
acceptable, ou juger que le pont vaut ce prix.

### 2.7 La feuille d'introduction

Chaque livre s'ouvre par une **feuille d'introduction** qui porte, une fois en amont, tout le cadre (situation, question du livre, comment lire, motifs, plan) — au lieu de le répéter en gloses page après page. L'introduction est la voix du projet (dense) ; le corps garde la voix vécue et ses gloses restent légères. Sections types : **Titre & Shem · Régime d'auteur · Thème · Date d'émergence · Date de consignation · Contexte historique · But · Comment lire · Vue d'ensemble · Caractéristiques particulières · Échos dans la Berit Hadashah · Plan · Repères.** Fichier `*-0-intro.md` à côté du livre. Inaugurée avec *Toledot Adam ve-Chavah*.

### 2.8 Les use cases d'annotation

Opérationnalise §2.1 : chaque terme du glossaire reçoit **un** use case — une combinaison fixe des trois niveaux, appliquée mécaniquement.

| UC | Type | Niveau 3 (hébreu) |
|---|---|---|
| **UC0** | Noms divins — hébreu/gras, jamais traduits ; glose fondatrice une fois dans tout le corpus | généreux |
| **UC1** | Intraduisible — le mot reste hébreu (gras) | 1re occ. |
| **UC2** | Noyau *(traduit, hébreu persistant)* — *shamayim*/Cieux, *eretz*/Terre, *adamah*/sol concret… | **≥ 1×/chapitre** (régime b) |
| **UC3** | Traduit standard *(le défaut)* — *tselem*/représentant fonctionnel, *banah*/édifia… | 1re occ., puis nu |
| **UC4** | Nom propre | 1re occ. + identification sur 5 occ. (§4.12) |
| **UC5** | Glose seule — structure (mérisme, chiasme, ambiguïté, silence) | — |
| **UC6** | Français simple — mot ordinaire hors glossaire | — |

Règle : le gras **est** la translittération exacte (apostrophes comprises : **Sheʾol**, **malʾakh**), jamais une francisation.


### 2.9 Comment s'écrit une translittération

Les sections précédentes disent **où** placer une translittération et **comment
la baliser**. Aucune ne disait **comment l'écrire** — et le corpus l'écrivait
pourtant d'une seule façon depuis le début, sans que rien ne la fixe.

**Pourquoi l'écrire maintenant.** C'est l'état exact où se trouvait la règle de
l'article avant le 25 août 2026 : le vault portait alors trois conventions à la
fois, et personne ne l'avait vu *parce que chaque liste était cohérente avec
elle-même*. Une pratique non écrite ne se compare à rien ; elle ne peut donc pas
diverger visiblement. Ce qui suit ne change aucune ligne du corpus — c'est le
relevé de ce qu'il fait déjà, rendu opposable.

#### Les consonnes

| lettre | rendu | exemples du corpus |
|---|---|---|
| **ח** *het* | `ch` | **chesed**, **chokhmah**, **chattat**, *choshekh*, *chayah* |
| **כ** *kaf* (avec dagesh) | `k` | *kavod*, *kohen*, *kavash* |
| **כ / ךְ** *khaf* (sans dagesh) | `kh` | cho**kh**mah, choshe**kh**, mela**kh**ah, Chano**kh** |
| **ק** *qof* | `q` | *qadosh*, *qodesh*, *qara*, *qanah* |
| **ט** *tet* | `t` | **tov**, **tevilah** |
| **ת** *tav* | `t` | *tohu*, *tehom*, **teshuvah** |
| **צ** *tsade* | `ts` | *tselem*, **tsedeq** |
| **שׁ** *shin* | `sh` | *shamayim*, **Shem**, **shaliach** |

Deux distinctions portent tout le système, et il faut les tenir :

- `ch` et `kh` ne sont **pas** deux graphies du même son — ils rendent deux
  lettres différentes, ==le het et le khaf==. Écrire « khata » pour חָטָא mettrait
  à la place du het le signe réservé au khaf ;
- `k` et `q` séparent de même le ==kaf== du ==qof==, ce qui garde *kohen* (כֹּהֵן)
  distinct de *qodesh* (קֹדֶשׁ).

**Le pe spirant se rend `f`, jamais `ph`.** Décision de l'auteur du 8 septembre
2026 — ==et c'est la même règle que celle du tet et du tav ci-dessous==.

Le principe que le tableau applique n'est pas « rendre la lettre » : c'est
==distinguer ce qui se percuterait==. `ch` et `kh` séparent le het du khaf ;
`k` et `q` séparent le kaf du qof. Le pe spirant, lui, ==n'entre en collision
avec rien== : aucune autre lettre hébraïque ne donne `f`.

`ph` paierait donc le coût d'un digramme ==sans rien acheter==. Et le coût est
réel : `שָׂפָה` s'écrirait `saphah`, où l'on ne saurait plus si c'est un pe
spirant suivi de `ah` ou un `p` suivi de `hah`. Le corpus porte quatre mots où
un pe est suivi d'un he.

*(Le digramme `kh` a exactement le même défaut — onze cas, dont* berakhah *—
et il est gardé parce qu'il ==achète une distinction==. C'est la comparaison
qui tranche, non l'ambiguïté prise seule.)*

**Huit mots divergeaient**, et c'est ce qui a rendu la règle nécessaire :
`Yafet`/`Yaphet`, `Ofir`/`Ophir`, `alef`/`aleph`, `Yosef`/`Yoseph`,
`shafat`/`shaphat`, `rachaf`/`rachaph`, `haʾaf`/`haaph`. ==Le même mot écrit des
deux façons==, ce qui n'est plus une convention lexicalisée mais la forme exacte
que le §2.9 existe pour fermer.

**227 occurrences converties**, et trois fiches renommées — `Yaphet` → `Yafet`
(105), `shiphchah` → `shifchah` (46), `Nephilim` → `Nefilim` (33).

==Le balayage a été fait par liste blanche, et il fallait.== Un filtre qui
excluait le français aurait converti *Pharaon*, *téléphone*, *Euphrate*,
*Philistins*, *orphelin*, *Josèphe*, *Memphis*, *alphabet*. On énumère les
formes hébraïques ; on ne soustrait pas les autres.

Et ==les noms de binyanim ne bougent pas== — *Hiphil*, *Niphal*, *Hophal*
relèvent de la nomenclature grammaticale internationale, non du vocabulaire du
corpus.

En revanche `t` rend indifféremment le **tet** et le **tav** : la distinction
existe en hébreu, l'ONT ne la porte pas, et l'hébreu de niveau 3 la rétablit
pour qui la cherche.

#### L'alef et le ayin se marquent partout — 9 septembre 2026

**Décision de l'auteur.** L'ONT adopte ==la convention savante== : l'alef prend
son demi-anneau `ʾ` et le ayin le sien `ʿ`, ==à l'initiale, au milieu et en
finale==, sans exception de position.

    ʾElohim     אֱלֹהִים        ʿolam      עוֹלָם
    naviʾ       נָבִיא          zeraʿ      זֶרַע
    ʾish        אִישׁ           ʿirin      עִירִין
    baraʾ       בָּרָא          chataʾ     חָטָא

==Ce que cette décision remplace, et pourquoi il faut le garder écrit.== Le
matin même, ce document posait l'inverse sur deux points : l'alef finale ne se
notait pas ==parce qu'elle est quiescente==, et rien ne se notait à l'initiale
==parce qu'il n'y a là aucune syllabe à couper==. Le second argument avait servi
à retirer sa marque à `**irin**`, et l'auteur l'avait demandé ==explicitement
linguistique==.

Les deux raisonnements étaient justes ==sur leur propre question==, qui était :
*qu'est-ce qui s'entend ?* La convention savante répond à une autre question :
*quelle lettre est là ?* Elle note ==le squelette consonantique==, et une lettre
muette est une lettre.

==On ne prend pas la moitié d'un système== — ce document le disait déjà en
écartant le demi-anneau savant pour le seul ayin initial. Le prendre entier, ou
pas du tout. Il est pris entier.

==Ce que ça n'a pas changé.== Le `t` rend toujours indifféremment le **tet** et
le **tav** : la convention savante les distingue par des points souscrits, que
l'ONT n'emploie pas. ==La décision porte sur les demi-anneaux, non sur les
diacritiques en général.==

==La passe.== ==2339 marques== — 635 sur les niveaux 3, 1704 sur les termes en
gras et les liens de **Shemot** —, et ==59 fiches renommées==. Différentiel
vérifié : 628 marques sans fiche avant, 628 après, ==aucun lien cassé==. Le slug
du pipeline retire les demi-anneaux sans séparateur, donc `naviʾ` et `navi`
retombent au même endroit.

==Le danger était `El`==, et il valait d'être vu. Le mot vit dans `**ʾEl
ʿElyon**`, dans `Bet-El`, et dans les **Shemot** théophores — `Mikhaʾel`,
`Yishmaʿel`, `Rafaʾel`. Un remplacement au motif les aurait tous détruits. Les
délimiteurs de gras et de lien l'ont évité : `**El**` et `[[ʾEl]]` ne matchent
que le mot seul. ==C'est la troisième fois de la journée qu'une liste blanche
sauve une passe== — après le pe et l'alef préfixée.

==Et un contrôle a servi en passant.== La règle du §3.2 sur le possessif —
*toujours ta/sa/ma **ʾishah**, jamais ton/son/mon* — était violée une fois. Le
glossaire la signale comme « erreur récurrente à ne jamais reproduire » ; elle
l'était en effet.

#### Le he final se rend `h` — sauf quand il est directionnel

**Décision de l'auteur du 8 septembre 2026.** Le ה final se translittère `h` :
*Chavah*, *Sarah*, *Amorah*, *Yonah*, *Mikhah*, *Nehemyah*.

**Ce he ne se prononce pas, et la règle tient quand même.** C'est le point que
l'auteur a soulevé le jour même, et il faut l'inscrire ici parce que la section
voisine dit le contraire ==pour une autre lettre==.

Le ה final est ==une mater lectionis== : une lettre-support, qui porte la
voyelle sans ajouter de son. *Sarah* se dit *sa-RA*, *emunah* *e-mou-NA*,
*Mosheh* *mo-SHÉ*. Le `h` y note ==la lettre==, non ==le son==.

Les deux décisions du 8 septembre reposent donc sur ==deux principes
distincts==, et les confondre conduirait à défaire l'une par l'autre :

| décision | ce qui la fonde |
|---|---|
| ayin final → `ʿ` | la ==phonétique== — il s'entend, avec patach furtif |
| he final → `h` | la ==graphie== — deux lettres qu'une seule écriture confondrait |

==La phrase « une lettre qui se prononce se translittère » ne vaut que pour le
ayin.== Appliquée au he, elle conduirait à ==retirer== le `h` final — l'inverse
de ce qui est décidé ici. Elle est écrite deux sections plus haut, et elle y est
juste ; elle ne s'étend pas.

**Le cas qui l'a éprouvée est le plus visible du corpus.** מֹשֶׁה finit par un
he : la règle donne donc `Mosheh`, appliqué le jour même, ==30 occurrences==.
`Moshe` aurait été une exception tacite sur le nom le plus reconnaissable —
c'est-à-dire exactement la forme de défaut que le §2.9 existe pour fermer. Une
exception peut se décider ; elle ne peut pas ==rester muette==.

Le corpus le faisait ==à 22 contre 14==, sans que rien ne le fixe — et les
quatorze divergences ne se voyaient pas, chaque nom étant cohérent avec lui-même.
C'est la forme que le §2.9 existe pour fermer, rencontrée une fois de plus sur
son propre terrain.

**Le cas qui tranche est une collision.** אֱלִישָׁ**ה**, fils de [[Yavan]] en
*Bereshit* 10, finit par un ==he==. אֱלִישָׁ**ע**, le **naviʾ**, finit par un
==ayin==. Deux lettres, deux noms, deux personnes. Les rendre tous deux par
`Elisha` ferait porter une seule graphie à deux **Shemot** distincts — ce que le
tableau des consonnes refuse déjà pour `ch`/`kh` et `k`/`q`.

**L'exception : le he directionnel.** סְפָרָה, en *Genèse* 10:30, n'est pas un
nom finissant par he — c'est *Sefar* ==plus le ה locatif==, celui qui dit « vers ».
Le même qui donne *Mitsraymah*, « vers Mitsrayim », et *hapetchah*, « vers
l'entrée ». ==Le ה n'appartient pas au nom==, il marque un mouvement.

On translittère alors le syntagme entier — `Sefarah` rend bien סְפָרָה —, mais
==la fiche garde le nom nu==, `Sefar`, parce que c'est lui le **Shem**.

**Cette exception a été trouvée en la ratant.** La passe avait produit `Sefarh`,
qui n'est ni le nom ni le syntagme. Deux coquilles préexistantes sont sorties du
même contrôle : `minchatoh` pour מִנְחָתוֹ, qui finit par un ==vav==, et
`tadsheh` pour תַּדְשֵׁא, qui finit par un ==alef==. ==Une règle qui se trompe
est plus lisible qu'une pratique muette== : elle produit une faute qu'on peut
voir.

#### Le het se rend `ch` partout, finale comprise

**Écrit le 8 septembre 2026, parce que la pratique existait sans la règle.**

Le tableau des consonnes donne ח → `ch` sans distinguer la position, et la
section sur l'alef pose une exception ==pour la finale==. On pouvait donc croire
que le het en avait une aussi. ==Il n'en a pas.==

**La raison est phonétique, et c'est la même qui fonde l'exception de l'alef.**
L'alef finale ne porte pas d'apostrophe parce qu'elle est ==quiescente== : elle
ne se prononce pas, elle sert de support graphique à la voyelle qui précède.

Le het, lui, ==se prononce en finale==. L'hébreu va même jusqu'à insérer une
voyelle pour qu'il le puisse : le ==patach furtif==, un /a/ qui se glisse avant
le het final quand la voyelle précédente ne le permettrait pas. On le voit dans
`רוּחַ` — **ruach**, et non « rouh » —, dans `מִזְבֵּחַ` — *mizbeach* —, dans
`יָרֵחַ` — *yareach*.

==Une lettre qui se prononce se translittère.== L'exception de l'alef ne
s'étend donc pas au het, et il n'y a pas de règle du het final à part : il y a
==la règle du het==, qui vaut partout.

**Le corpus le faisait déjà, et massivement.** Relevé du jour sur les
appariements translittération/hébreu :

    het final rendu `ch`   54 occurrences, 32 formes   Noach, mizbeach, ruach, Metoushelach
    het final rendu `h`    17 occurrences,  9 formes   Terah, Shelah, Kelah, yareah

Et `Noach` seul paraît ==314 fois== dans le corpus. La pratique n'était donc pas
en balance : elle était établie ==à quinze contre un==, et les dix-sept
divergences ne se voyaient pas ==parce que rien ne les rendait comparables==.
C'est la forme exacte que le §2.9 a été écrit pour fermer, et il l'avait laissée
ouverte sur son propre terrain.

**La passe qui a suivi.** ==540 occurrences== reprises, 56 formes, 92 fichiers,
et vingt fiches de **Shemot** renommées avec elles — `Terah` → `Terach` (108),
`Haran` → `Charan` (89 — ==et c'était faux==, voir plus bas), `Nahor` → `Nachor`
(38), `Het` → `Chet` (30).

Trois choses en sont sorties, qu'il faut garder :

- ==deux collisions homographes assumées== — `Hevron` devient `Chevron`, et
  `hut` (חוּט, le fil) devient `chut`. Le contexte les lève, mais elles
  surprendront ;
- ==l'araméen est resté dehors== — `Chobabish`, `Shemichazah` : le §2.9 ne
  légifère que sur l'hébreu. ==Cette réserve est levée le jour même== : voir
  « Ce que cette règle ne tranche pas encore », où l'araméen rejoint le système.
  ==À trancher par l'auteur== ;
- ==un chantier annoncé qui n'existait pas==, et il vaut d'être gardé pour
  cela. J'avais relevé que `Chivi`, `Chamati`, `Chitti` et `Chorim` ont pour
  hébreu `הַחִוִּי`, `הַחֲמָתִי` — donc que la translittération ==avalait
  l'article==, et qu'il faudrait `ha-Chivi`.

  ==Le contexte le dément en une ligne :== le corpus écrit *les [[Chivi]]
  (\*Chivi\* / הַחִוִּי)*. ==Le français porte déjà l'article==, et l'hébreu cité
  porte le sien parce que le verset l'a. Écrire `ha-Chivi` donnerait *« les
  ha-Chivi »* — un article doublé. C'est le traitement de ==tous les ethnonymes==
  de la table des nations, het ou non : `Arvadi / הָאַרְוָדִי`,
  `Emori / הָאֱמֹרִי`.

  La convention se lit donc ainsi, et elle n'était nulle part écrite : on
  translittère ==l'article quand on cite un syntagme du verset== — `hazahav` pour
  הַזָּהָב, « l'or » —, et ==la forme nue quand on nomme un peuple ou une
  personne==, le français fournissant l'article. Le `ha-` du §2.6 vise autre
  chose : les noms que l'ONT ==forge== — *El ha-Qolossiyim*, **Ruach ha-Qodesh**,
  **ha-satan** —, où l'article fait partie du nom.

  ==C'est le second chantier fantôme de la journée==, après les « vingt-deux
  marqueurs déséquilibrés » du §13.2, et il a le même profil : un relevé bien
  formé, produit sans regarder ==une seule occurrence en contexte==.

**Et une quatrième, relevée deux jours plus tard : la passe avait fondu deux
Shemot.** ==La liste blanche avait pris un he pour un het.== Les 89 `Haran`
n'étaient pas le même mot :

    הָרָן   he    Gn 11:26, 27 (×2), 28, 29, 31   le fils de Terach, père de Lot
    חָרָן   het   Gn 11:31, 32 ; 12:4, 5           la ville où Terach s'arrête

Deux lettres, deux **Shem**, deux référents — ==une personne et un lieu==. La
passe les a rendus tous deux par `Charan`, et le corpus a porté deux jours
==une homonymie qu'aucun manuscrit ne connaît==. Pis : les gloses verrouillées
de *Bereshit* 11 se sont mises à ==l'expliquer== — « les deux formes sont
identiques en translittération française », « l'homonymie n'est pas fortuite
dans un texte où les **Shem** portent la destinée ». ==Un artefact d'outil relu
comme un fait du texte==, et commenté comme tel dans un fichier verrouillé.

**La règle qui l'interdisait était déjà écrite, une section plus haut.** Celle
du he final : *« אֱלִישָׁה, fils de [[Yavan]] en *Bereshit* 10, finit par un he. אֱלִישָׁע, le
**naviʾ**, finit par un ayin. Deux lettres, deux noms, deux personnes. Les
rendre tous deux par `Elisha` ferait porter une seule graphie à deux Shemot
distincts. »* ==Le même cas, sur l'initiale au lieu de la finale== — et la passe
l'a produit le jour même où cette phrase était écrite. Une règle n'empêche que
ce qu'on pense à lui soumettre.

**Ce que ça apprend sur l'instrument.** Une liste blanche protège de ce qu'elle
==exclut==, jamais de ce qu'elle ==inclut==. Celle-ci avait été bâtie pour que
*Pharaon*, *Euphrate* et *orphelin* ne soient pas touchés, et elle a tenu cette
promesse-là ; ==personne ne lui a demandé si les formes qu'elle contenait
étaient bien celles qu'elle croyait==. Le contrôle qui manquait ne coûtait rien
— ==regarder l'hébreu du mot avant de changer sa translittération== —, et c'est
lui qui a tranché la séparation : une requête sur `sources/he-wlc/Gen.jsonl`,
où les lemmes Strong séparent le 2039 du 2771a sans qu'on ait à en juger.

**Séparés le 10 septembre 2026**, sur décision de l'auteur : le fils redevient
`Haran`, la ville reste `Charan`. ==51 occurrences converties==, `lexique/Haran.md`
écrite, `lexique/Charan.md` rendue à la ville seule, et les gloses de *Bereshit*
11 qui expliquaient l'homonymie réécrites — ==elles disaient une chose qui
n'était plus vraie==.

**Une famille entière avait échappé au relevé, et la cause est instructive.**
`Yitshaq` (יִצְחָק) et les deux formes verbales de sa racine — `vayitshaq`
(וַיִּצְחַק, *et il rit*), `vatitshaq` (וַתִּצְחַק, *et elle rit*) — écrivaient
le het en `h`, ==24 occurrences dans 10 fichiers==. Corrigées en `Yitschaq`,
`vayitschaq`, `vatitschaq`.

Le filtre les avait manquées ==parce qu'il excluait tout `h` précédé de `s`, `c`
ou `k`==, pour ne pas compter les digrammes `sh`, `ch`, `kh` comme des het nus.
La garde était juste, et elle a créé un angle mort ==exactement là où la graphie
était ambiguë== : dans `Yitshaq`, `ts` + `h` se lit `tsh`, une suite qui
n'existe pas dans le système.

==C'est le meilleur argument pour la nouvelle graphie==, et il ne vient pas de
la règle mais de l'instrument : `Yitschaq` sépare ce que `Yitshaq` fondait. La
même glose de *Bereshit* 17 écrivait d'ailleurs `tsachaq` — juste — et
`vayitshaq` — faux — pour la même racine, dans la même ligne.

**Et le relevé du chantier `kh` était incomplet.** Trois formes portaient encore
un het écrit `kh` — `akhuzat` (7), `akhoranit` (2) —, corrigées avec cette
passe. Une troisième, `beiqekha` pour `בְּחֵיקֶךָ`, ==ne rend pas le het du
tout== : ce n'est pas une graphie fautive mais une omission. ==À reprendre.==

#### Ce que cette règle ne tranche pas encore

- ==La règle vaut pour l'araméen aussi== — décision de l'auteur du 8 septembre
  2026. C'est ==le même alphabet, les mêmes lettres, les mêmes valeurs==, et le
  corpus le faisait déjà sans que rien ne l'ait écrit : `chelmin` (חלמין),
  `chabala` (חבלא), `qebalah` (קבלה), `ovadkhon` (עובדכון) suivent tous le
  système. Deux mots seuls divergeaient, corrigés avec cette décision —
  `Chobabish` (חובבש) et `Shemichazah` (שמיחזה), qui écrivaient leur het en `h`
  et en `kh`.

  ==L'exception de `**ʿirin**` a été posée, puis retirée, puis remise.== Ce
  va-et-vient vaut d'être gardé parce qu'il montre ==deux critères qui ne
  posaient pas la même question==.

  Elle avait été posée le 7 septembre au motif que l'araméen marquerait le ayin
  initial. ==Le corpus la contredisait dans sa propre langue== — `ʿAzazel`
  (עזאזל) et `ʿovadkhon` (עובדכון) ont le même ayin initial et ne portaient
  aucune marque —, et le 8 septembre elle est tombée sur un critère
  ==linguistique== : le demi-anneau ne note pas une lettre, ==il coupe une
  syllabe==. Sans lui, `malʾakh` se lirait `malakh`, les deux `a` fondus. À
  l'initiale il n'y a rien à couper, donc rien à marquer.

  Le 9 septembre, l'auteur a adopté la convention savante entière, et la marque
  est revenue — ==non parce que le critère précédent était faux==, mais parce
  qu'il répondait à *qu'est-ce qui s'entend ?* quand la convention savante
  répond à *quelle lettre est là ?*. Le terme s'écrit `**ʿirin**`, et
  `ʿAzazel` et `ʿovadkhon` avec lui.

  *(La formule qui avait servi à écarter la convention savante — ==on ne prend
  pas la moitié d'un système== — est celle qui a fini par la faire adopter en
  entier.)*
- Les voyelles ne sont pas fixées ici. Le corpus écrit `e`, `a`, `o`, `i`, `ou`
  selon l'oreille, sans système déclaré, et rien n'a encore divergé.

#### Deux divergences relevées et corrigées

**`Khanokh` → `Chanokh`**, le 29 août 2026. חֲנוֹךְ commence par un **het**, donc
`Ch` — le seul mot du corpus qui écrivait le het en `kh`, sans doute par
contagion de « Hénoch ». 115 occurrences, et les dossiers `38. khanokh` des deux
arborescences renommés : le livre n'étant pas encore écrit, le renommage était
gratuit, exactement le moment que le §2.6 décrit pour les identifiants.

**Cinq formes, le 8 septembre 2026 — et la passe précédente n'était pas close.**
Relevé exhaustif du dépôt : ==101 occurrences== écrivaient un het en `kh`.

    khuqqah / Khuqqah / khuqqot   →   chuqqah / Chuqqah / chuqqot     92
    khazah  (חָזָה)                →   chazah                           4
    khemar  (חֵמָר)                →   chemar                           2
    Khanokh (חֲנוֹךְ)               →   Chanokh                          2
    khanak  (חָנַךְ)                →   chanak                           1

Les deux derniers `Khanokh` sont ==le reste de la passe du 29 août==, que ce
document annonçait pourtant terminée. Et `khanak` paraissait ==sur la même ligne
que `Chanokh`==, dans la glose qui en donne la racine : deux graphies du même
het, à quinze caractères l'une de l'autre, dans un fichier verrouillé.

**Ce que le relevé a écarté, et c'est la moitié du travail.** Un balayage
mécanique aurait corrigé quatre formes de plus, toutes à tort :

- `khen` — ==כֵן, un vrai khaf==. C'est la formule d'accomplissement du §2.4,
  *vayehi khen*. Dix occurrences justes, qu'un remplacement en masse aurait
  détruites ;
- `kha`, `khaf`, `khol`, `khshad` — ==tous des khaf== (כְּ, כ, כֹּל) ;
- `Kheruvim` et `Khalneh` figuraient ici ==à tort==, et la contradiction se
  voyait dans la ligne même : l'hébreu qu'elle citait — כְּרֻבִים, כַּלְנֵה —
  ==porte un dagesh==, donc un kaf occlusif, donc `k`. Corrigés le 8 septembre
  2026 en `Keruvim` (17 occurrences) et `Kalneh` (6), fiches renommées avec.
  ==Un relevé qui cite son propre contre-exemple sans le lire== ;
- `khata` — c'est ==le contre-exemple pédagogique== de la section ci-dessus, qui
  cite la graphie fautive pour l'interdire. La corriger aurait effacé la règle ;
- `chanikh`, `hanakh` — un het rendu ==par `h` seul==, ce qui est ==un autre
  chantier==. Voir ci-dessous.

Et `sessions/` est ==exclu du balayage== : ce sont les transcriptions de
conversations de l'auteur, où sa propre frappe est archivée. Trente-quatre
`Khanokh` y subsistent, et ils doivent y subsister — ==corriger l'orthographe de
ce que quelqu'un a tapé n'est pas une correction, c'est une réécriture==.

**Un chantier ouvert, mesuré et non traité : le het rendu `h`.** ==98
appariements== où l'hébreu porte un ח et la translittération un `h` sans `ch` —
*Terach* (תֶּרַח), *Nachor*, *Shelach*, *Chavila*, *Chobabish*, *mishpechotam*. Il est
==bien plus délicat== que celui-ci : le het y est souvent ==final==, et un het
final après voyelle ne se traite pas comme un het initial. Plusieurs de ces
formes sont en outre des noms propres déjà fixés dans des chapitres verrouillés.
==À trancher par l'auteur== : ce document ne dit rien du het final, et c'est
précisément le trou que le §2.9 avait vocation à fermer.

### 2.10 Les Shemot — la troisième couche, `[[Nom]]`

**Décision de l'auteur du 29 août 2026.** Les noms propres reçoivent leur propre
couche : ils deviennent **touchables** et portent chacun une fiche, aussi tenue
que celle d'un intraduisible — sans devenir des intraduisibles.

**Pourquoi ils ne sont pas des intraduisibles.** `**chesed**` reste en hébreu
parce que « bonté » rate quelque chose : le mot est *intraduisible*. `Avraham`
n'est pas intraduisible, il est **non traduit** — le §4.12 l'impose déjà, et
pour une autre raison. Confondre les deux ferait promettre au lecteur une fiche
de concept là où il y a un **Shem**.

**Pourquoi ils méritent mieux que l'accentuation.** Le bordeaux dit « ceci est
une personne, un lieu » et s'arrête là. Or un **Shem** *porte* — ==Avraham== est
« père d'une multitude », ==Chavah== « la vivante », ==Peleg== le partage,
==Bavel== la confusion. Le §3.2 le dit du **Shem** lui-même : *l'acte d'existence
fonctionnelle*, et *nommer c'est faire entrer dans l'ordre*. Une couche qui ne
contient que des Shemot mérite le nom de la chose qu'elle contient.

#### La marque

`[[Nom]]` — le lien natif d'Obsidian.

Il a été retenu sur trois faits, non sur le goût :

- il **se voit en écrivant**, comme `==…==` ; c'est le critère qui avait fait
  écarter une marque inventée ;
- le pipeline le **reconnaissait déjà** (`inline.rs`, étape 4 de sa grammaire) et
  le corpus n'en comptait **aucun emploi** — rien à migrer ;
- et il travaille pour le traducteur : `lexique/<Nom>.md` étant une vraie note,
  `[[ʾAvraham]]` devient ==cliquable dans Obsidian même==. On touche le nom dans
  l'éditeur, on arrive sur la fiche. Aucune autre marque ne fait ça.

#### Ce que chaque marque produit dans La Bible ONT

| écriture | rendu | touchable |
|---|---|---|
| texte nu | encre | non |
| `==mot==` | bordeaux `#862742` / `#D87994` | non |
| `[[Nom]]` | **terre brûlée `#603518` / `#AA7550`** | **oui** → fiche de **Shem** |
| `**mot**` | or, semi-gras | **oui** → fiche de lexique |
| `*mot*` | italique | non |

#### La couleur, et pourquoi celle-là

Le design system raisonne en écart perceptuel **CIE Lab**, avec un plancher
déclaré : *sous ΔE 25, une couleur ne se distingue plus de façon fiable dans un
texte courant.* La terre brûlée tient les trois écarts —

    ΔE 34 de l'or profond · ΔE 33 du bordeaux · ΔE 29 de l'encre

**Un vieil or aurait été plus beau, et il était impossible.** L'espace chaud est
déjà occupé : l'or tient le jaune-brun, le bordeaux le rouge, et tout vieil or
tombe entre les deux — bronze à ΔE 11 de l'or, brun doré à 17, cuivre à 20. Le
lecteur ne saurait plus si un mot doré est un concept ou un nom. La terre brûlée
est le ==seul ton chaud qui s'en sorte==, et elle y arrive en descendant assez
bas pour frôler l'encre.

Sur fond sombre elle remonte à `#AA7550`, à teinte constante — même logique que
le bordeaux qui devient `#D87994`, et pour la même raison : elle disparaîtrait
dans le noir.

**Deux exigences distinctes, et il faut les deux.** Le ΔE mesure l'écart *entre
marquages* — que l'or, le bordeaux et la terre brûlée ne se confondent pas. Le
**contraste** mesure l'écart *au fond* — que le mot se lise. Une couleur peut
tenir la première et manquer la seconde.

C'est arrivé ici : la première valeur de nuit proposée, `#A3704D`, tenait ses
trois ΔE et ne donnait que ==4,34:1== sur le thème sombre, sous le seuil AA du
WCAG. Relevé par la session iOS, qui a le jeton de fond que le vault n'a pas.
`#AA7550` donne 4,68:1 sur sombre et 4,95:1 sur mystique, tous les ΔE restant
au-dessus du plancher.

Contrastes des deux valeurs, sur les fonds où chacune sert :

    #603518   parchemin 9,57:1   clair 10,40:1
    #AA7550   sombre     4,68:1   mystique 4,95:1

Et une couleur ne se juge que sur **les fonds où elle sert** : mesurer la valeur
de nuit sur le parchemin ne veut rien dire, elle n'y paraît jamais.

**La valeur n'est pas commune entre les dépôts — seul le nom l'est.** C'est le
site qui l'a établi, en refusant de reprendre `#AA7550` sans la mesurer : sa
nuit est une aubergine `#18090D`, et sa surface de verset désigné `#261016`.
Sur celle-ci, `#AA7550` donne ==4,60:1== — au-dessus du seuil AA, mais très en
dessous du plancher que le site s'est fixé, ==6,5:1==, qui est celui de son
`encre-douce` et de son `accentuation`. Le Shem y serait ==la couleur la plus
faible du site==.

Il emploie donc `#BA8C6C` — même teinte à 24,4°, même saturation, clarté
relevée de 47,1 % à 57,6 % : 6,51:1 sur sa nuit, 6,04:1 sur sa surface.

**Et l'app l'a rejoint, par sa propre mesure.** Le relevé du site l'a fait
regarder le bon chiffre : `#AA7550` tenait AA à 4,66 sur son thème sombre, et
==aurait été le marquage le plus faible de ses thèmes sombres==, quand son or y
donne 9,80 et son bordeaux 6,15. Or son `ONTColors.swift` écrit du bordeaux
qu'il a été remonté à *« 6,1:1 — au-delà du seuil AA »*. ==Le projet s'est donc
donné un standard plus haut qu'AA, écrit nulle part et tenu partout.==

Le Shem s'y range : `#BA8C6C` des deux côtés, 6,12 sur sombre et 6,51 sur
mystique — à hauteur du bordeaux. Les deux dépôts ont convergé sur la même
valeur ==sans se la copier==, chacun l'ayant dérivée de son propre fond. C'est ce
que la règle prédisait, et le fait qu'ils tombent au même endroit ne la contredit
pas : ==leurs fonds sombres se ressemblent, leurs fonds clairs non==.

Ce n'est pas une divergence à réduire, c'est ==la bonne façon de faire==. Le
précédent existe déjà avec `mystique`, dont le site est la référence et l'app la
transposition. Ce qui doit être commun est ==la teinte et le nom de la couche== ;
la valeur se remesure sur chaque fond, et une valeur juste ici n'a aucune raison
de l'être ailleurs.

**Et la règle se démontre, elle ne s'affirme pas.** Le site a dérivé sa valeur
==en partant de la mauvaise== — je lui avais transmis `#A3704D`, écartée deux
jours plus tôt. Mise en teinte, sa dérivation tombe pourtant sur la ligne de la
valeur courante :

    #AA7550   l'app     teinte 24,7°   saturation 36,0 %   clarté 49,0 %
    #BA8C6C   le site   teinte 24,6°   saturation 36,1 %   clarté 57,6 %

Teinte et saturation identiques ==au dixième== ; seule la clarté bouge. Ce n'est
donc pas une autre couleur : c'est la même, ==avec la clarté remesurée sur le
fond d'arrivée==. La teinte a traversé intacte alors même que la valeur
transmise était fausse — ce que la règle prédisait, et qui se vérifie ici par le
calcul plutôt que par l'accord entre sessions.

**Et le gravier était que rien ne mesurait les couleurs.** Les feuilles de style
écrivaient leurs ratios ==en commentaire==, et aucun contrôle ne les relisait.
Le site a posé
`aucune_couleur_de_texte_ne_descend_sous_le_plancher_de_la_rampe`, éprouvée en
la faisant échouer sur la valeur fautive — un instrument validé sur un cas dont
on connaît la réponse.

#### Les fiches

Elles vivent dans `lexique/`, comme celles des intraduisibles, et suivent
**exactement** le §2.5 ter : sa forme — titres intermédiaires compris — et le critère des
six ==ruachim== — faire voyager le lecteur *à l'intérieur* de l'époque plutôt que
lui décrire l'époque du dehors.

Ce qu'une fiche de **Shem** doit porter, quand le corpus le donne : ce que le
nom veut dire, qui le porte et quelle fonction il tient, ce que le récit fait de
son sens, et — pour un lieu — où il se trouve et ce qu'il pèse dans le monde du
texte. Jamais l'article d'encyclopédie : la scène, comme partout ailleurs.

#### Une fiche de Shem n'est jamais finie

**Quand un livre est écrit, il faut repasser sur les fiches de ses Shemot.**
C'est un chantier récurrent, pas une passe unique, et il faut l'inscrire ici
parce que rien d'autre ne le rappellera.

La raison est dans la nature de la couche. Une fiche d'intraduisible porte un
mot, et un mot ne change pas quand le corpus grandit. Une fiche de **Shem**
porte ==une personne ou un lieu==, et une personne gagne un rôle chaque fois
qu'un nouveau livre la fait paraître.

Le cas de ==Chanokh== le montre. Sa fiche repose aujourd'hui sur quatre livres :
*Bereshit* 5 lui donne six versets, le *Sefar Gibbaraya* le montre en fonction —
scribe, médiateur, celui qui prononce le décret —, et l'intro de ce même livre
relève que l'*Igeret Yehudah* le ==cite nommément==. Le jour où 1 *Chanokh*
(n° 38) et l'*Igeret Yehudah* (n° 68) seront écrits, la fiche devra être reprise :
le personnage n'aura pas changé, mais ce que le corpus en dit, oui.

**D'où la règle d'écriture :** une fiche de **Shem** se termine en disant ==sur
quoi elle repose et ce qui reste à venir==. Elle ne prétend pas être complète —
elle déclare son assise. Un lecteur qui la touche dans deux ans doit pouvoir
voir qu'elle a été reprise, et pourquoi.

#### Un **Shem** de fonction n'est pas un **Shem** d'identité — 8 septembre 2026

**Décision de l'auteur.** La couche distingue désormais deux choses qu'elle
nommait pareil : un **Shem** qui nomme ==un porteur==, et un **Shem** qui nomme
==un office==.

**Ce qui les sépare, et ce n'est pas une nuance.** Un **naviʾ** et un **malʾakh**
font le même geste — recevoir un **davar** des *shamayim*, le porter sur
l'*eretz*. Ce qui diffère est ==le surplus== : le **naviʾ** ==excède== sa mission,
il a une vie entre deux **devarim**, un **basar** qui vieillit, une souffrance
qui authentifie ce qu'il porte. Le **malʾakh**, lui, ==est== sa mission, et rien
de plus : hors d'elle, il n'y a personne qui subsiste.

Donc un nom de **malʾakh** ne désigne pas quelqu'un. Il ==cristallise une
fonction== que **YHWH** a instituée — et c'est pourquoi ces noms finissent tous
par **ʾEl** et pointent vers lui, jamais vers celui qui les porte.

**Le corpus le dit lui-même.** *Juges* 13:18 : Manoach demande son nom au
**malʾakh**, qui refuse — il est *pele* (*pele* / פֶּלִאי), insondable. Ce n'est pas
une dérobade. ==Il n'a pas de nom d'identité à donner==, parce qu'il n'y a pas
d'identité derrière la fonction. À comparer avec Yaʿaqov qui devient Israel : là,
un **Shem** change ==parce qu'un porteur a changé==.

**Ce que la distinction change, et ce qu'elle ne change pas.**

- ==La marque ne bouge pas.== Un **malʾakh** nommé garde `[[Nom]]` et la terre
  brûlée. L'espace chaud est saturé (voir les ΔE ci-dessus) : une quatrième
  couleur n'y tiendrait pas, et le lecteur a besoin de savoir qu'il peut toucher.
- ==La fiche, elle, doit le déclarer.== Une fiche de **Shem** de fonction dit
  qu'elle nomme ==une charge et non une personne==, et se garde de la
  biographie — il n'y en a pas à écrire. Elle porte ce que la fonction fait, sa
  permanence, et vers quoi le nom pointe.
- ==Le critère est le surplus.== S'il y a quelqu'un entre deux missions, c'est un
  porteur. Sinon, c'est un office.

**Ce que la règle n'a pas tranché.** Les êtres célestes qui se sont nommés
==eux-mêmes== — ceux qui sont tombés — ne sont ni l'un ni l'autre : un nom
retourné vers soi, chez un être constitué pour la transparence. Le
*Sefar Gibbaraya* les fait déjà paraître, et leurs fiches existent. ==À reprendre
quand 1 *Chanokh* sera écrit.==

#### Ce que la couche ne prend pas

- **Les homographes restent à l'auteur.** `Shem` le fils de Noach est un
  **Shem** ; `**Shem**` l'acte d'existence est un intraduisible. Même mot, deux
  couches. La casse ne les sépare pas — c'est un arbitrage verset par verset,
  déjà signalé au §2.5 bis pour `Adam`.
- **Le niveau 3 ne double pas la marque.** Dans `(*Chanokh* / חֲנוֹךְ)`, le nom
  est déjà porté ; on ne le remarque pas.
- **`==…==` garde tout le reste** : les mots que le texte nomme solennellement
  (`==« Jour »==`), et les métadonnées d'apparat (`==premier emploi dans
  l'ONT==`). L'accentuation ne disparaît pas, elle cesse seulement de servir aux
  noms propres.

### 2.11 Les renvois entre chuqqot — la quatrième couche

**Décision de l'auteur du 8 septembre 2026.** Une chuqqah qui en cite une autre
la ==rend touchable==, et le renvoi porte sa propre couleur.

#### La marque : `((cible|libellé))`

**Décision de l'auteur.** Un renvoi vers une chuqqah s'écrit entre ==doubles
parenthèses== :

    La première chuqqah — ((l-olam-est-un-regard|L'olam est un regard)) —
    a posé que l'**ʿolam** est ==un rapport de perceptibilité==.

La cible joint, le libellé s'affiche — même convention que `[[…]]`.

**Pourquoi une marque neuve, alors que `[[…]]` existait.** La première rédaction
de cette section proposait de réemployer `[[cible|libellé]]` et de ==distinguer
sur la cible== : une fiche de `lexique/` donnerait un **Shem**, une chuqqah un
renvoi. ==C'était faux, et le pipeline le disait déjà.==

`inline.rs` émet tout `[[…]]` en `Shem` ==sans jamais regarder la cible==, et
son commentaire porte la raison :

> le vault porte des renvois vers des porteurs pas encore écrits : ce sont des
> marques de travail à faire, pas des erreurs

Distinguer sur la cible obligerait donc à ==résoudre avant de typer==. Et le
défaut serait exactement celui que ce principe prévient : ==un renvoi vers une
chuqqah pas encore écrite sortirait en **Shem**==. Or c'est le cas le plus
fréquent, puisque le corpus s'écrit.

==Une marque se détecte sur place. Une cible demande de savoir ce qui existe.==

**Ce que la marque coûterait, et pourquoi elle ne le coûte pas.** `((…))` n'est
==pas un lien Obsidian== : on ne saute plus d'une chuqqah à l'autre depuis
l'éditeur, comme on le fait avec `[[Nom]]` vers une fiche.

==Ce prix n'en est plus un==, et c'est un fait qu'il faut inscrire parce que
rien d'autre ne le dirait. **L'auteur ne lit plus le corpus dans Obsidian** : il
le lit ==dans la liseuse du Mac==, écrite pour cela. Le §2.10 avait retenu
`[[…]]` sur trois faits, dont *« il travaille pour le traducteur : `[[ʾAvraham]]`
devient cliquable dans Obsidian même »*. ==Ce troisième argument a cessé de
peser==, et il ne doit plus être invoqué pour trancher une marque.

Les deux autres tiennent, eux, et suffisent : la marque ==se voit en écrivant==,
et elle n'a ==rien à migrer==.

**Le voisinage est libre, vérifié.** ==Zéro occurrence== de `((…))` dans le
vault. Et la parenthèse simple, que le pipeline emploie pour le niveau 3
`(*translittération* / hébreu)`, ne mord pas : son parseur exige que le contenu
porte de l'==hébreu réel== (`has_hebrew`), ce qu'un renvoi n'a pas.

#### La couleur : un bronze, et pour la première fois la teinte ne traverse pas

    #953D0E   parchemin 6,55:1   clair 7,11:1     teinte  21°
    #D08C43   sombre    6,55:1   mystique 6,93:1  teinte  31°

**Le §2.10 posait que ce qui est commun est la teinte et le nom de la couche, et
que seule la valeur se remesure. ==Cette couche y déroge, et il faut dire
pourquoi.==**

L'auteur voulait un bronze. Le §2.10 l'avait écarté pour les Shemot — ==ΔE 11 de
l'or==, très sous le plancher de 25 —, mais la question se repose autrement pour
une quatrième couche, et elle a été ==remesurée== plutôt que déduite de la
première décision.

Le résultat est ==asymétrique==, et personne ne l'attendait :

- ==de nuit, le bronze passe==. 226 valeurs tiennent les quatre écarts et le
  plancher de 6,5:1. `#D08C43` donne ΔE 31 de l'or, 51 du bordeaux, 25 de la
  terre brûlée, 48 de l'encre ;
- ==de jour, aucune==. Le moins mauvais bronze manque des deux côtés à la fois —
  ΔE 24 pour 25, contraste 6,36 pour 6,5 — et ce n'est déjà plus un bronze.

**La raison est structurelle.** Sur fond clair, il faut être ==sombre== pour
tenir 6,5:1 ; or c'est exactement là que vit la terre brûlée des Shemot. Deux
bruns chauds ne peuvent pas occuper la même case de clarté. Sur fond sombre, il
faut être ==clair==, et l'or y est — mais un bronze plus saturé et plus orangé
s'en écarte assez.

D'où la valeur de jour : `#953D0E`, une ==sienne brûlée== à 21°. C'est ==la
teinte la plus proche du bronze== qui passe sans rien abaisser — dix degrés
d'écart, et tous les écarts confortables : or 38, bordeaux 38, terre 27, encre
56.

**Ce qui a été refusé, et pourquoi le dire compte.** Deux relâchements auraient
laissé passer un vrai bronze de jour, et les deux ont été mesurés :

- ==plancher ΔE ramené à 21== — `#8F4119` passe, mais son écart aux **Shemot**
  tombe à 21. Un nom propre et un renvoi dans le même paragraphe cesseraient de
  se distinguer, ce qui est précisément le défaut que la mesure existe pour
  prévenir ;
- ==contraste ramené au seuil AA de 4,5== — `#A0481C` passe, à 5,62:1 sur
  parchemin. Écarté : c'est le plancher qui sert le plus le lecteur, et le
  projet s'est donné 6,5 délibérément (§2.10).

**Et la valeur se remesure sur chaque fond, comme toujours.** Ces deux-ci sont
mesurées sur les fonds de l'app. Le site a sa propre nuit — une aubergine — et
devra dériver les siennes, ==en gardant les teintes 21° et 31°==, non les hex.

#### La forme : petites capitales, en plus de la couleur

**Décision de l'auteur.** Un renvoi s'affiche en ==petites capitales==, et il
garde sa couleur. ==Les deux, non l'une ou l'autre.==

Une petite capitale est une majuscule ==à la hauteur d'une minuscule== : le mot
n'est ni plus gros ni plus gras, seule sa ==silhouette== change.

    couleur seule        L'olam est un regard
    couleur + forme      L'ᴏʟᴀᴍ ᴇsᴛ ᴜɴ ʀᴇɢᴀʀᴅ

**Pourquoi la forme s'ajoute.** Les trois premières couches ne se séparent que
par la teinte, et c'est ==fragile== : dès que deux couleurs se rapprochent, tout
est perdu d'un coup — c'est exactement ce qui a bloqué le bronze de jour. Une
silhouette distincte fait que le renvoi ==se repère même sans distinguer sa
teinte==, sur un écran fatigué ou en lumière forte.

==La couleur ne devient pas facultative pour autant.== Elle reste ce qui dit au
lecteur que le mot est ==touchable==, comme dans les trois autres couches, et
les valeurs mesurées ci-dessus tiennent inchangées. La forme est ==un renfort,
non un remplacement==, et le plancher ΔE de 25 n'est pas relâché.

**Ce que la couche gagne d'être différente en nature.** Un renvoi ne pointe pas
vers un mot du texte — il pointe vers ==un autre énoncé==. Qu'il ne se
distingue pas seulement par la nuance mais par la ==forme== dit cette différence
d'espèce, là où l'or, le bordeaux et la terre brûlée désignent tous trois
quelque chose ==dans== la phrase.

**Deux points de rendu, pour la liseuse.**

- ==Employer `small-caps` et non `all-small-caps`==. Le premier abaisse les
  minuscules et ==garde les capitales existantes== — `L'ᴏʟᴀᴍ` plutôt que
  `ʟ'ᴏʟᴀᴍ`. Une capitale initiale conservée aide à lire, et la casse du titre
  reste vraie.
- ==Vérifier que la police porte de vraies petites capitales.== Sans elles, le
  moteur les ==simule== en rétrécissant des majuscules — le résultat est plus
  gras que le texte autour, plus étroit, et il trahit ce que la forme cherchait :
  un mot de même poids, de silhouette différente. Si la police du corps n'en a
  pas, ==il vaut mieux renoncer à la forme que la simuler==.

#### Ce que la couche attend encore

==Elle n'est pas rendue.== Le pipeline ne connaît pas encore `((…))`, et il
faut deux choses : un cas dans `inline.rs`, ==testé avant celui du niveau 3== ou
après lui indifféremment puisque `has_hebrew` les sépare, et un nœud dans
`schema.rs` — lequel fera ==rougir la compilation== des liseuses, qui devront le
rendre. C'est le bon sens de la dépendance : un type neuf prévient, un fichier
neuf non.

En attendant, ==ne pas écrire de renvois==. Le pipeline les laisserait tels
quels, et le lecteur verrait les parenthèses. Les six chuqqot nomment donc les
autres en toutes lettres, sans marque — ==c'est délibéré==, et cela se reprendra
quand l'émission saura les lire.


### 2.12 Comment se prononce ce qui est écrit

**Décision de l'auteur du 8 septembre 2026.** La translittération donne ==les
lettres==, jamais les sons — et rien dans le vault ne disait comment passer des
unes aux autres. Cette section le dit, et chaque fiche de `lexique/` en porte
l'application à son mot.

**Le besoin est réel et il vient de l'auteur lui-même** : il prononçait
`Chanokh` ==« cha-no-q »==, c'est-à-dire le `ch` de « chat » et le `kh` d'un
`q`. Les deux consonnes sont fausses, et ==rien dans la graphie ne l'en
avertissait==. C'est le défaut normal d'une translittération sans diacritiques :
elle est faite pour ==remonter à la lettre==, pas pour guider la bouche.

#### Les consonnes que le français n'a pas

Cinq sons demandent un geste que le français ne fait jamais. Ce sont eux qui
décident, et les autres suivent.

| lettre | ONT | où ça se produit | comment le faire |
|---|---|---|---|
| **ח** het | `ch` | ==le pharynx== | Serre le fond de la gorge comme pour souffler sur une vitre, et souffle. C'est ==un souffle raclé==, sans vibration. Le ح arabe. ==Jamais le « ch » de « chat »== — celui-là se fait avec la langue et les lèvres, à l'avant. |
| **כ ךְ** khaf | `kh` | ==le voile du palais== | Bien plus en avant que le het. C'est le *ch* de l'allemand *Bach*, la *jota* espagnole. La langue frotte contre le palais mou. |
| **ק** qof | `q` | ==la luette== | Un `k` produit ==tout au fond==, contre la luette. Ferme puis relâche là où le `k` français ne va pas. |
| **ע** ayin | *(rien)* | ==le pharynx, avec la voix== | Le même resserrement que le het, ==mais sonore== : les cordes vibrent. Un son plein, un peu étranglé. Il n'a aucun signe dans la graphie ONT hors position médiane. |
| **א** alef | *(rien)* | ==la glotte== | Le petit arrêt entre deux voyelles quand on dit « ah ! ah ! » en français. En finale, ==il ne se prononce pas== (§2.9). |

==Le het et le khaf sont le nœud==, parce que la graphie les sépare — `ch` et
`kh` — mais que l'œil français lit `ch` comme « chat ». **La règle à retenir :
dans l'ONT, `ch` ne fait jamais le son de « chat ».** Il fait toujours un souffle
de gorge.

#### Les consonnes qui ne surprennent pas

`b`, `d`, `g` (toujours dur, comme « gare »), `l`, `m`, `n`, `p`, `t`, `v`, `z`
se disent comme en français. `s` est toujours sourd — jamais le `z` de « rose ».
`sh` est le « ch » de « chat » : ==c'est lui qui porte ce son, non le `ch`==.
`ts` se dit d'un seul geste, comme dans « tsar ». `r` roule ou racle selon les
traditions ; ==aucune n'est fautive==.

#### Les voyelles

L'hébreu ancien n'écrivait pas ses voyelles ; les points ont été ajoutés bien
plus tard. Elles se lisent simplement, et ==aucune n'est nasale== — jamais le
« on » de « bon » ni le « an » de « banc ». Un `o` suivi d'un `n` se dit ==o-n==,
détaché.

    a   comme « patte »           i   comme « lit »
    e   comme « été » ou « mer »  o   comme « pot », jamais « bon »
    ou  comme « loup »            é/è  selon le signe, sans conséquence de sens

Deux points de plus, qui expliquent des formes du corpus :

- ==le shva== est une voyelle très brève, presque avalée, notée `e` dans l'ONT :
  *bereshit* se dit à peu près ==« be-ré-chit »==, avec un premier `e` fugitif ;
- ==le patach furtif== glisse un `a` avant un het ou un ayin final, pour qu'il
  puisse se prononcer. C'est lui qui fait **ruach** et non « rouh », et c'est la
  raison pour laquelle le het final s'écrit `ch` (§2.9).

#### L'accent tonique

Il tombe ==presque toujours sur la dernière syllabe==. C'est le contraire du
réflexe français, qui l'attire vers l'avant du mot.

    Chanokh      cha-NOKH        et non CHA-nokh
    Avraham      av-ra-HAM       et non a-VRA-ham
    Elohim       é-lo-HIM        et non é-LO-him

Quelques mots portent l'accent sur l'avant-dernière, et les fiches le signalent
au cas par cas.

#### Le cas de l'auteur, déplié

`Chanokh` — חֲנוֹךְ

    ח   het        souffle de gorge, pharyngal          [ħ]
    ֲ   patach     a bref                                [a]
    נ   noun       n                                     [n]
    וֹ   holam      o long                                [oː]
    ךְ   khaf       frottement contre le palais mou       [x]

Soit ==deux syllabes==, accent sur la seconde : un souffle raclé, `a`, `no`, et
un `kh` de *Bach*. Ce qu'il disait — « cha-no-q » — remplaçait le souffle de
gorge par un « ch » de langue, et le frottement de palais par une occlusion de
luette. ==Deux gestes justes, aux deux mauvais endroits.==

#### Ce que chaque fiche porte

Toute fiche de `lexique/` ouvre par une section ==Prononciation==, placée
==avant tout le reste== : le mot découpé en syllabes avec l'accent, chaque
lettre non triviale expliquée par ==le geste qui la produit==, et la faute
probable d'un lecteur francophone quand elle existe. Voir §2.5 ter.

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
| רָאָה | *raʾah/vayar* | examiner | Regard évaluateur du maître d'œuvre — inspection fonctionnelle. |
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
| חָטָא | *chata* | **chataʾ** | Intraduisible — ==le premier verbe intraduisible de l'ONT==, décision de l'auteur du 25 août 2026. L'acte de rater sa cible, de manquer sa marque : le tireur qui vise et dont la flèche passe à côté, l'homme qui marche et dont le pied ne trouve pas la pierre. Non « dévier », qui suppose une route dont on s'écarte — l'hébreu ne connaît pas la route, il connaît ==la cible==. Et surtout non « pécher » : le français a reçu ce mot chargé de faute morale, alors que **chataʾ** dit d'abord un ==manque d'ajustement==, un geste qui n'atteint pas ce à quoi il était destiné. Distinct de **raʿ**, qui est l'état dysfonctionnel : **chataʾ** est ==l'acte==, **raʿ** est ==l'état==. Les formes nominales suivent — **chattat**, **chataʾah**, **chataʾim**. Laissé en hébreu. |
| הָלַךְ | *halakh* | marcher | Se mouvoir, aller. Au ==hitpael== — *hithalekh* — il prend le sens d'==une marche partagée==, un aller-avec dans la durée : c'est la forme employée pour Chanokh et pour Noach. Le simple *halakh* dit le déplacement, le *hithalekh* dit ==la compagnie==. |
| מוּת | *mut* | mourir | Cesser de vivre. ==Non l'anéantissement== : le mort descend au **Sheʾol**, où il demeure dans le silence et l'attente. L'infinitif absolu redoublé — *mot tamut* (§4.16) — n'ajoute pas d'intensité mais ==la certitude== : mourir est ce que l'acte est. |
| יָדַע | *yadaʿ* | connaître | ==Connaître par participation==, en étant engagé dans ce qu'on connaît — d'où son emploi pour l'union conjugale en *Genèse* 4:1, qui n'est pas un euphémisme mais le sens plein. Donne la **daʿat**. Non « savoir », qui pose un regard extérieur. |
| שִׂים | *sim* | poser / placer | Déposer en un lieu assigné. ==Un geste de dépôt, non de construction== : ce qui est *sim* est mis à son poste. Distinct de *natan*, qui attribue, et de *banah*, qui édifie. |
| אָכַל | *akhal* | manger | Consommer. ==Le verbe de l'interdit du Jardin==, repris tel quel quand l'acte advient (*Genèse* 3:6) — le corpus ne change pas de mot pour dire que ce qui était défendu a eu lieu. Donne *okhlah*, la nourriture. |

### 3.2 Noms et concepts fondamentaux

| Terme hébreu | Translittération | Traduction ONT | Ce qu'il signifie |
|---|---|---|---|
| אֱלֹהִים | *Elohim* | Elohim | Laissé en hébreu — intraduisible sans perte. Pluriel hébreu avec accord grammatical singulier. Même traitement que Ruach, Nefesh, Neshamah. |
| אוֹר | *or* | Lumière | Non pas la lumière physique — l'Ordre lui-même. Ce qui rend toute distinction possible. |
| חֹשֶׁךְ | *choshekh* | Ténèbres | L'absence de toute lumière — donc l'impossibilité de distinguer quoi que ce soit. |
| תֹהוּ וָבֹהוּ | *tohu vavohu* | sans ordre ni fonction ni habitant | Un espace non nommé, non délimité, non assigné — présent matériellement mais inexistant fonctionnellement. |
| תְהוֹם | *tehom* | eaux primordiales | L'océan sans fond, sans limite, sans bord — les eaux d'avant toute ordination. Apparenté à Tiamat. |
| רוּחַ | *ruach* | Ruach | Intraduisible : souffle, vent, esprit — trois dimensions inséparables. Toujours laissé en hébreu. |
| רָקִיעַ | *raqiaʿ* | Voûte | Surface délimitante tendue entre les eaux d'en haut et d'en bas. |
| שָׁמַיִם | *shamayim* | Cieux | Ce qu'on voit au-dessus de nous. Étymologiquement "là où sont les eaux". |
| אֶרֶץ | *eretz* | Terre | Le domaine terrestre habitable — avec majuscule une fois nommé. |
| אֲדָמָה | *adamah* | sol concret | La glaise, la terre cultivable dans sa dimension physique. Même racine qu'Adam. |
| אָדָם | *adam* | l'Être façonné du sol (Bereshit 1-7) / **ʾadam** intraduisible (Bereshit 8+) | Bereshit 1-7 : traduit "l'Être façonné du sol" pour rendre visible l'étymologie adamah/adam. Bereshit 8+ : intraduisible — laissé en hébreu en gras. Dans les contextes légaux et covenantaux de Gn 9, ha-adam désigne l'humanité dans son universalité ; la périphrase complète brise les chiasmes et alourdit la formulation du droit divin. Décision actée en Bereshit 8, v.5. Extension : le critère est l'ère, non le livre — dans un récit hors *Bereshit* mais en régime antédiluvien (avant le **mabbul**, ex. *Sefar Gibbaraya*), la périphrase "l'Être façonné du sol" vaut également, car c'est l'ère de *Bereshit* 1-7. ==Distinction essentielle== : la périphrase rend le ==générique== *ha-adam* / *benei ha-adam* (l'humanité, l'espèce). Le ==nom propre== Adam d'un personnage individuel (ex. *Toledot Adam ve-Chavah*, où Adam et Chavah sont des personnes nommées) demeure un ==nom propre== (§4.12) — ni traduit, ni balisé, glosé à la première occurrence. |
| אִשָּׁה / אִישׁ | *ishah* / *ish* | Ishah / Ish | Intraduisible. Non pas "femme/homme" au sens social. L'ishah est édifiée (banah) pour faire face à l'ish — "os de mes os, chair de ma chair." Le lien ish/ishah est une alliance de l'être même. *Ishto* = sa ishah (forme possessive). *Eshet* = ishah de (forme construite). *Neshei* = pluriel construit. Laissé en hébreu comme Ruach et Nefesh. ==RÈGLE ABSOLUE — accord du possessif : toujours "ta/sa/ma ishah", jamais "ton/son/mon ishah" même devant voyelle. Le hiatus est délibéré — il rend le genre féminin visible. Erreur récurrente à ne jamais reproduire.== |
| נֶפֶשׁ | *nefesh* | Nefesh | Intraduisible. Non pas "l'âme" grecque — le principe vital concret et incarné. Toujours laissé en hébreu. |
| צֶלֶם | *tselem* | représentant fonctionnel | Statue représentative d'un roi. L'être humain est le tselem d'Elohim sur la Terre. |
| דְּמוּת | *demut* | modelé sur | Conformité au caractère et à la manière d'être d'Elohim. Renforce *tselem*. |
| שֵׁם | *shem* | Shem | Intraduisible. Non pas "le nom" au sens français — l'acte d'existence fonctionnelle lui-même. Nommer c'est faire entrer dans l'ordre. Laisser en hébreu comme Ruach et Nefesh. |
| טוֹב | *tov* | **tov** | Intraduisible. Non pas "beau" ou "moralement bien" : ce qui est pleinement ajusté à sa destination dans l'ordre cosmique, ce qui accomplit sa fonction. Opposé : **raʿ**. |
| טוֹב מְאֹד | *tov meʾod* | **tov meʾod** | Intraduisible. **tov** + *meʾod* (l'intensificateur de plénitude totale). Utilisé une seule fois dans Bereshit 1 — pour le cosmos entier dans sa totalité intégrée. |
| רַע | *raʿ* | **raʿ** | Intraduisible. Opposé fonctionnel de **tov** — ce qui rate sa destination, ce qui s'écarte de l'ordre cosmique. Non pas "le Mal" au sens moral grec. Formes : *ra* (adjectif/nom), *raʿat* (construit : "le ra de"), *raʿim* (pluriel). |
| מְלַאכָה | *melakhah* | œuvre architecturale | Travail qualifié de l'architecte. Même mot pour la construction du Tabernacle. |
| קָדוֹשׁ | *qadosh* | consacré / sacré | Mis à part fonctionnellement pour le domaine divin. Non pas "moralement pur". |
| נָבִיא | *navi* | **naviʾ** | Intraduisible. Celui que **YHWH** envoie porter son **davar** dans le temps visible. De la racine *nava* — être appelé, porter la parole d'un autre. Non « prophète » au sens que le français a pris : un devin, quelqu'un qui annonce l'avenir. Le **naviʾ** annonce parfois, mais ce n'est pas sa fonction — sa fonction est de ==lire l'alliance dans l'histoire== et de prononcer le **mishpat** sur ce qu'il y voit : où le peuple, le roi, le Temple sont alignés ou désalignés. Il regarde le présent avant le futur. Sa réalité fonctionnelle est celle du **shaliach**, l'envoyé : le grec les a décomposés en fonctions distinctes (§2.6, note terminologique), l'hébreu n'en connaît qu'une. Pluriel **neviʾim** — d'où *Gevurot ha-Neviʾim*, nom ONT du n° 44 : les **gevurot** de **YHWH** accomplies *à travers* ses **neviʾim**, où **YHWH** est le sujet et le **naviʾ** l'instrument. Laissé en hébreu. |
| קֹדֶשׁ | *qodesh* | **qodesh** | Intraduisible. La forme nominale de **qadosh** : non pas la qualité d'être pur, mais ==l'état d'être mis à part pour un office==. De la racine *qadash* — séparer, réserver. Un ustensile devient **qodesh** quand il cesse d'être disponible pour l'usage ordinaire ; un temps devient **qodesh** quand il est retiré du compte des jours utiles. Rien n'est **qodesh** par nature : tout l'est par assignation. Le mot appartient donc à la même famille d'opérations que **binah** — séparer entre —, et c'est ce qui le rend intraduisible : « sainteté » en français nomme une perfection morale, là où l'hébreu nomme une ==mise à part fonctionnelle==. Laissé en hébreu. |
| רוּחַ הַקֹּדֶשׁ | *Ruach ha-Qodesh* | **Ruach ha-Qodesh** | Intraduisible. La **Ruach** en tant qu'elle ==met à part== — non « le Saint-Esprit » (formule chargée de dix-sept siècles de dogmatique trinitaire, §4.7), non « souffle sacré » (qui en ferait une qualité au lieu d'une opération). L'article *ha-* porte tout le sens : ce n'est pas une **Ruach** parmi d'autres, c'est ==la== **Ruach**, celle de **YHWH**, désignée par ce qu'elle fait — elle sépare, assigne, consacre à un office. C'est la même **Ruach** qui repose sur le roi promis en *Ésaïe* 11:2 et qui y porte les six capacités : **chokhmah**, **binah**, **ʿetsah**, **gevurah**, **daʿat** et **yirat YHWH**. Formes attestées dans le corpus hébreu : *Psaumes* 51:13, *Ésaïe* 63:10-11. Traitement définitif réservé à son locus. Laissée en hébreu. |
| בְּרִית | *berith* | **berith** | Structure fonctionnelle d'engagement. Développé en Bereshit 8 : ici unilatérale — Elohim seul s'engage, Noach n'est pas invité à promettre. Non pas un contrat bilatéral mais une déclaration souveraine de fidélité permanente. Meqim (qum : faire se tenir) et non karat (couper) — l'alliance se tient debout par la parole d'Elohim seul. |
| נְשָׁמָה | *neshamah* | **Neshamah** | Intraduisible. Le souffle qu'**ʾElohim** insuffle dans les narines de **l'Être façonné du sol** — *vayipach beʾapav nishmat chayim*. À ne pas confondre avec la **Ruach**, qui est aussi le vent et l'esprit, ni avec le **Nefesh**, que les animaux ont également. La **Neshamah** est ==ce qui est donné de bouche à narines==, dans un geste de proximité que le corpus ne répète pour aucune autre créature. Non « l'âme » (catégorie grecque : une part détachable qui survit au corps). Premier emploi *Genèse* 2:7. Laissée en hébreu. |
| אֱמוּנָה | *emunah* | **ʾemunah** | Intraduisible. De *aman* (אָמַן) — être ferme, porter, tenir bon ; le mot dont vient *amen*. ==Ce sur quoi on peut poser son poids.== Non « la foi » au sens d'une opinion tenue pour vraie : l'**ʾemunah** n'est pas un contenu de croyance mais ==une posture d'appui==. Le verbe est un hiphil — *heʾemin*, traiter comme ferme, s'appuyer sur —, que l'ONT rend **ʾemuna** (sans h, délibéré). Même logique fonctionnelle que **teshuvah** et **yirah** : une manière de se tenir, non un sentiment. Premier emploi *Genèse* 15:6. Laissée en hébreu. |
| צַדִּיק | *tsadiq* | **tsadiq** | Intraduisible. Forme adjectivale de **tsedeq** : ==celui qui est ajusté à l'ordre juste==. Non « le juste » au sens moral — la **tsedaqah** n'est pas une vertu de caractère mais ==une conformité structurelle==, et le corpus le montre en appelant **tsadiq** un Noach qui finira ivre sous sa tente. Opposé fonctionnel : **rashaʿ**, celui qui est de travers. La paire est constitutive du droit divin hébraïque. Pluriel **tsadiqim**. Premier emploi *Genèse* 6:9. Laissé en hébreu. |
| צְדָקָה | *tsedaqah* | **tsedaqah** | Intraduisible. Forme nominale de **tsedeq** : ==l'état ou l'acte d'être ajusté à l'ordre==. Jamais « justice » (*dikaiosyne*, catégorie grecque) ni « justification » (catégorie théologique tardive) — deux rendus que toutes les traductions existantes emploient et que l'ONT refuse. Inséparable du **mishpat** : *tsedaqah umishpat*, l'ordre-juste et le jugement-juste, sont le couple du droit divin. C'est elle qui est ==comptée== à Avraham en *Genèse* 15:6, non gagnée par lui. Premier emploi *Genèse* 15:6. Laissée en hébreu. |
| מַבּוּל | *mabbul* | **mabbul** | Intraduisible. Le terme technique des eaux de *Bereshit* 6-9, et de nulle part ailleurs dans la Torah — le corpus ne l'emploie pour aucune autre inondation. Non « le déluge » (mot latin banalisé, appliqué à toute crue) : le **mabbul** est ==une dé-création temporaire==, le retour des eaux d'en haut et d'en bas sur un monde dont les écluses se rouvrent. Ce que *Bereshit* 1 avait séparé se remêle, puis la **Ruach** repasse sur les eaux comme au commencement. Premier emploi *Genèse* 6:17. Laissé en hébreu. |
| חֶסֶד | *chesed* | **chesed** | Intraduisible. La fidélité loyale envers celui à qui l'on est lié par une **berith** : tenir parole et agir pour son bien, dans la durée. Non pas "bonté" (trop faible — rate la loyauté engagée), ni "grâce" (catégorie théologique tardive de la faveur imméritée — importée, §4.7), ni "miséricorde" (le **chesed** est *dû* à l'intérieur d'un lien, non simple pitié). S'étend de la fidélité de **YHWH** envers les siens (*chasdo* — qui « dure **leʿolam** », *Tehilim* 136) jusqu'à la loyauté entre humains liés (Ruth envers Naomi). Premier emploi en *Genèse* 19:19 — le **chesed** qui garde le **Nefesh** de Lot. Même logique relationnelle qu'**ʾemunah** : une posture de fidélité, non un sentiment. Traitement définitif (plus ample) réservé à son locus central — *Exode* 34:6-7 (*rav chesed*) et *Ruth*. Laissé en hébreu. |
| עוֹלָם | *olam* | **ʿolam** | Intraduisible. De la racine "caché, dissimulé" : la limite temporelle que le regard humain ne peut pas discerner — l'horizon qui se dérobe. Non pas l'éternité abstraite des Grecs (*aeternitas*), mais ce qui est au-delà du visible. ==Règle de rendu en corps de texte : translittérer le construit en entier.== *Berit olam* → **berith-olam**. *Achuzat olam* → **ʾachuzat-ʿolam**. *Ledorot olam* → **ledorot-olam**. *Ad-olam* → **ʿad-ʿolam**. *Leʿolam* → **leʿolam**. *Meʿolam* → **meʿolam**. Premier emploi *Genèse* 3:22 (*vechai leʿolam*). |
| פָּנִים | *panim* | face | Non pas une surface neutre — une surface orientée vers, en relation avec. |
| מוֹעֵד | *moʿed* | temps fixé | Le rendez-vous sacré, l'assemblée convoquée. Non pas "saison". |
| חַטָּאת | *chattat* | **chattat** | Intraduisible. Forme nominale de **chataʾ** — le manquement lui-même, devenu une chose qu'on peut nommer. Personnifié en *Genèse* 4:7 comme une bête tapie à l'entrée, couchée et guettant : la **chattat** n'y est pas une abstraction morale mais ==une présence qui attend==. Jamais « le péché » (catégorie morale grecque, qui déplace le mot du manquement vers la culpabilité). Formes : **chattat**, **chataʾah** (*Genèse* 18:20), **chataʾim** (le pluriel adjectival, *Genèse* 13:13). ==Attention à la finale== : חַטָּאת se termine par un ==tav==, donc **chattat** — le corpus a longtemps écrit « chattah », qui est l'habit de l'autre mot, חַטָּאָה, finale en ==he==. Les deux existent en hébreu biblique et l'ONT emploie les deux : **chattat** en *Genèse* 4:7, **chataʾah** en *Genèse* 18:20. Corrigé le 28 août 2026. Laissée en hébreu. |
| מִנְחָה | *minchah* | tribut | Geste du vassal vers son suzerain — non pas encore un terme sacrificiel technique. Apporter un tribut c'est reconnaître une autorité supérieure. |
| אָרוּר | *arur* | frappé de dysfonctionnement | Opposé de *barakh* (doter) — non pas l'absence de dotation, mais sa perversion. La dotation demeure mais devient dysfonctionnelle. Le serpent continue de se mouvoir, l'adamah continue de produire, Qayin continue de vivre : mais tout cela est atteint dans sa fonction. |
| קַלֵּל | *qallel* | retirer de sa kavod | De *qalal* — alléger, réduire le poids fonctionnel. Non pas supprimer totalement : l'adamah conserve de la kavod après *Bereshit* 3, elle fonctionne encore. *Qallel* allège — il ne vide pas. Opposé exact de *barakh* (doter, alourdir de capacité). Première occurrence *Genèse* 8:21 — YHWH promet de ne plus en retirer davantage. |
| כָּבוֹד | *kavod* | kavod | Intraduisible. De *kaved* (כָּבֵד) — être lourd, peser. La pesanteur fonctionnelle d'une réalité dans l'ordre cosmique : sa substance, son poids d'existence, sa densité dans l'ordre divin. Opposé de *qalal* (légèreté, vide). S'étend de la kavod d'une réalité créée jusqu'à la kavod de YHWH lui-même — la même racine, la même logique de pesanteur fonctionnelle. Laissé en hébreu. |
| חָכְמָה | *chokhmah* | **chokhmah** | Intraduisible. La compétence qui fait aboutir. Non « sagesse » — la sagesse grecque contemple, la **chokhmah** *opère* : elle est ce dont Betsalel est rempli pour bâtir le Mishkan (*Exode* 31:3), ce qu'ont le tisserand, le marin, le forgeron. Savoir-faire qui ajuste une chose à sa destination — l'opération dont **tov** est le résultat constaté. Première des six ==ruachim== de *Ésaïe* 11:2, appariée à **binah**. Laissée en hébreu. |
| בִּינָה | *binah* | **binah** | Intraduisible. Le discernement qui ==sépare entre==. De *bin* (בִּין), apparenté à *bein* (בֵּין) — « entre ». Non « intelligence » ni « compréhension » : la **binah** ne saisit pas un contenu, elle trace une frontière — le geste même par lequel **ʾElohim** sépare la lumière de l'obscurité en *Bereshit* 1. Elle est à la **chokhmah** ce que distinguer est à réussir. Deuxième des six ==ruachim== de *Ésaïe* 11:2. Laissée en hébreu. |
| עֵצָה | *etsah* | **ʿetsah** | Intraduisible. Le dessein arrêté. De *yaʿats* (יָעַץ) — délibérer, résoudre. Non « conseil » au sens d'un avis qu'on donne et qu'on peut écarter : l'**ʿetsah** est le plan qu'on a *résolu* de tenir, et qui engage celui qui l'a formé. Terme du Conseil Divin, où l'**ʿetsah** de **YHWH** se forme et tient. Troisième des six ==ruachim== de *Ésaïe* 11:2, appariée à **gevurah** — le dessein et le pouvoir de l'accomplir. Laissée en hébreu. |
| גְּבוּרָה | *gevurah* | **gevurah** | Intraduisible. La capacité d'accomplir. De *gabar* (גָּבַר) — l'emporter, prévaloir ; même racine que **gibbor**, et la distinction est le cœur de l'entrée : le **gibbor** est *celui qui pèse*, la **gevurah** est *le pouvoir de faire aboutir*. Non « force » (physique) ni « puissance » (domination) : la **gevurah** ne se mesure pas à ce qu'elle écrase mais à ce qu'elle mène à terme. Pluriel **gevurot** — les actes où elle se manifeste, d'où *Gevurot ha-Neviʾim*, nom ONT du n° 44 (§2.6). Quatrième des six ==ruachim== de *Ésaïe* 11:2. Laissée en hébreu. |
| דַּעַת | *daʿat* | **daʿat** | Intraduisible. Le connaître par participation. De *yada* (יָדַע) — connaître en étant engagé dans ce que l'on connaît. Non « connaissance » : le savoir français est un regard *extérieur* posé sur un objet, la **daʿat** suppose d'être ==à l'intérieur==. D'où son emploi pour l'union conjugale en *Genèse* 4:1, qui n'est pas un euphémisme mais le sens plein. C'est la **daʿat** de l'arbre — *etz hadaʿat tov vara*, *Genèse* 2:9 — et ce que l'arbre propose n'est pas un contenu de plus, c'est une *modalité* : juger l'ordre depuis le dehors au lieu d'y participer. Cinquième des six ==ruachim== de *Ésaïe* 11:2. Laissée en hébreu. |
| יִרְאָה | *yirah* | **yirah** | Intraduisible. La reconnaissance de sa place devant ce qui dépasse. De *yare* (יָרֵא). Non « crainte » ni « peur » — ce n'est pas un affect mais une ==posture==, celle qui se tient au rang qui est le sien devant **YHWH** ; même logique fonctionnelle qu'**ʾemunah** et **teshuvah**, qui ne sont pas non plus des sentiments. Forme construite **yirat YHWH**. Sixième des six ==ruachim== de *Ésaïe* 11:2 — et *Ésaïe* 11:3 les scelle par un jeu de racines que toute traduction perd : *vaharicho* (וַהֲרִיחוֹ), « il respirera », vient de רו״ח, les consonnes mêmes de **ruach**. Les six capacités se referment sur le souffle qui les portait. Laissée en hébreu. |
| טָהוֹר / לֹא טָהוֹר | *tahor* / *lo tahor* | Tahor / lo tahor | Intraduisible. Non pas "pur/impur" au sens moral ou hygiénique — pureté fonctionnelle rituelle : ce qui peut entrer en contact avec le domaine sacré sans le perturber, et ce qui ne le peut pas. Première occurrence en *Genèse* 7:2 — catégorie déjà opératoire avant le Sinai. Laissé en hébreu dans le corps du texte, expliqué dans les gloses. |
| עֹלָה | *olah* | Olah | Intraduisible. De *alah* (עָלָה) — monter, s'élever. L'offrande qui monte vers Elohim dans la fumée. Jamais "holocauste" (terme grec chargé d'histoire moderne) ni "burnt offering" (catégorie rituelle chrétienne). Premier emploi en *Genèse* 8:20 — acte inaugural après la re-création. Laissé en hébreu dans le corps du texte, expliqué dans les gloses. |
| מִזְבֵּחַ | *mizbeach* | autel | De *zavach* — égorger, sacrifier. Littéralement "le lieu d'égorgement". Traduit "autel" avec niveau 3 obligatoire à chaque première occurrence dans une Fondation : ==autel== (*mizbeach* / מִזְבֵּחַ). |
| כֹּהֵן | *kohen* | Kohen | Intraduisible. Non pas "prêtre" (catégorie romaine/catholique anachronique qui réduit le terme à la fonction sacrificielle). Le **kohen** hébreu est l'intermédiaire fonctionnel qui maintient l'interface entre le domaine humain et le domaine divin — il tient les deux côtés ouverts l'un à l'autre. Pluriel : **kohanim**. Forme construite : *kohen* de/de l'alliance. Premier emploi en *Genèse* 14:18 — Malki-tsedeq, **kohen** de **ʾEl ʿElyon**. Central dans tout Vayiqra. Laissé en hébreu. |
| צֶדֶק | *tsedeq* | tsedeq | Intraduisible. L'ordre juste cosmique, la conformité structurelle au bon fonctionnement de la réalité. Non pas "justice" au sens moral grec (*dikaiosyne*). Trois formes intraduisibles issues de cette racine : **tsedeq** (le concept), **tsadiq** (l'adjectif : celui qui est dans l'ordre juste — premier emploi Genèse 6:9), **tsedaqah** (la forme nominale : l'état ou l'acte de juste-ordre — premier emploi Genèse 15:6). |
| רָשָׁע | *rashaʿ* | **rashaʿ** | Intraduisible. L'opposé fonctionnel de **tsadiq** : celui dont l'existence est structurellement déviée de l'ordre cosmique. Non pas "méchant" au sens moral subjectif — celui qui est de travers dans l'ordre fonctionnel. La paire **tsadiq**/**rashaʿ** est constitutive du droit divin hébraïque et de tout le corpus des Neviʾim. Pluriel : **reshaʿim**. Premier emploi en *Genèse* 18:23. |
| אֲדֹנָי | *Adonai* | Adonai | Intraduisible. De *adon* (אָדוֹן) : le maître, le seigneur — *Adonai* = "mon seigneur/maître". Titre de maîtrise souveraine absolue adressé à **YHWH**. Distinct d'**ʾElohim** et de **YHWH**. Dans l'usage liturgique hébreu, *Adonai* deviendra la substitution prononcée pour **YHWH**. S'écrit seul ou combiné : **ʾAdonai** **YHWH**. Premier emploi en *Genèse* 15:2. |
| אֵל | *El* | **ʾEl** | Intraduisible depuis le 31 août 2026. Le nom du dieu au sommet de l'ordre, au ==singulier== — la forme que tout le Levant partage, et derrière laquelle **ʾElohim** est le pluriel. Non « Dieu » : le mot français arrive chargé de dix-sept siècles de dogmatique, quand *El* ne dit qu'==une place== — celui qui assigne, celui dont dépend ce qui ne dépend de rien d'autre. C'est ce partage du mot avec les voisins qui rend possible la scène de *Bereshit* 14 : Malki-tsedeq bénit par **ʾEl ʿElyon**, et Avram répond en identifiant ce nom à **YHWH** — l'échange n'a de sens que si les deux hommes emploient ==le même mot==. Il vit surtout ==dans les Shemot== : Mikhaʾel (« qui est comme **ʾEl** ? »), Rafaʾel (« **ʾEl** guérit »), Yishmaʿel (« **ʾEl** entend »), Israel, Bet-El. Composés déclarés à part : **ʾEl ʿElyon**, **ʾEl Roï**, **ʾEl Shaddai**. Laissé en hébreu. |
| אֵל עֶלְיוֹן | *El Elyon* | El Elyon | Intraduisible. *Elyon* de *alah* (עָלָה) : monter, s'élever — El le Souverain élevé, l'El au sommet de l'ordre cosmique. Titre du dieu suprême dans les cosmologies proche-orientales voisines. En *Bereshit* 14, Malki-tsedeq l'emploie, Avram l'identifie à **YHWH** : **YHWH** **ʾEl ʿElyon**. Laissé en hébreu. |
| אֵל רֳאִי | *El Roï* | El Roï | Intraduisible. De *El* (אֵל) + *roʿi* (רֳאִי) de *raʾah* (voir) : "El qui me voit", "El de la vision de moi". Nom divin unique dans toute la Bible — donné une seule fois, par Hagar, une servante égyptienne en fuite dans le désert. Première et unique occurrence en *Genèse* 16:13. Laissé en hébreu. |
| אֵל שַׁדַּי | *El Shaddai* | El Shaddai | Intraduisible. Étymologie débattue : *shadad* (שָׁדַד) : puissance absolue ; ou akkadien *šadu* : montagne ; ou *she-dai* (שֶׁ-דַּי) : "Celui-qui-suffit". Ce nom accompagne les moments où **YHWH** accomplit l'impossible humain. Premier emploi en *Genèse* 17:1. Laissé en hébreu. |
| מַלְאַךְ | *malʾakh* | malʾakh | Intraduisible. Non pas "ange" (catégorie grecque anachronique). L'envoyé-fonctionnaire de **YHWH** — de la racine *laʾakh* (envoyer, déléguer) : celui que **YHWH** mandate pour accomplir un acte dans le monde humain. Il n'est pas défini par sa nature mais par sa mission. Ambiguïté délibérée du texte : le **malʾakh** **YHWH** parle parfois en son propre nom, parfois comme **YHWH** lui-même. Pluriel : **malʾakhim**. Forme combinée : **malʾakh** **YHWH**. Premier emploi en *Genèse* 16:7. ==Malʾakhim nommés== : quand un envoyé céleste porte un nom (Mikhaʾel — premier de l'ONT, *Toledot Adam ve-Chavah* ; Rafaʾel — *Sefar Gibbaraya*), c'est un ==nom propre== (sans gras, niveau 3 + glose à la première occurrence, §4.12), non un intraduisible — il garde la fonction de **malʾakh**. Tout nouvel être céleste nommé se décide avec l'auteur (règle des termes chargés). |
| קָנָה | *qanah* | fonder et maîtriser | Double dimension inséparable dans l'hébreu antique : créer/fonder ET acquérir/posséder. *Qoneh shamayim vaʾarets* = "fondateur et maître des Cieux et de la Terre" — formule du dieu suprême dans les textes proche-orientaux. |
| שָׁלִיחַ | *shaliach* | **shaliach** | Intraduisible. De *shalach* (שָׁלַח) — envoyer, mandater. L'envoyé-mandaté : celui qui porte l'autorité de celui qui l'envoie et agit en son nom. Équivalent hébreu exact du grec *apostolos* — jamais "apôtre" dans l'ONT. Le *shaliach* est défini par sa mission, pas par son statut. Pluriel : *shlichim* (שְׁלִיחִים). Même logique fonctionnelle que *malʾakh* : défini par l'envoi, pas par la nature. |
| שִׁפְחָה | *shifchah* | **shifchah** | Intraduisible. La servante attachée à la sphère d'une **ʾishah** — non « servante » au sens d'un emploi qu'on occupe, mais une ==position dans une maison==. La **shifchah** appartient à la sphère de sa maîtresse, et c'est ce qui la rend disponible pour un acte qu'aucun contrat de travail ne prévoit : être donnée en **ʾishah** seconde afin d'engendrer au nom de la maîtresse — le droit familial proche-oriental le prévoit expressément (contrats de Nuzi). Distincte de l'*amah*, servante d'un **ʾish**, qui relève d'une autre sphère : les deux mots ne disent pas un rang mais ==à qui l'on est attaché==. Traduire « servante » efface cette appartenance, et avec elle ce que le récit met en mouvement — ==Hagar== ne change pas d'emploi, elle change de sphère. Premier emploi *Genèse* 16:1. Laissée en hébreu. |
| דָּבָר | *davar* | **davar** | Intraduisible. La parole ET la chose simultanément — en hébreu antique, la parole et la réalité qu'elle désigne sont le même mot. La distinction française parole/chose n'existe pas : **davar** est à la fois l'événement et la parole qui le nomme. Pluriel : **devarim**. *Devar YHWH* = le **davar** de **YHWH**. Premier emploi en *Genèse* 11:1 (*devarim achadim*). |
| מִילָה | *milah* | **milah** | Intraduisible. De *mul* (מוּל) : circoncire. L'acte par lequel le signe de la **berith** est incisé dans la chair. Non pas "circoncision" — le terme latin réduit l'acte à sa dimension physique et perd la dimension covenantale de l'inscription. Premier emploi en *Bereshit* 17. |
| גּוֹי / גּוֹיִם | *goy* / *goyim* | **goy** / **goyim** | Intraduisible. Le peuple-nation dans sa réalité territoriale, ethnique et politique constituée. Non pas "les nations" (abstraction) ni "les gentils" (catégorie religieuse tardive). Présent dès *Bereshit* 10 dans la table des nations ; terme actif de la promesse à Avraham en *Genèse* 17:4 (*av hamon goyim* : père d'une multitude de **goyim**). |
| עָרְלָה / עָרֵל | *orlah* / *arel* | **ʿorlah** / **ʿarel** | Intraduisible. De *aral* (עָרַל) : être couvert, non ouvert. La chair de l'**ʿorlah** est le lieu du signe de la **berith** ; mais le terme s'étend métaphoriquement : **ʿorlah** du cœur (*Deutéronome* 10:16), **ʿorlah** des lèvres (*Exode* 6:12), **ʿorlah** du fruit (*Lévitique* 19:23). **ʿarel** : celui qui a encore son **ʿorlah**, dont la chair n'a pas reçu le signe. Premier emploi en *Genèse* 17:11. |
| מִשְׁפָּט | *mishpat* | **mishpat** | Intraduisible. De *shafat* (שָׁפַט) : juger, rendre une décision. L'acte de jugement rendu dans l'ordre cosmique — la décision qui discerne et ordonne correctement les parties. Non pas "justice" au sens abstrait grec (*dikaiosyne*) : le **mishpat** est concret, situationnel. Inséparable de **tsedaqah** dans tout le corpus : *tsedaqah umishpat* — l'ordre-juste et le jugement-juste sont le couple constitutif du droit divin hébraïque. Pluriel : **mishpatim**. Premier emploi en *Bereshit* 18. |
| נָחַם | *nacham* | **nacham** | Intraduisible. Deux dimensions indissociables : être saisi au fond des entrailles — une émotion viscérale qui ébranle la totalité de l'être — ET reconsidérer depuis cet endroit affecté. Non pas un simple chagrin ni un simple changement d'avis. Même racine : le **shem** de Noach (*Genèse* 5:29 — *yenachameinu* : "il nous **nacham**era") et la consolation prophétique (*Ésaïe* 40:1 — *nachamu nachamu ami*). Appliqué à **YHWH** en *Genèse* 6:6 — le texte ne l'atténue pas. Premier emploi *Genèse* 5:29. |
| שֹׁפֵט | *shofet* | **shofet** | Intraduisible. De *shafat* (שָׁפַט) — même racine que **mishpat**. Celui qui exerce le **mishpat** dans une situation concrète : non pas le magistrat de tribunal (catégorie juridique moderne), mais celui qui rétablit l'ordre fonctionnel, qui discerne et ordonne. *Shofet kol haʾarets* ("le **shofet** de toute la Terre") — titre de souveraineté cosmique universelle de **YHWH** en *Genèse* 18:25. Le titre du livre *Shoftim* résonne directement : les **shoftim** d'Israël sont ceux qui exercent le **mishpat** de **YHWH** dans l'histoire concrète. Pluriel : **shoftim**. Premier emploi en *Genèse* 18:25. |
| שְׁאוֹל | *Sheʾol* | **Sheʾol** | Intraduisible. Le domaine bas où descendent les morts — non pas « l'enfer » (lieu de tourment, catégorie grecque/chrétienne tardive) ni « le séjour des morts » édulcoré. Le lieu du silence et de l'attente sous la Terre, où descend tout mort — **tsadiq** comme **rashaʿ** — dans la cosmologie hébraïque (§6). Opposé structurel de la montée de l'âme grecque : on descend au **Sheʾol**, on ne s'envole pas. Premier emploi dans l'ONT en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| תְּשׁוּבָה | *teshuvah* | **teshuvah** | Intraduisible. De *shuv* (שׁוּב) : se retourner, revenir. Le mouvement de retour vers **YHWH** **ʾElohim** — se réorienter vers la présence quittée. Non pas « repentance » (culpabilité subjective, §4.7) ni « pénitence » (mérite/satisfaction). Même logique fonctionnelle qu'**ʾemunah** — une posture relationnelle, non un sentiment. Premier emploi dans l'ONT en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| הַשָּׂטָן | *ha-satan* | **ha-satan** | Intraduisible. De *satan* (שָׂטָן) : accuser, s'opposer. **ha-satan** = *l'*accusateur, une ==fonction== du Conseil Divin (*Iyov* 1-2 ; *Zekharyah* 3) — non un nom propre : l'article défini « ha- » l'atteste. Non le « Satan » dualiste (dieu rival, principe métaphysique du mal), ni le serpent d'Eden (qui reste le *nachash* fonctionnel). Sa capacité à se transfigurer en lumière est corroborée par Shaul (2 Co 11:14). Traitement définitif réservé à *Iyov* ; introduit provisoirement en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| טְבִילָה | *tevilah* | **tevilah** | Intraduisible. De *taval* (טָבַל) : plonger, immerger. L'immersion de retour — passer par les eaux pour se retourner vers **YHWH** **ʾElohim** : le mouvement de la **teshuvah** rendu par le corps. Non « baptême » (catégorie chrétienne tardive) ni « pénitence » (mérite). Le mikveh du Second Temple ; l'immersion de Yohanan « pour la teshuvah » (Mc 1:4). Premier emploi dans l'ONT en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| מֶרְכָּבָה | *merkavah* | **merkavah** | Intraduisible. De *rakhav* (רָכַב) : monter (un char). Le ==trône-char== de **YHWH** **ʾElohim**, contemplé en vision — Yehezqel (Ez 1), mode de la traversée architecturale (Nistarot) ; Shaul ravi au troisième ciel (2 Co 12). Non un « chariot » ordinaire. Premier emploi en corps de texte en *Toledot Adam ve-Chavah*. Laissé en hébreu. |
| גַּן | *gan* | Jardin | De *ganan* (גָּנַן) — ==protéger, entourer==. Un espace ==clos et gardé==, non « la nature » : il a des bords, on peut en être chassé. Planté par **YHWH** **ʾElohim**, et confié à l'**ʾadam** pour qu'il le ==serve== et le ==garde== — deux verbes du service sacerdotal. Non *paradeisos*, le parc royal perse dont le grec a fait un séjour d'après la mort. |
| זֶרַע | *zeraʿ* | semence | Ce qui contient de quoi se continuer. Dit ==à la fois la graine et la descendance==, sans que l'hébreu sépare les deux — et c'est ce qui rend la promesse à Avraham lisible : le mot qui nomme le grain nomme la lignée. |
| תּוֹלְדוֹת | *toledot* | engendrements | De *yalad* (יָלַד) — enfanter. ==La formule qui structure tout *Bereshit*== : non une liste de noms mais ==ce qui est sorti de==. S'applique aussi aux Cieux et à la Terre (*Genèse* 2:4), ce qui interdit d'y voir une simple généalogie. |
| עֶרֶב | *erev* | soir | De *arav* (עָרַב) — ==se mêler== : le moment où les contours cessent d'être distincts. Non une position du soleil, ==une phase de la distinction== — ce qui est cohérent avec une Lumière posée trois jours avant les luminaires. |
| בֹּקֶר | *boqer* | matin | De *baqar* (בָּקַר) — ==examiner, discerner== : le moment où les choses redeviennent discernables. Apparié à *erev* dans la formule du §2.4, et les deux nomment ==le rythme de la distinction==, non le lever et le coucher. |
| חֵן | *chen* | faveur | De *chanan* (חָנַן) — ==se pencher vers==. Dit ==une seule chose== : l'initiative appartient à celui qui donne. Il ne dit ==rien== du mérite de celui qui reçoit — ni qu'il en avait, ni qu'il n'en avait pas. « Faveur imméritée » importe donc une catégorie que l'hébreu n'emploie pas ici (§4.7). |
| תֵּבָה | *tevah* | arche | ==Non un navire== : le mot ne désigne aucune embarcation ailleurs, et il n'y a ni gouvernail, ni voile, ni proue. Une caisse qui flotte. Le corpus ne l'emploie qu'ici et pour le coffret de Moshe sur le Nil — ==deux fois, deux sauvetages par les eaux==. |

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
| נְפִילִים | *nefilim* | **Nefilim** | Intraduisible. De *napal* (נָפַל) — tomber. Ceux qui sont tombés, ceux qui font tomber, ou les êtres de la chute : ==l'ambiguïté est délibérément maintenue==, le texte ne tranche pas. Jamais « géants » — la Septante a lu *gigantes* et l'imagerie a suivi, mais le mot ne dit rien de la taille. Ce sont des êtres ==sans identité fonctionnelle== : ni gardiens des Cieux ni serviteurs de la Terre, un poids déplacé entre les domaines que le franchissement de *Genèse* 6:1-4 a produit. Leur écho traverse le corpus — les **gibborim** du même verset, les ==Refaim== de *Bereshit* 14, ==Nimrod== « inauguration du **gibbor** » en *Genèse* 10:8, et tout le *Sefar Gibbaraya*. Premier emploi *Genèse* 6:4. Laissé en hébreu. |
| גִּבֹּר | *gibbor* | **gibbor** | Intraduisible. De *gabar* (גָּבַר) — l'emporter, prévaloir. Celui dont la force brute fait le poids dans l'ordre des hommes. Non « héros » (l'excellence grecque) ni « vaillant » (vertu morale) : le **gibbor** ne pèse ni par la sagesse ni par la fidélité, seulement par sa capacité de contrainte. Pluriel **gibborim** ; le corpus écrit aussi *gibor*. Équivalent araméen **gibbarayaʾ**, titre du livre n° 37. *Genèse* 6:4 les nomme *anshei ha-shem* — « les hommes du **Shem** » : leur renom est un **Shem** de démesure, non d'ordre, et c'est ce que le *Sefar Gibbaraya* retourne en plaçant ==Gilgamesh== parmi eux. Premier emploi *Genèse* 6:4. Laissé en hébreu. |
| זָכָר | *zakhar* | mâle | Terme ==fonctionnel et biologique==, non social. Employé pour les animaux comme pour l'humain, et c'est le point : *Genèse* 1:27 ne décrit pas des rôles mais ==une capacité d'engendrer==. Distinct d'**ʾish**, qui dit la relation. |
| נְקֵבָה | *neqevah* | femelle | De *naqav* (נָקַב) — ==percer==. Terme fonctionnel apparié à *zakhar*, et employé de même pour les bêtes. Distinct d'**ʾishah** comme *zakhar* l'est d'**ʾish** : ==le couple biologique n'est pas le couple relationnel==. |
| מְאֹרֹת | *meorot* | luminaires | De *or* (אוֹר), la Lumière du premier jour — ==mais ce ne sont pas la même chose==. Le verset 3 inaugure l'Ordre ; les *meorot* sont ==les instruments par lesquels il se mesure==. Délibérément non nommés « soleil » et « lune », qui sont des noms de divinités chez les voisins (§4.3). |

### 3.4 Les formes verbales hébraïques (*binyanim*)

L'hébreu biblique construit ses verbes sur sept formes (*binyanim*) qui modifient le sens d'une même racine. Ces formes apparaissent dans les gloses pour préciser comment un mot est construit et pourquoi son sens diffère de la racine simple. Référence pour le lecteur non-hébraïsant :

| Forme | Fonction | Exemple dans l'ONT |
|---|---|---|
| **Qal** | Forme simple active — l'action dans sa forme de base | *bara* (orchestrer) — Qal de ב-ר-א |
| **Niphal** | Forme passive ou réflexive — être fait / se laisser faire | *vayera* (se laissa voir) — Niphal de *raʾah* |
| **Piel** | Forme intensive active — action répétée, accomplie avec intensité | *dibber* (parla, adressé à) — Piel de *davar* |
| **Pual** | Forme intensive passive | — |
| **Hiphil** | Forme causative active — faire en sorte que / déclarer comme / traiter comme | *heʾemin* (emuna) — Hiphil de *aman* |
| **Hophal** | Forme causative passive | — |
| **Hitpael** | Forme réflexive-intensive — agir sur soi-même / marcher avec | *hithalekh* (marchait avec) — Hitpael de *halakh* |

Quand une glose écrit "hiphil de *aman*", elle dit : c'est la forme causative de la racine *aman* (être ferme) — soit "traiter comme ferme, s'appuyer sur". Quand elle écrit "niphal de *raʾah*", elle dit : c'est la forme passive-réflexive de *raʾah* (voir) — soit "se laisser voir, se révéler".

---

## 4. PRINCIPES DE TRADUCTION

### 4.1 Les gloses

Le lecteur occidental ne possède pas les réalités hébraïques en tête. Les gloses sont là pour expliciter ce que le lecteur hébreu comprenait implicitement par sa langue, sa culture et son vécu quotidien. Ce n'est pas de l'invention — c'est de la médiation culturelle nécessaire, dans la tradition des Targoums.

**Règle absolue :** On n'invente jamais — on explicite seulement dans les gloses.

**Une glose dit de quelle racine vient la forme.** Décision de l'auteur du
8 septembre 2026. Quand le niveau 3 porte une ==forme fléchie== et non le lemme,
la glose l'y ramène :

    ==formula== (*vayomer* / וַיֹּאמֶר) *[*vayomer* — de *amar* : la parole
    performative, qui accomplit ce qu'elle énonce]*

Le corpus le faisait déjà ==trente-huit fois==, sans que ce soit écrit —
*zeʿaqah* de *zaʿaq*, *vayitschaq* de *tsachaq*, *dibber* de *davar*. La règle
ne fait qu'en tirer la pratique.

**Elle double la déclaration de la fiche, et c'est voulu.** Elles ne servent pas
le même lecteur : la fiche sert ==celui qui touche== — et le pipeline qui
résout ; la glose sert ==celui qui lit== et veut savoir sur place, sans quitter
la page.

**Le sens du transport — décision de l'auteur du 30 août 2026.** *La restitution
ramène le monde antique vers le lecteur, jamais l'inverse.* Que le lecteur se
trouve porté à l'intérieur de l'époque est ==l'effet recherché==, et il est
glorieux quand il advient ; mais ce n'est pas le point de départ, et on ne peut
pas l'exiger de lui pour qu'il comprenne la page.

**Ce que cette règle décide en pratique : la densité de glose.** Elle se mesure
sur le lecteur qui arrive ==sans rien==, non sur celui qui sait déjà — et c'est
tout le piège, car ==celui qui écrit a fini par savoir==. À force de fréquenter
ce monde, l'implicite cesse de se voir : on le lit sans le remarquer, donc on ne
le glose pas, et l'on croit avoir été sobre quand on a été muet.

**D'où la contre-mesure, et elle est arithmétique.** La référence est *Bereshit*
4, verrouillé : ==2,69 gloses par verset== dans le corps. Une **parashah** qui
tombe très en dessous n'est pas plus sobre — elle a laissé l'implicite implicite.
Compter avant de clore coûte une commande, et c'est le seul contrôle qui ne
dépende pas de ce que le traducteur a fini par trouver évident.

**Et pour un livre dont le témoin est second, ce n'est pas la bonne mesure.**
Relevé du 9 septembre 2026, par la session du pipeline. La densité par verset
suppose de l'hébreu à commenter ; là où il n'y en a pas, elle punit le
traducteur pour un manque qui n'est pas le sien.

Le rapport qui sépare vraiment est ==gloses / niveaux 3== :

    livre                    vers.   gl/vers   n3/vers   gl/n3
    bereshit                   495      2,09      3,14    0,67
    chazon-avraham             157      1,04      0,25    4,21
    sefar-gibbaraya            180      0,36      0,46    0,78
    toledot-adam-ve-chavah     106      0,40      0,58    0,69

Lisez la dernière colonne. Le *Chazon Avraham* a ==le plancher de niveau 3 le
plus bas du corpus== — 0,25, structurel, il ne nous parvient dans aucune langue
qui soit la sienne — et il glose ==quatre fois== son niveau 3. Il a ==découplé
les deux==, ce que ce paragraphe demande.

Le *Sefar Gibbaraya* et *Toledot* glosent à 0,78 et 0,69 — ==le rapport de
*Bereshit*==. Ils se comportent comme un livre normal, c'est-à-dire qu'ils
glosent ==à proportion de l'hébreu disponible==, et l'hébreu disponible y est
presque nul.

==Ce n'est donc pas un manque d'effort, c'est un couplage.== Le réflexe est
juste — une glose autour d'un niveau 3 — et il ne peut rien produire dans un
texte qui n'a pas de niveau 3 à porter.

**La cible se dérive d'un pair, non de *Bereshit*.** 2,69 est la mesure d'un
récit dense en hébreu jouable, et rien ne dit qu'elle vaille pour un texte de
vision araméen. ==Le chiffre à viser est le `gl/n3` du *Chazon Avraham*, 4,21==,
parce qu'il vient d'un texte ==du même régime== et qu'il est ==déjà atteint dans
ce corpus==. Ce n'est pas une exigence théorique : c'est un seuil que le vault a
tenu une fois.

**L'arithmétique interne est une explicitation, non un apport.** Décision du
9 septembre 2026, prise sur les généalogies de *Bereshit* 5.

Additionner des nombres que le corpus donne ==n'importe rien du dehors== : cela
révèle ce que le texte contient déjà. Et une généalogie ne donne ==que== des
nombres — c'est sa forme entière. Un lecteur ancien qui recevait une liste
d'âges recevait quelque chose ==fait pour être compté==.

Trois exemples, tous vérifiés à l'unité :

    Metoushelach   187 + 182 + 600 = 969   il meurt ==l'année même des eaux==
    Lamekh         777 − 182 = 595         il meurt ==cinq ans avant==
    le mabbul      du 17/2 au 17/7 = 150 j des mois de ==trente jours==

**La condition est dans la formulation.** La glose dit ==ce que les nombres
donnent==, jamais ce que le texte dirait : *« la somme est là pour qui
compte »*, non *« le corpus enseigne que »*. ==Le corpus ne fait jamais la somme
lui-même==, et la glose ne doit pas le lui faire dire.

Ce qui reste interdit est inchangé : tirer un ==sens== du calcul. Que
Metoushelach meure l'année des eaux se constate ; ce que cela ==signifierait==
relève du commentaire, et le §4.9 demande de laisser le texte muet là où il
l'est.

*Le niveau 3 obéit à une autre logique et peut légitimement être plus rare* —
dans un livre qui ne nous parvient dans aucune langue qui soit la sienne, on
s'abstient là où la chaîne ne donne rien (§4.14). ==La glose n'a pas cette
excuse== : expliciter ne demande pas d'hébreu.

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

**Exemple appliqué :** En *Bereshit* 8, le *ruach* d'Elohim sur les eaux (v.1) reprend mot pour mot *Genèse* 1:2 — c'est la signature littéraire de la re-création. Ce chiasme décréation/re-création (les eaux montent → tout périt ; les eaux descendent → la Terre réapparaît) doit être rendu visible dans les gloses à chaque reprise lexicale significative.

### 4.9 Le silence narratif délibéré

Quand le texte hébreu lui-même ne commente pas une scène, les gloses doivent respecter ce silence. Ne pas surcharger de gloses ce que le texte a voulu sobre.

**Exemple appliqué :** Le corbeau et la colombe (*Genèse* 8:6-12) — deux envois d'oiseaux, aucun commentaire du narrateur. Le silence est le message. Les gloses restent minimales : on identifie les animaux (*orev* / עֹרֵב ; *yonah* / יוֹנָה) et on laisse le texte parler seul.

### 4.10 Les chiffres fonctionnels hébraïques

Certains nombres hébreux sont des **unités fonctionnelles**, non des durées physiques exactes. Signaler dans les gloses leur valeur fonctionnelle à leur première occurrence dans chaque contexte.

- **40** (*ʾarbaʿim* / אַרְבָּעִים) — unité de transformation : la durée qu'il faut pour qu'une réalité se transforme fondamentalement. 40 jours de pluie (Gn 7), 40 ans au désert, 40 jours de Moïse sur la montagne. Signaler : *[quarante — unité fonctionnelle hébraïque de la période de transformation]*.
- **7** (*shevaʿ* / שֶׁבַע) — unité de plénitude et d'accomplissement.

### 4.11 Restituer les ambiguïtés — ne pas résoudre ce que le texte ne résout pas

**Règle absolue :** Quand une construction hébraïque est structurellement ambiguë, l'ambiguïté est une information — elle doit être restituée, pas effacée. L'ONT restitue, il ne commente pas et ne tranche pas.

**Dans le corps du texte :** choisir une formulation française qui ne ferme pas l'ambiguïté quand c'est possible, ou qui la laisse suffisamment ouverte.

**Dans les gloses :** présenter explicitement toutes les lectures disponibles dans l'hébreu sans en choisir une. Formuler : "Le texte ne tranche pas", "L'hébreu laisse les deux lectures disponibles", "L'ambiguïté est dans la structure même de la phrase."

**Exemple appliqué :** *achi Yafet haggadol* (*Genèse* 10:21) — haggadol peut qualifier Yafet ("le frère de Yafet-l'aîné") ou qualifier achi ("le frère aîné de Yafet"). Le texte ne résout pas l'ordre de naissance — la glose présente les deux lectures sans trancher.

### 4.12 Les noms propres

**Règle absolue pour tout l'ONT :** Les prénoms et noms propres hébreux sont conservés dans leur forme hébraïque originale — jamais dans leur forme latine ou française traditionnelle.

- Qayin (jamais Caïn), Hevel (jamais Abel), Chavah (jamais Ève), Noach (jamais Noé), Avraham (jamais Abraham), etc.
- **Cette règle s'applique aussi aux noms géographiques :** Sedom (jamais Sodome), Amorah (jamais Gomorrhe), Yarden (jamais Jourdain), Chevron (jamais Hébron), Mitsrayim (jamais Égypte dans les renvois géographiques), Kenaʿan (jamais Canaan), etc. **Ethnonymes de même** : *Mitsri* (masc.) / *Mitsrit* (fém.) / *Mitsrim* (pl.) — jamais « Égyptien(ne) » (ex. « Hagar la Mitsrit », *Bereshit* 16 ; « les Mitsrim », *Bereshit* 12). Pour l'emploi **adjectival** (langue, culture, architecture d'un peuple), utiliser « de Mitsrayim » (ex. « fortifications de Mitsrayim », « titre royal de Mitsrayim »).
- **La règle vaut dans le corps du texte ET dans les gloses** — ne jamais écrire la forme française même dans une glose d'explication.
- Raison : les noms hébreux sont sémantiquement chargés — leur étymologie est partie intégrante du texte. Traduire le nom en efface le sens.
- **Règle absolue — niveau 2 ET niveau 3 obligatoires :** À la première occurrence de chaque nom propre dans chaque **parashah**, le nom doit porter à la fois son niveau 3 (translittération / הָעִבְרִית) ET sa glose (expliquant l'étymologie et la signification fonctionnelle du Shem). Exemple : Yafet (*Yafet* / יֶפֶת) *[de pata : étendre, élargir — son Shem porte la dotation que Noach lui formulera]*. Les occurrences suivantes du même nom dans la même unité n'ont pas besoin de répéter la glose — le nom seul suffit.
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

**On ne glose pas la syntaxe d'un passage que l'ONT a reconstruit.** Règle
écrite le 9 septembre 2026, sur un cas du *Sefar Gibbaraya*.

Plusieurs livres du corpus étendu ne nous parviennent qu'en fragments, et leurs
feuilles d'introduction disent lesquels de leurs versets ==suivent de près les
composantes attestées== et lesquels sont ==une expansion contrôlée==. Cette
distinction n'est pas un scrupule d'apparat : ==elle commande ce qu'une glose
peut dire==.

Sur un passage attesté, l'ordre des mots, le choix d'un passif, la place d'un
nom sont ==des faits du témoin== et se glosent comme tels. Sur une expansion,
ce sont ==des faits du restituteur== — et les commenter revient à ==prêter au
texte ancien une intention qui est celle de sa reconstruction==.

    ✗  « trois verbes de suite et pas un sujet — la lettre ne dit jamais qui »
    ✗  « l'ordre des mots est instructif : ici la place arrive avant le nom »

Ce qui reste permis, et qui est l'essentiel : ==gloser ce que le passage porte==
— la realia, le genre, les échos vers le corpus attesté, la logique du monde
qu'il met en scène. Ce sont des choses que la reconstruction ==transmet== ; sa
syntaxe est ce qu'elle ==ajoute==.

==Le contrôle est simple== : avant de gloser une forme, regarder si la feuille
d'introduction range ce verset parmi les composantes attestées ou parmi
l'expansion. Le §4.14 dit déjà de s'abstenir de niveau 3 là où la chaîne ne
donne rien ; ==la même prudence vaut pour la glose de forme==.

### 4.15 Le régime d'auteur

La notion antique d'auteur est **fonctionnelle**, non moderne-individuelle. Deux régimes :
- **Auteur attesté et de sa main** — identifiable, il a réellement produit le texte (ex. les *Igerot* de Shaul).
- **Auteur qui restitue** — le nom marque la *provenance et l'autorité* d'une vérité, non le scribe physique. Ce n'est pas une fraude : écrire sous un nom révéré déclare que la vérité appartient à ce courant.

Ainsi la Torah est mosaïque par **autorité**, non par chaque trait de plume : *Devarim* 34 raconte la mort de Mosheh, et *Bava Batra* 14b-15a le reconnaît depuis toujours (Yehoshua écrivit les derniers versets). Le régime d'auteur nomme *à qui la vérité appartient*, pas seulement *quelle main a tenu le calame*.

### 4.16 L'infinitif absolu — l'hébreu double le verbe, le français aussi

**Décision de l'auteur du 8 septembre 2026.** L'hébreu pose parfois le verbe
==deux fois== : d'abord à l'infinitif nu, puis conjugué — *mot tamut*
(מוֹת תָּמוּת), *harbeh arbeh* (הַרְבָּה אַרְבֶּה). Ce n'est pas une redondance de
style : la forme nue ==renforce== la forme conjuguée, et le français n'a pas
cette machine.

**La forme retenue : infinitif, virgule, verbe conjugué.**

    mot tamut        mourir, tu mourras
    akhol tokhel     manger, tu mangeras
    harbeh arbeh     multiplier, je multiplierai
    yadoaʿ tedaʿ     savoir, tu sauras
    hayo yihyeh      devenir, il deviendra

**Pourquoi l'infinitif et non le participe.** « Mourant, tu mourras » se lit
==pendant que tu meurs, tu mourras== : le participe français pose une
==simultanéité==. L'hébreu ne pose aucun temps — *mot* est une forme ==nue==,
sans personne et sans moment, qui nomme l'action sans la situer.

L'infinitif français fait ==la même opération==, et placé en tête il est une
vraie tournure d'insistance : *« Mourir, tu mourras »* se lit *« pour ce qui
est de mourir : tu mourras »*. Ce n'est pas un calque, c'est ==une
topicalisation== — exactement ce que l'hébreu fait en avançant l'infinitif.

**La valeur se dit dans la glose, jamais dans le corps.** La construction porte
==deux valeurs== selon le contexte, et le corps ne les distingue pas :

- ==la certitude== — *mot tamut* ne dit pas « tu risques de mourir » mais que
  ==cela aura lieu==. C'est le cas des verbes d'état ;
- ==l'intensité== — *harbeh arbeh* ne dit pas « il est sûr que je multiplierai »
  mais ==en très grande mesure==. C'est le cas des verbes de quantité.

Le corps double toujours de la même façon ; ==c'est la glose qui nomme la
valeur==. Le lecteur voit ainsi la même opération partout et apprend à la lire,
au lieu de rencontrer deux tournures françaises sans savoir qu'elles rendent
un seul geste hébreu.

**L'état où la règle a été trouvée.** ==Sept occurrences, six traitements== —
et deux versets consécutifs du même chapitre en portaient deux différents :

    akhol tokhel   Genèse 2:16   « tu peux manger en mangeant »      gérondif
    mot tamut      Genèse 2:17   « mourant, tu mourras »             participe
    lo mot temutun Genèse 3:4    « Mourants, vous ne mourrez pas »   participe pluriel
    harbeh arbeh   Genèse 3:16   « J'augmenterai grandement »        ==effacé==
    yadoaʿ tedaʿ   Genèse 15:13  « Sache, sache »                    impératif doublé
    harbeh arbeh   Genèse 16:10  « Je multiplierai, multipliant »    verbe + participe
    hayo yihyeh    Genèse 18:18  « deviendra vraiment »              ==effacé==

==Les gloses nommaient déjà la construction== là où le corps l'écrasait : celle
de 2:13 décrit le doublement de 2:12 ==et en donne le bon rendu==, que le corps
de 2:12 n'employait pas. L'apparat savait ; le corps ne suivait pas.

**Ce que l'effacement coûte, mesuré sur un cas.** En *Genèse* 3:4, le serpent
ne discute pas la parole du Jardin : ==il en reprend la forme==. *Mot tamut*
devient *lo mot temutun* — la construction qui portait l'irréversibilité de la
mort, retournée pour porter celle de la survie. ==Une contre-parole de puissance
formelle égale.== Rendre l'une par un doublement et l'autre par un adverbe
==efface l'affrontement== et laisse une simple contradiction de contenu.

**Deux coquilles sorties de la même passe.** Le corpus écrivait *akol tokhel* —
or אָכֹל porte un ==kaf sans dagesh==, donc `kh` (§2.9) : *akhol*. Et la même
formule s'écrivait *harbeh* en *Bereshit* 3 et *harba* en *Bereshit* 16. Le
premier mot de *yadoaʿ tedaʿ* perdait en outre son ==ayin final==.

### 4.17 Le regard qui évalue et le regard qui convoite

**Décision de l'auteur du 10 septembre 2026.** L'hébreu écrit cinq fois dans
*Bereshit* la même construction : `וַיַּרְא` + `אֶת` + objet plein + `כִּי` +
ce qui est constaté. Elle se rend ==en deux verbes==.

    examina [la chose] — et constata qu'elle était [ainsi]

**Pourquoi deux verbes.** La particule `אֶת` marque un ==objet direct plein==,
et sa présence installe ==deux temps== : le regard porte d'abord sur une chose,
le constat vient après, dans une seconde proposition. C'est ce que les
grammairiens nomment un ==objet proleptique== — du grec *prolêpsis*, la prise
par avance : l'objet est saisi en avance sur ce qui le décrira.

Le rendre d'un seul verbe — « vit que la chose était ainsi » — fond les deux
temps, ce que le français fait naturellement et que l'hébreu n'a pas fait. Les
deux rendus sont grammaticalement défendables ; ==le doublement est celui qui
respecte la construction==, et c'est lui qui est retenu.

**La variante en *vehinneh* prend un tiret**, et lui seul : `וַיַּרְא` + `אֶת` +
`וְהִנֵּה` donne « examina la Terre — et voilà qu'elle s'était corrompue »
(*Genèse* 6:12). ==Le tiret appartient à cette forme==, non à la forme en
*ki*, qui enchaîne sans lui (*Genèse* 1:4).

#### Et pourtant la règle ne vaut pas partout — c'est délibéré

**Décision de l'auteur, dans la même journée et dans le même souffle que la
précédente.** *Le vivant peut être singulier.*

Deux versets rendent cette construction ==d'un seul verbe==, et ils ont raison
de le faire :

| réf | qui regarde | ce qui suit immédiatement |
|---|---|---|
| *Genèse* 6:2 | les fils d'**ʾElohim** regardent les filles | « et ils ==prirent== des **ʾishah** » |
| *Genèse* 12:14 | les Mitsrim regardent l'**ʾIshah** | Sarai est ==emmenée== chez Pharaon |

La glose verrouillée de 6:2 en donne le motif, et il est ==narratif, non
syntaxique== :

> ce n'est pas le regard évaluateur du maître d'œuvre — c'est le regard de désir
> qui précède la prise

Celle de 12:14 va plus loin encore : elle ==insiste== sur le verbe unique —
*« tout le passage tient sur un seul verbe »*. L'ONT n'y a pas seulement écrit
un verbe : il a écrit une glose pour dire que le verbe unique ==est le point==.

**Le partage se lit donc ainsi**, et il n'est pas une exception à la règle mais
==une seconde règle, de rang narratif== :

- ==le regard qui évalue== — inspecter un ouvrage pour vérifier qu'il remplit sa
  fonction : deux verbes. C'est **ʾElohim** en 1:4 et 6:12 ;
- ==le regard qui convoite== — repérer ce qu'on veut avant de le prendre : un
  seul verbe. Il est toujours suivi d'une prise.

#### Ce que ce cas enseigne, et qui déborde très largement le verbe *raʾah*

**On ne fait pas des mathématiques linguistiques.** L'hébreu est ==une langue
vivante==, et ce qui est vivant peut être singulier : une règle du corpus n'a
pas à s'appliquer partout de la même façon pour être une règle.

C'est le cœur de ce qu'est l'ONT — ==une restitution==, qui transporte le
lecteur dans le passé pour que le sens lui parvienne au présent. Une restitution
sert le sens ; ==un système se sert lui-même==. Quand les deux divergent, c'est
le sens qui commande.

**D'où la marche à suivre, quand une construction identique paraît deux fois.**
Ne pas conclure de la syntaxe seule. Demander ==ce que la scène fait== :

1. **regarder ce qui suit le verset.** Un regard suivi d'une prise n'est pas un
   regard suivi d'une séparation ;
2. **regarder qui regarde.** Le sujet divin et le sujet humain n'accomplissent
   pas le même acte sous le même mot ;
3. **regarder ce que les gloses du corpus disent déjà.** Elles portent souvent
   l'arbitrage, écrit par l'auteur, avant que la règle ait été formulée.

**Le contrôle qui aurait évité l'erreur du 9 septembre**, où *Genèse* 13:10 a
été aligné sur 1:4 au motif que la syntaxe était identique : ==une règle
syntaxique ne se vérifie pas sur la syntaxe==. Elle se vérifie sur toutes ses
occurrences, en regardant ce que chacune raconte. Sur cinq occurrences, quatre
étaient déjà tranchées et deux d'entre elles disaient l'inverse de la règle
qu'on croyait appliquer.

---

## 5. CE QUI DISTINGUE L'ÊTRE HUMAIN DE L'ANIMAL

Point capital pour tout le reste de la Bible :

- **Le Nefesh** (*nefesh chayah*) — commun à l'être humain ET à tous les animaux. Ce n'est pas ce qui distingue l'homme.
- **Le Tselem** (*tselem elohim*) — exclusif à l'être humain. C'est le mandat de représentant fonctionnel d'Elohim sur la Terre. Ce qui distingue l'homme de l'animal n'est pas son âme (catégorie grecque) mais sa **fonction cosmique de vice-roi**.

---

## 6. LA STRUCTURE COSMOLOGIQUE HÉBRAÏQUE

Pour comprendre et traduire correctement tout le texte.

### 6.1 Ce que décrit cette section — et ce qu'elle ne décrit pas

**Le cosmos est un Temple.** Le §1 le pose comme principe fondateur : *le cosmos
hébreu n'est pas une usine, c'est un Temple*. Ce qui suit décrit donc ==les zones
d'un édifice==, non les étages d'un immeuble — et la différence commande tout le
reste.

Un étage se compte. Une zone de Temple, non : elle se définit par ==ce qu'on y
accède à faire==, et par ce qu'il faut être pour y tenir. Le parvis, le Lieu
Saint et le Saint des Saints ne sont pas trois hauteurs, ce sont trois régimes
de proximité.

**Ce qui gradue les zones est le kavod.** Le §3.2 le donne : de *kaved* (כָּבֵד),
==être lourd, peser==. La **kavod** de **YHWH** est la densité de sa présence.
La structure cosmique est donc ==un gradient de densité==, et non une distance.

**Pourquoi ce gradient est structurellement nécessaire.** *Exode* 33:20 en donne
la raison sans détour : *l'homme ne peut me voir et vivre*. Un contact non
médiatisé entre des réalités d'intensité radicalement différente ==détruit ce qui
est le moins dense==. La stratification n'est donc pas une hiérarchie de dignité
— catégorie grecque —, c'est ==une architecture de médiation== : ce qui rend la
relation possible sans destruction.

**Le raqia fait pour le cosmos ce que le parokhet fait pour le Bayit.** Ce n'est
pas une cloison entre deux pièces : c'est ==une interface qui gère une transition
de densité==. Même fonction, deux échelles — parce que c'est le même édifice.

L'homologie n'est pas une image, et elle est ==déjà dans le corpus verrouillé== :
la table des motifs de *Toledot Adam ve-Chavah* inscrit ==Eden = Saint des
Saints== d'après *Jubilés* 8:19.

### 6.2 Les zones

**En bas** — la Terre (*eretz*) — le sol habitable, posé sur les eaux primordiales souterraines (*tehom*). Plus bas encore, le **Sheʾol** — le domaine des morts dans le silence et l'attente, où descend tout mort (introduit en *Toledot Adam ve-Chavah*).

**Au milieu** — l'espace habitable — l'atmosphère dans laquelle vivent les hommes et les créatures ailées.

**Au-dessus** — la Voûte (*raqia*) / les Cieux (*shamayim*) — surface solide qui sépare l'espace habitable des eaux supérieures. Dans la Voûte sont enchâssés les luminaires comme des lampes dans un plafond.

**Au-dessus de la Voûte** — les eaux supérieures — l'océan céleste retenu par la Voûte. Quand il pleut, ce sont ses écluses qui s'ouvrent (*Genèse* 7:11).

**Structure de gouvernance cosmique :**
- Les luminaires (*meʾorot*) gouvernent le temps — les domaines temporels
- L'être humain (*adam*) gouverne le vivant — les domaines vivants
- Ensemble ils couvrent la totalité de la gouvernance cosmique déléguée par Elohim

### 6.3 Ce que le gradient commande au traducteur

**On ne compte pas les Cieux.** Certains textes du Second Temple étagent le
**shamayim** et le chiffrent — trois, sept. ==Le chiffre n'entre pas au corps de
l'ONT.== Ce n'est pas un doute sur l'authenticité du témoin : c'est que le
compte est une ==spatialisation== — sept planètes, sept degrés de ziggurat —, et
que le §4.7 interdit d'importer une cosmologie extérieure. Rendre « le septième
firmament » installerait un modèle d'==ascension par échelons==, qui est
précisément la catégorie que le projet filtre.

**En revanche l'étagement lui-même se rend**, et pleinement : les zones, ce qui
les peuple, ce qu'il faut pour y tenir. C'est le gradient de **kavod**, et il est
hébreu. ==On rend ce que la zone fait, non le rang qu'elle occupe.==

**La médiation est descendante.** **YHWH** descend et *prend* — il n'y a pas
d'échelle à gravir. Le corpus l'a déjà tranché une fois : dans *Toledot*, c'est
la **merkavah** qui vient et Adam qui est emporté. Quand un texte paraît raconter
une montée, ==regarder qui agit== : dans le *Chazon Avraham*, Avraham tombe sans
souffle, un **malʾakh** est *envoyé* pour le relever, et les oiseaux entiers sont
le *véhicule* de la montée. Il ne gravit rien — il est porté. La forme est
ascensionnelle, la structure reste descendante, et c'est la structure qu'on rend.

**Un point signalé, non tranché.** *Shemey ha-shamayim* — « les Cieux des Cieux »
(*Deutéronome* 10:14 ; *1 Rois* 8:27) — a la forme du superlatif sémitique par
récursion, comme *Qodesh ha-Qodashim* et *Shir Hashirim* : non pas un Ciel de
plus au-dessus des Cieux, mais ==le shamayim à son degré irréductible==. L'usage
appuie fortement cette lecture — en *1 Rois* 8:27 la phrase sert à dire que
même l'extrême ne peut contenir **YHWH**, ce qui est un argument de transcendance
et non de cartographie. Mais d'autres traditions y lisent une région distincte.
Le §4.11 s'applique : ==on restitue l'ambiguïté, on ne la résout pas==.

### 6.4 Pourquoi cette section a été réécrite — 30 août 2026

Elle ne portait que les zones, décrites ==dans l'espace== : en bas, au milieu,
au-dessus. Rien de faux, et rien qui dise de quel édifice ce sont les parties.
Le §1 déclarait le Temple ; le §6 en énumérait le mobilier sans nommer le
bâtiment.

Personne ne l'avait vu parce que ==aucun texte écrit jusque-là n'avait eu à
traverser le gradient==. Le *Chazon Avraham* est le premier, et il n'a pas créé
le problème : il l'a rendu visible.

C'est la forme exacte du §2.9 — une chose que le projet savait, appliquait, et
n'avait jamais écrite, donc que rien ne pouvait contredire visiblement. Et c'est
aussi la forme de l'erreur qui l'a précédée : la question avait d'abord été posée
en ==« combien de cieux ? »==, c'est-à-dire déjà en escalier. Une question qui
compte porte sa réponse grecque dans sa formulation.

---

## 7. PASSAGES À TRAITER OBLIGATOIREMENT AVEC L'AUTEUR

Ces passages introduisent des concepts nouveaux majeurs ou des décisions qui engagent tout le projet. Claude Code ne doit pas les traiter en autonomie.

### PRIORITÉ ABSOLUE

***Genèse* 2:4-25** — Le second récit de création
- Introduction de *YHWH Elohim* — décision capitale sur le Nom divin
- *Yatsar* vs *bara* — la création matérielle de l'homme
- L'Eden comme Temple cosmique
- La femme — *isha* et *ish*, *ezer kenegdo*
- Le premier mariage comme union fonctionnelle

***Bereshit* 3** — La rupture fonctionnelle
- Le serpent — *nachash*
- La Chute comme dysfonction cosmique, pas comme péché moral
- Les malédictions comme réorganisations fonctionnelles

***Exode* 3:1-15** — Le Nom divin YHWH
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
- *Goʾel* — le Rédempteur fonctionnel

***Iyov*** — Le problème de la souffrance
- Le Conseil Divin (*ha-satan* comme fonction, pas comme nom propre)
- Le tourbillon — réponse d'Elohim

### PRIORITÉ HAUTE

***Bereshit* 6-9** — Le déluge
- *Berith* — l'alliance comme structure fonctionnelle
- La géographie fonctionnelle du déluge

***Bereshit* 12, 15, 17** — Avraham
- *Berith* — développement de l'alliance
- *Emunah* — la foi comme fidélité fonctionnelle (non pas croyance intellectuelle)

***Vayiqra*** — Le système sacrificiel
- Tout le vocabulaire du sacrifice comme système fonctionnel
- *Kafar* — l'expiation fonctionnelle

### BRIT HADASHAH — PRIORITÉ ABSOLUE

***Yohanan* 1:1-18** — Le Prologue
- *En archē ēn ho Logos* : lire *Logos* comme **davar** (Bereshit 1), non comme le *Logos* de Philon d'Alexandrie — décision terminologique capitale pour tout Yohanan

***Gevurot ha-Neviʾim* 2** — La Pentecôte
- Le *ruach* sur les disciples : écho direct de *Genèse* 1:2 et 2:7 — décision terminologique sur la continuité cosmique

**Les *Igerot* de Shaul** — *Tsedaqah* et *emunah*
- Toutes les traductions existantes rendent *tsedaqah* par "justice" ou "justification" (catégorie grecque *dikaiosyne*) — l'ONT maintient **tsedaqah** intraduisible. Décision terminologique à confirmer systématiquement.

***Igeret ha-Ivrim*** — Lettre aux Hébreux
- Entièrement construite sur le système de *Vayiqra* — ne pas traiter avant que *Vayiqra* soit fondé
- *Kafar* / *kippurim* — l'expiation fonctionnelle au centre de l'argumentation

***Machazeh Yohanan*** — Apocalypse
- Dense en références à Yehezqel, Daniel et 1 Chanokh — ne pas traiter avant que ces textes soient au moins partiellement fondés dans l'ONT
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

→ Voir **`corpus-order.md`** à la racine du projet : numérotation globale 01-70, ordre détaillé par mode, structure des Igerot (fracture du Ḥurban), note sur *Tsavaʾat Lévi*.

---

## 12. FONDATIONS DE RÉFÉRENCE

Les Fondations verrouillées sont la référence stylistique et terminologique absolue de l'ONT. Consulter ces fichiers pour vérifier la cohérence de toute nouvelle traduction.

**Deux états, deux dossiers — le flux de validation.** Un texte vit d'abord dans
`brouillons/` tant qu'il porte la mention « à valider » (rédigé, en attente de la
relecture de l'auteur — voir §7). `brouillons/` **miroite exactement**
l'arborescence de `locked/` (même chemin *Kenesset → mode → livre*), afin qu'une
validation soit un simple déplacement vers le chemin identique. Quand l'auteur
valide, le fichier **passe de `brouillons/` au chemin identique dans `locked/`**,
et son pied passe de « à valider » à « Version X — verrouillée ». Seuls les
fichiers de `locked/` font **référence** au sens du §12 : c'est sur eux qu'on
aligne une traduction nouvelle.

**Mais `brouillons/` voyage, et ce document a longtemps dit le contraire.**
Corrigé le 9 septembre 2026, après que l'auteur eut remarqué que ==ses parashiot
en brouillon paraissaient dans l'app==. Vérification faite dans le code plutôt
que dans cette page :

    pipeline/src/config.rs
    pub const TREES: [(&str, &str); 2] = [("locked", "locked"), ("brouillon", "brouillons")];

Le pipeline lit ==les deux arbres== et les émet tous deux, en marquant chaque
unité d'un drapeau `locked`. `dist/books/bereshit.json` contient bien *Bereshit*
1, 2, 7, 13, 14 et 19, qui sont tous en brouillon.

==La validation n'est donc pas une barrière de publication.== C'est une
==déclaration d'état== : elle dit que l'auteur a relu, et elle fait de l'unité
une référence pour les suivantes. Ce qui voyage voyage dès qu'il est écrit.

**Ce qui ne voyage pas** : `context/`, `sessions/`, `scripts/` — et tout ce qui
n'entre dans aucun livre. C'est le cas des **chuqqot** au 9 septembre 2026 :
elles vivent dans `brouillons/chuqqot/`, mais ==le pipeline organise par livre==
et elles n'en sont pas un. `dist/books/` n'en porte aucune, et le seul écho du
mot au manifeste est `stats/unusedEntries: chuqqah`. ==Leur chemin d'émission
reste à écrire==, et c'est ce que la décision du 9 septembre demande à
`ONTBibleApp`.

**Chapitres actuellement en `brouillons/`** (non encore verrouillés — pour ceux-ci, lire `brouillons/…` et non `locked/…`, malgré les chemins de la liste ci-dessous) : *Bereshit* 1, 2, 7, 13, 14 (en révision ; *Bereshit* 2 et 7 attendent le traitement §7 de la *Neshamah*) et *Bereshit* 19 (à valider).

- **Bereshit 1** (Genèse 1:1 — 2:3) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-1.md` — référence fondatrice : toutes les conventions typographiques, le glossaire en action, les formules fixes. Toute traduction doit être cohérente avec elle.
- **Bereshit 2** (Genèse 2:4-25) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-2.md` — introduction de YHWH Elohim, *yatsar*, l'Eden comme Temple, *isha* / *ish*, *ezer kenegdo*, la *neshamah*.
- **Bereshit 3** (Genèse 3) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-3.md` — la rupture fonctionnelle, le *nachash*, les réorganisations cosmiques, *itsavon*, *arur*.
- **Bereshit 4** (Genèse 4) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-4.md` — Qayin et Hevel, *minchah*, *chattat*, *arur*, la ligne de Qayin.
- **Bereshit 5** (Genèse 5) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-5.md` — généalogie d'Adam à Noach, *toledot*, *hithalekh*, Chanokh.
- **Bereshit 6** (Genèse 6) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-6.md` — les Nefilim, la *berith* inaugurale, l'arche (*tevah*).
- **Bereshit 7** (Genèse 7-8) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-7.md` — le déluge, décréation et re-création, *tahor/lo tahor*, *olah*, *qallel*, *kavod*.
- **Bereshit 8** (Genèse 9:1-17) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-8.md` — la re-création après le *mabbul*, la *berith* noachide, *adam* intraduisible à partir d'ici, *olam*. (L'*olah* de Noach, Gn 8:20, est traitée en Bereshit 7, qui couvre Gn 7-8.)
- **Bereshit 9** (Genèse 9:18-29) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-9.md` — l'incident de la vigne, *ish haʾadamah*, *galah*, *arur* sur Kenaʿan, dotations de Shem et Yafet, *shakan* (ambiguïté du sujet maintenue).
- **Bereshit 10** (Genèse 10:1-32) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-10.md` — table des nations, *toledot* des fils de Noach, Nimrod (*gibor*, écho des Nefilim), *mamlakhah*, *lifnei YHWH* (ambiguïté maintenue), Ever / *ivri*, Peleg / *palag*.
- **Bereshit 11** (Genèse 11:1-32) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-11.md` — tour de Bavel, *safah* / *balal* / Bavel (polémique étymologique contre Bab-ilim), *hadal* vs *shavat*, toledot de Shem jusqu'à Terach, *aqarah* (stérilité de Sarai), Haran le fils (הָרָן, he) / Charan la ville (חָרָן, het) — deux **Shem** que l'hébreu n'a jamais confondus, séparés le 10 septembre 2026. Cette ligne disait « homonymie délibérée » : l'homonymie n'était pas dans le texte, elle était dans notre translittération (§2.9).
- **Bereshit 12** (Genèse 12:1-20) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-12.md` — *lekh-lekha* (ambiguïté maintenue), promesse à Avraham, *vayera* (mode de la révélation aux patriarches), *zera* (premier emploi dans la promesse), *niverekhu* (passif ou réflexif — ambiguïté maintenue), descente en Égypte, *negaʿim* (écho de Shemot).
- **Bereshit 13** (Genèse 13:1-18) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-13.md` — retour au Négev et à Bet-El, séparation d'Avram et Lot, *riv* (conflit pastoral), *kikar* (bassin du Yarden), *miqqedem* (mouvement vers l'orient comme éloignement fonctionnel), renouvellement de la promesse aux quatre horizons, *hithalekh baʾarets*, Chevron comme premier ancrage durable.
- **Bereshit 14** (Genèse 14:1-24) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-14.md` — guerre des rois, capture et délivrance de Lot, Malki-tsedeq roi-**kohen** de Shalem, **ʾEl ʿElyon** (premier emploi — intraduisible), **kohen** (intraduisible dès ici), *tsedeq* (l'ordre juste), *qoneh shamayim vaʾarets*, *ha-ivri* (double étymologie maintenue), *baʿalei berit*, *maʿaser* (ambiguïté du sujet maintenue), identification **YHWH**-**ʾEl ʿElyon** par Avram (v.22).
- **Bereshit 15** (Genèse 15:1-21) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-15.md` — *berith bein habetarim*, **ʾemunah** (intraduisible — verbe *heʾemin* rendu "**ʾemuna**"), **tsedaqah** (premier emploi — forme nominale de *tsedeq*), **tsadiq** (déjà posé en Genèse 6:9), *machazeh* (vision intérieure, distinct de *vayera*), *tardemah* (écho délibéré de Genèse 2:21), *ger* (premier emploi — étranger résident sans droits), *avon* (premier emploi — torsion structurelle, distinct de *chata* et *ra*), *berith* unilatérale confirmée (seul **YHWH** passe entre les morceaux), prophétie de l'exil et ambiguïté 400 ans / quatrième génération maintenue.
- **Bereshit 16** (Genèse 16:1-16) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-16.md` — **malʾakh** **YHWH** (premier emploi — intraduisible, ambiguïté délibérée entre le **malʾakh** et **YHWH** maintenue), **ʾEl Roï** (premier emploi — unique dans toute la Bible, donné par Hagar), Hagar (*ger* sans droits — première occurrence d'un personnage non-hébreu central), Ishmaʿel ("El entend"), Beer-lachai-roi, *shifchah* vs *amah*, ambiguïté de *acharei roʿi* (v.13b — trois lectures maintenues sans résolution).
- **Bereshit 17** (Genèse 17:1-27) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-17.md` — **ʾEl Shaddai** (premier emploi — accompagne les moments où **YHWH** accomplit l'impossible humain), **milah** (premier emploi — l'inscription covenantale dans la chair), **ʿorlah** / **ʿarel** (premier emploi — portée métaphorique large : cœur, lèvres, fruit), **goyim** / **goy** (actif dans la promesse : *av hamon goyim*), Avram → Avraham / Sarai → Sarah (reformulation des **Shem** covenantaux : possessif particulier → souverain universel), *tamim* = "intègre" (cohérence avec Noach en *Genèse* 6:9), *karet* (retranchement du peuple — sanction la plus grave du droit divin), formule covenantale *lihyot lekha l'Elohim* (v.7 — le nom cosmique comme engagement de relation personnelle).
- **Bereshit 18** (Genèse 18:1-33) → `locked/1. kenesset (le Rassemblement)/1. torah (la Fondation)/01. bereshit (Genèse)/bereshit-18.md` — **mishpat** / **mishpatim** (premier emploi — l'acte de jugement concret dans l'ordre cosmique ; *tsedaqah umishpat* posé en v.19), **rashaʿ** / **reshaʿim** (premier emploi — opposé fonctionnel de **tsadiq**, paire constitutive du droit divin hébraïque), **shofet** / **shoftim** (premier emploi — même racine que **mishpat** ; *shofet kol haʾarets* titre de souveraineté cosmique universelle ; écho vers le livre *Shoftim*), ambiguïté des trois **ʾish** maintenue (jamais nommés **malʾakhim** dans ce texte — titre donné seulement en *Genèse* 19:1), *zeʿaqah* (cri judiciaire de l'opprimé — déclenche la descente du **mishpat**), intercession 50→10 (Avraham demande un **mishpat** complet, non sa suspension).

---

## 13. CHANTIERS DE BALISAGE — CE QUI A ÉTÉ TRANCHÉ

*Relevé par le pipeline de La Bible ONT (`/Users/gloiiire_/ONTBible/ONTBibleApp`), qui contrôle à chaque construction que tout `**terme**` a bien son entrée de glossaire. Le rapport complet vit dans `dist/report.md` de ce dépôt.*

**Aucun chantier n'est ouvert au 25 août 2026.** Cette section garde ce qui a été tranché et pourquoi — y compris quand le relevé qui ouvrait le chantier s'est révélé faux. Quand le pipeline en signalera de nouveaux, les ajouter ici sous la même forme : le terme, l'issue, et ce que la décision a coûté ou révélé.

### 13.1 Les sept termes — soldés le 25 août 2026

Sept termes étaient écrits `**...**`, donc **déclarés intraduisibles**, sans entrée au §3 : dans l'app, le mot s'affichait en or, le lecteur le touchait, et il n'y avait pas de fiche. Les sept sont réglés.

| terme | issue |
|---|---|
| `tsadiqim` | forme dérivée de **tsadiq** — rattachée à sa puce, retombe sur `lexique/tsadiq.md` |
| `nashim` | forme dérivée d'**ʾishah** (pluriel absolu, à côté de `neshei`) |
| `tsedaqah umishpat` | construit apparié, déclaré sous **tsedaqah** comme **yirat YHWH** sous **yirah** |
| `Tov vara` | construit de l'arbre (*Genèse* 2:9), déclaré sous **tov** — les deux graphies, il ouvre parfois la phrase |
| `shaliachim` | **faute d'orthographe**, pas un arbitrage : le §2.5 fixe `shlichim`. Deux occurrences corrigées |
| `chataʾah` | issue A, et elle a entraîné **toute la famille** : voir ci-dessous |
| `shifchah` | issue A — entrée au §2.5 et au §3.2, fiche écrite. Voir ci-dessous |

**La question posée sur `shifchah` était incomplète, et il faut le noter.** Le §13 le donnait pour une occurrence isolée dans un titre. En ouvrant le chapitre, le pied verrouillé de *Bereshit* 16 portait la décision **inverse** — « traduit "servante" avec niveau 3 » — et le corps s'y tenait sur huit occurrences. Le titre contredisait son propre chapitre. L'auteur a maintenu l'intraduisible en connaissance de la reprise que cela demandait. *Un relevé qui compte les balises ne voit pas les décisions déjà prises autour d'elles.*

**`chataʾah` a entraîné sa racine entière.** Lui écrire une entrée posait la question de *chata* (« dévier ») et *chattat* (« la déviation »), tous deux traduits : garder un mot en hébreu et ses voisins en français aurait été le vrai défaut. L'auteur a tranché pour l'hébreu entier, ==verbe compris== — **chataʾ** est le premier verbe intraduisible de l'ONT, et la décision a été prise en connaissance du précédent qu'elle ouvre.

**Réglé le 20 août 2026 — `Nefilim`, `gibbor` / `gibborim` / `gibor`.** Issue A
pour les trois : ce sont de vrais intraduisibles, désormais au §2.5 et au §3.3.
*Nefilim* n'était pas dans cette liste — il était nu dans le texte, donc muet.
La décision de traduction que le §6 gardait en priorité haute est prise, et elle
ne fait qu'inscrire ce que la glose de *Genèse* 6:4 tenait déjà : l'ambiguïté
de *napal* est maintenue, et « géants » est écarté.

### 13.2 Les « vingt-deux marqueurs déséquilibrés » n'existaient pas

Cette section annonçait vingt-deux `**` ouverts sans être refermés dans les pieds de *Bereshit* 15 à 19. **Le compte était faux, et la façon dont il l'était vaut mieux que le compte.**

Il était relevé **par ligne**. Or un `**...**` enjambe légitimement un retour à la ligne : un paragraphe dont le gras s'ouvre à la fin d'une ligne et se ferme au début de la suivante donne deux lignes « impaires » et n'a aucun défaut. Mesuré **par paragraphe** — l'unité réelle du balisage —, il en restait ==deux==, non vingt-deux.

Les deux étaient réels, et corrigés le 25 août :

- *Bereshit* 16 — `**Avertissement : ` ouvrait un gras d'emphase jamais fermé, dans une puce déjà en italique. Le §2.5 interdit le gras d'insistance partout, notes comprises : passé en `==Avertissement==` ;
- *Bereshit* 17 — ses huit puces s'écrivaient `***Terme*`, un gras ouvert autour d'une italique et jamais refermé, plus un `**arel*` malformé. Normalisées sur la convention de *Bereshit* 16 : tête de puce en `==...==`, la marque d'apparat du §2.5 bis.

Le balayage a ensuite été repassé sur **tout** `locked/`, `brouillons/` et `in-writing/`, et non sur les seuls *Bereshit* 15-19 que cette section regardait : zéro paragraphe déséquilibré.

**Ce qui reste instructif ici n'est pas le compte, c'est l'instrument.** Un relevé par ligne produit un nombre bien formé, aligné, crédible — et il mesurait autre chose que la question posée. C'est le motif que le journal de `SYNCHRONISATION.md` a nommé le même jour : *le format de sortie survit à l'absence de mesure*, et *un instrument se valide sur un cas dont on connaît la réponse, jamais sur celui qu'on étudie*.

### 13.3 Déjà fait — ne pas refaire

Onze balises `**...**` posées pour insister, et non pour déclarer un intraduisible, ont été converties en `==...==` le 12 août 2026 : `« Jour »`, `« Nuit »`, `« Cieux »`, `« Mers »`, `« Terre »` (*Bereshit* 1), `Chavah` (3:20), `Noach` (5:29), `Sarah` (17:15), et trois métadonnées d'apparat dans *Bereshit* 19.
