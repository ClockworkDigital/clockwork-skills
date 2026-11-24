# Agent factory

Only this configuration lives here: the global `agent-factory` skill runs its bundled runner
against this repository (`factory.py --repo . status`). To pin a runner version instead,
vendor `factory/runner.py` and `factory/factorylib/` together. A repository runner takes precedence for jobs.
Providers (Codex, Claude) are chosen per step from machine-level accounts by headroom.
Review config.json, commit and merge setup to the remote base before starting a job.
One job per repository; three build rounds plus three review fixes; human merging unless auto_merge is on; no deployment.
