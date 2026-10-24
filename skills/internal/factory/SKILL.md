---
name: factory
description: Operate the Codex issue-to-reviewed-PR factory across repositories, install its repository configuration, inspect jobs, or open its live dashboard.
---

# Global Codex factory

Resolve `SKILL_DIR` to the directory containing this SKILL.md, then use
`python3 "$SKILL_DIR/scripts/factory.py" --repo REPO COMMAND`.
This works for collection checkouts, personal installs and project-local links.
Requires Python 3.9+, Git, authenticated GitHub CLI (`gh`), Codex CLI (`codex`),
and a POSIX system (macOS/Linux/WSL).
Resolve REPO from the user's project/current working directory; never infer it
from the dashboard's most recent project. Read the target repository's agent
instructions and `factory/README.md` when present.

Commands:
- `issue NUMBER`: explicitly selected open issue; no queue label required.
- `run`: resume unfinished work or select one issue labeled `factory`.
- `status`, `resume JOB_ID`, `rework JOB_ID --feedback-file PATH`: delegate to the
  project's installed runner. Inspect failures before rework; preserve partial work.
- `publish JOB_ID`: push/open a draft PR only when the user's request authorizes
  publication. Attach the PR to the chat when the app tool is available.
- `dashboard --port 8787`: serve the read-only dashboard on localhost. Keep its
  process running and open the exact URL it prints, including its access token.
  The board includes registered repositories and refreshes every two seconds.
- `register`: add the current repository to the local dashboard registry.
- `init --config PATH`: install the bundled runner and regression tests into a
  repository that has no factory. First inspect its toolchain and write a JSON
  config with its real `setup`, `checks`, `base_branch`, and optional `risk_guidance`.
  Read [configuration.md](references/configuration.md) before installing.

Existing project runners/configurations take precedence and are never silently
replaced. The global launcher routes commands; deterministic project runners
own sequencing, locks, checks and saved state. Project-local skills of the same
name can still take precedence; use this absolute launcher for global commands.
Do not remove or migrate a running project's skill or runner merely to deduplicate.

Defaults: Sol for intake/build/code/UI review, Astra for high-risk specifications
and security review, one job at a time per repository, three build rounds,
human merging. Never merge or deploy through the factory. The dashboard is a
read-only view of saved state, not proof that a process is alive or a remote PR
has merged. Never manually edit state or bypass failed gates.
