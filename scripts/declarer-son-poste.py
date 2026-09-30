#!/usr/bin/env python3
"""Déclarer un worktree **tout de suite**, hors de git.

## Pourquoi ce fichier existe, et pourquoi il n'est versionné nulle part

La règle du 21 septembre 2026 demande qu'une session inscrive son worktree dans
`SYNCHRONISATION.md` ==dans le même tour== que sa création. Le 30 septembre, on
a mesuré qu'elle est **infaisable** : `main` est protégée, tout passe par pull
request, donc la déclaration n'atteint `main` qu'à la fusion — une heure
d'ordinaire, ==une journée entière== quand la PR attend l'auteur.

Et c'est exactement la fenêtre que la règle existe pour fermer : les trois
worktrees disparus des 21-22 septembre l'ont été ==pendant que leur session y
travaillait encore==.

**Le défaut est plus retors que le délai**, et il a été mesuré : le contrôle
`cartographier-la-flotte.py --worktrees` lit la copie du journal *dans le
worktree*, donc il se tait dès que la session a déclaré — ==y compris quand sa
ligne n'est que dans une branche que personne d'autre ne lira==.

    poste déclaré et fusionné      main a la ligne · contrôle muet · sûr
    poste déclaré, PR en attente   main n'a rien   · contrôle muet · EN DANGER
    poste jamais déclaré           main n'a rien   · contrôle crie · protégé

==Le cas dangereux et le cas sûr rendent le même silence==, et le seul qui crie
est celui où la session a été négligente — donc celui où elle sait déjà. La
garde protège qui n'en a pas besoin et se tait sur qui en aurait besoin. Pire
qu'une garde absente : ==elle est rassurée par la chose même qui crée le
risque==.

## La décision de l'auteur, 30 septembre 2026

==Le durable et l'immédiat n'ont pas à être le même artefact.== Ce qui crée le
délai est le versionnement ; or la déclaration immédiate n'a pas besoin d'être
versionnée — elle a besoin d'être ==lisible sur la machine, tout de suite==.

    ~/ONTBible/.postes      écrit à la création, lu avant tout démontage
                            hors de tout dépôt, donc sans PR ni délai

    SYNCHRONISATION.md      la table durable, qui rattrape à la fusion
                            et qui porte le « pourquoi » pour la postérité

Précédent dans le dépôt : `~/ONTBible/.espace-disque`, que la veille écrit et
qu'on lit *sans rien lancer* — ce qui compte précisément quand plus rien ne se
lance.

## L'emploi

    python3 scripts/declarer-son-poste.py --dire
    python3 scripts/declarer-son-poste.py --poser "les témoins et les licences"
    python3 scripts/declarer-son-poste.py --retirer

`--poser` devine le worktree courant et le rôle par `HERDR_PANE_ID` quand il
est là ; `--qui` et `--ou` les forcent. ==Le « pourquoi » ne se devine pas== :
c'est la seule chose qu'aucun relevé ne produira jamais, et c'est pour elle que
ce fichier existe.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

RACINE = Path.home() / "ONTBible"
POSTES = RACINE / ".postes"

EN_TETE = """# Les postes tenus — déclarés à la création, lus AVANT tout démontage.
#
# Ce fichier n'est dans aucun dépôt, et c'est ce qui le rend immédiat : une
# déclaration versionnée n'atteint `main` qu'à la fusion, et la fenêtre
# d'attente est celle où trois worktrees ont été démontés pendant que leur
# session y travaillait (21-22 septembre 2026).
#
# La table durable vit dans SYNCHRONISATION.md et rattrape à la fusion.
# Écrit par scripts/declarer-son-poste.py — une ligne par poste, séparée par
# des tabulations : dossier, qui, pourquoi, depuis quand.
"""


def _lignes() -> list[list[str]]:
    """Les postes déclarés, en-tête et lignes vides écartés."""
    if not POSTES.exists():
        return []
    postes = []
    for ligne in POSTES.read_text().splitlines():
        if not ligne.strip() or ligne.lstrip().startswith("#"):
            continue
        champs = ligne.split("\t")
        # **On ne jette pas une ligne mal formée, on la garde telle quelle.**
        # Un fichier que quelqu'un a édité à la main reste lisible ; le perdre
        # silencieusement serait pire que de l'afficher de travers.
        postes.append(champs + [""] * (4 - len(champs)))
    return postes


def _ecrire(postes: list[list[str]]) -> None:
    corps = "".join("\t".join(p[:4]).rstrip() + "\n" for p in postes)
    POSTES.write_text(EN_TETE + "\n" + corps)


def _worktree_courant() -> str | None:
    """Le dossier du worktree où l'on se trouve, par git lui-même."""
    r = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=False, timeout=15,
    )
    return Path(r.stdout.strip()).name if r.returncode == 0 and r.stdout.strip() else None


def _qui_par_defaut() -> str:
    """Le volet Herdr est le seul identifiant stable d'une session.

    Le nom d'agent change à un `/rename`, la socket est un PID rebattu au
    redémarrage, la référence change à une reconnexion. ==Le volet est une
    place== : il vit dans la disposition, pas dans le processus.
    """
    return os.environ.get("HERDR_PANE_ID", "") or "—"


def dire() -> int:
    postes = _lignes()
    if not postes:
        print(f"\n  Aucun poste déclaré. ({POSTES})\n")
        return 0
    large = max(len(p[0]) for p in postes)
    print(f"\n  {len(postes)} poste(s) déclaré(s) — {POSTES}\n")
    for dossier, qui, pourquoi, depuis in postes:
        print(f"    {dossier:<{large}}  {qui:<14}  {pourquoi}")
        if depuis:
            print(f"    {'':<{large}}  depuis {depuis}")
    print()
    return 0


def poser(pourquoi: str, qui: str | None, ou: str | None) -> int:
    dossier = ou or _worktree_courant()
    if not dossier:
        print("  ✗ impossible de deviner le worktree — employer --ou")
        return 1
    if not pourquoi.strip():
        # ==La seule chose qu'aucun relevé ne produira jamais.== Une ligne sans
        # « pourquoi » a le coût d'une déclaration et n'en a pas le bénéfice.
        print("  ✗ le « pourquoi » est obligatoire — c'est tout l'objet du fichier")
        return 1
    postes = [p for p in _lignes() if p[0] != dossier]
    postes.append([dossier, qui or _qui_par_defaut(), pourquoi.strip(),
                   datetime.now().strftime("%Y-%m-%d %H:%M")])
    postes.sort(key=lambda p: p[0])
    _ecrire(postes)
    print(f"  ✓ {dossier} déclaré — {pourquoi.strip()}")
    print("    Porter la même ligne dans la table de SYNCHRONISATION.md,")
    print("    qui est la trace durable. Celle-ci est l'immédiate.")
    return 0


def retirer(ou: str | None) -> int:
    dossier = ou or _worktree_courant()
    if not dossier:
        print("  ✗ impossible de deviner le worktree — employer --ou")
        return 1
    postes = _lignes()
    restants = [p for p in postes if p[0] != dossier]
    if len(restants) == len(postes):
        print(f"  — {dossier} n'était pas déclaré, rien à retirer")
        return 0
    _ecrire(restants)
    print(f"  ✓ {dossier} retiré")
    print("    Retirer aussi sa ligne de SYNCHRONISATION.md.")
    return 0


def main() -> int:
    a = argparse.ArgumentParser(
        description="Déclarer son worktree tout de suite, hors de git.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="La table durable reste SYNCHRONISATION.md ; ce fichier-ci est "
               "l'immédiat, et c'est lui qu'on lit AVANT de démonter quoi que "
               "ce soit.",
    )
    a.add_argument("--dire", action="store_true", help="les postes déclarés")
    a.add_argument("--poser", metavar="POURQUOI", help="déclarer le poste courant")
    a.add_argument("--retirer", action="store_true", help="retirer le poste courant")
    a.add_argument("--qui", help="forcer le tenant (défaut : HERDR_PANE_ID)")
    a.add_argument("--ou", help="forcer le nom de dossier")
    o = a.parse_args()

    if o.poser is not None:
        return poser(o.poser, o.qui, o.ou)
    if o.retirer:
        return retirer(o.ou)
    return dire()


if __name__ == "__main__":
    sys.exit(main())
