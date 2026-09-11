#!/usr/bin/env python3
"""Chaque niveau 3 cite de l'hébreu. Est-il dans LE verset où il est accroché ?

    ./eprouver-les-citations.py

## Ce que ce contrôle ajoute au précédent

Un premier balayage demandait seulement si le mot cité ==existait quelque part==
dans le corpus hébreu. Celui-ci demande s'il est ==au bon endroit==.

Le second défaut est le plus insidieux des deux : une citation exacte accrochée
au mauvais verset ==a l'air juste partout où on la contrôle==. Elle passe la
relecture, elle passe la recherche, elle ne se voit qu'en ouvrant le verset.

## La jointure est positionnelle, jamais par numéro

Le §2.2 fait repartir la numérotation à ¹ quand un chapitre biblique commence au
milieu d'une **parashah**. Une unité qui couvre *Bereshit* 7-8 porte donc ==deux
versets numérotés ¹==. C'est la ==position== qui joint, et le contrôle
==s'abstient== plutôt que de joindre de travers : si le compte des versets ONT
diffère du compte des versets bibliques, l'unité est écartée et dite.

## Trois gravités, et une seule demande un arbitrage

- ==graphie== — pleine contre défective. Le mot est le bon, un vav ou un yod
  diffère. Se corrige sans décision.
- ==flexion== — construit, suffixe, hé directionnel, ou lemme non déclaré. La
  citation donne le mot du dictionnaire là où le verset le fléchit. C'est
  souvent ==légitime==, et le §4.1 le prévoit : la glose ramène à la racine.
- ==ABSENT== — aucun mot du verset ne partage trois consonnes consécutives avec
  la citation. ==C'est là que sont les fautes.==

## L'instrument s'éprouve avant de servir, et refuse de tourner sinon

Quatre témoins dont deux doivent être signalés. Ce n'est pas une précaution de
style : la version précédente de ce balayage, « améliorée » par une tolérance
aux sous-chaînes, avait déclaré attestés ==deux mots hébreux inventés pour
l'occasion==. Un instrument plus fin n'est pas un instrument plus juste, et le
seul garde-fou est de le passer sur un cas dont on connaît la réponse.

## La limite du classement, et elle est réelle

Le classement mesure ==à quelle distance== la citation est du verset, jamais
si l'écart est ==licite==. Les deux ne coïncident pas :

`rovetset` en *Bereshit* 4:7 est rangé en **flexion** — il partage sa racine
avec le `rovets` du verset. Et c'est pourtant une faute grave : le verset porte
le ==masculin==, la citation met le ==féminin==, et ce faisant elle efface le
désaccord grammatical le plus commenté du chapitre.

À l'inverse, une citation rangée en **flexion** parce qu'elle donne le lemme là
où le verset fléchit est parfaitement juste, et le §4.1 la prévoit.

**Donc `flexion` ne se lit pas comme « rien à voir ».** Elle se lit comme « un
œil humain doit trancher ». Seules `ABSENT` et `EMPRUNT` se suffisent à
elles-mêmes.

## Ce qu'il ne couvre pas

Seul *Bereshit* est joignable : les autres livres écrits — *Sefar Gibbaraya*,
*Toledot Adam ve-Chavah*, *Chazon Avraham* — ==ne sont pas dans le texte
massorétique==, et leur hébreu n'a donc rien à quoi se comparer.
"""
import json, re, glob, os, sys, unicodedata
from collections import defaultdict

EXPO = {"⁰":"0","¹":"1","²":"2","³":"3","⁴":"4","⁵":"5","⁶":"6","⁷":"7","⁸":"8","⁹":"9"}
NIV3 = re.compile(r"\(\*([^*()]+)\*\s*/\s*([^)]*[א-ת][^)]*)\)")
SEP  = re.compile(r"[\s־\-–—]+")
PREF = "והבכלמש"
# `*(Genèse / בְּרֵאשִׁית 4)*` · `… 10:1-32)*` · `… 1:1 — 2:3)*`
SOUS = re.compile(r"^\*\(\s*Gen[èe]se\s*/\s*[^0-9]*?"
                  r"(\d+)(?::(\d+))?\s*(?:[-—–]\s*(\d+)(?::(\d+))?)?\s*\)\*", re.M)

# **Les cinq finales sont d'autres caractères.** `ך ם ן ף ץ` ne sont pas
# `כ מ נ פ צ` pour Unicode, et l'hébreu bascule de l'une à l'autre selon la
# position dans le mot. `מִצְרַיִם` finit par un mem final ; `מִצְרַיְמָה`,
# le même nom avec le hé directionnel, porte au même endroit un mem médial.
# Sans cette table, les deux ne se reconnaissent pas — et une citation
# parfaitement juste remonte en « empruntée au verset voisin ».
FINALES = str.maketrans("ךםןףץ", "כמנפצ")

def cons(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^א-ת]", "", s).translate(FINALES)

# Les mots hébreux que le §3 déclare : un niveau 3 qui les cite donne le terme,
# non la forme du verset. C'est la convention du §2.5 — « le gras EST la
# translittération exacte » —, pas un écart.
LEMMES = set()
for ligne in open("CLAUDE.md", encoding="utf-8").read().splitlines():
    cases = [c.strip() for c in ligne.split("|")]
    if len(cases) < 5:
        continue
    heb = cases[1]
    # Une case peut porter deux formes — « אִשָּׁה / אִישׁ ». Exiger que la
    # case entière soit de l'hébreu les rejetait toutes les deux, et `ish` et
    # `ishah` remontaient alors comme fautes dans huit versets.
    if heb and all("\u0590" <= c <= "\u05ff" or c.isspace() or c in "/,·"
                   for c in heb):
        for mot in re.split(r"[\s/,·]+", heb):
            LEMMES.add(re.sub(r"[^\u05d0-\u05ea]", "",
                       "".join(c for c in unicodedata.normalize("NFD", mot)
                               if not unicodedata.combining(c))))
LEMMES.discard("")

# ── le texte hébreu, verset par verset ────────────────────────────────────────
VERSETS = {}
for l in open("sources/he-wlc/Gen.jsonl", encoding="utf-8"):
    d = json.loads(l)
    VERSETS[(d["c"], d["v"])] = {cons(w["t"]) for w in d["w"] if cons(w["t"])}
CHAPITRES = defaultdict(list)
for (c, v) in sorted(VERSETS):
    CHAPITRES[c].append(v)

def porte(ref, c):
    """Le verset porte-t-il ce mot ?

    **Généreux à dessein.** Tout ce que ce test refuse tombe dans le
    classement, où il risque d'être rangé sous une étiquette qui ne lui va pas.
    Un mot présent sous une forme fléchie doit donc passer ici, pas plus loin :

    - ==proclitique== des deux côtés — `ha-`, `be-`, `le-`, `me-` ;
    - ==suffixe pronominal== — le verset écrit `beiti`, la citation `bayit` ;
    - ==hé directionnel== — le verset écrit `Mitsraymah`, la citation
      `Mitsrayim` ;
    - ==pleine contre défective== — un vav ou un yod d'écart.

    Sans ces quatre tolérances, des citations parfaitement justes remontaient
    en « empruntées au verset voisin » : le mot était pourtant sous les yeux,
    fléchi.
    """
    mots = VERSETS.get(ref, set())
    if c in mots:
        return True

    def variantes(x):
        out = {x}
        for k in (1, 2):
            if len(x) > k + 1 and all(y in PREF for y in x[:k]):
                out.add(x[k:])
        if x.endswith("ה") and len(x) > 3:      # hé directionnel ou final
            out.add(x[:-1])
        return out

    def squelette(x):
        return x.replace("ו", "").replace("י", "")

    for m in mots:
        for a in variantes(m):
            for b in variantes(c):
                if a == b:
                    return True
                if a.startswith(b) and 0 < len(a) - len(b) <= 2:
                    return True      # le verset fléchit ce que la citation lemmatise
                if squelette(a) == squelette(b) and len(squelette(b)) >= 3 \
                        and abs(len(a) - len(b)) <= 2:
                    return True      # pleine contre défective
    return False

def voisin(ref, c, portee=4):
    """La forme est-elle dans un verset VOISIN du même chapitre ?

    C'est le discriminant que la réduction au lemme n'explique pas. Une glose
    qui ramène à la racine cite ==le mot du dictionnaire== : il n'a aucune
    raison d'être justement au verset d'à côté. Une citation empruntée au
    contexte, si.

    Le témoin est *Bereshit* 15:3 — le corpus y cite `יִירַשׁ`, que le verset
    n'a pas et que **15:4 porte**. Deux versets, deux personnages : celui
    qu'Avram redoute et celui que **YHWH** annonce.
    """
    c1, v1 = ref
    for v in range(max(1, v1 - portee), v1 + portee + 1):
        if v == v1:
            continue
        for m in VERSETS.get((c1, v), set()):
            # Le voisin peut porter un proclitique devant, un suffixe
            # pronominal derrière, ou les deux. Le témoin l'exige : la forme
            # citée en 15:3 est `יִירַשׁ`, et 15:4 porte `יִירָשְׁךָ` — même
            # mot, plus un `ךָ`. Exiger l'égalité stricte faisait manquer le
            # seul cas dont on connaisse la réponse.
            for k in (0, 1, 2):
                if k and not (len(m) > k + 1 and all(x in PREF for x in m[:k])):
                    continue
                n = m[k:]
                if n == c or (n.startswith(c) and 0 < len(n) - len(c) <= 2):
                    return (c1, v)
    return None


def classer(ref, c):
    """Toutes les absences ne se valent pas — trois gravités, et une seule
    demande un arbitrage."""
    mots = VERSETS.get(ref, set())
    # **L'emprunt se teste en premier.** Il est plus spécifique que tout le
    # reste, et il est fautif là où les autres classes sont souvent justes.
    if voisin(ref, c):
        return "EMPRUNT"

    # **Pleine contre défective, mais pas à n'importe quel prix.** Retirer tous
    # les vav et les yod réduit `יוֹרֵשׁ` et `יִירַשׁ` à deux lettres — et les
    # déclare identiques, alors que l'un est un participe et l'autre un
    # inaccompli. On exige donc trois consonnes de reste et une longueur
    # voisine : un vav ou un yod de différence, pas trois.
    def squelette(x):
        return x.replace("ו", "").replace("י", "")
    for m in mots:
        sm, sc = squelette(m), squelette(c)
        if sm == sc and len(sc) >= 3 and abs(len(m) - len(c)) <= 2:
            return "graphie"
    # **Trois consonnes consécutives partagées suffisent.** Comparer des
    # préfixes ne marche pas : le hé directionnel — `Mitsraymah` pour
    # `Mitsrayim`, `hanegbah` pour `hanegev` — s'ajoute à la FIN, et le
    # dépouillement de proclitiques ne l'atteint jamais. Il faisait passer pour
    # « absentes » des citations qui ne diffèrent que par un suffixe de
    # direction.
    for m in mots:
        if any(c[i:i+3] in m for i in range(len(c) - 2)):
            return "flexion"          # construit, suffixe, direction, lemme
    return "ABSENT"                   # aucun mot du verset ne partage sa racine

def plage(m):
    """Le sous-titre donne la suite des versets bibliques couverts."""
    c1 = int(m.group(1)); v1 = int(m.group(2)) if m.group(2) else None
    g3 = int(m.group(3)) if m.group(3) else None
    v2 = int(m.group(4)) if m.group(4) else None
    if v1 is None:                       # « Genèse 5 » — le chapitre entier
        return [(c1, v) for v in CHAPITRES[c1]]
    # **Ce qui suit le tiret est un verset, sauf s'il porte lui-même un `:`.**
    # « 10:1-32 » = versets 1 à 32 du chapitre 10 ; « 1:1 — 2:3 » traverse.
    # Les lire pareil faisait bâtir vingt-deux chapitres au lieu d'un, et le
    # garde-fou de longueur écartait alors treize chapitres sur dix-neuf.
    if v2 is None:
        fin = g3 if g3 is not None else v1
        return [(c1, v) for v in CHAPITRES[c1] if v1 <= v <= fin]
    c2 = g3
    out = [(c1, v) for v in CHAPITRES[c1] if v >= v1]     # « 1:1 — 2:3 »
    for c in range(c1 + 1, c2):
        out += [(c, v) for v in CHAPITRES[c]]
    out += [(c2, v) for v in CHAPITRES[c2] if v <= (v2 or CHAPITRES[c2][-1])]
    return out

def versets_ont(corps):
    """Découpe le corps aux exposants. Ils ne sont pas toujours en tête de
    ligne — un compteur qui l'a supposé a déjà sous-compté ici."""
    marques = [(m.start(), int("".join(EXPO[c] for c in m.group(0))))
               for m in re.finditer(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+", corps)]
    out = []
    for i, (pos, n) in enumerate(marques):
        fin = marques[i+1][0] if i+1 < len(marques) else len(corps)
        out.append((n, corps[pos:fin]))
    return out

def controler(chemin):
    t = open(chemin, encoding="utf-8").read()
    m = SOUS.search(t)
    if not m:
        return None
    ref = plage(m)
    vs = versets_ont(t[m.end():])
    # La numérotation repart à ¹ quand un chapitre biblique commence au milieu
    # d'une parashah (§2.2) : la suite des numéros n'est donc pas 1..N, et
    # c'est la POSITION qui joint, jamais le numéro affiché.
    if len(vs) != len(ref):
        return ("écarté", os.path.basename(chemin),
                f"{len(vs)} versets ONT contre {len(ref)} bibliques — jointure non sûre")
    mal = []
    lemmes = LEMMES
    for (n, corps), bib in zip(vs, ref):
        for mm in NIV3.finditer(corps):
            tr, heb = mm.group(1).strip(), mm.group(2).strip()
            absents = [w for w in SEP.split(heb)
                       if len(cons(w)) >= 3 and not porte(bib, cons(w))]
            absents = [w for w in absents if cons(w) not in LEMMES]
            for w in absents:
                mal.append((n, bib, tr, w, classer(bib, cons(w))))
    return ("ok", os.path.basename(chemin), mal)

# ── l'instrument s'éprouve avant de servir ────────────────────────────────────
assert porte((1, 1), cons("בְּרֵאשִׁית")), "Gen 1:1 doit porter bereshit"
assert not porte((1, 1), cons("נֹחַ")), "Gen 1:1 ne porte pas Noach"
assert porte((1, 1), cons("אֱלֹהִים")), "préfixes : elohim nu dans 1:1"
assert not porte((5, 29), cons("בְּרֵאשִׁית")), "Gen 5:29 ne porte pas bereshit"
assert voisin((15, 3), cons("יִירַשׁ")) == (15, 4), \
    "témoin d'emprunt : Gn 15:3 cite une forme que 15:4 porte"
assert voisin((1, 1), cons("בְּרֵאשִׁית")) is None, \
    "un mot du verset lui-même n'est pas un emprunt au voisinage"
print("instrument éprouvé : 6 témoins, dont 3 qui doivent être signalés\n")

ecartes, total, fautes = [], 0, 0
par_classe = {}
for chemin in sorted(glob.glob("locked/**/*.md", recursive=True) +
                     glob.glob("brouillons/**/*.md", recursive=True)):
    r = controler(chemin)
    if r is None:
        continue
    if r[0] == "écarté":
        ecartes.append((r[1], r[2])); continue
    total += 1
    for n, bib, tr, w, cl in r[2]:
        fautes += 1
        par_classe.setdefault(cl, []).append((r[1], n, bib, tr, w))

for cl in ("ABSENT", "EMPRUNT", "graphie", "flexion"):
    items = par_classe.get(cl, [])
    titre = {"ABSENT": "Aucun mot du verset ne partage sa racine",
             "EMPRUNT": "Citée d'un verset voisin — ce n'est pas une réduction au lemme",
             "graphie": "Pleine contre défective — le mot est le bon",
             "flexion": "Forme voisine — construit, suffixe, ou lemme non déclaré"}[cl]
    print(f"\n## {titre} — {len(items)}\n")
    for f, n, bib, tr, w in items[: (99 if cl in ("ABSENT", "EMPRUNT") else 12)]:
        ou = voisin(bib, cons(w))
        d = f"  ← Gn {ou[0]}:{ou[1]}" if ou else ""
        print(f"  {f:<16} Gn {bib[0]}:{bib[1]:<3} {w:<18} « {tr[:32]} »{d}")
    if len(items) > 12 and cl not in ("ABSENT", "EMPRUNT"):
        print(f"  …et {len(items)-12} autres")
print(f"\n{total} chapitres joints · {fautes} signalements")
if ecartes:
    print("\nécartés faute de jointure sûre :")
    for f, r in ecartes:
        print(f"  {f:<20} {r}")
