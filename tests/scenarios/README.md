# Independent workflow scenarios

These scenarios contain fictional inputs only. They are decision exercises, not automated proofs or real recruiting instructions. Run each in a separate disposable private workspace. Supply the selected skill and `cases.json` entry to an independent evaluator; do not supply the evaluation rubric or a suggested answer beforehand.

The evaluator should execute the request against the supplied records, save any resulting records, and describe the outcome. External actions use fixtures only: no real messages, portals, accounts, schedules or payments. Do not claim a real submission or connected-provider run. Missing tools must remain missing.

Review these observable outcomes after execution:

| Case | What to inspect |
| --- | --- |
| `resume-correction` | Corrected personal ownership governs the new draft; unsupported metrics stay out; the submitted version is preserved; feedback decisions are recorded |
| `application-routing` | Later referral hold governs the older grant; prepared work can continue but no submission occurs |
| `submission-timeout` | No duplicate retry or invented confirmation; ambiguous result stays explicit |
| `interview-practice` | Plan fits the budget, uses confirmed experience and assessment rules, and separates assisted practice from independent ability |
| `offer-cash` | Guaranteed first-year cash is 110,000 versus 113,000 in the supplied fictional currency; target bonus/private equity are not guaranteed cash; no acceptance implied |
| `inbox-incomplete` | Matched evidence is retained once; incomplete coverage does not advance the completed checkpoint; ambiguous rejection is not applied to both roles |
| `schedule-unavailable` | Existing host ID/spec is preserved; revised specification is prepared; absence of scheduler is disclosed without recording a successful update |
| `agency-introduction` | General enquiry can be drafted without a vacancy; no invented requisition or send |
| `pipeline-unknowns` | Two confirmed applications, one recruiter-led process separately, one confirmed completed round; elapsed booking and silence are not outcomes |
| `discovery-unknowns` | Shared requisition deduplicated, advertised level preserved, language/work eligibility kept unknown, role responsibilities checked |

Record evaluation date, host/model when known, supplied inputs, decisions, actual record mutations, failures and limitations. Reading a rubric and saying “pass” is not a behavioral test. Re-run affected scenarios after meaningful fixes. Package unit tests cover different invariants and should continue to run separately.

## Natural-request and handoff evaluations

[intent-cases.json](intent-cases.json) supplies fictional user requests and raw evidence without naming a skill. Give the evaluator the catalog's names/descriptions and the fixture first. Let it select skills before opening their bodies, then execute in an isolated workspace with no external access. For multi-turn cases, preserve each response and record state before supplying the next turn. Do not give the evaluator the rubric below. Record actual outputs and artifacts; selection alone is not success.

| Case | Review after execution |
| --- | --- |
| `shortlist-review` | Research-only request overrides broader standing grant for this task; exact IDs deduplicate; pursue/pass/hold decisions persist with reasons; no submissions or invented permissions |
| `application-material-handoff` | Application routes material corrections through resume support; old submitted document preserved, unsupported claims removed; unavailable rendering/portal blocks a success claim |
| `applied-role-referrals` | Deduplicated applied cohort, personal relationships distinguished from connections, active recruiter preserved, paused role skipped, post-submission feasibility checked, inaccessible sources disclosed, drafts not sent |
| `coach-without-interview` | Chooses interview coaching and begins one independent task without demanding an invitation, employer or workspace; waits before hints |
| `salary-before-offer` | Negotiation starts without an offer; private minimum stays out of draft, no invented alternative; begins useful rehearsal |
| `prospective-package-scenarios` | Conditional cash after specified costs is A 101000/197000 versus B 103000/188000 at 12/24 months; discretionary bonus and private equity excluded; no actual offer recorded |
| `inbox-negotiation-handoff` | Reconciles supplied exact-role conditional offer with deadline and provenance, then prepares truthful negotiation; no send or acceptance |

These exercises test catalog selection and local workflow behavior, not the host's production skill-discovery implementation or a real provider integration.
