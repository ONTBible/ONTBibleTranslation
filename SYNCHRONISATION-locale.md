# Journal local du vault ONT

### 14 septembre 2026 — la KB prépare les tâches avec leurs preuves *(local)*

La consultation locale passe du prototype lexical à une entrée par tâche.
`knowledge/consulter.py` assemble notices, conventions, fiches et témoins, avec
les sources et les limites des extraits. Les notices couvrent grammaire,
concepts, histoire, sources, interprétations, décisions et méthodes. Le contenu
déjà présent est lu à son emplacement ; les synthèses nouvelles sont attribuées.

Le moteur consulte aussi les occurrences annotées, l’apparat SBLGNT et les
agrégats du pont Septante. Le graphe reste documentaire : une fiche n’est pas
assimilée à un lexème, un renvoi n’est pas une parenté. Les deux Chanokh restent
distincts, et les deux numéros déclarés dans qahal sont conservés.

`AGENTS.md` donne l’entrée à Codex. `CLAUDE.md` importe le guide partagé et un
hook de projet prépare du contexte pour les nouveaux messages de Claude Code.
Leur configuration concerne ce dépôt ; les réglages personnels sont préservés.
Le contrat du hook est testé avec des événements JSON, sans lancer de génération
LLM. Le contrôle de contenu et les épreuves de récupération entrent dans la CI.

Le contrôle du journal commun constate une divergence antérieure dans les
dépôts voisins. Leur réconciliation et le raccordement des sessions qui y sont
ouvertes restent nécessaires ; `knowledge/synchronisation-a-terminer.md` porte
le relevé et la matière à transmettre. Cette entrée locale ne déclare pas la
synchronisation accomplie.

### 15 septembre 2026 — les raccordements voisins sont préparés pour revue *(local)*

Deux outils préparent les neuf changements d’instructions et de réglages des
assistants, ainsi que les variantes de dix journaux. Ils conservent les
préimages et n’écrivent que dans le dossier de préparation du vault. Les tests
vérifient la préservation des réglages existants, l’absence de doublons et
l’absence d’écriture dans les destinations pendant la préparation.

Sur dix-neuf différences de corps relevées, dix ne changent que le séparateur
Markdown final. Les neuf autres touchent des translittérations, y compris dans
des exemples historiques de défauts. Aucun texte n’a été choisi par majorité.
Le hook retrouve désormais le vault depuis un dépôt voisin, avec un test de ce
parcours. La configuration des voisins demeure non appliquée et le chargement
dans une session Claude active demeure non vérifié.

### 15 septembre 2026 — enrichir la KB et vérifier le contexte réellement transmis *(local)*

Dix-neuf synthèses attribuées portent le catalogue à 54 notices : les notions
RDF, SKOS, OWL, SHACL et PROV complètent les concepts de la base elle-même ;
l’infinitif construit, le participe et les négations enrichissent la grammaire.
Les références grammaticales de 1910 restent explicitement datées et limitées.

Les 25 questions d’évaluation retrouvent leurs preuves dans le dossier et
dans la sortie du hook Claude configuré. Ce dernier contrôle a révélé que le
rendu Markdown omettait l’attribution et la date des sources externes : elles
sont maintenant transmises. Une provenance externe manquante est signalée
sans empêcher le dossier de fournir ses autres preuves.

Le même contrat de hook est documenté pour Codex. Sa configuration proposée
réussit les 25 questions depuis un sous-dossier, mais `.codex/hooks.json` ne
peut pas être installé dans cette session. Aucun de ces tests ne prétend
prouver le chargement dans une session LLM active. Les tests unitaires sont
également au vert : 18 pour la KB et ses préparations, 7 pour le prototype.

### 15 septembre 2026 — grammaire, témoins et préparation des quatre hooks Codex *(local)*

Seize notices supplémentaires portent le catalogue à 70. Les distinctions
grammaticales sont documentées par les articles UHG ; l’IAA documente les
cotes, les genres, les langues et les écritures ; la TEI documente les états
de transcription. Les synthèses conservent l’attribution et la portée des
références sans importer leurs tableaux ni transformer un format documentaire
en nouvelle convention ONT.

Les 41 recherches d’évaluation passent dans le dossier et dans les deux
commandes de hook du vault. Les préparations pour la racine, l’app et le site
incluent désormais Codex : treize changements proposés au total. Les sept
commandes proposées retrouvent la notice KB-0067 depuis leurs destinations
ou un sous-dossier existant ; les préimages restent inchangées. Aucun fichier
de configuration n’a été installé chez les voisins ni dans `.codex`.

Les tests unitaires passent : 19 pour la KB et la préparation, 7 pour le
prototype. La validation native des hooks et la réconciliation du journal
commun restent nécessaires avant de déclarer le raccordement accompli.

### 15 septembre 2026 — le journal commun est réconcilié en proposition, avec ses notes locales *(local)*

`knowledge/reconcilier-journal.py` assemble les 79 entrées examinées. Les neuf
variantes de contenu retiennent la graphie historique attestée dans un commit
local de l’app ; les choix et leurs empreintes sont fixés dans
`knowledge/journal-resolutions.json`. Une variante non relue bloque la
préparation. Le préambule réunit les ajouts indépendants du vault et du Mac.

Quatre copies portent encore onze notes locales chacune. Leur conservation
dans des journaux locaux est proposée avant tout remplacement du tronc,
sans modifier les fichiers existants. Les corps, les sous-sections et les
préimages sont conservés. Les titres identiques de contenu différent sont
signalés comme conflits. Les tests éprouvent aussi la conservation des notes
déjà séparées et l’absence de doublons lors d’une seconde préparation.

Les contrôles passent : 70 notices valides dans sept domaines, 22 tests pour
la KB et ses préparations, 7 pour le prototype. Aucun journal voisin n’a été
écrit. Le raccordement des autres dépôts, la validation native des hooks et
la concordance effective restent à réaliser dans un environnement autorisé.

### 16 septembre 2026 — les références suffixées reviennent dans le graphe après revue croisée *(local)*

Travail coordonné avec la session Claude du vault : Astra corrige le moteur,
Claude relève les déclarations réelles puis valide avec un extracteur
indépendant, en lecture seule. La branche observée est `la-famille-de-qahal`,
HEAD `9b9b14d` ; le travail KB reste non committé au moment de cette mesure.

Les commandes `liens` et `graphe --lexique` rejetaient les lignes de `## Source`
portant un suffixe OSHB. Une ligne composée perdait aussi son élément sans
suffixe : `lev` perdait `3824`, `tov-meʾod` perdait `3966`, `ʾel-ʿelyon` perdait
`410`. Leur lecture est maintenant partagée dans `source_declaree()` ; les
suffixes a, b et c restent distincts et chaque élément séparé par + porte sa
propre relation. La ligne originale demeure la preuve.

Le graphe passe de 315 à 365 relations de numéro source, sur 354 fiches.
L’oracle indépendant de Claude confirme zéro référence perdue et zéro
référence ajoutée ; il contrôle aussi sept preuves et huit concordances entre
`liens` et `graphe`. Les 84 fiches sans `## Source` ne reçoivent aucun numéro
supposé. Les arbitrages `goy`/`goyim` et `tov`/`tov meʾod` restent ouverts.

Les 70 notices passent le contrôle de structure et de références ; les tests
passent, 9 pour le prototype et 23 pour la KB et ses préparations. Le lexique,
les textes et les interfaces de corpus consommées par les voisins ne changent
pas. Le journal commun et les raccordements voisins ne sont pas installés par
ce travail. Claude confirme la réception du contexte du hook dans sa session,
tout en relevant du bruit sur les messages de coordination. Ce point reste
distinct de la correction Strong et du raccordement Codex encore proposé.

### 17 septembre 2026 — trois repères pour vérifier une dérivation *(local)*

La KB passe de 70 à 73 notices. KB-0071 distingue la voyelle de l’article de
celle du nom, KB-0072 conserve le contexte accentuel du dagesh initial,
KB-0073 distingue forme majoritaire, forme attestée et forme de citation.
Sources relues : UHG sur l’article, GKC §21 a–d et OntoLex §3.2. Les applications
à l’audit sont signalées comme telles ; aucun taux historique n’est consacré
par ces notices. Aucun texte de traduction ni déclaration Strong n’est modifié.

Validation : 73 notices valides, 27 tests KB et préparation, 9 tests du
prototype. Les 45 questions de récupération passent en consultation directe,
par la commande Claude configurée et par la proposition Codex. Ce dernier
contrôle ne prouve pas un chargement natif dans Codex.

Les préparations datées du jour dans `knowledge/preparation/` constatent encore
13 changements de raccordement à appliquer. La revue des journaux lit 11
copies, 82 entrées distinctes et 20 divergences, dont 11 limitées au séparateur
final. Les neuf résolutions de contenu restent applicables après contrôle des
empreintes ; la proposition du journal est régénérée pour les 82 entrées.
Aucune destination voisine n’a été écrite.
Herdr permet de lire la session Claude du vault, mais l’envoi d’un message
est refusé par les permissions présentes. La concertation et l’installation
restent à reprendre dans un environnement autorisé.

### 17 septembre 2026 — le hook distingue une réception d’une question *(local)*

`knowledge/claude-hook.py` n’ajoute plus de dossier pour les formules entières
de réception ou de relance reconnues, par exemple « merci, j’ai bien reçu »
et « bien reçu, les 36 tests passent ». Une question ONT ajoutée à ces formules
déclenche toujours la recherche. Aucun expéditeur n’est exclu ; le filtrage
ne prétend pas classer les comptes rendus longs par leur sens.

Validation : 29 tests KB et préparation, 9 tests du prototype, 73 notices
valides. Les 47 questions documentaires passent en direct et dans les deux
commandes de hook ; six messages supplémentaires exigent leur silence, soit
53 cas par hook. La validation native dans les autres sessions reste ouverte.

Ce changement concerne les assistants qui exécutent ce script partagé, sans
modifier le corpus ni ses interfaces. Les configurations voisines et le
journal commun restent à installer avec les droits requis. La proposition
de migration des journaux locaux est régénérée pour conserver cette entrée.

Contrôle complémentaire des raccordements : les sept commandes proposées
passent 28 cas depuis leurs destinations et sous-dossiers. Les 13 préimages
restent identiques ; aucun fichier n’a été installé. Le rapport daté dans
`knowledge/preparation/raccordement-verifie-2026-09-17.json` garde les empreintes
du script et des notices testés. Le contrôle de concordance réel retourne 1 ;
les quatre troncs principaux restent différents. La suite nécessite les
droits d’installation et l’accès aux sessions pour éprouver leur usage réel.

### 18 septembre 2026 — les consultations du hook entrent dans le compteur *(local)*

La PR #117 a ajouté le journal des lancements de `consulter.py`. Le hook
appelait directement `dossier()` et échappait donc à cette mesure : KB-0006
était rendu pour une question sur le piel, avec zéro appel à `journaliser`.
Il journalise désormais `hook:dossier` après son filtrage et la résolution du
vault. Aucun message ni argument n’est conservé. Un journal inaccessible
n’empêche pas la consultation ; les salutations filtrées ne sont pas comptées.

Deux tests couvrent l’appel réel du hook, la confidentialité du journal,
l’absence de comptage des salutations et la continuité du dossier en cas
d’échec d’écriture. Le parent du vault de test appartient désormais à sa
fixture : le compteur n’écrit plus dans un fichier temporaire commun aux tests.
Les 33 tests KB et les 9 tests du prototype passent ; les 73 notices sont valides.

Les propositions sont actualisées pour le `CLAUDE.md` parent modifié et les
16 journaux présents : 13 raccordements attendent toujours leur installation,
83 entrées communes sont assemblées et 77 notes locales sont à préserver dans
sept migrations. Les voisins ne sont pas modifiés. L’annonce à Claude via
Herdr est refusée par les permissions. Le compteur est lui-même incomplet
ici tant que l’écriture dans le parent du vault reste interdite ; les tests
de commandes ne prouvent pas le chargement des hooks dans les applications.
