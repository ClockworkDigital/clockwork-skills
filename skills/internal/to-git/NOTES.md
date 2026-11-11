# To Git draft

- Status: Internal draft for review; two local conversion scenarios exercised on 21 October 2026.
- Maintainer: Clockwork; individual owner to be assigned.
- Intended tools: Claude Code and Codex with filesystem access and Git. Browser access and the source project's runtime are needed for application verification. Git-host publication additionally needs authenticated access.
- Invocation: `/to-git` in Claude Code after installation. Claude Code's `disable-model-invocation: true` and Codex's `agents/openai.yaml` configure explicit invocation. No personal installation or host settings are changed by adding this folder to the collection.
- Companion: `git-helper` is useful for later changes and importing into existing repositories, but is not required to create a new local baseline. Essential integration rules are included in this skill.
- Validation: Two independent agents exercised synthetic static-HTML and shared-storage React scenarios; 15 independent repository/file assertions passed. Browser verification was unavailable, and the React result correctly remained partial pending a backend/data-migration decision. See [scenario checks and limitations](TESTING.md).
- Schema compatibility: The common skill-creator validator does not recognise Claude Code's `disable-model-invocation` extension. Its Boolean value was checked separately, and the portable frontmatter/body passed validation with that extension omitted from a temporary validation copy. The actual skill retains the field. Claude.ai uploads may require a platform-specific package containing only supported fields; that packaging and native host invocation have not been tested.
- Known limitations: Not every Artifact export includes editable code, assets, hosted data, or runtime services. Claude-hosted features may require a separately chosen integration. A source archive alone is not evidence of a runnable app or completed Git repository.
- Distribution: Internal draft; an explicit licensing decision is required before external distribution.
