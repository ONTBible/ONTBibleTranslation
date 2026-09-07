#!/usr/bin/env python3
"""Importe l'apparat critique du SBLGNT.

    ./scripts/importer-l-apparat-du-sblgnt.py

Écrit `sources/grc-sblgnt/<livre>-apparat.jsonl`. Rend **1** si la forme amont
a bougé sous les pieds du script.

## ⚠️ Ce que cet apparat est, et ce qu'il n'est PAS

Il ==ne compare pas des manuscrits==. Il compare **quatre éditions imprimées
modernes** :

    WH      Westcott-Hort, 1881
    Treg    Tregelles, 1857
    NA28    Nestle-Aland, 2012
    RP      Robinson-Pierpont

Une entrée dit « à cet endroit, l'édition de Westcott-Hort porte ceci et celle
de Nestle-Aland porte cela ». Elle ne dira ==jamais== « le Codex Sinaiticus
porte ceci ».

C'est un piège de vocabulaire, et il faut que le lecteur en soit protégé :
« apparat critique » évoque des manuscrits, et celui-ci n'en montre aucun. Le
libellé de la liseuse doit tenir cette différence.

**Un quart est déjà à l'écran.** Robinson-Pierpont est l'une des quatre
éditions citées, et l'ONT l'affiche déjà comme second témoin grec. Le lecteur
*voit* donc cette divergence-là au lieu de lire qu'elle existe.

## La forme amont

    Mark 2:1                              ← l'en-tête, seul repère fiable
    2:1 εἰσελθὼν WH Treg NA28 ] εἰσῆλθεν RP
    • ἡμερῶν WH Treg NA28 ] + καὶ RP      ← même verset, entrée suivante

Le numéro qui ouvre une entrée est tantôt `2:1`, tantôt `2`, tantôt un `•` : il
dépend de ce qui précède. ==On ne le lit pas.== La référence vient de la ligne
d'en-tête, qui est complète et sans ambiguïté.

Le `]` sépare la leçon du SBLGNT — suivie des éditions qui l'appuient — des
variantes, elles-mêmes séparées par `;`.
"""

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

BASE = ("https://raw.githubusercontent.com/LogosBible/SBLGNT/master/"
        "data/sblgntapp/text/{}.txt")

AGENT = ("ONT-corpus/1.0 (https://ontbible.com; contact@ontbible.com) "
         "python-urllib")

# Les sigles d'édition, ==relevés et non devinés==.
#
# La première version n'en déclarait que six — les quatre principales plus NIV
# et Holmes — et le découpage s'arrêtait au premier jeton inconnu. Résultat :
# trente-neuf variantes rendues sans aucune édition, et des leçons polluées
# (« τεκνία WH Treg NA27 » au lieu de « τεκνία »).
#
# La liste ci-dessous vient d'un balayage de tous les jetons latins des
# 6 934 entrées, non d'une lecture d'échantillon. Ajouter les trois sigles
# aperçus aurait laissé passer les cinq autres.
EDITIONS = {
    "WH", "Treg", "NA28", "RP",          # les quatre éditions comparées
    "NA27", "WHmarg", "WHapp", "Tregmarg",  # états antérieurs et marges
    "NIV", "Holmes", "TR", "Greeven",    # témoins ponctuels
}

# amont → notre clé de livre, celle des fichiers grc-sblgnt/
LIVRES = {
    "Matt": "Mt", "Mark": "Mk", "Luke": "Lk", "John": "Jn", "Acts": "Ac",
    "Rom": "Ro", "1Cor": "1Co", "2Cor": "2Co", "Gal": "Ga", "Eph": "Eph",
    "Phil": "Php", "Col": "Col", "1Thess": "1Th", "2Thess": "2Th",
    "1Tim": "1Ti", "2Tim": "2Ti", "Titus": "Tit", "Phlm": "Phm",
    "Heb": "Heb", "Jas": "Jas", "1Pet": "1Pe", "2Pet": "2Pe",
    "1John": "1Jn", "2John": "2Jn", "3John": "3Jn", "Jude": "Jud",
    "Rev": "Re",
}

ENTETE = re.compile(r"^[A-Za-z0-9 ]+ (\d+):(\d+)\s*$")
OUVERTURE = re.compile(r"^(?:•|\d+(?::\d+)?)\s*")


def temoins_en_queue(morceau: str):
    """Détache les sigles d'édition de la fin d'un morceau.

    Rend `(texte, [sigles], [sigles entre doubles crochets])`. Le texte grec
    précède toujours ses sigles ; on remonte donc depuis la fin tant qu'on
    reconnaît une édition.

    ## Les doubles crochets ⟦ ⟧, qu'il ne faut pas jeter

    `⟦WH⟧` ne veut pas dire « WH ». Il veut dire ==WH imprime ce passage mais
    le tient pour douteux== — c'est la notation par laquelle Westcott et Hort
    ont gardé un texte tout en refusant de le garantir.

    Et les endroits où elle paraît ne sont pas quelconques : la sueur de sang
    de *Luc* 22:43-44, le « Père, pardonne-leur » de *Luc* 23:34, les
    non-interpolations occidentales de *Luc* 24, la finale longue de
    *Marc* 16:9-20, les signes du ciel de *Matthieu* 16:2-3. Perdre le crochet
    reviendrait à faire dire à Westcott-Hort qu'ils tenaient pour sûr ce
    qu'ils ont précisément voulu mettre en doute.
    """
    mots = morceau.split()
    sigles, doutes = [], []
    while mots:
        dernier = mots[-1].rstrip(".,")
        if dernier in EDITIONS:
            sigles.insert(0, dernier)
            mots.pop()
        elif dernier.startswith("⟦") and dernier.endswith("⟧") \
                and dernier[1:-1] in EDITIONS:
            doutes.insert(0, dernier[1:-1])
            mots.pop()
        else:
            break
    return " ".join(mots).strip(), sigles, doutes


def decouper_variantes(droite: str):
    """Sépare les variantes sans casser le grec.

    ==En grec, le `;` est le point d'interrogation.== Découper naïvement dessus
    briserait toute variante contenant une question — et le fait en silence,
    puisque les morceaux restent du grec bien formé.

    Le séparateur de l'apparat se distingue par ce qui le précède : il suit
    toujours un **sigle d'édition**, jamais du grec. On ne coupe donc qu'après
    un sigle.
    """
    morceaux, courant = [], []
    for jeton in re.split(r"(;)", droite):
        if jeton == ";":
            mots = " ".join(courant).split()
            if mots and mots[-1].rstrip(":") in EDITIONS:
                morceaux.append(" ".join(courant))
                courant = []
            else:
                courant.append(";")
        else:
            courant.append(jeton)
    if courant:
        morceaux.append(" ".join(courant))
    return [m for m in morceaux if m.strip()]


def lire(livre_amont: str, cle: str):
    url = BASE.format(livre_amont)
    req = urllib.request.Request(url, headers={"User-Agent": AGENT})
    texte = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")

    entrees = []
    reference = None
    for ligne in texte.splitlines():
        l = ligne.strip()
        if not l:
            continue
        if m := ENTETE.match(l):
            reference = (int(m.group(1)), int(m.group(2)))
            continue
        if "]" not in l:
            continue
        if reference is None:
            raise ValueError(
                f"{cle} : une entrée précède toute ligne d'en-tête — « {l[:50]} ». "
                f"La forme amont a changé, et deviner la référence serait pire "
                f"que s'arrêter.")
        corps = OUVERTURE.sub("", l, count=1)
        gauche, droite = corps.split("]", 1)
        lecon, appui, appui_doute = temoins_en_queue(gauche)
        variantes = []
        for part in decouper_variantes(droite):
            t, sig, doute = temoins_en_queue(part)
            if not sig and not doute:
                # « + 7:53–8:11 RP: 53 καὶ ἐπορεύθη… » — le sigle PRÉCÈDE le
                # texte et l'annonce par un deux-points. C'est la forme des
                # longs passages ajoutés : la péricope de la femme adultère,
                # la piscine de Bethesda, la doxologie de Romains 16.
                if m := re.match(rf"^(.*?)\s+({'|'.join(EDITIONS)}):\s*(.*)$",
                                 part, re.S):
                    t, sig = f"{m.group(1)} {m.group(3)}".strip(), [m.group(2)]
            if t or sig or doute:
                v = {"t": t, "editions": sig}
                if doute:
                    v["crochets"] = doute
                variantes.append(v)
        if not appui and not appui_doute and not variantes:
            raise ValueError(f"{cle} {reference} : entrée sans édition — « {l[:60]} »")
        c, v = reference
        entrees.append({
            "ref": f"{cle}.{c}.{v}",
            "c": c,
            "v": v,
            "lecon": lecon,
            "editions": appui,
            **({"crochets": appui_doute} if appui_doute else {}),
            "variantes": variantes,
        })
    return entrees


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", type=Path,
                    default=Path(__file__).resolve().parent.parent / "sources"
                            / "grc-sblgnt")
    a = ap.parse_args()
    a.sortie.mkdir(parents=True, exist_ok=True)

    total = 0
    manquants = []
    for amont, cle in sorted(LIVRES.items(), key=lambda kv: kv[1]):
        try:
            entrees = lire(amont, cle)
        except Exception as e:  # noqa: BLE001 — on veut le livre en cause
            manquants.append(f"{amont} : {e}")
            continue
        if not entrees:
            manquants.append(f"{amont} : aucune entrée lue")
            continue
        chemin = a.sortie / f"{cle}-apparat.jsonl"
        with chemin.open("w", encoding="utf-8") as f:
            for e in entrees:
                f.write(json.dumps(e, ensure_ascii=False,
                                   separators=(",", ":")) + "\n")
        total += len(entrees)

    # ── L'inscription au manifeste ────────────────────────────────────────
    #
    # L'apparat n'est PAS un témoin : il ne porte aucun texte ancien, il
    # compare des éditions modernes entre elles. Il vit donc dans l'entrée de
    # `grc-sblgnt`, à côté du témoin qu'il commente, et jamais comme une
    # cinquième source.
    manif = a.sortie.parent / "MANIFEST.json"
    doc = json.loads(manif.read_text(encoding="utf-8"))
    doc["sources"]["grc-sblgnt"]["apparat"] = {
        "oeuvre": "SBL Greek New Testament — apparat critique",
        "licence": "CC BY 4.0",
        "url": "https://github.com/LogosBible/SBLGNT",
        "avertissement": "Il compare QUATRE ÉDITIONS IMPRIMÉES — Westcott-Hort "
                         "1881, Tregelles 1857, Nestle-Aland 2012, "
                         "Robinson-Pierpont — et jamais des manuscrits. Une "
                         "entrée ne dira pas ce que porte un codex ancien. "
                         "Le libellé montré au lecteur doit tenir cette "
                         "différence : « apparat critique » évoque des "
                         "manuscrits, et celui-ci n'en montre aucun.",
        "deja_a_l_ecran": "Robinson-Pierpont est l'une des quatre éditions "
                          "comparées, et l'ONT l'affiche déjà comme second "
                          "témoin grec — le lecteur voit cette divergence-là "
                          "au lieu de la lire.",
        "crochets": "⟦WH⟧ signifie que Westcott-Hort imprime le passage tout "
                    "en le tenant pour douteux : Luc 22:43-44, Luc 23:34, la "
                    "finale longue de Marc. Le champ `crochets` le conserve.",
        "entrees": total,
        "editions": sorted(EDITIONS),
        "fichiers": "sources/grc-sblgnt/<livre>-apparat.jsonl",
    }
    manif.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8")

    print(f"{len(LIVRES) - len(manquants)} livres  {total} entrées d'apparat")
    if manquants:
        print("\nÉchecs :", *manquants, sep="\n  ", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
