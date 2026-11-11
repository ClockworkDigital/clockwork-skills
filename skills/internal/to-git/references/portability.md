# Portability decisions

Inspect the actual export before applying these routes. Do not assume a particular Claude runtime API or export shape from the artifact's age or title.

| Source | Default treatment | Evidence to check |
| --- | --- | --- |
| Standalone HTML/CSS/JS | Preserve a small static project. Add a local server command only when browser restrictions or routing require it. | Script imports, relative assets, external requests, functionality when opened outside Claude. |
| React JSX/TSX component | Add an entry point and minimal compatible build tooling, keeping JavaScript or TypeScript as supplied. | Actual imports, styling pipeline, local components, asset paths, aliases, browser APIs. |
| Project archive | Preserve the existing manifest, lockfile, and layout where sound. | Safe extraction paths, actual scripts, required runtime version, missing files, bundled credentials or `.git` metadata. |
| Markdown, SVG, diagram, or other source document | Version the editable source and necessary assets, with a suitable preview instruction. | Whether the export is editable source or only a rendered image/PDF. Do not claim to reconstruct source from a rendered export. |
| Link or screenshot with no source | Acquire an authorised source export or request it. | A rendered preview alone does not establish that complete source and assets are accessible. |

## Runtime features that may need migration

Detect features from the source and available runtime documentation. Host-injected globals, messaging bridges, sandbox filesystem paths, built-in components, and connector calls are not ordinary browser dependencies. Trace what each feature does before choosing a replacement.

- **Storage:** Determine whether the feature expects device-local, per-user, shared, or server-side persistence. Local browser storage may fit an explicitly local tool, but does not preserve shared data, access controls, or multi-device behaviour. Source export is not data migration. Do not claim stored records came across without an authorised data export and verification.
- **AI features:** Preserve the request/response intent. A browser-only export may rely on the host to authenticate and pay for calls. Moving that feature to a provider-backed server route introduces credentials, costs, and possibly a different data destination. Prepare that choice for the user; do not hard-code a provider key into the frontend or pretend that mock output is the original feature.
- **Connectors and identity:** Access to a service inside Claude does not automatically transfer to the standalone app. Identify the required service and operation, and use the user's authorised integration choice. An existing agent connector is not automatically a reusable app credential.
- **Files and assets:** Resolve exported assets and supplied uploads without assuming host-local paths work on the user's computer. Check whether remote assets require authentication or carry private tokens. Ask for missing source assets rather than substituting unrelated images or deleting the affected feature.
- **Styling and components:** Preserve the actual CSS, fonts, and components. Utility classes without their stylesheet do not preserve the appearance. Resolve local aliases to real files; do not infer an npm dependency solely from an import path that originally referenced host components.

Keep migration notes proportional to the project, normally in the README. Separate a feature that works, one that needs configuration, and one that has not been ported. A clearly labelled partial result is useful; silently degraded functionality is not.

## Export guidance and command scope

Claude's [Artifact documentation](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) describes different export controls for template artifacts and legacy artifacts. Guide the user according to their actual UI; avoid promising a code export for every type.

`/to-git` is the command name supplied by installing this skill in [Claude Code](https://code.claude.com/docs/en/skills). It does not install a new built-in command in every Claude chat. The equivalent skill can run in another capable agent host using that host's invocation mechanism. Actual conversion requires access to the source files and filesystem tools; committing requires Git and an author identity. Hosting additionally requires authenticated access to the intended Git host.

Documentation checked on 21 October 2026. Recheck the relevant official documentation when an actual source uses a different export or runtime contract.
