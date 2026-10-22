# Sri Lanka provider-specific payment security

Read payment-security.md first. Provider implementations differ. These notes are REVIEW CHECKLISTS, not a replacement for current provider-specific MID/API documentation.

## Sampath Bank IPG (including MPGS-based integrations where contracted)
- Check whether integration actually uses Mastercard Payment Gateway Services (MPGS), bank-supplied hosted session/checkout or another flow; do not assume all Sampath accounts use the same version.
- If MPGS-based, review merchant-specific gateway host and API version, session/token ownership, 3DS2 challenge and result, authorize vs capture, Retrieve Order/Transaction, reversal/void/refund and failure states.
- Confirm card-on-file/tokenization and merchant-initiated transaction permission from the bank; consent, initial customer-initiated transaction linkage and appropriate payment network requirements.
- Never treat an ACS/browser redirect as financial success. Verify actual order/transaction status server-side. Apply provider-supported webhook verification only where specified.

## Seylan Bank IPG / Mastercard MPGS
- Obtain the merchant's signed-off MPGS integration settings, merchant ID, gateway URL, API version, key/certificate mode and allowed operation set.
- Review Hosted Checkout/Hosted Session choices, tokenization, 3DS, transaction retrieval, authorize/capture/void/refund and server-side status verification. MPGS 'Retrieve Order' retrieves order and associated transactions; never assume a gateway-specific return status without documented semantics.
- Enforce merchant/order/amount/currency checks, exact terminal transaction state and replay-safe fulfillment. Review capture versus authorization and settlement versus payment.
- Lock down admin refund permissions, payment tokens, reconciliation, chargeback workflow, merchant egress and PCI responsibilities.
- 'Mastercard' is a card network/gateway technology, not evidence that any unrelated bank MID shares authentication details.

## OnePay
Official: https://docs.onepay.lk/api-documentation and https://docs.onepay.lk/api-documentation/payment-api
- OnePay's documented redirect flow creates checkout via /v3/checkout/link/, then redirects and verifies transaction with /v3/transaction/status/. Check exact version and merchant-specific credentials before implementation.
- Current public docs describe App ID + Hash Salt and SHA-256 request hashing for applicable API flows. Do not invent signing field concatenation, apply it indiscriminately to other OnePay products, or confuse app token authorization with request hashing.
- Do not grant entitlement on transaction_redirect_url alone. Check the server-side status lookup, merchant/order, amount, currency and final paid semantics.
- For OnePayJS/card-on-file/payment links, use the *specific* current product documentation and check token consent, replay protection, server-side charges, credential scope, refund and webhooks as applicable.

## PayHere
Official: https://support.payhere.lk/api-%26-mobile-sdk/checkout-api.I
- Checkout redirects to PayHere; status arrives at the server-side notify_url. The browser return_url is not reliable evidence of payment.
- Verify notification using PayHere's documented md5sig formula, fields, casing and merchant-secret for the **approved domain/app**. Match local merchant_id, order_id, exact amount, currency, and documented success status. Compare checksum safely.
- The protocol uses MD5-derived signature as published by PayHere: **do not silently replace it with a made-up HMAC-SHA256 header**. Follow PayHere specifications, secure merchant secret, and independently verify status when available and appropriate.
- Handle duplicate notifications, pending/failed statuses, missing public notify_url, tokenization/recurring consent, refund authorization and reconciliation.
- Store the domain/app-specific merchant secret only server-side; never expose in web/mobile builds.

## Provider-specific release gate
For each gateway, obtain CURRENT official specs from its portal/bank, test sandbox cases, record differences between docs and MID configuration and obtain approval for unknown flows. Do not assume the bank supports every MPGS feature. No fabricated callback signature, encryption algorithm, endpoint or success code.

Public sources checked: Mastercard Retrieve Order documentation; docs.onepay.lk Payment API and Integration Guide; PayHere Checkout API.
