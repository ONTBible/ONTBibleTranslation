#!/usr/bin/env python3
"""Prépare les changements des assistants voisins, sans écrire chez eux."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import shlex

RACINE = Path(__file__).resolve().parent.parent
DEBUT = "<!-- ONT-KB:debut -->"
FIN = "<!-- ONT-KB:fin -->"


def empreinte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def bloc(ancien, contenu):
    nouveau = DEBUT + "\n" + contenu.rstrip() + "\n" + FIN
    if ancien.count(DEBUT) != ancien.count(FIN) or ancien.count(DEBUT) > 1:
        raise ValueError("Marqueurs KB invalides dans les instructions existantes.")
    if DEBUT in ancien:
        a, b = ancien.index(DEBUT), ancien.index(FIN) + len(FIN)
        if b < a:
            raise ValueError("Ordre des marqueurs KB invalide.")
        return ancien[:a] + nouveau + ancien[b:]
    return ancien.rstrip() + ("\n\n" if ancien.strip() else "") + nouveau + "\n"


def reglages(ancien, commande, codex=False):
    data = json.loads(ancien) if ancien.strip() else {}
    if not isinstance(data, dict):
        raise ValueError("Les réglages existants ne sont pas un objet JSON.")
    hooks = data.setdefault("hooks", {})
    if not isinstance(hooks, dict):
        raise ValueError("Le champ hooks existant est invalide.")
    evenement = hooks.setdefault("UserPromptSubmit", [])
    if not isinstance(evenement, list):
        raise ValueError("UserPromptSubmit doit être une liste.")
    for groupe in evenement:
        for h in groupe.get("hooks", []):
            if h.get("command") == commande:
                return ancien
    handler = {"type": "command", "command": commande, "timeout": 10}
    if codex:
        handler.update(statusMessage="Consultation de la KB ONT", additionalContextLimit=12000)
    evenement.append({"hooks": [handler]})
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def preparer(parent):
    changements = []
    for nom, prefixe in (("racine", "ONTBibleTranslation"), ("ONTBibleApp", "../ONTBibleTranslation"),
                         ("ONTBibleWebapp", "../ONTBibleTranslation"), ("ONTBibleTranslation", ".")):
        dossier = parent if nom == "racine" else parent / nom
        if not dossier.is_dir():
            raise ValueError("Dossier absent : " + str(dossier))
        instruction = (f"Pour les tâches qui touchent au corpus ONT, lire `{prefixe}/knowledge/ASSISTANTS.md`.\n"
                       f"Préparer le contexte avec `python3 {prefixe}/knowledge/consulter.py dossier`\n"
                       "et une description de la tâche correctement citée, ou `--stdin`.\n"
                       "Lire les sources pertinentes avant de conclure. La KB ne remplace pas\n"
                       "les instructions de la session ni les conventions de traduction.")
        commande = f'python3 "${{CLAUDE_PROJECT_DIR}}/{prefixe}/knowledge/claude-hook.py"'
        commande_codex = ("python3 " + shlex.quote(str(parent / "ONTBibleTranslation/knowledge/claude-hook.py"))
                          if nom == "racine" else
                          'python3 "$(git rev-parse --show-toplevel)/' +
                          ("" if nom == "ONTBibleTranslation" else "../ONTBibleTranslation/") +
                          'knowledge/claude-hook.py"')
        fichiers = ((".codex/hooks.json",) if nom == "ONTBibleTranslation" else
                    ("AGENTS.md", "CLAUDE.md", ".claude/settings.json", ".codex/hooks.json"))
        for fichier in fichiers:
            p = dossier / fichier
            if p.is_symlink():
                raise ValueError("Lien symbolique à examiner : " + str(p))
            existe = p.exists()
            ancien = p.read_text(encoding="utf-8") if existe else ""
            if fichier == ".codex/hooks.json":
                nouveau = reglages(ancien, commande_codex, codex=True)
            else:
                nouveau = reglages(ancien, commande) if fichier.endswith(".json") else bloc(ancien, instruction)
            if ancien != nouveau:
                changements.append({"cible": str(p), "existe": existe,
                                    "sha256_avant": empreinte(ancien) if existe else None,
                                    "sha256_apres": empreinte(nouveau), "contenu_propose": nouveau,
                                    "diff": "".join(difflib.unified_diff(ancien.splitlines(True), nouveau.splitlines(True),
                                                                        fromfile=str(p) if existe else "/dev/null", tofile=str(p)))})
    return {"type": "proposition_non_appliquee", "parent": str(parent), "changements": changements,
            "condition": "Revoir les différences et vérifier chaque préimage dans une session autorisée à écrire aux destinations.",
            "limite": "Ne réconcilie pas les journaux et ne prouve pas le chargement d'une session active.",
            "validation_codex": "Examiner /hooks et valider chaque définition après installation. Vérifier les éventuels hooks inline de config.toml pour éviter un double raccordement.",
            "portee": "Prépare la racine et les trois checkouts principaux ; les worktrees doivent recevoir les fichiers par leur propre mise à jour."}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parent", type=Path, default=RACINE.parent)
    p.add_argument("--sortie", type=Path, default=RACINE / "knowledge/preparation/raccordement.json")
    a = p.parse_args()
    sortie = a.sortie.resolve()
    if not sortie.is_relative_to(RACINE):
        p.error("La préparation s'écrit uniquement dans le dépôt du vault.")
    try:
        resultat = preparer(a.parent.resolve())
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(json.dumps(resultat, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (ValueError, OSError, TypeError) as exc:
        p.error(str(exc))
    print(json.dumps({"proposition": str(sortie), "changements": len(resultat["changements"]), "appliques": 0}, ensure_ascii=False))


if __name__ == "__main__":
    main()
