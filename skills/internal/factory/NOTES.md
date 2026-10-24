# Factory maintenance notes

- Maintainer: Clockwork Digital.
- Supported agent: Codex; the runner invokes Codex CLI, including when launched from another host.
- Requirements: Python 3.9+, Git, authenticated GitHub CLI and Codex CLI, macOS/Linux/WSL. Project checks require their own toolchain.
- Origin: Clockwork Codex factory developed in Formwork and PayShap-City-Hop, imported from the local global skill on 2026-10-24. Dashboard interaction inspired by zazencodes; see references/configuration.md. No upstream dashboard code is vendored.
- Distribution: internal use; no external license granted. Decide licensing before external distribution.

## Validation

Run from the collection root:

```bash
python3 -B -m unittest discover -s skills/internal/factory/tests
python3 -B -m unittest discover -s skills/internal/factory/assets/template/tests
```

The imported package passed 4 global tests and 22 runner tests. Global tests exercise installation into a temporary repository, preservation of existing installs, dashboard snapshots, HTTP authentication, host validation and artifact path restrictions. Runner tests cover routing and execution safeguards. The global installation's dashboard board and artifact drawer were previously checked in a browser.

No paid model execution or live GitHub publication is part of these tests. Model availability depends on the user's account. Existing project runners remain authoritative and updates must be deliberate. The dashboard reads recorded state; it does not confirm process liveness or remote merge status. One job is allowed per repository, not across all repositories. Local skills of the same name may take precedence. Dashboard startup currently needs --repo pointing to a Git checkout, even when displaying all registered projects.
