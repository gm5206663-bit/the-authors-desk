# Coordinating agents and concurrent work

A public handoff is a coordination record, not a secret and not a Git lock.
No local lock file protects work by another agent on another machine.

## Before editing

1. Read the latest remote revision, local contracts, active handoffs and any
   project ownership notice. Check local `git status` before changing a checkout.
2. Prepare a [task claim](templates/TASK-CLAIM.md): target, authorization, scope,
   files, base revision, agent label, start time, next checkpoint and overlap.
3. For a multi-agent task, publish or communicate the claim in the already agreed
   public coordination home before overlapping edits. Do not create a new issue
   system or a second project-state ledger just to hold the same facts.
4. If a known owner overlaps, coordinate or work on disjoint files. A timestamp,
   abandoned claim or expired checkpoint never grants story permission.

## Before pushing

Commit your own changes; fetch the remote again. If its head moved, review the
new diff and rebase/merge without rewriting surviving public history. Rerun the
checks against the combined result. Never reset away another agent's edits or
force-push to make the conflict disappear.

A claim is advisory: Git history, branch protection and a re-fetch are the real
technical safeguards. Cross-repository changes are not atomic. Choose a safe
publication order (destination before links), record partial completion and give
the next agent exact outstanding revisions if interrupted.

## Finish, pause or recover

Mark a claim completed, blocked or handed off in its existing home and link its
receipt. Preserve failed attempts and recovery paths. When picking up a stale
claim, inspect the remote and ask the owner/author if required; do not assume a
silent agent lost ownership. Templates are intentionally empty: this rollout
creates no fictitious active agents or assignments.

[Back to start](START-HERE.md)
