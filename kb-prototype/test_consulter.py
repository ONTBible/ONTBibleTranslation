import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("kb", Path(__file__).with_name("consulter.py"))
kb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kb)


class Consultation(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.vault = Path(self.tmp.name).resolve()
        for dossier in ("lexique", "brouillons", "locked", "sources/he-wlc", "sessions"):
            (self.vault / dossier).mkdir(parents=True)
        self.ecrire("CLAUDE.md", "# Conventions\n\nUn rendu demeure discutable.\n")
        self.ecrire("lexique/qahal.md", "# qahal\n\nUn nom et un verbe.\n\n## Voir aussi\n\n[[Sinai]]\n\n## Formes\n\nqahal · vayiqahalu\n\n## Source\n\n6951 + 6950 · קָהָל\n")
        self.ecrire("lexique/Sinai.md", "# Sinai\n\nUne montagne.\n")
        self.ecrire("brouillons/exemple.md", "# Essai\n\nUne lecture incertaine.\n")
        self.ecrire("locked/exemple.md", "# Texte\n\nUne lecture relue.\n")
        self.ecrire("sources/MANIFEST.json", json.dumps({"sources": {"he-wlc": {
            "attribution": "Témoin de test", "livres": {"Gen": {}},
            "texte": {"licence": "domaine public"}}}}))
        self.ecrire("sources/he-wlc/Gen.jsonl", json.dumps({"ref": "Gen.1.1", "w": [{"t": "א", "oshb": {"lem": "1"}}]}) + "\n")

    def ecrire(self, nom, texte):
        (self.vault / nom).write_text(texte, encoding="utf-8")

    def test_recherche_preuve_et_statut(self):
        r = kb.chercher(self.vault, "lecture")["resultats"]
        self.assertEqual({x["nature"] for x in r}, {"brouillon", "traduction_verrouillee"})
        for x in r:
            lignes = (self.vault / x["fichier"]).read_text().splitlines()
            self.assertEqual(x["texte"], "\n".join(lignes[x["ligne_debut"]-1:x["ligne_fin"]]))

    def test_modification_visible_sans_cache(self):
        avant = kb.fiche(self.vault, "qahal")["sha256"]
        self.ecrire("lexique/qahal.md", "# qahal\n\nRectification récente.\n")
        apres = kb.chercher(self.vault, "rectification recente")["resultats"][0]
        self.assertNotEqual(avant, apres["sha256"])
        self.assertFalse(kb.chercher(self.vault, "vayiqahalu")["resultats"])

    def test_homonymes_non_fusionnes(self):
        self.ecrire("lexique/Chanokh-a.md", "# Chanokh\n\nPremier porteur.\n")
        self.ecrire("lexique/Chanokh-b.md", "# Chanokh\n\nAutre porteur.\n")
        with self.assertRaisesRegex(ValueError, "ambiguë"):
            kb.fiche(self.vault, "Chanokh")

    def test_liens_de_document_pas_affirmations_semantiques(self):
        relations = kb.liens(self.vault, "QAHAL")["relations"]
        self.assertEqual({r["objet"] for r in relations if r["predicat"] == "declare_un_numero_source"}, {"6950", "6951"})
        lien = next(r for r in relations if r["predicat"] == "contient_un_wikilien")
        self.assertEqual(lien["fiche_resolue"], "lexique/Sinai.md")
        self.assertFalse(any(r["predicat"] == "depend_de" for r in relations))

    def test_source_exacte_et_attribution(self):
        resultat = kb.reference(self.vault, "Gen.1.1")["temoins"][0]
        self.assertEqual(resultat["verset"]["w"][0]["oshb"], {"lem": "1"})
        self.assertEqual(resultat["attribution"], "Témoin de test")
        self.assertEqual(resultat["provenance"]["texte"]["licence"], "domaine public")
        self.assertFalse(kb.reference(self.vault, "Gen.1.2")["temoins"])

    def test_source_preserve_homonymes_composes_et_preuve(self):
        self.ecrire("lexique/composite.md", "# Composite\n\n## Source\n\n2896 b + 7451 b · טוֹב וָרָע\n")
        r = kb.liens(self.vault, "composite")["relations"]
        numeros = [x for x in r if x["predicat"] == "declare_un_numero_source"]
        self.assertEqual([x["objet"] for x in numeros], ["2896 b", "7451 b"])
        self.assertTrue(all(x["preuve"]["ligne_debut"] == 5 for x in numeros))
        self.assertTrue(all(x["preuve"]["texte"] == "2896 b + 7451 b · טוֹב וָרָע" for x in numeros))
        graphie = next(x for x in r if x["predicat"] == "declare_une_graphie_source")
        self.assertEqual(graphie["objet"], "טוֹב וָרָע")
        self.ecrire("lexique/composite.md", "# Composite\n\n## Source\n\n  2896a + 3966  · טוֹב מְאֹד\n")
        r = kb.liens(self.vault, "composite")["relations"]
        self.assertEqual([x["objet"] for x in r if x["predicat"] == "declare_un_numero_source"], ["2896 a", "3966"])

    def test_aucun_numero_invente_hors_declaration_source(self):
        self.ecrire("lexique/libre.md", "# Libre\n\n1471 a · Mention hors source\n\n## Source\n\nSans numéro ; voir 1471 a.\n1471 a + inconnu · graphie\n1471 a ·   \n")
        self.assertFalse(kb.liens(self.vault, "libre")["relations"])

    def test_sessions_exclues_et_saisie_fts_literalisee(self):
        self.ecrire("sessions/ancien.md", "# Ancien\n\nsecretfixture\n")
        self.assertFalse(kb.chercher(self.vault, "secretfixture")["resultats"])
        self.assertFalse(kb.chercher(self.vault, 'qahal" OR secretfixture')["resultats"])

    def test_titre_dans_code_ne_coupe_pas_section(self):
        self.ecrire("lexique/exemple.md", "# Exemple\n\n```markdown\n## Faux titre\n```\n\nTexte réel.\n")
        doc = kb.resoudre_fiche(self.vault, "exemple")
        self.assertEqual(len(list(kb.sections(doc))), 1)


if __name__ == "__main__":
    unittest.main()
