# Contributing skills

## Organization

Store each skill in its own folder using a short, lowercase, hyphenated name:

```text
skills/
  external/
    skill-name/
      SKILL.md
      PROVENANCE.md
  internal/
    skill-name/
      SKILL.md
```

Keep supporting scripts, references, and assets alongside the skill that uses them. Preserve an upstream skill's required structure when importing it.

## Adding an external skill

1. Identify the original source and confirm that its license permits the intended copying, modification, and use. If permission is unclear, retain a catalog link rather than copying the content.
2. Review the full skill and its supporting files, including commands, network access, filesystem changes, dependencies, and credential handling.
3. Try a representative task in a suitable environment. Record what was checked and any limitations; do not label an untested skill as tested.
4. Add permitted content under `skills/external/<skill-name>/`, preserving license notices and attribution.
5. Add `PROVENANCE.md` using the fields below, and add the skill to the README catalog.

```markdown
# Provenance

- Original author or organization:
- Original source URL:
- Upstream revision or release:
- License and license file:
- Date imported:
- Last reviewed:
- Maintainer:
- Compatible agent tools and prerequisites:
- Review status: pending / reviewed / tested
- Review notes and validation performed:
- Local modifications: none / describe changes
```

Use `pending` for candidates that have not completed review, `reviewed` after inspecting the instructions and supporting files, and `tested` after also running a representative task. These labels describe checks performed, not a guarantee of safety or compatibility.

## Adding an internal skill

1. Define the task the skill handles and when an agent should use it.
2. Create `skills/internal/<skill-name>/SKILL.md` with a clear name, description, actionable instructions, and any prerequisites.
3. Document the maintainer, supported agent tools, validation performed, and known limitations alongside the skill.
4. Exercise it on a representative task and update the README catalog.

## Maintaining the collection

Related tools, plugins, and rulesets can be cataloged under `tools/<name>/README.md` and in the README's companion tools table. Include the official source, purpose, license, reviewed revision, and scope of review. Source-only entries do not imply that an implementation has been reviewed or tested.

Review upstream updates before adopting them, update provenance when a skill changes, and record local deviations. Remove or mark obsolete entries when their sources, dependencies, or workflows no longer work. Avoid adding duplicate skills unless their differences justify keeping both.

Do not assign a repository-wide license to imported material without checking that its original terms permit it. Internal skills also need an explicit licensing decision before external distribution.
