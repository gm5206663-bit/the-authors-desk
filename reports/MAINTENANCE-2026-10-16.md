# Account maintenance — 2026-10-16

## Mandate and boundaries

Author instruction: **“Do more work more do how much you can”** (2026-10-16).
This pass strengthens management, navigation and verification. All repositories
remain public and unarchived. No story prose was edited, no surviving history
was rewritten, and no author-gated ruling was chosen.

## Measured starting state

Authenticated owner inventory: **13 public repositories, none archived**.
Fresh clones agree with the earlier corpus measurement: **24 registered books ·
377 chapters · 1,624,963 words · 30,865 spoken lines**. The Control Centre
reports **70 hard findings** (all Supergirl `over60`) and **242 advisories**:
234 repeat-across, four sightings, three orphan-work, one dialogue exemption.
Housekeeping covers 13/13 repositories; two-homes covers 377/377 chapter files
with no finding. These are measurements, not a claim that every story passes.

## Defects found and repaired

1. **The desk's actual Pages front door still said twelve.** Both the subtitle
   and pill disagreed with the thirteen-repository account. Fixed to thirteen;
   added Sara's reading-page link and this maintenance receipt.
2. **The stale-claim detector did not recognize repository-count claims.** It
   already scanned HTML, but its pattern covered only canonical book totals.
   Added narrowly scoped desk/profile front-door checks, handling spelled-out
   counts, digits, hyphenated wording and inline markup. Six new regressions
   prove stale counts fire, matching counts stay quiet, and history/prose are
   not treated as current account claims. The before-fix scan reproduces two
   findings; after the page fix, both disappear.
3. **The scheduled sweep could silently lose scope.** The old clone loop
   printed clone failures and carried on, and discovery read only one API page.
   The new public inventory paginates, validates names/owner/public visibility,
   refuses empty or duplicate inventories and existing destinations, records
   exact HEADs and fails on any unsuccessful clone. Fourteen offline tests.
4. **`|| true` could hide checker crashes as ordinary findings.** The sweep now
   captures the real status and validates completion markers, report artifacts,
   detector coverage and finding/status consistency. Known findings still do
   not turn a completed reporting run red; incomplete execution does. Twelve
   offline evidence tests cover both paths.
5. **The measuring machine had no automatic regression workflow.** Added
   `control-centre-tests` to the kit, triggered by edits to its tools and sweep
   workflow. It runs the detector, inventory, evidence, live gate, scope fixture
   and kit-verifier suites. Current detector suite: **50 passing checks**
   (44 before this pass, including the clean-account check; six added).
   The desk's older dated “43 selftest cases” record is left as history, not
   rewritten. This receipt records the newly measured count.
6. **The desk had no self-check.** Added a dependency-free navigation/map check,
   eight regression tests and a pinned, read-only verification workflow. Current
   README/Page counts must agree with `repos.txt`; the current report index's
   local links must resolve. Historical report bodies are not reinterpreted.
7. **Three verification workflows used mutable action tags and implicit
   permissions.** Adaptation Talent, Sara and the writing guide now pin checkout
   (and setup-python where already used), disable persisted checkout credentials,
   set `contents: read`, cancel superseded same-ref runs and cap jobs at ten
   minutes. Their verification commands and story standards are unchanged.

## Published implementation

| Repository | Commit | Change |
|---|---|---|
| `soul-land-universal-kit` | `1849ce8` | discovery/evidence hardening, six detector regressions, regression CI, operating contract, README link |
| `adaptation-talent` | `820a51f` | hardened workflow and matching manifest |
| `sara` | `03ccb41` | hardened workflow; all 29 manifest entries and ledger gates unchanged |
| `how-to-write-fanfiction` | `6207688` | hardened workflow and matching manifest |
| `the-authors-desk` | this receipt's commit | corrected Pages, Sara link, current maintenance links and desk CI |

Adaptation Talent's workflow change first reached GitHub as `627fc6f` without
its refreshed manifest; the existing check correctly detected the mismatch.
Immediate follow-up `820a51f` refreshes the hash, passes both local gates and
preserves history. No force-push was used.

## Verification

Local suites passed: 50 Control Centre checks; 14 inventory tests; 12 evidence
tests; live-book gate selftest; scope fixture (seven perturbations caught, zero
missed); kit verifier selftest; eight desk regression tests. Adaptation Talent:
56 manifest files, 175 local links and holder-count gate pass. Sara: 29 manifest
entries, 62 local links, 36 dated ledger entries/34 signed lines pass. Writing
guide: five defect classes caught, clean demo passes, 97 relative links and 35
manifest files pass.

### Remote verification addendum

Completed **success** on the exact implementation revisions:

| Repository / check | Run |
|---|---|
| Kit — `control-centre-tests` | [38846917880](https://github.com/gm5206663-bit/soul-land-universal-kit/actions/runs/38846917880) |
| Kit — dispatched hardened `account-sweep` | [38846974266](https://github.com/gm5206663-bit/soul-land-universal-kit/actions/runs/38846974266) |
| Desk — `verify` at `c555cf8` | [38846976182](https://github.com/gm5206663-bit/the-authors-desk/actions/runs/38846976182) |
| Adaptation Talent — `verify` at `820a51f` | [38846899025](https://github.com/gm5206663-bit/adaptation-talent/actions/runs/38846899025) |
| Sara — `verify` at `03ccb41` | [38846915460](https://github.com/gm5206663-bit/sara/actions/runs/38846915460) |
| Writing guide — `verify` at `6207688` | [38846915523](https://github.com/gm5206663-bit/how-to-write-fanfiction/actions/runs/38846915523) |

The hardened sweep actually cloned all 13 public repositories, validated both
checker evidence sets and uploaded its evidence successfully. Its broad house
gate declared 39 discovered books, 29 hard failures and 544 warnings; that is
**not** the Control Centre's registry scope. Nothing was automatically repaired.
The completed reporting workflow is not a claim of zero defects.

A second public-only discovery/clone rehearsal also completed 13/13 with exact
HEAD receipts. The fresh authenticated Control Centre report agrees with the
starting corpus: **24/377/1,624,963/30,865; 70 hard/242 advisory**, no two-homes
or stale claims, 3,115/3,115 documents checked for links with no dead-link
finding, housekeeping 13/13 and enforcement 11/11. (Coverage reflects the
snapshot at `c555cf8`, before these audit artifacts were added.)

**Chapter preservation: 377/377 registered live chapter files hash-identical**
between the starting checkout and the final public rehearsal; per-file SHA-256
receipts are included. All summary counts and finding-kind totals are unchanged.

Seven reading sites returned HTTP 200: desk, Adaptation Talent, writing guide,
Sara, kit, StoryOS and Soul Library. The desk's live HTML contains the thirteen
count and Sara link and no old “twelve repositories” pill. Desk Pages at
`c555cf8` completed successfully. The kit's separate Pages job for this pass was
still queued at the recorded CI snapshot; its existing site returned 200 and
no kit reader-page source changed. That queued deployment is not reported as
completed.

Durable evidence: [`account-audit/maintenance-2026-10-16/`](account-audit/maintenance-2026-10-16/)
contains the three-format final audit, clone inventory/HEADs, before/after stale
claim evidence, test transcripts, chapter-integrity hashes, CI status snapshot
and live-site checks, with SHA-256 checksums. Read its index for snapshot limits.

## Operating and recovery limits

The new [sweep operating contract](https://github.com/gm5206663-bit/soul-land-universal-kit/blob/main/SOUL_LAND_UNIVERSAL_KIT/tools/SWEEP-OPERATIONS.md)
explains complete-with-findings versus incomplete execution, replay commands,
public-only discovery, exact per-clone HEADs and artifact retention. Shallow
clone tarballs are working snapshots, **not full-history backups**. The broad
standalone house gate and Control Centre have different discovery scopes; their
verdict counts must not be conflated. No recovery/backup completeness is implied
by a green measurement workflow.

## Still the author's call

Unchanged: Supergirl A/B/C-or-edit; kit AT pointer choice (a)/(b); write-forward
serial name; Fire Phoenix V2 numbering; Lan Shen re-cadence/A6; MCU Order sign-off.
No book was chosen, renumbered, re-cadenced, unfrozen or automatically repaired.
