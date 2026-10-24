# Claude factory maintenance notes

- Maintainer: Clockwork Digital.
- Origin: adaptation of the sibling Clockwork `factory` skill, 2026-10-24. Dashboard interaction attribution remains in references/configuration.md; no upstream dashboard code is vendored.
- Supported agent: Claude Code. Requires Python 3.9+, Git, authenticated `gh` and `claude`, and macOS/Linux/WSL.
- Distribution: internal use; no external license granted. Decide licensing before external distribution.

## Validation

Run from the collection root:

```bash
python3 -B -m unittest discover -s skills/internal/factory-claude/tests
python3 -B -m unittest discover -s skills/internal/factory-claude/assets/template/tests
```

Validation on 2026-10-24: 4 global tests and 24 runner tests passed, plus skill metadata validation. Automated tests cover installation, HTTP/artifact restrictions, deterministic lifecycle, role routing, and a fake Claude executable exercising the CLI adapter. No live Claude run has been performed: Claude CLI is not installed on the development machine. This does not certify model availability or end-to-end Claude behavior. The dashboard UI is shared with the previously browser-checked Codex version.

The launcher needs --repo pointing to a configured Git checkout, even for the dashboard. State is one job per repository. Dashboard data is recorded state, not proof of process liveness. Read references/configuration.md for tool restrictions and migration limitations.
