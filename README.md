# Clockwork Skills

A curated collection of agent skills discovered around the web and created internally at Clockwork, plus companion tools and rulesets.

The collection favors useful, understandable, maintainable skills. Each skill should solve a clear problem, document its requirements, and make its origin easy to trace.

## Collection

| Location | Contents |
| --- | --- |
| [External skills](skills/external/) | Reviewed skills from the community, with attribution and source links. |
| [Internal skills](skills/internal/) | Skills developed and maintained internally. |
| [Companion tools](tools/) | Related tools, plugins, and rulesets, with source links and review notes. |

External skills are vendored at pinned upstream revisions. Each folder includes its license and review notes in `PROVENANCE.md`.

## Catalog

| Skill | Purpose | Origin | Source | Review status |
| --- | --- | --- | --- | --- |
| [unslop](skills/external/unslop/SKILL.md) | Remove AI writing patterns from prose. | External, pstack / Lauren Tan | [cursor/plugins](https://github.com/cursor/plugins/tree/88d47514b82e7c44f00f2b2a72ff6dd12158038c/pstack/skills/unslop) | Reviewed |
| [grilling](skills/external/grilling/SKILL.md) | Stress-test a plan, decision, or idea through questions. | External, Matt Pocock | [mattpocock/skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling) | Reviewed |
| [diagnosing-bugs](skills/external/diagnosing-bugs/SKILL.md) | Diagnose bugs using a reproducible feedback loop. | External, Matt Pocock | [mattpocock/skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/diagnosing-bugs) | Reviewed |

| [handoff](skills/external/handoff/SKILL.md) | Summarize a session for another agent without duplicating existing artifacts. | External, Matt Pocock | [mattpocock/skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/handoff) | Reviewed |
| [improve-codebase-architecture](skills/external/improve-codebase-architecture/SKILL.md) | Find architecture improvements and explore a chosen refactor. | External, Matt Pocock | [mattpocock/skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/improve-codebase-architecture) | Reviewed |
| [codebase-design](skills/external/codebase-design/SKILL.md) | Supporting dependency: shared vocabulary and techniques for module design. | External, Matt Pocock | [mattpocock/skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/codebase-design) | Reviewed |
| [domain-modeling](skills/external/domain-modeling/SKILL.md) | Supporting dependency: maintain project terminology and architecture decisions. | External, Matt Pocock | [mattpocock/skills](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/domain-modeling) | Reviewed |

The architecture workflow also uses `grilling`. Its supporting skills, `codebase-design` and `domain-modeling`, are included above.

## Companion tools

| Tool | Purpose | Source | Review status |
| --- | --- | --- | --- |
| [Ponytail](tools/ponytail/README.md) | Encourage agents to reuse existing code and build only what a task needs. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Source documentation reviewed; implementation unreviewed and untested |

## Curation principles

- Prefer skills with a specific purpose and clear instructions over broad, overlapping bundles.
- Review instructions, scripts, dependencies, permissions, and external services before including a skill.
- Preserve attribution and comply with the source license. Public availability alone does not grant permission to copy.
- Record the source revision and review date so updates can be assessed deliberately.
- Clearly label local modifications to external skills.
- Keep secrets, credentials, and private customer information out of the collection.

## Using the collection

Read a skill's `SKILL.md` and accompanying documentation before installing or running it. Requirements and installation methods may differ between agent tools; compatibility should be documented per skill.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the process for adding and maintaining skills.
