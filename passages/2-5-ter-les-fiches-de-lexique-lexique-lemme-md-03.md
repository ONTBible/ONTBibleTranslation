# 2.5 ter Les fiches de lexique — `lexique/<lemme>.md`

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « 2.5 ter Les fiches de lexique — `lexique/<lemme>.md` », partie 3. Empreinte de la section : `a8e22b3c16f394d7`. Régénérer : `python3 knowledge/decouper.py`.*

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

**Quand le témoin ne porte pas le mot.** Décision de l'auteur du 16 septembre
2026. Certains intraduisibles de l'ONT sont ==du Second Temple ou rabbiniques== :
`**milah**`, `**tevilah**`, `**shaliach**`. Le témoin porte leur racine et pas
leur nom — il a *mul*, *taval*, *shalach*, et aucun des trois substantifs.

La Source le ==déclare== au lieu de se taire :

    ## Source

    — · טְבִילָה

    Le témoin porte le verbe — *taval* (2881) — et aucun nom.

    Racine : 2881 · *taval*.

Le tiret dit ==le mot n'a pas de numéro==, la racine dit ==d'où il vient==, et
la note dit ==pourquoi==. Trois choses vraies, et aucune fausse jointure : le
pipeline ne lit aucun numéro sur cette ligne, donc il n'en affirme aucun.

==L'absence cesse d'être un silence.== Sans cette forme, rien ne distingue « le
témoin ne l'a pas » de « personne n'a cherché », et c'est exactement l'écart que
le contrôle doit pouvoir voir.

**Le cas est plus rare qu'il n'y paraît, et je m'y suis trompé.** Trois mots que
j'avais rangés ici ==ont bel et bien leur numéro== :

    YHWH Elohim   3068 + 430   deux mots, deux numéros — un composé
    teshuvah      8666         8 emplois, tous au construit ou préfixés
    parashah      6575         2 emplois dans Esther, « l'exposé exact »

Ma recherche cherchait ==la forme absolue vocalisée==, que le témoin n'écrit pas
toujours : `תְּשׁוּבָה` n'y paraît jamais nue, mais `לִתְשׁוּבַת` porte le lemme
8666. ==Chercher une forme n'est pas chercher un mot.==
