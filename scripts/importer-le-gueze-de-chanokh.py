#!/usr/bin/env python3
"""Récolte le guèze de 1 Chanokh (Dillmann 1851) et éprouve son découpage.

    ./importer-le-gueze-de-chanokh.py --sortie <dossier>

## La permission, et ce qu'elle engage

Le texte vient de la saisie Unicode de Ran HaCohen (2011), faite d'après la
numérisation de Michal Jerabek (1995) de l'édition de Dillmann (Leipzig, 1851).

L'assise est du domaine public, mais la page portait une notice non-commerciale.
**Ran HaCohen a donné son accord le 1er septembre 2026**, à une condition qu'il
faut tenir : ==« that you keep me posted about your project »==. C'est une
obligation continue, sans échéance qui la rappellerait — lui écrire aux étapes
qui se voient, et lui rendre ce que la lettre promettait : les fautes de
transcription trouvées, et la comparaison des divisions de versets.

## Un témoin de second degré, et il faut le dire

Le guèze n'est pas la langue de ce livre. *1 Chanokh* a été composé en araméen,
traduit en grec, puis du grec en guèze. ==Partout où l'araméen de Qumrân
subsiste, c'est lui qui prime== — c'est le critère d'inclusion de l'ONT, et le
guèze n'est ici que le seul témoin *complet*.

## Le découpage en versets n'est pas donné — il est déduit, donc éprouvé

Les pages ne portent qu'un numéro de chapitre. Le seul repère interne est le
`።`, point final éthiopien. Il coïncide avec la division en versets parce que
la numérotation moderne en a été tirée — mais coïncider n'est pas être, et un
découpage juste 99 fois sur 100 produit une sortie bien formée et fausse.

La mesure, faite contre les divisions du guèze de Knibb (comptées, jamais
copiées — un compte est un fait) : ==66 chapitres concordants sur 71==, et les
cinq écarts valent tous ±1 verset.
"""
import argparse, html, json, os, re, sys, time, urllib.request
from pathlib import Path

BASE = "https://www.tau.ac.il/~hacohen/Henoch/Henoch%20{}.html"
CHAPITRES = 108
# Les cinq chapitres où la ponctuation de Dillmann s'écarte de la division
# reçue. Résolus le 1er septembre 2026 par alignement mot à mot.
#
# La division retenue est ==celle de Charles 1906==, du domaine public, qui
# s'accorde avec Knibb sur ces cinq chapitres. Ce n'est pas un choix
# d'érudition : un numéro de verset est un ==système de renvoi==, et « Chanokh
# 26:4 » doit désigner la même chose ici et partout ailleurs. La ponctuation de
# Dillmann n'est pas perdue pour autant — chaque verset porte le nombre de `።`
# qu'il contient réellement.
#
# Les ancres sont prises dans le texte de Dillmann lui-même, jamais chez Knibb,
# qui n'a servi qu'à localiser mécaniquement les frontières.
#
# Contrôle indépendant : cinq des sept coupures s'ouvrent sur ወ (wa-, « et »).
# Sur les 1 054 segments du livre, un début de verset commence par ወ dans 77 %
# des cas contre 19 % pour un mot quelconque — les coupures proposées se
# comportent donc comme de vrais débuts de verset.
# ── État de la vérification, au 1er septembre 2026 ────────────────────────
#
# 1 054 segments bruts → ==1 061 versets== après 14 corrections sur 7 chapitres.
#
# ch. 1-71    contrôlés contre la division du guèze de Knibb, comptée et non
#             copiée. Les 5 écarts sont résolus par alignement mot à mot.
# ch. 72-108  le fichier de Knibb s'arrête au 71. Contrôlés contre Charles
#             1906, d'abord par sa traduction anglaise, puis — pour les cas
#             durs — ==en lisant ses planches guèze== sur le site de HaCohen.
#
# ==Ne reste ouvert que le ch. 93== — et il est douteux qu'il soit un défaut.
#
# ## Le ch. 98 n'en était pas un, et ce qu'il a appris vaut mieux que lui
#
# L'anglais de Charles y compte 16 versets, nous 15. Ses planches guèze en
# donnent ==15== : la planche 205 passe de son « 15. » directement à « XCIX. ».
# Notre verset 15 se ferme sur `ወኢይከውን ፡ ሎሙ ፡ ሰላም ፡ አላ ፡ ሞተ ፡ ይመውቱ ፡ ፍጡነ ።`
# — « il n'y aura pas de paix pour eux, mais ils mourront d'une mort soudaine »
# —, qui est mot pour mot son verset 16 anglais. Aucune correction n'est due.
#
# Donc : ==la traduction anglaise de Charles et son édition guèze ne divisent
# pas identiquement.== Le même homme, deux ouvrages, deux découpages.
#
# Ça ne condamne pas la vérification des ch. 72-108 — quand l'anglais a
# signalé quelque chose, il avait raison deux fois sur trois (103 et 108 oui,
# 98 non) — mais ça la ==dégrade d'autorité à indice==. Il reste un risque
# symétrique qu'on ne peut pas écarter sans lire les 37 séries de planches :
# un chapitre où notre compte et l'anglais s'accordent pendant que le guèze
# de Charles, lui, divise autrement.
#
# Les ch. 20, 37, 51 et 60 ne sont PAS des défauts : notre texte y suit
# exactement Knibb, et c'est Charles qui diverge d'un verset. Deux éditions
# critiques qui s'écartent, c'est l'ordinaire — le ch. 20 en est le cas connu,
# Charles y comptant un archange de plus.
#
# Le ch. 93 est probablement un faux écart lui aussi : Charles y déplace
# 91:11-17, l'Apocalypse des Semaines, donc les deux éditions n'y rangent pas
# la même matière.
#
# ## Ce que les planches ont appris
#
# Les éditions de Flemming et de Charles ne sont sur ce site que des images.
# Elles restent lisibles pour ce qu'on leur demande : Charles ==imprime ses
# numéros de verset dans le guèze==, et l'en-tête courant de chaque page donne
# sa plage (« CVIII. 3-7. »). On n'a pas besoin d'un OCR du guèze pour savoir
# où tombe une frontière — il suffit de regarder la planche.
#
# ## Le lecteur de Charles a menti quatre fois avant de dire vrai
#
# Chiffres du récit pris pour des versets, titres indentés, « LXXXVIII » à
# huit signes quand le motif s'arrêtait à sept, intertitres injectant leur
# plage dans le chapitre précédent. Chaque version rendait un tableau propre
# et faux. Il n'a été retenu qu'après calibrage sur les 70 chapitres dont
# Knibb donne la réponse. ==On ne mesure pas l'inconnu avec un instrument
# qu'on n'a pas éprouvé sur du connu.==
CORRECTIONS = {
    14: [("couper", "ራእይ", "አነ"), ("couper", "ሰማይ", "ወቦእኩ"), ("fusionner", 7)],
    26: [("couper", "ደብር", "ወመንገለ")],
    30: [("couper", "ዘኢይትዌዳዕ", "ወርኢኩ")],
    61: [("couper", "ዕለት", "ወይነሥኡ")],
    69: [("couper", "ማያት", "እምፍጥረተ"), ("couper", "ዐቢየ", "ወባረኩ"),
         ("fusionner", 18), ("fusionner", 25), ("fusionner", 29)],
    # 103 et 108 : résolus le 1er septembre en lisant les planches de
    # l'édition guèze de Charles 1906, sur le site même de HaCohen. Elles ne
    # sont que des images — mais Charles ==imprime ses numéros de verset dans
    # le guèze==, et l'en-tête courant donne la plage de chaque page. Il suffit
    # donc de regarder.
    #
    # Les deux chapitres tiennent au même fait : Dillmann marque ces
    # frontières-là d'un `፤` et non d'un `።`. Attention, ==ce n'est pas une
    # règle générale== : découper sur tous les `፤` du livre fait tomber
    # l'accord de 66/71 à 44/71. Le `፤` propose un candidat ; la planche
    # tranche.
    103: [("couper_aux_points_virgules", 1)],
    108: [("couper_aux_points_virgules", 6),
          ("couper_aux_points_virgules", 2)],
}


def recolter(n: int, cache: Path) -> str:
    f = cache / f"{n}.html"
    if not f.exists():
        f.write_bytes(urllib.request.urlopen(BASE.format(n), timeout=30).read())
        time.sleep(0.25)
    return f.read_text(encoding="utf-8", errors="replace")


def decouper(page: str, n: int):
    """Rend les versets d'un chapitre, séparés sur le `።`."""
    # couper APRÈS le `>` du <p> porteur : sinon le CSS de la balise entre
    # dans le premier verset — il l'a fait, et le compte l'a montré.
    i = page.find("text-align:justify")
    if i < 0:
        raise ValueError(f"chapitre {n} : paragraphe de corps introuvable.")
    corps = page[page.index(">", i) + 1:]
    txt = html.unescape(re.sub(r"<[^>]+>", "", corps))
    txt = re.sub(r"^\s*\d+\s*", "", " ".join(txt.split()))
    versets = [' '.join(v.split()) + " ።" for v in txt.split("።")
               if any(0x1200 <= ord(c) <= 0x137F for c in v)]
    for op in CORRECTIONS.get(n, []):
        if op[0] == "couper":
            _, avant, apres = op
            for k, v in enumerate(versets):
                m = re.search(rf"{re.escape(avant)}\s*፡?\s*({re.escape(apres)})", v)
                if m:
                    i = m.start(1)
                    versets[k:k + 1] = [v[:i].strip(), v[i:].strip()]
                    break
            else:
                raise ValueError(f"chapitre {n} : ancre de coupure « {avant} | "
                                 f"{apres} » introuvable — le texte amont a bougé.")
        elif op[0] == "couper_aux_points_virgules":
            k = op[1] - 1
            morceaux = [m.strip() for m in versets[k].split("፤") if m.strip()]
            if len(morceaux) < 2:
                raise ValueError(f"chapitre {n} : le verset {op[1]} ne porte "
                                 f"aucun ፤ — le texte amont a bougé.")
            versets[k:k + 1] = morceaux
        else:
            k = op[1] - 1
            if k + 1 >= len(versets):
                raise ValueError(f"chapitre {n} : fusion {op[1]} hors limites.")
            versets[k:k + 2] = [versets[k] + " " + versets[k + 1]]

    if not versets:
        raise ValueError(f"chapitre {n} : aucun verset lu — un chapitre vide "
                         f"et bien formé ne se voit pas, on s'arrête ici.")
    return versets


def mots_du(verset: str):
    """Le guèze sépare ses mots par `፡`. On rend la même forme que les autres
    sources — `w` est partout une liste de mots, jamais un bloc — pour que la
    couche se lise d'une seule façon en aval."""
    return [{"t": m} for m in
            (x.strip() for x in verset.replace("።", " ").split("፡"))
            if any(0x1200 <= ord(c) <= 0x137F for c in m)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sortie", type=Path,
                    default=Path(__file__).resolve().parent.parent / "sources"
                            / "gez-dillmann")
    ap.add_argument("--cache", type=Path, default=Path("/tmp/chanokh-geez"))
    a = ap.parse_args()
    a.cache.mkdir(parents=True, exist_ok=True)
    a.sortie.mkdir(parents=True, exist_ok=True)

    total_v = total_c = total_m = 0
    with (a.sortie / "Chanokh.jsonl").open("w", encoding="utf-8") as out:
        for n in range(1, CHAPITRES + 1):
            versets = decouper(recolter(n, a.cache), n)
            for i, v in enumerate(versets, 1):
                total_v += 1
                total_c += sum(1 for c in v if 0x1200 <= ord(c) <= 0x137F)
                total_m += len(mots_du(v))
                out.write(json.dumps(
                    {"ref": f"Chanokh.{n}.{i}", "c": n, "v": i,
                     "w": mots_du(v)},
                    ensure_ascii=False, separators=(",", ":")) + "\n")

    # Entrée au manifeste, fusionnée : les trois autres sources y vivent et
    # sont gérées par un autre script.
    manif = a.sortie.parent / "MANIFEST.json"
    doc = json.loads(manif.read_text(encoding="utf-8")) if manif.is_file() else {"sources": {}}
    doc.setdefault("sources", {})["gez-dillmann"] = {
        "nom": "Maṣḥafa Henok — le guèze de Dillmann",
        "langue": "gez",
        "temoin": "second degré : le guèze traduit le grec, qui traduisait "
                  "l'araméen. Là où l'araméen de Qumrân subsiste, il prime.",
        "texte": {
            "oeuvre": "August Dillmann, Liber Henoch aethiopice (Leipzig, 1851)",
            "licence": "domaine public",
        },
        "saisie": {
            "oeuvre": "Michal Jerabek (1995), converti en Unicode par "
                      "Ran HaCohen (2011) — Biblia Aethiopica",
            "url": "https://www.tau.ac.il/~hacohen/",
            "licence": "usage non commercial",
            "permission": "accordée par Ran HaCohen le 1er septembre 2026, "
                          "à charge de le tenir informé du projet",
        },
        "analyse": {"champ": None, "oeuvre": None,
                    "licence": "aucune — ce témoin ne porte pas de morphologie",
                    "copyleft": False},
        "attribution": "Texte : August Dillmann, Liber Henoch aethiopice "
                       "(Leipzig, 1851), domaine public. Saisie : Michal "
                       "Jerabek (1995), Unicode par Ran HaCohen (2011), "
                       "employée avec sa permission.",
        "decoupage": "déduit du ። puis corrigé — voir l'en-tête du script",
        "totaux": {"livres": 1, "versets": total_v, "mots": total_m,
                   "chapitres": CHAPITRES},
        "livres": {"Chanokh": {"ont": 38, "slug": "chanokh", "versets": total_v,
                               "mots": total_m, "chapitres": CHAPITRES}},
    }
    manif.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n",
                     encoding="utf-8")

    print(f"{CHAPITRES} chapitres  {total_v} versets  {total_m} mots  "
          f"{total_c} caractères guèze")
    corriges = sum(len(v) for v in CORRECTIONS.values())
    print(f"{corriges} corrections de frontière appliquées sur "
          f"{len(CORRECTIONS)} chapitres : {', '.join(f'ch.{k}' for k in CORRECTIONS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
