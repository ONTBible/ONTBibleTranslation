#!/usr/bin/env python3
"""Consultation ONT : sources exactes, recherche locale, aucune écriture du vault."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys
import unicodedata

DOSSIERS = {"lexique": "explication_ONT", "locked": "traduction_verrouillee",
            "brouillons": "brouillon", "context": "note_de_travail"}
FICHIERS = {"CLAUDE.md": "conventions_et_historique_ONT",
            "SYNCHRONISATION.md": "methode_et_journal_historique",
            "corpus-order.md": "ordre_du_corpus",
            "sources/README.md": "documentation_des_sources"}


def normaliser(texte):
    return "".join(c for c in unicodedata.normalize("NFD", texte.casefold())
                   if not unicodedata.combining(c))


def lire(vault, chemin, nature):
    if chemin.is_symlink() or not chemin.resolve().is_relative_to(vault):
        raise ValueError("La source doit être un fichier du vault.")
    brut = chemin.read_bytes()
    return {"fichier": chemin.relative_to(vault).as_posix(), "nature": nature,
            "sha256": hashlib.sha256(brut).hexdigest(),
            "lignes": brut.decode("utf-8").splitlines()}


def documents(vault):
    for nom, nature in FICHIERS.items():
        p = vault / nom
        if p.is_file():
            yield lire(vault, p, nature)
    for nom, nature in DOSSIERS.items():
        for p in sorted((vault / nom).rglob("*.md")):
            yield lire(vault, p, nature)


def sections(doc):
    debut, titre, pile, cloture = 0, doc["fichier"], [], None
    for i, ligne in enumerate(doc["lignes"]):
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})", ligne)
        if fence:
            marque = fence[1]
            if cloture is None:
                cloture = marque
            elif marque[0] == cloture[0] and len(marque) >= len(cloture):
                cloture = None
            continue
        match = re.match(r"^(#{1,6})\s+(.+)", ligne) if cloture is None else None
        if match:
            if i > debut:
                yield debut, i, titre
            niveau = len(match[1])
            pile = [(n, t) for n, t in pile if n < niveau]
            pile.append((niveau, match[2]))
            titre = " / ".join(t for _, t in pile)
            debut = i
    if len(doc["lignes"]) > debut:
        yield debut, len(doc["lignes"]), titre


def extrait(doc, debut, fin, titre=None):
    return {k: doc[k] for k in ("fichier", "nature", "sha256")} | {
        "ligne_debut": debut + 1, "ligne_fin": fin, "section": titre,
        "texte": "\n".join(doc["lignes"][debut:fin])}


def chercher(vault, requete, limite=6, nature=None, un_des_mots=False):
    mots = re.findall(r"\w+", normaliser(requete))
    if not mots:
        raise ValueError("Donner au moins un mot à chercher.")
    docs, morceaux = list(documents(vault)), []
    with sqlite3.connect(":memory:") as base:
        base.execute("CREATE VIRTUAL TABLE recherche USING fts5(fichier, titre, texte)")
        for doc in docs:
            if nature and doc["nature"] != nature:
                continue
            for debut, fin, titre in sections(doc):
                if not any(l.strip() and not l.startswith("#") for l in doc["lignes"][debut:fin]):
                    continue
                morceaux.append((doc, debut, fin, titre))
                base.execute("INSERT INTO recherche(rowid, fichier, titre, texte) VALUES (?, ?, ?, ?)",
                             (len(morceaux), normaliser(doc["fichier"]), normaliser(titre),
                              normaliser("\n".join(doc["lignes"][debut:fin]))))
        expression = "texte : (" + (" OR " if un_des_mots else " AND ").join('"' + m + '"' for m in mots) + ")"
        lignes = base.execute("SELECT rowid FROM recherche WHERE recherche MATCH ? "
                              "ORDER BY bm25(recherche, 8, 5, 1), rowid LIMIT ?", (expression, limite))
        resultats = []
        for (identifiant,) in lignes:
            doc, debut, fin, titre = morceaux[identifiant - 1]
            points = [i for i in range(debut + 1, fin)
                      if any(m in normaliser(doc["lignes"][i]) for m in mots)]
            point = points[0] if points else debut
            a, b = (debut, fin) if fin - debut <= 40 else (max(debut, point - 3), min(fin, point + 18))
            resultat = extrait(doc, a, b, titre)
            resultat.update(section_lignes=[debut + 1, fin], extrait_partiel=a != debut or b != fin)
            resultats.append(resultat)
    return {"requete": requete, "recherche": "lexicale", "limite": limite,
            "documents_parcourus": len(docs), "resultats": resultats,
            "absence": "Aucun résultat ne prouve pas une absence dans le corpus."}


def resoudre_fiche(vault, nom):
    cible = nom.removesuffix(".md")
    fiches = sorted((vault / "lexique").glob("*.md"))
    exactes = [p for p in fiches if p.stem == cible]
    candidates = exactes or [p for p in fiches if p.stem.casefold() == cible.casefold()]
    if len(candidates) != 1:
        suggestions = [p.name for p in fiches if normaliser(cible) in normaliser(p.stem)]
        raise ValueError(f"Fiche absente ou ambiguë : {nom}. Candidats : {suggestions}")
    return lire(vault, candidates[0], "explication_ONT")


def fiche(vault, nom):
    doc = resoudre_fiche(vault, nom)
    return extrait(doc, 0, len(doc["lignes"]))


def source_declaree(ligne):
    """Lit la convention « numéro [suffixe] + … · graphie », sans inférence.

    Le suffixe d'homonyme appartient à la référence déclarée. La preuve
    conserve la ligne originale ; seul l'espacement de la référence est normalisé.
    """
    numero = r"[0-9]+(?:\s*[a-z])?"
    m = re.fullmatch(r"\s*(" + numero + r"(?:\s*\+\s*" + numero + r")*)\s*·\s*(\S.*?)\s*", ligne)
    if not m:
        return None
    numeros = []
    for valeur in m[1].split("+"):
        ident = re.fullmatch(r"\s*([0-9]+)\s*([a-z]?)\s*", valeur)
        numeros.append(ident[1] + (" " + ident[2] if ident[2] else ""))
    return numeros, m[2]


def liens(vault, nom):
    doc, resultats = resoudre_fiche(vault, nom), []

    def ajouter(predicat, objet, ligne, type_objet):
        resultats.append({"sujet": doc["fichier"], "predicat": predicat, "objet": objet,
                          "type_objet": type_objet, "preuve": extrait(doc, ligne, ligne + 1)})

    for a, b, titre in sections(doc):
        rubrique = titre.rsplit(" / ", 1)[-1]
        for i in range(a, b):
            ligne = doc["lignes"][i]
            for m in re.finditer(r"\[\[([^\]\n]+)\]\]", ligne):
                cible = m[1].split("|", 1)[0].split("#", 1)[0]
                ajouter("contient_un_wikilien", cible, i, "cible_textuelle")
                try:
                    resolu = resoudre_fiche(vault, cible)["fichier"]
                except ValueError:
                    resolu = None
                resultats[-1]["fiche_resolue"] = resolu
            if rubrique == "Formes" and i > a and ligne.strip():
                for forme in ligne.split("·"):
                    if forme.strip():
                        ajouter("declare_une_forme", forme.strip(), i, "forme_ecrite")
            if rubrique == "Source":
                source = source_declaree(ligne)
                if source:
                    for numero in source[0]:
                        ajouter("declare_un_numero_source", numero, i, "numero_dans_la_fiche")
                    ajouter("declare_une_graphie_source", source[1], i, "graphie_ecrite")
    return {"fiche": doc["fichier"], "relations": resultats,
            "portee": "Observations documentaires. Aucune parenté, racine ou dépendance inférée."}


def reference(vault, ref, source=None):
    if not re.fullmatch(r"[A-Za-z0-9]+\.\d+\.\d+", ref):
        raise ValueError("Référence attendue : Gen.1.1, par exemple.")
    manifeste = json.loads((vault / "sources/MANIFEST.json").read_text())
    if source and source not in manifeste["sources"]:
        raise ValueError("Source absente du manifeste.")
    livre, resultats = ref.split(".")[0], []
    for cle, meta in manifeste["sources"].items():
        if (source and source != cle) or livre not in meta.get("livres", {}):
            continue
        p = vault / "sources" / cle / (livre + ".jsonl")
        if p.is_symlink() or not p.resolve().is_relative_to(vault):
            raise ValueError("Le témoin doit être un fichier du vault.")
        with p.open() as f:
            for numero, ligne in enumerate(f, 1):
                verset = json.loads(ligne)
                if verset["ref"] == ref:
                    resultats.append({"source": cle, "fichier": p.relative_to(vault).as_posix(),
                                      "ligne": numero, "attribution": meta.get("attribution"),
                                      "provenance": {k: v for k, v in meta.items() if k != "livres"},
                                      "verset": verset})
    return {"reference": ref, "temoins": resultats,
            "absence": "Un témoin absent peut manquer au dépôt ou comporter une lacune."}


def inventaire(vault):
    docs = list(documents(vault))
    manifeste = json.loads((vault / "sources/MANIFEST.json").read_text())
    sources = []
    for cle, meta in manifeste["sources"].items():
        versets, apparat = 0, 0
        for p in sorted((vault / "sources" / cle).glob("*.jsonl")):
            with p.open() as f:
                compte = sum(1 for _ in f)
            if p.stem.endswith("-apparat"):
                apparat += compte
            else:
                versets += compte
        sources.append({"source": cle, "versets_sur_disque": versets,
                        "entrees_apparat_sur_disque": apparat,
                        "versets_declares": meta.get("totaux", {}).get("versets"),
                        "manifest": "sources/MANIFEST.json"})
    return {"documents": dict(Counter(d["nature"] for d in docs)), "sources": sources,
            "exclus_recherche": ["sessions", "README.md", "DECISIONS.md", "scripts", "in-writing"],
            "limites": ["Recherche lexicale sur les documents Markdown sélectionnés.",
                        "Versets sources consultables par référence.",
                        "Pont Septante et apparats non interrogeables dans cette version.",
                        "La nature d'un document ne valide pas chacune de ses affirmations."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--vault", type=Path, default=Path(__file__).resolve().parent.parent)
    sous = p.add_subparsers(dest="commande", required=True)
    sous.add_parser("inventaire")
    recherche = sous.add_parser("chercher")
    recherche.add_argument("requete")
    recherche.add_argument("--limite", type=int, default=6)
    recherche.add_argument("--nature", choices=sorted(set(DOSSIERS.values()) | set(FICHIERS.values())))
    recherche.add_argument("--un-des-mots", action="store_true")
    for commande in ("fiche", "liens"):
        sous.add_parser(commande).add_argument("nom")
    ref = sous.add_parser("reference")
    ref.add_argument("ref")
    ref.add_argument("--source")
    args = p.parse_args()
    vault = args.vault.resolve()
    if not (vault / "CLAUDE.md").is_file() or not (vault / "lexique").is_dir():
        p.error("--vault doit désigner ONTBibleTranslation.")
    try:
        if args.commande == "inventaire":
            resultat = inventaire(vault)
        elif args.commande == "chercher":
            if not 1 <= args.limite <= 50:
                raise ValueError("La limite doit être comprise entre 1 et 50.")
            resultat = chercher(vault, args.requete, args.limite, args.nature, args.un_des_mots)
        elif args.commande == "reference":
            resultat = reference(vault, args.ref, args.source)
        else:
            resultat = {"fiche": fiche, "liens": liens}[args.commande](vault, args.nom)
    except (ValueError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"erreur": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(resultat, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
