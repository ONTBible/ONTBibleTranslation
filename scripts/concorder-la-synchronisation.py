#!/usr/bin/env python3
"""Éprouve que les quatre `SYNCHRONISATION.md` sont bien le même fichier.

    ./scripts/concorder-la-synchronisation.py                  dit ce qui diverge
    ./scripts/concorder-la-synchronisation.py --aligner-la-racine App

Rend **1** dès qu'une copie s'écarte, pour qu'un enchaînement s'arrête dessus.

## Pourquoi ce contrôle existe

`SYNCHRONISATION.md` se déclare identique partout où il se trouve — à la racine
`~/ONTBible/` et dans chacun des trois dépôts. C'était une promesse que **rien
ne tenait** : aucun outil ne comparait les copies, et une divergence ne se voit
depuis aucune d'elles. Chacune a l'air cohérente toute seule.

Le 25 août 2026, toute la section « `git worktree` » a disparu de l'app. Elle
n'avait pas été supprimée : trois entrées de journal avaient été écrites dans la
copie de **la racine**, puis recopiées vers les dépôts. La recopie n'a rien
perdu — elle a **imposé un état périmé**. La dérive a tenu deux jours sans que
personne ne la voie.

Trois règles écrites ne l'avaient pas empêchée. Une quatrième n'y ferait rien :
ce qui manquait n'était pas une consigne mais un **contrôle** — quelque chose
qui ne peut pas oublier de regarder.

## La racine est le point faible, et ce n'est pas un hasard

Les copies des dépôts sont versionnées : une fusion les met à jour, un `pull`
les rattrape, une revue les regarde. Celle de la racine n'a rien de tout cela —
`~/ONTBible/` n'est pas un dépôt. Elle ne peut donc que **prendre du retard**,
jamais en rattraper toute seule.

D'où deux conséquences, qui sont l'essentiel de ce fichier :

- **la racine ne vote jamais** dans le décompte de la version majoritaire. Son
  accord ne prouve rien, et un décompte naïf prend racine + un dépôt en retard
  contre deux dépôts à jour, puis désigne le contenu périmé comme référence.
  C'est exactement l'erreur qu'un premier relevé a commise le 25 août ;
- **elle s'aligne en dernier**, depuis un dépôt nommé — `--aligner-la-racine`.
  Le sens est dans l'argument, il ne se devine plus.

## L'octet décide, les titres expliquent

Deux mesures, et il faut les deux.

L'**empreinte** est le verdict : c'est la seule qui prouve que deux fichiers
sont le même. Mais elle dit « ça diffère » et se tait sur le reste.

Les **titres** — les `##` et `###`, l'unité à laquelle ce document s'écrit —
disent *quoi*. Et ils se rapportent en nommant **qui porte quoi**, jamais ce qui
manque à chacun : sur une section renommée, la seconde formulation annonce que
les trois dépôts ont perdu un titre, alors que l'ancien nom ne survit qu'à la
racine. Le rapport accuse alors les copies à jour.

Seuls, les titres laisseraient passer deux copies aux mêmes sections et au texte
différent — une phrase de la règle réécrite d'un côté. Le contrôle le nomme
quand il l'aperçoit, plutôt que de laisser croire que tout va bien.

## Il balaie, il ne tient pas de liste — et c'est la seule façon d'être exhaustif

Une liste en dur des trois dépôts paraît plus sûre. Elle ne l'est pas : elle
manque **les worktrees**, et depuis qu'ils sont la règle il y en a toujours
plusieurs. Une première version de ce contrôle, écrite ailleurs avec une liste
de quatre chemins, annonçait « les trois dépôts concordent » à un moment où les
deux pièges qu'on était en train de documenter n'existaient **que** dans des
worktrees. Un contrôle qui rassure sur son angle mort est pire que pas de
contrôle.

Et le balayage n'est pas seulement plus large : il est **complet**. Le site
dépend du pipeline de l'app par un chemin relatif — `../ONTBibleApp/pipeline` —,
donc un worktree monté ailleurs ne compile pas : `cargo metadata` échoue avant
tout le reste. Tout arbre de travail utilisable est donc, par construction, un
voisin des autres sous `~/ONTBible/`. Ce que ce contrôle ne voit pas en balayant
ce dossier n'existe pas.

## Ce qu'il lit

Pour chaque dépôt, **deux états**, parce qu'ils ne répondent pas à la même
question :

- l'état **publié** — `origin/dev` pour l'app, `origin/main` pour le vault et le
  site. C'est lui qui fait foi entre les dépôts : ce qui est fusionné est ce que
  la personne suivante recevra ;
- le fichier **sur le disque**, qui est ce qu'une session lit *maintenant* — et
  qui peut être une branche en cours, ou un worktree sur une autre branche.

## Ce qu'il ne fait pas

Aligner deux dépôts. C'est un geste de dépôt : ça passe par une branche et une
PR dans chacun, parce que c'est là que ça se regarde. La racine seule s'écrit
d'ici, puisque rien d'autre ne l'atteint.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

FICHIER = "SYNCHRONISATION.md"

# Le dépôt, et la branche où son exemplaire fait foi. L'app intègre sur `dev` —
# `main` y est l'App Store, plusieurs promotions en retard.
BRANCHES = {
    "ONTBibleApp": "dev",
    "ONTBibleTranslation": "main",
    "ONTBibleWebapp": "main",
}


def racine() -> Path:
    """`~/ONTBible/` — le dossier qui tient les dépôts côte à côte.

    Remontée depuis le script plutôt qu'écrite en dur : le vault peut être monté
    ailleurs, ou lu depuis un worktree.
    """
    return Path(__file__).resolve().parent.parent.parent


def git(depot: Path, *args: str) -> str | None:
    """La sortie de `git`, ou `None` si la commande échoue.

    Échouer est ordinaire ici — pas d'amont, branche détachée, fichier absent de
    la révision demandée. On veut le silence, pas une exception.
    """
    fait = subprocess.run(
        ["git", "-C", str(depot), *args], capture_output=True, text=True
    )
    return fait.stdout if fait.returncode == 0 else None


def empreinte(contenu: str | None) -> str:
    if contenu is None:
        return "—"
    return hashlib.sha256(contenu.encode("utf-8")).hexdigest()[:12]


def titres(texte: str) -> list[str]:
    """Les sections et les entrées de journal, dans l'ordre du fichier."""
    return [l.strip() for l in texte.splitlines() if re.match(r"^#{2,3} ", l)]


class Copie:
    """Une copie du fichier : ce qu'elle porte sur le disque, et ce qui fait foi."""

    def __init__(self, dossier: Path, base: Path) -> None:
        self.nom = dossier.name if dossier != base else "racine"
        self.disque = (dossier / FICHIER).read_text(encoding="utf-8")

        self.dossier = dossier
        self.depot = (dossier / ".git").exists()
        self.publie = None
        self.branche = None
        # Deux dossiers peuvent être **le même dépôt** : un worktree partage le
        # `.git` de son arbre principal. C'est leur `--git-common-dir` qui les
        # réunit, et sans ça le contrôle compte deux fois une même autorité —
        # et laisse un worktree sur une branche en cours servir de référence.
        commun = git(dossier, "rev-parse", "--path-format=absolute", "--git-common-dir")
        self.depot_reel = Path(commun.strip()).parent.name if commun else self.nom

        if self.depot:
            self.branche = BRANCHES.get(self.depot_reel, "main")
            git(dossier, "fetch", "-q", "origin", self.branche)
            self.publie = git(dossier, "show", f"origin/{self.branche}:{FICHIER}")

    @property
    def foi(self) -> str:
        """Ce qui fait autorité pour cette copie — le publié, sinon le disque."""
        return self.publie if self.publie is not None else self.disque

    def situation(self) -> str:
        if not self.depot:
            return "pas un dépôt — rien ne la met à jour"
        remarques = []
        if self.depot_reel != self.nom:
            remarques.append(f"worktree de {self.depot_reel}")
        if self.publie is None:
            remarques.append(f"origin/{self.branche} illisible")
        elif empreinte(self.publie) != empreinte(self.disque):
            sur = (git(self.dossier, "rev-parse", "--abbrev-ref", "HEAD") or "?").strip()
            remarques.append(f"disque ≠ origin/{self.branche} (sur {sur})")
        return ", ".join(remarques) or f"origin/{self.branche}"


def expliquer(reference: Copie, ecartee: Copie) -> None:
    """Dire par les titres ce que l'empreinte a seulement signalé."""
    a, b = titres(reference.foi), titres(ecartee.foi)
    lignes_a, lignes_b = reference.foi.splitlines(), ecartee.foi.splitlines()
    seuls_ici = [t for t in b if t not in a]
    manquants = [t for t in a if t not in b]

    print(f"  ── {ecartee.nom} vs {reference.nom}")
    if not seuls_ici and not manquants:
        # L'angle mort des titres, nommé plutôt que tu.
        ecart = len(lignes_b) - len(lignes_a)
        print("     mêmes titres, texte différent — le changement est **dans** une")
        print("     section, non dans leur liste : un paragraphe ajouté, retiré ou")
        print(f"     réécrit. ({ecart:+d} ligne{'s' if abs(ecart) > 1 else ''})")
        print()
        return
    for t in manquants:
        print(f"     {ecartee.nom} ne porte pas :\n         {t}")
    for t in seuls_ici:
        print(f"     seul {ecartee.nom} porte :\n         {t}")
    print()


def rapporter(copies: list[Copie]) -> int:
    largeur = max(len(c.nom) for c in copies)
    print(f"Les copies de {FICHIER} sous {racine()}\n")
    for c in copies:
        print(
            f"  {c.nom:<{largeur}}  {empreinte(c.foi)}  "
            f"{len(titres(c.foi)):>2} titres  {len(c.foi.splitlines()):>4} lignes   "
            f"{c.situation()}"
        )

    votants = [c for c in copies if c.vote] or [c for c in copies if c.depot]
    juges = votants + [c for c in copies if not c.depot]

    if len({empreinte(c.foi) for c in juges}) == 1:
        print(f"\nLes {len(copies)} exemplaires concordent.")
        return 0

    # La référence est le contenu que portent le plus de copies **versionnées**.
    # La racine ne pèse jamais : voir l'en-tête. À égalité, le nom tranche, pour
    # que deux exécutions disent la même chose.
    def poids(c: Copie) -> tuple[int, int, str]:
        tenue = sum(1 for a in votants if empreinte(a.foi) == empreinte(c.foi))
        return (tenue, 1 if c.depot else 0, c.nom)

    reference = max(juges, key=poids)
    if not reference.depot:
        print("\nAucune copie versionnée — rien qui fasse autorité.")
        return 1

    versions = len({empreinte(c.foi) for c in juges})
    print(f"\n{versions} versions différentes. Référence retenue : {reference.nom}.\n")
    for c in juges:
        if empreinte(c.foi) != empreinte(reference.foi):
            expliquer(reference, c)

    depots_ecartes = [
        c for c in votants if empreinte(c.foi) != empreinte(reference.foi)
    ]
    if depots_ecartes:
        print("Porter ce qui manque dans chaque dépôt, par une branche et une PR.")
        print("Jamais l'inverse : recopier depuis la racine impose son retard aux")
        print("autres — c'est ce qui a effacé la section du worktree le 25 août.")
    print(f"La racine s'aligne en dernier : --aligner-la-racine {reference.nom}")
    return 1


def main() -> int:
    base = racine()
    arguments = argparse.ArgumentParser(
        description="Éprouve que les quatre SYNCHRONISATION.md sont le même fichier."
    )
    arguments.add_argument(
        "--aligner-la-racine",
        metavar="DÉPÔT",
        help=f"recopie l'exemplaire publié d'un dépôt vers {base}/{FICHIER}",
    )
    options = arguments.parse_args()

    dossiers = [base] if (base / FICHIER).exists() else []
    dossiers += sorted(
        d for d in base.iterdir() if d.is_dir() and (d / FICHIER).exists()
    )
    if len(dossiers) < 2:
        print(f"Une seule copie sous {base} — rien à comparer.")
        return 0

    copies = [Copie(d, base) for d in dossiers]

    # Un worktree n'est pas un exemplaire de plus : il partage l'autorité de son
    # arbre principal. Le laisser dans le décompte compterait deux fois le même
    # dépôt — et pourrait lui faire porter la référence depuis une branche en
    # cours. On le garde dans le tableau, pour dire ce qu'il montre à la session
    # qui l'occupe, mais il ne vote pas.
    vus: set[str] = set()
    for c in copies:
        c.vote = c.depot and c.depot_reel not in vus
        if c.depot:
            vus.add(c.depot_reel)

    if options.aligner_la_racine:
        voulue = options.aligner_la_racine
        source = next((c for c in copies if c.nom == voulue and c.vote), None)
        if source is None:
            connus = ", ".join(c.nom for c in copies if c.vote)
            print(f"✗  « {voulue} » n'est pas un dépôt lisible. Au choix : {connus}")
            return 1
        (base / FICHIER).write_text(source.foi, encoding="utf-8")
        print(
            f"Racine alignée sur {source.nom} (origin/{source.branche}) — "
            f"{len(source.foi.splitlines())} lignes."
        )
        return 0

    return rapporter(copies)


if __name__ == "__main__":
    sys.exit(main())
