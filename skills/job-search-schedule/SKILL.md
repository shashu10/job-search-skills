---
name: job-search-schedule
description: Create, update or remove explicitly requested job-search reminders and recurring runs using the host's scheduler. Use for scheduled research, inbox checks and bounded authorized actions; installing skills does not schedule work.
---

# Job search schedule

Configure a requested recurrence with a clear action boundary, reliable recovery and useful notifications. This skill supplies instructions, not a scheduler, mailbox connector or background service.

## Establish the requested run

Read the selected private workspace's `AGENTS.md`, `roles/INDEX.md`, mapped preferences and relevant authorization records. Defaults are `roles/applications.md` for applications and `outreach/contacts.md` for messaging. Keep schedule state in the private `schedules/automations.md`; existing mappings take precedence. Do not use the installed skill directory for candidate data. If there is no workspace, use supplied records or `job-search-setup` when available.

Schedule only when the user requests a reminder, recurring run or monitor. Installing the package, preparing a plan and seeing unfinished work do not authorize background work. Reuse a valid request without asking for approval again. Recurring research authorizes research, not applications or outreach; application and sending grants must explicitly cover the recurring actions, lane and limits.

Resolve purpose, scope, frequency, start/end conditions, timezone, daily/run ceilings and notification intent from the request and records. Ask only about consequential missing choices. Use an explicit IANA timezone for wall-clock recurrences and verify daylight-saving behavior, including skipped or repeated times when relevant. A fixed UTC cadence differs from “each morning”; do not infer timezone from the machine or candidate's residence.

## Inspect the host and existing schedules

Discover the host's current scheduler tools and inspect their capabilities and instructions. Verify persistent execution, workspace access, required credentials/permissions, notification support and whether runs require the application, host or network to remain available. Use supported scheduler operations rather than inventing a daemon or installation hook.

Inspect existing jobs in the same workspace and scope before creating anything. Prefer updating the matching job, preserving unrelated settings. Read [run and recovery contract](references/run-contract.md) when composing a recurring prompt or changing an external-action schedule.

If scheduling is unavailable, provide a ready-to-use prompt, recurrence and prerequisites, and state that no new job was configured; existing jobs may remain unverified. Missing access or unknown running requirements are capability gaps; do not promise execution or notifications. Do not silently substitute an unsupported cron job, another service or a new account.

## Configure and verify

Save the user request's provenance and precise recurring grant privately. Include allowed actions, exclusions, owner/lane, limits, expiration and revocation rules. The scheduler prompt must reload current grants, holds and records on each run; a saved prompt cannot override later pauses. Refer to mapped private facts and approved materials rather than embedding a resume, credentials or mailbox export in the prompt.

Use the host's supported create/update operation, then verify returned identity, status, recurrence, timezone and next run where available. For an unknown outcome, inspect by stable identity before retrying; never create a second job merely because the first response was lost. Persist the job ID and verified configuration privately. If local recording fails after creation, report the existing job and repair its record without recreating it.

Deliver the confirmed schedule, action limits, relevant running requirements and notification behavior. Distinguish configured, pending verification, paused, failed and completed. For changes or cancellation, verify actual host state before reporting success. If a tool fails or no receipt is available, describe that gap. Scheduled runs can use optional sibling skills when installed; their absence does not expand authority or justify claiming an action ran.
