# Agent reference

## Install and update

Use the host's supported skill installer to install the folders under `skills/`. The repository also includes plugin metadata for compatible clients. Installation support varies by host; check the actual capabilities before reporting success.

Setup uses ordinary file tools and the [blank templates](../skills/job-search-setup/assets/workspace/AGENTS.md). Follow [job-search-setup](../skills/job-search-setup/SKILL.md) to create a private workspace or map existing records. No Python installation step is required.

For an update, replace the installed skill files through the host's installer or file tools. Preserve custom instructions and private records. Merge useful router changes into an existing `AGENTS.md`; do not replace it with the blank template. All ten skill IDs remain compatible with v0.3.0. A host may display all ten even though the README leads with four.

## Skill map

| Entry point | Stable ID |
| --- | --- |
| [Find and Apply to Jobs](../skills/job-research/SKILL.md) | `job-research` |
| [Find and Request Referrals](../skills/recruiting-outreach/SKILL.md) | `recruiting-outreach` |
| [Interview Coach](../skills/job-interview/SKILL.md) | `job-interview` |
| [Offer Negotiator](../skills/job-offer/SKILL.md) | `job-offer` |

The first two flows find options, present a concrete proposal and execute after confirmation. Applications use browser/computer-use tools for forms, uploads and submission; referrals use available messaging or browser tools. Keep explicit review-first requests in force even when an older grant exists. Supporting workflows remain available directly and through handoffs:

| Task | Skill |
| --- | --- |
| Map or create a private workspace | [job-search-setup](../skills/job-search-setup/SKILL.md) |
| Select or tailor materials | [job-resume](../skills/job-resume/SKILL.md) |
| Complete authorized applications | [job-application](../skills/job-application/SKILL.md) |
| Reconcile recruiting messages | [job-inbox](../skills/job-inbox/SKILL.md) |
| Review progress and next actions | [job-pipeline-review](../skills/job-pipeline-review/SKILL.md) |
| Configure requested recurring work | [job-search-schedule](../skills/job-search-schedule/SKILL.md) |

## Records and tools

The private `AGENTS.md` maps facts, preferences and live records. Each role has one authoritative history; outreach has a separate linked record. Preserve submitted resumes and receipts. Dashboards and summaries read these sources rather than creating another tracker.

Local files support drafts, coaching and supplied records. Current role research needs search access; resume visual checks need document tools. Applications, inbox checks and scheduled work need the corresponding host capabilities and authorization. Report missing access honestly.

There are no bundled accounts, connectors, telemetry or automatic background jobs. Skills provide instructions; they do not enforce permissions across every host or guarantee hiring outcomes. See [validation](VALIDATION.md) for what was tested and [the roadmap](RELEASE_PLAN.md) for planned work.
