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

def cons(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^א-ת]", "", s)

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
    """Le verset porte-t-il ce mot, préfixes tolérés dans les deux sens ?"""
    mots = VERSETS.get(ref, set())
    if c in mots:
        return True
    for m in mots:
        for k in (1, 2):
            if len(m) > k + 1 and all(x in PREF for x in m[:k]) and m[k:] == c:
                return True
            if len(c) > k + 1 and all(x in PREF for x in c[:k]) and c[k:] == m:
                return True
    return False

def classer(ref, c):
    """Toutes les absences ne se valent pas — trois gravités, et une seule
    demande un arbitrage."""
    mots = VERSETS.get(ref, set())
    for m in mots:
        if m.replace("ו", "").replace("י", "") == c.replace("ו", "").replace("י", ""):
            return "graphie"          # pleine contre défective : le mot est le bon
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
print("instrument éprouvé : 4 témoins, dont 2 qui doivent être signalés\n")

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

for cl in ("ABSENT", "graphie", "flexion"):
    items = par_classe.get(cl, [])
    titre = {"ABSENT": "Aucun mot du verset ne partage sa racine",
             "graphie": "Pleine contre défective — le mot est le bon",
             "flexion": "Forme voisine — construit, suffixe, ou lemme non déclaré"}[cl]
    print(f"\n## {titre} — {len(items)}\n")
    for f, n, bib, tr, w in items[: (99 if cl == "ABSENT" else 12)]:
        print(f"  {f:<16} Gn {bib[0]}:{bib[1]:<3} {w:<18} « {tr[:36]} »")
    if len(items) > 12 and cl != "ABSENT":
        print(f"  …et {len(items)-12} autres")
print(f"\n{total} chapitres joints · {fautes} signalements")
if ecartes:
    print("\nécartés faute de jointure sûre :")
    for f, r in ecartes:
        print(f"  {f:<20} {r}")
