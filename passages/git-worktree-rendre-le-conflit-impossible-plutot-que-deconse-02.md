# `git worktree` — rendre le conflit impossible plutôt que déconseillé

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « `git worktree` — rendre le conflit impossible plutôt que déconseillé », partie 2. Empreinte de la section : `3d60905440bddcb8`. Régénérer : `python3 knowledge/decouper.py`.*

5. **Un worktree retient sa branche, même fusionnée.** `git branch -d` refuse —
   « cannot delete branch used by worktree » — et la suppression automatique
   après fusion échoue de la même façon. Rencontré le 25 août, sur trois
   branches à la fois. La parade tient en un geste : **démonter le worktree dès
   que la branche est poussée**, sans attendre la fusion. Le travail vit alors
   sur le distant, et il n'y a plus rien à retenir.

6. **Ne jamais écrire dans la copie de la racine puis diffuser.**
   `~/ONTBible/SYNCHRONISATION.md` se présente comme la source des quatre, et
   c'est la seule que **rien** ne synchronise : la racine n'est pas un dépôt,
   aucun `pull` ne l'atteint, aucune fusion ne la corrige. Elle dérive donc en
   silence, et la recopier dans les dépôts n'y perd rien — elle y **impose un
   état périmé**.

   C'est arrivé le 25 août : trois entrées écrites à la racine puis recopiées
   ont effacé de l'app toute cette section-ci, arrivée par une fusion que la
   racine ignorait. Le vault et le site n'ont survécu que par accident, leurs
   propres PR la rapportant en parallèle.

   Partir d'un dépôt à jour, toujours, et porter le changement dans chacun.

7. **Une commande qui écrit sur le distant laisse l'arbre partagé périmé sur sa
   propre branche.** `gh pr update-branch` fusionne la branche de base **dans le
   dépôt distant** : l'arbre local ne l'apprend pas, et se retrouve en retard
   sur la branche qu'il croit tenir. Un commit posé par-dessus écraserait la
   fusion.

   Ce qui le rend dangereux n'est pas l'écart mais le silence : **`git status`
   répond « propre », et il dit vrai** — il compare l'arbre à l'index, pas à
   `origin`. Rien dans sa sortie ne suggère d'aller regarder ailleurs.

   Trouvé le 25 août par une session qui arrivait sur l'arbre et l'a contrôlé
   avant d'y écrire. La parade : `git fetch` puis `git rev-list --left-right
   --count origin/<branche>...HEAD` avant de toucher un arbre qu'on ne vient pas
   de quitter — et `git pull --ff-only` après toute commande `gh` qui écrit.

**Ce que ça ne remplace pas.** Se parler. Le worktree protège les fichiers, pas
les décisions : deux sessions qui refondent le même module chacune de leur côté
produiront deux refontes, proprement isolées et incompatibles.
