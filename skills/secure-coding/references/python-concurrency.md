# Python thread, process and async safety — special review

Use with python.md and concurrency-and-resource-safety.md.

## Thread limit controls
- Locate threading.Thread, ThreadPoolExecutor, asyncio.to_thread, loop.run_in_executor, third-party schedulers, Celery, Gunicorn, Uvicorn and process pools.
- Ensure ThreadPoolExecutor(max_workers=...) is explicitly sized for the workload, deployment memory, CPU and underlying connections. Python defaults vary by version; do not assume a universal number.
- max_workers limits active threads **but not queued submissions**. Enforce bounded admission with a semaphore, bounded queue, per-request/global work budgets or job broker; release permits reliably on exceptions/cancellation.
- Never spawn a thread per incoming request or uncontrolled fan-out from messages/events. Watch thread stack memory, context switches and overall process count.
- Watch nested .result() waits inside a limited executor; this can deadlock. Prefer structured orchestration, as_completed and explicit deadlines.
- Shutdown executors appropriately; avoid long-running background services in short-lived thread pools. Keep lifecycle tied to process startup and shutdown.
- Distinguish CPU-bound tasks (often process workers or external job systems) from I/O-bound tasks; GIL behavior depends on runtime/build and must not be assumed as a safety limit.
- Thread-unsafe database sessions and shared mutable objects must not be shared; use thread-local/per-task sessions, locks and atomic transactions where needed.

## Async and server worker limits
- Locate asyncio.create_task/gather, TaskGroup, semaphores, queues, blocking libraries and async endpoints.
- Avoid unbounded gather/coroutine spawning; bound concurrency AND backlog. Never call blocking sync I/O from event loop without suitable offloading and budget.
- Propagate cancellation and deadlines; set timeouts for HTTP, DB, Redis and external APIs. Check cleanup in finally and cancellation behavior.
- Configure Gunicorn/Uvicorn worker and concurrency limits, keepalive, request timeouts and graceful shutdown relative to CPU/RAM/DB pool; avoid assigning huge worker counts or blindly accepting defaults.
- Check Celery worker concurrency, prefetch, max tasks per child, rate/task limits, retry backoff, visibility timeout, queue lengths, idempotency and dead-letter strategy; choose values appropriate to task duration.
- Multiprocessing: review process limits, pickling/deserialization trust boundary, startup method, process lifecycle, CPU saturation and memory multiplication.

## Validation matrix
Record configured/observed thread count, executor active/queued cap, process count, DB connection count, async in-flight limit, request size/time limits, worst-case memory, tenant fairness, timeout/cancel behavior and shutdown behavior.
Tests: queue-full/overload, concurrent duplicate requests, forced downstream stall, deadlock regression, worker exception and graceful stop. Never load-test production without authorization.
