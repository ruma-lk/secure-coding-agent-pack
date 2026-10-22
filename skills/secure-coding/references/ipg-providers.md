# Payment gateway provider security: Master IPG, Bancstac IPG, OnePay, PayHere

First read `payment-security.md`. All guidance is framework- and OS-independent. These are security review checklists, not integration contracts. Use the provider's current official documentation and exact merchant configuration. Do not infer that gateways share APIs, callback schemes, tokens, or status codes.

## Master IPG
- Identify the precise hosted checkout, hosted session, direct API, or other configured product and its official documentation.
- Verify merchant identifiers, server-only authentication credentials, gateway host, API version, permitted operations, and environmental separation.
- Review session ownership, checkout initiation, applicable 3-D Secure flow, authorization versus capture, reversal, void, refund, tokenization and recurring consent only if supported by the contracted integration.
- Never fulfill an order based solely on the browser return URL, challenge result, or client-side message. Retrieve and confirm an authoritative transaction/order state server-side.
- Validate local order ownership, expected amount and currency, order-to-transaction association, status semantics, idempotent fulfillment and reconciliation.
- Independently inspect notification authentication and replay controls using documented mechanisms, never a guessed signature scheme.

## Bancstac IPG
- Obtain Bancstac's current official integration documentation for the contracted product, supported payment methods, endpoint host, sandbox/production credentials and callback/authentication mechanisms.
- Determine whether the integration is hosted, redirected, embedded, API-driven or another documented variant; never assume it behaves like Master IPG or another provider.
- Check how transaction status is verified authoritatively, and verify merchant identity, order reference, amount, currency, final status and replay/duplicate prevention.
- Check idempotency for payment initialization, processing, fulfillment, retries and refunds; enforce least-privilege refund access and reconciliation.
- Ensure signing/verification, redirects, tokenization, storage and supported operations match the actual documented merchant configuration. Mark undocumented elements NOT VERIFIED.

## OnePay
Official documentation: https://docs.onepay.lk/api-documentation
- Determine the exact API/product and version. For integrations using the documented payment-link flow, verify status server-side instead of treating the redirect as payment confirmation.
- Follow the applicable documented request authentication and hashing rules precisely; do not invent a universal algorithm or field order.
- Validate merchant, order, amount, currency, payment state, duplicate notifications, refund permissions, token consent and rate limits where applicable.

## PayHere
Official documentation: https://support.payhere.lk/api-%26-mobile-sdk/checkout-api.I
- Browser return_url is not authoritative payment proof. Validate the server-side notify_url message using the provider's documented `md5sig` calculation and merchant secret.
- Compare merchant_id, order_id, amount, currency and documented success state to the server-side order record using appropriate fixed-precision money representation.
- Avoid replacing provider-defined MD5-based message verification with a fabricated signing scheme. Protect the secret, use constant-time comparison where appropriate, and reconcile authoritative transaction status where available.
- Handle duplicate/delayed notifications, token or recurring-payment consent, refunds, environment separation and reconciliation.

## Required release evidence — all four providers
- Official specification and version or the relevant merchant-provided document.
- Payment state diagram and terminal-state semantics.
- Tests for forged/replayed callbacks, wrong amount/currency/order, duplicate success, failed/pending, concurrent success/refund and network timeouts.
- Production credentials remain server-side; do not expose payment tokens or secrets to browser/mobile apps.
- Explicit PASS / FAIL / NOT RUN / NOT VERIFIED for each check. Do not claim a provider-specific verification passed merely because code contains generic validation.
