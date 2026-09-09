#!/usr/bin/env python3
"""Récolte l'alignement hébreu → grec de MACULA Hebrew, et en tire le pont.

    ./importer-le-pont-septante.py --macula <clone> --sortie sources/pont-septante

## Ce que c'est, et ce que ce n'est pas

MACULA Hebrew (Biblica, CC BY 4.0) porte le Westminster Leningrad Codex avec,
sur ==chaque morphème hébreu==, le mot grec que la Septante emploie et son
numéro de Strong. C'est le seul alignement mot-à-mot massorétique → Septante
sous licence libre — les autres sont soit inexistants, soit fermés (CATSS).

Ce n'est **pas un témoin** : la Septante n'apparaît pas ici comme un texte à
lire, mais comme ==une correspondance à compter==. Le fichier produit ne va
donc pas au `MANIFEST.json` — décision de l'auteur du 9 septembre 2026 : outil
de travail, invisible au lecteur. Le manifeste est le seul interrupteur ; tant
que la clé n'y est pas, le pipeline n'émet rien.

## Pourquoi le pont se bâtit sur les numéros, jamais sur les formes

La colonne des formes grecques porte ==une confusion systématique χ / ξ / κ== :
`ἀρξῇ` pour ἀρχῇ, `βραξίων` pour βραχίων, `ἐχ` pour ἐκ. La colonne des numéros
de Strong, elle, est saine — `746` est bien ἀρχή.

On compte donc sur `greekstrong`, et les formes ne servent qu'à ==illustrer==.
Un pont bâti sur les chaînes hériterait du défaut sans le voir.

## Ce que l'alignement ne peut pas faire

- **Un seul sens.** Il n'y a aucun identifiant de mot grec : on va de l'hébreu
  vers le grec, jamais l'inverse. Les *plus* de la Septante — ce qu'elle ajoute
  et que l'hébreu n'a pas — sont ==invisibles ici==.
- **L'araméen est dégradé.** L'appariement de Daniel 7 est manifestement faux
  (`chelem`, le songe, apparié à κεφαλή, la tête). Les sections araméennes sont
  relevées à part et ==ne comptent pas dans le pont==.
- **L'édition grecque n'est pas nommée.** Ni le dépôt ni sa licence ne disent
  si le grec vient de Rahlfs ou de Göttingen. On ne le devine pas : le pont
  n'énonce que des ==numéros de Strong==, qui sont de 1890 et libres de droits.

## Attribution — elle voyage avec la donnée

    MACULA Hebrew Linguistic Datasets, available at
    https://github.com/Clear-Bible/macula-hebrew/
    © 2022-2024 Biblica, Inc — CC BY 4.0

Les colonnes SDBH (`sdbh`, `lexdomain`, `coredomain`) du même dépôt sont
« used with permission » et ==non couvertes par le CC BY==. On ne les lit pas.
"""
import argparse, json, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

# MACULA nomme ses livres en trois lettres majuscules ; le vault emploie déjà
# les noms d'Open Scriptures pour `sources/he-wlc/`. On s'aligne sur le vault :
# une clé de jointure qui diverge entre deux dossiers du même dépôt est une
# jointure qu'on écrira un jour à l'envers.
LIVRES = {
    "GEN": "Gen", "EXO": "Exod", "LEV": "Lev", "NUM": "Num", "DEU": "Deut",
    "JOS": "Josh", "JDG": "Judg", "RUT": "Ruth", "1SA": "1Sam", "2SA": "2Sam",
    "1KI": "1Kgs", "2KI": "2Kgs", "1CH": "1Chr", "2CH": "2Chr", "EZR": "Ezra",
    "NEH": "Neh", "EST": "Esth", "JOB": "Job", "PSA": "Ps", "PRO": "Prov",
    "ECC": "Eccl", "SNG": "Song", "ISA": "Isa", "JER": "Jer", "LAM": "Lam",
    "EZK": "Ezek", "DAN": "Dan", "HOS": "Hos", "JOL": "Joel", "AMO": "Amos",
    "OBA": "Obad", "JON": "Jonah", "MIC": "Mic", "NAM": "Nah", "HAB": "Hab",
    "ZEP": "Zeph", "HAG": "Hag", "ZEC": "Zech", "MAL": "Mal",
}

# Les passages araméens du corpus. Leur alignement est dégradé (voir l'en-tête)
# et ils sont relevés à part plutôt que comptés de travers.
ARAMEEN = [("Dan", 2, 4, 7, 28), ("Ezra", 4, 8, 6, 18), ("Ezra", 7, 12, 7, 26)]

MOT = re.compile(r"<w\b([^>]*)>([^<]*)</w>")
ATTR = re.compile(r'(\w+)="([^"]*)"')
REF = re.compile(r"^([A-Z1-9]{3})\s+(\d+):(\d+)")


def est_arameen(livre, c, v):
    """Vrai si ce verset tombe dans une section araméenne."""
    for l, c1, v1, c2, v2 in ARAMEEN:
        if l == livre and (c, v) >= (c1, v1) and (c, v) <= (c2, v2):
            return True
    return False


def lire_chapitre(chemin):
    """Rend les mots d'un fichier lowfat, chacun avec ses attributs utiles.

    On lit par expression rationnelle et non par analyseur XML : les fichiers
    lowfat sont profondément imbriqués (un `<w>` par morphème, sous plusieurs
    niveaux de `<wg>`), et seule la feuille nous intéresse. Un analyseur
    marcherait aussi ; il coûterait la mémoire de l'arbre pour rien.
    """
    texte = chemin.read_text(encoding="utf-8")
    for m in MOT.finditer(texte):
        a = dict(ATTR.findall(m.group(1)))
        r = REF.match(a.get("ref", ""))
        if not r:
            continue
        yield r.group(1), int(r.group(2)), int(r.group(3)), m.group(2), a


def importer(macula: Path, sortie: Path):
    lowfat = macula / "WLC" / "lowfat"
    fichiers = sorted(lowfat.glob("*.xml"))
    if not fichiers:
        sys.exit(f"échec : aucun fichier lowfat sous {lowfat}")

    par_livre = defaultdict(lambda: defaultdict(list))
    stats = defaultdict(lambda: [0, 0])           # livre -> [morphèmes, alignés]
    inconnus, arameens = Counter(), 0

    for f in fichiers:
        for code, c, v, texte, a in lire_chapitre(f):
            livre = LIVRES.get(code)
            if livre is None:
                inconnus[code] += 1
                continue
            if est_arameen(livre, c, v):
                arameens += 1
                continue
            stats[livre][0] += 1
            gs = a.get("greekstrong", "").strip()
            hs = a.get("strongnumberx", "").strip()
            if not gs or not hs:
                continue
            stats[livre][1] += 1
            par_livre[livre][(c, v)].append({
                "he": hs,
                "gr": gs,
                "hf": texte,
                "gf": a.get("greek", ""),
                "lem": a.get("lemma", ""),
            })

    if not par_livre:
        sys.exit("échec : zéro appariement extrait — le format a changé")

    sortie.mkdir(parents=True, exist_ok=True)
    for livre, versets in sorted(par_livre.items()):
        lignes = []
        for (c, v), paires in sorted(versets.items()):
            lignes.append(json.dumps(
                {"ref": f"{livre}.{c}.{v}", "c": c, "v": v, "p": paires},
                ensure_ascii=False))
        (sortie / f"{livre}.jsonl").write_text("\n".join(lignes) + "\n",
                                               encoding="utf-8")

    # **Le contrôle qui vaut le plus.** Un livre qui rend zéro appariement n'est
    # pas « un livre pauvre » : c'est un format qu'on a cessé de comprendre. Le
    # dire, plutôt que d'écrire un fichier vide que personne ne relira.
    vides = [l for l in LIVRES.values() if l not in par_livre]
    if vides:
        sys.exit(f"échec : aucun appariement pour {', '.join(vides)}")

    tot_m = sum(s[0] for s in stats.values())
    tot_a = sum(s[1] for s in stats.values())
    print(f"{len(par_livre)} livres · {sum(len(v) for v in par_livre.values())} versets")
    print(f"{tot_m} morphèmes · {tot_a} alignés ({100*tot_a/tot_m:.1f} %)")
    print(f"{arameens} morphèmes araméens écartés — alignement dégradé, voir l'en-tête")
    if inconnus:
        print(f"codes de livre inconnus : {dict(inconnus)}")

    faibles = sorted((s[1] / s[0], l) for l, s in stats.items() if s[0])[:5]
    print("couverture la plus basse : " +
          " · ".join(f"{l} {100*p:.0f} %" for p, l in faibles))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--macula", type=Path, required=True)
    ap.add_argument("--sortie", type=Path, required=True)
    a = ap.parse_args()
    importer(a.macula, a.sortie)
