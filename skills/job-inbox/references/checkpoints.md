# Incremental inbox reconciliation

Use these rules when continuing a previous scan or implementing an explicitly requested recurring check. Keep checkpoint state in the selected private workspace; never in the installed skill or public package.

## Coverage and retrieval

Prefer a provider's documented incremental change cursor when it covers the authorized source, including new messages in existing threads. Inspect cursor expiry, pagination and reset behavior. Do not assume a thread identifier changes when a message arrives. On an invalid cursor, perform a bounded full rescan of the agreed window and disclose any older uncovered interval.

For date-based retrieval, establish a fixed run cutoff and search from the last fully covered boundary minus an overlap through that cutoff. Choose overlap based on provider date granularity and known indexing delays, record the choice, and state that delays beyond it remain a limitation. The first run needs an agreed start date; do not silently ingest the entire mailbox.

Read the provider's timestamp and boundary semantics. Translate the intended interval into its supported syntax, widening if necessary and filtering locally. Dates without times may use the provider's timezone. Include archived messages or sent context where the authorized scope and event matching require them; an inbox label or unread search is not exhaustive recruiting coverage.

Exhaust pagination for each bounded interval/query partition. If tool limits, time limits, errors or search truncation prevent completion, split into smaller intervals when supported. Otherwise retain an incomplete window and resume token, and keep the last fully covered checkpoint. Never advance to the newest message seen or equate a result limit with exhaustion. An opaque ranking search without an exhaustive listing guarantee yields partial coverage, even if its last result page is reached.

Repeated queries can return duplicate messages or a thread containing messages already processed. Deduplicate by provider/account identity plus immutable message ID and relevant attachment/version identifiers. Where stable IDs are absent, use a conservative fingerprint of source, timestamp and normalized content, retain its uncertainty, and avoid automatic duplicate stage changes.

## State and recovery

Retain only sufficient private checkpoint state:

| Field | Purpose |
|---|---|
| Source, account alias, lane and query scope | Prevent reusing a cursor against a different mailbox or assignment |
| Cursor or fully covered interval | Establish the verified retrieval boundary |
| Run cutoff, overlap and provider date semantics | Make the next scan reproducible |
| Completed partitions and unfinished token/window | Resume bounded partial work |
| Message/event IDs and processing outcome | Make record updates idempotent |
| Pending ambiguous matches and failed writes | Prevent retrieved messages from being silently forgotten |
| Last successful record reconciliation, run result and recorded time | Distinguish scanned from applied evidence |

Apply a source event once per authoritative target record. On rerun, verify existing provenance before adding history or changing counts. If an event affects both application and outreach records and one write fails, mark each target's result separately and retry only the missing write. Do not claim reconciliation is complete until both required writes are verified.

A retrieval checkpoint may advance past an ambiguous message only after that message's identifier, evidence pointer, candidate matches and unresolved status are durably retained. The same applies to a failed record write. If durable retention fails, retain the prior checkpoint so the source can be retrieved again. Maintain separate retrieval and application-completion state; an empty new-message result does not mean the unresolved queue is empty.

Refresh mutable records and avoid overwriting another writer's changes. Serialize checkpoint writes or use the workspace's lock/atomic-write mechanism. Treat a crash after a record write but before checkpoint commit as a replay: inspect provenance, then finish recording the processing outcome. Retain corrections as later events, not duplicate initial outcomes.

## Reporting limits

State the actual interval, sources checked and remaining gaps. Report blocked authentication, expired cursors, truncation or unavailable full bodies separately from “no new recruiting messages.” Do not create a monitor to repair a gap unless the user requests one. A deeper rescan can be suggested when the overlap cannot establish the needed coverage.
