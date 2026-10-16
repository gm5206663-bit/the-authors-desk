# Agent guidance rollout — 2026-10-16

## Goal

Give a fresh agent one safe starting point, explicit source/permission routing,
resumable handoffs and tested guidance across the public account.

## Authorization

The author asked what else could guide other agents. The offered plan covered a
single starting page; separation of rules from changing state; task routing;
permissions; handoffs; coordination; worked examples; onboarding exercises;
security/evidence handling; and automatic guidance checks. The author replied
**“Do”** (2026-10-16). This authorizes the guidance rollout, not a story ruling.

## Target

Cross-account onboarding lives in `the-authors-desk/agents/`. Each repository
keeps a root `AGENTS.md` with navigation and local scope. Existing kit and
Supergirl contracts remain intact beneath a short navigation block.

## Base revision

| Repository | Base |
|---|---|
| adaptation-talent | `820a51f` |
| gm5206663-bit | `2f8562c` |
| how-to-write-fanfiction | `6207688` |
| mcu_eternal_fanfic | `7e45058` |
| pokemon-adaptation | `0e5bda4` |
| sara | `03ccb41` |
| soul-land-universal-kit | `1849ce8` |
| soul-library | `a1bfaad` |
| stark_heir | `950087f` |
| storyos-site | `867b03c` |
| supergirl-adrian-vale | `6372278` |
| the-authors-desk | `1973bf5` |
| the-universal-storyline-creation | `0684bf3` |

Fresh tokenless clone URLs were used; pre-existing local modified checkouts were
not reset or overwritten. The remote heads will be checked again before pushing.

## Delivered revision

At this receipt's initial write, implementation is prepared and locally checked;
publication and asynchronous CI are not yet claimed complete. The publication
addendum will record exact pushed revisions and remote results.

## Files changed

- Desk: root agent entry, `agents/` guide/registry/index/templates/examples/exercises,
  `tools/agent_check.py`, `agent_selftest.py`, `agent_sources.py`, index renderer,
  pinned `agent-guidance` workflow, README and Pages navigation, this receipt.
- All other repositories: root agent entry; existing local contracts preserved.
- Sara: README link and dated current-state loading note in the guided loading
  page. Canonical identity/profile/edition bytes are not edited; manifest refreshed.
- Adaptation Talent and writing guide: manifest entries for the new agent file.
- Profile: small local-entry/account-start pointer, not another state ledger.
- Supergirl: only the AGENTS checksum is refreshed, after verifying its old hash.
  Acceptance hashes and all unrelated checksum rows are left untouched.
- Kit: the intentional method-tool mirror is synchronized and its parity added
  to regression CI; see the maintenance defect below.
- Shelf: sentinel output refreshed after the mirror repair, with all checks passing.

## Work completed

The [starting page](../agents/START-HERE.md) links a task/permission workflow,
authority/current-state classification, source/security rules, coordination and
delivery procedures. A [single registry](../agents/registry.json) owns repository,
project, command and exercise references; the readable repository index is
generated from it and checked against it. There is no copied chapter/rank table.

Five templates cover handoff, advisory task claim, decision, source and executed
check receipts. They are empty templates, not fabricated active assignments.
Three worked examples distinguish a real navigation repair, a prepared ruling
brief and an explicitly hypothetical authorized chapter pipeline. Eight onboarding
exercises require live evidence; structural tests do not claim to grade an
agent's comprehension or literary judgment.

The validator checks guidance structure, links, route identity, safe paths,
command script existence and evidence references. It never executes registry
commands. Full-account mode refuses missing/extra checkouts, prints actual HEADs
and flags modified working trees. The public-source preparer refuses stale
nonempty destinations, retains the triggering desk checkout, clones tokenlessly
and treats failed clones as execution failures. Scheduled/PR/push CI checks
cross-repository dependencies, not just local documentation.

### A prior maintenance defect found and repaired

The preceding maintenance pass updated the released kit tools without updating
the intentional `SOUL_LAND_WORKSPACE/kit` mirror. A fresh baseline at `1849ce8`
reproduced the shelf sentinel's D1 failure: 25/26 checks passed. That defect was
agent-side, not a new story decision. Eight changed/missing tool files are now
copied from the released kit into its existing mirror; no unique file is deleted.
The two full kit trees compare equal excluding Git/Python cache directories.

Kit regression CI now triggers on both kit trees and compares them before running
tests. The shelf sentinel then passes **26/26**, and continuity lint passes. The
mirror remains intentional; this rollout does not create a new doctrine copy.

## Checks run

Local executed checks:

- Agent guidance regressions: **44/44 passing**, including clean/broken registry,
  missing sources, stale generated index, unsafe paths, missing permission fields,
  handoff validation, clone failure and no registry-command execution.
- Local guidance check and full sibling-account path check: zero errors across
  all declared public repositories. Initial working-tree checks are explicitly
  marked modified; post-push fresh-source checks will be recorded separately.
- Existing desk navigation: zero errors; eight regression tests pass.
- Adaptation Talent: 57 manifest files, 180 relative links and holder-count gate pass.
- Sara: 30 manifest entries, 68 relative links, existing ledger shape pass.
- Writing guide: 36 manifest entries and 101 relative links pass.
- Kit detector selftest passes; intentional kit mirror parity passes.
- Shelf sentinel selftest passes; live sentinel 26/26 and continuity lint pass.
- MCU Eternal and Stark Heir: verifier selftests and current project verifiers pass.
- Pokemon: gate selftest 24/24. This is not a drafting unlock.
- Universal storyline toolkit selftest passes.
- StoryOS: existing pinned-baseline wrapper exits 0 while retaining its four known
  Dragon Prince stage issues. This is not a clean stage report.
- Supergirl: existing pinned-baseline CI wrapper exits 0; raw selftest is **51/53**,
  with two acceptance-fixture failures reproduced unchanged in a clean baseline.
  Those results are not called a passing raw selftest.

Remote CI/Pages and post-push public-source validation are pending at initial
publication; no uncompleted run is described as successful here.

## Known failures

1. Supergirl baseline selftest has two failures tied to seven pending chapter
   acceptance hashes. The clean base checkout reproduces them. No acceptance hash,
   test expectation or CI baseline was weakened or changed by this rollout.
2. Supergirl's broad `CHECKSUMS.sha256` has 47 unrelated pre-existing missing/hash
   mismatches. Only the changed agent-entry row was refreshed, after checking its
   prior hash. This is not a claim that the whole historical checksum file verifies.
3. StoryOS retains the existing four pinned stage issues.
4. Pokemon's README, ruling records and stage-0 workflow conflict about lifecycle.
   The route names the conflict and stops dependent drafting; it does not choose
   which author interpretation wins.
5. Path existence and green guidance tests do not verify story quality, canon
   truth, permission meaning or private-account completeness.

## Pending decisions

No author-gated story decision is changed: Supergirl ruling/acceptance boundaries;
kit AT pointer choice; write-forward target; Fire Phoenix V2 numbering; Lan Shen
re-cadence/A6; MCU Order. Frozen projects remain frozen. Pokemon lifecycle
reconciliation remains a source/authority question, not an invented unlock.

## Next safe action

Publish the destination guide first, then the scoped entry links and mirror fix;
verify the public sources and CI; append exact revision/run evidence. Future
agents should begin at [START-HERE](../agents/START-HERE.md), select the named task,
load local authority and state, and leave a filled handoff in the task's existing
canonical home. No new story target is selected by this handoff.
