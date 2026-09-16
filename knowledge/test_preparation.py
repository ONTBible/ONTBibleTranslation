import importlib.util
import copy
import json
from pathlib import Path
import tempfile
import unittest


def charger(nom):
    spec = importlib.util.spec_from_file_location(nom, Path(__file__).with_name(nom + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


raccordement = charger("preparer-raccordement")
journaux = charger("preparer-journal")
reconciliation = charger("reconcilier-journal")


class Preparation(unittest.TestCase):
    def test_proposition_preserve_les_reglages_et_necrit_pas_chez_les_voisins(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp)
            for nom in ("ONTBibleApp", "ONTBibleWebapp", "ONTBibleTranslation"):
                (parent / nom).mkdir()
            p = parent / ".claude/settings.json"
            p.parent.mkdir()
            ancien = {"permissions": {"deny": ["Bash(rm:*)"]}, "hooks": {
                "UserPromptSubmit": [{"hooks": [{"type": "command", "command": "existing-hook"}]}]}}
            p.write_text(json.dumps(ancien))
            avant = {str(f): f.read_bytes() for f in parent.rglob("*") if f.is_file()}
            r = raccordement.preparer(parent)
            self.assertEqual(len(r["changements"]), 13)
            self.assertEqual(avant, {str(f): f.read_bytes() for f in parent.rglob("*") if f.is_file()})
            proposition = next(c for c in r["changements"] if c["cible"] == str(p))
            nouveau = json.loads(proposition["contenu_propose"])
            self.assertEqual(nouveau["permissions"], ancien["permissions"])
            self.assertEqual(nouveau["hooks"]["UserPromptSubmit"][0], ancien["hooks"]["UserPromptSubmit"][0])
            # Simulation autorisée dans la fixture, puis deuxième préparation sans doublons.
            for c in r["changements"]:
                cible = Path(c["cible"])
                cible.parent.mkdir(parents=True, exist_ok=True)
                cible.write_text(c["contenu_propose"])
            self.assertEqual(raccordement.preparer(parent)["changements"], [])

    def test_hook_codex_preserve_un_hook_preexistant(self):
        ancien = json.dumps({"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "existing-hook"}]}]}})
        nouveau = raccordement.reglages(ancien, "python3 /vault/hook.py", codex=True)
        self.assertEqual(json.loads(nouveau)["hooks"]["Stop"], json.loads(ancien)["hooks"]["Stop"])
        h = json.loads(nouveau)["hooks"]["UserPromptSubmit"][0]["hooks"][0]
        self.assertEqual(h["additionalContextLimit"], 12000)
        self.assertEqual(raccordement.reglages(nouveau, h["command"], codex=True), nouveau)

    def test_marqueurs_incomplets_refuses(self):
        with self.assertRaises(ValueError):
            raccordement.bloc("Instructions\n" + raccordement.DEBUT, "KB")

    def test_revue_conserve_variantes_et_distingue_separateur_et_texte(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp)
            for nom, mot, separation in (("a", "Elohim", ""), ("b", "Elohim", "\n\n---"), ("c", "ʾElohim", "")):
                dossier = parent / nom
                dossier.mkdir()
                (dossier / "SYNCHRONISATION.md").write_text(
                    "# Journal\n\n## 1 septembre 2026 — entrée\n\n" + mot +
                    "\n\n## 2 septembre 2026 — autre\n\nTexte" + separation + "\n")
            (parent / "SYNCHRONISATION.md").write_text("Racine ancienne non candidate")
            avant = {str(f): f.read_bytes() for f in parent.rglob("*.md")}
            r = journaux.preparer(parent)
            self.assertEqual(r["bilan"]["divergences_contenu"], 2)
            self.assertEqual(r["bilan"]["differences_separateur_final"], 1)
            self.assertEqual(len(r["entrees"][0]["variantes"]), 2)
            self.assertNotIn("Racine ancienne", str(r["preambules"]))
            self.assertEqual(avant, {str(f): f.read_bytes() for f in parent.rglob("*.md")})

    def test_reconciliation_preserve_les_entrees_et_refuse_une_variante_non_relue(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp)
            for nom, corps, ajout in (("a", "Exemple original", ""), ("b", "Exemple corrigé", ""),
                                     ("c", "Exemple original", "\n\n## 2 septembre 2026 — ajout\n\nÀ conserver")):
                dossier = parent / nom
                dossier.mkdir()
                (dossier / "SYNCHRONISATION.md").write_text("# Journal\n\n## 1 septembre 2026 — entrée\n\n" + corps + ajout + "\n")
            rapport = journaux.preparer(parent)
            e = rapport["entrees"][0]
            sha = rapport["preambules"][0]["sha256"]
            resolutions = {"preambules_examines": [sha], "preambules": dict.fromkeys(("vault", "base", "complement"), sha),
                           "reference_historique": {"commit": "fixture"}, "entrees": {e["titre"]: {
                               "sha256_corps_normalise": journaux.empreinte("Exemple original"),
                               "variantes_examinees": sorted(v["sha256_corps"] for v in e["variantes"]),
                               "motif": "Préserver la transcription historique relue."}}}
            avant = {str(f): f.read_bytes() for f in parent.rglob("*.md")}
            r = reconciliation.reconcilier(rapport, resolutions)
            self.assertEqual(len(r["entrees"]), 2)
            self.assertIn("À conserver", r["texte"])
            self.assertIn("Exemple original", r["texte"])
            self.assertNotIn("Exemple corrigé", r["texte"])
            self.assertEqual(avant, {str(f): f.read_bytes() for f in parent.rglob("*.md")})
            nouveau = copy.deepcopy(rapport)
            v = nouveau["entrees"][0]["variantes"][1]
            v["corps"] = "Texte changé depuis la revue"
            v["sha256_corps"] = journaux.empreinte(v["corps"])
            with self.assertRaisesRegex(ValueError, "Variante non relue"):
                reconciliation.reconcilier(nouveau, resolutions)

    def test_migration_locale_conserve_sous_sections_et_fichier_existant_sans_ecrire(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp)
            depot = parent / "depot"
            depot.mkdir()
            source = depot / "SYNCHRONISATION.md"
            locale = "### 1 septembre 2026 — note *(local)*\n\nTexte exact.\n\n#### Détail\n\nÀ garder.\n\n"
            source.write_text("# Journal\n\n" + locale + "## 2 septembre 2026 — commun\n\nCommun.\n")
            cible = depot / "SYNCHRONISATION-locale.md"
            ancien = "# Mes notes\n\n### 31 août 2026 — existante *(local)*\n\nDéjà écrite.\n"
            cible.write_text(ancien)
            avant = {str(f): f.read_bytes() for f in depot.iterdir()}
            rapport = journaux.preparer(parent)
            migration = reconciliation.preparer_locales(rapport["copies"])[0]
            self.assertTrue(migration["changement_propose"])
            self.assertTrue(migration["contenu_propose"].startswith(ancien))
            self.assertIn(locale, migration["contenu_propose"])
            self.assertNotIn("Commun.", migration["contenu_propose"])
            self.assertEqual(migration["entrees_a_preserver"][0]["ligne_source"], 3)
            self.assertEqual(avant, {str(f): f.read_bytes() for f in depot.iterdir()})
            # Application uniquement dans la fixture : une deuxième préparation n'ajoute rien.
            cible.write_text(migration["contenu_propose"])
            self.assertFalse(reconciliation.preparer_locales(rapport["copies"])[0]["changement_propose"])
            cible.write_text(migration["contenu_propose"].replace("Texte exact.", "Autre version."))
            with self.assertRaisesRegex(ValueError, "Conflit avec le journal local"):
                reconciliation.preparer_locales(rapport["copies"])

    def test_migration_cree_seulement_une_proposition_et_refuse_une_source_modifiee(self):
        with tempfile.TemporaryDirectory() as tmp:
            parent = Path(tmp)
            depot = parent / "depot"
            depot.mkdir()
            source = depot / "SYNCHRONISATION.md"
            source.write_text("# Journal\n\n## 1 septembre 2026 — note *(local)*\n\nUne note.\n")
            rapport = journaux.preparer(parent)
            migration = reconciliation.preparer_locales(rapport["copies"])[0]
            self.assertIsNone(migration["sha256_avant"])
            self.assertIn("Une note.", migration["contenu_propose"])
            self.assertFalse(Path(migration["cible"]).exists())
            source.write_text(source.read_text() + "Ajout concurrent.\n")
            with self.assertRaisesRegex(ValueError, "Journal modifié"):
                reconciliation.preparer_locales(rapport["copies"])


if __name__ == "__main__":
    unittest.main()
