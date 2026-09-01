#!/usr/bin/env python3
"""Importe les textes en langue source et leurs analyses morphologiques.

    ./scripts/importer-les-textes-sources.py --depots <dossier>   convertit
    ./scripts/importer-les-textes-sources.py --depots <dossier> --cloner

Écrit `sources/` : un fichier JSONL par livre-source, plus `MANIFEST.json`.
Rend **1** dès qu'un livre attendu manque ou qu'un fichier se lit mal.

## Pourquoi ce dossier existe

Un appui long sur un verset doit rendre le texte **dans sa langue source**.
Trois témoins le portent, et aucun n'est de l'ONT : ce sont des éditions
critiques extérieures, reprises telles quelles.

## Ce que le format ne décide pas — délibérément

`dist/` n'est pas arrêté : `schema.rs` est encore en discussion entre la
session app et la session vault. Ce dossier-ci est donc **neutre** — il ne
connaît ni les **parashiot** ni la numérotation interne des unités ONT (§2.2).
Il est classé **par référence biblique**, qui est la clé native des trois
sources, et c'est au pipeline de faire la jointure unité → référence.

C'est le bon joint : la correspondance « unité ONT ↔ versets bibliques » vit
déjà dans le sous-titre de chaque unité, et elle changera encore. Les données
sources, elles, ne changeront jamais.

## Les licences voyagent par source, jamais par livre

Chaque dossier de `sources/` porte **une** source et **une** licence, et
`MANIFEST.json` les déclare avec le commit amont exact. Ranger l'attribution
dans un écran « à propos » séparé du contenu la désynchroniserait.

## MorphGNT est en CC BY-SA — ses étiquettes vivent à part

C'est la seule contrainte qui ne se rattrape pas après coup. Tout ce que
MorphGNT apporte (catégorie, analyse, forme normalisée, lemme) est enfermé
dans le champ `mgnt`, et **rien** de la couche fonctionnelle de l'ONT ne doit
y entrer : le copyleft mordrait alors sur le travail de l'auteur. Le mot grec
lui-même reste dehors, dans `t` — il vient du SBLGNT, qui est en CC BY.

Le même cloisonnement est appliqué à l'hébreu (`oshb`) alors que CC BY ne
l'exige pas : une seule règle vaut mieux que deux, et OSHB pourrait changer
de licence un jour.
"""

import argparse
import json
import re
import subprocess
import unicodedata
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# Le namespace OSIS se lit sur la racine, jamais en dur : morphhb emploie
# `bibletechnologies.net` quand la documentation OSIS écrit `.com`, et une
# constante fausse ne lève rien — elle rend zéro verset en silence.
def _ns(racine) -> str:
    return racine.tag[:racine.tag.index("}") + 1] if "}" in racine.tag else ""

DEPOTS = {
    "he-wlc": ("https://github.com/openscriptures/morphhb.git", "morphhb"),
    "grc-sblgnt": ("https://github.com/morphgnt/sblgnt.git", "sblgnt"),
    "grc-byz": ("https://github.com/byztxt/byzantine-majority-text.git",
                "byzantine-majority-text"),
}

SOURCES = {
    "he-wlc": {
        "nom": "Westminster Leningrad Codex + Open Scriptures Hebrew Bible",
        "langue": "he",
        "texte": {"oeuvre": "Westminster Leningrad Codex",
                  "licence": "domaine public"},
        "analyse": {"champ": "oshb", "oeuvre": "Open Scriptures Hebrew Bible",
                    "licence": "CC BY 4.0",
                    "url": "https://creativecommons.org/licenses/by/4.0/",
                    "copyleft": False},
        "attribution": "Texte : Westminster Leningrad Codex (domaine public). "
                       "Lemmes et morphologie : Open Scriptures Hebrew Bible, "
                       "CC BY 4.0.",
    },
    "grc-sblgnt": {
        "nom": "SBL Greek New Testament + MorphGNT",
        "langue": "grc",
        "texte": {"oeuvre": "SBL Greek New Testament", "licence": "CC BY 4.0",
                  "url": "https://creativecommons.org/licenses/by/4.0/",
                  "reserve": "ne peut pas être vendu seul"},
        "analyse": {"champ": "mgnt", "oeuvre": "MorphGNT",
                    "licence": "CC BY-SA 3.0",
                    "url": "https://creativecommons.org/licenses/by-sa/3.0/",
                    "copyleft": True},
        "attribution": "Texte : SBL Greek New Testament, © Society of Biblical "
                       "Literature et Logos Bible Software, CC BY 4.0. "
                       "Analyse morphologique : MorphGNT, CC BY-SA 3.0.",
    },
    "grc-byz": {
        "nom": "The New Testament in the Original Greek: Byzantine Textform "
               "(Robinson-Pierpont)",
        "langue": "grc",
        "texte": {"oeuvre": "Robinson-Pierpont Byzantine Textform, RP2018",
                  "licence": "domaine public"},
        "analyse": {"champ": None, "oeuvre": "Robinson-Pierpont (analyse et Strong)",
                    "licence": "domaine public", "copyleft": False},
        "attribution": "Robinson-Pierpont Byzantine Textform (RP2018), domaine public.",
    },
}

# Correspondance livre-source → numérotation ONT (`corpus-order.md`).
# L'ONT réunit ce que les éditions séparent — Shemuel, Melakhim,
# Ezra-Nehemyah, Divrei Hayamim — d'où plusieurs livres-sources sur un numéro.
ONT_HE = {
    "Gen": (1, "bereshit"), "Exod": (2, "shemot"), "Lev": (3, "vayiqra"),
    "Num": (4, "bemidbar"), "Deut": (5, "devarim"),
    "Josh": (7, "yehoshua"), "Judg": (8, "shoftim"),
    "1Sam": (9, "shemuel"), "2Sam": (9, "shemuel"),
    "1Kgs": (10, "melakhim"), "2Kgs": (10, "melakhim"),
    "Jer": (11, "yirmeyahu"), "Lam": (12, "ekha"), "Ezek": (13, "yehezqel"),
    "Isa": (14, "yeshayahu"),
    "Hos": (15, "hoshea"), "Joel": (16, "yoel"), "Amos": (17, "amos"),
    "Obad": (18, "ovadyah"), "Jonah": (19, "yonah"), "Mic": (20, "mikhah"),
    "Nah": (21, "nahum"), "Hab": (22, "havaquq"), "Zeph": (23, "tsefanyah"),
    "Hag": (24, "haggai"), "Zech": (25, "zekharyah"), "Mal": (26, "malakhi"),
    "Ps": (27, "tehilim"), "Prov": (28, "mishlei"), "Job": (29, "iyov"),
    "Song": (30, "shir-hashirim"), "Ruth": (31, "ruth"),
    "Eccl": (32, "qohelet"), "Esth": (33, "esther"),
    "Ezra": (34, "ezra-nehemyah"), "Neh": (34, "ezra-nehemyah"),
    "1Chr": (35, "divrei-hayamim"), "2Chr": (35, "divrei-hayamim"),
    "Dan": (41, "daniel"),
}

ONT_GRC = {
    "Mk": (44, "marqus"), "Mt": (45, "matityahu"), "Lk": (46, "luqas"),
    "Jn": (47, "bereshit-ha-yohanan"), "Ac": (48, "gevurot-ha-neviim"),
    "Ro": (49, "el-ha-romiyim"), "1Co": (50, "el-ha-qorintiyim-alef"),
    "2Co": (51, "el-ha-qorintiyim-bet"), "Ga": (52, "el-ha-galatiyim"),
    "Eph": (53, "el-ha-efesiyim"), "Php": (54, "el-ha-filipiyim"),
    "Col": (55, "el-ha-qolossiyim"), "1Th": (56, "el-ha-tessaloniqiyim-alef"),
    "2Th": (57, "el-ha-tessaloniqiyim-bet"), "Phm": (58, "el-filemon"),
    "Jas": (59, "igeret-yaaqov"), "1Pe": (60, "igeret-kefa-alef"),
    "Heb": (61, "igeret-ha-ivrim"), "1Ti": (62, "el-timotiyos-alef"),
    "2Ti": (63, "el-timotiyos-bet"), "Tit": (64, "el-titos"),
    "1Jn": (65, "igeret-yohanan-alef"), "2Jn": (66, "igeret-yohanan-bet"),
    "3Jn": (67, "igeret-yohanan-gimel"), "2Pe": (68, "igeret-kefa-bet"),
    "Jud": (69, "igeret-yehudah"), "Re": (70, "machazeh-yohanan"),
}

# Les fichiers byzantins sont nommés autrement ; on les ramène sur la même clé.
BYZ_VERS_SBL = {
    "MAT": "Mt", "MAR": "Mk", "LUK": "Lk", "JOH": "Jn", "ACT": "Ac",
    "ROM": "Ro", "1CO": "1Co", "2CO": "2Co", "GAL": "Ga", "EPH": "Eph",
    "PHP": "Php", "COL": "Col", "1TH": "1Th", "2TH": "2Th", "1TI": "1Ti",
    "2TI": "2Ti", "TIT": "Tit", "PHM": "Phm", "HEB": "Heb", "JAM": "Jas",
    "1PE": "1Pe", "2PE": "2Pe", "1JO": "1Jn", "2JO": "2Jn", "3JO": "3Jn",
    "JUD": "Jud", "REV": "Re",
}


def commit_amont(dossier: Path) -> str:
    """Le SHA du clone, pour que l'import soit rejouable à l'identique."""
    try:
        return subprocess.run(["git", "-C", str(dossier), "rev-parse", "HEAD"],
                              capture_output=True, text=True, check=True
                              ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "inconnu"


# --------------------------------------------------------------------------
# Hébreu — OSIS XML de morphhb
# --------------------------------------------------------------------------

def lire_hebreu(chemin: Path):
    """Rend [(chapitre, verset, [mots])] pour un livre OSIS.

    Le `/` des `<w>` sépare les morphèmes : c'est une **analyse** d'OSHB, pas
    le texte de L. On le retire de `t` et on garde la forme découpée dans
    `oshb.seg`, afin que le champ public-domain et le champ CC BY ne se
    mélangent pas.
    """
    racine = ET.parse(chemin).getroot()
    OSIS = _ns(racine)
    versets = []
    for v in racine.iter(f"{OSIS}verse"):
        osis_id = v.get("osisID")
        if not osis_id:
            continue
        parties = osis_id.split(".")
        if len(parties) != 3:
            continue
        _, ch, vs = parties
        mots = []
        for enfant in v:
            balise = enfant.tag.replace(OSIS, "")
            if balise == "w":
                brut = (enfant.text or "").strip()
                if not brut:
                    continue
                mot = {"t": brut.replace("/", "")}
                oshb = {}
                if "/" in brut:
                    oshb["seg"] = brut
                for cle, attr in (("lem", "lemma"), ("morph", "morph"), ("id", "id")):
                    if enfant.get(attr):
                        oshb[cle] = enfant.get(attr)
                if oshb:
                    mot["oshb"] = oshb
                mots.append(mot)
            elif balise == "note" and enfant.get("type") == "variant":
                # Ketiv/Qere : le <w> porte le ketiv, la note donne le qere.
                qere = [(w.text or "").replace("/", "").strip()
                        for w in enfant.iter(f"{OSIS}w")]
                qere = [q for q in qere if q]
                if qere and mots:
                    mots[-1].setdefault("oshb", {})["qere"] = " ".join(qere)
        if mots:
            versets.append((int(ch), int(vs), mots))
    return versets


# --------------------------------------------------------------------------
# Grec éclectique — MorphGNT
# --------------------------------------------------------------------------

def lire_sblgnt(chemin: Path):
    """Sept colonnes : BBCCVV, catégorie, analyse, texte, mot, normalisé, lemme.

    Seule la colonne « texte » sort du champ `mgnt` : c'est le SBLGNT. Tout le
    reste est l'apport de MorphGNT, donc CC BY-SA, donc cloisonné.
    """
    par_verset = {}
    ordre = []
    for ligne in chemin.read_text(encoding="utf-8").splitlines():
        if not ligne.strip():
            continue
        col = ligne.split()
        if len(col) < 7:
            raise ValueError(f"{chemin.name} : ligne à {len(col)} colonnes — {ligne[:60]!r}")
        bcv, pos, parse, texte, mot_nu, normalise, lemme = col[:7]
        ch, vs = int(bcv[2:4]), int(bcv[4:6])
        cle = (ch, vs)
        if cle not in par_verset:
            par_verset[cle] = []
            ordre.append(cle)
        par_verset[cle].append({
            "t": texte,
            "mgnt": {"pos": pos, "parse": parse, "mot": mot_nu,
                     "norm": normalise, "lem": lemme},
        })
    return [(ch, vs, par_verset[(ch, vs)]) for ch, vs in ordre]


# --------------------------------------------------------------------------
# Grec byzantin — Robinson-Pierpont
# --------------------------------------------------------------------------

MOT_BYZ = re.compile(r"(\S+)\s+(\d+)\s+\{([^}]*)\}")


def _depouiller(mot: str) -> str:
    """Ramène un mot grec à ses lettres nues, pour comparer les deux éditions."""
    decompose = unicodedata.normalize("NFD", mot)
    sans_signes = "".join(c for c in decompose if not unicodedata.combining(c))
    return re.sub(r"[^\w]", "", sans_signes, flags=re.UNICODE).lower()


def _lire_csv_byz(chemin: Path):
    import csv
    with chemin.open(encoding="utf-8-sig", newline="") as f:
        return {(int(r["chapter"]), int(r["verse"])): r["text"]
                for r in csv.DictReader(f) if r.get("text")}


def lire_byzantin(accentue: Path, analyse: Path, livre: str):
    """Deux éditions du **même** texte, recousues mot à mot.

    Robinson-Pierpont est publié en deux jeux disjoints, et aucun ne suffit :
    `ccat/no-variants` porte les accents, les esprits et la ponctuation mais
    aucune analyse ; `strongs/with-parsing` porte le Strong et l'analyse mais
    un texte **tout en minuscules et sans accents**.

    Prendre le second seul aurait donné un byzantin nu affiché à côté d'un
    SBLGNT accentué — deux témoins qu'on présente côte à côte et qui n'auraient
    pas eu la même mise. On coud donc les deux.

    La couture est sûre parce qu'elle est **vérifiée**, pas supposée : les deux
    jeux sont la même édition dans le même ordre, et la fonction s'arrête net
    si un verset dément l'alignement. Tout est en domaine public des deux
    côtés — il n'y a rien à cloisonner ici.
    """
    textes, analyses = _lire_csv_byz(accentue), _lire_csv_byz(analyse)
    versets = []
    for cle in sorted(analyses, key=lambda k: (k[0], k[1])):
        ch, vs = cle
        parses = [(m.group(1), int(m.group(2)), m.group(3))
                  for m in MOT_BYZ.finditer(analyses[cle])]
        if cle not in textes:
            raise ValueError(f"{livre} {ch}:{vs} : absent de l'édition accentuée.")
        formes = textes[cle].split()
        if len(formes) != len(parses):
            raise ValueError(
                f"{livre} {ch}:{vs} : {len(formes)} mots accentués contre "
                f"{len(parses)} analysés — les deux éditions ont divergé.")
        mots = []
        for forme, (nu, strong, parse) in zip(formes, parses):
            if _depouiller(forme) != _depouiller(nu):
                raise ValueError(
                    f"{livre} {ch}:{vs} : {forme!r} en face de {nu!r} — "
                    f"l'alignement des deux éditions est rompu.")
            mots.append({"t": forme, "strong": strong, "parse": parse})
        versets.append((ch, vs, mots))
    return versets


# --------------------------------------------------------------------------

def ecrire(sortie: Path, versets, livre: str) -> dict:
    """Une ligne JSON par verset, ordre du texte conservé. Rend le compte."""
    if not versets:
        raise ValueError(
            f"{livre} : aucun verset lu. Un lecteur qui rend zéro sans lever "
            f"produit un `sources/` vide et bien formé — on s'arrête ici.")
    sortie.parent.mkdir(parents=True, exist_ok=True)
    mots = 0
    with sortie.open("w", encoding="utf-8") as f:
        for ch, vs, ws in versets:
            mots += len(ws)
            f.write(json.dumps({"ref": f"{livre}.{ch}.{vs}", "c": ch, "v": vs, "w": ws},
                               ensure_ascii=False, separators=(",", ":")) + "\n")
    return {"versets": len(versets), "mots": mots}


def cloner(depots: Path):
    depots.mkdir(parents=True, exist_ok=True)
    for _, (url, nom) in DEPOTS.items():
        cible = depots / nom
        if cible.exists():
            print(f"  {nom} : déjà là")
            continue
        print(f"  {nom} : clone…")
        subprocess.run(["git", "clone", "--depth", "1", "--quiet", url, str(cible)],
                       check=True)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--depots", type=Path, required=True,
                    help="dossier contenant les clones des trois dépôts amont")
    ap.add_argument("--sortie", type=Path,
                    default=Path(__file__).resolve().parent.parent / "sources")
    ap.add_argument("--cloner", action="store_true",
                    help="cloner les dépôts manquants avant de convertir")
    args = ap.parse_args()

    if args.cloner:
        print("Clones amont :")
        cloner(args.depots)

    manquants, manifeste = [], {}

    # -- hébreu ------------------------------------------------------------
    racine_he = args.depots / DEPOTS["he-wlc"][1] / "wlc"
    livres_he = {}
    for livre, (num, slug) in sorted(ONT_HE.items(), key=lambda kv: (kv[1][0], kv[0])):
        src = racine_he / f"{livre}.xml"
        if not src.exists():
            manquants.append(f"he-wlc/{livre}.xml")
            continue
        stats = ecrire(args.sortie / "he-wlc" / f"{livre}.jsonl",
                       lire_hebreu(src), livre)
        livres_he[livre] = {"ont": num, "slug": slug, **stats}
    manifeste["he-wlc"] = livres_he

    # -- grec éclectique ---------------------------------------------------
    racine_sbl = args.depots / DEPOTS["grc-sblgnt"][1]
    fichiers_sbl = {}
    for f in racine_sbl.glob("*-morphgnt.txt"):
        fichiers_sbl[f.name.split("-")[1]] = f
    livres_sbl = {}
    for livre, (num, slug) in sorted(ONT_GRC.items(), key=lambda kv: kv[1][0]):
        src = fichiers_sbl.get(livre)
        if src is None:
            manquants.append(f"grc-sblgnt/{livre}")
            continue
        stats = ecrire(args.sortie / "grc-sblgnt" / f"{livre}.jsonl",
                       lire_sblgnt(src), livre)
        livres_sbl[livre] = {"ont": num, "slug": slug, **stats}
    manifeste["grc-sblgnt"] = livres_sbl

    # -- grec byzantin -----------------------------------------------------
    racine_byz = args.depots / DEPOTS["grc-byz"][1] / "csv-unicode"
    byz_analyse = racine_byz / "strongs" / "with-parsing"
    byz_accentue = racine_byz / "ccat" / "no-variants"
    livres_byz = {}
    for court, livre in sorted(BYZ_VERS_SBL.items(), key=lambda kv: ONT_GRC[kv[1]][0]):
        a, b = byz_accentue / f"{court}.csv", byz_analyse / f"{court}.csv"
        if not (a.exists() and b.exists()):
            manquants.append(f"grc-byz/{court}.csv")
            continue
        num, slug = ONT_GRC[livre]
        stats = ecrire(args.sortie / "grc-byz" / f"{livre}.jsonl",
                       lire_byzantin(a, b, livre), livre)
        livres_byz[livre] = {"ont": num, "slug": slug, **stats}
    manifeste["grc-byz"] = livres_byz

    # -- manifeste ---------------------------------------------------------
    # Les sources qu'un AUTRE script gère doivent survivre à cet import.
    # Écrire le manifeste en entier les effacerait sans un mot — et un
    # `sources/` amputé reste bien formé, donc invisible.
    anciennes = {}
    ancien = args.sortie / "MANIFEST.json"
    if ancien.is_file():
        try:
            anciennes = {c: m for c, m in
                         json.loads(ancien.read_text(encoding="utf-8"))
                         .get("sources", {}).items() if c not in SOURCES}
        except json.JSONDecodeError:
            pass

    doc = {
        "avertissement": "Forme neutre, classée par référence biblique. Ne "
                         "connaît ni les parashiot ni la numérotation interne "
                         "des unités ONT — la jointure est au pipeline.",
        "sources": dict(anciennes),
    }
    for cle, meta in SOURCES.items():
        livres = manifeste.get(cle, {})
        doc["sources"][cle] = {
            **meta,
            "commit_amont": commit_amont(args.depots / DEPOTS[cle][1]),
            "depot_amont": DEPOTS[cle][0],
            "totaux": {"livres": len(livres),
                       "versets": sum(v["versets"] for v in livres.values()),
                       "mots": sum(v["mots"] for v in livres.values())},
            "livres": livres,
        }
    args.sortie.mkdir(parents=True, exist_ok=True)
    (args.sortie / "MANIFEST.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
        encoding="utf-8")

    for cle in anciennes:
        t = doc["sources"][cle].get("totaux", {})
        print(f"{cle:12} {t.get('livres', '?'):>3} livres  "
              f"{t.get('versets', '?'):>6} versets  (gérée ailleurs, préservée)")
    for cle in SOURCES:
        t = doc["sources"][cle]["totaux"]
        print(f"{cle:12} {t['livres']:3} livres  {t['versets']:6} versets  "
              f"{t['mots']:7} mots")

    if manquants:
        print("\nManquants :", ", ".join(manquants), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
