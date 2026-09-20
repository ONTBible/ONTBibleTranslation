# 2.5 ter Les fiches de lexique — `lexique/<lemme>.md`

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « 2.5 ter Les fiches de lexique — `lexique/<lemme>.md` », partie 2. Empreinte de la section : `a8e22b3c16f394d7`. Régénérer : `python3 knowledge/decouper.py`.*

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
