# Deux artefacts, et il faut les deux — 30 septembre 2026

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « Deux artefacts, et il faut les deux — 30 septembre 2026 », partie 2. Empreinte de la section : `4a2e698c627824d5`. Régénérer : `python3 knowledge/decouper.py`.*

herdr agent list      rend le dossier de LANCEMENT du volet, jamais le worktree
    lsof                  ne voit rien entre deux tours — un agent qui réfléchit
                          n'a aucun fichier ouvert
    date de l'index git   vieillit sur un poste où l'on lit sans commiter

==Vu du dehors, une session ne se prouve que par sa réponse.== Et une réponse
n'est pas consultable quand la session est occupée, partie, ou — comme Astra
pendant deux jours — incapable d'écrire. D'où la déclaration : ==ce qu'aucun
instrument ne mesure, on l'écrit==.

**Ce que ça a coûté de ne pas l'avoir.** Le 21 septembre, un démontage de cinq
worktrees a failli emporter ==un commit qui ne tenait que par un worktree== —
`HEAD` détaché, sur une branche que son propre auteur avait supprimée le matin
même sans voir qu'un worktree y pendait. Et ==un banc de mesure de 229 lignes==
qui vivait en fichier non suivi, dont les deux « exemplaires de réserve »
étaient la version d'avant.

**Une leadeuse n'a rien à créer, et sa ligne n'est pas une déclaration.** La
décision ci-dessus vise ==celle qui crée un worktree==. La leadeuse d'un dépôt
n'en crée pas : elle tient ==l'arbre principal==, qui existait avant elle et
qui existera après. Sa ligne figure quand même dans la table — ==le poste est
un fait du dépôt, pas un acte de session==.

==Sans cette clause, l'absence se lit comme un manquement== : quelqu'un qui
vérifie la table contre `git worktree list` trouve l'arbre principal, cherche
qui l'a déclaré, et conclut que la leadeuse ne l'a pas fait. ==Elle n'avait rien
à déclarer.== Relevé par le vault le 29 septembre 2026, le jour même où la table
est entrée dans `main` — et c'est le bon moment pour le dire, avant que
quelqu'un tire la mauvaise conclusion.

C'est la même distinction que partout ailleurs dans ce fichier : ==ce qui se
mesure ne se déclare pas, ce qui ne se mesure pas se déclare==. `git worktree
list` prouve l'arbre principal ; il ne prouve pas ==à qui== est un worktree, ni
==pourquoi== il existe. Les deux colonnes de droite sont là pour ça, et elles
seules demandent une main.
