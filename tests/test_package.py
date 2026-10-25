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

    def test_svg_allows_native_shapes_filters_and_local_references(self):
        source = '''<svg xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 100 100">
          <defs>
            <marker id="arrow"><path d="M0 0L5 5L0 10Z"/></marker>
            <filter id="shadow"><feGaussianBlur stdDeviation="2"/></filter>
            <g id="card"><rect width="50" height="30"/></g>
          </defs>
          <use xlink:href="#card" style="filter: url('#shadow')"/>
          <path d="M0 0L100 100" marker-end="url(#arrow)"/>
          <text aria-label="Stage: review">Review<tspan> and confirm</tspan></text>
        </svg>'''
        self.assertEqual(module.inspect_svg(source), [])

    def test_svg_rejects_executable_embedded_or_external_content(self):
        fragments = (
            '<script>alert(1)</script>',
            '<foreignObject><p>HTML</p></foreignObject>',
            '<image href="data:image/png;base64,AAAA"/>',
            '<feImage href="#shape"/>',
            '<use href="https://example.invalid/external.svg#shape"/>',
            '<use href="external.svg#shape"/>',
            '<use href="&#104;ttps://example.invalid/external.svg#shape"/>',
            '<rect onclick="alert(1)"/>',
            '<rect fill="url(external.svg#paint)"/>',
            '<rect style="fill: url(https://example.invalid/paint.svg)"/>',
            '<style>@import "https://example.invalid/style.css";</style>',
            '<style>rect { fill: url(data:image/png;base64,AAAA); }</style>',
        )
        for fragment in fragments:
            with self.subTest(fragment=fragment):
                self.assertTrue(module.inspect_svg('<svg>' + fragment + '</svg>'))
        for source in (
            '<svg><rect></svg>',
            '<?xml-stylesheet href="external.css"?><svg/>',
            '<!DOCTYPE svg SYSTEM "external.dtd"><svg/>',
        ):
            with self.subTest(source=source):
                self.assertTrue(module.inspect_svg(source))

    def test_svg_and_renderer_still_receive_privacy_screening(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"))
            personal_path = "/" + "Users" + "/fictional-person/resume.md"
            (root / module.WORKFLOW_SVG).write_text('<svg><text>' + personal_path + '</text></svg>')
            renderer = root / "scripts/render-workflow.mjs"
            renderer.write_text('// ' + personal_path)
            errors = module.check(root)
            self.assertIn(module.WORKFLOW_SVG + ": personal machine path", errors)
            self.assertIn("scripts/render-workflow.mjs: personal machine path", errors)
            # Numeric XML references cannot hide the same path from SVG parsing.
            encoded = personal_path.replace("/", "&#47;")
            self.assertIn("personal machine path", module.inspect_svg('<svg><text>' + encoded + '</text></svg>'))

    def test_svg_and_renderer_are_allowed_only_at_exact_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "package"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store"))
            (root / "unapproved.svg").write_text('<svg/>')
            (root / "unapproved.mjs").write_text('// synthetic script')
            errors = module.check(root)
            for name in ("unapproved.svg", "unapproved.mjs"):
                self.assertIn(name + ": unexpected file type; inspect before sharing", errors)

    def test_documentation_link_allowed(self):
        self.assertEqual(module.inspect_text("https://developers.openai.com/codex/skills"), [])


if __name__ == "__main__":
    unittest.main()
