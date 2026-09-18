# 2 septembre 2026 — le pipeline d'un arbre périmé rend un rapport faux

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « 2 septembre 2026 — le pipeline d'un arbre périmé rend un rapport faux », partie 3. Empreinte de la section : `a165bcf57accca3a`. Régénérer : `python3 knowledge/decouper.py`.*

Et l'app ne reste pas muette devant un lemme absent : elle ouvre une feuille et
écrit *« Terme non documenté — ce mot est balisé dans le texte mais n'a pas
encore d'entrée dans le glossaire »*. ==C'est faux== : l'entrée existe, sous le
lemme du singulier. **Un lien mort qui ne fait rien est un défaut ; un lien mort
qui affirme une lacune inexistante est une perte de confiance** — le lecteur en
conclut que le glossaire est plus creux qu'il n'est, cent vingt-six fois.

**Le remède est à l'émission, non chez les consommateurs**, et la raison vaut
d'être gardée : corriger côté app en indexant `forms` obligerait chaque
plateforme à réécrire sa propre version de `slugify` pour faire se rejoindre
`malʾakhim` et `malakhim`. ==Deux normalisations écrites séparément divergent==,
et le défaut deviendrait intermittent au lieu d'être systématique — pire que
maintenant. Le pipeline, lui, tient les deux au moment d'émettre : la forme
rencontrée et l'entrée qu'elle désigne.

**Décision réservée à l'auteur**, parce que le pipeline sert les trois
plateformes : une correction de normalisation change ce que le site compile
autant que ce que l'app lit.

Corollaire de méthode, gagné en se trompant : **une hypothèse réfutée par un
pair est le meilleur moment pour remesurer**, pas pour clore. La réfutation
était juste et le défaut existait quand même — deux étages plus bas.
