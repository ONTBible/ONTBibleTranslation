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

## #122 · Où chaque rôle se tient — la carte Herdr

    ouverte le   18 septembre 2026, par la manageuse
    vers         main
    état         ouverte

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
