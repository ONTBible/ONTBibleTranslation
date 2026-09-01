#!/usr/bin/env python3
"""Éprouve `sources/` — la couche des textes en langue source.

    ./scripts/eprouver-les-sources.py

Rend **1** dès qu'un contrôle échoue, pour qu'un enchaînement s'arrête dessus.

## Pourquoi une épreuve, et pas seulement une relecture

Trois des contrôles ci-dessous portent sur des **licences**. Une licence qui
n'est tenue que par l'intention de celui qui écrit tient jusqu'à la première
session qui ne l'a pas lue.

Le plus important est le cloisonnement de **MorphGNT**. Ses étiquettes sont en
CC BY-SA — une clause de copyleft : ce qui s'y mélange en hérite. Elles vivent
donc dans le seul champ `mgnt`, et la couche fonctionnelle de l'ONT ne doit
jamais y entrer. Un schéma qui les fusionne ne se défusionne pas, et la clause
mordrait alors sur le travail de l'auteur.

C'est exactement le genre de contrainte qu'on croit tenir parce qu'on l'a
comprise. On la tient parce qu'une machine la mesure.
"""

import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SOURCES = RACINE / "sources"

# Ce qu'un mot a le droit de porter, par source. Un champ inattendu est une
# fuite : soit une donnée amont non déclarée, soit de la couche ONT qui
# descend dans un espace sous licence étrangère.
CHAMPS = {
    "he-wlc": ({"t", "oshb"}, "oshb", {"seg", "lem", "morph", "id", "qere"}),
    "grc-sblgnt": ({"t", "mgnt"}, "mgnt", {"pos", "parse", "mot", "norm", "lem"}),
    "grc-byz": ({"t", "strong", "parse"}, None, set()),
    # Le guèze ne porte aucune morphologie : rien à cloisonner, mais la liste
    # reste fermée — un champ inattendu resterait une fuite.
    "gez-dillmann": ({"t"}, None, set()),
}


def main() -> int:
    plaintes = []

    def plainte(msg):
        plaintes.append(msg)

    if not SOURCES.is_dir():
        print("sources/ est absent.", file=sys.stderr)
        return 1

    manifeste = SOURCES / "MANIFEST.json"
    if not manifeste.is_file():
        print("sources/MANIFEST.json est absent.", file=sys.stderr)
        return 1
    doc = json.loads(manifeste.read_text(encoding="utf-8"))

    declarees = set(doc.get("sources", {}))
    sur_disque = {d.name for d in SOURCES.iterdir() if d.is_dir()}
    if declarees != sur_disque:
        plainte(f"le manifeste déclare {sorted(declarees)} ; "
                f"le disque porte {sorted(sur_disque)}")

    for cle, meta in doc.get("sources", {}).items():
        # -- l'attribution voyage avec la source, jamais dans un écran à part --
        if not meta.get("attribution"):
            plainte(f"{cle} : pas d'attribution déclarée")
        for bloc in ("texte", "analyse"):
            if not (meta.get(bloc) or {}).get("licence"):
                plainte(f"{cle} : licence du {bloc} non déclarée")
        # Une source tirée d'un dépôt git doit dire lequel et à quel commit.
        # Une source tirée d'un site doit dire l'URL et la permission obtenue.
        if meta.get("depot_amont"):
            if meta.get("commit_amont") in (None, "", "inconnu"):
                plainte(f"{cle} : commit amont inconnu — import non rejouable")
        else:
            saisie = meta.get("saisie") or {}
            if not saisie.get("url"):
                plainte(f"{cle} : ni dépôt amont ni URL de saisie")
            if saisie.get("licence") and "non commercial" in saisie["licence"] \
               and not saisie.get("permission"):
                plainte(f"{cle} : saisie sous clause non commerciale sans "
                        f"permission déclarée")

        attendus, ilot, champs_ilot = CHAMPS.get(cle, (None, None, set()))
        if attendus is None:
            plainte(f"{cle} : source inconnue de l'épreuve")
            continue

        # -- le cloisonnement du copyleft, mesuré et non supposé ---------------
        copyleft = (meta.get("analyse") or {}).get("copyleft")
        if copyleft and ilot is None:
            plainte(f"{cle} : analyse sous copyleft sans champ dédié")

        for livre, attendu in sorted(meta.get("livres", {}).items()):
            chemin = SOURCES / cle / f"{livre}.jsonl"
            if not chemin.is_file():
                plainte(f"{cle}/{livre}.jsonl : absent")
                continue
            versets = mots = 0
            vus = set()
            for n, ligne in enumerate(chemin.read_text(encoding="utf-8").splitlines(), 1):
                try:
                    v = json.loads(ligne)
                except json.JSONDecodeError as e:
                    plainte(f"{cle}/{livre}.jsonl:{n} : JSON illisible — {e}")
                    break
                ref = v.get("ref")
                if ref in vus:
                    plainte(f"{cle}/{livre}.jsonl:{n} : référence en double — {ref}")
                vus.add(ref)
                if ref != f"{livre}.{v.get('c')}.{v.get('v')}":
                    plainte(f"{cle}/{livre}.jsonl:{n} : `ref` désaccordé — {ref}")
                versets += 1
                for mot in v.get("w", []):
                    mots += 1
                    trop = set(mot) - attendus
                    if trop:
                        plainte(f"{cle}/{livre}.jsonl:{n} : champs non déclarés "
                                f"au niveau du mot — {sorted(trop)}")
                    if ilot and ilot in mot:
                        fuite = set(mot[ilot]) - champs_ilot
                        if fuite:
                            plainte(f"{cle}/{livre}.jsonl:{n} : `{ilot}` porte "
                                    f"{sorted(fuite)} — l'îlot sous licence "
                                    f"étrangère doit rester fermé")
                    if not mot.get("t"):
                        plainte(f"{cle}/{livre}.jsonl:{n} : mot sans texte")
            if versets != attendu["versets"] or mots != attendu["mots"]:
                plainte(f"{cle}/{livre}.jsonl : {versets} versets / {mots} mots "
                        f"sur le disque, {attendu['versets']} / {attendu['mots']} "
                        f"au manifeste")

    for p in plaintes[:40]:
        print(p, file=sys.stderr)
    if len(plaintes) > 40:
        print(f"… et {len(plaintes) - 40} autres.", file=sys.stderr)

    if plaintes:
        print(f"\n{len(plaintes)} plainte(s).", file=sys.stderr)
        return 1

    t = {c: m["totaux"] for c, m in doc["sources"].items()}
    for c, v in t.items():
        print(f"{c:12} {v['livres']:3} livres  {v['versets']:6} versets  "
              f"{v['mots']:7} mots")
    print("\nsources/ : rien à redire.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
