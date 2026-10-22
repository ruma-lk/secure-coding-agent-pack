# Optional Graphify navigation — detect, offer installation, fall back safely

For multi-file code exploration and security audits, use Graphify as an optional local source-navigation index, **never a security authority**.

## Availability detection
1. Check for executable `graphify` using an appropriate OS-safe command and run `graphify --version` if available. Do not infer availability from a directory name or old graph output alone.
2. Check project graph files under `graphify-out/` and their provenance, source revision, schema and freshness. A stale or mismatched graph must be rebuilt before relying on its relationships.
3. If Graphify is absent, inform the user that optional graph-based navigation could reduce broad file reads. **Ask before installing a third-party executable**; an explicit prior installation approval for this project may be reused. Never silently install it, run curl-to-shell commands, use sudo/admin, change the agent's global instructions, or enable third-party hooks.
4. Installation, network/package permissions and privacy must be reviewed before proceeding. Prefer documented official `graphifyy` Python package (double 'y') in isolated tooling via `uv tool install graphifyy` or `pipx install graphifyy` after approval. Python 3.10+ and a supported installer are prerequisites. Pin or review the chosen version where possible. Check https://github.com/Graphify-Labs/graphify and official documentation for current instructions. Validate `graphify --version` afterward.
5. `graphify install` registers agent-specific skill/hooks and changes agent configuration. This is a **separate opt-in action**, not required merely to call the CLI. Inspect its effects and obtain approval; don't overwrite or conflict with existing secure-coding instructions.

## Index and query
1. Before first use, obtain consent for scanning project sources and agree what directories are in scope. Default to local code AST mapping, excluding secret directories, credentials, production dumps, private backups and other sensitive data. Never upload private artifacts to Cloud/API backends without explicit permission. Documents/media semantic analysis may use models or configured APIs, so inspect privacy settings first.
2. Generate or refresh graph using installed CLI instructions (e.g. `graphify .` if supported by the installed version). Inspect ignored files, paths and output size. Persist output locally only when allowed and keep graph artifacts out of public commits if they reveal private architecture.
3. Query scoped paths using `graphify query "question"`, `graphify explain "symbol"`, or `graphify path "A" "B"` as supported. Prefer concise results and source locations, never ingest entire `graph.json` or `GRAPH_REPORT.md` into agent context for ordinary tasks.
4. Graph relationships are `EXTRACTED` or `INFERRED`, not verified runtime authority. Follow affected paths to source code, caller/callee tests, configuration, dynamic dispatch, reflection, queues, event/webhook handlers, permissions and deployments as needed.
5. Refresh/revalidate after code edits, branch changes, large merges, regenerated code or schema changes. Track revision and tool version in compact project state; do not assume a graph is current merely because output files exist.

## Security completeness
- Graph lookup must **never replace** all mandatory framework and specialist checks. Maintain security findings and task evidence even if graph results omit a path.
- Explicitly inspect missed or poorly represented runtime behavior: dynamic imports, framework magic, authorization middleware, config, external calls, SQL, queues, CDN, browser/mobile storage, service infra, IPG callbacks and eSMS.
- Never interpret absence of a node/edge as proof of no dependency, no vulnerability or no required test.
- Measure peak context and total tokens on representative tasks with/without Graphify rather than repeating vendor savings claims.

## Failure and handoff
If installation is declined, missing prerequisites, commands fail, index is stale, unsupported language, permissions block access, or graph has weak coverage: set `graphify_status: unavailable|declined|stale|failed|partial` and continue with direct scoped code search plus task-state tracking. No security task is skipped or reported PASS due to Graphify failure.

Report `graphify_status`, tool version (if known), indexed revision, source coverage limitations, queries used, and which code paths were independently verified.
