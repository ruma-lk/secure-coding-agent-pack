# Dialog eSMS and SMS gateway security

Apply across all stacks and mobile apps. This document provides secure integration controls, NOT an assertion of specific Dialog eSMS API parameters. Obtain currently valid official Dialog account-specific SMS API documentation, sender IDs, auth method, balance/delivery/status APIs and quota terms before implementing.

## Server-side gateway integration
- Only backend workers may hold Dialog eSMS credentials/tokens. Do not ship credentials in React/React Native/Flutter, HTML, Git, logs, crash traces or CI artifacts.
- Authenticate exactly as specified by the contracted Dialog eSMS API version. Do not invent OTP endpoints, token refresh flows, encryption or delivery report signatures.
- Protect config with managed secrets, least privilege, rotation, environment separation and egress TLS verification. Limit admin ability to change recipient, template, sender ID or credits.
- Enforce permitted sender ID, phone validation (Sri Lankan +94 normalization as applicable), content encoding (GSM-7 vs Unicode), length/segment cost and recipient policy. Prevent user-supplied arbitrary templates, impersonation, links and injection into message content.
- Apply per-account, phone, user, IP and tenant sending limits, daily spend/credit budgets, bulk campaign caps and per-template abuse limits; mask numbers in logs.
- Queue sends with bounded backlog, worker concurrency and API timeouts. Use jittered bounded retry only for transient errors, respect provider limits/Retry-After if documented, and avoid resending uncertain accepted messages blindly.
- Persist send intent, provider message/reference ID, masked destination, correlation ID, enqueue/send/delivery status, attempt count and cost, without OTP or sensitive body. Distinguish accepted/submitted from delivered; handle provider delivery receipts according to official docs.
- Webhooks/delivery receipts, if supported, must have verified authenticity, deduplication and tenant isolation; otherwise poll trusted provider status when available.
- Implement opt-out and consent rules for marketing texts, suppression list, legal retention/deletion and approval of bulk campaigns; transactional OTP is a different category from marketing SMS.
- Monitor balance depletion, delivery failures, throttling, recipient anomalies, fraud, worker saturation, duplicate sends, unexpected volumes and costs.

## OTP and identity verification
- Generate OTP with a cryptographically secure random generator, short TTL, single-use server-side verification and limited attempts; hash/protect server-held verifier.
- Limit OTP requests and verification separately by phone, account, IP/device and risk context. Apply resend cooldown and expiry; do not confirm whether an account/phone is registered.
- On success mark consumed atomically to prevent concurrent re-use. Protect account recovery, phone changes and step-up authentication against SIM swap risks.
- SMS is not phishing-resistant MFA; prefer stronger methods for high-risk changes and never treat a successful SMS API response as proof of user possession.

## Required tests
Invalid tokens, unapproved sender ID, malformed phone, Unicode segmentation/cost, absent consent, opt-out, abuse bursts, exhausted budget, insufficient balance, API 429/5xx, timeout after accepted send, duplicate queue delivery, concurrent OTP verification, expired/guessed OTP, log disclosure and delayed or forged delivery reports.

## Evidence
Record official version, authentication, sender IDs, documented limits, retry behaviors, endpoint URLs, credential ownership, OTP policy, queue bounds, privacy/consent requirements, tests and NOT RUN unknowns.
