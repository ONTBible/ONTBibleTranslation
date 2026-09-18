#!/usr/bin/env python3
"""Regarde l'espace libre, prévient avant la panne, et nettoie avant le zéro.

    ./scripts/veiller-sur-l-espace.py            mesure et agit selon le seuil
    ./scripts/veiller-sur-l-espace.py --dire     mesure et n'agit jamais
    ./scripts/veiller-sur-l-espace.py --poser    installe l'agent qui l'appelle

## Pourquoi ce fichier existe

`recuperer-de-l-espace.py` sait rendre l'espace, et il le fait bien : le
18 septembre 2026 il en a rendu **82 Go** sur un disque tombé à **214 Mo**.
Ce n'est pas lui qui manquait.

Ce qui manquait, c'est **ce qui le déclenche**. Les deux fois où le disque est
tombé à zéro — le 1er septembre, puis le 18 —, on l'a su parce que l'auteur a
regardé une capture d'écran. Entre les deux, sept sessions ont compilé sans que
rien ne compte les octets restants.

Et la panne n'est pas ordinaire : à zéro octet, **Claude Code ne peut plus
lancer une commande**, parce que l'outil doit écrire son fichier de sortie avant
d'exécuter. La session qui pourrait réparer est exactement celle que la panne
désarme. Le 18, le message d'erreur était :

    ENOSPC: no space left on device

Donc la réparation ne pouvait plus venir d'ici : il a fallu que l'auteur ouvre
le Terminal de macOS et lance le script à la main.

**Un disque plein n'est donc pas l'accident, c'est la manifestation.** Nettoyer
une troisième fois serait la rustine ; ce fichier est la remontée à l'énoncé.

## Les deux seuils, et pourquoi deux

    ≥ 20 Go     silence          il reste de quoi travailler
    < 20 Go     on prévient      la place est encore là, l'action est humaine
    <  5 Go     on nettoie       personne n'a regardé, la panne est proche

Le premier seuil existe pour que la décision reste **humaine tant qu'elle peut
l'être**. Le second existe parce qu'à ce niveau il n'y a plus de décision à
prendre : en dessous, la session qui devrait agir ne le peut déjà plus.

`recuperer-de-l-espace.py` est appelé **sans `--tout`** : il ne touche qu'aux
postes sûrs, épargne les symboles des appareils physiques, et **refuse de
nettoyer pendant une compilation**. Cette dernière garde est la raison pour
laquelle un nettoyage automatique est acceptable ici : ce n'est pas nous qui
décidons qu'il est sûr, c'est lui, et il sait des choses que nous ne savons pas.

## Ce que la veille ne fait jamais

- **elle ne passe pas `--tout`.** Ce qui coûte une recompilation à une session
  voisine n'est pas à elle de le décider : c'est la règle de veille du projet —
  rien ne se supprime sans réclamation vérifiée ni accord de l'auteur ;
- **elle ne nettoie pas deux fois de suite.** Un délai de garde d'une heure
  sépare deux nettoyages : si le disque se remplit malgré un passage, c'est un
  problème qu'une répétition n'arrangera pas, et qu'il vaut mieux voir ;
- **elle ne se lance pas en double.** Un verrou tient le temps d'un passage,
  et il porte son propre âge pour ne pas rester coincé après un arrêt brutal ;
- **elle ne remplit pas le disque avec son journal.** Le fichier est rogné à
  64 Kio — un veilleur d'espace qui grossit sans fin serait une plaisanterie.

## Ce qu'elle laisse derrière elle

Un état lisible par tout le monde, dans `~/ONTBible/.espace-disque` : une ligne,
la date, les octets libres, et le seuil franchi. Les sessions peuvent le lire
sans lancer quoi que ce soit — ce qui compte quand justement plus rien ne se
lance.
"""

from __future__ import annotations

import argparse
import os
import plistlib
import subprocess
import sys
import time
from pathlib import Path

RACINE = Path.home() / "ONTBible"
ETAT = RACINE / ".espace-disque"
JOURNAL = Path.home() / "Library" / "Logs" / "ont-veille-espace.log"
VERROU = Path("/tmp/ont-veille-espace.lock")
DERNIER = Path("/tmp/ont-veille-espace.dernier-nettoyage")
AGENT = Path.home() / "Library" / "LaunchAgents" / "com.ontbible.veille-espace.plist"

GIGA = 1024**3
SEUIL_ALERTE = 20 * GIGA
SEUIL_NETTOYAGE = 5 * GIGA
GARDE_ENTRE_NETTOYAGES = 3600  # une heure
AGE_MAX_DU_VERROU = 1800  # une demi-heure
JOURNAL_MAX = 64 * 1024
INTERVALLE = 900  # un quart d'heure


def libre() -> int:
    """Les octets réellement disponibles, sur le volume qui porte le travail.

    On mesure `/System/Volumes/Data` et non `/` : sur APFS le second est le
    volume système scellé, et son chiffre ne dit rien de la place qu'un
    `DerivedData` occupe. Les deux partagent le même conteneur, donc la valeur
    est la même — mais elle est *juste pour la bonne raison*, et le jour où
    Apple les séparera ce fichier n'aura pas à être relu.
    """
    cible = "/System/Volumes/Data"
    if not Path(cible).exists():  # ailleurs que sur macOS
        cible = "/"
    s = os.statvfs(cible)
    return s.f_bavail * s.f_frsize


def humain(octets: int) -> str:
    for unite, seuil in (("To", GIGA * 1024), ("Go", GIGA), ("Mo", 1024**2)):
        if octets >= seuil:
            return f"{octets / seuil:.1f} {unite}"
    return f"{octets} o"


def inscrire(ligne: str) -> None:
    """Ajoute au journal, en le rognant s'il grossit."""
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    horodate = time.strftime("%Y-%m-%d %H:%M:%S")
    with JOURNAL.open("a", encoding="utf-8") as f:
        f.write(f"{horodate}  {ligne}\n")
    if JOURNAL.stat().st_size > JOURNAL_MAX:
        gardees = JOURNAL.read_text(encoding="utf-8").splitlines()[-300:]
        JOURNAL.write_text("\n".join(gardees) + "\n", encoding="utf-8")


def poser_l_etat(octets: int, seuil: str) -> None:
    """Le fichier que les sessions peuvent lire quand plus rien ne se lance."""
    try:
        RACINE.mkdir(parents=True, exist_ok=True)
        ETAT.write_text(
            f"{time.strftime('%Y-%m-%d %H:%M')}  {humain(octets)} libres  [{seuil}]\n",
            encoding="utf-8",
        )
    except OSError:
        pass  # sur un disque plein, l'état est le premier à ne plus s'écrire


def prevenir(titre: str, texte: str) -> None:
    """Une notification macOS — le seul canal qui atteigne l'auteur sans lui."""
    try:
        subprocess.run(
            [
                "osascript",
                "-e",
                f'display notification {texte!r} with title {titre!r}',
            ],
            check=False,
            capture_output=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        pass


def verrou_pris() -> bool:
    """Vrai si un autre passage tient le verrou — et qu'il n'est pas périmé."""
    if VERROU.exists():
        age = time.time() - VERROU.stat().st_mtime
        if age < AGE_MAX_DU_VERROU:
            return True
        VERROU.unlink(missing_ok=True)  # un passage interrompu ne bloque pas
    VERROU.write_text(str(os.getpid()), encoding="utf-8")
    return False


def nettoyage_trop_recent() -> bool:
    if not DERNIER.exists():
        return False
    return (time.time() - DERNIER.stat().st_mtime) < GARDE_ENTRE_NETTOYAGES


def nettoyer() -> tuple[int, str]:
    """Appelle le script du dépôt, sans `--tout`. Rend l'espace et sa sortie."""
    script = Path(__file__).resolve().parent / "recuperer-de-l-espace.py"
    avant = libre()
    r = subprocess.run(
        [sys.executable, str(script), "--nettoyer"],
        capture_output=True,
        text=True,
        timeout=900,
    )
    DERNIER.write_text(str(time.time()), encoding="utf-8")
    return libre() - avant, (r.stdout or "") + (r.stderr or "")


def poser_l_agent() -> int:
    """Installe l'agent de session qui appelle ce fichier tous les quarts d'heure.

    Un `LaunchAgent` plutôt qu'un `cron` : il est propre à la session ouverte,
    il se recharge au redémarrage sans rien demander, et `launchctl` dit
    lui-même s'il est chargé — trois choses que `cron` ne donne pas.
    """
    AGENT.parent.mkdir(parents=True, exist_ok=True)
    AGENT.write_bytes(
        plistlib.dumps(
            {
                "Label": "com.ontbible.veille-espace",
                "ProgramArguments": [sys.executable, str(Path(__file__).resolve())],
                "StartInterval": INTERVALLE,
                "RunAtLoad": True,
                "StandardErrorPath": str(JOURNAL),
            }
        )
    )
    subprocess.run(["launchctl", "unload", str(AGENT)], capture_output=True, check=False)
    r = subprocess.run(["launchctl", "load", str(AGENT)], capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  ✗ launchctl a refusé : {r.stderr.strip()}")
        return 1
    print(f"  ✓ Agent posé — un passage toutes les {INTERVALLE // 60} minutes.")
    print(f"    {AGENT}")
    print(f"    Journal : {JOURNAL}")
    print("\n    Pour le retirer :")
    print(f"      launchctl unload {AGENT} && rm {AGENT}\n")
    return 0


def main() -> int:
    parseur = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parseur.add_argument(
        "--dire", action="store_true", help="mesurer et n'agir en aucun cas"
    )
    parseur.add_argument(
        "--poser", action="store_true", help="installer l'agent qui appelle ce script"
    )
    args = parseur.parse_args()

    if args.poser:
        return poser_l_agent()

    octets = libre()

    if args.dire:
        print(f"\n  {humain(octets)} libres")
        seuil = (
            "au-dessus des seuils"
            if octets >= SEUIL_ALERTE
            else "sous l'alerte" if octets >= SEUIL_NETTOYAGE else "sous le nettoyage"
        )
        print(f"  {seuil} — alerte à {humain(SEUIL_ALERTE)}, "
              f"nettoyage à {humain(SEUIL_NETTOYAGE)}\n")
        return 0

    if octets >= SEUIL_ALERTE:
        poser_l_etat(octets, "sain")
        return 0

    if verrou_pris():
        return 0

    try:
        if octets >= SEUIL_NETTOYAGE:
            poser_l_etat(octets, "alerte")
            inscrire(f"alerte — {humain(octets)} libres")
            prevenir(
                "ONT — l'espace disque baisse",
                f"{humain(octets)} libres. Le nettoyage se lancera seul "
                f"sous {humain(SEUIL_NETTOYAGE)}.",
            )
            return 0

        # Sous le second seuil : plus personne ne peut décider, donc on agit.
        poser_l_etat(octets, "nettoyage")
        if nettoyage_trop_recent():
            inscrire(f"critique — {humain(octets)} libres, nettoyage déjà passé")
            prevenir(
                "ONT — le disque se remplit malgré le nettoyage",
                f"{humain(octets)} libres. Un passage a déjà eu lieu dans l'heure — "
                "à regarder à la main.",
            )
            return 1

        inscrire(f"critique — {humain(octets)} libres, nettoyage lancé")
        rendu, sortie = nettoyer()
        maintenant = libre()
        poser_l_etat(maintenant, "nettoyé")

        if "Une compilation tourne" in sortie:
            inscrire("nettoyage refusé — une compilation tourne")
            prevenir(
                "ONT — nettoyage impossible",
                f"{humain(maintenant)} libres, mais une compilation tourne. "
                "Rien n'a été supprimé.",
            )
            return 1

        inscrire(f"nettoyé — {humain(rendu)} rendus, {humain(maintenant)} libres")
        prevenir(
            "ONT — espace disque rendu",
            f"{humain(rendu)} rendus. {humain(maintenant)} libres.",
        )
        return 0
    finally:
        VERROU.unlink(missing_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
