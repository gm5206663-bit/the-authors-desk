# REGISTER RECONCILE — 2026-10-13

*One day, two measurements, one truth. This records why the account's numbers moved
and how every tool was brought back into agreement.*

## The drift

| measurement | when | books | chapters | words | trees |
|---|---|---:|---:|---:|---|
| register as first published | 02:14 | 22 | 375 | 1,617,455 | 50 of 50 |
| dispatched account sweep (run `38376498992`) | 09:24 UTC | 24 | 377 | 1,624,963 | 59 of 59 |
| clean regen + local Control Centre, full 12-repo clone set | 10:34 | 24 | 377 | 1,624,963 | 59 of 59 |

## The diagnosis

The 02:14 regen — and every surface that quoted it — ran over a set that did not
include two **shelf-only serials** which live in exactly one place, the Soul Library
shelf:

- `soul-library/chapters/sl3_new` — 1 chapter · 3,802 words (kit twin: `soul_land_3_new`)
- `soul-library/chapters/dragon_prince_yuan` — 1 chapter · 3,706 words (kit twin: `dragon_prince_yuan_native_oc_fanfiction`)

Both are status **"registered where found"** — the shelf serial with no other home.
The same partial view undercounted the classified sightings (8 → 15 shelf copies;
50 → 59 trees total).

## The fix

- Both registers were regenerated over a **full 12-repo clone set** (the sweep's own
  recipe) — the desk's account register
  (`tools/register.py --root <clone set> --label "the whole account"`) and the kit's
  kit-scope one; the kit register proved **identical**, so it was left untouched.
- Every current-state surface was corrected the same hour: this desk (README,
  THE-AUTHORS-DESK), the guide (README, docs/06), and the profile row.
- Dated receipts from earlier today keep their morning numbers **on purpose** — they
  record their moment; this file explains the movement, and the register itself is
  the fixing tool.

## The verification

A fresh local Control Centre run over the same clone set reproduces the sweep run
exactly: **24 books · 377 chapters · 1,624,963 words · 30,865 spoken lines**. The run
is archived verbatim: [`account-audit/account-2026-10-13-reconciled.md`](account-audit/account-2026-10-13-reconciled.md)
(with `.html` and `.json` beside it).

- **70 hard findings — all of them the supergirl 70-sentence ruling** (standing in
  the author's hands; nothing mechanical to repair).
- 244 advisory, every class explained: 234 book↔published-copy repeats (that is what
  publishing does), 2 independent two-homes (`dragon_prince_yuan` ×3 homes,
  `sl3_new` ×2 — shelved and published copies), 4 classified sightings, 3
  orphan-work rows (all correctly "registered where found"), 1 documented dialogue
  exemption citing live receipts.
- Housekeeping: **0 machine files or archives across 3,809 files, 12 repositories.**

## The lesson

**Regenerate over the whole account or the register is measuring the root you gave
it.** A partial clone set undercounts in exactly the way the register was built to
prevent: a serial that exists in one place was, for one morning, missing from the
count of everything.

*Register: [`../THE-COMPLETE-REGISTER.md`](../THE-COMPLETE-REGISTER.md).*
