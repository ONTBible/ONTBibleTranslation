#!/usr/bin/env python3
"""Relever une forme dans le vault — **jamais un compte sans ses appariements**.

## Pourquoi cet outil existe

Le 8 septembre 2026, deux chantiers ont été annoncés à l'auteur et n'existaient
pas. Les « vingt-deux marqueurs déséquilibrés » du §13.2 en comptaient deux.
L'article `ha-` prétendument avalé sur cinquante occurrences en comptait zéro :
le corpus écrit *les [[Chivi]] (\\*Chivi\\* / הַחִוִּי)*, et le français y porte
déjà l'article.

Les deux ont le **même profil**, et c'est lui qu'il faut empêcher :

    un compte produit par un motif, sans qu'une seule ligne ait été lue,
    puis rendu dans un format propre qui lui donne l'apparence du fait.

Le skill `concerter-les-sessions` porte déjà la parade — *la parade n'est pas un
meilleur motif, c'est de regarder les appariements*. Elle n'a pas suffi, parce
qu'une règle n'oblige à rien et qu'un compte se produit plus vite qu'une
lecture.

## Ce que l'outil garantit

**Il ne peut pas rendre un compte nu.** Chaque forme relevée sort avec au moins
une ligne de son contexte réel. Si le contexte dément le motif, ça se voit
avant que le chiffre ne soit transmis — et non après.

    python3 scripts/relever.py 'kh[a-z]+'            # motif
    python3 scripts/relever.py --formes Terah Nahor  # formes exactes
    python3 scripts/relever.py 'ha-' --lignes 3      # plus de contexte

`sessions/` est toujours exclu : ce sont les transcriptions de l'auteur, où sa
propre frappe est archivée.
"""

import argparse
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
EXCLUS = ("sessions/",)
LARGEUR = 150


def fichiers():
    for p in sorted(RACINE.rglob("*.md")):
        rel = p.relative_to(RACINE).as_posix()
        if rel.startswith(EXCLUS) or "/.git/" in rel:
            continue
        yield rel, p


def relever(motif, par_forme):
    """Rend {forme: [(fichier, numéro, ligne)]} — le contexte, jamais le seul compte."""
    trouve = {}
    for rel, p in fichiers():
        try:
            lignes = p.read_text(encoding="utf-8").split("\n")
        except UnicodeDecodeError:
            continue
        for n, ligne in enumerate(lignes, 1):
            for m in motif.finditer(ligne):
                forme = m.group(0) if par_forme else motif.pattern
                trouve.setdefault(forme, []).append((rel, n, ligne.strip()))
    return trouve


def main():
    a = argparse.ArgumentParser(
        description="Relever une forme — jamais un compte sans ses appariements."
    )
    a.add_argument("motif", nargs="?", help="expression régulière")
    a.add_argument("--formes", nargs="+", help="formes exactes, en mots entiers")
    a.add_argument("--lignes", type=int, default=1,
                   help="lignes de contexte par forme (défaut 1)")
    o = a.parse_args()

    if o.formes:
        motif = re.compile(r"\b(?:" + "|".join(re.escape(f) for f in o.formes) + r")\b")
    elif o.motif:
        motif = re.compile(o.motif)
    else:
        a.error("donner un motif ou --formes")

    trouve = relever(motif, par_forme=True)
    if not trouve:
        print("  aucune occurrence.")
        print("\n  ⚠ Un zéro n'est pas un fait tant que l'instrument n'a pas été")
        print("    éprouvé sur un cas dont on connaît la réponse. Relance sur une")
        print("    forme certainement présente avant de rapporter cette absence.")
        return 0

    total = sum(len(v) for v in trouve.values())
    print(f"  {total} occurrences · {len(trouve)} formes distinctes")
    print(f"  {len(set(f for v in trouve.values() for f, _, _ in v))} fichiers\n")

    def corpus_d_abord(t):
        """Le contexte utile est dans le corpus, pas dans ce qui en parle.

        Sans ce tri, l'outil montre volontiers la ligne du `CLAUDE.md` qui
        *décrit* le chantier — et l'on croit avoir lu une occurrence quand on
        a lu sa propre note. Constaté à la première exécution.
        """
        rel = t[0]
        meta = rel in ("CLAUDE.md", "SYNCHRONISATION.md", "DECISIONS.md")
        return (rel.startswith("scripts/"), meta, rel)

    for forme, occ in sorted(trouve.items(), key=lambda kv: -len(kv[1])):
        occ = sorted(occ, key=corpus_d_abord)
        print(f"  ── {forme} · {len(occ)} ──")
        vus = set()
        montres = 0
        for rel, n, ligne in occ:
            if rel in vus and montres >= o.lignes:
                continue
            vus.add(rel)
            print(f"     {rel}:{n}")
            print(f"       {ligne[:LARGEUR]}")
            montres += 1
            if montres >= o.lignes:
                break
        if len(occ) > montres:
            print(f"     … {len(occ) - montres} autres occurrences")
        print()

    print("  ── avant de rapporter ce relevé ──")
    print("     Chaque forme ci-dessus a montré au moins une ligne réelle.")
    print("     Les as-tu lues ? Un compte dont le contexte n'a pas été lu")
    print("     n'est pas un chantier — c'est une hypothèse bien formatée.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
