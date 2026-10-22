# Task-Driven Security Execution

This workflow is mandatory for multi-file changes, full audits, and requests to fix multiple findings. For small single-file fixes, a compact in-memory checklist may be sufficient.

## Plan before changes
1. Inspect the repository and identify scope, user intent, baseline tests, risks, dependencies and platform constraints.
2. Produce a prioritized checklist with stable IDs, file scope, risk/severity, dependencies, acceptance criteria, validation commands, and estimated change impact. Show a short plan to the user.
3. Store the project-local plan as `.security-tasks.md` **only when project write access and user intent permit**. Do not commit this file or leak sensitive findings without approval. Reuse an existing tracker where the team already uses one.
4. Mark tasks TODO / IN_PROGRESS / PASS / FAIL / BLOCKED / NOT_RUN. Only one implementation task should be IN_PROGRESS at a time unless truly independent tasks justify parallelism.

## Execute and verify
1. Choose highest-priority actionable task considering dependencies. Avoid rewriting unrelated code.
2. Record the baseline and use minimal changes; never disable security protections/tests to force a pass.
3. Run relevant unit, integration, regression, authorization and security tests. For payment, OTP, caching, and concurrency flows, include negative and duplicate/race tests where possible.
4. Mark PASS only when acceptance criteria are actually met and required verification succeeded. Mark NOT_RUN when verification cannot run, FAIL on unmet criteria, BLOCKED for missing prerequisites/approval.
5. Record evidence including commands and concise outcomes (not secrets), touched files, unverified risks and next step.
6. Move on to next task while safe and authorized. Pause for required approvals, ambiguous destructive operations, production deployment, secrets/credentials, or unresolved high-impact risk.

## Resume sessions
Before beginning, read the existing tracker or plan (if present); check repository status and recent changes, reconcile stale status, and continue from the first actionable incomplete task. Do not assume previous agent claims constitute evidence. Avoid duplicate fixes and preserve work from other contributors.

## Reporting
Provide:
- Task summary: total, PASS, FAIL, BLOCKED, NOT_RUN, TODO.
- Current task, changes, verification evidence, blockers, and next actionable task.
- A release readiness conclusion based on actual evidence, not a fabricated percentage.

## Safety
- Never perform unattended production changes, destructive operations or external side effects without required authorization.
- Do not create infinite retry loops. Stop after bounded attempts when tests keep failing; report blockers.
- Do not silently modify user-defined plans or skip tasks. Changes in priority/scope should be explained.
- An agent only works while it has an active execution environment. A task file enables later resumption but does not create a background worker.
