# Provenance

- Original author or organization: Matt Pocock
- Original source URL: https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/improve-codebase-architecture
- Upstream revision: `5beb35b040e3de97e54fa9e386d7e42d15c295c2`
- License: MIT, preserved in [LICENSE](LICENSE).
- Date imported: 2026-10-20
- Last reviewed: 2026-10-20
- Maintainer: Unassigned
- Review status: reviewed
- Local modifications: None to upstream files. Added this provenance record and a copy of the applicable upstream license.

## Requirements and review

Requires codebase and Git history access, sub-agent support, a skill invocation mechanism, and HTML viewing. Calls codebase-design, grilling, and domain-modeling, all included in this collection. Writes a report to the OS temporary directory and opens it using an OS command. Its report template loads Tailwind and Mermaid from external CDNs and configures Mermaid with securityLevel: loose; review report content before opening it. Later phases may update GLOSSARY.md and propose ADRs. No bundled executable scripts.

Read every imported file and checked the upstream skill directory for supporting files. Verified imported bytes against pinned upstream downloads and checked local Markdown file references. No representative task has been run, and compatibility has not been tested in an agent runtime.
