# Repository setup

The global skill is installed once. Each repository keeps a versioned
`factory/runner.py` and `factory/config.json` so ongoing jobs retain their known
implementation and snapshotted configuration. Existing runners remain compatible;
no migration is needed for the dashboard.

For a new repository, inspect its instructions and package scripts. Supply a
JSON config to `init --config FILE` containing real checks as arrays of command
arguments (not interpolated shell strings). Set `setup` as needed. Example:

```json
{
  "base_branch": "main",
  "setup": [["npm", "ci"]],
  "checks": [["npm", "test"], ["npm", "run", "build"]],
  "risk_guidance": "Changes to tenant isolation and billing require high risk."
}
```

This is an example, not a universal npm default. Confirm required runtime versions,
working-directory assumptions, test credentials and generated-file ignores.
Defaults include configurable Sol/Astra role profiles, protected instruction/CI
paths and the three-round cap. Generic risk factors include access control, trust
boundaries, destructive data, shared infrastructure, business integrity and unclear
impact. Add project-specific examples through `risk_guidance`.

The installer refuses existing factory files and local factory skills. It never
commits, pushes, creates labels or runs a model. Review and commit the generated
files, merge the setup to the configured base branch, then start from a clean
primary checkout matching that remote base. The runner's baseline checks must
pass before any model runs.

Dashboard registry: `~/.codex/factory/projects.json` (or `$CODEX_HOME/factory`).
Each registered repository is resolved to its primary checkout. Jobs remain in
that repository's Git common directory under `factory-state/jobs`; worktrees and
Git metadata are never exposed by the HTTP server. Artifacts are served as text.
Malformed/in-progress files are shown as warnings rather than hiding other jobs.
The dashboard cannot approve, rework, publish, or merge. Missing usage is unknown,
and published state is not automatically reconciled with GitHub merges.

The dashboard follows the board/chips/artifact-drawer interaction of
https://github.com/zazencodes/zazencodes-season-3/tree/main/src/software-factory-claude-code
with a new implementation for Codex JSON artifacts. No upstream dashboard code is
vendored. Unlike the original, ours has no automatic approver or merge action.
