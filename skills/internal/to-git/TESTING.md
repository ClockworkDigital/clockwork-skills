# To Git scenario checks

Tested on 21 October 2026 with two independent agent sessions following the skill, using synthetic Artifact source fixtures in disposable directories. These were conversion tests, not a live Claude export or a study with beginners. No repository was uploaded and no personal skill installation was changed.

## Standalone HTML calculator

**User:** “Turn this into a local project in the studio-calculator subfolder so I can keep working on it with an agent.”

**Source:** A self-contained HTML quote calculator with inline styling, hours and hourly-rate inputs, and calculate/reset controls. No package manifest, external assets, network calls, or host APIs.

**Observed:** The agent copied the source byte-for-byte to `index.html`, added a README and `.gitignore`, and created an independent local repository with its first commit on `main`. It did not add a framework, dependency installation, remote, or deployment.

The agent exercised default, decimal, and zero calculations, submit prevention, and the reset callback using Node with a simulated DOM. Browser tooling was unavailable, so it explicitly left appearance, native input behaviour, browser interaction, and console checks unverified. The README and final response both disclosed that limit.

**Verified independently:** The project root was independent; there was one baseline commit on `main`; the tree was clean; no remote existed; the supplied test identity was used; the source bytes matched; exactly `.gitignore`, `README.md`, and `index.html` were tracked.

**Result:** Local conversion and logic checks passed. End-to-end browser verification remains pending.

## Shared team board

**User:** “I want this in its own local project, and the whole team must still see the same tasks from their own computers. We already have tasks saved in the Artifact.”

**Source:** A React component using a host-provided storage global for a shared list. No backend, credentials, data export, dependency metadata, or cached packages were available. The test prohibited network access.

**Observed:** The agent preserved the component byte-for-byte, added an entry point with an explicit missing-storage notice, documented migration gaps, and checkpointed the partial project. It did not replace shared storage with browser-local storage, invent package versions, claim to have imported task data, or claim that the app was runnable.

It asked:

> Should this connect to a shared database your team already uses, or should we plan a new private shared database? We'll also need an export of the existing tasks before switching over.

**Verified independently:** The project root was independent; there was one baseline commit on `main`; the tree was clean; no remote existed; the supplied test identity was used; the original component bytes matched; the README said the project was not yet runnable; no `localStorage` substitute was introduced.

**Result:** Correctly stopped at the shared-data migration decision after preserving useful independent work. Build, browser behaviour, persistence, and multi-device access remain untested. The agent inspected npm's local cache; incidental npm logging outside the fixture was not ruled out, so this is not a filesystem-isolation audit.

## Validation and remaining coverage

All 15 independent repository/file assertions passed across the two fixtures. The portable skill schema and reference existence were checked. Claude Code's `disable-model-invocation` Boolean and Codex's invocation policy were checked separately because the bundled skill-creator validator does not recognise the Claude-specific frontmatter extension. Native command discovery and invocation were not exercised.

Still untested: real Artifact download/export, inaccessible links, project archives, React dependency installation, full browser rendering, existing-repository import, identity prompts, data migration, host authentication, remote creation, upload retries, hosted PR creation, and server-side protection. The tests support the recorded local outcomes and migration decisions only.
