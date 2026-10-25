---
name: job-search-setup
description: Set up a private job-search workspace or map an existing search to reusable workflows, confirmed facts and authoritative trackers. Use for onboarding or restructuring, not routine applications or status reviews.
---

# Set up a job search

Create enough structure to pursue suitable interviews without turning preparation into the objective. Keep candidate data separate from the public skill package.

## Choose the workspace

Use the user's selected private workspace. A skill's install location is not the data location. If the active project already contains a search, inspect its instructions and map its existing profile, preferences, application trackers, outreach, resume inventory and interview notes. Preserve its names, storage services and ownership; do not impose a migration or create duplicate live trackers. A dashboard, if present, reads those same sources; it does not own a second set of stages.

For a new workspace, use the bundled [initializer](scripts/init_workspace.py) with the user-selected destination. It copies only the [blank workspace templates](assets/workspace/AGENTS.md), refuses existing destinations and makes no external calls. When working from the public repository, `--skills-dir <repository>/skills` also installs the bundle locally. A standalone installed skill can initialize templates without copying other skills. Run it only after resolving the intended destination; choose a sibling private folder when creating a new workspace beside a public repository.

## Gather only the missing decisions

Reuse a supplied resume and existing answers. Ask a small batch of questions about target work and level, feasible employment locations/work authorization, working languages, constraints, and immediate priorities. Record unknowns instead of blocking setup on optional details. Do not collect sensitive identifiers or legal declarations before a relevant authorized application needs them.

Keep facts with their source, confirmation date and precision in `references/profile.md`. Mark corrections and superseded claims. Link substantial work stories or evidence instead of repeating them in every application. Put preferences, exclusions, travel/relocation choices, workflow limits and any user-granted permission scopes in `references/preferences.md`. Record the user's chosen timezone for scheduling; a device timezone is not proof of residence or work rights. Do not turn an employer-specific answer or one-role exception into a general rule. Leave external-action permissions unset unless the user grants them.

## Establish loading and record ownership

Keep the private `AGENTS.md` short: standing boundaries, source mapping and when to load each installed skill/reference. Read [recordkeeping](assets/workspace/references/recordkeeping.md) when choosing tracker fields. Start with a single `roles/applications.md`; use `roles/INDEX.md` to map additional lanes and owners only if necessary. Use one outreach record, linked from relevant applications.

Reuse existing resume sources and templates; record usable variants in `resumes/INVENTORY.md`. Preserve submitted versions and receipts. Use `job-resume` when available for evidence gathering, feedback and material changes; setup need not rebuild materials. If that skill is unavailable, use the workspace's existing document workflow.

The template routes all ten skills without requiring every workflow at onboarding. `interviews/INDEX.md` maps briefs and practice notes; `offers/INDEX.md` maps offer evidence and comparisons; `inbox/reviews.md` records search coverage; `schedules/automations.md` records requested scheduler jobs and scope. Leave unused records blank. Employer outcomes still belong in application trackers, and communications still belong in outreach. Neither an inbox ledger nor an automation definition grants a new recruiting permission.

Verify that local links resolve, the next agent can identify its lane and current record, corrections remain discoverable, and no private files were put into the distributable package. Report what is ready, important unknowns and the next useful recruiting action. Setup itself sends no messages, submits no applications and schedules no monitoring.
