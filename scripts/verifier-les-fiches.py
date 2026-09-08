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

**Les blocs que la liseuse ne rend pas.** Elle en avale certains **sans rien
dire** : ils disparaissent chez le lecteur, en silence, et rien ne le signale.

Ce contrôle ne vaut donc que s'il décrit **ce que le consommateur fait
aujourd'hui**. Relevé dans `BlocDeFiche.swift` le 8 septembre 2026, en lisant
son `switch` :

    .paragraph  .heading  .list  .quote  .rule    rendus
    .verses  .table                               EmptyView() — avalés

Seuls les **tableaux** sont donc à signaler. Les versets ne concernent pas une
fiche, qui n'en porte pas.

**Ce que ce commentaire disait avant, et pourquoi c'est instructif.** Il tenait
les titres et les listes pour perdus, en nommant un `TermSheet.swift` qui ne
fait plus le rendu. C'était vrai jusqu'au 30 août 2026, date à laquelle le §2.5
ter a permis les titres intermédiaires *parce que la liseuse avait appris à les
rendre*. Le script n'a pas suivi, et il a signalé pendant neuf jours des fautes
qui n'en étaient plus — sur des fiches parfaitement rendues.

C'est le motif que le journal a nommé le 8 septembre : **une mesure juste dont
la fraîcheur est invisible**. Rien dans la sortie ne disait de quand datait la
capacité qu'elle supposait. D'où le relevé daté ci-dessus, et la règle qui
suit : **avant de croire ce contrôle, rouvrir `BlocDeFiche.swift` et comparer
son `switch` au tableau.**

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
            # Seuls les tableaux : voir le relevé daté de l'en-tête. Les titres,
            # listes, citations et filets sont rendus depuis le 30 août 2026.
            if n > 1 and nu.startswith("| "):
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
