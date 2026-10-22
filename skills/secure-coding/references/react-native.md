# React Native Security Guide

Apply universal.md and react.md. Covers Android and iOS applications built with React Native and Expo.

## Mandatory review
- Treat mobile app binaries and JS bundles as publicly inspectable; never embed API keys with privileged access, signing credentials, hardcoded secrets or sensitive environment data.
- Validate identity and all object permissions on backend; client navigation/hidden screens do not provide authorization.
- Store refresh/access tokens using platform-backed secure credential storage where warranted, not AsyncStorage or plain files for secrets. Avoid storing unnecessary PII.
- Implement token expiry, refresh rotation and secure logout/revocation; guard against account switching leaks.
- Use TLS and platform network security config; never disable certificate verification. Carefully assess pinning and rotation if threat model calls for it.
- Review deep links, custom schemes and universal/app links; validate all inbound route parameters and prevent redirect/intent abuse.
- Limit WebView JavaScript bridges, injected scripts and allowed origins; do not load untrusted HTML with elevated privileges.
- Restrict Android exported components/intents and iOS entitlements/URL handlers; review permissions and privacy disclosures.
- Avoid logs, crash reporting, notifications, screenshots and analytics exposing sensitive data. Review clipboard and background tasks.
- Review native modules, OTA update configuration, dependencies and signed release artifacts; protect signing keys and CI secrets.
## Tests and tooling
Use jest/unit tests, mobile integration tests and platform-specific checks. Audit npm/yarn/pnpm dependency locks and native packages; review Android manifest and iOS entitlements. Static-only reviews are not a substitute for device/backend testing.
