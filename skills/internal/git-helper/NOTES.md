# Git Helper draft

- Status: Draft for review; six initial scenarios plus three workflow-policy checks exercised on 21 October 2026. Real beginner usability testing is pending.
- Maintainer: Clockwork; individual owner to be assigned.
- Intended tools: Codex and Claude Code with local Git and filesystem access. Uploads and review requests also require authenticated access to the chosen host.
- Invocation: Written for users to call deliberately. Codex invocation policy is included in `agents/openai.yaml`. Equivalent enforcement in other hosts has not been configured or verified.
- Validation: Skill structure checked with the skill-creator validator. Three independent agents exercised the initial six scenarios in disposable repositories; 16 independent file/history assertions passed. After adding workflow enforcement, a new local-save scenario passed five assertions, and two mock-host policy checks covered PR reuse and a blocked merge. Hosted operations were not executed. See [scenario tests and limitations](TESTING.md).
- Known limitations: Git cannot reliably attribute mixed edits to a particular agent without supporting session evidence. Git history does not capture external application state, ignored files, or unsaved editor buffers. Recovery and sharing claims must be limited to what the tools verify.
- Enforcement: [Workflow rules](references/workflow.md) govern the active skill; they do not install repository rules or restrict other sessions. Local saves can proceed without a tracker, while substantial shared work needs a task record before review readiness. Server-side protection and live issue/PR integration remain untested.
- Distribution: Internal draft. Licensing must be decided before external distribution.
