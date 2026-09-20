# Les sept rôles — se trouver sans se nommer

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « Les sept rôles — se trouver sans se nommer », partie 1. Empreinte de la section : `9361a25990792135`. Régénérer : `python3 knowledge/decouper.py`.*

**Posé le 7 septembre 2026, à la demande de l'auteur** : « je veux que vous
communiquiez toutes l'une à l'autre pour vous connaître ». Les sept sessions se
sont présentées, et la carte vit ici plutôt que dans leurs mémoires : ce fichier
est le même dans les trois dépôts et le contrôle de concordance compare les
exemplaires — une carte qui y vit ne peut pas diverger. Sept mémoires le
peuvent, et le feraient.

**Par rôles, jamais par noms de session.** La collecte l'a démontré : les
annuaires ne sont pas partagés — chaque session voit les autres sous des noms
propres à son propre `ListAgents`, et deux sessions se sont désignées toute une
semaine par des noms que l'autre ignorait. Un registre de noms serait donc faux
pour six lecteurs sur sept au moment même de l'écrire. Les rôles sont la seule
chose que tout le monde voit pareil — c'est d'ailleurs ainsi que l'auteur les a
énumérés. Qui tient un rôle *aujourd'hui* se relève par `ListAgents`, en disant
depuis quel annuaire on nomme.

- **La manageuse** — travaille depuis la racine `~/ONTBible`, seul endroit d'où
  les trois dépôts se voient. Tient la concertation, la synchronisation
  inter-dépôts et l'outillage de la machine (l'espace disque, les règles
  communes). À joindre pour : tout ce qui traverse plus d'un dépôt, un registre
  ou une carte à diffuser, une règle commune (rulesets, CI exigée), le disque.

- **Le vault** — `ONTBibleTranslation` sur `main` : le `CLAUDE.md` (balisage
  §2.5 / §2.5 bis / §2.10, glossaire §3), les fiches de `lexique/`,
  `corpus-order.md`, la rédaction des **parashiot**, des introductions et des
  fiches ; l'index `DECISIONS.md` (`scripts/decisions.py`) et les contrôles de
  `pipeline/src/controles.rs`. À joindre pour : toute prose que le lecteur
  lira, toute question de balisage ou de glossaire — et « cette décision
  a-t-elle été prise ? » se demande d'abord à `scripts/decisions.py <mot>`.

- **Les langues sources** — importe les textes en hébreu, grec, guèze et
  latin, les joint aux unités ONT et les émet dans `dist/sources/` ; tient les
  permissions auprès des éditeurs et des projets savants. À joindre pour :
  `sources/` dans le vault, et la couche source dans l'app comme sur le site.
