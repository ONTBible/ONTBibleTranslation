# 12. FONDATIONS DE RÉFÉRENCE

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « 12. FONDATIONS DE RÉFÉRENCE », partie 1. Empreinte de la section : `4fa339ab50dcd362`. Régénérer : `python3 knowledge/decouper.py`.*

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
