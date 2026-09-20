# 2.5 Marquage des termes intraduisibles — convention Affinity Publisher

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « 2.5 Marquage des termes intraduisibles — convention Affinity Publisher », partie 9. Empreinte de la section : `0d61da19ae2530b5`. Régénérer : `python3 knowledge/decouper.py`.*

**Appliquer dès la rédaction** — ne pas attendre une passe séparée.

**`**...**` est EXCLUSIVEMENT réservé aux intraduisibles** — jamais pour l'emphase (mettre en valeur une phrase, un mot ordinaire ou un titre), **y compris dans les feuilles d'introduction et les notes** : le gras déclencherait à tort le style « Transliteration » d'Affinity au copier-coller, et l'app afficherait le mot en or, touchable, ouvrant une fiche de lexique vide. Pour l'emphase ordinaire, utiliser l'italique `*...*` ; pour une **accentuation**, voir §2.5 bis.

**Jusqu'où porte cet interdit — écrit le 8 septembre 2026, parce qu'il ne
l'était pas.** La règle vaut pour ==ce qui est distribué== : le corps des
traductions, les gloses, les notes de bas de section, les feuilles
d'introduction, et les fiches de `lexique/`. Elle ne vaut pas pour les documents
de travail du dépôt — ce `CLAUDE.md`, `SYNCHRONISATION.md`, les plans, les
rapports —, où le gras d'insistance reste permis.

Le motif n'est pas une tolérance, c'est ==la raison d'être de l'interdit==. Les
deux dégâts qu'il prévient sont mécaniques : Affinity applique son style au
copier-coller, et l'app affiche le mot en or et le rend touchable. ==Un fichier
qui ne passe ni dans l'un ni dans l'autre ne peut produire ni l'un ni l'autre.==

**Une exception, et elle est le vrai périmètre.** Ce qui compte n'est pas le
fichier, c'est ==ce qui fabrique un lemme==. Les entrées de glossaire de ce
document sont lues par le pipeline et émises vers `dist/` : un gras d'insistance
posé ==à l'intérieur d'une entrée== y devient un terme émis, donc un mot d'or
sans fiche. Dix-neuf l'ont été et ont été convertis le 25 août 2026 — c'est le
seul endroit de ce fichier où la règle mord, et elle y mord entièrement.

==Mesuré, et non déduit.== Deux témoins plantés le 8 septembre 2026, un dans une
puce du §2.5 et un dans une case du §3, puis une construction :

- celui du §2.5 ==est devenu un lemme==. La puce d'un terme devient sa note de
  balisage dans `glossary.json`, et cette note est découpée en nœuds : le gras y
  ressort en nœud `term`, avec son propre `lemma`, et le rapport l'a signalé en
  lien mort ;
- celui du §3 ==n'a rien produit==. Le §2.5 a la préséance sur le §3 pour la
  définition (`reference.rs`), et le terme témoin avait déjà sa puce : sa case du
  §3 n'était pas lue.

Le §3 mord donc lui aussi, mais ==seulement pour les termes qui n'ont pas de
puce au §2.5== — ceux dont il fournit la définition. La prudence est de traiter
les deux, ce que la passe du 25 août avait fait.
