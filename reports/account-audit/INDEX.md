# THE HOUSE LIBRARY — collected
**Built 2026-10-11.** Four documents, collected from 18 repositories and 562 method-bearing files.

---

## The four documents

| Document | What it is | Size |
|---|---|---|
| **[THE-COMPLETE-GUIDE.md](THE-COMPLETE-GUIDE.md)** | **The method, organised for use.** Nine parts: the five decisions · **twelve kinds of fan fiction** · the craft · canon discipline · the gates · the chapter loop · structure and handoff · the mistake atlas · quick-reference cards. **This is the one to read and keep open.** | ~9,500 words |
| **[THE-MISTAKE-ATLAS.md](THE-MISTAKE-ATLAS.md)** | **Every mistake ever paid for, organised by *class* rather than by project.** Twelve recurring classes, 109+ catalogued rows, every author strike quoted verbatim, and the law each one produced. | ~5,000 words |
| **[THE-COMPLETE-METHOD.md](THE-COMPLETE-METHOD.md)** | **The raw collection.** Every law, gate, rule, pattern and lesson, gathered from all seven places it was written down, marked ⬛ universal / 🟦 franchise / 🟥 serial-specific. Includes the source map and the contradictions found while collecting. | ~11,500 words |
| **[THE-SCOPE-LAW.md](THE-SCOPE-LAW.md)** | **THE DEEP FINDING.** Every gate defect in the house is the *same defect*: a check that reports success while covering less than it claims. Five instances, one shape, and the law that closes it. **Read this one first.** Now carries the resolution of instance 1, the sixth instance (the gate that passes empty), and what the new fixture caught. | ~3,700 words |
| **[REPAIR-2026-10-11-DIALOGUE-FLOOR-AND-GATE-SCOPE.md](REPAIR-2026-10-11-DIALOGUE-FLOOR-AND-GATE-SCOPE.md)** | **THE FIRST REPAIR UNDER THE SCOPE LAW.** Four published chapters had no spoken line; four more were published with no author edition and had never been gated. What changed, what it cost, and what was deliberately left alone. Pushed `39a26e9`, live. | ~1,800 words |
| **[AUDIT-2026-10-11.md](AUDIT-2026-10-11.md)** | **The account audit that started this.** Repo-by-repo state, security scan, and the action plan. | ~2,400 words |

Plus `audit.json` — machine-readable repo metadata for all 18 repositories.

---

## Read them in this order

0. **THE SCOPE LAW** — the deep finding; why every gate in the house is green and one of them is wrong
1. **AUDIT** — what state the account was in
2. **THE COMPLETE GUIDE** — the method, usable
3. **THE MISTAKE ATLAS** — why each rule exists
4. **THE COMPLETE METHOD** — the full collection and source map

---

## The three findings that shaped all four documents

**1. The universal method existed — but was not in the repo that publishes it.**
`how-to-write-fanfiction` claims *"works for any fandom."* It teaches **0 of the 9 core universal teachings** (five failures, five registers, seven gates, twelve locks, anchor table, handoff law, style patterns, scope law, mis-measurements) and carries **941 project-specific term hits** — mostly one serial's power-system rules. The method was scattered across a vault, four kit copies, and an archived repo.

**2. The CI was blocked by a token scope, not by a method problem.**
Two repos carry a written, ready workflow with the note: *"held here until a workflow-scoped token exists."* Thirteen repos have gate scripts. One has CI. The workflow that was waiting is now armable.

**3. The house's own hardest discipline was already implemented — in seven places, running nowhere.**
`selftest.py` exists in seven repos. It tests the gates against known-bad input. It has never been wired to a runner.

---

## The twelve mistake classes

*The house kept its mistakes by project. Filed by class, the same eight shapes kept returning.*

| # | Class | The cure |
|---|---|---|
| 1 | Assert-without-verifying | read before asserting; try to disprove your own claim |
| 2 | Inventing instead of sourcing | canon-first; label every invention `[design]` |
| 3 | Centering the OC in canon's house | the Multi-Panel Law; scope canon's superlatives |
| 4 | Prose register drift | the Plain-Scene Law; measure, never eyeball |
| 5 | Two-copies rot | one authority per fact; derive, don't type |
| 6 | Checkers that lie | selftest; scope the gate; calibrate thresholds |
| 7 | Cleanup that cuts the wrong thing | byte-verify **before** removal |
| 8 | Misreading the ask | identify the project from its own contents |
| 9 | Process and state failure | commit first, then rebase |
| 10 | Handoff failure | one status source; stamp the stale |
| 11 | Account and publishing failure | verify public surfaces like any other copy |
| 12 | Documentation drift | the Two-Copies Law applies to docs too |

---

## The seven rules that carry the most weight

> **A chapter is not done when it reads well. It is done when it has been checked.**

> **A check that executes nothing verifies nothing.**

> **A gate that has only ever been seen to pass is a gate nobody has tested.**

> **A fact maintained in two places will be wrong in one of them.**

> **A sentence that must be read twice is wrong, no matter how lawful its words.**

> **When the author says "go see how canon is written," GO SEE.**

> **Consistency > convenience. Causality > coincidence. Character agency > author control. Earned progression > arbitrary escalation. Consequences > spectacle. Truth > memory.**

---

**Added 2026-10-11 (later):** [`THE-ACCOUNT-WHOLE.md`](../scope-sweep/THE-ACCOUNT-WHOLE.md)
— a sweep of all 18 repositories, 443 chapters and 77 gate scripts. Five more
instances of the Scope Law found and repaired; one apparent defect (eleven
speechless chapters in *Devouring Dragon*) proved to be the serial's own
no-voices law. Raw evidence: `scope-sweep/INVENTORY.md`, `INVENTORY2.md`,
`gate_runs.txt`, `sweep.json`.

**Added 2026-10-11 (last):** [`REPAIR-2026-10-11-HOUSE-GATE.md`](REPAIR-2026-10-11-HOUSE-GATE.md)
— the house gate ships (`soul-land-universal-kit` `1b3f71e`): one gate for every
book in the account, a written exemption for Devouring Dragon's no-voices law,
and a fixture that shrinks its scope four ways. The first account run's numbers
were discarded as contaminated by the gate's own five bugs; the verified run was
**24 books · 71 hard failures · 0 scope refusals**, and after §8's repair sweep
the same gate reads **17 hard failures · 0 scope refusals**. Raw:
`scope-sweep/house_gate_2026-10-11.txt` (re-run, post-repair).

**Added 2026-10-11 (control centre):** [`scope-sweep/control-centre/`](../scope-sweep/control-centre/)
— the account layer, pushed to `soul-land-universal-kit` (`24edc4b`, `215897a`).
Six detectors over every book in one run; coverage declared, evidence carried,
stable ids, fingerprinted baselines so runs report NEW / FIXED / STILL OPEN.
Read `11_CONTROL_CENTER.md` first: it records the nine bugs the system found in
itself (the eighth: the dupes detector counting a book's own published copy as a
second place — 61 of 66 NEW findings in one run; the ninth: the housekeeping walk
reporting files this session had just created itself) — including 1,034 hard findings on its first account run of which roughly
half were its own mistakes, none of which were reported anywhere until fixed.
