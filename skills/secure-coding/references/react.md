# React Security
- React escapes normal JSX text, but do not assume arbitrary HTML/URLs or third-party rendering libraries are safe.
- Avoid dangerouslySetInnerHTML; if essential, sanitize with a maintained sanitizer and review policy.
- Keep authorization on the server; hidden UI controls and protected routes are not security boundaries.
- Avoid placing secrets in public env variables, bundles, browser logs, localStorage or client source.
- Review cookie-based authentication CSRF defenses, SameSite, Secure, HttpOnly and session expiry.
- Restrict external scripts, iframe origins and links; use rel=noopener noreferrer when needed.
- Validate file types and sizes on the server; client validation is UX only.
- Review redirects, user-controlled links and any postMessage origin checking.
- Test cross-role data exposure, stale caches and frontend error handling.
