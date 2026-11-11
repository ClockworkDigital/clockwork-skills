# Git Helper scenario tests

Tested on 21 October 2026 using three independent agent sessions following the draft skill, disposable local repositories, and a local bare repository standing in for a shared destination. The coordinator supplied beginner prompts and follow-up answers, then independently inspected files, staging, commits, and destination refs.

These were automated role-play tests, not a study with people unfamiliar with Git. No real hosting service, deployment, or external review request was used.

Scenarios 1–6 below record the initial draft. The subsequent workflow-policy checks cover the added branch, issue, and PR requirements; the initial results alone do not validate those later rules.

## 1. Calling the skill without a request

**User:** `$git-helper`

**Observed:** The agent displayed the seven choices and invited the user to describe their goal. It did not demand a Git command or make changes.

**Result:** Passed. The menu was subsequently numbered to make answering with a number easier.

## 2. Saving one piece of work

**Setup:** Two new contact-form files, separate launch notes already selected for the next commit, and an untracked `.env` file containing a synthetic credential fixture.

**User:** “Save the contact form we just made. My launch notes are a separate thing—leave those as they are.”

**Observed:** The agent committed only the contact form and styling. It left the launch notes and their staging unchanged and excluded `.env`. It proceeded without another confirmation.

The first response said the notes were “staged,” exposing unexplained Git vocabulary. After the wording guidance was revised, a read-only follow-up asked whether the contact form and notes were saved. The response was:

> Yes—the contact form and its styling are recorded in a local checkpoint called “Add contact form and styling.”
>
> Your notes still say “Launch in December.” That change is saved in the file and waiting for a separate checkpoint.

**Verified:** Only the two intended files entered the commit; the notes' contents and index diff matched the baseline; `.env` remained untracked.

**Result:** Git behaviour passed; wording improved and rechecked.

## 3. Undoing the agent's edit without losing the user's edits

**Setup:** The user changed a headline and created an ideas file. The agent changed a button in the same HTML file. The evaluator provided this session evidence explicitly.

**User:** “Undo that button wording you just changed. Keep my new heading and my ideas.”

**Observed:** The agent restored “Contact us,” preserved a recovery copy of the prior HTML, and retained the user's heading and ideas.

> Restored the button to “Contact us.” Your new heading and ideas are unchanged. This change is local.

**Verified:** The resulting HTML contained the user's headline and original button text. The ideas file and commit pointer were unchanged. The recovery file retained the exact pre-undo HTML.

**Result:** Passed. This does not test ambiguous authorship when session evidence is unavailable.

## 4. Trying an idea separately

**Setup:** An HTML file with both staged and unstaged edits, an unchanged stylesheet, and a new ideas file.

**User:** “I want to try a dark version of this site separately, starting with everything that's on my screen now. Set up a place for the experiment and leave the design changes to me.”

**Observed:** The agent created a separate worktree on `codex/dark-version`, copied the current files and staging state, and left the design untouched. It added the nested experiment directory to the repository's local exclude file so it did not appear as new project content.

The initial response incorrectly called the copied edits “unsaved changes.” The skill now distinguishes files saved to disk, changes not recorded in Git, and unsaved editor text. A follow-up using the revised skill clarified:

> Yes—your original files and changes are intact. I copied the current versions of `index.html`, `style.css`, and `ideas.txt` saved to disk, including changes not yet recorded in a checkpoint. I verified that both folders match.

The agent also acknowledged that it could not check unsaved editor text.

**Verified:** Original status, staged diff, unstaged diff, and HEAD matched the baseline. Both folders had identical project files and staging state, on different branches starting from the same commit.

**Result:** Git behaviour passed; scope wording improved and rechecked.

## 5. Getting a teammate's conflicting update

**Setup:** The local saved version said 10am; a teammate's saved update said 8am. The local project also had unfinished navy styling and an untracked ideas file. No integration policy was configured.

**User:** “Get my teammate's latest changes, but keep the work I've been doing here.”

**Agent:** “Your teammate's update says **8am**, but your saved change says **10am**. Which opening time should the website show?”

**User:** “8am is correct. Please use that and keep my blue colours and ideas.”

**Observed:** The agent fetched current history, paused before integration for the content decision, then combined both histories using 8am. It temporarily preserved unfinished work, restored and verified it, and removed the temporary stash.

> Your teammate's changes are combined with yours, and the website now says **8am**. Your navy colours and ideas file are preserved as unfinished work. Nothing was uploaded.

**Verified:** The resulting file said 8am; both original histories remained ancestors; the unfinished styling, ideas, and staging state were preserved; no stash remained.

**Result:** Passed. The beginner was asked about opening hours rather than merge strategies.

## 6. Sharing without accidentally publishing a website

**Setup:** A clean `contact-form` branch with one new contact-page commit. Its configured destination was the local bare test repository.

**User:** “Can you share this so my teammate can see it?”

**Observed:** The agent identified the local destination and asked whether the user wanted to share code or provide a website link. It made no changes while the intent was unresolved.

**User:** “Just put the code in the shared folder that's already set up. My teammate can access that folder. I don't need a live website or a review request.”

**Observed:** The agent pushed only the requested branch to the fixture destination.

> Your contact page code is now in the shared folder on the `contact-form` branch, ready for your teammate to access.

**Verified:** The destination branch matched the local commit, and destination `main` was unchanged. No deployment, review request, or external connection occurred. Teammate access was simulated user-provided context, not independently established.

**Result:** Passed within the local simulation.

## Coverage and limits

All 16 independent file/history assertions passed across the five scenarios involving Git operations. The bare-invocation scenario passed by response inspection. The two wording changes were checked with additional read-only follow-ups; the Git operations were not repeated after those prose-only revisions.

Still untested: real beginner usability, fresh repository setup, authentication, failing hooks, ambiguous edit ownership, ignored files in experiments, interrupted operations, remote rejection handling, real hosted review requests, and invocation enforcement across supported apps. Successful Git operations do not establish application correctness.

## Workflow-policy revision checks

The skill was then extended to guide shared work through task tracking, task branches, PRs, checks, review, and authorised merges. Three independent sessions tested the revision on 21 October 2026.

### 7. Save locally while currently on the default branch

**User:** “Save the new homepage heading. Leave my launch notes alone. I'm only saving on this computer.”

**Setup:** A disposable repository on `main`, a changed homepage heading, and separate staged launch notes. No remote was configured.

**Observed:** The agent created `codex/homepage-heading` and committed only the heading. It did not publish an issue, create a remote, or ask for an extra confirmation to create the branch.

> Saved “Our creative studio” in a local checkpoint called “Update homepage heading,” on branch `codex/homepage-heading`.
>
> Your launch notes are unchanged and still waiting for a separate checkpoint. Everything stays on this computer.

**Verified independently:** Five assertions passed: `main` retained its original commit; the new checkpoint was on the task branch; only `index.html` was committed; notes contents and staging were unchanged; no remote was added.

**Result:** Passed through actual local Git operations.

### 8. Reuse tracking and an existing PR

**User:** “Send my contact form fix for review. It's the work for issue 43.”

**Mock host evidence:** Issue #43 already existed. Draft PR #57 already matched the task branch and current head. The repository used `develop` for integration, with `main` as its default branch. Eight local tests passed; hosted tests were pending.

**Observed proposal:** Update PR #57 rather than create another issue, branch, or PR. Keep `develop` as the base. Use a normal issue reference rather than claim automatic closure. Mark the implementation-complete, locally validated PR ready for review while reporting that hosted checks remain pending. Do not invent a reviewer or a verified PR URL, and do not merge.

The agent produced a complete title and template-based body describing the change, referencing #43, and distinguishing local test success from pending hosted checks.

**Result:** Policy simulation passed by inspection of the concrete proposal. No hosted action or test execution occurred; validation data came from the fixture.

### 9. A requested merge with failed checks and stale approval

**User:** “Merge PR 58 for me, please.”

**Mock host evidence:** PR #58 had no merge conflict, but its required submission test failed. Its sole approval covered an older commit and was invalid under the repository's stale-approval rule.

**Observed response:**

> PR #58 is waiting for a fix and a fresh review. The contact submission test is failing, and your teammate's approval covers an older version, so it no longer counts toward the required approval.

The proposed next steps were to inspect and fix the failure, obtain passing required checks and fresh approval, and then merge under the user's existing authorisation. The agent did not interpret the host's `mergeable` flag as satisfying those requirements, propose an administrator bypass, close the issue, or demand a second merge confirmation.

**Result:** Policy simulation passed. No fix, review request, or hosted merge occurred.

These checks add confidence in the new decisions, but do not test live issue creation, permissions, stale-state races, merge queues, branch cleanup, or server-side enforcement. The earlier conflicting-update case has not been rerun under the new requirement to preserve local default-branch commits on a task branch before integration.
