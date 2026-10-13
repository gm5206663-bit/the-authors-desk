# THE AUTHOR'S DESK

**Every decision that is yours, on one page — 2026-10-12 · updated 2026-10-13.**
Nothing here is broken machinery. It is the set of things where the house rule
says *the author decides, not the agent*. Each item carries its evidence and what
happens if you say either way.

**Where things live (organised 2026-10-13; published the same day):** everything on this
desk lives in this repository and only here — this file · `repos.txt` (the account map,
twelve repositories) · `THE-COMPLETE-REGISTER.md` (the measured account register) ·
`reports/` (close reports · account audit · scope sweep · CI rollout). The working machine
keeps pointers only. The projects live in **`soul-land-universal-kit`**; its `README.md` is
the one-screen cockpit and `HISTORY.md` is the dated change log.

---

## NEW · 2026-10-13 — from the reading-queue pass

**A · Lan Shen — the arc map needs re-cadencing (your next-phase decision).**
The pre-flight ARC MAP no longer describes the shipped serial: loaded canon chapters fill a
full band alone, so the "2 canon per chapter" ratio broke at ch 2. REBUILD_PLAN now carries
a "PACING AS LIVED" section marking the map stale; re-cadencing it is logged as your call
(`lan_shen/audits/AUDIT_2026-10-10_DEEP.md`, finding A1). Same audit, smaller: A6 — a
numbering collision in `OPEN_DECISIONS` (duplicate "### 1." and duplicate 11/12), filed for
your renumber, not self-healed.
**Your call:** approve a new cadence — or say "as lived" and the map gets rewritten to match.

**B · Fire Phoenix — the V2 public-promotion numbering decision is still awaiting you.**
The 2026-10-03 promotion proposal stages a contiguous C48–C55 candidate and cannot apply it
without your numbering decision (on file: `AWAITING_AUTHOR_NUMBERING_DECISION`; the public
layer otherwise ends at Chapter 52). The internal V2 line (C48–C60) sits in
`workshop/late_arc_rebuild/rebuild_v2/`.
**Your call:** the numbering — then the candidate can be promoted, or hold the line as it is.

**C · The Adaptation Talent has its own public home now — one follow-up decision (your call).**
`adaptation-talent` is live (`6ee8f94`): the universal core v2.0 locked, the level
framework, the codex + firewall, **19 module files for 16 holders across 5 worlds**, the
guided docs (01–05), the craft layer, and full provenance with a verify-the-whole-repo
`MANIFEST.sha256`. Every copy is byte-preserving; every module hash-matches its source; 138
relative links, 0 broken. Close report: `reports/AT-REPO-2026-10-13.md`.
**The open question:** the kit still carries its own copies of the same talent files (the
master foundation twice, the codex twice, every module). The house rule says one copy of one
thing; the new repository is now the reading home.
**Your call:** (a) repoint the kit's AT-family files to `adaptation-talent` — the new
repository becomes the single canonical home and the kit keeps pointers; or (b) keep both
standing — the kit copies stay working copies, the new repository is the shelf edition.
Nothing is deleted either way until you say.

---

## 1 · Supergirl: new acceptance receipts (the machine is waiting on you)

**What happened.** Chapters 9–14 carried 7,702 repeated words — in *Chapter 11 —
The Sun*, the same closing paragraph twenty times in a row. Removed
(`8bf9271`). The serial's `verify.py` now fails with six `ACCEPTED_HASH` errors,
**and that failure is true**: accepted text changed, so the acceptance is stale.
No receipt or hash was rewritten to hide it.

**Your call:** write six new receipts (`canon_coverage/Chapter_09…14_ACCEPTED.json`),
or `git revert 8bf9271` to restore the padding exactly.
**Also:** five chapters now sit below the `Full 3000+ Words` their own headers
claim (2,569 / 2,729 / 1,333 / 2,256 / 2,933). The padding *was* the length.
Restoring it means writing prose — yours.

## 2 · Supergirl: the 70 remaining long sentences

They are written in this serial's compressed beat style from end to end (the
`foundation/` beats read the same way), and fewer than half have any punctuation
a split could use. **Your call:** keep the voice, or apply the 60-word law and
accept that most need rewriting rather than splitting.

## 3 · Grey Wolf, Chapter 10: the stale duplicated ending

Recorded since 2026-10-11, still not cut. The same passage stands twice; one copy
is stale. **Your call:** cut the stale copy (one edit) or keep it deliberately.

## 4 · The two dialogue-floor scaffolds

`soul_land_starter` Ch01 and `soul_land_new` Ch01 — 20-word stubs with no
speaker. The gate fails them; they are scaffolds, so this may be intended.
**Your call:** declare them, or let the repair stand (adding a spoken line to a
stub is authoring).

## 5 · The one sentence that needs a writer

`Soul_Land_2_Project/chapter_02.md` holds a 60+-word sentence with no boundary —
no punctuation to split on. The repair tool reported it rather than butchering
it. **Your call:** rewrite that sentence; everything else in the kit is under the
cap.

## 6 · The committed archives (0.02–2.77 MB) *(updated 2026-10-13: the how-to-write zip was already removed — `7a65ad8`; four remain)*

Two fire-phoenix snapshots, the starter zip, supergirl's
`…53PASS.zip`. Git already keeps every version; a zip on top is dead weight and a
stale copy of prose. **Your call:** keep them (say so and the finding is
dismissed) or let them be removed.

## 7 · Three broken citation links

Supergirl's `canon_coverage/EPISODE_05/06_BEAT_MAP.md` cite
`[SRC-U31-USER](user_request_U31)` — the files are nowhere in the repository.
**Your call:** commit the user-request files, or change the citations to plain
text. (Found by the new link detector; it is the only real dead links in 4,334
documents.)

## 8 · CI: two repos held back, one needs your machine

- **supergirl-adrian-vale** — the workflow is written and one command away, but
  its verifier is red by design until item 1 is ruled. Arm after, not before.
- **storyos-site** — `verify_stage.py` reports 4 real failures in the
  `dragon_prince_yuan` stage (index.html/state.json/state.txt size-drift against
  its own manifest, and missing `RULES OF ENGAGEMENT`). The stage is built from
  sources that only exist on your machine, so it cannot be rebuilt here.
  **Your call:** rebuild the stage, then it can be armed.
- **token `workflow` scope** — optional forever now: the deploy-key route works
  and leaves nothing behind.

## 9 · Lin Hao / Adaptive Prodigy — one serial, two editions, now home

Consolidation settled a question the register had only suspected: **"Lin Hao" and
"Adaptive Prodigy" are one serial in two editions** — 64 chapter files byte-identical.
Both editions are now inside the kit: the newest text first (116 chapters) with its
2026-09 codex and docs; the older 101-chapter edition was archived in `_archive/2026-10-12_one-home/` and then deleted with the other extras in the same day's second pass (2026-10-12) — retrievable from the kit's own history (`git show 9379d40^:_archive/2026-10-12_one-home/adaptive_prodigy_reference_edition/<path>`; ledger in `PROJECTS.md`).

**Its one open question: 477 sentences run past the 60-word ceiling in the newest
text.** Repair (the splitter moves no word and changes no count), or leave it frozen
as reference? The older edition's 405 sit behind it, untouched either way.

---

## 10 · Gu Yuan (SL1) — the one real loss

**Approved edge = Chapter 98. What exists on GitHub: Chapter 75.** Chapters 54–98
were written in a workspace (`/home/user/SL1_GuYuan`) that was never uploaded. The
upload pack survived in the frozen archive and now lives in the kit
(`SL1_GU_YUAN/uploads/`, Ch 75 included). **If any copy still exists on your disk or
in an old chat export, it should come home — that is the only way these come back.**

---

## 11 · The consolidation — done, all points closed

1. **DONE 2026-10-12.** Every duplicate deleted. Nine imports; six source repositories
   emptied to one-line pointers; every unique file preserved first into the kit's
   `_archive/2026-10-12_one-home/` (verified file-by-file, zero unknowns); the Grey Wolf
   reading page relocated to `soul-land-universal-kit/docs/grey-wolf/`. **One copy of
   each serial remains — in the kit.** The six shells were **deleted** the same day, on your
   full-permission token — **the account is 10 repositories** (the Fire Phoenix pair went the same day — see point 2), **one home for everything**
   (GitHub keeps deleted repositories restorable for 90 days). *(Twelve since 2026-10-13 —
   the desk layer itself became `the-authors-desk`, and the Adaptation Talent doctrine
   became `adaptation-talent`.)*
2. **DONE — Fire Phoenix is home.** Chapters, working layers, the whole workshop —
   imported complete, file-by-file verified; both former repositories deleted the same
   day. The pipeline now runs from `soul_land_4_fire_phoenix/`.
3. **DONE — the extras deleted.** The preserved older editions and the workshop's
   snapshot layers are gone (1,592 files; ledger in `PROJECTS.md`). Nothing that was the
   only copy of its text was touched; the reading surfaces keep their copies because
   that is what they are.

---

## What no longer needs you (done since yesterday)

- **CI: 10 repositories armed, every first run green** — grey-wolf, kit, lan_shen,
  mcu, stark_heir, soul-library (cross-repo, 26 checks), fire-dragon,
  pokemon (stage-0 lock + gate selftest), universal-storyline toolkit, and the
  then-private fire-phoenix (consolidated into the kit the same week; its workflow copy is
  kept in `reports/ci-rollout-2026-10-12/`). Each push went through a one-shot deploy key, used once and
  deleted; **zero deploy keys standing account-wide**.
- **The account now measures itself weekly.** `account-sweep` (kit `de038ab`) clones
  every public repo on Mondays 04:23 UTC, runs the house gate + all eleven detectors,
  publishes the verdict to the run page and uploads the evidence. First run: 23
  books · 223 chapters · 884,693 words · 138 hard · 83 advisory.
- **The kit's own D1 law was broken for two weeks** (its two trees drifted from
  2026-09-28) **and the check that caught it could not fail the build.** Both
  fixed: the trees are byte-identical again (`c63e2a6`), and soul-library's
  sentinel now exits 1 on any failed check, declares a true capacity (`26 of 26`),
  and has a selftest (`c725757` + CI `ee1641b`).
- **The workspace was organised completely (2026-10-13, your word).** The kit root stopped
  being a pile: one-screen `README.md` cockpit, the old 398-line dated README kept verbatim
  as `HISTORY.md`, `STATE.md` retitled as the dated sweep record, **every root folder given
  its own README**, and one wrong label corrected — the tree long called *"Tianyu —
  dropped"* is the earlier **Lan Shen** build (the true Tianyu died with the 2026-10-12
  extras). The register's own coverage claim was fixed too: from inside the kit it had been
  reporting `0 of 0` trees — a guarantee that never ran; it now reports **33 of 33**. The
  ship script was rewired to the new cockpit (it bumps the Devouring Dragon row with both
  figures measured). Nothing was deleted — things moved and got one home.
- **Three new detectors**: dead links, generated-view stamps (11 of 11 verified
  honest), CI coverage. Then two more the same day: **the shelf/reference register
  fix** (Adaptive Prodigy and Lin Hao are books now) and **sightings** — the
  guarantee that every one of the chapter-bearing trees on disk is either a
  registered book, a classified sighting, or a hard finding — 82 at the time, 50 today
  after the extras left; zero unexplained either day.
  Control Centre now runs eleven detectors, 34 selftest cases, every number
  sample-verified against the text.
- **`THE-COMPLETE-REGISTER.md`** (and `REGISTER.md` in the kit): every book and
  every tree on the account in one generated table — 24 books · 377 chapters ·
  1,624,963 words · 70 over-60 sentences, with every non-book chapter-bearing tree
  classified (59 of 59 accounted — reconciled the same day; see
  `reports/REGISTER-RECONCILE-2026-10-13.md`). Regenerate any time:
  `python3 tools/register.py --root DIR --out REGISTER.md`.

*Rule the house keeps re-learning, now written into the code: a coverage line is
a claim — it gets checked like one. Today's examples: the sentinel said "26 of
22", and a new detector's first version said "13 of 12". Both were caught by
reading the number, not by trusting it.*
