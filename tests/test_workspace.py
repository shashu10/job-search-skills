"""Exercise real initialization boundaries in disposable directories."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/job-search-setup/scripts/init_workspace.py"
spec = importlib.util.spec_from_file_location("workspace_init", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def test_cli_creates_private_workspace_with_ten_skills(self):
        target = self.base / "search with spaces"
        result = subprocess.run([sys.executable, str(SCRIPT), str(target), "--skills-dir", str(ROOT / "skills")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(list((target / ".agents/skills").glob("*/SKILL.md"))), 10)
        self.assertTrue((target / "references/profile.md").is_file())
        self.assertTrue((target / "roles/applications.md").is_file())
        for relative in ("interviews/INDEX.md", "offers/INDEX.md", "inbox/reviews.md", "schedules/automations.md"):
            self.assertTrue((target / relative).is_file(), relative)
        self.assertIn("*", (target / ".gitignore").read_text().splitlines())
        self.assertFalse((target / "gitignore.template").exists())
        self.assertFalse((target / ".git").exists())

    def test_existing_destination_unchanged(self):
        target = self.base / "existing"
        target.mkdir()
        marker = target / "AGENTS.md"
        marker.write_text("Existing decisions must survive.")
        with self.assertRaises(ValueError):
            module.create_workspace(target)
        self.assertEqual(marker.read_text(), "Existing decisions must survive.")
        self.assertEqual(list(target.iterdir()), [marker])

    def test_package_destination_rejected_without_creation(self):
        target = ROOT / "private-test-must-not-exist"
        with self.assertRaises(ValueError):
            module.create_workspace(target)
        self.assertFalse(target.exists())

    def test_symlink_destination_rejected(self):
        actual = self.base / "actual"
        actual.mkdir()
        target = self.base / "alias"
        target.symlink_to(actual, target_is_directory=True)
        with self.assertRaises(ValueError):
            module.create_workspace(target)
        self.assertEqual(list(actual.iterdir()), [])

    def test_invalid_catalog_does_not_create_workspace(self):
        empty = self.base / "empty"
        empty.mkdir()
        target = self.base / "uncreated"
        with self.assertRaises(ValueError):
            module.create_workspace(target, empty)
        self.assertFalse(target.exists())

    def test_standalone_setup_needs_no_other_skills(self):
        target = module.create_workspace(self.base / "standalone")
        self.assertTrue((target / "AGENTS.md").is_file())
        self.assertFalse((target / ".agents").exists())

    def test_skill_symlink_rejected_before_writes(self):
        catalog = self.base / "catalog"
        catalog.mkdir()
        (catalog / "job-research").symlink_to(ROOT / "skills/job-research", target_is_directory=True)
        target = self.base / "uncreated"
        with self.assertRaises(ValueError):
            module.create_workspace(target, catalog)
        self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
