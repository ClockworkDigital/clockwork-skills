# Task, branch, and review workflow

Read before a Git Helper operation that changes branches, commits, integrates, or publishes work. These are this skill's working defaults, not a claim that every team uses the same process.

## Establish the repository's rules

Inspect relevant repository instructions, contribution guidance, issue and PR templates, branch conventions, merge methods, and configured checks. For hosted work, inspect the actual default branch, target branch, protection requirements, and available permissions using the connected host or authenticated CLI. Respect documented release, fork, or stacked-PR workflows instead of assuming every PR targets `main`.

Use the defaults below where the repository has no convention. If required metadata cannot be read, state what is unknown; do not label unavailable checks or approvals as passed. A local-only project can use task branches and checkpoints without a hosting account. Explain which shared workflow steps remain unavailable, without blocking a local save or silently replacing a hosted PR with a direct push.

## One task, one branch, an appropriate tracking record

- Reuse the relevant issue or external task record. Search before creating another. Group checkpoints for the same outcome under that task; unrelated work should have separate branches and PRs.
- Require a linked issue or recognised task record for shared feature, bug-fix, or substantial maintenance work before marking its PR ready for review. Follow repository exemptions for small changes; absent a policy, a self-contained typo or formatting correction may be described entirely in the PR. A private experiment or local checkpoint does not require publishing an issue.
- Write an issue around the problem, desired outcome, scope, and observable completion criteria. Respect the repository template and audience. Do not copy credentials or private session details into it. Use existing labels and assignees only when their applicability is established.
- A request to file or track work in the shared tracker authorises creating the scoped issue. A request to save locally does not. If a review request needs a new shared issue and publishing it has not been authorised, first prepare the exact title and body, then ask one concrete question. Continue preparing the branch and PR content meanwhile. Do not fabricate an issue number or treat a local draft as a published record.
- Link partial work with a normal reference. Use closing language only when the PR satisfies the issue's completion criteria. On GitHub, `Closes #123` has automatic linking/closure semantics only for PRs targeting the default branch; do not promise automatic closure for another target. Never close an issue merely because a branch was pushed or a PR opened.

## Keep task commits off shared integration branches

- A genuinely new, independent repository with no commits may record its initial project baseline on its initial branch. This bootstrap exception also allows seeding a newly requested, verified-empty remote. It does not apply to an existing repository or remote with any history; subsequent task changes use branches and review as below.
- Before making a new task commit, check the branch. On the default, release, or other shared integration branch, create a task branch while preserving staged, unstaged, and untracked work. Routine branch creation is part of saving safely, not an extra approval step.
- Reuse the current task branch when its purpose fits. Follow repository naming rules; otherwise use the host's required prefix, or a short descriptive name such as `fix/contact-form`. Include an existing issue ID when useful. Do not create a new branch for every save or invent an issue ID.
- For a fresh task with no existing edits, start from the current intended base after fetching where available. For existing edits or local commits, preserve their actual starting point; do not reset to the remote default branch and lose work. Explain any meaningful inclusion of earlier changes.
- If task commits already exist on the local default branch, make them reachable from a task branch before doing anything else. Do not reset, delete, or rewrite the original branch simply to tidy it. Work and integrate updates on the task branch; repair the original pointer only within a separately authorised, verified recovery plan.
- Make checkpoints focused and descriptive. Preserve unrelated staging and edits. Follow established commit-message conventions without imposing a new format. Do not amend published commits or force-push as a routine way to make history look clean.
- The default rule is no direct pushes of task changes to a shared integration branch. Route requests such as “put my changes on main” through the PR workflow. An explicitly requested repository workflow exception must be acknowledged as an exception, must be within the user's authority, and must not bypass host protections.

## Prepare a reviewable pull request

When asked to send work for review, inspect the complete branch diff and outgoing history, the intended base, existing PRs, and issue linkage. Reuse the matching open PR rather than creating a duplicate. Surface unrelated commits before publishing them; do not silently rewrite history to remove them.

Use the repository PR template. Otherwise include the problem and resulting behaviour, the linked task, relevant validation with actual results, and known limitations. Add screenshots or reproduction steps when they help review. Keep the PR focused enough that someone can assess the change without the chat history.

Run checks appropriate to the change and the repository's requirements. A failed or unrun check is not a pass. A local checkpoint may preserve unfinished work; it does not establish readiness to merge. Publish a draft PR when implementation, task linkage, or necessary local validation is incomplete, stating what remains. Successful local checks do not prove hosted checks have passed.

Creating or updating the PR is within a request to send the work for review. Request review from an established owner or user-specified reviewer where that is part of the authorised workflow; do not guess people or send separate messages. Follow the host's artifact-linking requirements and return a verified PR link.

## Merge only when ready and authorised

Before merging, verify all of the following against the current PR and head commit:

1. The user authorised merging this work, or an already authorised end-to-end workflow includes it. “Save,” “upload,” and “send for review” alone do not.
2. The destination and scope match the task, and the PR is ready rather than a draft.
3. Required checks are complete and accepted by the host's rules, and relevant task validation has no unresolved failures. Pending, inaccessible, or absent results must not be reported as successful. If no CI is configured, report that and use the applicable local validation rather than inventing a CI requirement.
4. Required reviews and code-owner approvals are satisfied; blocking feedback and conflicts are resolved. Check whether new commits invalidated prior approval. Do not dismiss reviews, mark unresolved feedback resolved, use an administrator bypass, or replace a required human approval with the agent's own review.
5. If the repository has no formal review requirement, the user or a reviewer has accepted the concrete current changes. An explicit instruction to merge a specified PR can supply that acceptance when the reviewed scope is clear; do not demand a second confirmation. A vague “finish everything” before the diff exists does not establish review acceptance.

Use the repository's allowed merge method or merge queue. If several methods are allowed and no convention exists, prefer squash for a single coherent task, explaining it as combining the work into one change; preserve separate commits when the task or project calls for that history. Do not use merge options that bypass unmet requirements. Enable automatic merging only when the user authorises it; queued or automatic merging is pending until the host confirms completion.

After success, verify the host's merged state and resulting commit. Confirm linked issue closure only when the full task is complete and closure is verified. For authorised cleanup, remove a task branch only after verifying that it has no additional unmerged work or active workspace depending on it; account for squash/rebase merges rather than relying only on ancestry. Preserve other contributors' branches and unfinished work.

Report the outcome as “saved locally,” “uploaded,” “waiting for review,” “waiting for checks,” or “merged,” as appropriate. Do not call all of these states “done.”

## Basis and enforcement boundary

The branch-and-review structure follows [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow). Issue-linking details follow [GitHub's issue and PR linking documentation](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue). The task-record requirement and no-direct-push default are choices for this skill, with the scoped exceptions above.

The skill can enforce its own workflow while it is active. Server-side enforcement requires separately configured [branch protection or rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). Inspect existing protections, but do not silently install or weaken them. Documentation checked on 21 October 2026.
