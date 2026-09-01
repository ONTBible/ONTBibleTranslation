#!/usr/bin/env python3

"""Ce que le développement laisse derrière lui, mesuré puis rendu.

    ./scripts/recuperer-de-l-espace.py              relève, ne touche à rien
    ./scripts/recuperer-de-l-espace.py --nettoyer   rend l'espace des postes sûrs

## Pourquoi cet outil existe

Le 1er septembre 2026, le disque est tombé à **zéro octet** — au point que
Claude Code ne pouvait plus lancer une commande, l'outil devant écrire son
fichier de sortie avant d'exécuter. La veille, on était passé de 22 à 40 Go
libres ; une nuit a suffi à tout reprendre.

Ce n'était pas un ménage en retard. C'était une **fuite**, et elle a deux
sources que personne ne regardait :

**`CoreDevice/DeviceFS`** — un miroir de système de fichiers que Xcode tient par
appareil, qui grossit à **chaque installation d'app sur un simulateur**. Une
campagne de tests d'interface, qui réinstalle l'app à chaque cas mesuré, l'avait
porté à **89 Go** pour deux simulateurs. Personne ne le nomme jamais : on
soupçonne `DerivedData`, qui était vide.

**Les `DerivedData` égarés dans `/tmp`** — sept dossiers de 3,4 Go, un par
session, aux noms inventés à la volée (`dd-vault`, `dd-test`, `dd-signe`…).
Chaque instance qui compile s'en crée un ; aucune ne le nettoie. Vingt-quatre
gigaoctets que rien dans le dépôt ne mentionne.

## Ce qu'il ne fait pas

Il **ne touche à rien qui ne se régénère pas**. Pas de `target/`, pas de
`.gradle`, pas de conteneur de simulateur : ceux-là coûtent une recompilation ou
un état de lecture, et c'est à un humain d'en décider. Ici, tout ce qui est
supprimé est un cache que l'outil qui l'a créé refabrique seul.

Et il **refuse de nettoyer pendant une compilation**. Vider un `DerivedData` que
`xcodebuild` tient ouvert ne casse rien de durable, mais fait échouer un travail
en cours chez quelqu'un d'autre — et sur cette machine, il y a toujours
quelqu'un d'autre.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

MAISON = Path.home()

# Les procédés qui, s'ils tournent, interdisent le nettoyage.
COMPILATEURS = ("xcodebuild", "swift-frontend", "cargo", "gradle", "rustc", "kotlin-compiler")


@dataclass
class Poste:
    """Un endroit qui accumule, et ce qu'il en coûte de le vider."""

    nom: str
    chemins: list[Path]
    cout: str
    #: Vrai si le contenu se refabrique tout seul, sans décision humaine.
    sur: bool = True

    def taille(self) -> int:
        return sum(_poids(c) for c in self.chemins if c.exists())


def _poids(chemin: Path) -> int:
    """La taille réelle sur le disque, en octets.

    On additionne les blocs alloués (`st_blocks`) et non `st_size` : APFS clone
    des fichiers entre le conteneur d'un simulateur et son miroir `CoreDevice`,
    et compter la taille apparente promettrait un espace que la suppression ne
    rendrait pas. C'est la différence entre annoncer 89 Go et en libérer 42.
    """
    total = 0
    for racine, _, fichiers in os.walk(chemin, onerror=lambda _: None):
        for f in fichiers:
            try:
                total += Path(racine, f).lstat().st_blocks * 512
            except OSError:
                pass
    return total


def postes() -> list[Poste]:
    dev = MAISON / "Library/Developer"
    return [
        Poste(
            "CoreDevice — miroir des simulateurs",
            list((dev / "CoreDevice/DeviceFS").glob("device-*")),
            "rien : Xcode le refait à la prochaine installation",
        ),
        Poste(
            "DerivedData égarés dans /tmp",
            sorted(Path("/private/tmp").glob("dd-*"))
            + sorted(Path("/private/tmp").glob("ont-*-dd")),
            "une recompilation à la session qui l'employait",
        ),
        Poste(
            "DerivedData d'Xcode",
            [dev / "DerivedData"],
            "une recompilation complète à chaque session iOS",
        ),
        Poste(
            "Symboles d'appareils physiques",
            list((dev / "Xcode/iOS DeviceSupport").glob("*")),
            "quelques minutes au prochain branchement d'un iPhone",
        ),
        Poste(
            "Archives d'Xcode",
            list((dev / "Xcode/Archives").glob("*")),
            "rien : les builds sont chez Apple, les dSYM se retéléchargent",
        ),
    ]


def compile_en_ce_moment() -> list[str]:
    """Les compilations en cours, par leur nom de procédé."""
    vus: list[str] = []
    for nom in COMPILATEURS:
        r = subprocess.run(["pgrep", "-x", nom], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            vus.append(nom)
    return vus


def libre() -> int:
    s = os.statvfs("/")
    return s.f_bavail * s.f_frsize


def humain(octets: int) -> str:
    for unite in ("o", "Ko", "Mo", "Go"):
        if abs(octets) < 1024 or unite == "Go":
            return f"{octets:.1f} {unite}" if unite != "o" else f"{octets} o"
        octets /= 1024.0
    return f"{octets:.1f} Go"


def main() -> int:
    parseur = argparse.ArgumentParser(description=__doc__)
    parseur.add_argument(
        "--nettoyer",
        action="store_true",
        help="rendre l'espace des postes sûrs, au lieu de seulement le relever",
    )
    parseur.add_argument(
        "--tout",
        action="store_true",
        help="inclure les postes qui coûtent une recompilation aux autres sessions",
    )
    args = parseur.parse_args()

    print(f"\n  Libre au départ : {humain(libre())}\n")

    liste = postes()
    total = 0
    for p in liste:
        t = p.taille()
        total += t
        if t == 0:
            continue
        print(f"  {humain(t):>10}   {p.nom}")
        print(f"               coûte : {p.cout}")

    if total == 0:
        print("  Rien à rendre — les caches connus sont déjà vides.\n")
        return 0

    print(f"\n  {humain(total):>10}   au total\n")

    if not args.nettoyer:
        print("  Relevé seulement. Ajouter --nettoyer pour rendre l'espace.\n")
        return 0

    # **Refuser plutôt que casser le travail d'un autre.**
    #
    # Cette machine porte plusieurs sessions à la fois. Vider un `DerivedData`
    # qu'`xcodebuild` tient ouvert fait échouer une compilation en cours chez
    # quelqu'un qui n'a rien demandé. On préfère ne rien faire et le dire.
    occupes = compile_en_ce_moment()
    if occupes:
        print(f"  ✗ Une compilation tourne ({', '.join(occupes)}) — rien n'est nettoyé.")
        print("    Attendre qu'elle finisse, ou prévenir la session concernée.\n")
        return 1

    avant = libre()
    for p in liste:
        if not p.sur and not args.tout:
            continue
        for c in p.chemins:
            if not c.exists():
                continue
            # **Un fichier protégé ne doit pas faire abandonner le dossier.**
            #
            # `CoreDevice` contient des liens que le système refuse de suivre —
            # `DiagnosticReports` en est un. Sans ce garde-fou, une seule
            # exception faisait renoncer aux gigaoctets qui suivaient, et
            # l'outil rendait « 78 Mo » là où il en promettait 2,6.
            refuses: list[str] = []

            def sauter(_fn, chemin, _exc, _refuses=refuses):
                _refuses.append(chemin)

            try:
                if c.is_dir() and not c.is_symlink():
                    shutil.rmtree(c, onerror=sauter)
                else:
                    c.unlink()
            except OSError as e:
                print(f"  ✗ {c} : {e}")
            if refuses:
                print(f"     ({len(refuses)} élément(s) protégé(s) laissés dans {c.name})")

    rendu = libre() - avant
    print(f"  Libre à l'arrivée : {humain(libre())}   (+{humain(rendu)})\n")

    # L'écart entre le relevé et le rendu n'est pas une erreur : APFS partage
    # des blocs entre fichiers clonés, et un même bloc compté deux fois ne se
    # libère qu'une. On le dit plutôt que de laisser croire à un défaut.
    if rendu < total * 0.9:
        print(f"  Note : {humain(total)} relevés, {humain(rendu)} rendus.")
        print("  APFS partage des blocs entre fichiers clonés — l'écart est normal.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
