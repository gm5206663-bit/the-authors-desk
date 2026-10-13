# CLEANUP CLOSE — 2026-10-13

**The mandate (verbatim):** *"please do cleanup, make everything clear and clean and readble,
synthetic and natural and organised everything is tooo mess and others things, organise
everything completely"* — with the standing law: **nothing may be lost; history moves, it does
not vanish.**

**Pins after this pass:** kit **`de097b1` → `d8fa297` → `4c676a9`** · how-to **`4ebc1f8`**
(lane 5 earlier the same day: kit `2517d58`, how-to `c9f4035` — untouched by this pass).
Everything below verified live on the remote via raw fetch.

---

## What was wrong when the pass started

- The kit's front door was a 398-line **append-only log** (the README was mostly ~20 dated
  "ADDITION — …" sections); STATE.md said *"read this first"* while stale since 2026-10-07.
- `PROJECTS.md` carried a **wrong label** — the `soul_land_new/` row read *"Tianyu — DROPPED"*,
  but that tree is the **earlier Lan Shen build** (its `bible/PROTAGONIST.md` is author-given
  2026-09-15) — plus pre-measure totals.
- **Eight root folders had no README** (CODEX, Miraculous_Project, SL_ARCHIVE,
  Soul_Land_5_Project, adaptive_prodigy, docs, tools, _archive).
- The kit's own **register claimed a guarantee that never ran** — generated from inside the
  repo, it reported *"0 of 0 chapter-bearing trees"*: vacuous, not verified. `ship_chapter.py`
  still parsed the old README; `AGENTS.md` pointed agents at the **deleted** private Fire
  Phoenix repo; the workspace root held a drifted **second copy** of the corpus ledger.
- Live drift the detectors had skipped: Grey Wolf's README said *"six chapters / Ch7 next"*
  while its own panel says **v5.4.3, Ch10, 10 IN SYNC**; the how-to scoreboard was stale
  (219/928K+, Grey Wolf 6, Lan Shen 2, Stark Heir 4).

## What was done

| Target | Change |
|---|---|
| Kit `README.md` | **one-screen cockpit** — where to read, every serial with state + measured counts, the method/records map, the house rules. The old README moved **verbatim** → `HISTORY.md` (with an addendum correcting the Tianyu row) |
| Kit `STATE.md` | retitled **"the dated sweep record"** + pointer to the cockpit; content untouched |
| Kit `PROJECTS.md` | `soul_land_new/` row corrected to **"Lan Shen — the earlier build"** (dated receipt in the row); totals now point at `REGISTER.md`; Fire Dragon Lizard moved to Kept (shipped); exact figures |
| 8 folders | each given its own **README** (what it is, what's inside, the law, where next) |
| Register honesty | `account_checks._repos` taught that a one-repo root is a repo; kit register now reports **33 of 33 trees accounted** (28 under books, 5 classified sightings) — regenerated |
| `tools/ship_chapter.py` | rewired to the cockpit row (Devouring Dragon chapter **and word** figures, both measured from the book); mirrors checklist updated (HISTORY.md receipts, register regen) |
| `AGENTS.md` | dated amendment: the FP private-repo boundary is history — the live tree is in-repo; cockpit/history split; register fix |
| `SARA.md` | newest-truth standing note at the top (nothing below edited) |
| Grey Wolf README | corrected to its panel's truth (10 chapters, Ch10 live edge, v5.4.3 Canon-Strict) |
| `/home/user` | `PROJECTS.md` → **pointer** (the ledger's one copy lives in the kit); new **`reports/`** gathers the loose records: `account-audit/` (was github-audit), `scope-sweep/`, `ci-rollout-2026-10-12/` (was staged), the lane close reports; internal paths updated; revoked `.ght.old*` removed |
| How-to repo | verified structurally clean (18 relative links, 0 dead); **number drift fixed** — shelf **230 ch / 955,737 w**, Grey Wolf **10 ch v5.4.3**, Lan Shen **7 ch / 32,211 w** (V1 epoch deleted 2026-10-12, retrievable from kit history), Stark Heir **5 ch / 27,673 w**, superseded Grey Wolf spec figures corrected (Spirit Connection 200–300, body 100–150 kg, Ring Veil true colour) |
| Desk | new layout line (where everything lives) + cleanup entry; register figures refreshed to measured |

## Gates run (all green, in the same turn as the edits)

- kit `selftest.py` — **PASSED** · kit `account_selftest.py` — **PASSED**
- receipts detector over all 16 books — **16 of 16 clean** (no drift)
- dead-link detector — **0 dead of 1,988 documents**
- D1 mirror — **byte-identical** (`diff -rq` empty)
- register — **33 of 33** chapter-bearing trees accounted
- remote verification — every key string fetched back from `raw.githubusercontent.com`

## Found while cleaning (and fixed)

1. **Grey Wolf README drift** — "six chapters" vs panel's 10. It had escaped the receipts
   detector because that detector **skips lines over 400 chars** (the status line is one long
   line). Blind spot noted, not changed — the fix is a fix to the *book*, not the gate.
2. **How-to scoreboard drift** — the guide's own recurring class ("numbers must be
   re-measured"): five figures were stale.
3. **The register's vacuous guarantee** — a coverage line is a claim; this one had never been
   tested from inside a single repo. Now it is, and it holds.
4. **Two cockpit descriptors** corrected against each project's own self-description —
   Devouring Dragon carries its true setting (*1,000 years after SL1*; it had been untagged/
   conflicting with `PROJECTS.md`), and the Golden Lion one-liner now matches its status panel.

## Deliberately untouched

- **Supergirl's 70 over-cap sentences** — author-blocked; the standing ruling (compressed
  voice) stands; no repair applied.
- **The detector's >400-char skip** — design choice, flagged here rather than changed.
- **Author-space items** — lan_shen A1 arc re-cadence + A6 renumber, Fire Phoenix V2 numbering
  decision: both on `THE-AUTHORS-DESK.md`, not self-healed.
- **Every text** — moves only. The only deletions in this pass: the revoked `.ght.old*`
  credential files and the drifted duplicate ledger copy at the workspace root (its one home
  is the kit; the pointer says where).

*One sentence for the author: open `README.md` in the kit and you see everything the workshop
is, on one screen — where to read the fiction, every serial with its live count, the rules of
the house, and one door into each folder; everything else is dated history, kept, in its
place.*
