# Cache Security, Isolation, and Availability

Mandatory when using Redis, Valkey, Memcached, Laravel Cache, Django cache, Spring Cache, Rails cache, Node/Python cache clients, API caching, CDN/reverse-proxy caches, or browser/mobile offline caches. Apply across all programming languages.

## Inventory and classify
- Discover every cache: service, local/in-process, CDN/edge, reverse proxy, browser, application object cache, sessions, rate-limit counters, locks, queues, and OTP/idempotency stores.
- Identify trust boundary, owner, data classification (public/private/secret), tenant/user scope, authoritative source of truth, TTL, eviction, invalidation, and failure mode.
- Flag any cache used as a security authority: cached user roles/entitlements, sessions, revocation status, fraud limits, rate counters, OTP, payment states, distributed locks, or idempotency keys.

## Service hardening
- Never expose Redis/Valkey/Memcached unauthenticated to the public internet; use private networking, firewall rules and TLS when supported/appropriate.
- Enforce named least-privilege credentials/ACLs where supported; protect secrets in runtime secret stores. Avoid sharing unrestricted admin credentials with application workers.
- Review dangerous administrative commands, client isolation, backup permissions, patch versions, and unauthorized key scans.
- Avoid secrets and high-sensitivity records in plaintext cache unless explicitly justified and appropriately protected; enforce retention and deletion policies.
- Bound connection pool size, active commands, client timeouts, maxmemory/memory quota, key cardinality and size, expensive scans, eviction policies, persistence settings and disk use.

## Cache key and cross-tenant isolation
- Namespace keys by app, environment, version, tenant, user/role, locale and other relevant authorization dimensions when required.
- Never derive cache keys only from untrusted IDs if result access depends on user/tenant permissions.
- Do not assume a cached object remains authorized: revalidate permissions at access or use verifiably safe permission-scoped keys and invalidation.
- Defend against key collisions, cache poisoning, cache deception and unbounded user-controlled keys.
- Never share credentials, private API responses, account data or payment/customer data through a public CDN or shared browser cache.
- For HTTP responses, verify Cache-Control private/no-store for authenticated and sensitive endpoints, Vary where needed, CDN bypass rules and authorization/cookie interactions.

## Correctness, expiration, and failure modes
- Assign justified TTLs, explicit invalidation triggers and tests for logout, role changes, password resets, payment/refund transitions, pricing/inventory changes and account deletion.
- Use atomic primitives for counters and TTL assignment; test expiration races. For security-sensitive counters/OTP and anti-replay keys, use appropriate durable/atomic semantics; document consequences if cache evicts or restarts.
- Decide fail-open versus fail-closed per control (especially rate limiting, session validation and security policy); document availability and bypass implications.
- Use jittered TTLs, bounded stampede protection (single-flight/locking), stale-if-error only for safe data, circuit breakers and monitored cache fallback.
- Avoid treating cache as the sole durable ledger for money, payment fulfillment, refunds or identity recovery. Use transactional persistent storage and robust idempotency controls.
- Distributed locks must have owner tokens/expiry and safe release. Do not assume a cache lock alone makes financial state changes atomic.

## Multi-node and deployment
- Check consistency across instances, eviction/restart effects, failover, Redis replication/cluster assumptions, rolling deployments, region boundaries and versioned key changes.
- Never use local-only rate counters or cache sessions when consistent multi-instance enforcement is required, unless explicitly designed otherwise.
- Separate cache pools for security-critical controls and general content where contention/eviction can compromise enforcement.
- Measure hit/miss ratio, latency, timeouts, evictions, RSS, connections, key count, replication lag, queue delay, error rates, and 429/503 during faults.

## Tests (only in authorized development or staging)
- Cross-user/tenant cache leakage; logout/role-change invalidation; stale auth responses; cached private page at CDN; cache key poisoning.
- Concurrent counters, OTP replay, token revocation, anti-replay TTL, cache full/evicted/restarted, connection starvation and network partition.
- Stampede under expiry, fallback correctness, stale data impact on checkout/pricing, and multi-node rate limit bypass.
- Record PASS/FAIL/NOT RUN, environment, control owner, tested TTLs/limits, and residual risk. Never run disruptive load tests against production without explicit authorization.

## Framework touchpoints
- Laravel: cache stores, tags, sessions, queues, Redis rate limiting, middleware, tenant scoping; do not assume drivers guarantee distributed locks equally.
- Node/React: server Redis/cache clients, edge fetch caching, Next.js or other framework render/data caches, auth cookie responses and CDN.
- Python: Django per-site/per-view caching, Flask-Caching, FastAPI service caches, Celery broker/results; check thread/async-safe clients and connection pools.
- Java: Spring Cache, Redis/Hazelcast/Caffeine, annotations, principal-specific cache keys and session invalidation.
- Go: redis/memcache clients, context deadlines, pools, race-safe in-process maps and bounded local caches.
- Ruby: Rails.cache, Redis/session store, Sidekiq and cache key scoping.
- React Native/Flutter: secure local persistence, account-switch/logout cache clearing, offline PII data, app backups and encryption.
