# Go Security Guide

Apply universal.md first. Covers net/http, Gin, Echo, Fiber, gRPC and services.

## Mandatory review
- Map HTTP/gRPC middleware order, auth identity propagation, per-resource permissions and tenant isolation.
- Validate input sizes/types/encodings using strict schemas and bounded readers; reject oversized JSON/multipart bodies.
- Use database/sql placeholders or safe ORM bindings, never string-build untrusted query structures.
- Handle untrusted paths with safe joining/containment checks; reject traversal and symlink escapes.
- Prevent SSRF with allowlisted outbound hosts, validated resolutions and constrained redirects/network egress.
- Set explicit HTTP server read/write/idle timeouts and graceful shutdown; constrain client timeouts and redirects.
- Enforce TLS and secure cookies for browser sessions; protect cookie-authenticated mutations against CSRF and restrict CORS.
- Avoid leaking secrets in logs, errors or panic traces. Use context cancellation, resource limits and request rate limits.
- Review subprocess use (os/exec arguments, no shell interpolation), archive extraction and unsafe/reflect usage.
- Use crypto/rand and maintained crypto libraries; do not implement custom authentication crypto.
- Lock go.mod/go.sum, examine module provenance and run go vet and govulncheck when available.
## Tests and tooling
Run go test ./..., go vet ./..., govulncheck ./... if installed, and negative cross-role/tenant API tests. Report gaps explicitly.
