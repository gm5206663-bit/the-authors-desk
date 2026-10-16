# Handoff and delivery

## Definition of done

- The requested artifact exists at its canonical home, with no competing state copy.
- Author-gated decisions remain unchanged unless explicitly ruled.
- Required checks ran at the delivered revision; failures, coverage and unrun
  checks are disclosed. Check exit codes directly, not through a misleading pipe.
- Sources/derivatives and manifests are synchronized where the local contract
  requires it. Inspect build side effects; do not assume every check is read-only.
- Changes are committed and pushed; remote revision is verified. If CI/Pages is
  pending, say pending and give its run, rather than claiming success early.
- A concise handoff states the next safe action and any blocker.

## Standard handoff

Use [HANDOFF.md](templates/HANDOFF.md). Required fields are Goal, Authorization,
Target, Base revision, Delivered revision, Files changed, Work completed,
Checks run, Known failures, Pending decisions and Next safe action.

For checks include command, working directory, actual status, coverage, revision
and evidence path/run. Say "not run" with a reason when appropriate. Do not put
an empty "all green" box over a required check you could not execute.

Publish task-specific handoffs in their existing local journal/handoff home. Use
a dated desk report for cross-account maintenance. Templates are not active
handoffs and should not be copied into every repository unfilled.

## Interrupted work

Preserve the partial diff and failed attempts safely; never leave an abandoned
checkout as the only home of managed work. Publish an authorized WIP branch or
public handoff with enough detail to recover, without fabricating completion.
Record which repositories were pushed and which dependent links remain pending.
Never push broken work to a protected release branch merely to satisfy a slogan.

## Resume check

Read the handoff, fetch its exact revisions, compare the remote for newer work,
recheck permissions/ownership and rerun the relevant baseline. A handoff is
navigation to evidence, not an exemption from checking today's state.

[Back to start](START-HERE.md)
