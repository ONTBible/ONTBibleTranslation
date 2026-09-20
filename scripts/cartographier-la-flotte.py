#!/usr/bin/env python3
"""Relève où chaque agent se tient, et dit si le journal a pris du retard.

    ./scripts/cartographier-la-flotte.py             la carte, telle qu'elle est
    ./scripts/cartographier-la-flotte.py --comparer  ce qui a changé depuis le journal

## Pourquoi ce fichier existe

La carte de `SYNCHRONISATION.md` a été établie le 18 septembre 2026 en
interrogeant sept sessions une par une, puis en lisant l'état de Herdr pour
placer la huitième — qui ne peut envoyer aucun message.

**Ce travail ne doit pas se refaire.** Une carte recopiée à la main périme sans
que personne le voie : c'est exactement ce que le contrôle de concordance des
`SYNCHRONISATION.md` a été écrit pour empêcher sur un autre fichier, après que
la dérive eut tenu deux jours.

## Ce qu'il lit, et pourquoi c'est la bonne source

`~/.config/herdr/sessions/<session>/session.json` — la disposition que Herdr
persiste. Elle donne, pour chaque volet, son **dossier de lancement**, son
**moteur** et l'**identifiant de session de l'agent**.

C'est mieux que d'interroger les agents, pour trois raisons :

- **elle n'oublie personne.** Astra tourne sur codex et ne peut pas répondre ;
  elle est pourtant dans ce fichier ;
- **elle ne se trompe pas de mémoire.** Deux sessions ont affirmé ne pas voir
  leur place sans avoir lancé `env | grep HERDR` ; leurs réponses étaient
  argumentées et fausses ;
- **elle est une place, pas un processus.** Le nom change à un `/rename`, le
  socket est un PID, la référence change à une reconnexion. Le volet, non.

## Ce qu'il ne fait pas

**Il ne réécrit pas le journal.** Il dit ce qui a bougé ; c'est à un humain — ou
à la session qui tient le registre — de porter le changement, avec son récit.
Une carte qui se met à jour toute seule perd ce qui fait sa valeur : *pourquoi*
tel agent est là.

Et il ne relève **que ce qui dure** — espace, onglet, volet, moteur. Pas les
branches ni les PR : celles-ci bougent à l'heure, et ce sont des mesures, pas
une identité.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SESSIONS = Path.home() / ".config" / "herdr" / "sessions"
JOURNAL = Path(__file__).resolve().parent.parent / "SYNCHRONISATION.md"


def volets(session: str) -> list[dict]:
    """Chaque volet de la session, avec sa place et ce qui l'occupe."""
    fichier = SESSIONS / session / "session.json"
    if not fichier.exists():
        raise SystemExit(
            f"  Aucune session Herdr « {session} » sous {SESSIONS}.\n"
            f"  Sessions présentes : {', '.join(sorted(p.name for p in SESSIONS.iterdir()))}"
            if SESSIONS.exists()
            else f"  {SESSIONS} n'existe pas — Herdr n'est pas installé ici."
        )
    etat = json.loads(fichier.read_text(encoding="utf-8"))
    releve = []
    for espace in etat.get("workspaces", []):
        # Les index internes ne sont pas les numéros affichés : `public_*`
        # traduit. Ne jamais déduire un identifiant d'une position à l'écran —
        # dans « ONT App », l'onglet affiché en premier est `t3`.
        num_onglets = espace.get("public_tab_numbers", [])
        num_volets = espace.get("public_pane_numbers", {})
        for i, onglet in enumerate(espace.get("tabs", [])):
            for interne, volet in (onglet.get("panes") or {}).items():
                agent = volet.get("agent_session") or {}
                releve.append(
                    {
                        "espace": espace.get("custom_name") or espace["id"],
                        "onglet": onglet.get("custom_name") or "—",
                        "volet": f"{espace['id']}:p{num_volets.get(interne, '?')}",
                        "onglet_id": f"{espace['id']}:t{num_onglets[i]}"
                        if i < len(num_onglets)
                        else "?",
                        "moteur": agent.get("agent") or "—",
                        "dossier": volet.get("cwd") or "—",
                        "session": agent.get("value") or "",
                    }
                )
    return releve


def du_journal() -> set[str]:
    """Les volets que la table du journal déclare, lus dans sa colonne."""
    if not JOURNAL.exists():
        return set()
    texte = JOURNAL.read_text(encoding="utf-8")
    debut = texte.find("### Où chaque rôle se tient")
    if debut < 0:
        return set()
    fin = texte.find("\n#### ", debut)
    return set(re.findall(r"`(w[0-9A-Za-z]+:p\d+)`", texte[debut : fin if fin > 0 else len(texte)]))


def main() -> int:
    parseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parseur.add_argument("--session", default="ont", help="la session Herdr à relever")
    parseur.add_argument(
        "--comparer",
        action="store_true",
        help="dire ce qui a bougé depuis la table du journal",
    )
    args = parseur.parse_args()

    releve = volets(args.session)
    if not args.comparer:
        print(f"\n  Session Herdr « {args.session} » — {len(releve)} volets\n")
        largeur = max(len(v["espace"]) for v in releve)
        for v in sorted(releve, key=lambda x: x["volet"]):
            print(
                f"  {v['volet']:<8} {v['espace']:<{largeur}}  {v['onglet']:<12} "
                f"{v['moteur']:<7} {v['dossier']}"
            )
        print()
        return 0

    # **Le critère est le dossier, non la présence d'un agent.**
    #
    # Il a d'abord été « un volet sans agent n'est pas un rôle », pour écarter
    # le shell de l'auteur. C'était faux, et la première utilisation réelle l'a
    # montré : quand un espace vient d'être ouvert, son volet **n'a pas encore
    # d'agent attaché** — et il disparaissait donc de la comparaison, au moment
    # précis où il fallait le voir.
    #
    # Une garde qui se tait sur le cas neuf est une garde qui se tait quand on
    # a besoin d'elle. Le dossier, lui, dit tout de suite si le volet appartient
    # au projet.
    racine = Path.home() / "ONTBible"
    vivants = {
        v["volet"]
        for v in releve
        if v["dossier"] != "—" and Path(v["dossier"]) == racine
        or v["dossier"] != "—" and racine in Path(v["dossier"]).parents
    }
    ecrits = du_journal()
    if not ecrits:
        print("\n  Le journal ne porte aucune carte — rien à comparer.\n")
        return 1

    apparus = sorted(vivants - ecrits)
    disparus = sorted(ecrits - vivants)
    if not apparus and not disparus:
        print(f"\n  ✓ La carte du journal est à jour — {len(vivants)} volets.\n")
        return 0

    print("\n  La carte du journal a pris du retard.\n")
    for v in apparus:
        d = next(x for x in releve if x["volet"] == v)
        print(f"    + {v:<8} « {d['espace']} / {d['onglet']} »  {d['moteur']}")
    for v in disparus:
        print(f"    − {v:<8} déclaré au journal, absent de Herdr")
    print(
        "\n  Le porter à la main, avec son récit : une carte qui se met à jour\n"
        "  seule perd ce qui fait sa valeur — pourquoi tel agent est là.\n"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
