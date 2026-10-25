# Product and release plan

Updated 25 October 2026 for v0.3.4. The [README](../README.md) is the current capability reference.

## Current: four entry points, ten supporting workflows

Lead with Find and Apply to Jobs, Find and Request Referrals, Interview Coach and Offer Negotiator. Preserve the ten stable workflow IDs: setup, resume, research, outreach, application, interview, offer, inbox, pipeline review and requested scheduling. Keep private facts and live records outside the public package. Use natural-language installation and agent-managed setup from blank templates. Include a fictional walkthrough, decision scenarios, validation notes and an MIT license.

Sourcing produces a reviewable shortlist. Confirmation starts applications, including resume work, browser/computer-use form filling, uploads and verified submission. Referral research can sweep the applied-role cohort, preserve existing conversations and send selected requests after confirmation. Interview coaching and compensation discussions can start before an invitation or offer. Execution, inbox and scheduling use available host tools; they do not bundle connectors or a scheduler. Resume preparation uses available document tooling; no personal template or new renderer is included.

## Next: records and optional UI

Define a versioned contract for opportunities, applications, contacts, outreach, interview rounds, materials, evidence, permissions and dated events. Preserve separate event and reporting dates. Support existing Markdown workspaces through explicit mapping; do not create a competing tracker.

Build a local read-only dashboard opening on **What needs attention?** Show verified deadlines, preparation, employer requests, blockers and their sources. Connect verified experience, the exact resume submitted, conversations, receipt evidence, interview instructions and preparation gaps.

Applications and referrals are parallel routes. An invitation, a completed round and confirmed advancement are separate events. A board drag must not assert that an external action occurred.

Introduce editing only after choosing one authoritative record representation and a shared mutation interface. Validate identities and record revisions; refresh holds before external execution. Distinguish protections enforced by code from instructions followed by the agent.

## Demonstrate continuity

Use one fictional journey in the article, README and short recording: source → review → authorize → select or tailor resume → application evidence → referral route → practice → feedback → retry → compensation discussion. Also demonstrate that coaching works independently. Label interface concepts and fixture evidence; demonstrate only implemented capabilities.

Start with experienced engineers already using coding agents. Observe 5–10 users completing setup and a role workflow. Measure time to a useful brief, repeated questions, corrections caught and whether a returning user can identify the next action without reconstructing old chats. Hiring outcomes require dated cohorts and cannot establish causation alone.

## Positioning and distribution

Suggested headline: **Find and apply to jobs, request referrals, practice interviews and negotiate offers with the AI agent you already use.**

Lead with connected context, inspectable records and useful next steps. Open source, local storage and agent skills already appear in related projects; avoid first/only claims or unsupported promises of better hiring outcomes. The [fictional walkthrough](../examples/walkthrough.md) should make the benefit tangible.

Pair a tagged GitHub release with a practical article and short demo. Give readers one action: paste the install prompt into their agent. Invite specific contributions such as an importer, document adapter or evaluation case. Prioritize repeat use and successful workflows over star counts or application volume.

## Release discipline

Run package/unit checks, independent synthetic exercises and a manual privacy review. Inspect the exact Git tree and release archive. Use public no-reply commit metadata. Publish source and downloadable artifacts with checksums. Describe host-installation and external-tool limitations honestly.

Keep the useful core under MIT. Consider hosted sync or paid support only after demonstrated demand; neither is required for this release.
