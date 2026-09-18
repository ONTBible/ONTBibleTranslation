#!/usr/bin/env python3
"""Questions réelles de l'ONT : évalue les preuves retrouvées, pas un LLM."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import consulter as kb

CAS = [
    ("Pourquoi qahal a deux numéros Strong ?", ["KB-0011"], ["6951", "6950"]),
    ("Différence entre geveret et gevirah et arbitrage ouvert", ["KB-0028"], ["À trancher par l'auteur"]),
    ("Distinguer les deux personnes Chanokh et le fils de Qayin", ["KB-0012"], ["Chanokh-fils-de-Qayin"]),
    ("Le piel veut-il toujours dire intensif ?", ["KB-0006"], ["causatif", "Gesenius"]),
    ("Comprendre l'infinitif absolu et son rendu ONT", ["KB-0007", "KB-0029"], ["113", "4.16"]),
    ("Datation du Second Temple et manuscrits de Qumrân", ["KB-0014", "KB-0015"], ["Israel Antiquities Authority"]),
    ("Lacune latine de Chazon Ezra et numérotation 7:36", ["KB-0020"], ["7:106"]),
    ("L'apparat SBLGNT compare-t-il des manuscrits ?", ["KB-0018"], ["éditions"]),
    ("Utiliser le pont Septante et ses alignements", ["KB-0021"], ["MACULA"]),
    ("Préparer la traduction du verset Gen.1.1", ["KB-0031"], ["Gen.1.1", "בָּרָ֣א"]),
    ("Lire HR/Ncfsa dans la morphologie OSHB", ["KB-0001"], ["féminin singulier"]),
    ("Analyser un état construit et divrei", ["KB-0005"], ["maqqef"]),
    ("Que désignent sujet prédicat et objet dans un triplet RDF ?", ["KB-0036"], ["ne prouve pas", "W3C"]),
    ("Un identifiant IRI doit-il être opaque ?", ["KB-0037"], ["n’exige pas"]),
    ("Comment distinguer les libellés SKOS prefLabel et altLabel ?", ["KB-0040"], ["étiquette de langue"]),
    ("Quelle direction pour la hiérarchie SKOS broader ?", ["KB-0041"], ["spécifique vers"]),
    ("Peut-on imposer des champs obligatoires dans un graphe avec SHACL ?", ["KB-0042"], ["minCount"]),
    ("Documenter la provenance PROV d’une extraction", ["KB-0043"], ["activité", "responsable"]),
    ("En OWL une information absente est-elle fausse ?", ["KB-0046"], ["inconnue"]),
    ("Comment interroger un graphe avec SPARQL SELECT et ASK ?", ["KB-0047"], ["recherche lexicale"]),
    ("L’infinitif construit avec une préposition exprime-t-il toujours un but ?", ["KB-0049"], ["temporelle"]),
    ("Un participe se traduit-il toujours au présent ?", ["KB-0051"], ["contexte", "116"]),
    ("Distinguer lo et al dans une défense au jussif", ["KB-0052"], ["interdictions"]),
    ("Que signifie ein devant un participe ?", ["KB-0053"], ["suffixe personnel"]),
    ("Avec kol, choisir entre aucun et pas tous", ["KB-0054"], ["portée", "152"]),
    ("Le qatal impose-t-il un passé français ?", ["KB-0055"], ["présent ou au futur"]),
    ("Yiqtol indique-t-il un futur ou une possibilité ?", ["KB-0056"], ["modalité", "UHG"]),
    ("Un niphal est-il toujours passif ?", ["KB-0057"], ["réciproques"]),
    ("Faut-il reconstruire un qal pour traduire un hiphil ?", ["KB-0058"], ["lexicalisées"]),
    ("Distinguer אֵת marqueur d’objet et préposition avec", ["KB-0059"], ["vocalisation"]),
    ("Un jussif est-il forcément à la troisième personne ?", ["KB-0060"], ["deuxième personne"]),
    ("Le cohortatif exprime-t-il une prédiction ?", ["KB-0061"], ["intention"]),
    ("Que peut indiquer une antéposition dans le récit ?", ["KB-0062"], ["interruption"]),
    ("Une cote de manuscrit désigne-t-elle toujours une seule composition ?", ["KB-0063"], ["recto", "verso"]),
    ("Définir le pesher et son rapport au Yahad", ["KB-0064"], ["prophéties"]),
    ("Une écriture carrée suffit-elle à reconnaître la langue ?", ["KB-0065"], ["araméen"]),
    ("Que date la paléographie : une copie ou une composition ?", ["KB-0066"], ["objet daté"]),
    ("Distinguer gap et unclear dans une transcription TEI", ["KB-0067"], ["lecture difficile"]),
    ("Comment attribuer le texte restitué dans supplied ?", ["KB-0068"], ["resp"]),
    ("Distinguer corr d’une correction du scribe dans le témoin", ["KB-0069"], ["modification visible"]),
    ("Que signifie le degré de confiance cert dans une lecture TEI ?", ["KB-0070"], ["confiance éditoriale"]),
    ("Déduire la forme de dictionnaire en retirant un article hébreu : attestations et limites de la mesure", ["KB-0071", "KB-0073"], ["voyelle du préfixe", "trois questions distinctes"]),
    ("La voyelle de l’article est-elle la voyelle du nom ?", ["KB-0071"], ["ne permet pas d’attribuer toute voyelle du nom"]),
    ("Le dagesh initial dépend-il des accents du mot précédent ?", ["KB-0072"], ["coupures accentuelles", "exceptions"]),
    ("Une forme nue majoritaire est-elle forcément la forme de citation ?", ["KB-0073"], ["conventions lexicographiques", "trois questions distinctes"]),
    ("Merci, peux-tu vérifier si le piel veut toujours dire intensif ?", ["KB-0006"], ["causatif", "Gesenius"]),
    ("Les tests passent. La session du vault demande si la forme nue majoritaire est forcément la forme de citation.", ["KB-0073"], ["trois questions distinctes"]),
]

SANS_DOSSIER = [
    "Merci, j’ai bien reçu !", "Bien reçu. Les 36 tests passent.",
    "Oki 👌", "Vas-y", "continue", "Merci beaucoup ! À bientôt.",
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--hook", action="store_true", help="Éprouver la commande du hook configuré, sans lancer de LLM.")
    parser.add_argument("--hook-config", type=Path, help="Éprouver un autre fichier de configuration ou une proposition, avec --hook.")
    args = parser.parse_args()
    if args.hook_config and not args.hook:
        parser.error("--hook-config demande --hook.")
    vault = Path(__file__).resolve().parent.parent
    commande = None
    if args.hook:
        reglages = json.loads((args.hook_config or vault / ".claude/settings.json").read_text())
        commandes = [h["command"] for g in reglages["hooks"]["UserPromptSubmit"] for h in g["hooks"]
                     if h.get("type") == "command" and "knowledge/claude-hook.py" in h.get("command", "")]
        if len(commandes) != 1:
            parser.error("Un unique hook KB configuré est attendu.")
        commande = commandes[0]
    def appeler_hook(question):
        # Le message passe par stdin ; seule la commande déjà configurée est du shell.
        evenement = {"hook_event_name": "UserPromptSubmit", "cwd": str(vault / "lexique"), "prompt": question}
        r = subprocess.run(["/bin/sh", "-c", commande], input=json.dumps(evenement), text=True,
                           capture_output=True, cwd=vault / "lexique", timeout=10,
                           env={**os.environ, "CLAUDE_PROJECT_DIR": str(vault)})
        if r.returncode:
            raise RuntimeError(r.stderr)
        return json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"] if r.stdout.strip() else ""

    resultats = []
    for question, attendus, indices in CAS:
        if commande:
            texte = appeler_hook(question)
            ids = set(re.findall(r"^## (KB-\d+) —", texte, re.MULTILINE))
        else:
            d = kb.dossier(vault, question)
            ids = {n["id"] for n in d["notices"]}
            texte = json.dumps(d, ensure_ascii=False)
        absents = [a for a in attendus if a not in ids] + [a for a in indices if a.casefold() not in texte.casefold()]
        resultats.append({"question": question, "reussite": not absents, "manquants": absents})
    if commande:
        for question in SANS_DOSSIER:
            texte = appeler_hook(question)
            resultats.append({"question": question, "attente": "aucun_contexte",
                              "reussite": not texte,
                              "manquants": ["silence attendu pour ce message sans tâche"] if texte else []})
    print(json.dumps({"type": "preuves_du_hook_configure" if commande else "preuves_retrouvees",
                      "configuration_testee": str(args.hook_config or vault / ".claude/settings.json") if commande else None,
                      "session_llm_verifiee": False, "cas": resultats}, ensure_ascii=False, indent=2))
    return int(any(not r["reussite"] for r in resultats))


if __name__ == "__main__":
    sys.exit(main())
