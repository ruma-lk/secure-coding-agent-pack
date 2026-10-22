# Concurrency, resource and lifecycle security

Apply to every language and framework, not only Python.

## Bounded workloads
- Review thread/process/async task count, thread pools, executor sizing, OS processes/file descriptors, connection pools, queue depth, memory/CPU and disk quota, container limits and autoscaling.
- No unbounded thread creation, fan-out, task spawning, child processes, job submissions or event-loop blocking. Explicitly define upper bounds on tasks in-flight AND queued; a thread pool max_workers limit alone does NOT bound submissions.
- Enforce per-tenant fairness, deadlines, timeouts and cancellation from request boundary through DB/network calls. Avoid blocking waits under locks or in async event loops.
- Review deadlocks (nested futures, locks), races, state mutation, lost updates and shared resource ownership; use locks, transactions and idempotency keys where appropriate.
- Bound connection pool and DB concurrency; prevent N+1, large joins, uncontrolled recursion/regex complexity and batch/stream memory growth.
- Ensure threads/processes/tasks terminate on errors and shutdown; release locks, sessions, file handles, sockets and temporary files. Handle worker crashes and poison jobs; bounded retry/backoff and dead-letter handling.
- Review retry/backpressure and circuit breakers; test overload without turning partial outages into full outages.
- Protect cache eviction and resource exhaustion; review TTLs, cardinality, cache stampedes and key collision/tenant isolation.
- Monitor worker count, active tasks, queue wait/depth, leaked handles, heap/RSS, event loop lag, saturation, blocked threads, deadlocks and p95/p99 latency.
- Verify behavior under retries, duplicate messages, partial failures, database outages, cancellation, timeouts and graceful deploy restarts.

## Release evidence
Document code locations for every bound, configuration by environment, load-test results if authorized, and NOT RUN where not verified.
