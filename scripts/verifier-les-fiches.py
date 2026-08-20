#!/usr/bin/env python3
"""Contrôle les fiches de `lexique/` — et corrige le gras d'insistance.

    ./scripts/verifier-les-fiches.py            # simulation, n'écrit rien
    ./scripts/verifier-les-fiches.py --ecrire

## Ce qu'il vérifie

**Le gras qui ne mène nulle part.** `**…**` promet une entrée de lexique : le
mot sort en or et le lecteur le touche. Employé pour insister — « le poids
**réel** » —, il promet une fiche absente, et c'est le défaut que le §2.5 bis a
été écrit pour supprimer. La forme juste, pour insister, est `==…==`.

Le pipeline le relève déjà dans son rapport ; ce script le **corrige**, ce qui
est plus utile quand on écrit cent fiches d'affilée.

**Les blocs que la liseuse ne rend pas.** `TermSheet.swift` n'affiche que les
paragraphes et laisse tomber le reste **sans rien dire** : un titre
intermédiaire ou une liste disparaîtrait chez le lecteur, en silence. Seul le
titre `#` de première ligne est admis — le pipeline l'ignore.

## Pourquoi il lit `dist/glossary.json`

C'est la sortie du pipeline, donc la seule liste de lemmes qui fasse foi, formes
dérivées comprises. Une liste tenue à la main ici divergerait au premier terme
déclaré.
"""

import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
LEXIQUE = RACINE / "lexique"
GLOSSAIRE = RACINE.parent / "ONTBibleApp" / "dist" / "glossary.json"

GRAS = re.compile(r"\*\*([^*]+)\*\*")


def lemmes() -> set[str]:
    if not GLOSSAIRE.exists():
        sys.exit(f"{GLOSSAIRE} manque — lancer le pipeline d'abord")
    données = json.loads(GLOSSAIRE.read_text())
    entrées = données.get("entries", données) if isinstance(données, dict) else données
    connus = set()
    for e in entrées:
        connus.add(e["lemma"].lower())
        for f in e.get("forms") or []:
            connus.add(f.lower())
    return connus


def main() -> None:
    ecrire = "--ecrire" in sys.argv
    connus = lemmes()
    fiches = sorted(LEXIQUE.glob("*.md"))
    convertis, blocs = 0, []

    for f in fiches:
        texte = f.read_text(encoding="utf8")

        for n, ligne in enumerate(texte.split("\n"), 1):
            nu = ligne.strip()
            if n > 1 and (nu.startswith("#") or nu.startswith(("- ", "* ", "> ", "| "))):
                blocs.append(f"{f.name}:{n} — {nu[:60]}")

        def convertir(m: re.Match) -> str:
            nonlocal convertis
            if m.group(1).lower() in connus:
                return m.group(0)
            convertis += 1
            return f"=={m.group(1)}=="

        sortie = GRAS.sub(convertir, texte)
        if ecrire and sortie != texte:
            f.write_text(sortie, encoding="utf8")

    print(f"{len(fiches)} fiches")
    print(f"  {convertis} gras d'insistance {'convertis' if ecrire else 'à convertir'}")
    if blocs:
        print(f"  {len(blocs)} blocs que la liseuse ne rendra pas :")
        for b in blocs[:10]:
            print(f"    {b}")
    if not ecrire and (convertis or blocs):
        print("simulation — relancer avec --ecrire")
    if blocs:
        sys.exit(1)


main()
