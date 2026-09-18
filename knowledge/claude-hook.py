#!/usr/bin/env python3
"""UserPromptSubmit : joint un dossier local, sans bloquer le message utilisateur."""
import json
from pathlib import Path
import re
import sqlite3
import sys

import consulter


def message_sans_tache(prompt):
    """Reconnaître uniquement un message entier de réception ou de relance.

    Ne pas exclure un message parce qu'il commence par « merci » ou vient
    d'un pair : il peut aussi contenir une vraie question sur le corpus.
    """
    mots = re.findall(r"[^\W_]+", consulter.documents.normaliser(prompt))
    texte = " ".join(mots)
    if not texte:
        return True
    formules = (
        r"salut|bonjour|bonsoir|merci(?: beaucoup)?|ok(?:ay|i)?|oui|non|go",
        r"vas ?y|continue|bien recu|c ?est recu|j ?ai bien recu|entendu",
        r"d accord|parfait|a bientot",
        r"(?:les )?(?:\d+ )?tests (?:passent|sont passes)",
    )
    formule = "(?:" + "|".join(formules) + ")"
    return re.fullmatch(formule + "(?: " + formule + ")*", texte) is not None


def contexte(evenement):
    if evenement.get("hook_event_name") != "UserPromptSubmit":
        return None
    prompt = evenement.get("prompt", "")
    if not isinstance(prompt, str) or not prompt.strip():
        return None
    if message_sans_tache(prompt):
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
    # Le hook appelle dossier() directement : le compteur de main() ne le voit
    # pas. Distinguer cet appel automatique, sans journaliser son message.
    consulter.journaliser(vault, "hook:dossier")
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
