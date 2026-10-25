# Maintaining Job Search Skills

This repository contains public workflows and blank templates, not a candidate's job search. Keep personal records in a separate private workspace.

Read the relevant `skills/<name>/SKILL.md` before changing that workflow. Preserve progressive loading, scoped user approvals, factual corrections, evidence-backed stages, and the distinction between application and outreach records. Candidate preferences, countries, seniority, browser limits and employer exceptions are configuration, not universal policy.

Use synthetic examples in tests. Never copy a real resume, receipt, email, contact list, account identifier, local machine path or private conversation into this repository, including commit messages. Do not execute recruiting actions while maintaining skills.

After changes, run `python3 scripts/check_package.py` and `python3 -m unittest discover -s tests -v`. For substantial workflow changes, also run an independent scenario review using synthetic records. Structural checks do not prove safe agent behavior. Keep the install instructions and skill loading routes consistent with the files.

Publishing or connecting a remote is a separate action from preparing this repository. Do not create background jobs or add telemetry, credentials, external connectors or executable install hooks.
