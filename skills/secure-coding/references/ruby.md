# Ruby Security Guide

Apply universal.md first. Covers Rails, Sinatra, Rack and Ruby background jobs.

## Mandatory review
- Identify auth filters, routes, ActiveRecord scopes, tenant ownership and privileged/admin actions.
- Enforce model/object authorization (policy/guard) on each request and background job; test cross-user and cross-tenant IDOR.
- Use strong parameters but remember permitted attributes do not enforce authorization or safe business logic.
- Use ActiveRecord bind parameters; avoid SQL fragments from untrusted params, unsafe constantize, send/public_send, eval and shell interpolation.
- Avoid unsafe YAML.load, Marshal.load and deserializing untrusted Ruby objects; use safe parsing.
- Protect Rails forms with CSRF tokens for cookie-authenticated requests; restrict CORS and use secure session cookie settings.
- Prevent XSS: preserve autoescaping, review html_safe/raw, helpers, rich text and URL schemes.
- Secure Active Storage/uploads with file-type/size/content validation, private access and authorized download links.
- Review redirects, outbound URLs, SSRF, path traversal, archive extraction and webhook signature/replay protection.
- Keep credentials encrypted/managed; avoid logging parameters with secrets; enforce production error handling and safe Rails configuration.
- Audit Gemfile.lock (bundler-audit or compatible scanner), review Rails security updates, and isolate CI/deployment permissions.
## Tests and tooling
Run relevant RSpec/Minitest, Brakeman for Rails, bundler-audit if installed, and explicit unauthorized/CSRF/tenant isolation tests. Missing checks are NOT RUN.
