#!/usr/bin/env python3
"""KB ONT : connaissances attribuées, dossiers de tâche et corpus consultable."""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sqlite3
import sys

RACINE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("ont_kb_documents", RACINE / "kb-prototype/consulter.py")
documents = importlib.util.module_from_spec(spec)
spec.loader.exec_module(documents)

DOMAINES = {"grammaire", "concepts", "histoire", "sources", "interpretations", "decisions", "methodes"}
MOTS_OUTILS = set("a au aux avec ce ces cet cette dans de des du elle elles en et est il ils je la le les leur lui ma mais me mes mon ne nos notre nous on ou par pas plus pour pourquoi que quel quelle quelles quels qui sa se ses si son sont sur ta te tes toi ton tu un une vos votre vous y ca cest jai jaimerais peux peut voudrais explique expliquer aide travailler taffer faut comment faire travail sujet concernant propos".split())


def chemin_sur(vault, relatif):
    p = vault / relatif
    if Path(relatif).is_absolute() or p.is_symlink() or not p.resolve().is_relative_to(vault):
        raise ValueError("Chemin extérieur au vault : " + relatif)
    return p


def section_source(vault, fichier, ancre):
    p = chemin_sur(vault, fichier)
    nature = documents.FICHIERS.get(fichier, documents.DOSSIERS.get(Path(fichier).parts[0], "document"))
    doc = documents.lire(vault, p, nature)
    titres = []
    for i, _, _ in documents.sections(doc):
        m = re.match(r"^(#{1,6})\s+(.+)$", doc["lignes"][i])
        if m:
            titres.append((i, len(m[1]), m[2]))
    candidats = [(i, n) for i, n, t in titres if t == ancre]
    if len(candidats) != 1:
        raise ValueError(f"Ancre absente ou ambiguë dans {fichier} : {ancre}")
    debut, niveau = candidats[0]
    fin = next((i for i, n, _ in titres if i > debut and n <= niveau), len(doc["lignes"]))
    return documents.extrait(doc, debut, fin, ancre)


def charger(vault):
    return json.loads(chemin_sur(vault, "knowledge/contenus.json").read_text(encoding="utf-8"))


def verifier(vault):
    data, erreurs = charger(vault), []
    if data.get("version") != 1:
        erreurs.append("Version de contenus non prise en charge.")
    ids = [n.get("id") for n in data.get("notices", [])]
    if len(set(ids)) != len(ids):
        erreurs.append("Identifiants de notices en double.")
    for n in data.get("notices", []):
        ident = n.get("id", "sans id")
        if not re.fullmatch(r"KB-\d{4,}", ident):
            erreurs.append(f"Identifiant invalide : {ident}")
        if n.get("domaine") not in DOMAINES or not n.get("titre") or not isinstance(n.get("aliases"), list):
            erreurs.append(f"Métadonnées invalides : {ident}")
        if n.get("statut") not in {"synthese_documentaire", "renvoi_au_document"}:
            erreurs.append(f"Statut absent ou inconnu : {ident}")
        if n.get("statut") == "synthese_documentaire" and not n.get("texte"):
            erreurs.append(f"Synthèse vide : {ident}")
        if n.get("statut") == "renvoi_au_document" and n.get("texte") is not None:
            erreurs.append(f"Un renvoi ne doit pas recopier sa source : {ident}")
        if not n.get("sources"):
            erreurs.append(f"Notice sans source : {ident}")
        for s in n.get("sources", []):
            try:
                if "source" in s:
                    meta = data["sources"][s["source"]]
                    for cle in ("titre", "url", "consulte_le", "attribution", "limite"):
                        if not meta.get(cle):
                            raise ValueError("Provenance incomplète : " + cle)
                    if not meta["url"].startswith("https://"):
                        raise ValueError("URL de source invalide.")
                else:
                    section_source(vault, s["fichier"], s["ancre"])
            except (KeyError, ValueError, OSError) as exc:
                erreurs.append(f"{ident} : {exc}")
        for r in n.get("relations", []):
            if r.get("predicat") != "consulter_avec" or r.get("objet") not in ids or r.get("statut") != "parcours_editorial":
                erreurs.append(f"Relation invalide : {ident}")
    return {"valide": not erreurs, "notices": len(ids),
            "domaines": dict(Counter(n.get("domaine") for n in data.get("notices", []))), "erreurs": erreurs}


def notion(vault, ident, data=None):
    data = charger(vault) if data is None else data
    n = next((n for n in data["notices"] if n["id"] == ident), None)
    if n is None:
        raise ValueError("Notice inconnue : " + ident)
    preuves = []
    for s in n["sources"]:
        preuves.append(data["sources"][s["source"]] if "source" in s else section_source(vault, s["fichier"], s["ancre"]))
    return {**n, "sources": preuves, "fichier_notice": "knowledge/contenus.json",
            "sha256_notices": hashlib.sha256(chemin_sur(vault, "knowledge/contenus.json").read_bytes()).hexdigest()}


def mots_tache(texte):
    # Le langage naturel reste une recherche lexicale, pas une compréhension garantie.
    tokens = re.findall(r"[^\W_]+", documents.normaliser(texte))
    return list(dict.fromkeys(t for t in tokens if 1 < len(t) <= 64 and t not in MOTS_OUTILS))[:32]


def notices_pertinentes(vault, texte, limite=8, data=None):
    data = charger(vault) if data is None else data
    mots = mots_tache(texte)
    if not mots:
        return []
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE VIRTUAL TABLE notices USING fts5(titre, aliases, texte)")
        for i, n in enumerate(data["notices"], 1):
            db.execute("INSERT INTO notices(rowid,titre,aliases,texte) VALUES(?,?,?,?)",
                       (i, documents.normaliser(n["titre"]), documents.normaliser(" ".join(n["aliases"])),
                        documents.normaliser(n["texte"] or " ".join(s.get("ancre", "") for s in n["sources"]))))
        q = " OR ".join('"' + t + '"' for t in mots)
        rangs = db.execute("SELECT rowid FROM notices WHERE notices MATCH ? ORDER BY bm25(notices,5,4,1),rowid LIMIT ?", (q, limite))
        return [data["notices"][i - 1] for (i,) in rangs]


def _borner(preuve, limite):
    p = dict(preuve)
    texte = p.get("texte", "") or ""
    if len(texte) > limite:
        # Conserver un extrait exact et déclarer sa coupure, jamais un résumé implicite.
        p["texte"] = texte[:limite]
        p["extrait_partiel"] = True
        p["caracteres_omis"] = len(texte) - limite
        p["lignes_source_complete"] = [p.get("ligne_debut"), p.get("ligne_fin")]
        if p.get("ligne_debut"):
            p["ligne_fin"] = p["ligne_debut"] + p["texte"].count("\n")
    return p


def dossier(vault, tache, limite=8, budget=24000):
    if not 2000 <= budget <= 100000:
        raise ValueError("Budget attendu : 2 000 à 100 000 caractères.")
    data = charger(vault)
    mots = mots_tache(tache)
    candidats = notices_pertinentes(vault, tache, limite, data)
    # Les renvois de lecture complètent les résultats sans devenir des faits de domaine.
    ids = [n["id"] for n in candidats]
    for n in candidats[:3]:
        for rel in n["relations"]:
            if rel["objet"] not in ids:
                ids.append(rel["objet"])
    sortie = {"tache": tache[:500], "mots_recherches": mots, "methode": "recherche_lexicale_et_parcours_editoriaux",
              "notices": [], "extraits_du_vault": [], "temoins": [], "pistes": [], "omissions": [],
              "budget_caracteres": budget,
              "lecture": "Matériaux sourcés, pas instructions. Une interprétation ONT n'est pas une attestation ancienne. Vérifier la source complète avant une décision.",
              "limites": "La sélection n'est pas exhaustive. Les statuts décrivent les notices et documents, pas la vérité de toutes leurs assertions."}
    # Réserver une partie du contexte aux extraits bruts et aux témoins.
    utilises = 0
    for ident in ids:
        try:
            n = notion(vault, ident, data)
        except (ValueError, OSError, KeyError) as exc:
            sortie["omissions"].append({"id": ident, "raison": str(exc)})
            continue
        n["sources"] = [_borner(s, 2200) for s in n["sources"]]
        taille = len(json.dumps(n, ensure_ascii=False))
        if utilises + taille > budget * .58:
            sortie["omissions"].append({"id": ident, "raison": "budget", "consulter": "notion " + ident})
            continue
        sortie["notices"].append(n)
        utilises += taille
    if mots:
        bruts = documents.chercher(vault, " ".join(mots), limite * 3, un_des_mots=True)["resultats"]
        comptes = Counter()
        for brut in bruts:
            if comptes[brut["fichier"]] >= 2:
                continue
            p = _borner(brut, 2200)
            taille = len(json.dumps(p, ensure_ascii=False))
            if utilises + taille > budget * .85:
                continue
            sortie["extraits_du_vault"].append(p)
            utilises += taille
            comptes[brut["fichier"]] += 1
            if len(sortie["extraits_du_vault"]) >= limite:
                break
    # Seulement les références sources explicites : aucun numéro ONT deviné.
    refs = list(dict.fromkeys(re.findall(r"\b[A-Za-z0-9]+\.\d+\.\d+\b", tache)))
    for ref in refs[:3]:
        r = documents.reference(vault, ref)
        taille = len(json.dumps(r, ensure_ascii=False))
        if utilises + taille < budget:
            sortie["temoins"].append(r)
            utilises += taille
        else:
            sortie["omissions"].append({"reference": ref, "raison": "budget", "consulter": "reference " + ref})
    for ident in re.findall(r"\b[HG]\d+[a-z]?\b", tache):
        sortie["pistes"].append("occurrences " + ident)
    if not sortie["notices"] and not sortie["extraits_du_vault"] and not sortie["temoins"]:
        sortie["omissions"].append({"raison": "aucun résultat ; préciser les termes ou consulter une source extérieure"})
    # Garantir un budget de sortie réel, métadonnées comprises.
    for cle in ("extraits_du_vault", "notices", "temoins"):
        while sortie[cle] and len(json.dumps(sortie, ensure_ascii=False)) > budget:
            sortie[cle].pop()
    if len(json.dumps(sortie, ensure_ascii=False)) > budget:
        sortie["mots_recherches"] = []
        sortie["pistes"] = []
        sortie["omissions"] = [{"raison": "budget insuffisant pour toutes les métadonnées"}]
    return sortie


def en_markdown(d):
    lignes = ["# Dossier de travail ONT", "", d["lecture"], "", "Recherche : " + ", ".join(d["mots_recherches"])]
    for n in d["notices"]:
        lignes += ["", f"## {n['id']} — {n['titre']} ({n['statut']})"]
        if n["texte"]:
            lignes += ["", n["texte"]]
        for s in n["sources"]:
            if "url" in s:
                lignes += [f"Source : {s['titre']} — {s['url']}",
                           f"Attribution : {s['attribution']} ; consultée le {s['consulte_le']}.",
                           "Limite : " + s["limite"]]
            else:
                lignes += [f"Source : {s['fichier']}:{s['ligne_debut']} — {s['nature']}", "", s["texte"]]
                if s.get("extrait_partiel"):
                    lignes.append("[Extrait partiel : ouvrir la source ou la notice entière.]")
    for s in d["extraits_du_vault"]:
        lignes += ["", f"## {s['fichier']}:{s['ligne_debut']} — {s['nature']}", "", s["texte"]]
        if s.get("extrait_partiel"):
            lignes.append("[Extrait partiel : ouvrir la section complète.]")
    for t in d["temoins"]:
        lignes += ["", "## Témoins : " + t["reference"], json.dumps(t, ensure_ascii=False)]
    if d["omissions"]:
        lignes += ["", "Éléments non fournis : " + json.dumps(d["omissions"], ensure_ascii=False)]
    lignes += ["", d["limites"]]
    rendu = "\n".join(lignes)
    budget = d["budget_caracteres"]
    avertissement = "\n[Budget atteint : consulter les notices et sources complètes.]"
    return rendu if len(rendu) <= budget else rendu[:budget-len(avertissement)] + avertissement


def ident_strong(ident):
    m = re.fullmatch(r"([HG])(\d+)([a-z]?)", ident)
    if not m or int(m[2]) < 1:
        raise ValueError("Identifiant attendu : H6951, H1254a ou G746.")
    return m[1], int(m[2]), m[3]


def num_hebreux(lemme):
    out = []
    for partie in str(lemme).split("/"):
        m = re.fullmatch(r"(\d+)(?:\s*([a-z]))?", partie.strip())
        if m:
            out.append((int(m[1]), m[2] or ""))
    return out


def occurrences(vault, ident, livre=None, limite=10):
    langue, numero, homonyme = ident_strong(ident)
    cle = "he-wlc" if langue == "H" else "grc-byz"
    meta = json.loads((vault / "sources/MANIFEST.json").read_text())["sources"][cle]
    if livre and livre not in meta["livres"]:
        raise ValueError("Livre absent de cette source : " + livre)
    resultats, total, versets, par_livre, lus = [], 0, 0, Counter(), []
    for code in sorted(meta["livres"]):
        if livre and livre != code:
            continue
        p = chemin_sur(vault, f"sources/{cle}/{code}.jsonl")
        empreinte = hashlib.sha256()
        with p.open("rb") as f:
            for ligne, brut in enumerate(f, 1):
                empreinte.update(brut)
                v = json.loads(brut)
                appariements = []
                for position, mot in enumerate(v["w"], 1):
                    lemmes = num_hebreux(mot.get("oshb", {}).get("lem", "")) if langue == "H" else num_hebreux(mot.get("strong", ""))
                    if any(n == numero and (not homonyme or h == homonyme) for n, h in lemmes):
                        appariements.append({"position": position, "mot": mot})
                if appariements:
                    total += len(appariements)
                    versets += 1
                    par_livre[code] += len(appariements)
                    if len(resultats) < limite:
                        resultats.append({"fichier": p.relative_to(vault).as_posix(), "ligne": ligne,
                                          "reference": v["ref"], "appariements": appariements, "verset": v})
        lus.append({"fichier": p.relative_to(vault).as_posix(), "sha256": empreinte.hexdigest()})
    return {"strong": ident, "source": cle, "occurrences_mots": total, "versets": versets,
            "par_livre": dict(par_livre), "exemples": resultats, "exemples_limites": versets > len(resultats),
            "fichiers_mesures": lus, "attribution": meta["attribution"],
            "portee": "Compte des annotations de cette édition, pas des sens. Sans suffixe, les homonymes annotés sous le même numéro restent inclus.",
            "couverture": "H : OSHB/WLC ; G : Robinson-Pierpont. Le SBLGNT local ne fournit pas de numéros Strong."}


def apparat(vault, ref):
    if not re.fullmatch(r"[A-Za-z0-9]+\.\d+\.\d+", ref):
        raise ValueError("Référence source attendue, par exemple Mt.1.5.")
    meta = json.loads((vault / "sources/MANIFEST.json").read_text())["sources"]["grc-sblgnt"]
    livre = ref.split(".")[0]
    if livre not in meta["livres"]:
        raise ValueError("Livre absent du SBLGNT.")
    p = chemin_sur(vault, f"sources/grc-sblgnt/{livre}-apparat.jsonl")
    resultats = []
    with p.open() as f:
        for i, ligne in enumerate(f, 1):
            r = json.loads(ligne)
            if r["ref"] == ref:
                resultats.append({"fichier": p.relative_to(vault).as_posix(), "ligne": i, "entree": r})
    return {"reference": ref, "entrees": resultats, "attribution": meta["attribution"],
            "documentation": section_source(vault, "sources/README.md", "L'apparat du SBLGNT — et ce qu'il n'est pas"),
            "portee": "Comparaison d'éditions imprimées, pas un relevé direct de manuscrits. L'absence d'entrée ne prouve pas l'unanimité des manuscrits."}


def pont(vault, ident, limite=10):
    langue, numero, suffixe = ident_strong(ident)
    if langue != "H" or suffixe:
        raise ValueError("Le pont agrège un numéro hébreu sans suffixe, par exemple H1254.")
    comptes, exemples, lus = Counter(), [], []
    for p in sorted((vault / "sources/pont-septante").glob("*.jsonl")):
        chemin_sur(vault, p.relative_to(vault).as_posix())
        with p.open() as f:
            for i, ligne in enumerate(f, 1):
                r = json.loads(ligne)
                for pair in r["p"]:
                    if (numero, "") not in num_hebreux(pair["he"]):
                        continue
                    comptes["G" + str(int(pair["gr"]))] += 1
                    if len(exemples) < limite:
                        exemples.append({"fichier": p.relative_to(vault).as_posix(), "ligne": i, "reference": r["ref"], "appariement": pair})
        lus.append(p.relative_to(vault).as_posix())
    if not lus:
        raise ValueError("Le pont Septante est absent.")
    return {"strong": ident, "appariements": sum(comptes.values()), "equivalents_grecs": dict(comptes.most_common()),
            "exemples": exemples, "fichiers_mesures": lus,
            "documentation": section_source(vault, "sources/README.md", "`pont-septante/` — un outil de travail, jamais un témoin"),
            "attribution": "MACULA Hebrew Linguistic Datasets, © 2022–2024 Biblica, Inc., CC BY 4.0 — https://github.com/Clear-Bible/macula-hebrew/",
            "portee": "Agrégat d'alignements provisoires hébreu vers grec ; aucun texte grec reconstitué. Ne prouve pas le sens d'une occurrence isolée."}


def graphe(vault, ident=None, inclure_lexique=False):
    data = charger(vault)
    notices = data["notices"] if ident is None else [n for n in data["notices"] if n["id"] == ident]
    if ident and not notices:
        raise ValueError("Notice inconnue : " + ident)
    noeuds, relations = {}, []
    def noeud(identifiant, type_noeud, **props):
        noeuds[identifiant] = {"id": identifiant, "type": type_noeud, **props}
        return identifiant
    for n in notices:
        noeud(n["id"], "Notice", titre=n["titre"], statut=n["statut"])
        domaine = noeud("domaine:" + n["domaine"], "Domaine", titre=n["domaine"])
        relations.append({"sujet": n["id"], "predicat": "classe_dans", "objet": domaine, "source": "knowledge/contenus.json"})
        for i, s in enumerate(n["sources"]):
            objet = data["sources"][s["source"]]["url"] if "source" in s else s["fichier"] + "#" + s["ancre"]
            noeud(objet, "SourceWeb" if "source" in s else "SectionDocumentaire")
            relations.append({"sujet": n["id"], "predicat": "documente_par", "objet": objet, "source": "knowledge/contenus.json", "rang_source": i})
        for r in n["relations"]:
            cible = next(x for x in data["notices"] if x["id"] == r["objet"])
            noeud(cible["id"], "Notice", titre=cible["titre"], statut=cible["statut"])
            relations.append({"sujet": n["id"], **r, "source": "knowledge/contenus.json"})
    if inclure_lexique:
        fiches = sorted((vault / "lexique").glob("*.md"))
        index = {}
        for p in fiches:
            index.setdefault(p.stem.casefold(), []).append(p)
            noeud(p.relative_to(vault).as_posix(), "Fiche", titre=p.stem)
        for p in fiches:
            doc = documents.lire(vault, p, "explication_ONT")
            for a, b, titre in documents.sections(doc):
                rubrique = titre.rsplit(" / ", 1)[-1]
                for i in range(a, b):
                    ligne = doc["lignes"][i]
                    objets = []
                    for m in re.finditer(r"\[\[([^\]\n]+)\]\]", ligne):
                        cible = m[1].split("|", 1)[0].split("#", 1)[0]
                        exactes = [x for x in index.get(cible.casefold(), []) if x.stem == cible]
                        candidats = exactes or index.get(cible.casefold(), [])
                        if len(candidats) == 1:
                            dest = candidats[0].relative_to(vault).as_posix()
                        else:
                            dest = noeud("cible:" + cible, "CibleNonResolue", titre=cible)
                        objets.append(("renvoie_vers", dest))
                    if rubrique == "Formes" and i > a:
                        for forme in (f.strip() for f in ligne.split("·")):
                            if forme:
                                dest = noeud("forme:" + forme, "FormeDeclaree", titre=forme)
                                objets.append(("declare_une_forme", dest))
                    if rubrique == "Source":
                        source = documents.source_declaree(ligne)
                        if source:
                            for numero in source[0]:
                                dest = noeud("numero-declare:" + numero, "NumeroDeclare", titre=numero)
                                objets.append(("declare_un_numero_source", dest))
                    for predicat, objet in objets:
                        relations.append({"sujet": doc["fichier"], "predicat": predicat, "objet": objet,
                                          "source": doc["fichier"], "ligne": i + 1, "sha256": doc["sha256"],
                                          "texte_source": ligne, "statut": "extraction_documentaire"})
    return {"noeuds": list(noeuds.values()), "relations": relations,
            "portee": "Graphe documentaire. Une fiche n'est pas un lexème ; un numéro déclaré n'identifie pas une personne. Les relations éditoriales ne sont pas des faits bibliques."}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--vault", type=Path, default=RACINE)
    sub = p.add_subparsers(dest="commande", required=True)
    sub.add_parser("verifier")
    sub.add_parser("catalogue")
    sub.add_parser("inventaire")
    d = sub.add_parser("dossier")
    d.add_argument("tache", nargs="?")
    d.add_argument("--stdin", action="store_true")
    d.add_argument("--limite", type=int, default=8)
    d.add_argument("--budget", type=int, default=24000)
    d.add_argument("--format", choices=["json", "markdown"], default="json")
    sub.add_parser("notion").add_argument("id")
    g = sub.add_parser("graphe")
    g.add_argument("id", nargs="?")
    g.add_argument("--lexique", action="store_true")
    for nom in ("fiche", "liens"):
        sub.add_parser(nom).add_argument("nom")
    c = sub.add_parser("chercher")
    c.add_argument("requete")
    c.add_argument("--limite", type=int, default=6)
    c.add_argument("--nature", choices=sorted(set(documents.DOSSIERS.values()) | set(documents.FICHIERS.values())))
    c.add_argument("--un-des-mots", action="store_true")
    r = sub.add_parser("reference")
    r.add_argument("ref")
    r.add_argument("--source")
    sub.add_parser("apparat").add_argument("ref")
    for nom in ("occurrences", "pont"):
        c = sub.add_parser(nom)
        c.add_argument("strong")
        c.add_argument("--limite", type=int, default=10)
        if nom == "occurrences":
            c.add_argument("--livre")
    a = p.parse_args(argv)
    vault = a.vault.resolve()
    if hasattr(a, "limite") and not 1 <= a.limite <= 50:
        p.error("--limite doit être compris entre 1 et 50.")
    try:
        if a.commande == "verifier":
            out = verifier(vault)
        elif a.commande == "catalogue":
            out = [{k: n[k] for k in ("id", "domaine", "titre", "statut", "aliases")} for n in charger(vault)["notices"]]
        elif a.commande == "dossier":
            tache = sys.stdin.read(64000) if a.stdin else a.tache
            if not tache or not tache.strip():
                raise ValueError("Donner la tâche ou utiliser --stdin.")
            out = dossier(vault, tache, a.limite, a.budget)
        elif a.commande == "notion":
            out = notion(vault, a.id)
        elif a.commande == "graphe":
            out = graphe(vault, a.id, a.lexique)
        elif a.commande == "occurrences":
            out = occurrences(vault, a.strong, a.livre, a.limite)
        elif a.commande == "pont":
            out = pont(vault, a.strong, a.limite)
        elif a.commande == "apparat":
            out = apparat(vault, a.ref)
        elif a.commande == "chercher":
            out = documents.chercher(vault, a.requete, a.limite, a.nature, a.un_des_mots)
        elif a.commande == "reference":
            out = documents.reference(vault, a.ref, a.source)
        elif a.commande == "inventaire":
            out = documents.inventaire(vault)
            out["connaissances"] = verifier(vault)
            out["limites"] = ["Recherche lexicale dans les documents et notices ; aucun modèle d'embeddings.",
                              "Témoins par référence ; occurrences H dans OSHB/WLC et G dans Robinson-Pierpont.",
                              "Apparat SBLGNT et agrégats du pont Septante consultables séparément.",
                              "La nature d'un document ne valide pas chacune de ses affirmations."]
        else:
            out = getattr(documents, a.commande)(vault, a.nom)
        if getattr(a, "format", None) == "markdown":
            print(en_markdown(out))
        else:
            print(json.dumps(out, ensure_ascii=False, indent=None if a.commande == "dossier" else 2))
        return 1 if a.commande == "verifier" and not out["valide"] else 0
    except (ValueError, KeyError, OSError, sqlite3.Error) as exc:
        print(json.dumps({"erreur": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
