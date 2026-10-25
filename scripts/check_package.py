#!/usr/bin/env python3
"""Check the distributable's structure, links and common accidental data leaks."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "job-search-setup", "job-research", "job-application",
    "recruiting-outreach", "job-interview", "job-pipeline-review",
    "job-resume", "job-offer", "job-inbox", "job-search-schedule",
}
SKIP_PARTS = {".git", "__pycache__", ".cache"}
TEXT_SUFFIXES = {".md", ".py", ".json", ".yaml", ".yml", ".template", ".txt"}
WORKFLOW_SVG = "docs/assets/job-search-workflow.svg"
# Keep these exceptions narrow; both still pass the text privacy screen.
APPROVED_TEXT_ASSETS = {WORKFLOW_SVG, "scripts/render-workflow.mjs"}
SVG_NAMESPACE = "http://www.w3.org/2000/svg"
SVG_ELEMENTS = {
    "svg", "g", "defs", "title", "desc", "style", "symbol", "use",
    "path", "rect", "circle", "ellipse", "line", "polyline", "polygon",
    "text", "tspan", "textPath", "marker", "clipPath", "mask", "pattern",
    "linearGradient", "radialGradient", "stop", "filter", "feBlend",
    "feColorMatrix", "feComponentTransfer", "feComposite", "feConvolveMatrix",
    "feDiffuseLighting", "feDisplacementMap", "feDistantLight", "feDropShadow",
    "feFlood", "feFuncA", "feFuncB", "feFuncG", "feFuncR", "feGaussianBlur",
    "feMerge", "feMergeNode", "feMorphology", "feOffset", "fePointLight",
    "feSpecularLighting", "feSpotLight", "feTile", "feTurbulence",
}
# Binary contents cannot pass the text privacy screen. Approve each asset only
# after visual/privacy review; any replacement requires a new reviewed digest.
APPROVED_BINARY_ASSETS = {
    "docs/assets/job-search-workflow.png": "60673d6e88addf06b85b06569eb1e66b6719b82afe1751f74e458d7353d87041",
}
SENSITIVE_PATTERNS = {
    "personal machine path": re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/"),
    "Windows personal path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\", re.IGNORECASE),
    "private Page or thread URL": re.compile(r"(?:chatgpt\.com/(?:space/)?page_|codex://threads/)[A-Za-z0-9-]+"),
    "private record identifier": re.compile(r"\bpage_[a-f0-9]{24,}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    "credential-like token": re.compile(r"\b(?:gh[pousr]_|github_pat_|sk-proj-|xox[baprs]-)[A-Za-z0-9_-]{20,}\b"),
    "email address": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
}


def inspect_text(text: str) -> list[str]:
    """Deliberately conservative screening; not a complete privacy detector."""
    return [label for label, pattern in SENSITIVE_PATTERNS.items() if pattern.search(text)]


def inspect_svg(content: str) -> list[str]:
    """Accept self-contained SVG shapes/text, without executable or fetched data."""
    if re.search(r"<!\s*(?:DOCTYPE|ENTITY)\b|<\?(?!xml(?:\s|\?>))", content, re.IGNORECASE):
        return ["SVG declarations or processing instructions are not allowed"]
    try:
        document = ET.fromstring(content)
    except ET.ParseError:
        return ["invalid SVG XML"]
    if document.tag not in {"svg", f"{{{SVG_NAMESPACE}}}svg"}:
        return ["SVG root must be svg"]

    errors: set[str] = set()
    allowed_namespaces = {SVG_NAMESPACE, "http://www.w3.org/1999/xlink", "http://www.w3.org/XML/1998/namespace"}

    def inspect_value(value: str, *, css: bool = False) -> None:
        # XML parsing resolves character references before privacy/link checks.
        errors.update(inspect_text(value))
        if re.search(r"(?:https?|file|data|javascript):|//", value, re.IGNORECASE) and not css:
            errors.add("SVG external references are not allowed")
        for match in re.finditer(r"url\s*\((.*?)\)", value, re.IGNORECASE | re.DOTALL):
            target = match.group(1).strip().strip("\"'")
            if not re.fullmatch(r"#[A-Za-z_][\w:.-]*", target):
                errors.add("SVG external references are not allowed")
        if "\\" in value or (css and re.search(r"@import\b|expression\s*\(", value, re.IGNORECASE)):
            errors.add("SVG CSS imports, escapes and expressions are not allowed")

    for element in document.iter():
        tag = element.tag.removeprefix(f"{{{SVG_NAMESPACE}}}")
        if tag not in SVG_ELEMENTS:
            errors.add("SVG contains a non-native or disallowed element")
        if element.text:
            errors.update(inspect_text(element.text))
            if tag == "style":
                inspect_value(element.text, css=True)
        if element.tail:
            errors.update(inspect_text(element.tail))
        for name, value in element.attrib.items():
            if name.startswith("{"):
                namespace, name = name[1:].split("}", 1)
                if namespace not in allowed_namespaces:
                    errors.add("SVG uses an unsupported attribute namespace")
            if name.lower().startswith("on"):
                errors.add("SVG event handlers are not allowed")
            if name == "href" and not re.fullmatch(r"#[A-Za-z_][\w:.-]*", value):
                errors.add("SVG external references are not allowed")
            inspect_value(value, css=name == "style")
    return sorted(errors)


def check(root: Path) -> list[str]:
    errors: list[str] = []
    root = root.resolve()
    for file in sorted(root.rglob("*")):
        relative = file.relative_to(root)
        if any(part in SKIP_PARTS for part in relative.parts) or file.name == ".DS_Store":
            continue
        if file.is_symlink():
            errors.append(f"{relative}: symbolic links must not enter the distributable")
            continue
        if not file.is_file():
            continue
        if relative.parts[0] in {"private", "workspace", "roles", "outreach", "resumes"}:
            errors.append(f"{relative}: candidate-data directory at package root")
        if relative.as_posix() in APPROVED_BINARY_ASSETS:
            digest = hashlib.sha256(file.read_bytes()).hexdigest()
            if digest != APPROVED_BINARY_ASSETS[relative.as_posix()]:
                errors.append(f"{relative}: changed binary asset; visual/privacy review required")
            continue
        if (file.suffix not in TEXT_SUFFIXES and file.name not in {"LICENSE", ".gitignore"}
                and relative.as_posix() not in APPROVED_TEXT_ASSETS):
            errors.append(f"{relative}: unexpected file type; inspect before sharing")
            continue
        try:
            content = file.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"{relative}: non-text data")
            continue
        errors.extend(f"{relative}: {label}" for label in inspect_text(content))
        if relative.as_posix() == WORKFLOW_SVG:
            errors.extend(f"{relative}: {label}" for label in inspect_svg(content))
        if file.suffix == ".json":
            try:
                json.loads(content)
            except json.JSONDecodeError as exc:
                errors.append(f"{relative}: invalid JSON: {exc}")
        if file.suffix == ".md":
            for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
                url = match.group(1).strip().strip("<>")
                if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("#"):
                    continue
                local = unquote(url.split("#", 1)[0])
                target = (file.parent / local).resolve()
                if not target.is_relative_to(root) or not target.exists():
                    errors.append(f"{relative}: unresolved/outside local link {url}")

    skills = root / "skills"
    found = {p.parent.name for p in skills.glob("*/SKILL.md")}
    if found != EXPECTED_SKILLS:
        errors.append(f"Skill catalog mismatch: expected {sorted(EXPECTED_SKILLS)}, found {sorted(found)}")
    for name in sorted(found):
        skill = skills / name
        content = (skill / "SKILL.md").read_text()
        if not content.startswith("---\n") or "\n---\n" not in content[4:]:
            errors.append(f"{name}: missing frontmatter")
            continue
        header = content.split("---", 2)[1]
        fields = dict(line.split(":", 1) for line in header.strip().splitlines() if ":" in line)
        fields = {k.strip(): v.strip().strip('\"\'') for k, v in fields.items()}
        if fields.get("name") != name or not fields.get("description"):
            errors.append(f"{name}: name/description does not match skill")
        if len(content.split()) > 700:
            errors.append(f"{name}: entrypoint exceeds this package's 700-word budget")
        ui = skill / "agents" / "openai.yaml"
        if not ui.exists():
            errors.append(f"{name}: missing UI metadata")
            continue
        # This package deliberately uses only quoted scalar UI fields.
        values = {}
        for key in ("display_name", "short_description", "default_prompt"):
            m = re.search(rf"^  {key}: (.+)$", ui.read_text(), re.MULTILINE)
            try:
                value = json.loads(m.group(1)) if m else None
            except json.JSONDecodeError:
                value = None
            if not isinstance(value, str):
                errors.append(f"{name}: invalid quoted UI field {key}")
            else:
                values[key] = value
        if "short_description" in values and not 25 <= len(values["short_description"]) <= 64:
            errors.append(f"{name}: UI description length outside 25–64")
        if f"${name}" not in values.get("default_prompt", ""):
            errors.append(f"{name}: UI prompt must invoke this skill")

    try:
        manifest = json.loads((root / "plugin.json").read_text())
        onboarding = manifest["extensions"]["com.openai"]["onboardingSkill"]
        if not (root / onboarding).is_file():
            errors.append("Plugin onboarding skill does not exist")
        catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text())
        entry = catalog["plugins"][0]
        if entry["name"] != manifest["name"] or (root / entry["source"]["path"]).resolve() != root:
            errors.append("Marketplace does not resolve to this package")
    except (OSError, KeyError, IndexError, json.JSONDecodeError) as exc:
        errors.append(f"Plugin/catalog error: {exc}")

    template = skills / "job-search-setup/assets/workspace"
    for relative in ("AGENTS.md", "gitignore.template", "references/profile.md",
                     "references/preferences.md", "references/recordkeeping.md", "roles/INDEX.md",
                     "roles/applications.md", "outreach/contacts.md", "resumes/INVENTORY.md",
                     "interviews/INDEX.md", "offers/INDEX.md", "inbox/reviews.md", "schedules/automations.md"):
        if not (template / relative).is_file():
            errors.append(f"Missing blank template: {relative}")
    if (template / ".gitignore").exists():
        errors.append("Bundled .gitignore would hide templates; keep gitignore.template until initialization")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Package or extracted release directory")
    args = parser.parse_args()
    errors = check(args.root)
    if errors:
        print("Package check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Package check passed: {len(EXPECTED_SKILLS)} skills, routing links, templates, metadata and leak screening.")
    print("This is a local structural/privacy screen, not host installation or complete privacy certification.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
