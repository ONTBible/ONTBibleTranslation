# Les sept rôles — se trouver sans se nommer

*Passage engendré — ne pas éditer. Source : `SYNCHRONISATION.md`, section « Les sept rôles — se trouver sans se nommer », partie 2. Empreinte de la section : `9361a25990792135`. Régénérer : `python3 knowledge/decouper.py`.*

- **iOS / iPadOS** — `app/Sources`, `app/Packages` (ONTKit, ONTData,
  ONTDesignSystem, ONTFeatures), le widget, `app/Tests` et `app/UITests`. Les
  décisions **d'interface** se prennent ici et s'appliquent ailleurs, quand
  Android ou macOS n'ont pas de raison propre de diverger ; pour les
  **données**, le sens est inverse — le pipeline et le vault font foi, iOS s'y
  plie comme les autres. À joindre pour : tout arbitrage de ce que le lecteur
  voit et touche sur iPhone et iPad, la forme des types de domaine d'ONTKit,
  les contrats de données côté liseuse.

- **Android** — `android/`, depuis son worktree dédié, intégration sur
  `device` ; la fiche Play et la chaîne de parution. N'arbitre pas l'interface :
  les initiatives viennent d'iOS, Android applique — règle de l'auteur. À
  joindre pour : `android/`, la fiche Play, ce qui traverse le pipeline
  jusqu'à Kotlin — et **avant** de toucher `scripts/corpus.sh` ou
  `pipeline/src/schema.rs`, qui l'atteignent l'un en silence, l'autre par le
  compilateur.

- **macOS** — la liseuse du Mac : `app/MacSources` et la part proprement Mac
  des fichiers partagés (fenêtre, barre latérale, cartes-modales, haptiques,
  verre) ; la chaîne Homebrew de bout en bout (tap, cask, signature,
  notarisation) ; la couche donnée des sources (`SourcesUpdater`). À joindre
  pour : ce qui se voit ou se sent sur le Mac, le cask et la distribution hors
  App Store. Les arbitrages d'interface vont à iOS, le Kotlin à Android.

- **Le site** — `ONTBibleWebapp` / `ontbible.com`. Lit `../ONTBibleApp/dist/`
  à la compilation, appelle le backend de l'app à l'exécution (`/auth/*`,
  `/sync`) ; porte les **originaux de la marque** — la palette de
  `style/main.css` et les vecteurs de `public/images/`, que l'app recopie,
  jamais l'inverse. À joindre pour : une couleur ou un vecteur à changer, un
  changement de forme dans `dist/` ou dans une réponse du backend, un lien
  `ontbible.com/fr/lire/…` qui ne mène pas où il devrait.

La table porte les rôles, qui durent — pas les chantiers ni les arbitrages en
attente, qui périment : ceux-là voyagent par message, et par `DECISIONS.md`
pour ce qui attend l'auteur.

---
