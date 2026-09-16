#!/usr/bin/env python3
"""Rassemble les variantes des journaux pour revue, sans élire ni écraser une copie."""
import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path
import re

RACINE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("journal_ont", RACINE / "scripts/concorder-la-synchronisation.py")
journal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(journal)
DATE = re.compile(r"^#{2,3}\s+(\d{1,2}(?:er|ᵉʳ)?\s+(?:janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s+20\d{2}\b.*)$")


def empreinte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def sans_separateur_final(texte):
    """Comparaison seulement : les variantes originales restent intégralement conservées."""
    lignes = texte.strip().splitlines()
    while lignes and lignes[-1].strip() in {"", "---"}:
        lignes.pop()
    return "\n".join(lignes)


def decouper(texte):
    """Découpage du tronc normalisé ; les numéros sont ceux de ce tronc, pas du disque."""
    lignes = texte.splitlines(keepends=True)
    debuts = [(i, m[1]) for i, ligne in enumerate(lignes) if (m := DATE.match(ligne))]
    preambule = "".join(lignes[:debuts[0][0]]) if debuts else texte
    entrees = []
    for rang, (i, titre) in enumerate(debuts):
        fin = debuts[rang + 1][0] if rang + 1 < len(debuts) else len(lignes)
        entrees.append({"titre": titre, "ligne_tronc": i + 1,
                        "niveau": len(lignes[i]) - len(lignes[i].lstrip("#")),
                        "texte": "".join(lignes[i:fin]),
                        "corps": "".join(lignes[i + 1:fin]).strip()})
    return preambule, entrees


def preparer(parent):
    dossiers = sorted(d for d in parent.iterdir() if d.is_dir() and (d / journal.FICHIER).is_file())
    groupes, copies, preambules = defaultdict(dict), [], {}
    for dossier in dossiers:
        p = dossier / journal.FICHIER
        if p.is_symlink():
            raise ValueError("Journal symbolique à examiner : " + str(p))
        brut = p.read_text(encoding="utf-8")
        tronc = journal.tronc(brut)
        preambule, entrees = decouper(tronc)
        copies.append({"fichier": str(p), "sha256": empreinte(brut), "sha256_tronc": empreinte(tronc),
                       "entrees_datees": len(entrees), "locales_dans_ce_fichier": journal.locales(brut)})
        cle = empreinte(preambule)
        preambules.setdefault(cle, {"sha256": cle, "texte": preambule, "copies": []})["copies"].append(str(p))
        for e in entrees:
            # Le niveau du titre est une variation de structure, signalée séparément.
            cle = empreinte(e["corps"])
            groupe = groupes[e["titre"]]
            groupe.setdefault(cle, {"sha256_corps": cle, "corps": e["corps"], "origines": []})["origines"].append({
                "fichier": str(p), "ligne_tronc": e["ligne_tronc"], "niveau_titre": e["niveau"]})
    entrees = []
    for titre, variantes in groupes.items():
        niveaux = {o["niveau_titre"] for v in variantes.values() for o in v["origines"]}
        presence = {o["fichier"] for v in variantes.values() for o in v["origines"]}
        entrees.append({"titre": titre, "divergence_contenu": len(variantes) > 1,
                        "difference_limitee_au_separateur_final": len(variantes) > 1 and
                        len({sans_separateur_final(v["corps"]) for v in variantes.values()}) == 1,
                        "divergence_niveau": len(niveaux) > 1,
                        "absent_de": [c["fichier"] for c in copies if c["fichier"] not in presence],
                        "variantes": list(variantes.values())})
    racine = parent / journal.FICHIER
    return {"type": "revue_non_appliquee", "copies": copies, "preambules": list(preambules.values()), "entrees": entrees,
            "racine_non_utilisee_comme_source": {"fichier": str(racine), "sha256": empreinte(racine.read_text()) if racine.is_file() else None},
            "bilan": {"copies": len(copies), "entrees_distinctes": len(entrees),
                       "divergences_contenu": sum(e["divergence_contenu"] for e in entrees),
                       "differences_separateur_final": sum(e["difference_limitee_au_separateur_final"] for e in entrees),
                       "divergences_niveau": sum(e["divergence_niveau"] for e in entrees),
                       "versions_preambule": len(preambules)},
            "limites": ["Les entrées sont regroupées par titre exact ; un renommage demeure deux entrées à rapprocher en revue.",
                        "Les variantes comprennent les exemplaires de travail ; elles ne remplacent pas les versions publiées.",
                        "Les origines donnent des lignes dans le tronc normalisé. Vérifier l'empreinte du fichier avant toute application.",
                        "La racine ne fournit aucune variante candidate. Aucun contenu n'est choisi par majorité."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parent", type=Path, default=RACINE.parent)
    p.add_argument("--sortie", type=Path, default=RACINE / "knowledge/preparation/journaux.json")
    a = p.parse_args()
    sortie = a.sortie.resolve()
    if not sortie.is_relative_to(RACINE):
        p.error("Le dossier de revue s'écrit uniquement dans le vault.")
    try:
        r = preparer(a.parent.resolve())
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    print(json.dumps({"rapport": str(sortie), **r["bilan"], "copies_modifiees": 0}, ensure_ascii=False))


if __name__ == "__main__":
    main()
