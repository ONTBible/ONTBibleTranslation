# La couleur, et pourquoi celle-là

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « La couleur, et pourquoi celle-là », partie 2. Empreinte de la section : `cf5f51284c121ad4`. Régénérer : `python3 knowledge/decouper.py`.*

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
