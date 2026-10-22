# Python Security Guide

Apply universal.md first. Covers Django, Flask, FastAPI, scripts, workers, and Python services.

## Mandatory review
- Identify framework, ASGI/WSGI boundary, authentication, role/tenant scope, exposed routers, background workers and serialization formats.
- Enforce authorization on every handler, query and object, not only router decorators. Test cross-tenant IDOR and privilege escalation.
- Validate request data using maintained framework/schema validation; constrain types, size, nesting and file sizes. Avoid unsafe pickle, yaml.load without SafeLoader, marshal and untrusted deserialization.
- Use ORM parameter binding or prepared statements; avoid string-interpolated SQL, shell=True, dynamic eval/exec and untrusted template strings.
- Prevent SSRF: validate outbound targets and DNS resolution, restrict private/link-local/metadata addresses and egress; review redirects.
- Secure Django CSRF/session/ALLOWED_HOSTS/SECURE_* settings; for FastAPI/Flask cookie-based sessions add CSRF controls, explicit CORS origins and secure cookies.
- For uploads, inspect content, limit size, separate storage and verify retrieval authorization.
- Do not expose stack traces or credentials; configure logging redaction and secret injection at runtime. Avoid debug=True in production.
- Lock dependencies, audit packages and review build hooks; isolate virtualenv and least-privilege worker credentials.
- Protect async jobs, webhooks and queues against replay, race conditions and duplicate execution.
## Tests and tooling
Use project test runner (pytest/unittest), dependency scanner (pip-audit or appropriate tool), Semgrep, and Gitleaks if installed. Test authn/authz negative paths. State NOT RUN when unavailable; never install scanners without approval.

## Required Python concurrency audit
Always consult `python-concurrency.md` and `concurrency-and-resource-safety.md` when Python uses threading, concurrent.futures, asyncio, Gunicorn/Uvicorn, Celery or multiprocessing. Explicitly review executor max_workers, bounded submission queues, process/worker counts, cancellation, timeouts, deadlocks and DB connection pressure.
