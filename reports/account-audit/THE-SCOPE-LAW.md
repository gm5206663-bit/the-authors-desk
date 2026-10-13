# THE SCOPE LAW
### What every gate in the house has in common — and why none of them said so
**Deep pass · 2026-10-11** · 15 repos cloned clean · every checker in the house run for real

---

## THE FINDING, IN ONE LINE

> **Every defect found in this pass is the same defect: a check that reports success while covering less than it claims.**

Not one of them is a broken check. Not one is a wrong threshold. Every one of them **runs, passes, prints a clean result — and quietly covers a smaller scope than the reader of that result will assume.**

This is the general form of a class the house already knew as a list of instances. Your own mistake ledger names them:

> **"Checkers that lie — a gate that can't fire, a rule gated on one fix's wording, a scanner that knows one project's filenames."**

Those are three instances. **This is the shape they share.** And until the shape is named, each instance gets fixed alone and the next one arrives in a new costume.

---

## THE FIVE INSTANCES

| # | The check | What it appears to cover | What it actually covered | What it reported |
|---|---|---|---|---|
| 1 | `grey-wolf/tools/style_gate.py` | the serial | `chapters/` — **6** files | ✅ `ALL HARD CHECKS PASS` |
| — | …while **10** chapters are published via `manuscript/` → `docs/` | | **4 chapters ungated** | ✅ green |
| 2 | `grey-wolf` + `kit` `style_gate.py` | 7 hard gates | **3** conditions; dialogue computed and printed but never consulted | ✅ `ALL HARD CHECKS PASS` |
| 3 | `soul-library/tools/sentinel.py` | 26 checks | **1** check without `--kit` | ✅ `1 pass / 0 warn / 0 fail` |
| 4 | `storyos-site` published `state.txt` | the stage's status | a stage that **fails** `verify_stage` (3 files drifted, one section missing) | ✅ `GATE: PASS (errors=0, warnings=0)` |
| 5 | `storyos-site/verify_stage.py` | the published site | **0 files** with no argument · **381 files** (mostly wrong) with `.` | ⚠️ `FAIL — 0 files checked` |

**Instance 5 is the tell.** Read that output literally:

```
VERIFY_STAGE: FAIL (0 files checked, 1 issues)
```

**The gate checked nothing and reported a verdict.** It failed — correctly — but for a reason that has nothing to do with the site. Anyone reading it learns that `agents.md` is missing; nobody learns that the site was never examined.

---

## WHY THIS CLASS IS WORSE THAN A BROKEN GATE

A broken gate fails. **You notice.** A scope defect *succeeds*, at a smaller scope, in the same voice it would use for the full one.

Compare:

| | Broken gate | Scope defect |
|---|---|---|
| Exit code | 1 | **0** |
| Output | `FAIL` | **`PASS`** |
| Badge | 🔴 red | **🟢 green** |
| Discovered by | anyone | **only by auditing what was covered** |
| Effect | blocks the work | **certifies work that was never checked** |

**The green badge is the danger.** A red badge costs a night. A green badge on an unverified artifact costs the credibility of every green badge you have ever shown.

And the house's whole public claim rests on that badge:

> *"every chapter machine-checked against canon before it lands here"* — the reading site
> *"every chapter machine-gated"* — the profile

**A green tick from a gate that covers 60% of the chapters is worse than no tick at all**, because it transfers confidence that was never earned.

---

## THE TEST THAT FINDS THEM

There is exactly one test, and it has three questions. Ask them of any check:

```
1. WHAT DID IT SAY IT COVERED?
2. WHAT DID IT ACTUALLY LOOK AT?     ← count the files. name the directory.
3. DOES THE OUTPUT DISTINGUISH THE TWO?
```

If the answer to (3) is no, **the check has a scope defect**, whether or not it is currently green.

### Applied to this pass

| Check | Says it covers | Actually looked at | Output distinguishes? |
|---|---|---|---|
| grey-wolf style_gate | "every chapter" (docstring) | `chapters/` — 6 files | ❌ no count printed |
| kit style_gate | "ALL HARD CHECKS PASS" | 3 of 7 gates | ❌ no gate list printed |
| sentinel | "sentinel:" | 1 of 26 | ❌ prints "1 checks" with no expectation stated |
| storyos `state.txt` | `GATE: PASS` | not verified | ❌ no verification reference |
| verify_stage (no arg) | "VERIFY_STAGE: FAIL" | 0 files | ⚠️ prints the count, but the verdict reads as being about the site |

**Note that the last one is half-right.** It prints `0 files checked` — the single most useful six characters in this whole pass. **Every check in the house should print that.**

---

## THE LAW

> ### THE SCOPE LAW
>
> **A check must declare the scope it actually covered, and must fail loudly when it could not cover its full scope.**
>
> 1. **Print the count.** Every gate prints how many files it examined and how many it expected.
> 2. **Print the coverage, not just the verdict.** `6 of 10 chapters · 3 of 7 gates` — never a bare `PASS`.
> 3. **Absence of scope is a failure.** If a gate cannot find its inputs, it exits non-zero and says *"I could not check X"* — it does **not** report a clean result for the part it managed.
> 4. **A gate with an optional mode states which mode ran.** `sentinel: 1/26 checks (kit not supplied — 25 checks DID NOT RUN)`.
> 5. **No gate reports `PASS` for a scope it did not declare.**

### Why rule 3 is the load-bearing one

Every instance above is a variation on one behaviour: **when the gate could not do its full job, it did the part it could and reported success.**

- The sentinel without `--kit`: ran 1 check, said `0 fail`. It never said *"25 checks did not run."*
- The style gate: measured dialogue, printed it, and never put it in the pass condition. The measurement was **right there in the output** and did not affect the verdict.
- `state.txt`: asserted `PASS` with no reference to any check that could have produced it.

**A gate that cannot run its checks must say so as loudly as it would say `FAIL`** — because from the outside, `I could not check` and `I checked and it is fine` are indistinguishable. That is the whole disease.

---

## THE SELF-TEST CONNECTION

The house already has the right instinct here, and it is the reason this law is a **generalisation**, not a new idea.

> **A gate that has only ever been seen to pass is a gate nobody has tested.**
> **If you add an eighth gate, add an eighth fixture.**

The selftest proves **a gate can fail**. It does *not* prove **a gate can fail about the right thing**. Those are different properties:

| Property | Proved by | Which gates have it |
|---|---|---|
| The gate can fail | selftest (defect injection) | 7 repos ✅ |
| The gate looks at the right thing | **scope assertion** | **0 repos** ❌ |

**The house built the first and not the second.** Every finding in this pass is in the second column.

### The missing fixture: a scope fixture

A selftest proves a gate catches a bad input. A **scope fixture** proves a gate *examines the right inputs*. They are different tests:

```
SELFTEST (exists):    inject a defect  → does the gate fail?
SCOPE TEST (missing): remove an input  → does the gate say so?
                      add an input     → does the gate see it?
```

**Concretely for this house:**

- Remove `manuscript/` → does the gate complain, or pass on `chapters/`? *(currently: passes)*
- Add a chapter to `manuscript/` only → does the gate notice it is ungated? *(currently: no)*
- Run sentinel without `--kit` → does it say 25 checks did not run? *(currently: `1 pass`)*
- Point `verify_stage` at an empty directory → does it say "0 files checked, verdict withheld"? *(currently: reports `FAIL` about `agents.md`)*

**Every one of those is a five-line test.** None of them exist.

---

## WHAT TO BUILD

### 1 · A coverage line in every gate

One line, printed before the verdict, every time:

```
COVERAGE: 6 of 10 chapters (chapters/=6, manuscript/=10, published=10) — MISMATCH
COVERAGE: 3 of 7 hard gates enforced (unwired: script, digits, placeholders, marker)
COVERAGE: 1 of 26 checks (kit not supplied — 25 DID NOT RUN)
COVERAGE: 0 of 121 files (root not found: <cwd>/storyos-site)
```

That single line would have surfaced all five defects in this pass **on the day they appeared.**

### 2 · Make the scope a declared constant

Each gate declares what it expects to cover, and compares:

```python
EXPECTED_CHAPTER_DIRS = ['chapters/', 'manuscript/']
EXPECTED_GATES = 7
EXPECTED_CHECKS = 26

# coverage is not a nicety — it is the pass condition
if covered < expected and not allow_partial:
    print(f"COVERAGE INCOMPLETE: {covered} of {expected}. Verdict withheld.")
    sys.exit(1)
```

### 3 · An independent scope audit

The house already knows the principle — `soul-library/tools/sentinel.py` is described as an
*"independent drift scanner [that] does not trust the project's checker"*, and the guide notes
*"two checkers disagree is the most honest alarm."*

**Apply it to scope.** A check that reads the same directories as the gate will agree with the
gate. An independent audit reads **what is published** and asks whether the gate saw it:

```
published: docs/chapter_10.html   (live, HTTP 200)
gated:     chapters/ ends at 06
→ 4 PUBLISHED CHAPTERS HAVE NEVER BEEN GATED
```

**That check is about twenty lines, and it would have caught the biggest defect in this pass.**

---

## THE META-LESSON

The house's eight meta-lessons are the shapes its mistakes take. **This pass adds a ninth**, and
it is the smallest and most general of them:

> **9 · The scope defect** — a check that passes while covering less than it claims. The cure is
> a declared scope, a printed count, and a loud failure when the full scope could not be reached.

And one more, about **this pass specifically**, which the house's own law demanded and which
paid off twice:

> **Before logging a defect, try to disprove it.**
>
> Twice in this pass, the agent read an exit code through a pipe and reported a false failure —
> `supergirl`'s selftest "failing 2 checks" and `storyos`'s gate "exiting 0 with 25 failures."
> Both were `PIPESTATUS` artifacts. Both were disproved by re-running without a pipe and reading
> the real code. **The gate was right both times; the measurement was wrong.**
>
> And a third: a token left in `.git/config` by the agent's own clone method produced two
> secret-scan failures that did not exist. **The clean clone showed 53/53.**
>
> *A checker can prove false presence. It cannot prove false absence. And an agent can prove
> false absence too — if it does not re-measure.*

---

## RECEIPTS

| Finding | Where it lives | Status |
|---|---|---|
| Gate reads drafts, not published text | `grey-wolf/AUDIT_2026-10-11_GATE_SCOPE_AND_LIVE_EDGE.md` | ✅ pushed |
| Dialogue floor measured, not enforced | `grey-wolf/GATE_GAP_DIALOGUE_2026-10-11.md` | ✅ pushed, corrected in place |
| Sentinel runs 1 of 26 without `--kit` | measured this pass, not yet filed | ⏳ needs a ruling |
| Published stage is stale; state.txt says PASS | `storyos-site/AUDIT_2026-10-11_STALE_STAGE_AND_SCOPE.md` | ✅ pushed |
| `verify_stage` scope by invocation | same record, §"the quieter defect" | ✅ pushed |

**Class sweep performed:** every repo in the house checked for published-greater-than-gated.
**Only `soul-land-2-the-grey-wolf` is affected.** The kit's System Cheat is aligned at 4/4/4.
Every other repo has no manuscript/publish split. *One instance, not twelve — verified, not assumed.*

**Every gate in the house was run for real:** 29 checks across 15 repositories. Most non-zero
exits were usage messages requiring arguments, not failures — **checked one by one, not assumed.**

---

*Written 2026-10-11. This is the general form of a class the house already had three instances of. The instances were fixed; the shape was not named. Now it is.*

---

# RESOLUTION — 2026-10-11 — INSTANCE 1 FIXED, AND A SIXTH INSTANCE FOUND

Instance 1 in the table above — *grey-wolf `style_gate.py`: appears to cover
the serial, actually covered `chapters/` — 6 files* — is now repaired. Doing
the repair found one more instance of the same law, and one more shape of it.

**Instance 6 — the gate that passes empty.** The old gate ended with:

```python
if not paths: print("(no chapters yet — the gate passes empty)")
```

Delete the directory and the gate reported success. Not a small scope —
*zero* scope, reported as green. This is the purest form of the law: a check
whose coverage can fall to nothing without a word of complaint. The cure is
now the first rule of the rebuilt gate: **0 files found is a hard failure.**
A check that executes nothing verifies nothing.

## The repair, and what it cost to trust it

Instance 1 turned out to be worse than the table said. It was not that the
gate read the wrong directory — it was that **four published chapters had no
author edition for it to read.** The pipeline ran one way (`chapters/` →
`manuscript/` → `docs/`) and nobody ever noticed four chapters entering it
below the join. The gate could not have seen them at any scope. A scope fix
that only repoints a directory would have missed this entirely.

Both ends are now gated, a `COVERAGE:` line is printed by every gate, an
unaccounted-for chapter fails in either direction, and a reader edition that
has drifted from its author edition fails as the Two-Copies defect.

## What the fixture caught

The fixture — seven tests, each breaking the tree on purpose — was written to
test the *gate*. It caught two bugs, and **both were in the fixture and in my
own hands, not in the gate**: a test that removed the wrong file and so could
not fail, and a `cp`/`rm` pair that deleted a published manuscript file
outright. No gate defect was found, because the gate was right.

That is the argument for the fixture in one line: *it does not test the gate;
it tests your belief that the gate works.* Belief was wrong twice in one
afternoon.

## Applies to

- `soul-land-2-the-grey-wolf` — repaired, pushed `39a26e9`, live.
  Record: `REPAIR-2026-10-11-DIALOGUE-FLOOR-AND-GATE-SCOPE.md`
- `soul-land-universal-kit` — **repaired, pushed `77916ba`, live.** Same gate,
  same defect, ported repair: floor enforced, both ends covered, coverage
  declared, fixture attached. Its content needed nothing — 4/4/4 aligned and
  every chapter already above the floor. `soul_land_system_cheat` is the
  first of the eleven remaining gate-script repos to carry the fixed file.
- `storyos-site/verify_stage.py` — instance 5, still open: no argument means
  **0 files** checked and the tool still reports.
