"""Verify screening catches representative leaks without using private fixtures."""

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_check", ROOT / "scripts/check_package.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PackageTests(unittest.TestCase):
    def test_package_is_consistent(self):
        self.assertEqual(module.check(ROOT), [])

    def test_private_link_flagged(self):
        fixture = "https://chatgpt.com/space/" + "page_" + "a" * 32
        self.assertIn("private Page or thread URL", module.inspect_text(fixture))

    def test_contact_address_flagged(self):
        fixture = "candidate" + "@" + "example.invalid"
        self.assertIn("email address", module.inspect_text(fixture))

    def test_credential_flagged(self):
        fixture = "ghp_" + "x" * 36
        self.assertIn("credential-like token", module.inspect_text(fixture))

    def test_oauth_and_fine_grained_tokens_flagged(self):
        for prefix in ("gho_", "ghs_", "github_pat_", "sk-proj-", "xoxb-"):
            with self.subTest(prefix=prefix):
                self.assertIn("credential-like token", module.inspect_text(prefix + "x" * 36))

    def test_personal_paths_flagged(self):
        unix_path = "/" + "Users" + "/fictional-person/resume.md"
        windows_path = "C:" + "\\" + "Users" + "\\fictional-person\\resume.md"
        self.assertIn("personal machine path", module.inspect_text(unix_path))
        self.assertIn("Windows personal path", module.inspect_text(windows_path))

    def test_private_key_flagged(self):
        fixture = "-----BEGIN " + "OPENSSH PRIVATE KEY-----"
        self.assertIn("private key", module.inspect_text(fixture))

    def test_release_scan_rejects_unexpected_files_and_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"))
            (root / "resume.pdf").write_bytes(b"synthetic binary")
            (root / "linked.md").symlink_to(root / "README.md")
            errors = module.check(root)
            self.assertTrue(any("resume.pdf: unexpected file type" in e for e in errors))
            self.assertTrue(any("linked.md: symbolic links" in e for e in errors))

    def test_release_scan_rejects_changed_approved_image(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"))
            image = root / "docs/assets/job-search-workflow.png"
            image.write_bytes(image.read_bytes() + b"synthetic change")
            self.assertIn(
                "docs/assets/job-search-workflow.png: changed binary asset; visual/privacy review required",
                module.check(root),
            )

    def test_release_scan_rejects_image_outside_approved_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"))
            # Even reviewed bytes are permitted only at their approved path.
            shutil.copyfile(root / "docs/assets/job-search-workflow.png", root / "unapproved.png")
            self.assertIn(
                "unapproved.png: unexpected file type; inspect before sharing",
                module.check(root),
            )

    def test_documentation_link_allowed(self):
        self.assertEqual(module.inspect_text("https://developers.openai.com/codex/skills"), [])


if __name__ == "__main__":
    unittest.main()
