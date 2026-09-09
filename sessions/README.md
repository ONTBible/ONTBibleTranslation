# Ce dossier ne se balaye pas, ne se nettoie pas, ne se corrige pas

Il porte les **transcriptions des échanges de l'auteur** — ce qu'il a tapé, tel
qu'il l'a tapé. Ce ne sont pas des documents de travail, et rien ici n'est
régénérable : ces fichiers ne se reconstruisent depuis aucune source.

**La règle, et sa raison.** Le `CLAUDE.md` du dépôt l'écrit au §2.9, à propos de
la passe orthographique du 8 septembre 2026 :

> Trente-quatre `Khanokh` y subsistent, et ils doivent y subsister — corriger
> l'orthographe de ce que quelqu'un a tapé n'est pas une correction, c'est une
> réécriture.

Ce compte est un **témoin** : il vaut contrôle d'intégrité. `grep -roh "Khanokh"
sessions | wc -l` doit rendre **34**. S'il rend autre chose, quelque chose a
touché à ce dossier.

**Ce qui est donc interdit ici**, sans exception et quelle que soit la passe :

- toute correction d'orthographe, de translittération, de balisage ou de casse ;
- tout balayage automatique, même en lecture-écriture prudente ;
- toute suppression, tout déplacement, tout renommage.

**Pourquoi cette note existe.** Le 9 septembre 2026, ce dossier a été supprimé
en entier de l'arbre de travail — dossier compris. Rien n'était perdu : la
suppression n'était pas commitée, et `git checkout -- sessions` a tout rendu. Ce
qui a manqué n'est pas la sauvegarde, c'est **l'avertissement sur place**.

La règle existait, et elle était à quatre mille lignes d'ici, dans un document
que rien n'oblige à ouvrir avant de nettoyer un dossier. Une session qui arrive
par `ls` ne la rencontre jamais. Elle est donc écrite ici aussi, là où on la
lira au moment où elle sert.
