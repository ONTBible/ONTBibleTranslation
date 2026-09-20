# 2 septembre 2026 — le pipeline d'un arbre périmé rend un rapport faux

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « 2 septembre 2026 — le pipeline d'un arbre périmé rend un rapport faux », partie 1. Empreinte de la section : `a165bcf57accca3a`. Régénérer : `python3 knowledge/decouper.py`.*

Même vault, même commande, deux exemplaires du pipeline :

    ~/ONTBible/ONTBibleApp   (branche de travail abandonnée)   204 fiches orphelines
    worktree détaché @ origin/dev                                2 fiches orphelines

L'écart n'est pas une régression : la branche est **en amont** du correctif des
Shemot, de 939 lignes sur `pipeline/`. C'est la troisième forme de prémisse
fausse déjà nommée — **juste ici, fausse là-bas, sans que rien n'ait bougé** —,
et elle a failli produire un signalement de régression 3 → 204 à la session app.

**Pour les trois dépôts :** un outil de contrôle se mesure **avec la référence
sur laquelle il tourne**, au même titre qu'un `grep`. `git worktree add -f
--detach <scratch> origin/dev` coûte une ligne et donne l'état publié.

Deux faits utiles au passage. Le binaire du pipeline résout le vault en relatif
depuis son propre chemin : hors de l'arbre habituel il faut `ONT_VAULT`, et il
s'arrête net avec un message clair si on l'oublie — bon comportement. Et
`scripts/corpus.sh` ne se lance **pas** sur un arbre partagé : il fait `rm -rf
app/Resources/data`, réécrit les DTO Swift et rejoue `xcodegen`. Le binaire
seul écrit dans `dist/`, qui est ignoré.

**Et un défaut réel, trouvé en se faisant contredire.** J'avais avancé que le
balayage ne collectait les `[[Nom]]` que depuis les unités d'un livre. La
session app l'a **réfuté sur pièces** — les fiches produisent bien leurs nœuds
de lien, et l'app les rend touchables. Elle a en même temps donné **la date de
son propre corpus**, vieux de deux jours, plutôt que la conclusion sans elle :
c'est ce qui m'a fait remesurer au lieu de conclure.

Le vrai défaut est ailleurs, et il est plus large. Sur `dist/` fraîchement
construit depuis `origin/dev` :

    liens émis          corps de chapitre 4447   ·   fiches 2948
    lemmes introuvables corps de chapitre  133   ·   fiches   88

**Deux causes distinctes, et il faut les séparer parce que le remède diffère.**
