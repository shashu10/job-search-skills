# Contributing

Improve a workflow, add a fictional evaluation scenario, or report an installation problem. Keep changes focused and explain the request that motivated them. Read [AGENTS.md](AGENTS.md) before editing.

Use synthetic records. Do not attach real resumes, inbox exports, screenshots, account identifiers, private links, credentials or employer correspondence to issues or pull requests. Describe bugs with a minimal fictional reproduction. The public repository is for procedures and blank templates; personal searches belong in separate private workspaces.

Run these checks with Python 3.10 or later:

```sh
python3 scripts/check_package.py
python3 -m unittest discover -s tests -v
```

For workflow changes, also perform an independent dry run using [the evaluation scenarios](tests/scenarios/README.md). Inspect actual decisions and resulting records, including preservation of prior evidence. Passing a string-matching test does not establish correct agent behavior.

Skills should work with mapped private records and degrade usefully when optional siblings or external tools are unavailable. Do not hardcode countries, seniority, legal declarations, browser providers or personal preferences. Preserve current user authorization within scope and later corrections or holds.

Update workflow routing and the skill catalog when adding a skill. Keep `SKILL.md` under 700 words; put longer conditional guidance in a linked reference. Every skill has a concise trigger and matching `agents/openai.yaml`. Do not add telemetry, credentials, automatic install hooks or background jobs.

Changes are contributed under the repository's MIT license.
