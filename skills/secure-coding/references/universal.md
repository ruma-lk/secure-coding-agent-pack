# Universal Security Requirements
Use a risk-based threat model for every feature. Trace entry points through authorization, validation, storage, output and logging.
## Identity and access
Deny by default. Validate identity server-side. Enforce authorization at each protected action and object; test cross-user, cross-role and cross-tenant access. Require secure sessions, rotation, expiry, logout, recovery and rate limiting. Passwords require slow salted password hashing using trusted libraries. MFA for privileged/high-risk operations.
## Input and output
Use allowlist validation and size/type limits, server-side business rules, canonicalized paths, contextual output encoding and safe templating. Parameterize SQL and avoid shell interpolation. Prevent XSS, CSRF where cookies authenticate, SSRF via constrained destination and egress, path traversal, open redirects and injection into templates or logs.
## Data and cryptography
Never commit credentials. Use managed secrets and minimal permissions. Prefer TLS, secure cookie flags, safe logging, encryption at rest where warranted, tested backups and audited key lifecycle. Do not expose sensitive data in errors, URLs, analytics or logs.
## APIs, resources and files
Implement pagination, rate limiting, timeouts, quotas and body limits. Verify uploads by actual content and enforce size, extension, isolated storage and download authorization. Secure async jobs and webhooks with signatures and replay protection.
## Dependencies and deployment
Pin dependencies, review lockfiles, audit transitive packages and build scripts. Limit CI permissions and use protected branches, reviewed changes and artifact provenance. Disable debug in production; review reverse-proxy, CORS, headers, cloud IAM, containers, databases and network exposure.
## Tests
Include negative tests for unauthenticated, forbidden and cross-object requests; fuzz edge-case inputs when feasible. Treat scan results as partial coverage. Document blockers, unrun checks and residual risk before shipping.
