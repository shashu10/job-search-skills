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
