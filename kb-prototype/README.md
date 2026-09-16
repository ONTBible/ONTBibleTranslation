# Ancienne entrée de consultation

Le prototype reste disponible pour les commandes `chercher`, `fiche`, `liens`,
`reference` et `inventaire`. Le moteur documentaire est réutilisé par la KB.

L’entrée actuelle est [knowledge/README.md](../knowledge/README.md). Elle ajoute
les notices attribuées, les dossiers par tâche, les occurrences, les variantes,
le pont Septante, le graphe et le raccordement aux assistants du vault.

    python3 knowledge/consulter.py dossier 'Pourquoi qahal a deux numéros ?' --format markdown

Les tests du prototype restent exécutés :

    python3 -m unittest discover -s kb-prototype -p 'test_*.py'
