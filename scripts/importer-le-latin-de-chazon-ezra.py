#!/usr/bin/env python3
"""Importe le latin du *Chazon Ezra* — la Vulgate clémentine, chapitres 3-14.

    ./scripts/importer-le-latin-de-chazon-ezra.py

Rend **1** si la source amont a bougé sous les pieds du script.

## Pourquoi le latin, et pas une autre langue

*4 Esdras* n'est conservé dans aucune langue sémitique. Son ==témoin principal
est le latin== — c'est par lui que le livre a traversé le Moyen Âge, glissé en
appendice de la Vulgate par des scribes qui ne le tenaient pas pour canonique.
Le syriaque, l'éthiopien, le géorgien, l'arabe et l'arménien complètent, mais
c'est le latin qui porte.

Comme le guèze de *1 Chanokh*, c'est un ==témoin de second degré== : le latin
traduit un grec perdu, qui traduisait un hébreu perdu. Le dire fait partie de
l'honnêteté de la couche.

## Les chapitres 3 à 14, et pas les seize

Le manuscrit latin porte seize chapitres. Les chapitres 1-2 et 15-16 sont des
==additions chrétiennes hellénisées==, et le critère d'inclusion de l'ONT les
écarte : ce sont des textes qui pensent en grec. Seuls les chapitres 3-14
forment l'apocalypse juive.

## ⚠️ La lacune de 7:36-105, et pourquoi elle reste ouverte

Soixante-dix versets manquent au chapitre 7, et ==ce n'est pas un accident de
transmission==. Le passage porte sur l'intercession pour les morts, et il a été
==retranché des manuscrits latins au Moyen Âge== parce qu'il la refusait. On a
coupé la page.

Robert Bensly l'a retrouvée en 1875 dans un manuscrit du IXᵉ siècle à Amiens,
qui avait échappé au couteau. Son édition est dans le domaine public — mais elle
n'existe qu'en fac-similé, et son OCR est illisible.

**Le syriaque, lui, a gardé le passage.** Il n'a jamais subi cette censure.
C'est la voie pour combler la lacune, et elle dépend d'une question de licence
posée à l'Online Critical Pseudepigrapha.

En attendant, ==la lacune est déclarée, pas masquée== : le lecteur qui touche un
verset de cette zone doit savoir qu'il manque, et pourquoi.

## La numérotation est ramenée à la norme, et voici comment on l'a établi

La Clémentine numérote son chapitre 7 de 1 à 69 sans trou : chez elle, la lacune
tombe **entre** 7:35 et 7:36. Les éditions modernes restaurent le fragment et
numérotent 7:1-140. Ce fichier porte ==la numérotation moderne==, parce qu'un
numéro de verset est un ==système de renvoi== : « Chazon Ezra 7:120 » doit
désigner la même chose ici et partout ailleurs.

Le décalage a d'abord paru invérifiable : 69 + 70 = 139, quand la norme va à
140. Un verset d'écart, sans témoin pour dire d'où il venait.

**Il venait du texte lui-même.** Le dernier verset clémentin, 7:69, fait
==171 signes quand les autres du chapitre en font 96== en moyenne, et il porte
deux propositions distinctes :

    Et judex si non ignoverit his qui curati sunt verbo ejus
    et deleverit multitudinem contentionum                     ← 7:139
    non fortassis derelinquerentur in innumerabili multitudine
    nisi pauci valde                                           ← 7:140

La Clémentine ==fusionne les deux derniers versets==. Tout l'écart est là.

Le décalage de +70 a ensuite été contrôlé sur quatre ancres réparties dans la
zone — 7:36, 7:44, 7:50 et 7:68, qui tombent sur 7:106, 7:114, 7:120 et 7:138 —
et il tient sur les quatre.

D'où la correspondance appliquée :

    clémentine 7:1-35    →  7:1-35      inchangé
    clémentine 7:36-68   →  7:106-138   décalé de +70
    clémentine 7:69      →  7:139 + 7:140   défusionné

Les versets 36 à 105 ==n'existent donc pas dans ce fichier==, et c'est la
vérité : ils manquent au témoin latin.

## L'assise, et pourquoi Wikisource n'est qu'un facteur

Le texte est celui de la ==Vulgate clémentine (1592)==, dans le domaine public
sans discussion. Wikisource n'en est que le transporteur : une transcription
fidèle d'un texte libre ne crée aucun droit nouveau, faute d'originalité. C'est
le même raisonnement que pour Dillmann 1851.
"""

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

PAGE = "Vulgata Clementina/Liber Quartus Esdrae"
API = ("https://la.wikisource.org/w/api.php?action=parse&page={}"
       "&prop=wikitext&format=json&formatversion=2")

PERIMETRE = range(3, 15)          # les seize chapitres moins les additions
LACUNE = (7, 36, 105)             # chapitre, premier et dernier verset absents

# Ramener le ch. 7 de la numérotation clémentine à la norme moderne.
# Le décalage est établi, non supposé : voir l'en-tête.
DECALAGE_CH7 = 70                 # clémentine 36-68 → moderne 106-138
DERNIER_CLEMENTIN = 69            # qu'il faut défusionner en 139 + 140
COUPURE_139_140 = "non fortassis"  # l'ancre, prise dans le texte lui-même
ATTENDU = {3: 36, 4: 52, 5: 55, 6: 59, 7: 69, 8: 63,
           9: 47, 10: 60, 11: 46, 12: 51, 13: 58, 14: 47}


# Wikimedia exige un agent qui se nomme et laisse un contact — une requête
# anonyme reçoit un 403. Ce n'est pas une formalité : c'est ce qui leur permet
# de nous joindre plutôt que de nous bloquer.
AGENT = ("ONT-corpus/1.0 (https://ontbible.com; contact@ontbible.com) "
         "python-urllib")


def wikitexte() -> str:
    url = API.format(urllib.parse.quote(PAGE))
    req = urllib.request.Request(url, headers={"User-Agent": AGENT})
    d = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))
    if "parse" not in d:
        raise ValueError(f"Wikisource n'a pas rendu la page « {PAGE} ».")
    return d["parse"]["wikitext"]


def nettoyer(t: str) -> str:
    """Retire le balisage wiki ; garde le latin et sa ponctuation."""
    t = re.sub(r"\{\{[^{}]*\}\}", " ", t)
    t = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[\[([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"<ref[^>]*>.*?</ref>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = t.replace("'''", "").replace("''", "")
    return " ".join(t.split())


def mots_du(verset: str):
    """`w` est une liste de mots partout dans `sources/` — ici comme ailleurs."""
    return [{"t": m} for m in
            (x.strip(" ,;:.!?()[]«»—") for x in verset.split())
            if any(c.isalpha() for c in m)]


def lire():
    w = wikitexte()
    caps = list(re.finditer(r"==\s*Caput\s+(\d+)\s*==", w))
    if not caps:
        raise ValueError("aucun « == Caput N == » — la page a changé de forme.")
    versets = []
    vus = {}
    for k, m in enumerate(caps):
        n = int(m.group(1))
        if n not in PERIMETRE:
            continue
        fin = caps[k + 1].start() if k + 1 < len(caps) else len(w)
        corps = w[m.end():fin]
        # Les versets sont ouverts par <sup>N</sup> ; on découpe dessus.
        bornes = list(re.finditer(r"<sup>\s*(\d+)\s*</sup>", corps))
        if not bornes:
            raise ValueError(f"chapitre {n} : aucun <sup>N</sup> — forme changée.")
        for j, b in enumerate(bornes):
            v = int(b.group(1))
            texte = nettoyer(corps[b.end(): bornes[j + 1].start()
                                   if j + 1 < len(bornes) else fin - m.end()])
            if not texte:
                continue
            if n == 7 and v >= 36:
                if v < DERNIER_CLEMENTIN:
                    versets.append((n, v + DECALAGE_CH7, texte))
                else:
                    i = texte.find(COUPURE_139_140)
                    if i < 0:
                        raise ValueError(
                            f"7:{v} : l'ancre « {COUPURE_139_140} » a disparu — "
                            f"la défusion des versets 139/140 n'est plus sûre.")
                    versets.append((n, 139, texte[:i].strip()))
                    versets.append((n, 140, texte[i:].strip()))
            else:
                versets.append((n, v, texte))
        vus[n] = len(bornes)
    manquants = [n for n in PERIMETRE if n not in vus]
    if manquants:
        raise ValueError(f"chapitres absents de la page : {manquants}")
    faux = {n: (vus[n], ATTENDU[n]) for n in ATTENDU if vus[n] != ATTENDU[n]}
    if faux:
        raise ValueError(
            f"le compte des versets a bougé depuis le relevé : {faux}. "
            f"Un import qui suit un amont modifié sans le dire est pire "
            f"qu'un import qui s'arrête.")
    return versets


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", type=Path,
                    default=Path(__file__).resolve().parent.parent / "sources"
                            / "lat-vulgata")
    a = ap.parse_args()
    a.sortie.mkdir(parents=True, exist_ok=True)

    versets = lire()
    total_m = 0
    with (a.sortie / "ChazonEzra.jsonl").open("w", encoding="utf-8") as f:
        for ch, v, t in versets:
            mots = mots_du(t)
            total_m += len(mots)
            f.write(json.dumps({"ref": f"ChazonEzra.{ch}.{v}", "c": ch, "v": v,
                                "w": mots}, ensure_ascii=False,
                               separators=(",", ":")) + "\n")

    manif = a.sortie.parent / "MANIFEST.json"
    doc = json.loads(manif.read_text(encoding="utf-8")) if manif.is_file() \
        else {"sources": {}}
    ch, d, fin = LACUNE
    doc.setdefault("sources", {})["lat-vulgata"] = {
        "nom": "Liber Quartus Esdrae — la Vulgate clémentine",
        "langue": "lat",
        "temoin": "second degré : le latin traduit un grec perdu, qui "
                  "traduisait un hébreu perdu.",
        "texte": {"oeuvre": "Vulgata Clementina (1592), Liber Quartus Esdrae",
                  "licence": "domaine public"},
        "saisie": {"oeuvre": "Wikisource latin — transcription fidèle d'un "
                             "texte du domaine public",
                   "url": "https://la.wikisource.org/wiki/"
                          "Vulgata_Clementina/Liber_Quartus_Esdrae",
                   "licence": "domaine public (l'assise de 1592 le porte ; "
                              "une transcription fidèle ne crée pas de droit)"},
        "analyse": {"champ": None, "oeuvre": None,
                    "licence": "aucune — ce témoin ne porte pas de morphologie",
                    "copyleft": False},
        "attribution": "Vulgata Clementina (1592), domaine public ; "
                       "transcription de Wikisource latin.",
        "perimetre": "chapitres 3-14 seulement. Les ch. 1-2 et 15-16 sont des "
                     "additions chrétiennes hellénisées, écartées par le "
                     "critère d'inclusion de l'ONT.",
        "numerotation": "moderne, celle des éditions qui restaurent le "
                        "fragment (7:1-140). La Clémentine numérote 1-69 sans "
                        "trou ; la correspondance a été établie et appliquée : "
                        "7:1-35 inchangés, clémentine 36-68 décalés de +70 vers "
                        "106-138, et le dernier verset clémentin défusionné en "
                        "139+140 — il portait deux propositions et faisait 171 "
                        "signes contre 96 de moyenne. Décalage contrôlé sur "
                        "quatre ancres (36, 44, 50, 68 → 106, 114, 120, 138). "
                        "Les versets 36-105 n'existent pas dans ce fichier : "
                        "ils manquent au témoin latin.",
        "lacune": f"Le fragment de {d} à {fin} en numérotation moderne, soit "
                  f"{fin - d + 1} versets, est absent de tout manuscrit latin "
                  f"ordinaire : il en a été retranché au Moyen Âge parce qu'il "
                  f"refusait l'intercession pour les morts. Bensly l'a "
                  f"retrouvé en 1875 dans un manuscrit du IXᵉ siècle d'Amiens "
                  f"qui avait échappé au couteau, mais son édition n'existe "
                  f"qu'en fac-similé et son OCR est illisible. Le syriaque, "
                  f"lui, n'a jamais subi cette censure.",
        "totaux": {"livres": 1, "versets": len(versets), "mots": total_m,
                   "chapitres": len(PERIMETRE)},
        "livres": {"ChazonEzra": {"ont": 42, "slug": "chazon-ezra",
                                  "versets": len(versets), "mots": total_m,
                                  "chapitres": len(PERIMETRE)}},
    }
    manif.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8")

    print(f"{len(PERIMETRE)} chapitres (3-14)  {len(versets)} versets  "
          f"{total_m} mots")
    print(f"lacune déclarée : {fin - d + 1} versets ({ch}:{d}-{fin} en "
          f"numérotation moderne) absents du témoin latin")
    print("numérotation moderne appliquée au ch. 7 — décalage +70 établi sur "
          "quatre ancres, dernier verset défusionné")
    return 0


if __name__ == "__main__":
    sys.exit(main())
