#!/usr/bin/env python3
"""Dénombre, pour chaque mot hébreu, les mots grecs que la Septante lui oppose.

    ./etablir-le-pont-septante.py --strong <strongsgreek.xml> --sortie <rapport.md>

## Ce que ce pont est, et il faut le dire avant de s'en servir

La donnée vient de MACULA Hebrew, et **ses auteurs la déclarent eux-mêmes
provisoire** — la documentation du dépôt écrit : *« a tentative alignment to
the Septuagint […] This data has never been manually checked and is released
as a starting point for further work. »*

Ce n'est donc **pas un appariement éditorial**. Pris mot à mot, il se trompe :
en *Daniel* 7 il apparie *chelem*, le songe, à κεφαλή, la tête.

**Et c'est exactement pourquoi on compte au lieu de lire.** Une erreur isolée
est du bruit dans un dénombrement, quand elle est décisive dans une lecture.
Quand 2 146 occurrences d'*asah* sur 2 269 tombent sur ποιέω, aucune poignée
d'appariements faux ne fabrique ce chiffre. ==Le pont est faible au mot, fort
à l'agrégat== — et l'ONT ne lui demande que l'agrégat.

Un pont qui affirmerait « ce mot grec rend ce mot hébreu » outrepasserait sa
donnée. Celui-ci dit : ==« sur N occurrences alignées, voici la distribution »==,
et laisse l'auteur trancher.

## Pourquoi les numéros et jamais les formes

La colonne des formes grecques porte une ==interversion χ / ξ== : `ἀρξῇ` pour
ἀρχῇ, `ξόρτου` pour χόρτου, `ψυξὴν` pour ψυχήν.

**Elle est réparable en apparence, et on ne la répare pas.** Mesuré sur les
1 474 formes distinctes concernées : l'inversion en répare ==1 048==, mais
==55 étaient déjà justes== — `ἔβρεχεν`, `ἕχει`, `ἐλέγχει`. Un échange en masse
casserait celles-là, et rien ne le dirait.

Les numéros de Strong, eux, sont sains : `746` est bien ἀρχή. On compte donc
sur eux, et les formes ne servent qu'à ==illustrer==, avec leur défaut annoncé.

## Le dictionnaire grec

Strong 1890, domaine public, par la transcription de MorphGNT. Il ne sert qu'à
rendre un numéro lisible — aucune définition n'en est reprise.
"""
import argparse, glob, json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

PONT = "sources/pont-septante"


def lemmes_grecs(chemin: Path):
    """Numéro de Strong grec -> lemme unicode."""
    x = chemin.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'<entry strongs="(\d+)">(.*?)</entry>', x, re.S):
        u = re.search(r'<greek[^>]*unicode="([^"]*)"', m.group(2))
        if u:
            out[str(int(m.group(1)))] = u.group(1)
    if not out:
        sys.exit(f"échec : aucun lemme lu dans {chemin} — le format a changé")
    return out


def nu(s: str) -> str:
    """Sans points-voyelles ni accents — pour comparer deux graphies."""
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if not unicodedata.combining(c))


def batir():
    """(Strong hébreu, Strong grec) -> compte, plus les index de lecture."""
    pont = Counter()
    lem_he = defaultdict(Counter)
    par_he = Counter()
    refs = defaultdict(list)
    fichiers = sorted(glob.glob(f"{PONT}/*.jsonl"))
    if not fichiers:
        sys.exit(f"échec : rien sous {PONT} — lancer d'abord l'importateur")
    for f in fichiers:
        for ligne in open(f, encoding="utf-8"):
            d = json.loads(ligne)
            for p in d["p"]:
                chiffres = re.sub(r"\D", "", p["he"])
                if not chiffres:
                    continue
                he = str(int(chiffres))
                # Un morphème peut porter plusieurs mots grecs — huit cas dans
                # tout le corpus. On les compte tous plutôt que d'en choisir un.
                grecs = [g for g in re.split(r"[|,;]", p["gr"]) if g.strip().isdigit()]
                for g in grecs:
                    gr = str(int(g))
                    pont[(he, gr)] += 1
                    par_he[he] += 1
                    if len(refs[(he, gr)]) < 3:
                        refs[(he, gr)].append(d["ref"])
                if p["lem"]:
                    lem_he[he][p["lem"]] += 1
    return pont, lem_he, par_he, refs


def termes_de_l_ont(claude: Path):
    """Les mots hébreux que le §3 déclare, avec leur rendu ONT.

    On lit les tables du §3 : `| hébreu | *translit* | rendu | … |`. Le §2.5
    ne donne pas l'hébreu de tous ses termes, le §3 si — c'est lui la source.
    """
    if not claude.is_file():
        return []
    out = []
    for ligne in claude.read_text(encoding="utf-8").splitlines():
        cases = [c.strip() for c in ligne.split("|")]
        if len(cases) < 5:
            continue
        heb, translit, rendu = cases[1], cases[2], cases[3]
        # La première case doit être de l'hébreu, et rien d'autre.
        if not heb or not all("֐" <= c <= "׿" or c.isspace() for c in heb):
            continue
        out.append((nu(heb).strip(), translit.strip("* "), rendu))
    return out


def rendre(sortie: Path, strong: Path, claude: Path):
    grec = lemmes_grecs(strong)
    pont, lem_he, par_he, refs = batir()

    # Hébreu sans points -> numéro de Strong le plus fréquent sous cette graphie.
    par_graphie = defaultdict(Counter)
    for he, formes in lem_he.items():
        for forme, n in formes.items():
            par_graphie[nu(forme).strip()][he] += n

    l = ["# Le pont Septante — ce que le grec oppose à chaque mot hébreu", "",
         "Dénombré sur l'alignement de MACULA Hebrew (Biblica, CC BY 4.0).",
         "",
         "> **Ce pont compte, il n'atteste pas.** Ses auteurs déclarent",
         "> l'alignement *« tentative […] never been manually checked »*. Pris mot",
         "> à mot il se trompe ; pris en masse il informe. Les pourcentages",
         "> ci-dessous portent sur les occurrences **alignées**, non sur toutes",
         "> les occurrences du mot — la couverture est de 69 % en moyenne.",
         "",
         f"{sum(pont.values())} appariements · {len(pont)} paires distinctes · "
         f"{len(par_he)} mots hébreux", ""]

    termes = termes_de_l_ont(claude)
    if termes:
        l += ["## Les termes que le §3 déclare", "",
              "| terme | rendu ONT | alignés | le grec, par fréquence |",
              "|---|---|---:|---|"]
        vus = set()
        for graphie, translit, rendu in termes:
            cands = par_graphie.get(graphie)
            if not cands:
                continue
            he = cands.most_common(1)[0][0]
            if he in vus:
                continue
            vus.add(he)
            tot = par_he[he]
            sous = sorted(((k, v) for k, v in pont.items() if k[0] == he),
                          key=lambda x: -x[1])[:3]
            part = " · ".join(f"**{grec.get(g, g)}** {100*n/tot:.0f} %"
                              for (_, g), n in sous)
            l.append(f"| *{translit}* | {rendu} | {tot} | {part} |")
        l.append("")

    l += ["## Les cent mots hébreux les plus alignés", "",
          "| hébreu | alignés | le grec, par fréquence | exemple |", "|---|---:|---|---|"]
    for he, tot in par_he.most_common(100):
        forme = lem_he[he].most_common(1)[0][0] if lem_he[he] else "?"
        sous = sorted(((k, v) for k, v in pont.items() if k[0] == he),
                      key=lambda x: -x[1])[:3]
        part = " · ".join(f"**{grec.get(g, g)}** {100*n/tot:.0f} %"
                          for (_, g), n in sous)
        ex = refs[sous[0][0]][0] if sous else ""
        l.append(f"| {forme} | {tot} | {part} | {ex} |")

    sortie.write_text("\n".join(l) + "\n", encoding="utf-8")
    print(f"{sortie} — {len(l)} lignes")
    print(f"{sum(pont.values())} appariements · {len(pont)} paires · {len(par_he)} mots hébreux")
    if termes:
        print(f"{len(termes)} termes lus au §3, {len(vus)} retrouvés dans le pont")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--strong", type=Path, required=True)
    ap.add_argument("--sortie", type=Path, required=True)
    ap.add_argument("--claude", type=Path, default=Path("CLAUDE.md"))
    a = ap.parse_args()
    rendre(a.sortie, a.strong, a.claude)
