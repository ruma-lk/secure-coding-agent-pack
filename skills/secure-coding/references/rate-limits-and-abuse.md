# Rate limiting and abuse prevention

Treat rate limiting as a security AND availability requirement; limits must match tested workload and business rules, not copied arbitrary constants.

## Inventory / policy
- Inventory routes, methods, GraphQL fields, WebSocket messages, background job triggers, expensive queries, searches, exports, email/SMS/OTP, login, reset, registration, checkout, payment, uploads and AI endpoints.
- Define per-route **request rate**, **burst**, **in-flight concurrency**, **work units**, and **daily/cost budgets** as applicable. Record the responsible owner, configured values, reasons and environment.
- Separate actors: unauthenticated IP/network and authenticated user/account/API key/tenant; ensure admin/service bypasses are intentional and audited. Do not trust forwarded IP headers unless from a trusted proxy.
- Implement enforcement at edge/gateway AND within application for sensitive flows; multiple instances need coordinated/atomic counters (e.g. trusted Redis) with documented fail-open/fail-closed strategy.
- Apply per-user/tenant quota to expensive operations; bound pagination, query complexity, batch size, request body, upload decompression and third-party spending. Avoid globally shared limit that lets one tenant starve others.
- For errors: use 429 where suitable, provide bounded Retry-After where practical, generic messages for sensitive auth flows, and log limit decisions without secrets/PII leakage.
- Test distributed bypass, race conditions, burst behavior, fixed-window boundary, retries, token rotation, proxy configuration and multi-region consistency.

## Resilience
- Include bounded waiting queues, timeouts, cancellation, backpressure, circuit breakers, bulkheads, retries with jitter and maximum attempts; avoid retry storms.
- Set both server and client timeouts, appropriate 503 behavior for overload, graceful shutdown and worker admission control.
- Metrics: rejected/allowed requests, queue depth, in-flight requests, per-route p95/p99 latency, CPU/memory, database pool pressure, downstream failures, 429/503 counts and third-party cost.
- Never stress-test production or third-party endpoints without explicit authorization, limits and rollback. Prefer deterministic unit tests and staging load tests.

## Agent evidence
Provide an endpoint matrix with key, burst, concurrency, budget, location of enforcement, tests and gaps. NEVER mark PASS by merely finding middleware installed.
