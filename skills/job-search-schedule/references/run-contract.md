# Recurring run and recovery contract

Read when composing or updating a recurring prompt. Persist concrete configuration in the private workspace selected by the user. This is guidance for the host scheduler; it installs nothing by itself.

## Configuration to retain

| Field | Meaning |
|---|---|
| User request and date | Provenance of the recurring authorization |
| Purpose, workspace, owner and lane | Exact assignment; shared files do not transfer other queues |
| Allowed actions and exclusions | Separate research, record updates, submissions, messages and reminders |
| Applicable grants and expiration | References to current approval records, including contact/role exceptions |
| Schedule and IANA timezone | Local wall-clock recurrence or fixed elapsed cadence; start/end conditions |
| Per-run/day ceilings and day timezone | Caps, not quotas or permission to lower fit standards |
| Provider job ID and configuration status | Stable identity for updates, cancellation and recovery |
| Checkpoint location and overlap policy | Resume work without duplicating earlier actions |
| Notification policy | Destination and meaningful events to report |
| Verified running requirements | Whether the host/app must be open, signed in, online or awake |

When a daily limit exists, define its day boundary using the intended timezone. Apply limits across retries and overlapping jobs for the same authorized scope, not separately for each invocation. Clarify whether the user's limit concerns attempts, verified completions or both if it affects allowed volume. Reserve remaining capacity atomically in the shared action ledger before an external action. An unknown outcome retains its reservation until resolved; release it only when evidence establishes that the action did not occur, subject to any attempt limit. Stop when there are fewer suitable opportunities than the ceiling.

Do not invent sponsorship, qualification or recruiting permissions to satisfy a schedule. Recurring approval is revocable. Check the current tracker and outreach records at each run and before each external action; later holds or user corrections take precedence over the saved schedule prompt.

## Prompt contract

Write a cohesive prompt that names the task and mapped records, then includes the applicable constraints:

1. Reload the current assignment, facts, preferences, grants and checkpoint. Process time-sensitive evidence first when consistent with the assigned task. Do not expand into another lane or unrelated queue.
2. Respect configured browser/session limits. Before shared browser work, acquire the workspace's shared lock atomically and record the job/run owner, scope and start time. If no lock convention exists, establish one shared location in the private schedule configuration before the first browser run. Verify existing browser state and preserve unfinished forms even when the lock is free. If another owner holds the lock, do independent permitted work or defer the browser step. Age alone does not make a lock stale; verify the owner has stopped before clearing it. Release only this run's lock. All cooperating workers must use the same lock.
3. Refresh exact-role/contact records and deduplicate immediately before mutations. Keep an action ledger with identity, grant, attempt, outcome and evidence. On a timeout after submission or send, reconcile portal receipts, sent-message evidence or provider status before any retry. An unknown outcome must not trigger another send or submission.
4. Record each verified action in its authoritative record before continuing. Count verified events once, retain unresolved outcomes and preserve evidence. If an action succeeds but recording fails, stop further external actions until the record is repaired or the gap is surfaced for intervention.
5. Commit a checkpoint only for covered work. For inbox scans, follow `job-inbox` when installed, or retain complete retrieval boundaries, stable IDs, durable unresolved items and separate scanned/applied state. A partial or failed scan is not “nothing new.” Retries must stay inside remaining limits and the current grant.
6. Stay quiet while state is unchanged or non-actionable unless the user requested periodic reports. Notify on meaningful progress, completion, failure, a time-sensitive deadline, exhausted access or a required decision. Use the host's notification settings where supported. Do not send recruiting messages as a substitute for user notifications.
7. Stop or pause according to the user's explicit completion/expiry conditions and the scheduler's supported lifecycle. Do not automatically extend the grant, buy credits or create another schedule after failure.

An optional sibling skill supplies its workflow only. If it or a required tool is unavailable, use available authorized capabilities, state the limitation, and retain incomplete work. A provider's prompt or recurring-task description is not evidence that a run executed successfully.

## Idempotent lifecycle

Identify matching jobs by host job ID where possible, otherwise by workspace, lane, purpose and schedule. Titles alone may collide. Distinguish a request for a second independent job from an update. If several plausible jobs remain, resolve identity before altering them; do not delete unrelated jobs to simplify setup.

On an unknown create/update/delete outcome, inspect current provider state first. Preserve job IDs even if the local write fails. Only mark cancellation or completion after the host confirms the relevant state. If next-run previews are unavailable, say so instead of calculating a guaranteed execution time from an unverified recurrence interpretation.
