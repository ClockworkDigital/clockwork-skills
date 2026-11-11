---
name: git-helper
description: Guide people unfamiliar with Git through saving and undoing work, task branches, linked issues, pull requests, and reviewed merges. Use when the user invokes git-helper or asks for guided Git workflow help.
---

# Git Helper

Help the user describe the outcome they want, then carry out the appropriate Git workflow. Assume no Git knowledge. Keep explanations short and connect choices to their effect on the user's work.

This is a user-invoked workflow. Do not start it merely because an agent's coding task involves Git.

## Workflow to enforce

Guide shared work through **issue → task branch → focused checkpoints → pull request → checks and review → authorised merge**. Follow the repository's documented equivalent when it has one. The user describes the outcome; choose the routine Git mechanics for them.

Before changing branches, recording checkpoints, integrating changes, or publishing work, read [workflow rules](references/workflow.md). Apply the relevant gates: keep new task commits off the default or shared integration branch, reuse existing task tracking, and use a reviewed pull request to integrate shared work. Do not turn every checkpoint into a new issue or PR. Local saving must remain available when hosting is unavailable.

These rules govern the agent while using the skill. They do not install server-side branch protection or govern other sessions. Do not change repository permissions, rulesets, or required checks unless the user asks for that configuration work.

## Start with the user's intent

If the invocation includes a request, go directly to that workflow. Use the conversation to resolve references such as “these changes” or “what you just did.”

If there is no request, ask:

> What would you like to do with your project?
>
> 1. Save my progress
> 2. See what's changed
> 3. Try an idea separately
> 4. Undo something
> 5. Share my work or ask for review
> 6. Get the latest changes
> 7. Help me fix a problem
> 8. Start or track a piece of work
> 9. Finish and merge reviewed work
>
> You can also describe what you're trying to achieve.

Accept a number, a menu label, or a description. Do not make the user choose a Git command or repeat an intent they already provided.

## Check the project

Use available tools to inspect the relevant project before changing it. Determine the repository root, current branch, staged and unstaged changes, new files, and any operation already in progress. Inspect recent history and configured remote destinations when the request needs them. Fetch remote state when a current comparison is necessary; do not describe old tracking information as current.

A file saved in an editor may still have changes that are not recorded in a Git checkpoint. Filesystem inspection cannot establish whether an editor also contains unsaved text. If the user refers to everything on screen, describe the scope as the current files saved to disk unless editor access establishes more. Do not claim to have included unsaved editor changes.

If several projects could be intended and context does not resolve the choice, ask which one. If Git or tool access is unavailable, explain the missing prerequisite and give the smallest useful next step. Never claim an action was performed when you only supplied instructions.

If the folder is not in a Git repository, explain that Git can record checkpoints for it. Offer setup when needed for the user's request; direct requests to set up Git already authorise that work. Check for a parent repository before initialising. Exclude secrets and generated files appropriately, and do not invent a commit identity or silently change global Git settings.

## Choose and carry out the workflow

Briefly describe the intended action and proceed when the request and scope are clear. Ask only about choices that change the outcome. Prefer questions such as “Do you want to keep the contact form changes?” over questions about resets or reverts.

Respect authorisation already given in the conversation. Routine inspection, local checkpoints, and creating a separate place to experiment do not need repeated confirmation. Before discarding work or rewriting shared history, identify the affected work and explain the consequence; obtain confirmation if that specific action and scope have not already been authorised. Prepare the relevant comparison before asking.

### Save my progress

Inspect the changes and create a local commit with a descriptive message on the task branch. If currently on the default or another shared integration branch, first preserve the changes on a suitable task branch according to the workflow rules. Treat “save my progress” as a local checkpoint unless the user also asks to upload it. When the intended scope is clear, include the relevant work without asking the user to name every file.

Check staged changes as well as unstaged and new files. Preserve unrelated edits and staging choices; do not use blanket staging when it would include unrelated work. If several unrelated pieces of work make the scope unclear, summarise them and ask what belongs in this checkpoint. Inspect for likely credentials before committing without printing their values.

If there is nothing new to save, say so. If a hook or other check fails, explain the blocker and address it within scope; do not bypass checks just to complete the save.

### See what's changed

Explain changes in terms of features, content, and behaviour. For a general request, compare current files with the latest local checkpoint, including staged changes and new files. State the comparison used. Ask only if a different comparison is implied but unclear.

Show a diff or file details when useful or requested. Do not modify files as part of this workflow.

### Try an idea separately

Create a branch or a separate worktree suited to the task and environment, following repository conventions. Explain where the experiment will happen and how the user can return to the original work.

Account for existing edits before switching or creating a workspace. A new branch alone does not preserve uncommitted edits as a checkpoint, and a new worktree does not automatically contain them. Preserve the original work and make clear whether the experiment includes the current edits or starts from a saved checkpoint. Do not assume the starting point is the default branch.

### Undo something

Identify the intended change and what must remain. Inspect the diff, history, and available session evidence. Do not assume the latest commit contains only the agent's work, or that all uncommitted changes were made by the agent.

Prefer a targeted reversal. For shared commits, prefer a new commit that reverses the relevant change while preserving history, on a task branch for review through a pull request. If the target overlaps other work or its origin is unclear, show the ambiguity and ask before modifying it. Do not substitute a whole-project reset for an unclear request.

Before discarding uncommitted work, preserve a recoverable copy where practical and record how to find it. A branch pointing at the current commit does not preserve those edits. Do not promise recovery unless the affected content was actually retained.

### Share my work

Establish the intended destination and audience from context or existing configuration. If “share” is ambiguous, ask whether the user wants to upload their branch, request a review, or publish a live result. These are different outcomes.

Inspect the full set of commits and files that would be uploaded, including earlier local commits. Explain any unexpected scope before proceeding. Push the task branch to the intended destination when authorised. When review is requested, follow the issue-linking, PR-content, and draft-readiness rules in the workflow reference; reuse an existing PR for this task and base branch. An upload-only request does not require a PR yet, but integrating shared work does. Do not infer permission to merge, change repository visibility, or deploy from a request to share. If pushing may trigger configured automation, mention known consequences relevant to the choice.

If a remote rejects the upload, inspect the cause. Do not retry with a force push or switch destinations without resolving the reason and authorisation.

### Get the latest changes

Check the current branch, intended source, and local work. Fetch and inspect the relationship between local and remote history before integrating updates. Use a fast-forward when possible. If a local shared integration branch has task commits that are absent upstream, first preserve those commits on a task branch. Combine teammate updates there; do not create new task or merge commits on the shared integration branch as a shortcut. For other divergence, follow established project policy when it resolves the choice safely; otherwise explain the situation and the meaningful options.

Preserve local work before integration. If conflicts arise, resolve only those whose intended result is clear from the task and surrounding code. Ask about product or content choices that cannot be inferred. Track any temporary stash or other saved copy, and verify restoration before deleting it.

### Help me fix a problem

Inspect the failed operation, relevant error, and repository state. Explain the cause in ordinary language and make the smallest appropriate repair. Do not blindly repeat a failed command, bypass checks, or delete Git metadata.

For authentication problems, guide the user through the host's normal sign-in flow without asking them to paste credentials into chat. Pause an in-progress merge or rebase when resolving it requires a decision from the user.

### Start or track a piece of work

Establish the intended outcome and what would make it complete. Reuse an existing issue or task record, or prepare one following the workflow reference. Create or reuse the corresponding task branch, accounting for current work before choosing its starting point. Explain the task and workspace in ordinary language. Setting up the workflow does not itself authorise implementing the feature.

### Finish and merge reviewed work

Inspect the actual PR, latest changes, linked issue, required checks, review decisions, and unresolved feedback. Apply the merge gates in the workflow reference. A request to merge authorises merging once those gates are met; do not ask again solely because merging changes the remote. If a requirement is unmet, explain the concrete blocker and continue any authorised work that can resolve it. Verify the merged result before reporting completion or closing the task.

## Confirm the result

Verify the resulting Git state after making changes. Report what actually happened, any work still outstanding, and whether the result is local or uploaded. For an experiment or recovery copy, give the location or identifier needed to find it again. Do not equate a local checkpoint with an off-device backup, an upload with a deployment, or a successful Git command with a tested application.

Use a brief response such as:

> Saved a local checkpoint called “Add contact form.” It includes the form and styling changes. You can ask me to return to this checkpoint later.

Or:

> Uploaded your changes to the `contact-form` branch and opened a review request: [Review changes](https://example.com/review). The changes are waiting for review.

Replace illustrative names and links with verified results. Mention excluded work or recovery details when relevant. Introduce Git terms only when they help, for example “a checkpoint, called a commit in Git.” Offer further explanation when asked rather than turning each action into a lesson.

Keep the result understandable without Git vocabulary. Say “Your launch notes are still waiting for a separate checkpoint” instead of “Your notes remain staged,” unless the staging detail matters; then explain it as work selected for the next checkpoint. Describe uncommitted work as “changes not yet recorded in a checkpoint,” not “unsaved changes.”
