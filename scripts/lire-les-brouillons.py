#!/usr/bin/env python3
"""Rend le corpus bâti en une page de lecture — sans une seule italique.

    python3 scripts/lire-les-brouillons.py <dist> [livres] [sortie]
    python3 scripts/lire-les-brouillons.py ../ONTBibleApp/dist

Sans liste de livres, tous ceux qui portent au moins un chapitre sont rendus.

## Pourquoi cette page existe

Relire un texte en cours de rédaction dans un aperçu markdown ne marche pas :
le corps et les gloses n'y sont distingués que par **la pente des lettres**.
C'est le plus faible des discriminants pour tout le monde, et le pire pour un
œil kératocônique — l'astigmatisme irrégulier y produit des images fantômes
superposées, que l'italique multiplie au lieu de séparer.

Ici, corps et apparat se distinguent par **la couleur, la taille et le fond**,
et aucune branche du rendu ne produit d'italique. La glose reçoit un bleu
ardoise **froid**, choisi pour être le plus éloigné possible des trois
marquages ONT, qui sont tous chauds.

## Le contrôle est dans l'instrument, pas en commentaire

Les feuilles de style du projet ont longtemps écrit leurs ratios de contraste
en commentaire, sans que rien ne les relise. Ici, `controler()` mesure chaque
couleur sur son fond **avant d'écrire quoi que ce soit**, et rend 1 si l'une
passe sous le plancher.

## Pourquoi trois couleurs diffèrent de celles de l'app

Le garde a mordu sur les jetons du projet : l'or à 4,61:1 sur parchemin, le
bordeaux à 6,17 et le Shem à 6,15 sur fond sombre. Plutôt que de baisser le
plancher, on applique la règle du §2.10 — **la teinte est commune, la clarté
se remesure sur chaque fond**. Les valeurs ci-dessous sont donc dérivées des
jetons de l'app à teinte et saturation constantes (elles traversent au dixième
près) ; seule la clarté bouge.

Ce ne sont pas les jetons de l'app et elles n'ont pas à l'être : cette page est
un outil de lecture, non une surface de marque.
"""
import json, pathlib, sys, html

PLANCHER = 6.5

def lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

THEMES = {
    "parchemin": dict(fond="#FAF5EB", encre="#29211C", or_="#685532", bordeaux="#862742",
                      shem="#603518", glose="#2C5164", sourd="#5C5049"),
    "sombre":    dict(fond="#171416", encre="#E0DBD4", or_="#CDBE83", bordeaux="#DA7F98",
                      shem="#BE9274", glose="#93BBD1", sourd="#A79B92"),
}

def controler():
    """Un instrument qui ne mesure pas ne sert à rien : on mesure avant d'écrire."""
    mauvais = []
    for nom, t in THEMES.items():
        for role in ("encre", "or_", "bordeaux", "shem", "glose", "sourd"):
            r = ratio(t[role], t["fond"])
            marque = "ok " if r >= PLANCHER else "SOUS"
            print(f"   {nom:<10} {role:<9} {t[role]}  {r:5.2f}:1  {marque}")
            if r < PLANCHER:
                mauvais.append((nom, role, round(r, 2)))
    if mauvais:
        print(f"\n  ARRÊT — {len(mauvais)} couleur(s) sous le plancher de {PLANCHER}:1 : {mauvais}")
        sys.exit(1)
    print(f"\n  toutes les couleurs tiennent le plancher de {PLANCHER}:1\n")

E = lambda s: html.escape(s or "")

def rendre(n):
    """Un nœud. Aucune branche ne produit d'italique — c'est la règle de la page."""
    t = n.get("t")
    if t == "text":          return E(n.get("v"))
    if t == "term":          return f'<b class="or">{E(n["v"])}</b>'
    if t == "shem":          return f'<b class="shem">{E(n["v"])}</b>'
    if t == "accentuation":  return f'<b class="acc">{suite(n["children"])}</b>'
    if t == "em":            return f'<span class="tr">{suite(n["children"])}</span>'
    if t == "gloss":         return f'<span class="glose">{suite(n["children"])}</span>'
    if t == "heb":           return f'<span class="heb">{E(n["v"])}</span>'
    if t == "translit":
        return (f'<span class="n3">(<span class="tr">{E(n["translit"])}</span>'
                f' / <span class="heb">{E(n["hebrew"])}</span>)</span>')
    if t == "break":         return "<br>"
    return suite(n.get("children", []))

def suite(ns): return "".join(rendre(x) for x in ns or [])

SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

def bloc(b):
    t = b.get("t")
    if t == "heading":
        return f'<h{min(b.get("level",2)+1,6)}>{suite(b["nodes"])}</h{min(b.get("level",2)+1,6)}>'
    if t == "para":   return f'<p>{suite(b["nodes"])}</p>'
    if t == "quote":  return f'<blockquote>{suite(b["nodes"])}</blockquote>'
    if t == "rule":   return "<hr>"
    if t == "list":
        b_ = "ol" if b.get("ordered") else "ul"
        return f'<{b_}>' + "".join(f"<li>{suite(i)}</li>" for i in b.get("items", [])) + f"</{b_}>"
    if t == "table":
        th = "".join(f"<th>{suite(h)}</th>" for h in b.get("headers", []))
        tr = "".join("<tr>" + "".join(f"<td>{suite(c)}</td>" for c in r) + "</tr>" for r in b.get("rows", []))
        return f"<div class='tab'><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>"
    if t == "verses":
        out = []
        for v in b["verses"]:
            num = str(v["n"]).translate(SUP)
            out.append(f'<p class="v"><span class="num">{num}</span> {suite(v["nodes"])}</p>')
        return "".join(out)
    return ""

def page(dist, livres):
    corps, sommaire = [], []
    for slug in livres:
        p = pathlib.Path(dist) / "books" / f"{slug}.json"
        if not p.exists():
            print(f"  ignoré (absent) : {slug}"); continue
        b = json.loads(p.read_text(encoding="utf-8"))
        for ch in b.get("chapters", []):
            cid = ch["id"]
            sommaire.append(f'<a href="#{E(cid)}">{E(ch.get("title"))}</a>')
            st = ch.get("subtitle") or {}
            sous = ""
            if st:
                bits = [E(st.get("french")), f'<span class="heb">{E(st.get("hebrew"))}</span>'
                        if st.get("hebrew") else "", E(st.get("reference"))]
                sous = '<p class="sous">' + " · ".join(x for x in bits if x) + "</p>"
            etat = ch.get("status")
            corps.append(f'<section id="{E(cid)}"><h2>{E(ch.get("title"))}'
                         f'{f"<em class=etat>{E(etat)}</em>" if etat else ""}</h2>{sous}'
                         + "".join(bloc(x) for x in ch.get("blocks", [])) + "</section>")
    vars_ = "\n".join(
        f'  [data-theme="{k}"] {{ --fond:{t["fond"]}; --encre:{t["encre"]}; --or:{t["or_"]};'
        f' --bordeaux:{t["bordeaux"]}; --shem:{t["shem"]}; --glose:{t["glose"]}; --sourd:{t["sourd"]}; }}'
        for k, t in THEMES.items())
    return TPL.replace("/*VARS*/", vars_).replace("<!--SOMMAIRE-->", " ".join(sommaire)) \
              .replace("<!--CORPS-->", "\n".join(corps))

TPL = r"""<!doctype html><html lang="fr" data-theme="parchemin"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ONT — lecture des brouillons</title><style>
/*VARS*/
:root{ --taille:24px; --interligne:1.85; }
*{box-sizing:border-box}
html{background:var(--fond)}
body{margin:0;background:var(--fond);color:var(--encre);
  font-family:"Iowan Old Style",Palatino,Georgia,serif;
  font-size:var(--taille);line-height:var(--interligne);
  -webkit-font-smoothing:antialiased}
.barre{position:sticky;top:0;z-index:10;background:var(--fond);
  border-bottom:2px solid var(--sourd);padding:14px 22px;
  display:flex;flex-wrap:wrap;gap:22px;align-items:center;
  font-family:ui-sans-serif,-apple-system,system-ui,sans-serif;font-size:16px}
.barre label{display:flex;align-items:center;gap:9px;cursor:pointer}
.barre input[type=range]{width:190px}
.barre button{font:inherit;padding:8px 16px;border:2px solid var(--sourd);
  background:transparent;color:var(--encre);border-radius:3px;cursor:pointer}
main{max-width:46ch;margin:0 auto;padding:40px 26px 140px}
h2{font-size:1.5em;margin:2.4em 0 .2em;line-height:1.25}
h3,h4,h5{font-size:1.12em;margin:1.9em 0 .3em;color:var(--sourd);
  font-family:ui-sans-serif,system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase}
.etat{font-family:ui-sans-serif,system-ui,sans-serif;font-size:.5em;font-style:normal;
  letter-spacing:.09em;text-transform:uppercase;color:var(--sourd);margin-left:.9em;vertical-align:middle}
.sous{color:var(--sourd);font-size:.92em;margin:.1em 0 1.6em}
p{margin:0 0 1.15em}
.num{font-size:.66em;vertical-align:.5em;color:var(--sourd);margin-right:.2em;
  font-family:ui-sans-serif,system-ui,sans-serif}
/* Les trois marquages ONT — jamais penchés, toujours colorés. */
.or{color:var(--or);font-weight:600}
.shem{color:var(--shem);font-weight:600}
.acc{color:var(--bordeaux);font-weight:600}
/* Une translittération : ni italique ni couleur, un espacement. */
.tr{letter-spacing:.05em}
/* L'apparat : sa couleur, sa taille, et un fond qui montre où il commence. */
.glose{color:var(--glose);font-size:.87em;
  background:color-mix(in srgb,var(--glose) 8%,transparent);
  padding:.1em .34em;border-radius:3px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.glose::before{content:"[";opacity:.55}
.glose::after{content:"]";opacity:.55}
.heb{font-family:"SBL Hebrew","Ezra SIL","Frank Ruhl Libre",serif;
  font-size:1.08em;direction:rtl;unicode-bidi:isolate}
blockquote{margin:1.3em 0;padding:.2em 0 .2em 1.1em;border-left:4px solid var(--sourd)}
hr{border:0;border-top:2px solid var(--sourd);margin:2.4em 0;opacity:.5}
ul,ol{padding-left:1.4em} li{margin:.5em 0}
.tab{overflow-x:auto;margin:1.4em 0}
table{border-collapse:collapse;width:100%} th,td{border:1px solid var(--sourd);padding:.5em .7em;text-align:left}
.sommaire{max-width:46ch;margin:0 auto;padding:26px;display:flex;flex-wrap:wrap;gap:10px 20px;
  font-family:ui-sans-serif,system-ui,sans-serif;font-size:.7em}
.sommaire a{color:var(--glose)}
body.sans-glose .glose{display:none}
body.sans-n3 .n3{display:none}
</style></head><body>
<div class="barre">
  <label>Taille <input id="t" type="range" min="18" max="52" value="24"></label>
  <label><input id="g" type="checkbox" checked> Gloses</label>
  <label><input id="n" type="checkbox" checked> Niveau 3</label>
  <button id="th">Thème</button>
</div>
<nav class="sommaire"><!--SOMMAIRE--></nav>
<main><!--CORPS--></main>
<script>
const r=document.documentElement,b=document.body;
t.oninput=e=>r.style.setProperty('--taille',e.target.value+'px');
g.onchange=e=>b.classList.toggle('sans-glose',!e.target.checked);
n.onchange=e=>b.classList.toggle('sans-n3',!e.target.checked);
th.onclick=()=>r.dataset.theme=r.dataset.theme==='parchemin'?'sombre':'parchemin';
</script></body></html>"""

def tous(dist):
    """Tout livre qui porte au moins un chapitre — l'ordre du manifeste."""
    out = []
    for p in sorted((pathlib.Path(dist) / "books").glob("*.json")):
        try:
            b = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if b.get("chapters"):
            out.append((b.get("slot", 999), p.stem))
    return [s for _, s in sorted(out)]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    dist = sys.argv[1]
    livres = sys.argv[2].split(",") if len(sys.argv) > 2 and sys.argv[2] else tous(dist)
    sortie = sys.argv[3] if len(sys.argv) > 3 else "lecture.html"
    print("  contrôle des couleurs :")
    controler()
    pathlib.Path(sortie).write_text(page(dist, livres), encoding="utf-8")
    ko = pathlib.Path(sortie).stat().st_size // 1024
    print(f"  écrit : {sortie} ({ko} Ko)")
