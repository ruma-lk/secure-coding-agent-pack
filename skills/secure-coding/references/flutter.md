# Flutter Security Guide

Apply universal.md. Covers Flutter/Dart Android, iOS, web and desktop clients.

## Mandatory review
- Treat Dart code and compiled binaries as inspectable; never ship privileged service secrets, static credentials or signing keys.
- Enforce API authorization, tenant and object ownership server-side. Screen guards are UX only.
- Use platform-secure storage for sensitive tokens, not SharedPreferences or unencrypted app files; review backups and keychain/keystore behavior.
- Use TLS and default certificate validation; never accept all certificates in HttpOverrides.badCertificateCallback or equivalent. Pinning requires planned rotation/failure handling if used.
- Validate deep links, app links, navigation arguments and URI schemes; restrict external URL launches and redirects.
- Limit embedded WebViews, JavaScript channels and origins; constrain untrusted HTML/content and file access.
- Review Android manifest exported components/permissions, iOS entitlements/privacy declarations and release signing.
- Avoid sensitive logging, debug banners/config, analytics payloads, screenshots, clipboard leaks and verbose crash reports.
- Review isolates/background services for auth state, safe serialization, local database encryption and sensitive caches.
- Verify pubspec.lock, pub.dev dependencies, native plugins and CI signing/OTA-delivery security.
## Tests and tooling
Run flutter analyze, flutter test, dart pub outdated for review (does not establish safety) and platform integration/security tests. Audit plugins and native code; report checks NOT RUN where absent.
