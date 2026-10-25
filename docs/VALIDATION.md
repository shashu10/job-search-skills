# Validation and limits

Release: v0.2.0, 25 October 2026.

## Automated checks

The package checker validates the ten-skill catalog, frontmatter, UI metadata, local routing links, blank templates and representative privacy patterns. It rejects unexpected file types and symlinks. To inspect an extracted release, run `python3 scripts/check_package.py --root PATH`.

The 16-test unit suite exercises fresh initialization with all ten skills, existing destination preservation, public-package destination refusal, invalid catalogs, symlink boundaries, standalone setup, private links, credential patterns and personal paths. CI is configured for Python 3.10 and 3.13.

These are structural and program tests. They do not prove that a model obeys every instruction or that every portal works.

## Independent decision exercises

The inputs in [cases.json](../tests/scenarios/cases.json) are fictional. Independent evaluators receive the named skill and raw inputs without the scoring rubric, execute into disposable workspaces, and preserve outputs and record changes. The [scenario guide](../tests/scenarios/README.md) describes the checks reviewed afterward.

On 25 October 2026, two independent Codex evaluators executed five cases each. The release coordinator inspected their responses and selected persisted records. All ten cases produced the intended bounded decisions; no substantive workflow failure was observed. [Observed responses](../tests/scenarios/observed-responses.json) contain the actual fictional outputs, with no local execution paths or candidate data.

| Case | Observed result |
| --- | --- |
| Resume correction | Unsupported ownership/metric removed; submitted artifact hash unchanged; feedback decision left attributable |
| Application routing | Later referral hold retained; no submission |
| Submission timeout | Attempt stayed unconfirmed; no retry or confirmed count |
| Interview practice | 60-minute plan and first independent question; actual interview AI restriction preserved |
| Offer cash | First-year cash 110,000 versus 113,000; discretionary bonus/equity excluded; no acceptance |
| Inbox incomplete | Duplicate skipped, exact-role invitation applied, rejection unresolved, previous checkpoint retained |
| Schedule unavailable | Requested change saved separately from last verified state; no successful update claimed |
| Agency introduction | General enquiry drafted without inventing a vacancy or sending |
| Pipeline unknowns | Two applications and a separate recruiter process; only one confirmed completed round |
| Discovery unknowns | Exact requisition deduplicated, level preserved, eligibility and language unknowns retained |

No real employer, mailbox, contact, scheduler or application was exercised. The interview stopped for a candidate answer; no performance gain was established. Resume visual QA was unavailable and not claimed. Provider pagination, concurrent writes, crashes and expired cursors were not exercised against live software. Model identifiers were not captured in the evaluation records. These are single dry-run observations, not a reliability score or cross-model benchmark.

## Compatibility and external execution

The helper requires Python 3.10 or later and no third-party libraries. Direct skill folders and plugin metadata follow the documented format. Marketplace installation has not been certified across host versions. No universal plugin-directory listing is claimed.

This release includes no provider implementations, scheduler service, UI or deterministic permission-enforcement runtime. External outcomes depend on the host, tools, user access and actual instructions. Resume rendering requires separate document tools. Behavioral evaluations are limited observations, not guarantees of future behavior.

## Privacy review

Release preparation uses public procedures, blank templates and fictional evidence. The automated scanner is supplemented by manual file-content review and inspection of the exported tree. Git identity uses the public account name and its no-reply address. A release archive excludes `.git`, local caches and untracked data.
