# Les propositions — ce qui est ouvert, par qui, et ce que ça engage

**Décision de l'auteur du 21 septembre 2026.** Toute PR s'inscrit ici, **par
celle qui l'ouvre**, avec ce qu'aucun tableau GitHub ne montre : pourquoi elle
existe, et ==ce qu'elle engage chez les voisins==.

## Pourquoi ce fichier, à côté de `DECISIONS.md`

`DECISIONS.md` porte ce qui est ==tranché== ; celui-ci porte ce qui est
==proposé et attend==. Une PR *est* une proposition — le nom dit ce qu'elle est,
et le couple dit où chaque chose vit.

**Ce qu'un tableau de PR ne donne pas**, et qui manque à chaque relecture :

- **qui l'a ouverte.** Les huit sessions poussent sous le compte `gloiiire` :
  `gh pr list --author @me` rend ==toutes les PR du dépôt==. Trois sessions y
  sont tombées le même jour. ==L'auteur git ne distingue personne== ;
- **pourquoi.** Le titre dit ce que la PR fait, jamais le défaut qu'elle répare
  ni la mesure qui l'a rendue nécessaire ;
- **ce qu'elle engage.** C'est la règle du `CLAUDE.md` racine — *demander ce que
  ce travail change pour les autres dépôts* — et rien ne la portait. ==Un
  changement de forme dans une réponse casse une plateforme qui n'est pas celle
  qu'on regarde en le faisant.==

## Ce que ça coûte : rien

==L'entrée voyage dans la PR qu'elle décrit.== On l'écrit sur la branche qu'on
vient de pousser, avant d'ouvrir la PR — pas de commit de plus, pas de CI de
plus, pas de fusion supplémentaire à attendre.

C'est la différence avec la déclaration d'un worktree, qui coûte un aller-retour
parce qu'elle ne s'attache à aucun travail en cours.

## La forme

    ## #NNN · le titre
    
        ouverte le   la date, par le RÔLE — jamais un nom de session
        vers         la branche de base
        état         ouverte · fusionnée le … · abandonnée le …
    
    **Pourquoi.** Le défaut, et la mesure qui l'a rendu visible.
    
    **Ce que ça engage.** Ce qui traverse vers les autres dépôts, ce qui
    devient irréversible, ce qu'une autre session devra reprendre.
    
    **Pour la relire.** Ce qu'il faut savoir qu'on ne devinerait pas.

==On ne retire pas une entrée quand la PR est fusionnée== : on change son état
et on date. Une proposition abandonnée reste, avec le motif — ==c'est souvent
elle qui a le plus à apprendre==.

**Et on n'écrit pas le « pourquoi » d'une PR qu'on n'a pas ouverte.** Une entrée
peut donc porter ==*à écrire par qui l'a ouverte*== : ce trou-là est une
information, et il se voit.

---

## #135 · La garde contre un biais est elle-même un biais

    ouverte le   30 septembre 2026, par la manageuse
    vers         main
    état         ouverte

**Pourquoi.** L'auteur travaille une thèse sur la motivation du langage hébreu,
et un exemple y revient partout — la famille פ-ר, où un noyau « rupture »
==semble== apparaître. Avant qu'il entre dans une chuqqah, on a voulu tuer ou
confirmer ce « semble ».

Test en aveugle : פ-ר mêlée à ==sept paires tirées au sort==, huit groupes
anonymisés, clé scellée, lecture faite sans elle.

**Deux résultats, et il faut les deux.** ==1 paire sur 7== a réellement un
noyau — donc פ-ר est inhabituel, pas unique. Mais ==3 sur 7== semblent en avoir
un à la première lecture : la méthode produit ==43 % de faux positifs==.
==La paréidolie n'est pas dans la langue, elle est dans l'œil.==

**Ce que ça engage.** Rien de technique. Mais la clause *motivé ≠ déterminant*
engage ==la page « Le pourquoi » du site== (PR #161, en attente de l'auteur) :
sans elle, une chuqqah sur la motivation du langage aurait l'air de contredire
ce que la page affirme déjà.

Et deux chiffres sont rectifiés avant de voyager : Blasi et al. 2016 a analysé
==4 298 langues== et non 6 000, et Bohas se dit ==« publiée et poursuivie,
réception non mesurée »== plutôt que « contestée ».

**L'entrée porte aussi ce que le dispositif a appris sur lui-même.** Quatre
biais ont été trouvés, ==les quatre penchant du même côté== sans que personne
ne le cherche — et ==aucun par plus de rigueur dans la mesure== : tous en
regardant une forme, ou en faisant lire quelqu'un d'autre.

Mon propre décompte penchait aussi, ==dans la direction qui me faisait
honneur==, ce qui est précisément ce qui le rendait invisible.

## #134 · Le registre a un point fixe, et le contrôle le nomme

    ouverte le   29 septembre 2026, par la manageuse
    vers         main
    état         ouverte

**Pourquoi.** ==« Zéro écart » n'est pas atteignable==, et personne n'en est
responsable. Relevé par iOS le 29 septembre en datant trois entrées : ==sa
propre PR d'entretien est née « ouverte· »==, parce qu'une entrée qui *voyage
dans la PR qu'elle décrit* est écrite ==avant sa fusion== et ne peut donc pas
connaître sa date.

    #345 date #343, #328, #326   →  #345 naît « ouverte »
    #346 daterait #345           →  #346 naîtrait « ouverte »

==La plus récemment fusionnée est indatable par construction== : rien n'a
fusionné après elle pour la dater. Toutes les autres, si — elles relèvent du
prochain lot, et celui-là est du vrai travail.

**Ce que ça engage.** Rien d'autre que cet outil. Le relevé sépare désormais
==le plancher== des écarts réels, et dit pourquoi il existe.

==On nomme le cas au lieu de relever le seuil==, et c'est la décision de fond.
Ne s'alarmer qu'à partir de deux aurait été plus simple et ==aurait masqué un
oubli isolé== — c'est-à-dire le seul cas que ce contrôle existe pour attraper.
Distinguer *laquelle* est structurelle ne masque rien, et ==ne coûte aucun état
à tenir== : c'est la date de fusion, que GitHub donne déjà.

**Mesuré :** 6 écarts avant, ==3 écarts et 3 points fixes== après — un par
dépôt, exactement ce que le raisonnement prédisait.

==C'est le prix de la règle qui fait voyager l'entrée avec sa PR, et cette
règle vaut mieux que ce qu'elle coûte== : elle est ce qui rend l'entrée
gratuite, donc ce qui fait qu'elle est écrite. iOS l'a formulé ainsi en me le
signalant, et c'est le bon arbitrage.

## #133 · Une proposition ouverte se relit sur sa propre tête

    ouverte le   29 septembre 2026, par la manageuse
    vers         main
    état         ouverte

**Pourquoi.** Le contrôle `--propositions` ==criait sur le comportement qu'il
existe pour obtenir==. Ce registre prescrit que *« l'entrée voyage dans la PR
qu'elle décrit »* — c'est ce qui la rend gratuite —, donc elle est ==invisible
depuis la branche d'intégration jusqu'à la fusion==. Le contrôle lisait
l'intégration pour les deux écarts, et rendait « ouverte, aucune entrée » sur
des PR dont l'autrice avait fait exactement ce qu'on lui demandait.

==Relevé le même jour par deux sessions, séparément== — le site sur sa propre
PR, iOS sur celle d'Android —, et chacune a dû ouvrir le diff à la main pour
conclure. C'est le coût d'un avertissement qu'on apprend à ne plus lire, que la
table des worktrees invoquait déjà pour refuser une colonne « branche ».

==Le contrôle jumeau avait le même défaut==, et il a été corrigé dans la
même PR. La table des worktrees vit dans `SYNCHRONISATION.md`, qui est
versionné : une ligne écrite ==dans le même tour que la création du worktree==
— ce que la règle exige — voyage dans la branche de ce worktree. Quatre
worktrees étaient signalés le soir du 29 septembre, et ==les quatre étaient
déclarés==. Trois étaient les miens — ==j'ai écrit la règle et je ne l'avais
pas tenue== —, le quatrième celui des langues sources, ==qui l'avait tenue
parfaitement== et se faisait rappeler à l'ordre pour ça.

Là, aucun service n'est interrogé : ==la copie du journal est sur le disque==,
à côté du worktree qu'elle décrit. 4 signalés → 1, et le dernier est juste.

**Ce que ça engage.** Rien d'autre que cet outil. Un appel `gh pr diff` de plus
par PR ouverte sans entrée à l'intégration — quelques secondes, et seulement
sur les candidates.

**Mesuré, sur les mêmes PR :** 16 écarts dont ==7 faux== avant, ==9 et aucun
faux== après. La sortie compte désormais à part celles *dont l'entrée voyage
encore dans sa PR* : l'état souhaité cesse de ressembler au manquement.

==La première écriture du correctif ne corrigeait rien==, et c'est gardé dans
le code : elle passait un pathspec que `gh pr diff` refuse, la fonction rendait
« pas d'entrée », et le relevé était identique à l'ancien. ==Un échec d'outil
déguisé en réponse==, vu parce que le contrôle a été éprouvé sur un cas dont on
connaissait la réponse avant d'être commité.

## #122 · Où chaque rôle se tient — la carte Herdr

    ouverte le   18 septembre 2026, par la manageuse
    vers         main
    état         fusionnée le 29 septembre 2026

**Pourquoi.** La table des sept rôles disait *ce que* chacun tient, jamais *où*.
Quatre identifiants ont péri en un jour avant qu'on trouve le bon — le nom à un
`/rename`, le socket au redémarrage, la référence à une reconnexion, l'auteur
d'une PR qui ne distingue personne. Le volet Herdr, lui, est une **place** : il
vit dans la disposition, pas dans le processus.

**Ce que ça engage.** Rien de technique — c'est de la prose de journal. Mais la
carte devient la référence pour s'adresser, et elle porte **Astra**, qui
n'apparaît dans aucun `ListAgents` et dont la place a été établie sans qu'elle
puisse la dire. Elle porte aussi la table des worktrees et son contrôle.

**Pour la relire.** Elle est entrée par la même porte que la section des
worktrees : les deux vivent à côté de la table des rôles, non en fin de fichier,
pour ne pas entrer en conflit avec les entrées de journal.

## #125 · Deux corrections à l'entrée du 18

    ouverte le   20 septembre 2026, par la manageuse
    vers         main
    état         ouverte

**Pourquoi.** Deux ajouts venus après coup. La clause d'Android **n'avait jamais
été écrite** alors que j'avais rapporté qu'elle l'était : la commande qui
l'ajoutait a été refusée en bloc par le garde-fou du harnais, et la reprise a
écrit avec `>>` sur un fichier que la première n'avait jamais créé. Une absence
rapportée comme une présence, trouvée deux jours plus tard en vérifiant autre
chose. Le second ajout est le versant positif de la septième forme.

**Ce que ça engage.** Rien qui traverse. Le texte doit rester identique dans les
trois dépôts — c'est le tronc commun, et `concorder-la-synchronisation.py` le
vérifie.

**Pour la relire.** Les trois exemplaires du journal **divergent
volontairement** : un tronc commun plus des entrées marquées `*(local)*`. Un
`cp` d'un exemplaire sur l'autre détruirait les entrées locales des deux autres.

## #92 · Porter l'entrée de la nuit du 11

    ouverte le   11 septembre 2026
    vers         main
    état         ouverte, en brouillon

*À écrire par qui l'a ouverte.*

## #123 · Compter les consultations KB sans confondre coordination et questions

    ouverte le   18 septembre 2026, par la session chargée de la KB et de ses raccordements (Codex)
    vers         main
    état         ouverte, en brouillon

**Pourquoi.** Le hook appelle `dossier()` directement : ses consultations
échappaient au compteur des commandes de `consulter.py`. Un essai sur le piel
rendait KB-0006 sans entrée au compteur. La PR ajoute `hook:dossier` après le
filtrage, sans conserver le message ni ses arguments ; l'impossibilité d'écrire
le journal ne bloque pas le dossier. Les fixtures isolent aussi le parent du
vault temporaire pour ne pas partager leur journal entre tests.

Un second défaut est apparu depuis les consommateurs : iOS a reçu des notices
de grammaire sur une annonce technique, et la manageuse a relevé les termes
`uds`, `socks` et un identifiant de socket dans la recherche. Le hook cherchait
aussi dans l'enveloppe SendMessage. Il ne traitait pas littéralement chaque
message : les salutations et confirmations simples étaient déjà filtrées.
La PR sépare désormais les corps des enveloppes reconnues et permet d'exclure
explicitement les annonces techniques.

**Ce que ça engage.** Pour les sessions du Vault et celles des dépôts voisins
qui utilisent ce script, les consultations automatiques deviennent visibles
dans le compteur. Pour exclure une annonce sans tâche corpus, l'expéditeur
doit commencer son message par
`[Nom, message de pair, coordination technique]`. Un message de pair ordinaire
reste traité, y compris une vraie question corpus dans un lot mêlé à une
annonce technique. Sans marqueur, une annonce peut encore produire du bruit.
La convention doit donc être connue des expéditeurs ; cette PR ne modifie pas
leurs fichiers d'instructions et n'installe aucun hook chez les voisins.

Le compteur mesure des lancements, essais compris, pas des services rendus.
L'ajout du comptage automatique puis l'exclusion des annonces marquées changent
la série. Il faut relire les anciens bilans en distinguant commandes, essais
et consultations automatiques, sans comparer une baisse ou une hausse à
travers ces changements comme un fait d'usage. Les anciennes entrées ne portent
ni version du filtre ni contenu permettant de les reclasser : on ne peut pas
reconstituer la frontière après coup. La date du commit ne donne pas la date
d'activation dans chaque checkout. Aucun corpus, format consommé par l'app ou
le site, réglage partagé ni journal historique d'usage n'est modifié.

**Pour la relire.** Le code est dans `knowledge/claude-hook.py`, les limites
dans `knowledge/README.md`, et le suivi d'installation dans
`knowledge/synchronisation-a-terminer.md`. Les essais du 18 septembre sur
`323fa0d` donnent 73 notices valides, 36 tests KB et 9 tests du prototype
réussis. Ils couvrent les deux transports, l'avis SendMessage avec ou sans sa
dernière phrase, les lots mixtes et la conservation intégrale d'un format
inconnu ou d'une question extérieure au lot. Le prompt reçu par l'assistant
reste intact : seule la requête KB est préparée.

Le chargement natif de dossiers a été rapporté par le Vault avant ce dernier
correctif ; il ne prouve pas l'activation du nouveau filtre. Les raccordements
supplémentaires restent retirés en attendant une réponse directe de l'auteur
sur leur activation. La fusion de cette PR, l'activation dans les sessions et
la vérification native sur les deux transports sont trois étapes distinctes.

---

## #136 · Éprouver un noyau consonantique — l'instrument, pas le chiffre

    ouverte le   30 septembre 2026, par les langues sources
    vers         main
    état         ouverte

**Pourquoi.** L'entrée du journal du 30 septembre cite « 80 % contre 38 % ».
==Le chiffre se recopie, l'instrument se relance== — et celui-ci vivait dans
`/tmp`, qui meurt au prochain redémarrage. Quelqu'un voudra refaire la mesure ;
sans le script, il la referait autrement, et un autre protocole rendrait un
autre chiffre sans que personne sache lequel croire.

La graine par défaut rejoue **exactement** le tirage du 30 : même clé, même
mesure.

**Ce que ça engage.** Rien — `scripts/` ne voyage pas dans `dist/`, aucune
liseuse ne le lit. Le lexique d'OpenScriptures (CC BY 4.0) n'est pas versionné
mais mis en cache, et `.cache/` entre au `.gitignore` : ==le lire pour écrire
une analyse ne redistribue rien==, ce que #132 pose en règle.

**Pour la relire.** Le fichier existe pour ses **quatre biais**, plus que pour
sa mesure. Deux sont corrigés dans le code parce qu'ils ne se voient pas à
l'usage — le préfixe mem pris pour une radicale, shin et sin fondus — et
==les deux frappaient les témoins en épargnant le candidat==, פ n'étant ni une
lettre préfixe ni un graphème à deux valeurs. Les deux autres sont fermés par
`--aveugle`, et ils ont été trouvés trop tard : la forme trahit la paire, et le
numéro de Strong aussi, ==ses plages suivant l'ordre alphabétique==.

Le mode aveugle est contrôlé : 68 lignes de données sur 68 ne portent ni forme
ni numéro.

Et il déclare ce qu'il ne fait pas : ==ce n'est pas la thèse de Bohas==, dont
l'étymon est une paire non ordonnée à n'importe quelle position. Un résultat
négatif ne réfuterait que la version simplifiée qui circule.

---

## #138 · Départager les ex æquo — le mot partagé n'était pas reproductible

    ouverte le   30 septembre 2026, par les langues sources
    vers         main
    état         ouverte

**Pourquoi.** `--harmonisation` élisait **un** mot partagé par groupe, et ce mot
==changeait d'une exécution à l'autre== quand plusieurs étaient à égalité :
`Counter.most_common` départage par ordre de première rencontre, lequel dépend
ici de l'itération d'un `set`, donc du hachage, donc du processus.

    PYTHONHASHSEED=0  ר-ע « rule »      PYTHONHASHSEED=2  ר-ע « pasture »
    PYTHONHASHSEED=4  ר-ע « tend »      — à compte et pourcentage identiques

==Le §2.5 ter du `CLAUDE.md` portait déjà l'avertissement==, mot pour mot, sur
`Counter.most_common` et les ex æquo. Je l'ai reproduit dans un script dont le
docstring entier traite des biais d'instrument. ==Une règle n'empêche que ce
qu'on pense à lui soumettre.==

**Ce que ça engage.** Le journal du 30 septembre (#135) et sa correction (#137)
citent ces mots. ==Deux valeurs sur huit étaient instables== — `ר-ע` (19 ex
æquo) et `שׁ-ק` (2) ; les six autres avaient un vainqueur unique et étaient
reproductibles depuis le début. Le rang, le compte et le pourcentage n'ont
jamais bougé.

**Pour la relire.** La correction ==ne choisit pas mieux, elle refuse de
choisir== : à égalité, l'outil dit *combien* de mots sont ex æquo et les nomme
tous. Et ce refus ==apprend quelque chose que l'élection cachait== : sur ר-ע,
dix-neuf mots atteignent le plafond de 2/9, c'est-à-dire qu'==aucun mot n'est
partagé== — le 22 % n'était pas un signal faible, c'était du bruit.

Le résultat en sort plus net, pas moins : `פ-ר` est ==le seul groupe où une
majorité de lemmes partage un mot==, 8 sur 10. Partout ailleurs le maximum est
minoritaire, et deux fois il est au plancher.
