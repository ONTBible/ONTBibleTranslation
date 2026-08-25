#!/usr/bin/env python3
"""Vérifie que les quatre `SYNCHRONISATION.md` sont bien le même fichier.

## Pourquoi ce script existe

`SYNCHRONISATION.md` se déclare lui-même identique partout où il se trouve — à
la racine `~/ONTBible/` et dans chacun des trois dépôts. C'est une promesse que
**rien ne tenait** : aucun outil ne les compare, et une divergence ne se voit
depuis aucun des quatre endroits. Chaque copie a l'air cohérente toute seule.

Le 25 août 2026, trois entrées de journal écrites dans la copie de la racine
puis recopiées vers les dépôts ont effacé de l'app une section entière, arrivée
là par une fusion que la racine ignorait. Le vault et le site n'ont survécu que
par accident : leurs propres PR rapportaient la section en parallèle. Personne
ne l'a vu au moment où c'est arrivé — c'est en allant chercher autre chose,
deux heures plus tard, qu'on l'a découvert.

Ce script est le regard qui manquait. Il ne répare rien : il **dit** ce qui
diverge, et de quel côté est le retard.

## La racine est le point faible, et ce n'est pas un hasard

Les trois copies des dépôts sont versionnées : une fusion les met à jour, un
`pull` les rattrape, une revue les regarde. La copie de la racine n'a rien de
tout cela — `~/ONTBible/` n'est pas un dépôt. Elle ne peut donc que **prendre
du retard**, jamais en rattraper toute seule.

D'où la seule direction sûre, que le rapport rappelle à chaque divergence :
d'un dépôt à jour vers la racine, jamais l'inverse.

## Ce qu'il regarde

Pour chaque copie trouvée sous `~/ONTBible/` :

- le **fichier sur le disque**, qui est ce qu'une session lit ;
- pour un dépôt, en plus, ce que porte sa **branche courante** et ce que porte
  son **amont** — parce qu'un fichier peut être juste sur le disque et pas
  encore poussé, ou déjà dépassé par une fusion qu'on n'a pas tirée.

## Ce qu'il ne fait pas

Il n'écrit rien, nulle part. Aligner les copies est un geste de dépôt : ça
passe par une branche et une PR dans chacun, parce que c'est là que ça se
regarde.

Code de sortie : `0` si les copies concordent, `1` sinon — donc utilisable dans
un enchaînement.
"""

from __future__ import annotations

import difflib
import hashlib
import subprocess
import sys
from pathlib import Path

FICHIER = "SYNCHRONISATION.md"


def racine() -> Path:
    """`~/ONTBible/` — le dossier qui tient les dépôts côte à côte.

    Trouvé en remontant depuis le script plutôt qu'écrit en dur : le vault peut
    être monté ailleurs, ou lu depuis un worktree.
    """
    return Path(__file__).resolve().parent.parent.parent


def git(depot: Path, *args: str) -> str | None:
    """Retourne la sortie de `git`, ou `None` si la commande échoue.

    Échouer est un cas ordinaire ici — pas d'amont, branche détachée, fichier
    absent de la révision demandée. On veut le silence, pas une exception.
    """
    issue = subprocess.run(
        ["git", "-C", str(depot), *args],
        capture_output=True,
        text=True,
    )
    return issue.stdout if issue.returncode == 0 else None


def empreinte(contenu: str) -> str:
    return hashlib.sha256(contenu.encode("utf-8")).hexdigest()[:12]


class Copie:
    """Une copie du fichier, et ce que son dépôt en dit."""

    def __init__(self, chemin: Path, base: Path) -> None:
        self.chemin = chemin
        self.nom = str(chemin.parent.relative_to(base.parent)) or "."
        self.contenu = chemin.read_text(encoding="utf-8")
        marque = chemin.parent / ".git"
        self.depot = marque.exists()
        # Un worktree porte un `.git` **fichier**, pas un dossier. Il compte
        # comme une copie versionnée — mais il montre une autre branche du même
        # dépôt, et le dire évite de lire une divergence de branche comme une
        # divergence de dépôt.
        self.worktree = marque.is_file()
        self.branche = None
        self.amont = None
        self.propre = True

        if self.depot:
            branche = git(chemin.parent, "rev-parse", "--abbrev-ref", "HEAD")
            self.branche = branche.strip() if branche else None
            suivi = git(chemin.parent, "status", "--porcelain", "--", FICHIER)
            self.propre = not (suivi or "").strip()
            if self.branche:
                amont = git(chemin.parent, "show", f"origin/{self.branche}:{FICHIER}")
                self.amont = amont

    @property
    def sha(self) -> str:
        return empreinte(self.contenu)

    @property
    def lignes(self) -> int:
        return self.contenu.count("\n")

    def situation(self) -> str:
        """Ce qui, dans ce dépôt, mérite d'être dit à côté de l'empreinte."""
        if not self.depot:
            return "pas un dépôt — ne se met à jour toute seule d'aucune façon"
        remarques = ["worktree"] if self.worktree else []
        if self.branche:
            remarques.append(self.branche)
        if not self.propre:
            remarques.append("modifiée, non commise")
        if self.amont is not None and empreinte(self.amont) != self.sha:
            remarques.append("diffère de son amont")
        elif self.amont is None and self.branche:
            remarques.append("sans amont")
        return ", ".join(remarques)


def rapporter(copies: list[Copie]) -> int:
    largeur = max(len(c.nom) for c in copies)
    print(f"Les copies de {FICHIER} sous {racine()}\n")
    for c in copies:
        print(f"  {c.nom:<{largeur}}  {c.sha}  {c.lignes:>4} lignes   {c.situation()}")

    empreintes = {c.sha for c in copies}
    if len(empreintes) == 1:
        print("\nLes copies concordent.")
        return 0

    # La copie de référence est le contenu que portent le plus de copies
    # **versionnées**. La racine ne pèse jamais dans ce compte : elle n'est
    # corrigée par rien, donc son accord ne prouve rien — c'est précisément en
    # la croyant faisant nombre qu'on impose un état périmé. À égalité, le nom
    # tranche, pour que deux exécutions disent la même chose.
    def poids(c: Copie) -> tuple[int, int, str]:
        tenue = sum(1 for a in copies if a.sha == c.sha and a.depot)
        return (tenue, 1 if c.depot else 0, c.nom)

    reference = max(copies, key=poids)
    if not reference.depot:
        print("\nAucune copie versionnée — rien qui fasse autorité.")
        return 1
    print(f"\n{len(empreintes)} versions différentes. Référence retenue : {reference.nom}.\n")

    for c in copies:
        if c.sha == reference.sha:
            continue
        print(f"── {c.nom} vs {reference.nom}")
        ecart = difflib.unified_diff(
            reference.contenu.splitlines(keepends=True),
            c.contenu.splitlines(keepends=True),
            fromfile=reference.nom,
            tofile=c.nom,
        )
        for ligne in ecart:
            print("   " + ligne.rstrip("\n"))
        print()

    print("Pour aligner : partir d'un dépôt à jour, porter le changement dans")
    print("chacun des autres par une branche et une PR, et n'écrire la racine")
    print("qu'en dernier. Jamais l'inverse — la racine n'est corrigée par rien,")
    print("donc la recopier impose un état périmé.")
    return 1


def main() -> int:
    base = racine()
    chemins = []
    a_la_racine = base / FICHIER
    if a_la_racine.exists():
        chemins.append(a_la_racine)
    chemins += sorted(
        d / FICHIER for d in base.iterdir() if d.is_dir() and (d / FICHIER).exists()
    )

    if len(chemins) < 2:
        print(f"Une seule copie trouvée sous {base} — rien à comparer.")
        return 0

    return rapporter([Copie(c, base) for c in chemins])


if __name__ == "__main__":
    sys.exit(main())
