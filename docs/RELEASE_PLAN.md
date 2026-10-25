# Product and release plan

Updated 25 October 2026 for v0.2.0. This replaces the earlier six-skill pilot proposal. The [README](../README.md) is the current capability reference.

## v0.2.0: the complete skill package

Ship ten focused workflows: setup, resume, research, outreach, application, interview, offer, inbox, pipeline review and requested scheduling. Keep private facts and live records outside the public package. Include blank templates, a Python initializer, a fictional walkthrough, decision scenarios, validation notes and an MIT license.

The inbox and scheduling skills instruct the user's agent how to use available capabilities; they do not bundle a mailbox connector or scheduler. Offer evaluation uses supplied terms and current primary evidence when needed. Resume preparation uses available document tooling; no personal template or new renderer is included.

## Next: records and optional UI

Define a versioned contract for opportunities, applications, contacts, outreach, interview rounds, materials, evidence, permissions and dated events. Preserve separate event and reporting dates. Support existing Markdown workspaces through explicit mapping; do not create a competing tracker.

Build a local read-only dashboard opening on **What needs attention?** Show verified deadlines, preparation, employer requests, blockers and their sources. Connect verified experience, the exact resume submitted, conversations, receipt evidence, interview instructions and preparation gaps.

Applications and referrals are parallel routes. An invitation, a completed round and confirmed advancement are separate events. A board drag must not assert that an external action occurred.

Introduce editing only after choosing one authoritative record representation and a shared mutation interface. Validate identities and record revisions; refresh holds before external execution. Distinguish protections enforced by code from instructions followed by the agent.

## Demonstrate continuity

Use one fictional journey in the article, README and short recording: confirmed experience → reviewed resume → suitable role → routing decision → application evidence → practice → debrief → targeted retry. Show a factual correction and a changed referral route. Label interface concepts and fixture evidence; demonstrate only implemented capabilities.

Start with experienced engineers already using coding agents. Observe 5–10 users completing setup and a role workflow. Measure time to a useful brief, repeated questions, corrections caught and whether a returning user can identify the next action without reconstructing old chats. Hiring outcomes require dated cohorts and cannot establish causation alone.

## Positioning and distribution

Suggested headline: **Run your job search with the AI agent you already use.**

Lead with connected context, inspectable records and useful next steps. Open source, local storage and agent skills already appear in related projects; avoid first/only claims or unsupported promises of better hiring outcomes. The [fictional walkthrough](../examples/walkthrough.md) should make the benefit tangible.

Pair a tagged GitHub release with a practical article and short demo. Give readers one action: download the package and run the example. Invite specific contributions such as an importer, document adapter or evaluation case. Prioritize repeat use and successful workflows over star counts or application volume.

## Release discipline

Run package/unit checks, independent synthetic exercises and a manual privacy review. Inspect the exact Git tree and release archive. Use public no-reply commit metadata. Publish source and downloadable artifacts with checksums. Describe host-installation and external-tool limitations honestly.

Keep the useful core under MIT. Consider hosted sync or paid support only after demonstrated demand; neither is required for this release.
