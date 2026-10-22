# Java Security Guide

Apply universal.md first. Covers Spring Boot, Jakarta EE, servlets and Java services.

## Mandatory review
- Discover framework, Spring Security filters, authorization annotations, controller routes, service-layer checks, IAM/tenant model and serializers.
- Require server-side method/object authorization; scope database lookups by owner/tenant; guard against insecure direct object references.
- Validate inputs with Bean Validation and domain constraints. Use parameterized queries/JPA parameters; never concatenate raw SQL or LDAP filters.
- Prevent unsafe Java native deserialization and type-polymorphic JSON deserialization; do not accept untrusted object graphs or unrestricted Jackson default typing.
- Review XML parsing for XXE/external entity expansion; configure secure parsers.
- Protect file operations against path traversal; constrain uploads, URLs, redirects and SSRF.
- Configure Spring Security correctly: CSRF for browser cookie auth, restricted CORS, session fixation protection, secure cookies, password hashing, role hierarchy and authorization matchers.
- Minimize Actuator exposure; no production debug traces, dev consoles or secrets in properties/config.
- Review logging and exception handlers for sensitive data; enforce TLS, timeouts, quotas and per-endpoint abuse protection.
- Audit Maven/Gradle dependencies and plugins; pin versions and review supply-chain build tasks.
## Tests and tooling
Run Maven/Gradle tests, authorization integration tests and dependency scanning (e.g. OWASP Dependency-Check/OSV Scanner when installed). Review security filter chain with negative permission tests. Mark NOT RUN where unverified.
