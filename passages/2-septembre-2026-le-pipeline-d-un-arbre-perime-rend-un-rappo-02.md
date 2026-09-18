# 2 septembre 2026 — le pipeline d'un arbre périmé rend un rapport faux

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « 2 septembre 2026 — le pipeline d'un arbre périmé rend un rapport faux », partie 2. Empreinte de la section : `a165bcf57accca3a`. Régénérer : `python3 knowledge/decouper.py`.*

- **Une forme dérivée s'émet elle-même comme lemme.** `**gibborim**` sort en
  `lemma: "gibborim"`, quand l'entrée s'appelle `gibbor` et déclare
  `forms: [gibbor, gibborim, gibor]`. Le rapport dit « 0 mot d'or sans fiche »
  parce que **lui** traverse `forms` ; le nœud livré, non. Et pour une partie
  d'entre elles la traversée ne suffirait pas : `forms` garde le texte brut —
  `malʾakhim`, `leʿolam`, `kohen gadol` — tandis que `lemma` est passé par
  `slugify`, qui **laisse tomber l'apostrophe sans séparateur**. `malʾakhim`
  devient `malakhim`, qui n'est dans aucune liste de formes. Ces liens-là sont
  morts quel que soit le consommateur : **25 occurrences pour le seul
  `malʾakhim`, dans des corps de chapitre.**
- **Une fiche citée seulement par d'autres fiches est écartée de l'index — et
  les liens vers elle continuent d'être émis.** `shem-fils-de-noach` est visé
  **37 fois** et `kasdim` **6 fois** depuis d'autres fiches ; ni l'un ni l'autre
  n'entre dans `shemot.json`. C'était bien un chemin de traversée qui ne voit
  pas une source, mais ce n'est pas celui que j'avais nommé : ce n'est pas le
  *rendu* qui rate les fiches, c'est le **critère d'inclusion**.

**Pour les trois dépôts :** un rapport qui rend `0` peut être exact et
n'attester de rien pour le lecteur, parce qu'il **normalise autrement que le
consommateur**. Le rapport résout la forme dérivée ; le fichier livré ne la
résout pas. La mesure qui compte n'est pas « le contrôle passe » mais
**« chaque lien émis retombe-t-il sur une entrée du même fichier »** — et elle
se fait sur `dist/`, pas sur le rapport.

**Confirmé indépendamment, et c'est pire que des liens morts.** La session app
a mesuré de son côté, sur un corpus plus ancien : `126` morts dans les corps et
`131` dans les fiches, ==les mêmes coupables==. Et elle a lu le consommateur :

    LexiconModel.swift:24   byLemma = Dictionary(entries.map { ($0.lemma, $0) }, …)
    LexiconModel.swift:36   func entry(_ lemma: String) -> GlossaryEntry? { byLemma[lemma] }

**Lemme exact, rien d'autre** — le consommateur ne traverse pas `forms`. La
première cause vaut donc les 133, non les quatre.
