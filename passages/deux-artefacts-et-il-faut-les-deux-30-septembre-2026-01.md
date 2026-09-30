# Deux artefacts, et il faut les deux — 30 septembre 2026

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « Deux artefacts, et il faut les deux — 30 septembre 2026 », partie 1. Empreinte de la section : `4a2e698c627824d5`. Régénérer : `python3 knowledge/decouper.py`.*

==« Dans le même tour » était infaisable, et c'est mesuré.== `main` est
protégée : la déclaration n'atteignait le journal qu'à la fusion — une heure
d'ordinaire, ==une journée entière== quand la PR attend l'auteur. Or c'est
exactement la fenêtre que la règle existe pour fermer.

**Et le défaut était pire que le délai.** Le contrôle lisait la copie du
journal *dans le worktree*, donc il se taisait dès qu'une session avait
déclaré — ==y compris quand sa ligne n'était que dans une branche que personne
d'autre ne lirait== :

    poste déclaré et fusionné      main a la ligne · contrôle muet · sûr
    poste déclaré, PR en attente   main n'a rien   · contrôle muet · EN DANGER
    poste jamais déclaré           main n'a rien   · contrôle crie · protégé

==Le cas dangereux et le cas sûr rendaient le même silence==, et le seul qui
criait était celui où la session avait été négligente — donc celui où elle
savait déjà. ==La garde était rassurée par la chose même qui créait le
risque.==

**Décision de l'auteur du 30 septembre 2026 :** ==le durable et l'immédiat
n'ont pas à être le même artefact==. Ce qui crée le délai est le
versionnement ; la déclaration immédiate n'a pas besoin d'être versionnée, elle
a besoin d'être ==lisible sur la machine, tout de suite==.

    python3 scripts/declarer-son-poste.py --poser "pourquoi ce poste existe"
    python3 scripts/declarer-son-poste.py --dire
    python3 scripts/declarer-son-poste.py --retirer

| | ce qu'il porte |
|---|---|
| `~/ONTBible/.postes` | ==l'immédiat== — hors de tout dépôt, donc sans PR ni délai. **C'est lui qui décide si un poste est déclaré**, et c'est lui qu'on lit ==avant tout démontage== |
| la table ci-dessous | ==le durable== — le *pourquoi* pour la postérité, et il rattrape à la fusion |

==Un poste déclaré à l'immédiat et pas encore au durable n'est pas un
manquement== : c'est l'état normal entre la création et la fusion. Le contrôle
le dit sans le reprocher.

Précédent dans le dépôt : `~/ONTBible/.espace-disque`, que la veille écrit et
qu'on lit ==sans rien lancer== — ce qui compte précisément quand plus rien ne
se lance.

**Pourquoi une déclaration, et non un relevé.** Parce que ==rien ne prouve
qu'une session tient un worktree==. Trois pistes ont été éprouvées le
21 septembre, les trois échouent :
