#!/usr/bin/env python3
"""Engendrer des passages à partir des sections trop grosses — sans toucher aux sources.

Pourquoi. La recherche de la KB classe par BM25, qui pénalise la longueur :
une section de 47 605 caractères perd contre une fiche de 900 qui porte le
même mot. Mesuré le 18 septembre 2026 sur `knowledge/banc-recherche.py` —
médiane des sections ratées 16 094 caractères, contre 3 500 pour les trouvées.

Pourquoi dériver et non découper la source. Le `CLAUDE.md` **interdit** de
poser un sous-titre dans son §2.5 : il fermerait la section, et les formes
déclarées en dessous deviendraient invisibles à la jointure sans que rien ne
le signale. Les sections les plus grosses sont donc exactement celles qu'on
ne peut pas couper sur place.

Et surtout : **un passage n'est pas une copie à maintenir.** Il est engendré,
jamais édité à la main, et il porte l'empreinte de la section dont il sort.
`--verifier` refuse qu'il s'en écarte. C'est le mécanisme posé le même jour
pour les sources locales des notices, et il est là pour la même raison —
deux copies qui divergent en silence sont le défaut, pas la solution.

    python3 knowledge/decouper.py             engendre
    python3 knowledge/decouper.py --verifier  contrôle la dérive, n'écrit rien
"""
import argparse
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys

RACINE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("ont_kb", RACINE / "knowledge/consulter.py")
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)

SORTIE = "passages"
SEUIL = 4000   # au-delà, la section se dilue et perd son propre sujet
VISEE = 2500   # taille visée d'un passage


def decouper(lignes):
    """Couper aux lignes vides, en visant VISEE sans jamais casser un bloc.

    On ne coupe pas au caractère : une ligne de tableau ou une puce tronquée
    ne dit plus rien. Les blocs de code sont gardés entiers.
    """
    blocs, courant, dans_code = [], [], False
    for l in lignes:
        if re.match(r"^\s{0,3}(`{3,}|~{3,})", l):
            dans_code = not dans_code
        if not l.strip() and not dans_code and courant:
            blocs.append(courant); courant = []
        else:
            courant.append(l)
    if courant:
        blocs.append(courant)

    # Un tableau n'a pas de ligne vide : sans ce traitement il reste un seul
    # bloc. C'est le cas du §3.2, 32 780 caractères — la section même que le
    # banc rate le plus. On coupe à la rangée, en redonnant l'en-tête à
    # chaque part : une rangée sans son en-tête ne dit plus de quoi elle parle.
    eclates = []
    for b in blocs:
        pleines = [x for x in b if x.strip()]
        est_tableau = len(pleines) > 3 and all(x.lstrip().startswith("|") for x in pleines)
        if est_tableau and sum(len(x) for x in pleines) > VISEE:
            tete, rangees, part, n = pleines[:2], pleines[2:], [], 0
            for r in rangees:
                if part and n + len(r) > VISEE:
                    eclates.append(tete + part); part, n = [], 0
                part.append(r); n += len(r)
            if part:
                eclates.append(tete + part)
        else:
            eclates.append(b)

    passages, accu, taille = [], [], 0
    for b in eclates:
        n = sum(len(x) for x in b)
        if accu and taille + n > VISEE:
            passages.append(accu); accu, taille = [], 0
        accu.extend(b + [""]); taille += n
    if accu:
        passages.append(accu)
    return passages


def deriver(vault):
    """Les passages que les sources commandent — calculés, rien d'écrit."""
    faits, derives = [], []
    for doc in kb.documents.documents(vault):
        if doc["fichier"] not in kb.documents.FICHIERS:
            continue  # on ne découpe que les documents de référence
        for debut, fin, titre in kb.documents.sections(doc):
            corps = doc["lignes"][debut + 1:fin]
            if sum(len(l) for l in corps) <= SEUIL:
                continue
            ex = kb.documents.extrait(doc, debut, fin, titre)
            empreinte = kb.empreinte_section(ex)
            feuille = titre.split(" / ")[-1]
            base = re.sub(r"[^a-z0-9]+", "-", kb.documents.normaliser(feuille)).strip("-")[:60]
            for i, p in enumerate(decouper(corps), 1):
                nom = f"{base}-{i:02d}.md"
                texte = (
                    f"# {feuille}\n\n"
                    f"*Passage engendré — ne pas éditer. "
                    f"Source : `{doc['fichier']}`, section « {feuille} », "
                    f"partie {i}. Empreinte de la section : `{empreinte}`. "
                    f"Régénérer : `python3 knowledge/decouper.py`.*\n\n"
                    + "\n".join(p).strip() + "\n")
                derives.append((nom, texte, doc["fichier"], titre, empreinte))
            faits.append((doc["fichier"], feuille, sum(len(l) for l in corps), i))

    return derives, faits


def engendrer(vault):
    derives, faits = deriver(vault)
    dossier = vault / SORTIE
    if dossier.exists():
        shutil.rmtree(dossier)   # engendré : on repart de zéro, jamais de fusion
    dossier.mkdir(parents=True)
    for nom, texte, *_ in derives:
        (dossier / nom).write_text(texte, encoding="utf-8")
    return {"sections_decoupees": len(faits), "passages": len(derives),
            "detail": [{"fichier": f, "section": s, "caracteres": n, "parties": k}
                       for f, s, n, k in faits]}


def verifier(vault):
    """Les passages posés disent-ils encore la vérité de leur source ?"""
    dossier = vault / SORTIE
    if not dossier.exists():
        return {"passages": 0, "perimes": [], "absents": [], "en_trop": []}
    attendus = {nom: texte for nom, texte, *_ in deriver(vault)[0]}
    presents = {p.name for p in dossier.glob("*.md")}
    perimes = [n for n, t in attendus.items()
               if n in presents and (dossier / n).read_text(encoding="utf-8") != t]
    return {"passages": len(attendus),
            "perimes": sorted(perimes),
            "absents": sorted(set(attendus) - presents),
            "en_trop": sorted(presents - set(attendus))}


def main(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--vault", default=str(RACINE))
    a.add_argument("--verifier", action="store_true")
    o = a.parse_args(argv)
    vault = Path(o.vault).resolve()
    if o.verifier:
        r = verifier(vault)
        print(json.dumps(r, ensure_ascii=False, indent=2))
        return 1 if (r["perimes"] or r["absents"] or r["en_trop"]) else 0
    print(json.dumps(engendrer(vault), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
