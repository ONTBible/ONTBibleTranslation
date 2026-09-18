# `git worktree` — rendre le conflit impossible plutôt que déconseillé

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « `git worktree` — rendre le conflit impossible plutôt que déconseillé », partie 1. Empreinte de la section : `3d60905440bddcb8`. Régénérer : `python3 knowledge/decouper.py`.*

**Posé le 24 août 2026.** Deux sessions travaillaient en parallèle sur
`ONTBibleApp` ; l'une a changé de branche pendant que l'autre écrivait. Rien n'a
été perdu — elle a prévenu, et vérifié après coup que la branche voisine était
intacte — mais le seul rempart avait été sa vigilance.

Un dépôt git confond deux choses parce qu'elles vivent au même endroit : le
dossier `.git`, qui porte **toute** l'histoire, et les fichiers autour, qui n'en
montrent **qu'une branche**. D'où la limite : un dépôt, une branche visible. En
changer déplace les fichiers de tout le monde.

`git worktree` sépare les deux :

    git worktree add ../ONTBibleApp-android ma-branche

donne un **second dossier de fichiers**, sur une **autre branche**, partageant le
**même** `.git`. Ce n'est pas un clone : rien n'est dupliqué, et le `.git` du
nouveau dossier n'est même pas un dossier — c'est un fichier d'une ligne qui
renvoie vers l'original.

    ONTBibleApp/              ← branche A        session 1
      .git/                   ← l'histoire, partagée
    ONTBibleApp-android/      ← branche B        session 2
      .git                    ← un renvoi, pas une copie

Chaque dossier a son propre `HEAD`. Un `switch` chez l'une ne touche plus
l'autre. Les commandes utiles tiennent en quatre lignes :

    git worktree list                    qui travaille où, sur quelle branche
    git worktree add <dossier> <branche>
    git worktree remove <dossier>
    git worktree prune                   nettoie les dossiers effacés à la main

**Quand l'employer.** Dès qu'une session sœur est présente — `ListAgents` le
dit. Le monter coûte une seconde ; la passation d'arbre coûte une conversation,
et un oubli coûte une journée.

**Quatre choses à savoir, dont une qui mord.**

1. **Une branche ne s'ouvre que dans un seul worktree.** Git refuse la seconde
   sortie — c'est une protection : deux dossiers sur la même branche
   divergeraient.
2. **Les fichiers non suivis ne suivent pas.** C'est le vrai piège, et il s'est
   présenté le jour même : le travail en cours n'était pas encore commité, il a
   fallu le déplacer à la main. Commiter avant de monter le worktree l'évite.
3. **Branches, commits, `stash` sont partagés** — c'est le même dépôt. Seuls les
   fichiers de travail sont séparés, et c'est exactement ce qu'on veut.
4. **Les artefacts de build sont à refaire.** Chaque worktree a ses `target/`,
   `build/`, `.gradle/`. Compter une première compilation complète, et un
   `cargo clean` de plus en fin de chantier.
