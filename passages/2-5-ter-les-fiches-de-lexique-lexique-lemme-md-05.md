# 2.5 ter Les fiches de lexique — `lexique/<lemme>.md`

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « 2.5 ter Les fiches de lexique — `lexique/<lemme>.md` », partie 5. Empreinte de la section : `a8e22b3c16f394d7`. Régénérer : `python3 knowledge/decouper.py`.*

==Une occurrence n'est pas une forme de citation.== Le dagesh initial d'un mot
dépend de ce qui le précède et des accents (Gesenius §21) ; le choisir comme
cible fait juger du contexte pour une propriété du lexique.

**Ce qu'il faut fixer avant de remesurer** : quelle forme est la cible, comment
traiter le kétiv/qeré, que faire des ex æquo, et ==dans quel ordre on lit les
fichiers==. Le dernier point n'est pas une précaution de style — mesuré le même
jour, un simple `sorted` sur la liste des fichiers déplace le résultat :

    glob.glob (ordre du disque)    1220 majoritaires · 1326 attestées
    sorted(glob.glob)              1218              · 1328

`Counter.most_common` départage les ex æquo par ordre de première rencontre.
==Un pourcentage qui bouge quand on trie un `glob` ne mesure pas ce qu'on croit.==

**Et les huit restent une recherche lexicographique**, pas un arbitrage qu'un
programme puisse rendre.

**Ce que les chiffres disaient — et il faut lire la clause ci-dessus avant.**
==82,3 % sur l'ensemble, 70,3 % sur les gentilés==, la population qui importait.
Un taux se calcule sur ==la bonne population== ; ici elle se trouve être la
moins bonne, et c'est le contraire de ce qu'on attendait.

==Un 98,1 % a été publié une heure, et il était faux.== La comparaison ôtait
==tous== les points-voyelles pour juger si deux graphies étaient le même mot :
`עָם` et `עַם` y passaient pour identiques alors que ce sont deux sons. Un
instrument trop indulgent ne rend pas un chiffre approximatif — il rend ==un
chiffre faux, et toujours dans le sens qui arrange==.

Le résidu honnête se répartit ainsi, et seule la troisième ligne est du bruit :

    82,3 %   exact au caractère près
     7,4 %   voyelle différente      l'écrit ne dit pas si elle a été allongée
     7,4 %   lettre-support seule    le scribe note la voyelle autrement
     2,9 %   autre forme             deux pluriels, deux lieux

**Et la limite est structurelle**, non un défaut de la règle. L'auteur l'a
nommée en rappelant que ==l'hébreu est d'abord une langue orale== : les
points-voyelles sont une notation tardive, posée sur un texte qui se
transmettait par la voix. Quand l'article allonge la voyelle d'un mot, ==l'écrit
garde le résultat et perd l'opération== — `הָעָם` et `הֶעָשׂוּי` portent le même
signe, l'un l'a reçu de l'article et l'autre l'avait déjà. Un lecteur qui savait
la langue entendait la différence ; la page ne la porte pas. Trois règles
phonétiques ont été essayées sur ce résidu : elles ont gagné ==trois cas sur
1482==.
