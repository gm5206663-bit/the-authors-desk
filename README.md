# THE AUTHOR'S DESK

**For agents:** [local entry](AGENTS.md) · [account starting page](https://github.com/gm5206663-bit/the-authors-desk/blob/main/agents/START-HERE.md).

The control room for the whole account — **thirteen repositories, one read**. This is the
home of the **desk** (the author's decisions), the **register** (measured books and
chapter-bearing trees), the **records** (dated operational evidence), and the shared
**agent guide** (safe entry, task routing and handoffs).

No serial's text lives in this repository. The texts live in their own homes — every Soul Land
project in [`soul-land-universal-kit`](https://github.com/gm5206663-bit/soul-land-universal-kit),
the reading site in [`soul-library`](https://github.com/gm5206663-bit/soul-library).

---

## The layout

| Path | What it is |
|---|---|
| `THE-AUTHORS-DESK.md` | **The desk** — every decision awaiting the author, each with its evidence and both outcomes. The items no agent may rule on. |
| `THE-COMPLETE-REGISTER.md` | **The register** — every book, every chapter-bearing tree, every count, generated. On 2026-10-13: 24 registered books · 377 chapters · 1,624,963 words · coverage 59 of 59 trees — reconciled the same day, see [`reports/REGISTER-RECONCILE-2026-10-13.md`](reports/REGISTER-RECONCILE-2026-10-13.md). |
| [`agents/START-HERE.md`](agents/START-HERE.md) | The shared agent starting point — routes, permission/state boundaries, templates, examples and onboarding checks. |
| `repos.txt` | The account map — which repository is the home of what. |
| `docs/index.html` | The desk as a page — the front door on GitHub Pages: [gm5206663-bit.github.io/the-authors-desk](https://gm5206663-bit.github.io/the-authors-desk/). |
| `reports/` | The dated records — close notes per lane, the account audit, the scope sweep, the CI rollout. Index in `reports/README.md`. |
| `NOTICE.md` | The fan-work disclaimer. |

## Current maintenance

The [2026-10-16 maintenance receipt](reports/MAINTENANCE-2026-10-16.md) records
the fresh account audit, complete-scope sweep hardening, front-door drift fix,
and verification-workflow safeguards. No author-gated story decision changed.

The desk now checks its own current navigation and map consistency on every
push: `python3 tools/check.py` (fixtures: `python3 tools/selftest.py`). This is
a local-map check, not live repository discovery; the account sweep supplies that.

## The rules this room runs on

**One copy of one thing.** The desk layer lives here and only here; the working machine keeps
pointers. A document kept in two places will be wrong in one of them.

**Counts are measured, never typed.** The register regenerates in one command:

```bash
# with the account's repositories cloned into one directory (e.g. ~/account/):
python3 soul-land-universal-kit/SOUL_LAND_UNIVERSAL_KIT/tools/register.py \
        --root ~/account --out THE-COMPLETE-REGISTER.md
```

**Everything public.** No archived repositories, no private state, no hidden corners.

**The register is generated; the desk is written.** Edit the desk freely; never hand-edit the
register — regenerate it.

## Who reads this

- **The author** reads the desk: each item states the question, the evidence, and what happens
  on either answer.
- **A fresh agent** reads all three files and reaches correct account state without being told
  anything twice — the same promise the kit's cockpit and the Control Centre make for the books.

---

*Soul Land (斗罗大陆 / Douluo Dalu) and all related characters, settings and terms belong to
Tang Jia San Shao and the original rights holders. Everything in this account is
non-commercial derivative fan work. See `NOTICE.md`.*
