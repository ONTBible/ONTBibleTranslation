#!/usr/bin/env python3
"""Ce que la recherche de la KB trouve, et ce qu'elle rate.

Douze questions en français, et pour chacune la source qui y répond
vraiment — relevée dans les documents **avant** tout lancement.

C'est la seule chose qui rend ce banc utile, et c'est la règle du dépôt :
*un instrument se valide sur un cas dont on connaît la réponse, jamais sur
celui qu'on étudie.* Une amélioration jugée à l'impression n'est pas une
amélioration ; ici elle se chiffre.

    python3 knowledge/banc-recherche.py
    python3 knowledge/banc-recherche.py --json

Point de départ, mesuré le 18 septembre 2026 sur `main` @ 68c7849 :

    5 trouvées sur 12 — 42 %
    rang moyen quand trouvé : 1,2 sur 8 rendus

Les deux causes des sept ratées, mesurées et non supposées :

    taille de la section    médiane ratée 16 094 car. contre 3 500 trouvée
    population homogène     « Prononciation » paraît dans 437 fiches
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

RACINE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("ont_kb", RACINE / "knowledge/consulter.py")
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)

DEPART = 5  # sur 12, le 18 septembre 2026 — à ne pas bouger sans remesurer

# (question, fichier attendu, fragment du titre de la section attendue)
BANC = [
    ("pourquoi chesed ne se traduit pas par grâce ?",
     "CLAUDE.md", "3.2 Noms et concepts fondamentaux"),
    ("comment se prononce le qof ?",
     "CLAUDE.md", "Les consonnes que le français n'a pas"),
    ("est-ce qu'on compte les cieux dans l'ONT ?",
     "CLAUDE.md", "6.3 Ce que le gradient commande"),
    ("le het en finale s'écrit comment ?",
     "CLAUDE.md", "Le het se rend"),
    ("quelle différence entre malkhut, mamlakhah et melukhah ?",
     "CLAUDE.md", "2.5 Marquage des termes intraduisibles"),
    ("comment marquer un renvoi d'une chuqqah vers une autre ?",
     "CLAUDE.md", "2.11 Les renvois entre chuqqot"),
    ("que met-on dans la Source quand le témoin ne porte pas le mot ?",
     "CLAUDE.md", "2.5 ter Les fiches de lexique"),
    ("quelle densité de glose viser dans un texte de vision araméen ?",
     "CLAUDE.md", "4.1 Les gloses"),
    ("un numéro de Strong dit-il ce que le mot veut dire ?",
     "CLAUDE.md", "2.5 ter Les fiches de lexique"),
    ("pourquoi Haran et Charan sont-ils deux noms distincts ?",
     "CLAUDE.md", "Le het se rend"),
    ("comment écrit-on l'article défini dans un nom de livre ?",
     "CLAUDE.md", "2.6 Les noms des livres bibliques"),
    ("que fait-on quand le français force une majuscule que l'hébreu n'a pas ?",
     "CLAUDE.md", "Quand le français n'a aucune forme neutre"),
]


def rendus(d):
    """Tout ce que le dossier a ramené, dans l'ordre — extraits puis sources.

    On est généreux à dessein : la cible compte pour trouvée si elle paraît
    n'importe où dans le dossier, pas seulement en tête. Un banc qui se
    montre dur avec l'instrument qu'il mesure flatte l'amélioration suivante.
    """
    out = [(e.get("fichier", ""), e.get("section", "")) for e in d["extraits_du_vault"]]
    out += [(s.get("fichier", ""), s.get("ancre", ""))
            for n in d["notices"] for s in n.get("sources", [])]
    return out


def passer(vault, limite=8, budget=12000):
    lignes = []
    for question, fichier, cible in BANC:
        elems = rendus(kb.dossier(vault, question, limite=limite, budget=budget))
        # La cible compte si la BONNE SECTION remonte — que ce soit depuis le
        # document de référence ou depuis un passage qui en est engendré.
        # Le critère de section ne bouge pas : un passage du §2.6 ne vaudra
        # jamais pour une question du §3.2. Seul le fichier porteur devient
        # indifférent, parce que le découpage déplace le contenu sans le
        # changer. Sans cette clause, le banc mesurerait l'emplacement au
        # lieu de la trouvaille — et punirait l'amélioration qu'il mesure.
        rang = next((i for i, (f, s) in enumerate(elems, 1)
                     if cible.lower() in (s or "").lower()
                     and (f == fichier or f.startswith("passages/"))), None)
        lignes.append({"question": question, "attendu": f"{fichier} § {cible}",
                       "rang": rang, "trouve": rang is not None,
                       "tete": f"{elems[0][0]} § {elems[0][1]}" if elems else None})
    trouves = sum(l["trouve"] for l in lignes)
    rangs = [l["rang"] for l in lignes if l["rang"]]
    return {"questions": len(BANC), "trouvees": trouves,
            "taux": round(100 * trouves / len(BANC)),
            "rang_moyen": round(sum(rangs) / len(rangs), 1) if rangs else None,
            "depart": DEPART, "ecart": trouves - DEPART, "details": lignes}


def rendre(r):
    print(f"\n  {'question':64} {'rang':>5}  ce qui remonte en tête")
    print("  " + "─" * 108)
    for l in r["details"]:
        rang = f"#{l['rang']}" if l["rang"] else "✗"
        print(f"  {l['question'][:64]:64} {rang:>5}  {(l['tete'] or '— rien —')[:36]}")
    print("  " + "─" * 108)
    print(f"\n  TROUVÉES {r['trouvees']}/{r['questions']} ({r['taux']} %)"
          f"   ·   rang moyen {r['rang_moyen']}"
          f"   ·   départ {r['depart']}/{r['questions']}", end="")
    if r["ecart"] > 0:
        print(f"   ·   \033[32m+{r['ecart']} depuis le départ\033[0m")
    elif r["ecart"] < 0:
        print(f"   ·   \033[31m{r['ecart']} — RÉGRESSION\033[0m")
    else:
        print("   ·   inchangé")


def main(argv=None):
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--vault", default=str(RACINE))
    a.add_argument("--json", action="store_true")
    a.add_argument("--limite", type=int, default=8)
    o = a.parse_args(argv)
    r = passer(Path(o.vault).resolve(), limite=o.limite)
    print(json.dumps(r, ensure_ascii=False, indent=2)) if o.json else rendre(r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
