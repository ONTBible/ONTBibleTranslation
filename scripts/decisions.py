#!/usr/bin/env python3
"""Où une décision du projet est écrite — et lesquelles sont encore ouvertes.

## Le besoin, et pourquoi ce n'est pas un document de plus

Le savoir du projet est éclaté sur cinq sources qui ont toutes une bonne raison
d'exister : `CLAUDE.md` porte les règles, `SYNCHRONISATION.md` le journal des
leçons de méthode, `lexique/` trois cent treize fiches, `corpus-order.md`
l'ordre des livres, `context/` les dossiers de travail — et les arbitrages les
plus récents vivent dans les **pieds de section** des chapitres, là où personne
ne pense à chercher.

Quand on demande « est-ce que X a déjà été tranché ? », on fait un `grep` et on
espère tomber sur le bon mot. Le coût n'est pas de chercher : c'est de **ne pas
trouver et de retrancher**, en croyant décider pour la première fois.

## Pourquoi un index engendré, et jamais un document écrit

Le §2.5 ter pose la règle à laquelle cet outil doit obéir : *« Ce n'est pas une
source de vérité dédoublée : une seule source par fait. »*

Une base de connaissance rédigée à la main serait une sixième source, et elle
divergerait — c'est le mode de défaillance que le journal de ce projet
documente depuis une semaine. Celle-ci ne **copie** rien : elle dit *où* une
décision est écrite, jamais *ce qu'elle dit*. On ne peut donc pas la
contredire ; au pire elle est incomplète, et un `grep` reste possible.

    scripts/decisions.py                  l'index, sur la sortie standard
    scripts/decisions.py --ecrire         l'écrit dans DECISIONS.md
    scripts/decisions.py chesed           tout ce qui touche un terme
    scripts/decisions.py --ouvertes       ce qui attend encore l'auteur

## Ce qu'il relève, et où

| ce qui est relevé | où il le lit |
|---|---|
| une décision datée | « décision de l'auteur du 25 août 2026 », partout |
| une décision **ouverte** | « à trancher / à confirmer par l'auteur », « réservé à l'auteur » |
| un intraduisible et son premier emploi | les puces du §2.5, les lignes du §3 |
| un passage réservé | le §7 du `CLAUDE.md` |
| une leçon de méthode | les titres `###` du journal |
| une fiche | `lexique/` |
| un dossier de travail | `context/` |

Les décisions ouvertes viennent en tête : ce sont celles qu'on oublie, et le
seul relevé dont l'absence coûte quelque chose.
"""

import re
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

# Les dossiers qu'on ne parcourt pas : ni le `.git`, ni les sources bibliques —
# quarante mille versets qui ne portent aucune décision et noieraient tout.
IGNORES = {".git", "sources", "utilities", "node_modules", "dist", ".github"}

# **L'index ne s'indexe pas lui-même.** Sans cette ligne il se cite, et chaque
# exécution recopie ses propres lignes dans les suivantes : la table grossit à
# vide, les recherches rendent des résultats qui pointent sur l'index au lieu de
# la source, et deux exécutions cessent de rendre le même fichier. Trouvé en
# éprouvant l'idempotence, qui est le seul contrôle qu'un fichier engendré
# réclame vraiment.
SORTIE = "DECISIONS.md"

DATE = r"(?:1er|1ᵉʳ|\d{1,2})\s+(?:janvier|février|mars|avril|mai|juin|juillet|"
DATE += r"août|septembre|octobre|novembre|décembre)\s+20\d\d"

MOTIFS = {
    # (étiquette, expression) — l'ordre est celui de l'affichage.
    "ouverte": re.compile(
        r"==?[ÀA]\s+(?:confirmer|trancher)\s+par\s+l'auteur==?"
        r"|[Dd]écision\s+réservée?\s+à\s+l'auteur"
        r"|réservée?\s+à\s+l'auteur"
        r"|à\s+trancher\s+par\s+l'auteur",
        re.I,
    ),
    "datée": re.compile(rf"[Dd]écision\s+de\s+l'auteur\s+du\s+{DATE}"),
    "tranchée": re.compile(rf"(?:tranché|arrêté|acté|verrouillé)e?\s+le\s+{DATE}"),
}


def sans_accents(s: str) -> str:
    d = unicodedata.normalize("NFD", s)
    return "".join(c for c in d if not unicodedata.combining(c)).lower()


def slug(s: str) -> str:
    """Le lemme d'une forme — **la règle du pipeline, à l'identique**.

    `inline.rs::slugify` : décomposition, retrait des diacritiques, minuscules,
    puis les apostrophes **tombent sans séparateur** — `mal'akh` → `malakh` —
    tandis que tout autre signe devient un tiret. Réécrire cette règle « à peu
    près » est ce qui a produit le défaut que le contrôle des liens morts
    mesure : deux normalisations écrites séparément divergent.
    """
    s = sans_accents(s).replace("'", "").replace("\u2019", "").replace("\u02bc", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def fichiers():
    """Tous les `.md` du vault, sauf ce qui ne porte pas de décision."""
    for p in sorted(RACINE.rglob("*.md")):
        rel = p.relative_to(RACINE)
        if any(part in IGNORES for part in rel.parts) or str(rel) == SORTIE:
            continue
        yield p


def contexte(ligne: str, largeur: int = 96, autour: "re.Match | None" = None) -> str:
    """Une ligne de markdown rendue lisible, centrée sur ce qui a été trouvé.

    **Le centrage n'est pas cosmétique.** Sans lui, une puce de trois cents
    signes rend toujours ses cent premiers, et la marque qu'on cherche — qui
    est presque toujours en fin de phrase, parce qu'on tranche après avoir
    exposé — n'apparaît jamais. L'index affichait alors des lignes justes qui
    ne montraient pas pourquoi elles avaient été retenues.
    """
    t = re.sub(r"\*\*(.+?)\*\*|==(.+?)==|\*(.+?)\*", lambda m: next(g for g in m.groups() if g), ligne)
    t = re.sub(r"\[\[(.+?)\]\]", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip(" -*#|")
    if len(t) <= largeur:
        return t
    if autour is None:
        return t[: largeur - 1] + "…"
    # Le décalage se recalcule sur le texte nettoyé : les marques retirées ont
    # déplacé les positions, et un index de la ligne brute pointerait à côté.
    aiguille = re.sub(r"[*=\[\]]", "", autour.group(0))
    i = t.find(aiguille)
    if i < 0:
        return t[: largeur - 1] + "…"
    debut = max(0, i - largeur // 3)
    fin = min(len(t), debut + largeur)
    return ("…" if debut else "") + t[debut:fin] + ("…" if fin < len(t) else "")


def relever():
    """Les décisions, par étiquette : (fichier, ligne, texte)."""
    trouve = {k: [] for k in MOTIFS}
    for p in fichiers():
        rel = p.relative_to(RACINE)
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            for etiquette, motif in MOTIFS.items():
                m = motif.search(ligne)
                if m:
                    trouve[etiquette].append((str(rel), n, contexte(ligne, autour=m)))
    return trouve


def intraduisibles():
    """Les intraduisibles du §2.5, avec leur premier emploi quand il est écrit.

    Lus **au même endroit que le pipeline les lit** — les formes entre accents
    graves des puces du §2.5 —, pour que l'index ne puisse pas désigner un terme
    que le pipeline ne connaît pas.
    """
    claude = (RACINE / "CLAUDE.md").read_text(encoding="utf-8")
    section = claude.split("### 2.5 bis")[0].split("### 2.5")[-1]
    out = []
    for ligne in section.splitlines():
        if not ligne.lstrip().startswith("- `"):
            continue
        # **Exactement l'expression du pipeline** — `reference.rs:39`. Toute
        # autre la ferait diverger, et un index qui contredit le producteur
        # est pire qu'une absence d'index : il aurait fallu le croire.
        # La classe exclut `*`, ce qui écarte les formes combinées écrites
        # `**Adonai** **YHWH**` : ce ne sont pas des lemmes, et une expression
        # plus permissive en fabriquait un — `Adonai** **YHWH`.
        formes = re.findall(r"`\*\*([^`*]+)\*\*`", ligne)
        if not formes:
            continue
        emploi = re.search(r"Premier emploi\s+([^.]+)\.", ligne)
        out.append((formes[0], formes[1:], emploi.group(1).strip() if emploi else None))
    return out


def reserves():
    """Les passages que le §7 réserve à l'auteur."""
    claude = (RACINE / "CLAUDE.md").read_text(encoding="utf-8")
    m = re.search(r"## 7\..*?(?=\n## 8\.)", claude, re.S)
    if not m:
        return []
    # Deux formes coexistent dans le §7, et n'en attraper qu'une en perdait
    # neuf sur quatorze — sans que rien ne le signale, puisqu'une liste courte
    # ressemble à une liste :
    #
    #     ***Tehilim***                — un livre entier
    #     ***Bereshit* 2:4-25**        — un passage : italique du titre, puis
    #                                    le renvoi, et le gras se ferme après
    out = []
    for ligne in m.group(0).splitlines():
        ligne = ligne.strip()
        if not ligne.startswith("***"):
            continue
        titre, _, reste = ligne[1:].partition("** —")
        titre = titre.replace("*", "").strip()
        out.append((titre, reste.strip()))
    return out


def journal():
    """Les leçons de méthode — un titre de journal par entrée."""
    p = RACINE / "SYNCHRONISATION.md"
    if not p.exists():
        return []
    return [
        l[4:].strip()
        for l in p.read_text(encoding="utf-8").splitlines()
        if l.startswith("### ")
    ]


# ─────────────────────────────────────────────────────────────────────────────


def index() -> str:
    t = relever()
    l = [
        "# Où les décisions du projet sont écrites",
        "",
        "*Engendré par `scripts/decisions.py`. ==Ne pas modifier à la main== —",
        "ce fichier ne dit pas ce qui a été décidé, il dit ==où c'est écrit==.",
        "Une seule source par fait (§2.5 ter) : la source reste le fichier",
        "désigné, et cet index n'en est qu'une table.*",
        "",
        "## Ce qui attend encore l'auteur",
        "",
    ]
    if t["ouverte"]:
        l += ["| Où | Ligne | Ce qui est en attente |", "|---|---:|---|"]
        for f, n, txt in t["ouverte"]:
            l.append(f"| `{f}` | {n} | {txt} |")
    else:
        l.append("*Rien d'ouvert.*")

    l += ["", "## Décisions datées", ""]
    if t["datée"] or t["tranchée"]:
        l += ["| Où | Ligne | La décision |", "|---|---:|---|"]
        for f, n, txt in sorted(t["datée"] + t["tranchée"]):
            l.append(f"| `{f}` | {n} | {txt} |")
    else:
        l.append("*Aucune.*")

    intr = intraduisibles()
    l += [
        "",
        f"## Les {len(intr)} intraduisibles déclarés au §2.5",
        "",
        "Le lemme d'abord, ses formes dérivées ensuite — c'est l'ordre que le",
        "pipeline lit, et les dérivées retombent sur la fiche du lemme.",
        "",
        "| Lemme | Formes dérivées | Premier emploi | Fiche |",
        "|---|---|---|:-:|",
    ]
    # Une fiche peut porter le lemme slugifié ou son nom d'origine : le vault
    # écrit `lexique/Avraham.md` autant que `lexique/chesed.md`.
    fiches_connues = {slug(f.stem) for f in (RACINE / "lexique").glob("*.md")}
    lemmes_propres = {slug(x[0]) for x in intr}
    partagees = False
    for lemme, formes, emploi in intr:
        marquees = []
        for f in formes:
            # Une casse différente du lemme lui-même n'est pas un partage :
            # `**Elohim**` / `elohim` slugifient pareil et sont la même entrée.
            if slug(f) != slug(lemme) and slug(f) in lemmes_propres:
                marquees.append(f"{f} ◆")
                partagees = True
            else:
                marquees.append(f)
        l.append(
            f"| **{lemme}** | {', '.join(marquees) or '—'} | "
            f"{emploi or '—'} | {'✓' if slug(lemme) in fiches_connues else '·'} |"
        )
    if partagees:
        l += [
            "",
            "◆ — cette forme est ==aussi déclarée comme lemme par sa propre puce==.",
            "Le §2.5 la cite dans la prose de la puce voisine pour l'en *écarter*",
            "— « ni les composés qui ont leur propre entrée » —, mais l'extraction",
            "ne lit que les formes entre accents graves et ne distingue pas une",
            "citation d'une déclaration. Vérifié sans conséquence sur le corpus",
            "actuel : `**El Elyon**` est bien émis avec `lemma: el-elyon`, non",
            "`el`. C'est une fragilité, pas un défaut — signalée pour qu'elle ne",
            "se découvre pas le jour où l'ordre de lecture changera.",
        ]

    res = reserves()
    l += ["", f"## Les {len(res)} passages que le §7 réserve à l'auteur", ""]
    for titre, quoi in res:
        # Italique seul, jamais `***…***` : le §2.5 réserve le gras aux
        # intraduisibles, et un titre de livre relève du §2.6. Le §7 du
        # `CLAUDE.md` l'écrit encore en gras-italique — sans conséquence, car
        # le pipeline ne lit pas cette section —, et on ne recopie pas la
        # forme fautive en la transportant ici.
        l.append(f"- *{titre}* — {quoi}" if quoi else f"- *{titre}*")

    jrn = journal()
    l += [
        "",
        f"## Les {len(jrn)} leçons du journal",
        "",
        "*Dans `SYNCHRONISATION.md`, et portées à l'identique dans les trois dépôts.*",
        "",
    ]
    for titre in jrn:
        l.append(f"- {titre}")

    l += [
        "",
        "---",
        "",
        f"*{len(list(fichiers()))} fichiers parcourus · "
        f"{len(list((RACINE / 'lexique').glob('*.md')))} fiches dans `lexique/`.*",
    ]
    return "\n".join(l) + "\n"


def chercher(terme: str) -> int:
    """Tout ce qui touche un mot, dans toutes les sources à la fois.

    C'est le mode qui sert le plus souvent, et il remplace le `grep` qu'on
    faisait en espérant tomber sur le bon mot : celui-ci cherche sans accents ni
    casse, et il **dit dans quelle source** chaque résultat se trouve, ce qu'un
    `grep` sur un arbre de trois cents fichiers ne fait pas.
    """
    cible = sans_accents(terme)
    par_source = {}
    for p in fichiers():
        rel = str(p.relative_to(RACINE))
        source = (
            "la règle" if rel == "CLAUDE.md"
            else "le journal" if rel == "SYNCHRONISATION.md"
            else "une fiche" if rel.startswith("lexique/")
            else "un dossier de travail" if rel.startswith("context/")
            else "l'ordre du corpus" if rel == "corpus-order.md"
            else "un brouillon" if rel.startswith("brouillons/")
            else "un texte verrouillé" if rel.startswith("locked/")
            else "ailleurs"
        )
        for n, ligne in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            plat = sans_accents(ligne)
            if cible in plat:
                # On recherche sur la ligne brute pour centrer au bon endroit,
                # en repartant de la position trouvée dans la version aplatie.
                i = plat.find(cible)
                faux = re.compile(re.escape(ligne[i : i + len(terme)]))
                par_source.setdefault(source, []).append(
                    (rel, n, contexte(ligne, autour=faux.search(ligne)))
                )

    if not par_source:
        print(f"  rien sur « {terme} ».")
        print("  Un mot absent de l'index n'est pas un mot non décidé : il peut")
        print("  l'avoir été sous une autre forme. Essayer le lemme, ou l'hébreu.")
        return 1

    total = sum(len(v) for v in par_source.values())
    print(f"\n  « {terme} » — {total} mentions dans {len(par_source)} sources\n")
    # L'ordre d'autorité : la règle, puis le journal, puis le reste.
    ordre = ["la règle", "le journal", "une fiche", "un dossier de travail",
             "l'ordre du corpus", "un texte verrouillé", "un brouillon", "ailleurs"]
    for source in ordre:
        lignes = par_source.get(source)
        if not lignes:
            continue
        print(f"  ── {source} ({len(lignes)})")
        for rel, n, txt in lignes[:12]:
            print(f"     {rel}:{n}")
            print(f"       {txt}")
        if len(lignes) > 12:
            print(f"     … et {len(lignes) - 12} autres")
        print()
    return 0


def ouvertes() -> int:
    t = relever()["ouverte"]
    if not t:
        print("  Rien n'attend l'auteur.")
        return 0
    print(f"\n  {len(t)} décisions attendent l'auteur\n")
    for f, n, txt in t:
        print(f"  {f}:{n}")
        print(f"    {txt}\n")
    return 0


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print(index())
    elif args[0] == "--ecrire":
        cible = RACINE / SORTIE
        cible.write_text(index(), encoding="utf-8")
        print(f"  écrit : {cible.relative_to(RACINE)}")
    elif args[0] == "--ouvertes":
        sys.exit(ouvertes())
    else:
        sys.exit(chercher(" ".join(args)))
