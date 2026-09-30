#!/usr/bin/env python3
"""Un noyau de sens sous deux consonnes — et sept témoins tirés au sort.

## Le besoin

Une thèse circule sur le sémitique : les consonnes d'une racine ne seraient pas
arbitraires, et un noyau à **deux** consonnes porterait déjà un sens que la
troisième module. Sur פ-ר on lit *parad* séparer, *paras* rompre, *paraq*
arracher, *parar* briser — et un noyau « rupture » **semble** apparaître.

C'est le « semble » que cet outil éprouve. Il ne dit pas si la thèse est vraie :
il dit si le motif qu'on croit voir sur une paire se voit aussi sur des paires
tirées au sort. ==Si un noyau plausible sort de huit paires sur huit, la méthode
en fabrique partout et n'en prouve aucune.==

## Pourquoi en aveugle, et pourquoi l'aveugle doit porter sur les DONNÉES

Éprouvé le 30 septembre 2026. Quatre biais s'étaient glissés dans le premier
dispositif, et **les quatre penchaient du même côté** — celui de la thèse :

    la paire « deux premières lettres »   ramassait des noms à préfixe mem,
                                          dont la racine est ailleurs. פ n'est
                                          pas une lettre préfixe : l'artefact
                                          frappait les témoins, pas le candidat
    shin et sin fondus                    שָׁבַע jurer et שָׂבַע être rassasié
                                          comptés comme une famille
    les formes hébraïques en clair        la lectrice a reconnu פ-ר avant
                                          d'avoir lu une glose
    les numéros de Strong                 ils suivent l'ordre alphabétique :
                                          leurs plages trahissent la lettre

Les deux premiers sont corrigés dans le code — **verbes seuls**, dont la forme
de dictionnaire *est* la racine, et shin distingué de sin. Les deux autres sont
ce que `--aveugle` existe pour fermer.

> **Aveugler les étiquettes ne sert à rien si la donnée se reconnaît.**

## Ce que l'outil ne fait pas, et doit dire

**Ce n'est pas la thèse de Bohas** (*Matrices, étymons, racines*, Peeters,
1997). Son étymon est une paire **non ordonnée**, à n'importe quelle position,
implémentant une matrice de traits phonétiques. On éprouve ici les deux
premières radicales dans l'ordre — un cas particulier étroit, et un résultat
négatif ne réfuterait que la version simplifiée qui circule.

**Les gloses viennent de Strong (1890), et Strong croyait aux racines.** Il
rédigeait ses définitions en famille. `--harmonisation` mesure ce défaut plutôt
que de l'ignorer : la part des lemmes d'un groupe partageant un même mot de
contenu. Mesuré le 30 septembre, פ-ר rend **80 %** quand les sept témoins
plafonnent à **38 %** — et leurs mots partagés sont *hence*, *literal*,
*causatively*, des mots d'appareil et non de sens.

D'où le critère, qui est de la manageuse :

> Un noyau qui se lit dans les mots du glossateur est suspect ; un noyau qu'il
> faut aller chercher sous ses mots est un fait de langue.

**Et sa clause, qui ne se sépare pas de lui : il écarte un témoin, il ne
tranche pas la question.** 80 % ne dit pas que le noyau de פ-ר est faux — il se
peut que Strong ait écrit *break* huit fois parce que ces verbes veulent dire
briser. On ne peut plus l'établir *avec Strong*, voilà tout.

## Le lexique n'est pas versionné ici

`HebrewStrong.xml` d'OpenScriptures, **CC BY 4.0**, est téléchargé à la demande
dans un cache. Le lire pour écrire une analyse ne redistribue rien (cf.
`context/etat-des-sources.md`, « Consulter n'est pas redistribuer »).
"""

import argparse, collections, json, pathlib, random, re, sys, unicodedata, urllib.request

RACINE   = pathlib.Path(__file__).resolve().parent.parent
TEMOIN   = RACINE / "sources" / "he-wlc"
LEXIQUE  = RACINE / ".cache" / "HebrewStrong.xml"
SOURCE   = "https://raw.githubusercontent.com/openscriptures/HebrewLexicon/master/HebrewStrong.xml"

FAIBLES  = set("אהוינ")           # elles tombent, se redoublent, disparaissent
FINALES  = {"ך":"כ","ם":"מ","ן":"נ","ף":"פ","ץ":"צ"}
SHIN, SIN = "ׁ", "ׂ"
# mots de l'appareil de Strong : ils ne disent pas un sens partagé
APPAREIL = set("""to a an the of or and by in as with be being is it that from for on out up off away
i.e. e.g. cf. etc properly figuratively literally especially specifically generally
implication causatively causative denominative primitive root word same""".split())


def consonnes(mot: str) -> list[str]:
    """Le squelette consonantique, shin et sin tenus pour deux lettres."""
    brut = []
    for ch in unicodedata.normalize("NFD", mot):
        if ch in (SHIN, SIN):           brut.append(ch)
        elif unicodedata.category(ch) == "Mn": continue
        elif "א" <= ch <= "ת": brut.append(FINALES.get(ch, ch))
    sortie = []
    for ch in brut:
        if ch in (SHIN, SIN):
            if sortie and sortie[-1] == "ש": sortie[-1] = "ש" + ch
        else:
            sortie.append(ch)
    return sortie


def unites(paire: str) -> str:
    """Rend « שׁ-ל » et non « ש-ׁ-ל » : le point du shin appartient à sa lettre."""
    u = []
    for ch in paire:
        if ch in (SHIN, SIN) and u: u[-1] += ch
        else: u.append(ch)
    return "-".join(u)


def charger_lexique(chemin: pathlib.Path) -> dict:
    if not chemin.exists():
        print(f"  lexique absent — téléchargement depuis OpenScriptures (CC BY 4.0)", file=sys.stderr)
        chemin.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(SOURCE, chemin)
    s = chemin.read_text(encoding="utf-8")
    lex = {}
    for m in re.finditer(r'<entry id="H(\d+)">(.*?)</entry>', s, re.S):
        num, corps = m.group(1), m.group(2)
        def champ(motif):
            x = re.search(motif, corps, re.S)
            return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x.group(1))).strip() if x else ""
        pos = re.search(r'pos="([^"]+)"', corps)
        lex[num] = {"heb": champ(r"<w [^>]*>(.*?)</w>"), "pos": pos.group(1) if pos else "?",
                    "sens": champ(r"<meaning>(.*?)</meaning>") or champ(r"<usage>(.*?)</usage>")}
    return lex


def relever(lex: dict, seuil: int) -> dict:
    """Les verbes du témoin, groupés par leurs deux premières radicales."""
    compte = collections.Counter()
    for f in sorted(TEMOIN.glob("*.jsonl")):
        for ligne in f.open(encoding="utf-8"):
            for mot in json.loads(ligne).get("w", []):
                lem = (mot.get("oshb") or {}).get("lem", "")
                # « b/7225 » : le mot est le DERNIER segment ; « 1008+ » : continuation
                part = str(lem).split("/")[-1].strip().rstrip("+").strip()
                if re.fullmatch(r"\d+(\s+[a-z])?", part): compte[part] += 1
    groupes = collections.defaultdict(list)
    for lem, n in compte.items():
        e = lex.get(lem.split()[0])
        # VERBES SEULS : leur forme de dictionnaire est la racine, un nom peut
        # porter un préfixe et faire croire à une paire qui n'en est pas une.
        if not e or not e["heb"] or e["pos"] != "v" or n < seuil: continue
        c = consonnes(e["heb"])
        if len(c) < 2: continue
        groupes["".join(c[:2])].append({"lem": lem, "n": n, "cons": c, **e})
    return {k: sorted(v, key=lambda x: (-x["n"], x["lem"])) for k, v in groupes.items()}


def harmonisation(bloc: list) -> tuple[list[str], int, float]:
    """Part des lemmes partageant un même mot de CONTENU — le défaut de Strong.

    ==Rend TOUS les mots ex æquo, jamais un seul élu.== `Counter.most_common`
    départage par ordre de première rencontre, lequel dépend ici de l'itération
    d'un `set` — donc du hachage, donc du processus. Mesuré : le groupe ר-ע
    rendait « rule », « pasture » ou « tend » selon `PYTHONHASHSEED`, à compte
    identique. Le rang et le pourcentage étaient stables, **le mot ne l'était
    pas**, et le journal a failli en citer un.

    Le §2.5 ter du `CLAUDE.md` portait déjà l'avertissement — *un pourcentage
    qui bouge quand on trie un `glob` ne mesure pas ce qu'on croit*. Une règle
    n'empêche que ce qu'on pense à lui soumettre.
    """
    c = collections.Counter()
    for x in bloc:
        c.update({w for w in re.findall(r"[a-z]+", x["sens"].lower())
                  if w not in APPAREIL and len(w) > 2})
    if not c: return ([], 0, 0.0)
    n = max(c.values())
    return (sorted(w for w, k in c.items() if k == n), n, n / len(bloc))


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--paire", default="פר", help="la paire à éprouver (défaut : פר)")
    p.add_argument("--temoins", type=int, default=7, help="combien de paires tirer au sort")
    p.add_argument("--graine", type=int, default=20260930,
                   help="la graine du tirage — la rejouer redonne le même tirage")
    p.add_argument("--bande", type=float, default=0.30,
                   help="écart d'effectif toléré entre témoins et candidat")
    p.add_argument("--seuil", type=int, default=5, help="emplois minimum dans le témoin")
    p.add_argument("--aveugle", action="store_true",
                   help="cécité complète : identifiant opaque, ni forme ni Strong")
    p.add_argument("--cle", action="store_true", help="rendre la clé (APRÈS la lecture)")
    p.add_argument("--harmonisation", action="store_true",
                   help="mesurer l'harmonisation lexicale des gloses de Strong")
    p.add_argument("--lexique", type=pathlib.Path, default=LEXIQUE)
    a = p.parse_args()

    groupes = relever(charger_lexique(a.lexique), a.seuil)
    if a.paire not in groupes:
        print(f"  la paire {a.paire} n'a aucun verbe au seuil de {a.seuil} emplois"); return 1

    cible = len(groupes[a.paire])
    # appariés au candidat : deux lettres fortes, effectif comparable.
    # Une paire à lettre faible serait plus bruitée, donc moins susceptible de
    # montrer un noyau — ce qui avantagerait le candidat sans qu'on le voie.
    vivier = sorted(k for k, v in groupes.items()
                    if k != a.paire and not (set(k) & FAIBLES)
                    and (1 - a.bande) * cible <= len(v) <= (1 + a.bande) * cible)
    if len(vivier) < a.temoins:
        print(f"  vivier trop maigre : {len(vivier)} paires pour {a.temoins} témoins"); return 1

    tirage = random.Random(a.graine)
    choisies = tirage.sample(vivier, a.temoins)
    blocs = [a.paire] + choisies
    tirage.shuffle(blocs)
    etiquettes = dict(zip("ABCDEFGHIJKLMNOP", blocs))

    if a.cle:
        print(f"  clé — graine {a.graine}, vivier de {len(vivier)} paires\n")
        for lab, pr in etiquettes.items():
            print(f"   {lab}  →  {unites(pr)}" + ("    ← le candidat" if pr == a.paire else ""))
        if a.harmonisation:
            print("\n  harmonisation lexicale des gloses — part des lemmes partageant un mot de contenu\n")
            for lab, pr in sorted(etiquettes.items(),
                                  key=lambda t: (-harmonisation(groupes[t[1]])[2], t[0])):
                mots, n, part = harmonisation(groupes[pr])
                if len(mots) == 1:  quoi = f"« {mots[0]} »"
                else:               quoi = f"{len(mots)} ex æquo : " + ", ".join(mots[:4])
                print(f"   {lab}  {unites(pr):7} {n}/{len(groupes[pr]):<3} "
                      f"{part:5.0%} {'█' * round(part * 24)}  {quoi}")
            print("\n  Un noyau qui se lit dans les mots du glossateur est suspect ; un noyau")
            print("  qu'il faut chercher sous ses mots est un fait de langue.")
            print("  Mais le critère ÉCARTE UN TÉMOIN, il ne tranche pas la question.")
        return 0

    print(f"# {len(blocs)} familles de verbes — lecture en aveugle\n")
    print("Un seul de ces groupes est celui qu'on éprouve. Pour chacun : **vois-tu")
    print("un noyau de sens commun, et lequel ?** Réponds *non* quand c'est non —")
    print("c'est cette réponse-là qui fait marcher le test.\n")
    if not a.aveugle:
        print("> ⚠ Les formes et les numéros de Strong sont en clair, donc la paire se")
        print("> reconnaît. Pour une vraie cécité : `--aveugle`.\n")
    for lab, pr in etiquettes.items():
        bloc = groupes[pr]
        print(f"\n## Groupe {lab} — {len(bloc)} verbes, {sum(x['n'] for x in bloc)} emplois\n")
        if a.aveugle:
            print("| id | emplois | glose de Strong (1890) |")
            print("|---|---|---|")
        else:
            print("| forme | Strong | emplois | glose de Strong (1890) |")
            print("|---|---|---|---|")
        for i, x in enumerate(bloc, 1):
            marque = " †" if len(x["cons"]) >= 3 and x["cons"][2] in FAIBLES else ""
            if a.aveugle:
                print(f"| {lab}-{i:02}{marque} | {x['n']} | {x['sens'][:95]} |")
            else:
                print(f"| {x['heb']}{marque} | {x['lem']} | {x['n']} | {x['sens'][:95]} |")
    print("\n`†` troisième radicale faible (א ה ו י נ) : elle tombe ou se redouble,")
    print("la famille y est moins nette qu'elle n'en a l'air.")
    print(f"\nLa clé, après lecture : `--cle --graine {a.graine}`")
    return 0


if __name__ == "__main__":
    sys.exit(main())
