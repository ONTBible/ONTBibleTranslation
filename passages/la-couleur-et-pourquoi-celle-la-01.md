# La couleur, et pourquoi celle-là

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « La couleur, et pourquoi celle-là », partie 1. Empreinte de la section : `cf5f51284c121ad4`. Régénérer : `python3 knowledge/decouper.py`.*

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
