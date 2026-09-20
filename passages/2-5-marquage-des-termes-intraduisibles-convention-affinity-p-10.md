# 2.5 Marquage des termes intraduisibles — convention Affinity Publisher

*Passage engendré — ne pas éditer. Source : `CLAUDE.md`, section « 2.5 Marquage des termes intraduisibles — convention Affinity Publisher », partie 10. Empreinte de la section : `0d61da19ae2530b5`. Régénérer : `python3 knowledge/decouper.py`.*

**Pourquoi il fallait l'écrire.** Le document portait 337 gras d'insistance, et
==la phrase qui interdit le gras d'insistance en emploie trois==, dont un sur le
mot « accentuation », dans la clause même qui renvoie à `==…==`. Une règle que
son propre porteur viole à chaque page n'est pas violée : elle a ==un périmètre
que personne n'a écrit==. C'est exactement la forme du §2.9 — une pratique non
écrite ne se compare à rien, donc elle ne peut pas diverger visiblement. Elle est
écrite maintenant.

**Polices hébraïques — dossier `utilities/`.** Les polices pour composer le script hébreu (niveau 3) et le rendre dans Affinity Publisher vivent dans `utilities/` à la racine du dépôt : **SBL Hebrew** (`SBL_Hbrw.ttf`) et **Ezra SIL** (`EzraSIL2.51/`) — hébreu biblique avec voyelles et cantillation (*teʿamim*) ; **Taamey Frank CLM** (projet Culmus) — hébreu avec *teʿamim* ; **Frank Ruhl Libre** — hébreu moderne (fonte variable + statiques). **Attention aux licences** : Ezra SIL et Frank Ruhl Libre sont sous OFL, donc redistribuables — ce sont les deux que La Bible ONT embarque. SBL Hebrew relève d'un EULA propriétaire et Taamey Frank CLM d'une GPL dont l'exception ne couvre que les documents composés, pas un binaire : ces deux-là restent réservées à la composition Affinity et ne doivent jamais entrer dans une app ni dans un site. Ce sont les **assets typographiques** du projet, suivis dans le dépôt pour la composition — non distribués au lecteur (cf. principe de distribution : seuls l'intro et les chapitres du slot voyagent).
