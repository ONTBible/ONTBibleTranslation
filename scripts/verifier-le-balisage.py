#!/usr/bin/env python3
"""Contrôle le balisage du corpus, PARAGRAPHE PAR PARAGRAPHE.

Pourquoi par paragraphe. C'est l'unité réelle du balisage, et le §13.2 l'a
établi en ramenant « vingt-deux marqueurs déséquilibrés » à deux : un `**...**`
enjambe légitimement un retour à la ligne, jamais un blanc de paragraphe.

Pourquoi les gloses. Le 8 septembre 2026, huit gloses de *Bereshit* 1 ont été
coupées par un blanc que leur auteur y avait mis pour aérer un texte devenu
long. Le pipeline analysant par paragraphe, la glose cessait d'en être une et
le lecteur aurait vu `*[` et `]*` bruts. Aucun contrôle ne le voyait : ils
comptaient les gras et les accentuations, jamais les marqueurs de glose.

    Le contrôle était vert sur ce qu'il mesurait, et muet sur le reste.

C'est la raison d'être de ce fichier : ce qui n'est mesuré nulle part finit
par diverger sans que rien ne le signale.
"""
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
ZONES = ("locked", "brouillons", "lexique")

# Un lien de Shem voisine les mêmes caractères qu'une glose, et il produit des
# faux positifs dans les deux sens — mesurés le 8 septembre 2026 :
#
#     *[[Enosh]]        une italique ouvrant sur un lien   →  fausse ouverture
#     [[Avraham]]*      un lien fermant une italique       →  fausse fermeture
#     *[[[Amrafel]] …]* une glose ouvrant SUR un lien      →  vraie ouverture
#
# Aucun délimiteur ne les sépare : il faut BALAYER, en sautant chaque lien
# comme un bloc atomique. Deux tentatives par motif ont donné 101 puis 90 faux
# positifs là où le comptage naïf en donnait 15 — un instrument plus fin n'est
# pas un instrument plus juste.


def marqueurs_ouverts(par):
    """compte les gloses restées ouvertes, en sautant les liens [[…]]"""
    ouvert, i = 0, 0
    while i < len(par):
        if par.startswith("[[", i):
            f = par.find("]]", i)
            i = len(par) if f < 0 else f + 2
            continue
        if par.startswith("*[[[", i):      # une glose qui s'ouvre SUR un lien
            ouvert += 1; i += 2; continue
        if par.startswith("*[[", i):       # une italique suivie d'un lien : pas une glose
            i += 1; continue
        if par.startswith("*[", i):
            ouvert += 1; i += 2; continue
        if par.startswith("]*", i):
            ouvert -= 1; i += 2; continue
        i += 1
    return ouvert


def deséquilibres(texte):
    """rend les paragraphes dont un marqueur reste ouvert"""
    trouvés = []
    for n, par in enumerate(texte.split("\n\n"), 1):
        motifs = {
            "glose": marqueurs_ouverts(par),
            "gras": par.count("**") % 2,
            "accentuation": par.count("==") % 2,
        }
        ouverts = [k for k, v in motifs.items() if v]
        if ouverts:
            trouvés.append((n, ouverts, par[:70].replace("\n", " ")))
    return trouvés


def main():
    cibles = [Path(a) for a in sys.argv[1:]] or [
        p for z in ZONES for p in (RACINE / z).rglob("*.md")
    ]
    total = 0
    for p in sorted(cibles):
        for n, ouverts, extrait in deséquilibres(p.read_text(encoding="utf-8")):
            print(f"  ✗ {p.stem} ¶{n} — {', '.join(ouverts)} : {extrait}…")
            total += 1
    if total:
        print(f"\n{total} paragraphe(s) déséquilibré(s)")
        return 1
    print(f"{len(cibles)} fichiers — tout est refermé")
    return 0


if __name__ == "__main__":
    sys.exit(main())
