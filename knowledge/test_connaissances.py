import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import consulter as kb


class BaseDeConnaissances(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        # Le compteur écrit chez le parent du vault : celui-ci doit lui aussi
        # appartenir à la fixture, pas au dossier temporaire commun à tous.
        self.vault = (Path(self.tmp.name) / "vault").resolve()
        self.vault.mkdir()
        for dossier in ("knowledge", "lexique", "sources/he-wlc", "sources/grc-byz",
                        "sources/grc-sblgnt", "sources/pont-septante", "brouillons", "locked"):
            (self.vault / dossier).mkdir(parents=True)
        self.ecrire("CLAUDE.md", "# Règles\n\n## Prudence\n\nUne décision reste ouverte.\n\n### Exception\n\nCette réserve compte.\n\n## Suite\n\nAutre règle.\n")
        self.ecrire("lexique/qahal.md", "# qahal\n\nUne assemblée.\n\n## Formes\n\nqahal · Qahal\n\n## Source\n\n6951 + 6950 · קהל\n\n## Voir aussi\n\n[[Sinai]] et [[Inconnu]]\n")
        self.ecrire("lexique/Sinai.md", "# Sinai\n\nUne montagne.\n")
        self.data = {"version": 1, "sources": {"ref": {"titre": "Source test", "url": "https://example.org/source",
                     "consulte_le": "2026-09-14", "attribution": "Auteur test", "limite": "Une portée limitée."}},
                     "notices": [{"id": "KB-0001", "domaine": "decisions", "titre": "Prudence qahal", "aliases": ["qahal"],
                                  "statut": "renvoi_au_document", "texte": None,
                                  "sources": [{"fichier": "CLAUDE.md", "ancre": "Prudence"}],
                                  "relations": [{"predicat": "consulter_avec", "objet": "KB-0002", "statut": "parcours_editorial"}]},
                                 {"id": "KB-0002", "domaine": "grammaire", "titre": "État construit", "aliases": ["construit"],
                                  "statut": "synthese_documentaire", "texte": "Une connaissance attribuée.",
                                  "sources": [{"source": "ref"}], "relations": []}]}
        self.enregistrer()
        self.ecrire("sources/MANIFEST.json", json.dumps({"sources": {
            "he-wlc": {"livres": {"Gen": {}}, "attribution": "OSHB"},
            "grc-byz": {"livres": {"Mt": {}}, "attribution": "RP"},
            "grc-sblgnt": {"livres": {"Mt": {}}, "attribution": "SBLGNT"}}}))
        self.jsonl("sources/he-wlc/Gen.jsonl", [
            {"ref": "Gen.1.1", "w": [{"t": "א", "oshb": {"lem": "b/1254 a"}}, {"t": "ב", "oshb": {"lem": "1254 b"}}]},
            {"ref": "Gen.1.2", "w": [{"t": "ג", "oshb": {"lem": "1254 a"}}]},
            {"ref": "Gen.1.3", "w": [{"t": "ד", "oshb": {"lem": "12540"}}]}])
        self.jsonl("sources/grc-byz/Mt.jsonl", [{"ref": "Mt.1.1", "w": [{"t": "ἀρχή", "strong": "746"}]}])
        self.jsonl("sources/grc-sblgnt/Mt-apparat.jsonl", [{"ref": "Mt.1.1", "lecon": "α", "editions": ["WH"],
                     "variantes": [{"t": "β", "editions": ["NA28"], "crochets": ["NA28"]}]}])
        self.jsonl("sources/pont-septante/Gen.jsonl", [{"ref": "Gen.1.1", "p": [
            {"he": "1254", "gr": "4160", "hf": "א"}, {"he": "1254", "gr": "2936", "hf": "ב"},
            {"he": "12540", "gr": "4160", "hf": "ג"}]}])
        self.ecrire("sources/README.md", "# Sources\n\n## L'apparat du SBLGNT — et ce qu'il n'est pas\n\nÉditions imprimées.\n\n## `pont-septante/` — un outil de travail, jamais un témoin\n\nAlignement provisoire.\n")

    def ecrire(self, chemin, texte):
        (self.vault / chemin).write_text(texte, encoding="utf-8")

    def jsonl(self, chemin, lignes):
        self.ecrire(chemin, "\n".join(json.dumps(x, ensure_ascii=False) for x in lignes) + "\n")

    def enregistrer(self):
        self.ecrire("knowledge/contenus.json", json.dumps(self.data, ensure_ascii=False))

    def test_les_sources_locales_incluent_les_exceptions(self):
        n = kb.notion(self.vault, "KB-0001")
        self.assertIn("Cette réserve compte", n["sources"][0]["texte"])
        self.assertNotIn("Autre règle", n["sources"][0]["texte"])
        self.assertIsNone(n["texte"])

    def test_ancre_dans_un_exemple_de_code_ignoree(self):
        self.ecrire("CLAUDE.md", "# Règles\n\n```markdown\n## Prudence\nFausse source\n```\n\n## Prudence\nVraie source\n")
        r = kb.section_source(self.vault, "CLAUDE.md", "Prudence")
        self.assertIn("Vraie source", r["texte"])
        self.assertNotIn("Fausse source", r["texte"])

    def test_deplacement_de_lignes_et_correction_relus(self):
        avant = kb.notion(self.vault, "KB-0001")["sources"][0]
        p = self.vault / "CLAUDE.md"
        p.write_text("\n\n" + p.read_text().replace("reste ouverte", "est corrigée"))
        apres = kb.notion(self.vault, "KB-0001")["sources"][0]
        self.assertEqual(apres["ligne_debut"], avant["ligne_debut"] + 2)
        self.assertNotEqual(apres["sha256"], avant["sha256"])
        self.assertIn("est corrigée", apres["texte"])

    def test_verification_rougit_sur_source_perimee(self):
        self.assertTrue(kb.verifier(self.vault)["valide"])
        self.data["notices"][0]["sources"][0]["ancre"] = "Disparue"
        self.enregistrer()
        r = kb.verifier(self.vault)
        self.assertFalse(r["valide"])
        self.assertIn("Disparue", " ".join(r["erreurs"]))

    def test_relation_inconnue_et_id_duplique_refuses(self):
        self.data["notices"].append(copy.deepcopy(self.data["notices"][0]))
        self.data["notices"][0]["relations"][0]["objet"] = "KB-9999"
        self.enregistrer()
        self.assertGreaterEqual(len(kb.verifier(self.vault)["erreurs"]), 2)

    def test_sortie_sourcee_et_bornee(self):
        r = kb.dossier(self.vault, "Explique qahal", budget=5000)
        self.assertTrue(any(n["id"] == "KB-0001" for n in r["notices"]))
        self.assertTrue(any(n["id"] == "KB-0002" for n in r["notices"]))
        self.assertLessEqual(len(json.dumps(r, ensure_ascii=False)), 5000)
        self.assertLessEqual(len(kb.en_markdown(r)), 5000)
        long = kb.dossier(self.vault, "qahal " * 1000, budget=2000)
        self.assertLessEqual(len(json.dumps(long, ensure_ascii=False)), 2000)
        enorme = kb.dossier(self.vault, " ".join(str(i) + "x" * 60 for i in range(35)), budget=2000)
        self.assertLessEqual(len(json.dumps(enorme, ensure_ascii=False)), 2000)

    def test_source_manquante_signalee_sans_synthese_inventee(self):
        (self.vault / "CLAUDE.md").write_text("# Disparu\n")
        r = kb.dossier(self.vault, "qahal")
        self.assertTrue(any(o.get("id") == "KB-0001" for o in r["omissions"]))

    def test_provenance_externe_absente_ne_supprime_pas_les_autres_preuves(self):
        del self.data["sources"]["ref"]
        self.enregistrer()
        self.assertFalse(kb.verifier(self.vault)["valide"])
        r = kb.dossier(self.vault, "qahal construit")
        self.assertTrue(any(n["id"] == "KB-0001" for n in r["notices"]))
        self.assertTrue(any(o["id"] == "KB-0002" for o in r["omissions"]))

    def test_occurrences_sans_fusion_de_sens_ou_de_numeros(self):
        r = kb.occurrences(self.vault, "H1254", limite=1)
        self.assertEqual(r["occurrences_mots"], 3)
        self.assertEqual(r["versets"], 2)
        self.assertEqual(len(r["exemples"]), 1)
        self.assertTrue(r["exemples_limites"])
        self.assertEqual(kb.occurrences(self.vault, "H1254a")["occurrences_mots"], 2)
        self.assertEqual(kb.occurrences(self.vault, "G746")["occurrences_mots"], 1)

    def test_apparat_preserve_les_crochets(self):
        r = kb.apparat(self.vault, "Mt.1.1")
        self.assertEqual(r["entrees"][0]["entree"]["variantes"][0]["crochets"], ["NA28"])
        self.assertIn("éditions", r["portee"])

    def test_pont_agrege_et_ne_cree_pas_de_grec(self):
        r = kb.pont(self.vault, "H1254")
        self.assertEqual(r["appariements"], 2)
        self.assertEqual(r["equivalents_grecs"], {"G4160": 1, "G2936": 1})
        with self.assertRaises(ValueError):
            kb.pont(self.vault, "G4160")

    def test_graphe_toutes_les_extremites_existent(self):
        r = kb.graphe(self.vault, "KB-0001", inclure_lexique=True)
        ids = {n["id"] for n in r["noeuds"]}
        self.assertTrue(all(e["sujet"] in ids and e["objet"] in ids for e in r["relations"]))
        self.assertIn("cible:Inconnu", ids)
        self.assertIn("forme:qahal", ids)
        self.assertIn("forme:Qahal", ids)
        self.assertFalse(any(e["predicat"] == "est_le_pere_de" for e in r["relations"]))

    def test_chemin_exterieur_refuse(self):
        with self.assertRaises(ValueError):
            kb.section_source(self.vault, "../autre.md", "Titre")
        with self.assertRaises(ValueError):
            kb.apparat(self.vault, "../../fichier")

    def test_graphe_et_liens_preservent_les_memes_references_suffixees(self):
        for nom, declaration in (("goy", "1471 a · בְּגוֹיֵהֶם"), ("goyim", "1471 a · גּוֹי"),
                                 ("autre", "1471 b · Autre"), ("general", "1471 · Général"),
                                 ("compose", "2896 a + 3966 · טוֹב מְאֹד")):
            self.ecrire("lexique/" + nom + ".md", "# " + nom + "\n\n## Source\n\n" + declaration + "\n")
        g = kb.graphe(self.vault, inclure_lexique=True)
        numeros = [e for e in g["relations"] if e["predicat"] == "declare_un_numero_source"]
        partage = {e["sujet"] for e in numeros if e["objet"] == "numero-declare:1471 a"}
        self.assertEqual(partage, {"lexique/goy.md", "lexique/goyim.md"})
        ids = {n["id"] for n in g["noeuds"]}
        self.assertTrue({"numero-declare:1471", "numero-declare:1471 a", "numero-declare:1471 b"} <= ids)
        self.assertTrue(all(e["sujet"] in ids and e["objet"] in ids for e in g["relations"]))
        for p in (self.vault / "lexique").glob("*.md"):
            liens = [r for r in kb.documents.liens(self.vault, p.stem)["relations"]
                     if r["predicat"] == "declare_un_numero_source"]
            dans_graphe = [e for e in numeros if e["sujet"] == "lexique/" + p.name]
            self.assertEqual({r["objet"] for r in liens}, {e["objet"].removeprefix("numero-declare:") for e in dans_graphe})
            for e in dans_graphe:
                self.assertEqual(e["texte_source"], p.read_text().splitlines()[e["ligne"] - 1])
                self.assertEqual(e["sha256"], kb.documents.fiche(self.vault, p.stem)["sha256"])

    def test_hook_avec_evenement_reel(self):
        script = Path(__file__).with_name("claude-hook.py")
        def appel(prompt):
            return subprocess.run([sys.executable, str(script)], input=json.dumps({"hook_event_name": "UserPromptSubmit", "cwd": str(self.vault), "prompt": prompt}), capture_output=True, text=True)
        r = appel("Explique qahal")
        self.assertEqual(r.returncode, 0, r.stderr)
        out = json.loads(r.stdout)
        self.assertNotIn("decision", out)
        self.assertIn("KB-0001", out["hookSpecificOutput"]["additionalContext"])
        self.assertIn("Auteur test", out["hookSpecificOutput"]["additionalContext"])
        self.assertIn("2026-09-14", out["hookSpecificOutput"]["additionalContext"])
        self.assertEqual(appel("Bonjour").stdout, "")

    def test_hook_depuis_voisin_retrouve_le_vault_commun(self):
        voisin = self.vault / "ONTBibleApp" / "sous-dossier"
        voisin.mkdir(parents=True)
        cible = self.vault / "ONTBibleTranslation"
        cible.mkdir()
        for p in tuple(self.vault.iterdir()):
            if p not in (cible, voisin.parent):
                p.rename(cible / p.name)
        r = subprocess.run([sys.executable, str(Path(__file__).with_name("claude-hook.py"))],
            input=json.dumps({"hook_event_name": "UserPromptSubmit", "cwd": str(voisin), "prompt": "Explique qahal"}),
            capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("KB-0001", json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"])

    def test_hook_silencieux_pour_reception_et_relance_sans_sujet(self):
        for prompt in ("Merci, j’ai bien reçu !", "Bien reçu. Les 36 tests passent.",
                       "Oki 👌", "Vas-y", "continue", "Merci beaucoup ! À bientôt."):
            with self.subTest(prompt=prompt):
                r = subprocess.run([sys.executable, str(Path(__file__).with_name("claude-hook.py"))],
                    input=json.dumps({"hook_event_name": "UserPromptSubmit", "cwd": str(self.vault), "prompt": prompt}),
                    capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertEqual(r.stdout, "")

    def test_hook_conserve_une_question_dans_un_message_de_coordination(self):
        for prompt in ("Merci, explique qahal", "Les tests passent. Vérifie qahal et son état construit.",
                       "Message de la session du vault : explique qahal", "Continue sur qahal"):
            with self.subTest(prompt=prompt):
                r = subprocess.run([sys.executable, str(Path(__file__).with_name("claude-hook.py"))],
                    input=json.dumps({"hook_event_name": "UserPromptSubmit", "cwd": str(self.vault), "prompt": prompt}),
                    capture_output=True, text=True)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertIn("KB-0001", json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"])

    def test_hook_compte_la_consultation_sans_le_message_ni_les_salutations(self):
        script = Path(__file__).with_name("claude-hook.py")
        for prompt in ("Merci, bien reçu", "Explique qahal, note privée à ne pas journaliser"):
            r = subprocess.run([sys.executable, str(script)],
                input=json.dumps({"hook_event_name": "UserPromptSubmit", "cwd": str(self.vault), "prompt": prompt}),
                capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("KB-0001", json.loads(r.stdout)["hookSpecificOutput"]["additionalContext"])
        lignes = (self.vault.parent / kb.JOURNAL_USAGE).read_text().splitlines()
        self.assertEqual(len(lignes), 1)
        entree = json.loads(lignes[0])
        self.assertEqual(entree["c"], "hook:dossier")
        self.assertEqual(sorted(entree), ["b", "c", "q", "s"])
        self.assertNotIn("qahal", lignes[0])
        self.assertNotIn("note privée", lignes[0])

    def test_hook_fournit_le_dossier_meme_si_son_journal_est_inaccessible(self):
        spec = importlib.util.spec_from_file_location("hook_pour_test", Path(__file__).with_name("claude-hook.py"))
        hook = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(hook)
        with patch.object(kb, "JOURNAL_USAGE", str(self.vault / "absent" / "usage.jsonl")):
            texte = hook.contexte({"hook_event_name": "UserPromptSubmit", "cwd": str(self.vault),
                                   "prompt": "Explique qahal"})
        self.assertIn("KB-0001", texte)

    def test_controles_voient_deux_fiches_qui_se_percutent(self):
        # Le cas du 12 septembre : malakh le verbe et malʾakh l'envoyé, deux mots
        # que l'hébreu sépare par un alef, une seule clé tant que le slug pardonne.
        self.ecrire("lexique/malakh.md", "# malakh\n\nRégner.\n")
        self.ecrire("lexique/malʾakh.md", "# malʾakh\n\nL'envoyé.\n")
        r = kb.controles(self.vault)
        collisions = [c for c in r["constats"] if c["controle"] == "collision_de_cle"]
        self.assertTrue(collisions, "la collision doit être vue")
        self.assertEqual(r["bloquants"], len(collisions))
        self.assertEqual(sorted(collisions[0]["fiches"]), ["malakh", "malʾakh"])
        self.assertEqual(collisions[0]["regle"], "slug actuel")
        # Sous le demi-anneau signifiant elles cessent de se percuter.
        self.assertNotIn("demi-anneau signifiant", [c["regle"] for c in collisions])

    def test_l_apostrophe_tombe_et_ne_devient_pas_un_separateur(self):
        # Épreuve de régression, écrite sur une faute commise. Le slug du pipeline
        # SUPPRIME l'apostrophe (inline.rs:123) : « L'Être façonné du sol » donne
        # « letre-faconne-du-sol », sans tiret après le l. Une approximation qui la
        # rendait par un tiret a fait renommer une fiche juste, et coupé soixante
        # mots d'or de leur définition.
        self.ecrire("locked/unite.md", "¹ Et **l'Être façonné du sol** fut posé.\n")
        self.ecrire("lexique/letre-faconne-du-sol.md", "# letre\n\nLa périphrase.\n")
        self.assertEqual(kb.controles(self.vault)["bloquants"], 0,
                         "le nom sans tiret est celui que le pipeline engendre")
        (self.vault / "lexique/letre-faconne-du-sol.md").rename(
            self.vault / "lexique/l-etre-faconne-du-sol.md")
        r = kb.controles(self.vault)
        manquants = [c["terme"] for c in r["constats"] if c["controle"] == "terme_inatteignable"]
        self.assertIn("l'Être façonné du sol", manquants,
                      "avec un tiret, la fiche n'est plus celle du terme")

    def test_un_lien_de_shem_sans_fiche_est_un_signal_un_gras_sans_fiche_est_bloquant(self):
        # Épreuve de régression, écrite sur une faute de ce contrôle lui-même.
        # Il rendait BLOQUANTS les deux, et condamnait donc ce que le CLAUDE.md
        # autorise en toutes lettres : « le vault porte des renvois vers des
        # porteurs pas encore écrits : ce sont des marques de travail à faire,
        # pas des erreurs » (ligne 1934, et inline.rs:408 dit le même).
        #
        # La distinction n'est pas de goût, elle est de conséquence. Un gras
        # sans fiche s'affiche EN OR ET TOUCHABLE : le lecteur l'ouvre et ne
        # trouve rien — une promesse rompue. Un lien de Shem sans fiche est la
        # liste de ce qui reste à écrire, et le pipeline l'émet exprès pour
        # qu'elle reste visible.
        self.ecrire("locked/unite.md", "¹ Et [[Yosef]] formula devant **chesed**.\n")
        self.ecrire("lexique/chesed.md", "# chesed\n\nLa fidélité loyale.\n")
        r = kb.controles(self.vault)
        self.assertEqual(r["bloquants"], 0,
                         "un Shem sans fiche ne barre pas : c'est du travail annoncé")
        shemot = [c["terme"] for c in r["constats"] if c["controle"] == "shem_sans_fiche"]
        self.assertIn("Yosef", shemot, "le Shem sans fiche se signale quand même")
        (self.vault / "lexique/chesed.md").unlink()
        r = kb.controles(self.vault)
        self.assertEqual(r["bloquants"], 1,
                         "un gras sans fiche barre : l'app le rend en or et il n'ouvre rien")
        gras = [c["terme"] for c in r["constats"] if c["controle"] == "terme_inatteignable"]
        self.assertIn("chesed", gras)
        self.assertNotIn("Yosef", gras, "un lien de Shem n'est pas un gras")

    def test_controles_voient_un_terme_qu_aucune_fiche_ne_sert(self):
        self.ecrire("locked/unite.md", "¹ Et **termeorphelin** fut posé.\n")
        r = kb.controles(self.vault)
        manquants = [c["terme"] for c in r["constats"] if c["controle"] == "terme_inatteignable"]
        self.assertIn("termeorphelin", manquants)
        self.ecrire("lexique/termeorphelin.md", "# terme\n\nUne définition.\n")
        self.assertEqual(kb.controles(self.vault)["bloquants"], 0)

    def test_un_numero_partage_est_un_signal_et_non_un_verdict(self):
        # Un construit se déclare à part et partage son numéro : c'est voulu.
        self.ecrire("lexique/basar.md", "# basar\n\nLa chair.\n\n## Source\n\n1320 · בשר\n")
        self.ecrire("lexique/basar-echad.md", "# basar echad\n\nLe construit.\n\n## Source\n\n1320 + 259 · בשר אחד\n")
        r = kb.controles(self.vault)
        partages = [c for c in r["constats"] if c["controle"] == "numero_partage"]
        self.assertTrue(partages)
        self.assertTrue(all(c["gravite"] == "signal" for c in partages))
        self.assertEqual(r["bloquants"], 0, "un signal ne barre pas")


    def test_le_compteur_ne_fait_jamais_echouer_l_outil_et_ne_note_aucun_argument(self):
        # Épreuve de régression sur les deux promesses du compteur d'usage,
        # posées par l'auteur le 18 septembre 2026.
        #
        # La première : il NE FAIT JAMAIS ÉCHOUER L'OUTIL. Un compteur qui casse
        # la chose qu'il compte est pire que pas de compteur — et il écrit hors
        # du dépôt, donc sur un chemin que rien ne garantit.
        #
        # La seconde : il NE NOTE AUCUN ARGUMENT. Une tâche passée à `dossier`
        # peut contenir du texte du vault ; un journal d'usage n'a pas à le
        # recopier.
        reel = kb.JOURNAL_USAGE
        try:
            kb.JOURNAL_USAGE = "/racine-qui-n-existe-pas/impossible/x.jsonl"
            kb.journaliser(self.vault, "controles")  # ne doit rien lever
        finally:
            kb.JOURNAL_USAGE = reel

        kb.journaliser(self.vault, "dossier")
        journal = self.vault.parent / kb.JOURNAL_USAGE
        self.assertTrue(journal.exists(), "le compteur écrit quand il le peut")
        entree = json.loads(journal.read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual(sorted(entree), ["b", "c", "q", "s"],
                         "quatre champs et pas un de plus : démarrage, commande, "
                         "quand, session — aucun argument")
        self.assertEqual(entree["c"], "dossier")
        # Le socket est un PID : il se réattribue au redémarrage. Sans le champ
        # `b`, une fenêtre d'une semaine fondrait deux sessions sous un numéro
        # et couperait une session en deux, SANS QUE RIEN NE LE DISE. Relevé par
        # la session manageuse avant que le compteur ait produit une journée.
        self.assertIsInstance(entree["b"], int)
        journal.unlink()
