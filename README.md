<a href="https://www.clockworkmedia.co.za/">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/clockwork-symbol-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/clockwork-symbol-light.svg">
    <img src="assets/clockwork-symbol-light.svg" alt="Clockwork symbol" width="96" height="96">
  </picture>
</a>

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
| [factory-claude](skills/internal/factory-claude/SKILL.md) | Run the Claude Code factory with Sonnet/Opus routing and a read-only dashboard. | Internal, Clockwork | [Maintenance notes](skills/internal/factory-claude/NOTES.md) | Automated tests; live Claude run unverified |
| [factory](skills/internal/factory/SKILL.md) | Run the Codex issue-to-reviewed-PR factory and its read-only dashboard. | Internal, Clockwork | [Maintenance notes](skills/internal/factory/NOTES.md) | [26 automated tests; prior dashboard browser check](skills/internal/factory/NOTES.md#validation) |
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

## Install for Codex and Claude Code

You need access to this private GitHub repository, Git, and a current installation of Codex or Claude Code. These commands use Bash on macOS, Linux, or WSL. Run them on the machine where your agent runs.

### 1. Clone the collection

With the [GitHub CLI](https://cli.github.com/) installed:

```bash
gh auth login
gh repo clone ClockworkDigital/clockwork-skills
cd clockwork-skills
```

Alternatively, clone `https://github.com/ClockworkDigital/clockwork-skills.git` using your existing Git credentials. Keep the clone in a permanent location; the links below depend on it.

### 2. Choose the installation scope

Run one of these blocks from the collection's root. Personal installation makes skills available across your local projects:

```bash
# Codex only
skill_dest="$HOME/.agents/skills"

# Claude Code only: use this instead
# skill_dest="$HOME/.claude/skills"
```

To install for one project instead, set an absolute project path and choose its tool-specific folder:

```bash
project_dir="/absolute/path/to/your-project"
skill_dest="$project_dir/.agents/skills"       # Codex
# skill_dest="$project_dir/.claude/skills"     # Claude Code
```

### 3. Link the skills

Run this in the same Bash session after choosing `skill_dest`:

```bash
collection_dir="$(pwd -P)"
mkdir -p "$skill_dest"
for skill_dir in "$collection_dir"/skills/external/* "$collection_dir"/skills/internal/*; do
  [ -f "$skill_dir/SKILL.md" ] || continue
  skill_name="${skill_dir##*/}"
  if [ -e "$skill_dest/$skill_name" ] || [ -L "$skill_dest/$skill_name" ]; then
    printf 'Skipped existing entry: %s\n' "$skill_dest/$skill_name"
    continue
  fi
  ln -s "$skill_dir" "$skill_dest/$skill_name"
done
```

For both tools, run steps 2 and 3 again with the other destination. Existing entries are skipped, including links from an earlier run. Inspect any skipped skill to confirm it points to the version you intend to use. Each link exposes the whole folder, including references, scripts, licenses, and provenance.

Project links containing absolute paths are specific to your machine. For a shared or cloud project, copy the selected complete skill folders into `.agents/skills/` or `.claude/skills/` and commit those copies instead. Keep licenses and provenance with them. Personal installs are local and do not transfer to remote or cloud environments.

### 4. Use a skill

Start a fresh session in the project you want to work on. In Codex CLI or the IDE extension, use `/skills` or type `$` to select a skill; in the desktop app, select it from the skills picker. Claude Code exposes installed skills as slash commands.

| Task | Codex prompt | Claude Code command |
| --- | --- | --- |
| Run the Claude factory | `$factory-claude issue 1` (requires Claude CLI) | `/factory-claude issue 1` |
| Run the software factory | `$factory issue 1` | Requires Codex CLI; see skill prerequisites |
| Review a plan | `$grilling Stress-test this plan…` | `/grilling Stress-test this plan…` |
| Diagnose a bug | `$diagnosing-bugs Investigate this failure…` | `/diagnosing-bugs Investigate this failure…` |
| Improve architecture | `$improve-codebase-architecture` | `/improve-codebase-architecture` |
| Prepare a handoff | `$handoff Continue the API work next session` | `/handoff Continue the API work next session` |
| Edit prose | `$unslop Review this draft…` | `/unslop Review this draft…` |

Install `codebase-design`, `domain-modeling`, and `grilling` together with `improve-codebase-architecture`. The loop above includes them all. Architecture exploration and grilling require sub-agent support. Upstream references to the “Skill tool” mean invoking the named companion skill using the host's available mechanism; host compatibility has not been tested for every workflow.

If a skill is missing, check that `<destination>/<skill-name>/SKILL.md` resolves, confirm the clone hasn't moved, and restart the agent. Review each skill's `PROVENANCE.md` for its requirements. Ponytail is a separate [companion tool](tools/ponytail/README.md) and is not installed by these commands.

### Updates and removal

Update the clone from its root:

```bash
git pull --ff-only
```

Linked skills pick up the changed files. Rerun the linking loop for newly added skills; remove obsolete links when a skill is removed or renamed. Restart the agent if changes do not appear. For copied project skills, copy updates deliberately and review the diff before committing.

To uninstall one linked skill, select the same `skill_dest` as above, then remove only its link:

```bash
skill_name="unslop"
if [ -L "$skill_dest/$skill_name" ]; then
  unlink "$skill_dest/$skill_name"
fi
```

Installation locations and invocation guidance were checked on 2026-10-20 against the official [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skills documentation](https://code.claude.com/docs/en/skills).

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
