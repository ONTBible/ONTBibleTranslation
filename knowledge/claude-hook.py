#!/usr/bin/env python3
"""UserPromptSubmit : joint un dossier local, sans bloquer le message utilisateur."""
import json
from pathlib import Path
import sqlite3
import sys

import consulter


def contexte(evenement):
    if evenement.get("hook_event_name") != "UserPromptSubmit":
        return None
    prompt = evenement.get("prompt", "")
    if not isinstance(prompt, str) or not prompt.strip():
        return None
    salutation = consulter.documents.normaliser(prompt).strip(" \n.!?🙂👋")
    if salutation in {"salut", "bonjour", "bonsoir", "merci", "ok", "oui", "non", "go"}:
        return None
    # Lire le checkout actif, y compris après un déplacement dans un worktree.
    courant = Path(evenement.get("cwd") or consulter.RACINE).resolve()
    # Privilégier un vault actif ; depuis App/Webapp, chercher le vault voisin.
    parents = (courant, *courant.parents)
    vault = next((p for p in parents
                  if (p / "knowledge/contenus.json").is_file() and (p / "lexique").is_dir()), None)
    if vault is None:
        vault = next((p / "ONTBibleTranslation" for p in parents
                      if (p / "ONTBibleTranslation/knowledge/contenus.json").is_file()
                      and (p / "ONTBibleTranslation/lexique").is_dir()), None)
    if vault is None:
        return "KB ONT : aucun vault trouvé dans le dossier actif ; consulter la KB explicitement si la tâche concerne l’ONT."
    dossier = consulter.dossier(vault, prompt[:16000], limite=5, budget=12000)
    if not dossier["notices"] and not dossier["extraits_du_vault"] and not dossier["temoins"]:
        return "KB ONT : aucun passage pertinent retrouvé pour ce message. Une recherche vide ne prouve pas une absence ; préciser les termes si nécessaire."
    return consulter.en_markdown(dossier)


def main():
    try:
        evenement = json.loads(sys.stdin.read(64000))
        if not isinstance(evenement, dict):
            raise ValueError("L'événement doit être un objet JSON.")
        texte = contexte(evenement)
    except (ValueError, OSError, KeyError, TypeError, sqlite3.Error) as exc:
        texte = "KB ONT indisponible : " + str(exc)[:500] + ". Consulter les sources directement et signaler cette limite."
    if texte:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": texte}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
