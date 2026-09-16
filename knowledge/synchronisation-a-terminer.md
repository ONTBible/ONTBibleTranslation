# Raccordement et journal commun — état du 15 septembre 2026

L’objectif conserve le raccordement des assistants et la synchronisation du
journal entre dépôts. Les fichiers de configuration créés ici concernent le
vault. Le journal local consigne ce qui y fonctionne ; le travail commun ne
doit pas être déclaré terminé.

## État vérifié

`python3 scripts/concorder-la-synchronisation.py` retourne 1. Il trouve trois
versions du tronc commun dans les dépôts, et une quatrième dans la racine.
Le défaut précède les modifications de la KB : `SYNCHRONISATION.md` n’a pas
été changé pendant ce travail.

| Exemplaire principal | Empreinte du tronc, préfixe relevé |
|---|---|
| Racine `~/ONTBible/` | `004b40f443e3` |
| ONTBibleApp | `d89bfe6f4158` |
| ONTBibleTranslation | `f2015afafa25` |
| ONTBibleWebapp | `a694f1a24193` |

Le contrôle relève également les worktrees. Il refuse de désigner une copie
majoritaire comme référence ou de réaligner la racine tant que les dépôts
divergent. Les empreintes ci-dessus sont un constat daté ; relancer le contrôle
avant toute réconciliation.

Le workflow du vault `.github/workflows/journal.yml` décrit une propagation
future depuis le vault. Le receveur correspondant est absent du checkout
principal de l’app examiné. L’existence du workflow émetteur ne prouve donc
pas qu’une propagation est opérationnelle.

## Ce qui reste nécessaire

1. Régénérer et relire la proposition de journal commun et ses migrations
   locales. Les divergences examinées ont des résolutions explicites ; toute
   nouvelle variante exige une nouvelle revue. Préserver les notes locales
   avant de remplacer leurs journaux sources.
2. Inscrire l’arrivée de la KB dans le tronc commun réconcilié, puis propager
   ce tronc aux dépôts et worktrees concernés. Aligner la racine en dernier.
3. Raccorder les instructions des assistants ouverts depuis les autres dépôts
   ou le dossier parent à la KB du vault. Utiliser le guide existant et le
   chemin du vault ; éviter une copie manuelle des connaissances.
4. Vérifier le chargement dans les assistants concernés, puis relancer le
   contrôle de concordance. Une configuration écrite ne prouve pas qu’une
   session déjà ouverte l’a chargée.

Ces écritures sont hors du périmètre autorisé de la session actuelle : seul
`ONTBibleTranslation` est modifiable. Elles n’ont pas été tentées en contournant
la restriction. Les modifications locales, les tests et ce relevé restent
disponibles pour poursuivre depuis un environnement qui peut écrire dans les
dépôts voisins.

## Préparation disponible dans le vault

Trois commandes produisent des propositions consultables, sans modifier leurs
destinations :

```sh
python3 knowledge/preparer-raccordement.py
python3 knowledge/preparer-journal.py
python3 knowledge/reconcilier-journal.py
```

`knowledge/preparation/raccordement.json` contient treize changements proposés
pour la racine et les trois dépôts : instructions et réglages des assistants.
Chaque changement conserve le texte proposé, le diff et l’empreinte de la
version lue. Les réglages existants sont préservés et une seconde préparation
après application simulée n’ajoute pas de doublon. Le hook sait retrouver le
vault voisin depuis un sous-dossier de l’app ; ce cas est testé.

`knowledge/preparation/journaux.json` rassemble dix copies de travail, avec
79 titres d’entrées distincts et quatre versions du préambule. Dix des dix-neuf
différences de corps se limitent au séparateur Markdown final. Les neuf autres
portent des changements de translittération, parfois dans des exemples de bugs
historiques : leur remplacement automatique risquerait de changer la preuve
citée. Les variantes et leurs origines sont conservées intégralement.
Les titres différents ne sont pas automatiquement rapprochés.

Ces nombres décrivent le disque examiné le 15 septembre, tandis que le contrôle
de concordance examine aussi les références publiées connues localement.
Les fichiers de préparation sont ignorés par Git et se régénèrent pour éviter
de publier des préimages périmées.

La troisième commande produit `journal-reconcilie.txt` et son relevé JSON.
Les 79 entrées sont conservées. Les neuf variantes de contenu retiennent la
graphie historique attestée dans le commit local de l’app
`bf100b40f7502ead968dc40e9cafda6ed402c940`, sans moderniser les caractères
des exemples de bugs. `journal-resolutions.json` fixe les choix et les
empreintes examinées ; une variante nouvelle fait échouer la préparation.
Le préambule conserve les ajouts indépendants du vault et du checkout Mac.

Quatre copies contiennent encore chacune onze notes locales dans leur journal
commun. Le JSON prépare leur transfert vers `SYNCHRONISATION-locale.md`, avec
les corps intégraux, les sous-sections et les empreintes avant/après. Les
journaux locaux existants sont conservés. Un titre local identique portant
un texte différent est refusé pour revue ; il n’est pas dédoublonné en silence.
La préparation ne remplace aucun des dix journaux et n’applique aucune des
quatre migrations. Les notes locales doivent être conservées avant
l’installation du tronc commun, après vérification des empreintes lues.

`claude doctor` s’est terminé avec le code 0, sans erreur de réglages signalée,
mais il a signalé une authentification indisponible et un trousseau non
modifiable. Ce diagnostic ne prouve pas que le hook a été chargé dans une
session Claude active. Aucun accès au trousseau n’a été forcé.

La vérification du 15 septembre a aussi confirmé le contrat de hook Codex
dans sa documentation officielle. La proposition
`knowledge/codex-hooks.proposition.json` est testée depuis un sous-dossier du
vault sur les mêmes 41 questions que le hook Claude configuré. Elle demeure
non installée : `.codex` est protégé en écriture, même dans le vault.
La [validation native des hooks Codex](https://learn.chatgpt.com/docs/hooks)
reste nécessaire après installation. La préparation commune inclut maintenant
les quatre configurations Codex (racine, vault, app et site), en complément
des neuf changements précédents. Les sept commandes de hook proposées ont été
exécutées depuis leurs dossiers cibles ou un sous-dossier existant : elles
retrouvent la notice KB-0067. Les préimages des treize destinations sont
inchangées après cette vérification. Il ne s’agit pas d’un test de leur
chargement par les applications.

Le diagnostic natif `codex doctor --summary --no-color --ascii` ne valide pas
une session : il constate une configuration et une authentification présentes,
mais aucune application Desktop ni serveur persistant actifs, et signale des
échecs d’intégrité de l’état local et de connectivité. Ces diagnostics n’ont
pas été traités comme une autorisation de modifier l’installation personnelle.

## Matière de l’entrée commune

### Vérification complémentaire du 16 septembre

Une revue avec la session Claude du vault via Herdr a confirmé, selon son
retour, la réception effective des dossiers injectés dans cette session.
L’authentification expirée a été renouvelée par l’utilisateur. Cette preuve
locale ne valide ni Codex ni les sessions voisines. Le contexte injecté sur
des messages de coordination comporte du bruit ; son filtrage reste ouvert.

La revue a identifié puis validé une correction de l’extraction de `## Source`.
`liens` et `graphe --lexique` partagent maintenant la même lecture des suffixes
OSHB et des références composées : 365 relations sur 354 fiches, dont 50
relations auparavant omises. Les références et leurs suffixes sont conservés,
sans fusion de fiches ni inférence de parenté. Le contrôle indépendant de
Claude concorde avec ce relevé. Les fichiers du lexique ne changent pas, ni
les interfaces du corpus consommées par l’app et le site.

Les autorisations peuvent désormais être demandées dans la session Codex.
La restriction antérieure n’établit donc plus une impossibilité permanente :
les raccordements et migrations préparés doivent être relus avec leurs
préimages actuelles avant toute installation autorisée. Aucun n’a été appliqué
pendant cette correction.

### Description à reprendre lors de l’installation

La KB ONT donne accès à des notices attribuées dans sept domaines, aux fiches,
aux règles et aux témoins. Une commande prépare un dossier pour une tâche.
Les occurrences par Strong, l’apparat SBLGNT, les agrégats du pont Septante et
le graphe documentaire se consultent avec leurs limites. Les instructions
Codex et le hook Claude Code du vault sont configurés. Les interfaces de
corpus consommées par l’app et le site ne changent pas. Chaque assistant doit
conserver la distinction entre source ancienne, analyse linguistique,
interprétation ONT et arbitrage encore ouvert.
