#!/usr/bin/env python3
"""Porte les noms propres d'une unité vers la couche des Shemot — §2.10.

Convertit `==Nom==` en `[[Nom]]`, et `[[cible|Nom]]` quand le nom est un
homonyme dont il faut désigner le porteur.

## Les zones qu'il ne touche jamais

L'ordre est celui du tokeniseur du pipeline, et c'est ce qui rend l'opération
sûre :

- **le niveau 3** — `(*Cham* / חָם)`. Le nom y est déjà porté ; le baliser une
  seconde fois ferait deux signaux pour une information (§2.5) ;
- **l'intérieur d'une translittération en italique** — `*Eretz Cham*`. Le §2.5
  écarte explicitement ces zones, et la conversion y produit en plus une
  **rupture de balisage** : `]]` suivi du `*` de fermeture se lit comme le `]*`
  d'une fin de glose, et la glose entière se casse. Constaté le 29 août 2026 sur
  `bereshit-9.md`, où le contrôle a rendu deux marqueurs déséquilibrés ;
- **les intraduisibles** — `**Shem**` reste un intraduisible. C'est ce qui règle
  l'homographie sans avoir à la deviner.

## Ce qu'il ne décide pas

Les homonymes. `Shem` le fils de Noach et `**Shem**` l'acte d'existence, `Adam`
le personnage et le générique : la casse ne les sépare pas, et le §2.5 bis
réserve cet arbitrage à l'auteur. Le script prend une table explicite et ne
devine rien.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Les homonymes, et le porteur que chaque occurrence désigne dans ce fichier.
# Rien ici n'est déduit : la table est écrite à la main, unité par unité.
HOMONYMES = {
    "Lamekh": "Lamekh-fils-de-Metoushelach",
    "Chanokh": "Chanokh-qui-marche-avec-Elohim",
    "Shem": "Shem-fils-de-Noach",
    "Mechouyaël": "Mechouyael",
    "Metoushaël": "Metoushael",
    # Un même porteur, deux **Shem** — la reformulation covenantale de
    # *Bereshit* 17. Les deux mènent à la même fiche, qui raconte le passage.
    "Sarai": "Sarai",
    "Sarah": "Sarai",
    "Avram": "Avraham",
}

# Un nom propre commence par une capitale. Ce qui suit est de l'apparat, pas un
# nom — le §2.5 bis les garde en accentuation.
APPARAT = ("Candidat", "Premier", "Avertissement", "Décision", "Version")


def zones_protegees(texte: str) -> list[tuple[int, int]]:
    """Les intervalles où la conversion ne doit pas entrer."""
    zones = []
    # le niveau 3
    zones += [(m.start(), m.end())
              for m in re.finditer(r"\(\*[^*]+\*\s*/\s*[^)]*\)", texte)]
    # une translittération en italique — `*Eretz Cham*`.
    #
    # Le motif doit exclure l'**ouverture de glose** `*[`, sans quoi il avale la
    # glose entière et protège des noms qui, eux, doivent être convertis : le
    # §2.10 s'applique dans les gloses. Une translittération ne contient donc ni
    # crochet, ni `[`, et reste courte.
    #
    # Et l'ouverture ne doit pas non plus suivre un `]` : le `*` qui **ferme**
    # une glose — `]*` — se laisse sinon apparier avec le `*` suivant, et tout
    # ce qui les sépare passe pour une italique. Sur `bereshit-10.md`, où chaque
    # nom est suivi d'un niveau 3, ce seul oubli a protégé **72 occurrences**
    # sur 409 — silencieusement, puisqu'un nom non converti ne lève rien.
    zones += [(m.start(), m.end())
              for m in re.finditer(r"(?<![*\]])\*(?!\[)[^*\n\[\]]{1,40}\*(?!\*)", texte)]
    # les intraduisibles
    zones += [(m.start(), m.end()) for m in re.finditer(r"\*\*[^*\n]+\*\*", texte)]
    return zones


def porter(chemin: Path, homonymes: dict[str, str] | None = None) -> int:
    texte = chemin.read_text(encoding="utf-8")
    table = {**HOMONYMES, **(homonymes or {})}
    protege = zones_protegees(texte)

    def dans_zone(i: int) -> bool:
        return any(a <= i < b for a, b in protege)

    # On remplace de la fin vers le début : les indices des zones restent bons.
    faits = 0
    for m in reversed(list(re.finditer(r"==([^=\n]{2,32})==", texte))):
        nom = m.group(1)
        if not nom[:1].isupper() or nom.startswith(APPARAT) or nom.startswith(("«", "*")):
            continue
        if dans_zone(m.start()):
            continue
        cible = table.get(nom)
        lien = f"[[{cible}|{nom}]]" if cible else f"[[{nom}]]"
        texte = texte[: m.start()] + lien + texte[m.end() :]
        faits += 1

    chemin.write_text(texte, encoding="utf-8")
    return faits


def main() -> int:
    if len(sys.argv) < 2:
        print("usage : porter-les-shemot.py <unité.md> [...]")
        return 2
    for arg in sys.argv[1:]:
        for chemin in Path(".").rglob(arg if arg.endswith(".md") else f"{arg}.md"):
            if chemin.parts[0] not in ("locked", "brouillons", "in-writing"):
                continue
            print(f"  {chemin.name:<32} {porter(chemin):>4} conversions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
