# Context-Efficient Security Execution (mandatory for multi-task work)

Goal: lower **peak context** without dropping security coverage. Splitting tasks in the same session does not clear history; isolated subagents/new sessions are optional, never presumed available. Preserve security invariants and verifiable state across boundaries.

## Graph-first option
Follow `graphify-navigation.md` for broad exploration when the tool is available and the project allows local indexing. Query scoped graph relationships to reduce searches; independently verify relevant source paths. If Graphify is missing, request permission before installing it, and continue with ordinary code navigation if not approved or installation fails. Graphify is not a prerequisite to safe task execution.

## A. Scan once, map risks, then plan
1. Read `SKILL.md` and `universal.md`, inspect project structure and security-sensitive entry points without reading secrets. Identify stack, tenants, auth boundaries, financial/SMS flows, caches, exposed endpoints and external services.
2. Create stable task IDs, dependencies, severity, relevant files, risk/attack scenario, acceptance criteria, required negative tests, and exact required reference names. **Preserve all findings** in a task tracker; don't drop or de-scope findings to meet a context budget.
3. Before modifying code, record baseline revision, test outcome and existing worktree changes. Use existing project tracker or a locally stored `.security-work/` folder when permitted. Do not overwrite user files or commit sensitive findings without approval.
4. Keep `.security-work/PROJECT_STATE.md` compact (architecture, trust boundaries, invariants, decisions, last verified revision, next task). Keep detailed task evidence in `.security-work/TASKS.json` with the schema from `templates/TASKS.example.json`. Use minimal summary, not truncated evidence.

## B. Single-task execution, selective loading
1. Read state and task index, select one dependency-ready task. Verify current git diff/status and whether prior evidence still applies.
2. Load core safety rules **every task**: SKILL.md and universal.md. Load only the task's language references **plus all mandatory applicable specialist references** (payments, eSMS, caches, rate limits, concurrency, Python thread/async, etc.). Do not skip specialist checks for token savings.
3. Read only affected code, its callers/callees, security boundaries and tests; widen scope when evidence requires it.
4. Implement minimal change. Run the task's positive, negative and regression tests. Recheck authorization and trust boundaries on related call paths.
5. Record files, commit/diff revision, commands, PASS/FAIL/NOT_RUN, evidence references, residual risks and impact on other tasks. A fix is only PASS when its acceptance criteria and required validation pass. `NOT_RUN` and `BLOCKED` remain outstanding.
6. Execute the next task in the active agent session while safely possible. If a subagent with a genuinely isolated context is supported, give it only task ID, relevant scoped files, required guides, acceptance criteria and baseline revision. The coordinator still must verify outcomes.
7. For a new session, reload stored state, validate the actual repository revision against evidence, and resume. Never treat stale tracker status as truth.

## C. Hard security gates: never optimize away
- Authn/authz, BOLA/IDOR, tenant isolation, input/output encoding, secret handling, error/log leakage and dependency integrity.
- Payments: exact merchant/order/amount/currency, authoritative provider verification, replay/idempotency, refund authorization and reconciliation.
- eSMS/OTP: sender identity, rates, TTL, one-time atomic consumption, bounded queue, delivery/cost controls and abuse.
- Rate limiting, thread/process/async/queue bounds, timeouts, cancellation, retries, safe cache isolation/TTL and fail-open/closed decisions.
- For any changed security boundary, include an abuse/negative test, or explicitly mark NOT_RUN with impact. Do not silently weaken protections.
- Never release with unresolved critical/high findings without the authorized owner's explicit documented risk acceptance and relevant organization release policies.

## D. Context and quality controls
- Keep agent-facing handoff summary brief (target ~500–1200 tokens, **guideline**, not a hard truncation). Point to task evidence/files rather than paste entire logs. Store commands and outputs in project-local records when authorized, with secrets removed.
- Do NOT aggressively summarize provider specifications, financial state machines, incident evidence or security decisions. Retain links/source versions and full tests separately.
- When nearing the context limit, stop at a safe checkpoint, persist current task and state, then request/perform a fresh agent session **only if the environment supports it**. Do not claim automatic context reset or background continuation without actual support.
- Track optional per-task token estimates and observed values if the agent exposes them. Do not fabricate token counts or security scores.

## E. Handoff report
Show: current task ID and status, validation evidence, risks/blockers, previous revision, next task, mandatory reference coverage, and any tests NOT_RUN. If evidence missing, status stays unresolved.
