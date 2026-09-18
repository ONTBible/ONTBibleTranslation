# La base de connaissances de travail ONT

Cette base aide un assistant à préparer une tâche avec les connaissances et
les preuves pertinentes : grammaire, concepts, histoire, sources,
interprétations, décisions et méthodes. Elle relie des notices de référence,
les fiches du vault, les conventions et les témoins disponibles sur disque.

## Partir d’une tâche

```sh
python3 knowledge/consulter.py dossier 'Préparer la traduction de Gen.1.1 et vérifier sa morphologie' --format markdown
python3 knowledge/consulter.py dossier 'Distinguer geveret et gevirah et retrouver le choix en attente' --format markdown
python3 knowledge/consulter.py dossier 'Le piel implique-t-il toujours une intensité ?' --format markdown
python3 knowledge/consulter.py dossier 'Un participe se traduit-il toujours au présent ?' --format markdown
python3 knowledge/consulter.py dossier 'Que désignent sujet prédicat et objet dans un triplet RDF ?' --format markdown
python3 knowledge/consulter.py dossier 'Déduire la forme de dictionnaire en retirant un article hébreu : attestations et limites de la mesure' --format markdown
```

Le dossier contient les notices sélectionnées, les extraits originaux avec
leurs emplacements, les attributions et, si la demande donne une référence
source explicite, ses témoins. Il signale les passages coupés ou non fournis.
`--budget` limite les caractères de contexte ; ce n’est pas un compte de tokens.
`--stdin` permet de fournir une tâche sans l’interpoler dans une commande shell.

Le moteur est lexical, avec un vocabulaire de recherche et des parcours
éditoriaux déclarés. Il ne prétend pas comprendre toutes les paraphrases. Les
résultats préparent le travail du LLM ; ils ne sont pas une réponse déjà jugée.

## Consulter les connaissances et les témoins

| Besoin | Commande après `python3 knowledge/consulter.py` |
|---|---|
| Voir les domaines et notices | `catalogue` |
| Lire une notice et sa source complète | `notion KB-0006` |
| Lire une fiche du vault | `fiche qahal` |
| Chercher dans les documents du vault | `chercher 'qahal nom verbe'` |
| Voir les déclarations d’une fiche | `liens qahal` |
| Voir un verset dans les éditions disponibles | `reference Gen.1.1` |
| Compter et examiner un lemme hébreu | `occurrences H6951 --limite 5` |
| Restreindre les occurrences à un livre | `occurrences H1254 --livre Gen` |
| Conserver un homonyme annoté | `occurrences H1254a` |
| Consulter un Strong grec dans RP | `occurrences G746` |
| Examiner les variantes d’édition | `apparat Mt.1.5` |
| Agréger le pont hébreu vers grec | `pont H1254` |
| Obtenir le graphe des notices et du lexique | `graphe --lexique` |
| Mesurer la couverture présente | `inventaire` |

Les sorties ordinaires sont du JSON. Le graphe se reconstruit depuis les
sources ; aucun fichier de triplets ne devient une seconde version manuelle.
Les comptages parcourent les fichiers déclarés et conservent des exemples,
leur référence et leur position. Les formes et annotations originales sont
restituées telles qu’elles sont stockées.

Les références attendues sont celles des sources : `Gen.1.1`, `Mt.1.5`,
`ChazonEzra.7.106`. Un numéro interne ONT n’est pas converti implicitement.
La collection grecque SBLGNT fournit ici des lemmes, mais pas de numéros Strong :
la commande d’occurrences grecques mesure Robinson-Pierpont et le dit.

## Ce qui constitue une connaissance

`contenus.json` est l’emplacement de référence des nouvelles notices. Deux
formes sont possibles :

- Une **synthèse documentaire** apporte un repère nouveau, écrit pour le
  travail de l’assistant, avec une source extérieure identifiée et sa portée.
- Un **renvoi au document** donne un accès thématique à une connaissance déjà
  écrite dans le vault. Son contenu est lu dans la section source à chaque
  appel, sans paraphrase manuelle à maintenir.

Chaque notice a un identifiant opaque `KB-…`, un domaine, un titre, des mots
de recherche, un statut et des sources. Une ancre locale est vérifiée contre
le titre de la section. Si elle disparaît ou devient ambiguë, le contrôle
échoue et le dossier signale la source manquante. Un déplacement de lignes
est pris en compte à la lecture.

Les sources web indiquent leur titre, leur adresse, leur attribution, la date
de consultation et une limite d’utilisation intellectuelle. Les synthèses
initiales de grammaire s’appuient sur la documentation OSHB et sur plusieurs
sections de Gesenius–Kautzsch–Cowley. Cette grammaire de 1910 est une référence
historique, pas une garantie de consensus contemporain. Les repères historiques
proviennent de l’Israel Antiquities Authority. Les distinctions entre entrée,
forme et sens sont documentées par OntoLex.

Le statut `renvoi_au_document` ne signifie pas « vrai » ou « définitivement
décidé ». Une section peut porter une lecture ONT, une réserve, une décision
ancienne ou une contradiction. Le LLM doit lire son attribution et son
contexte. La KB ne transforme pas une hypothèse en fait attesté.

## Ce que le graphe représente

Les nœuds actuels distinguent notice, domaine, source web, section documentaire,
fiche, forme déclarée, numéro déclaré et cible non résolue. Les relations disent
qu’une notice relève d’un domaine, qu’elle se documente dans une source,
qu’une fiche déclare une forme ou renvoie à une autre fiche. `consulter_avec`
est un parcours éditorial explicite.

Les deux Chanokh restent deux fiches. Une fiche qui déclare plusieurs numéros
ne devient pas automatiquement un lexème unique. Les identifiants des notices
sont persistants ; ceux des fichiers et formes décrivent l’état courant du
vault et peuvent changer à sa régénération. Les relations de parenté, les
étymologies et les dépendances de rédaction ne sont pas déduites d’un wikilien.

`graphe --lexique` inclut les déclarations des fiches ; `graphe` seul porte
les notices et leurs sources. L’extraction de `## Source` est partagée avec
`liens` : `1471 a` garde son suffixe, et `2896 a + 3966` produit deux relations.
`1471`, `1471 a` et `1471 b` restent trois références distinctes. La preuve
conserve la ligne originale et son empreinte. Deux fiches partageant une
référence ne sont pas automatiquement fusionnées ou déclarées fautives ;
une fiche sans `## Source` ne reçoit aucun numéro supposé.

## Raccordement aux assistants

Dans les sessions ouvertes dans ce dépôt :

- Codex charge `AGENTS.md`, qui demande la consultation pour les tâches de
  traduction, d’explication, de recherche et d’audit du corpus.
- Claude Code importe `ASSISTANTS.md` depuis `CLAUDE.md`. Le réglage partagé
  `.claude/settings.json` ajoute un hook `UserPromptSubmit` : il construit un
  dossier pour le message reçu et le fournit en contexte supplémentaire.

Le hook est local, sans réseau ni génération payante. Il ne bloque pas les
messages, ignore les salutations, accusés de réception et relances sans sujet
reconnus comme messages entiers, annonce une erreur de consultation
et ne modifie aucun texte. Les réglages privés de l’utilisateur sont conservés.
Il utilise le checkout actif lorsqu’un worktree est reconnu.

La configuration est écrite dans le projet ; son activation dans une session
Claude déjà ouverte dépend du chargement des réglages et de la confiance
accordée au projet. Le script et son contrat JSON sont éprouvés localement.
Aucune session LLM payante n’est lancée par la suite de tests. Pour vérifier
le chargement réel, ouvrir une session dans ce dépôt et consulter les fichiers
d’instructions ou la liste des hooks chargés.

Le 16 septembre 2026, la session Claude du vault a confirmé recevoir les
dossiers injectés pendant une revue coordonnée via Herdr. Cette observation
concerne cette session ; elle ne valide pas le chargement dans Codex ni dans
les sessions des autres dépôts. La revue a aussi relevé du contexte peu
pertinent sur des messages de coordination. Le filtrage du 17 septembre écarte
les formules courtes comme « bien reçu, les tests passent ». Un message qui
contient aussi une question de corpus reste consulté. Les comptes rendus longs
passent toujours par le moteur lexical ; leur pertinence reste à améliorer.

Les sessions ouvertes dans `ONTBibleApp`, `ONTBibleWebapp` ou leur dossier
parent ne sont pas configurées par ces seuls fichiers. Leur raccordement
reste séparé de celui du vault.

Codex propose également un événement `UserPromptSubmit` compatible avec la
sortie JSON du script. `codex-hooks.proposition.json` prépare ce raccordement
pour le vault : sa commande est testée, mais le fichier n’est pas installé dans
`.codex/hooks.json`, ce dossier étant protégé dans cette session. Le nom
`claude-hook.py` est conservé ; le contrat utilisé est commun aux deux outils.
Après installation dans une session autorisée, le hook doit être examiné et
validé dans `/hooks`. Ne pas écraser d’éventuels hooks existants ni installer
plusieurs copies héritées du même raccordement.

Les commandes `python3 knowledge/preparer-raccordement.py` et
`python3 knowledge/preparer-journal.py` préparent les changements des voisins
et la revue des journaux dans `knowledge/preparation/`, sans les appliquer.
La préparation des raccordements inclut les hooks Codex pour la racine et
les trois dépôts, avec les textes proposés et les empreintes des destinations.
Les commandes peuvent être éprouvées sans installer leurs fichiers ; cette
épreuve ne remplace pas le contrôle du chargement dans les applications.
Le [relevé de synchronisation](synchronisation-a-terminer.md) précise ce qui
reste à vérifier.

`python3 knowledge/reconcilier-journal.py` prépare ensuite le journal commun
avec les résolutions relues dans `journal-resolutions.json`. Il refuse une
variante nouvelle et conserve les décisions, leurs origines et les textes
écartés. `knowledge/preparation/journal-reconcilie.txt` est consultable ; le
JSON associé contient aussi les propositions de conservation des notes
locales. Ces notes doivent être préservées avant de remplacer un journal.
La commande ne modifie aucune destination.

Documentation des mécanismes consultée : [instructions Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[mémoire Claude Code](https://code.claude.com/docs/en/memory),
[hooks Claude Code](https://code.claude.com/docs/en/hooks).
Le mécanisme Codex et sa validation sont décrits dans les
[hooks Codex](https://learn.chatgpt.com/docs/hooks).

## Enrichir sans perdre la provenance

### Mesurer les consultations

`python3 knowledge/consulter.py usage` restitue le compteur de lancements.
Les appels directs portent leur sous-commande ; les consultations automatiques
du hook portent `hook:dossier`. Les salutations et confirmations filtrées ne
comptent pas comme consultations. Le compteur ne conserve ni le message ni les
arguments : seulement la date à la minute, la commande, l’identifiant de socket
disponible et le démarrage de la machine.

Le journal `.kb-usage.jsonl` se trouve dans le dossier parent du vault. Si ce
dossier est inaccessible en écriture, la consultation fonctionne mais n’est
pas comptée.
Un zéro ne suffit donc pas à conclure à une absence de consultation.

Un lancement de test est également un lancement : `hook:dossier` ne prouve pas
à lui seul qu’une application a chargé son hook, ni qu’un LLM a utilisé les
preuves rendues. Il faut rapprocher le relevé de l’observation dans la session.
Une socket absente est notée `—` ; elle ne distingue pas les sessions concernées.

Pour une annonce uniquement technique entre sessions, commencer par
`[Nom, message de pair, coordination technique]` désactive explicitement le
dossier automatique et son comptage. Ne pas employer ce marqueur pour une
question sur le corpus ; un simple `[Nom, message de pair]` conserve la recherche.
Le hook ne sait pas déduire de façon fiable la pertinence d'un message de
coordination : sans ce marqueur, des mots communs peuvent ramener des notices
hors sujet. La commande `dossier` reste utilisable explicitement.

**Rupture de mesure :** le filtre de coordination a été introduit dans le
commit `e724cc5` (PR #123, 18 septembre 2026). Sa date de création n'est pas
sa date d'activation : chaque session utilise le script de son checkout.
Avant son activation, une annonce marquée pouvait produire `hook:dossier` ;
après, elle est exclue. Les anciennes entrées ne portent pas de version du
filtre et ne permettent pas de retrouver cette frontière. Ne pas interpréter
une baisse de ce compteur comme une baisse d'usage, ni comparer des périodes
qui traversent un changement de script sans relever sa version et son
activation dans les sessions concernées.

Le préfixe se place au début du message envoyé. Herdr le transmet directement.
Pour SendMessage, le hook extrait les corps des enveloppes
`cross-session-message` avant la recherche : les chemins de socket, noms
d'agents et l'avis standard du transport ne deviennent plus des mots-clés.
Dans un lot, seules les annonces explicitement marquées sont exclues ; une
question de corpus dans une autre enveloppe conserve son dossier. Cela change
uniquement l'entrée de recherche, pas le prompt ni les règles reçus par
l'assistant. Un format inconnu ou du texte extérieur au lot reste intact pour
ne pas supprimer une question. Les variantes rapportées par la manageuse le
18 septembre sont éprouvées par des fixtures ; leur activation native reste à
constater après installation.

### Compléter les notices

La grammaire comprend aussi des repères UHG sur qatal, yiqtol, niphal, hiphil,
le marqueur d’objet, les formes volitives et l’ordre des mots. Les notices
documentaires distinguent cote et composition, langue et écriture, lacune,
lecture incertaine, restitution et correction éditoriale. Leurs sources et
leurs limites sont conservées avec chaque synthèse.

Les notices KB-0071 à KB-0073 traitent la dérivation d’une forme sans article :
formes de l’article selon UHG, dagesh initial en contexte selon GKC §21,
et choix lexicographique d’une forme de citation selon OntoLex. Elles
distinguent les descriptions des sources de leur application à l’audit ONT.
Les questions d’évaluation vérifient aussi la présence des réserves : retrouver
une forme attestée ou majoritaire ne prouve pas sa qualité de forme de citation.

Ajouter une notice au domaine concerné, avec un nouvel identifiant. Quand le
fait existe déjà, déclarer son ancre. Pour un apport extérieur, rédiger une
synthèse attribuée après consultation du passage pertinent ; ne pas recopier
un chapitre ou inventer une référence. Garder les limitations et les lectures
concurrentes. Ajouter des mots de recherche correspondant aux questions
réellement posées, puis une question d’évaluation avec ses preuves attendues.

L’extension reste ouverte : morphosyntaxe plus détaillée, lexicographie comparée,
histoire des textes, témoins fragmentaires, bibliographie et divergences
d’interprétation. La taille seule n’est pas le critère : la base doit aider à
résoudre une tâche avec des éléments vérifiables.

## Vérification et limites

```sh
python3 knowledge/consulter.py verifier
python3 -m unittest discover -s kb-prototype -p 'test_*.py'
python3 -m unittest discover -s knowledge -p 'test_*.py'
python3 knowledge/evaluer.py
python3 knowledge/evaluer.py --hook
python3 knowledge/evaluer.py --hook --hook-config knowledge/codex-hooks.proposition.json
```

La CI exécute ces contrôles. Ils vérifient les sources, les renvois, les bornes
de contexte, les homonymes, les comptes, les variantes, le graphe et le contrat
du hook. L’évaluation de questions du corpus mesure la récupération des preuves,
pas l’exactitude générale d’un modèle de langage.

Le mode `--hook` exécute la commande présente dans le fichier indiqué, depuis
un sous-dossier du vault, avec le message transmis par JSON sur l’entrée
standard. Utiliser uniquement un fichier de configuration relu : cette option
exécute ses commandes. Elle contrôle les notices effectivement restituées,
leurs preuves et leurs attributions avec le budget du hook. Elle n’ouvre pas
de session LLM et ne démontre pas que l’application a chargé ou autorisé le hook.
L’évaluation ajoute six messages sans tâche en mode hook et exige qu’ils ne
produisent aucun contexte ; deux questions précédées d’une formule de
coordination contrôlent que le filtrage conserve le besoin documentaire.

L’apparat SBLGNT compare des éditions imprimées. Le pont Septante est un
alignement provisoire et ne restitue aucun texte grec. Une source absente ne
prouve pas que l’événement, la forme ou le passage n’existe pas ailleurs.

Le point encore incomplet de synchronisation est documenté dans
`synchronisation-a-terminer.md`. Aucun journal voisin n’a été écrasé.
