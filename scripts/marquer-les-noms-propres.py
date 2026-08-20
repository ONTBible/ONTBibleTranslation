#!/usr/bin/env python3
"""Marque tous les noms propres du vault en `==Nom==` — §2.5 bis généralisé.

## Pourquoi

Le §2.5 bis prévoyait déjà `==Chavah==`, `==Noach==` pour « un nom propre dont
le verset explique l'étymologie ». La règle est **généralisée** : tout nom
propre porte la marque, à **toutes** ses occurrences, corps du texte et gloses
comprises.

Rien à changer en aval : le pipeline lit déjà `==…==` comme un terme important,
l'app le rend en bordeaux (`#862742` clair / `#D87994` sombre) et le site
aussi. Le vault est le seul dépôt touché.

## Ce que le script ne touche jamais

L'ordre des zones protégées est celui du tokeniseur du pipeline
(`pipeline/src/inline.rs`), et c'est ce qui rend l'opération sûre :

- `**Shem**` — un intraduisible reste un intraduisible. C'est ce qui règle
  l'homographie sans avoir à la deviner : `Shem` le fils de Noach est nu dans
  le texte et sera marqué ; `**Shem**` l'acte d'existence est déjà balisé,
  donc protégé. Idem pour `adam`, `Ish`, `She'ol`.
- `(*Noach* / נֹחַ)` — le niveau 3 porte déjà le nom, le marquer une seconde
  fois ferait deux signaux pour une information.
- `==Noach==` — déjà marqué. Le script est **idempotent** : on peut le relancer
  après chaque nouveau chapitre sans rien doubler.
- les titres, le sous-titre de référence, le pied de version.

## Les gloses, elles, sont marquées

Décision explicite de l'auteur, le 19 août 2026. La glose cite beaucoup de
noms pour situer les personnages, et un lecteur qui y retrouve la même couleur
que dans le corps n'a pas à se demander s'il s'agit du même Cham.

    ./scripts/marquer-les-noms-propres.py            # simulation, n'écrit rien
    ./scripts/marquer-les-noms-propres.py --ecrire
"""

import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
GLOSSAIRE = RACINE.parent / "ONTBibleApp" / "dist" / "glossary.json"
DOSSIERS = ("locked", "brouillons", "in-writing")

# Les noms de livres ne sont pas des personnages : dans une glose, « en
# Bereshit 3 » est une référence bibliographique, pas une entrée en scène.
# *Khanokh* n'y figure pas — c'est d'abord le patriarche de Bereshit 5, et le
# livre porte son nom parce qu'il le porte.
LIVRES = {
    "Bereshit", "Shemot", "Vayiqra", "Bemidbar", "Devarim", "Tehilim",
    "Mishlei", "Iyov", "Ruth", "Qohelet", "Esther", "Shoftim", "Yehoshua",
    "Yeshayahu", "Yirmeyahu", "Yehezqel", "Zekharyah", "Nahum", "Havaquq",
    "Ovadyah", "Yovelim", "Kenesset", "Torah", "Nistarot", "Nevi'im",
    "Ketouvim", "Berit Hadashah", "Besorot", "Igerot", "Tanakh",
    "Sefar Gibbaraya", "Toledot Adam ve-Chavah", "Chazon Avraham",
    "Chazon Ezra", "Chazon Barukh", "Machazeh Yohanan", "Divrei Hayamim",
    "Shir Hashirim", "Ezra-Nehemyah", "Tsava'at Lévi",
}

# Deux noms que la machine ne peut pas trancher, et qu'elle ne doit donc pas
# toucher. `Shem` est le fils de Noach **et** l'acte d'existence
# fonctionnelle ; `Adam` est le personnage de *Toledot* **et** l'intraduisible
# de *Bereshit* 8+. La casse ne les sépare pas : les deux s'écrivent
# capitalisés, et 130 occurrences nues mélangent les deux sens — dont des
# gloses qui *définissent* l'intraduisible sans le baliser.
#
# Les marquer en masse donnerait du bordeaux à des intraduisibles, c'est-à-dire
# exactement l'inverse de ce que la marque veut dire. C'est un arbitrage
# verset par verset, et il appartient à l'auteur. Le script les compte et le
# dit plutôt que de deviner.
AMBIGUS = {"Shem", "Adam"}

# Un caractère de mot, apostrophes et trait d'union compris : c'est ce qui
# empêche `Qayin` de mordre dans `Tuval-Qayin`, et `Aza` dans `Azazel`.
MOT = r"[^\W\d_]|['’\-]"

# Le niveau 3 — `(*noach* / נֹחַ)`. La barre oblique interne est admise : elle
# sépare deux graphies d'un même nom, `(*Hahyah/Ahyah* / ההיה)`.
NIVEAU_3 = re.compile(r"\(\*([^*]+?)\*\s*/\s*[^)]+\)")

# Les mots français capitalisés que la seconde source ramasse et qui ne sont
# pas des noms propres. Ils portent la majuscule pour une autre raison :
# l'ONT nomme solennellement quelques réalités du récit — les Cieux, la Voûte,
# l'Orient —, et le §2.5 bis leur réserve la marque au cas par cas, pas en
# masse. « Saint » et « Roi » sont des qualités, « Pharaon » une fonction.
#
# Cette liste n'existe que pour ce que la garde ci-dessous ne peut pas voir :
# un mot qui ne paraît jamais en minuscule dans tout le corpus.
CONCEPTS = {
    "Cieux", "Voûte", "Orient", "Saint", "Pharaon", "Arche", "Alliance",
    # Des ouvertures de phrase que la garde ne voit pas : elles ne paraissent
    # jamais en minuscule parce qu'elles n'ouvrent que des phrases.
    "Cependant", "Sépare-toi", "Vraiment", "Seulement", "Faisons",
}

# Les gentilés sont des noms propres — arbitrage de l'auteur, 20 août 2026.
#
# Ils avaient été mis de côté un temps : « Hittite » se devine à peu près là où
# « Mitsrayim » ne se devine pas, et les colorer double la surface bordeaux
# d'une table des nations. L'auteur a tranché dans l'autre sens, et **sans
# exception** — un peuple est une entité du récit au même titre qu'un homme ou
# qu'un lieu, et le lecteur qui ne sait pas ce qu'est un Yevousite est
# précisément celui pour qui la marque existe.
#
# Ils n'ont donc plus de traitement propre. Cette note reste pour dire que
# l'absence de liste est une décision, et non un oubli.

# Les noms propres que la garde des minuscules écarte à tort.
#
# Elle demande au corpus si le mot paraît jamais en minuscule. « Ai » et
# « Moreh » y paraissent — mais dans une italique mal fermée et dans
# `l'*elon moreh*`, jamais comme mots ordinaires. La garde est bonne ; ce sont
# ses deux seuls faux négatifs, et les écrire ici coûte moins que de
# l'affaiblir pour tout le reste.
NOMS_FORCÉS = {"Ai", "Moreh"}


def noms_propres() -> list[str]:
    """Les noms propres du vault, relevés par leur niveau 3 capitalisé.

    C'est la marque que le §4.12 impose à chaque nom propre : le relevé suit
    donc la règle du vault au lieu d'une liste tenue à la main, qui serait
    périmée au prochain chapitre.
    """
    trouves = set()
    adjacents = set()
    for f in fichiers():
        texte = f.read_text()
        for m in NIVEAU_3.finditer(texte):
            # Le composé `(*Hahyah/Ahyah* / ההיה)` porte deux graphies d'un
            # même nom. L'ancien motif refusait la barre oblique et ne voyait
            # donc ni l'une ni l'autre : 24 occurrences sont restées nues.
            for graphie in m.group(1).split("/"):
                mot = graphie.strip()
                if mot[:1].isupper():
                    trouves.add(mot)
            # Le mot capitalisé **collé au niveau 3**. C'est la seconde source,
            # et elle rattrape ce que la première ne peut pas voir :
            #
            # - le niveau 3 en minuscule, parce qu'il porte la forme fléchie —
            #   `le Yarden (*hayarden* / …)`, `en Eden (*be'eden* / …)` ;
            # - la graphie du corps qui diffère de celle du niveau 3 —
            #   `Ishma'el (*Yishma'el* / …)`, `le Prat (*perat* / …)`.
            #
            # Elle est fondée : le §4.12 impose un niveau 3 à la première
            # occurrence de tout nom propre. Le mot qui le précède **est** le
            # nom, dans la graphie que le lecteur lira.
            avant = texte[max(0, m.start() - 40):m.start()].rstrip()
            if colle := re.search(rf"((?:{MOT})+)$", avant):
                if colle.group(1)[:1].isupper():
                    adjacents.add(colle.group(1))

    # Les intraduisibles sont déjà en `**…**` et ont leur fiche : les marquer
    # ici leur retirerait l'or, donc la promesse d'une explication.
    intraduisibles = set()
    if GLOSSAIRE.exists():
        données = json.loads(GLOSSAIRE.read_text())
        entrées = données.get("entries", données) if isinstance(données, dict) else données
        for e in entrées:
            lemme = (e.get("lemma") or "").lower()
            intraduisibles.add(lemme)
            for forme in e.get("forms") or []:
                intraduisibles.add(forme.lower())

    # Ce qui s'écrit aussi en minuscule n'est pas un nom propre.
    #
    # La seconde source ramasse tout mot capitalisé collé à un niveau 3 —
    # « les Cieux (*hashamayim* / …) » aussi bien que « le Yarden (*hayarden*
    # / …) ». Plutôt qu'une liste de mots français à tenir à jour, on demande
    # au corpus : « Terre », « Jardin », « Vie » y paraissent en minuscule ;
    # « Yarden », « Eden », « Ishma'el » jamais. La majuscule de début de
    # phrase tombe par la même règle — « Vraiment », « Cependant », « Un ».
    #
    # Les zones protégées sont retirées d'abord : le niveau 3 porte la
    # translittération en minuscule — `(*be'eden* / …)` — et compterait « Eden »
    # comme un mot ordinaire.
    minuscules = set()
    for f in fichiers():
        libre = PROTÉGÉ_MINUSCULE.sub(" ", f.read_text())
        minuscules |= {m.group(0).replace("’", "'").lower()
                       for m in re.finditer(rf"(?<!{MOT})(?:{MOT}){{2,}}(?!{MOT})", libre)
                       if m.group(0)[:1].islower()}

    retenus_adjacents = {
        n for n in adjacents
        if n.replace("’", "'").lower() not in minuscules
        and n not in CONCEPTS
        or n in NOMS_FORCÉS
        and "'" not in n[:2] and "’" not in n[:2]   # l'élision : « L'arc », « J'ai »
    }
    écartés = sorted(adjacents - retenus_adjacents - trouves)
    trouves |= retenus_adjacents

    gardés = [
        n for n in trouves
        if n not in LIVRES
        and n not in AMBIGUS
        and n.lower() not in intraduisibles
        # Un composé dont chaque membre est un nom divin — « YHWH Elohim » —
        # est un intraduisible en deux mots, pas un nom propre.
        and not all(p.lower() in intraduisibles for p in n.split())
    ]
    # Le plus long d'abord : « Ur Kasdim » avant « Ur », « Tuval-Qayin » avant
    # « Qayin ». Sinon le court mord dans le long et le casse en deux.
    return sorted(gardés, key=lambda n: (-len(n), n)), écartés


def fichiers() -> list[pathlib.Path]:
    out = []
    for d in DOSSIERS:
        out += sorted((RACINE / d).rglob("*.md")) if (RACINE / d).exists() else []
    return out


# Les zones que le script traverse sans y toucher. L'ordre reproduit celui du
# tokeniseur : le niveau 3 et l'intraduisible commencent tous deux par un
# caractère que l'italique revendique aussi.
# Pour le relevé des minuscules seulement : l'italique simple est ajouté, car
# le niveau 3 et les gloses y logent les translittérations.
PROTÉGÉ_MINUSCULE = re.compile(
    r"\(\*[^*]+?\*\s*/\s*[^)]+\)|\*\*.+?\*\*|\*[^*\n]+?\*|\[\[.+?\]\]"
)

PROTÉGÉ = re.compile(
    # Le niveau 3, barre oblique interne comprise. Elle était exclue ici alors
    # que la détection l'accepte : `(*Hahyah/Ahyah* / ההיה)` n'était donc pas
    # protégé, et le script est allé marquer à l'intérieur du niveau 3.
    r"\(\*[^*]+?\*\s*/\s*[^)]+\)"    # (*Noach* / נֹחַ)   — le niveau 3
    r"|\*\*.+?\*\*"                  # **Shem**            — l'intraduisible
    r"|==.+?=="                      # ==Noach==           — déjà marqué
    r"|\[\[.+?\]\]"                  # [[lien]]
    # Un titre de livre en deux mots dont le premier est aussi un lieu :
    # `Sefar Gibbaraya` porte le nom du port d'Arabie de *Bereshit* 10:30.
    # Sans cette zone, le titre du livre sort colorié sur son premier mot.
    + "|" + "|".join(re.escape(l) for l in sorted(LIVRES, key=len, reverse=True))
)


def marquer_ligne(ligne: str, motif: re.Pattern) -> tuple[str, int]:
    """Marque les noms d'une ligne, en sautant les zones protégées."""
    out, i, n = [], 0, 0
    for zone in PROTÉGÉ.finditer(ligne):
        libre, compte = motif.subn(r"==\g<0>==", ligne[i:zone.start()])
        out.append(libre)
        out.append(zone.group())
        n += compte
        i = zone.end()
    libre, compte = motif.subn(r"==\g<0>==", ligne[i:])
    out.append(libre)
    return "".join(out), n + compte


def main() -> None:
    ecrire = "--ecrire" in sys.argv
    noms, écartés = noms_propres()
    print(f"{len(noms)} noms propres relevés\n")

    motif = re.compile(
        rf"(?<!{MOT})(?:" + "|".join(re.escape(n) for n in noms) + rf")(?!{MOT})"
    )

    total, touches = 0, 0
    for f in fichiers():
        lignes = f.read_text().split("\n")
        sorties, compte = [], 0
        for ligne in lignes:
            nu = ligne.lstrip()
            # Titres, sous-titre de référence, séparateurs, pied de version :
            # la couleur y serait un ornement, pas une information.
            if (
                nu.startswith(("#", "---", "*(", "> "))
                or not nu
                or "— Version" in ligne
                or "à valider" in ligne
            ):
                sorties.append(ligne)
                continue
            marquee, n = marquer_ligne(ligne, motif)
            sorties.append(marquee)
            compte += n
        if compte:
            touches += 1
            total += compte
            print(f"  {compte:>5}  {f.relative_to(RACINE)}")
            if ecrire:
                f.write_text("\n".join(sorties))

    print(f"\n{total} marques dans {touches} fichiers")

    nus = {n: 0 for n in AMBIGUS}
    for f in fichiers():
        for ligne in f.read_text().split("\n"):
            reste = PROTÉGÉ.sub("", ligne)
            for n in AMBIGUS:
                nus[n] += len(re.findall(rf"(?<!{MOT}){re.escape(n)}(?!{MOT})", reste))
    print("\nlaissés à l'auteur — nom propre ou intraduisible selon le verset :")
    for n, c in sorted(nus.items()):
        print(f"  {n:<8} {c} occurrences nues")
    # Ce que le script écarte, il le dit. Un relevé qui se tait sur ses
    # refus se lit comme une couverture complète — c'est exactement ainsi que
    # Yarden, Eden et Ishma'el sont restés nus sans que rien ne le signale.
    if écartés:
        print("\nécartés — capitalisés près d'un niveau 3, non retenus :")
        print("  " + ", ".join(écartés))
        print("  (concept français ou ouverture de phrase — à verser dans"
              " NOMS_FORCÉS si l'un d'eux est bien un nom propre)")
    if not ecrire:
        print("simulation — relancer avec --ecrire pour appliquer")


main()
