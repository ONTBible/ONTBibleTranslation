#!/usr/bin/env python3
"""Prépare un journal commun à partir des variantes relues, sans l'installer."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile

RACINE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("revue_journal", Path(__file__).with_name("preparer-journal.py"))
revue = importlib.util.module_from_spec(spec)
spec.loader.exec_module(revue)


def extraire_locales(texte):
    """Même portée de section que le contrôle commun, avec le texte original."""
    lignes = texte.splitlines(keepends=True)
    entrees, i = [], 0
    while i < len(lignes):
        titre = revue.journal.TITRE.match(lignes[i])
        if not (titre and revue.journal.LOCALE.search(lignes[i])):
            i += 1
            continue
        debut, niveau = i, len(titre[1])
        i += 1
        while i < len(lignes):
            suivant = revue.journal.TITRE.match(lignes[i])
            if suivant and len(suivant[1]) <= niveau:
                break
            i += 1
        entrees.append({"titre": lignes[debut].strip(), "ligne_source": debut + 1,
                        "texte": "".join(lignes[debut:i])})
    return entrees


def preparer_locales(copies):
    """Préserve les notes intégrées avant tout remplacement futur du tronc."""
    migrations = []
    for copie in copies:
        source = Path(copie["fichier"])
        brut = source.read_bytes().decode("utf-8")
        if revue.empreinte(brut) != copie["sha256"]:
            raise ValueError("Journal modifié depuis sa lecture : " + str(source))
        cible = source.with_name("SYNCHRONISATION-locale.md")
        if cible.is_symlink():
            raise ValueError("Journal local symbolique à examiner : " + str(cible))
        ancien = cible.read_bytes().decode("utf-8") if cible.exists() else None
        existantes = {}
        for e in extraire_locales(ancien or ""):
            contenu = revue.sans_separateur_final(e["texte"])
            if e["titre"] in existantes and existantes[e["titre"]] != contenu:
                raise ValueError("Variantes locales à revoir : " + e["titre"])
            existantes[e["titre"]] = contenu
        texte = ancien or ""
        entrees = extraire_locales(brut)
        for e in entrees:
            contenu = revue.sans_separateur_final(e["texte"])
            if e["titre"] in existantes:
                if existantes[e["titre"]] != contenu:
                    raise ValueError("Conflit avec le journal local : " + str(cible) + " — " + e["titre"])
                e["action"] = "deja_presente_a_identique"
            else:
                if not texte:
                    texte = "# Journal local de " + source.parent.name + "\n"
                # Ne pas modifier le préambule ni les entrées du fichier existant.
                texte += "\n\n" + e["texte"]
                existantes[e["titre"]] = contenu
                e["action"] = "ajout_propose"
        # Relecture après assemblage : les sous-sections ne doivent pas être avalées.
        relues = {e["titre"]: revue.sans_separateur_final(e["texte"])
                  for e in extraire_locales(texte)}
        if relues != existantes:
            raise ValueError("La migration locale change la structure : " + str(cible))
        migrations.append({"source": str(source), "sha256_source": copie["sha256"],
                           "cible": str(cible), "existe_avant": ancien is not None,
                           "sha256_avant": revue.empreinte(ancien) if ancien is not None else None,
                           "contenu_propose": texte if ancien is not None or entrees else None,
                           "sha256_apres": revue.empreinte(texte) if ancien is not None or entrees else None,
                           "changement_propose": bool(entrees) and texte != ancien,
                           "entrees_a_preserver": entrees})
    return migrations


def reconcilier(rapport, resolutions):
    preambules = {p["sha256"]: p["texte"] for p in rapport["preambules"]}
    if sorted(preambules) != resolutions["preambules_examines"]:
        raise ValueError("Les préambules ont changé : une nouvelle revue est nécessaire.")
    # Fusion textuelle uniquement ; aucun index Git ni journal source n'est écrit.
    with tempfile.TemporaryDirectory() as tmp:
        fichiers = []
        for role in ("vault", "base", "complement"):
            p = Path(tmp) / role
            p.write_text(preambules[resolutions["preambules"][role]], encoding="utf-8")
            fichiers.append(str(p))
        fusion = subprocess.run(["git", "merge-file", "-p", *fichiers], capture_output=True, text=True)
        if fusion.returncode:
            raise ValueError("Conflit dans le préambule : résoudre avant de préparer le journal.")
    morceaux, decisions = [fusion.stdout.rstrip()], []
    conflits = {e["titre"] for e in rapport["entrees"] if e["divergence_contenu"]
                and not e["difference_limitee_au_separateur_final"]}
    if conflits != set(resolutions["entrees"]):
        raise ValueError("La liste des divergences a changé : revoir les résolutions.")
    # L'ordre du relevé conserve les séquences des exemplaires ; les entrées
    # supplémentaires se placent après elles, sans deviner l'heure d'une journée.
    for e in rapport["entrees"]:
        variantes = e["variantes"]
        if e["divergence_niveau"]:
            raise ValueError("Hiérarchie à revoir : " + e["titre"])
        if e["titre"] in conflits:
            choix = resolutions["entrees"][e["titre"]]
            if sorted(v["sha256_corps"] for v in variantes) != choix["variantes_examinees"]:
                raise ValueError("Variante non relue : " + e["titre"])
            retenus = [v for v in variantes if revue.empreinte(revue.sans_separateur_final(v["corps"]))
                       == choix["sha256_corps_normalise"]]
            if not retenus:
                raise ValueError("Résolution absente des sources : " + e["titre"])
            v = retenus[0]
            motif = choix["motif"]
        else:
            v = variantes[0]
            motif = "Texte identique ; seul le séparateur final est uniformisé si nécessaire."
        corps = revue.sans_separateur_final(v["corps"])
        niveau = v["origines"][0]["niveau_titre"]
        morceaux.append("#" * niveau + " " + e["titre"] + "\n\n" + corps)
        decisions.append({"titre": e["titre"], "sha256_corps_normalise": revue.empreinte(corps),
                          "origines_retenues": v["origines"], "motif": motif,
                          "variantes_examinees": [x["sha256_corps"] for x in variantes]})
    texte = "\n\n---\n\n".join(morceaux) + "\n"
    # Chaque entrée doit encore exister après assemblage avec son corps exact.
    _, relues = revue.decouper(texte)
    attendu = [(e["titre"], e["sha256_corps_normalise"]) for e in decisions]
    obtenu = [(e["titre"], revue.empreinte(revue.sans_separateur_final(e["corps"]))) for e in relues]
    if obtenu != attendu:
        raise ValueError("L'assemblage a changé la structure des entrées.")
    return {"type": "journal_reconcilie_propose_non_applique", "texte": texte,
            "sha256": revue.empreinte(texte), "entrees": decisions, "copies_lues": rapport["copies"],
            "reference_historique": resolutions["reference_historique"],
            "migrations_locales": preparer_locales(rapport["copies"]),
            "limites": ["La racine n'est pas une source candidate.",
                        "Les variantes non retenues restent dans journaux.json et les choix dans journal-resolutions.json.",
                        "La proposition rassemble les copies de travail examinées ; elle n'atteste pas leur publication.",
                        "Installer les migrations locales proposées avant de remplacer leurs journaux sources ; vérifier toutes les préimages.",
                        "L'arrivée de la KB doit être inscrite lors de son raccordement effectif, avec ses preuves."]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parent", type=Path, default=RACINE.parent)
    a = p.parse_args()
    try:
        rapport = revue.preparer(a.parent.resolve())
        resolutions = json.loads((RACINE / "knowledge/journal-resolutions.json").read_text())
        proposition = reconcilier(rapport, resolutions)
        for copie in rapport["copies"]:
            if hashlib.sha256(Path(copie["fichier"]).read_bytes()).hexdigest() != copie["sha256"]:
                raise ValueError("Une source a changé pendant la préparation : " + copie["fichier"])
        for migration in proposition["migrations_locales"]:
            cible = Path(migration["cible"])
            actuel = hashlib.sha256(cible.read_bytes()).hexdigest() if cible.exists() else None
            if actuel != migration["sha256_avant"]:
                raise ValueError("Un journal local a changé pendant la préparation : " + str(cible))
        dossier = RACINE / "knowledge/preparation"
        if not dossier.resolve().is_relative_to(RACINE):
            raise ValueError("Le dossier de sortie doit rester dans le vault.")
        for nom in ("journaux.json", "journal-reconcilie.json", "journal-reconcilie.txt"):
            if (dossier / nom).is_symlink():
                raise ValueError("Sortie symbolique à examiner : " + str(dossier / nom))
        dossier.mkdir(exist_ok=True)
        for nom, data in (("journaux.json", rapport), ("journal-reconcilie.json", proposition)):
            (dossier / nom).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (dossier / "journal-reconcilie.txt").write_text(proposition["texte"], encoding="utf-8")
    except (ValueError, OSError, KeyError) as exc:
        p.error(str(exc))
    print(json.dumps({"entrees": len(proposition["entrees"]), "sha256": proposition["sha256"],
                      "migrations_locales": sum(m["changement_propose"] for m in proposition["migrations_locales"]),
                      "entrees_locales_a_preserver": sum(len(m["entrees_a_preserver"]) for m in proposition["migrations_locales"]),
                      "proposition": str(dossier / "journal-reconcilie.txt"), "journaux_modifies": 0}, ensure_ascii=False))


if __name__ == "__main__":
    main()
