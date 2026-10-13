# THE AUTHOR'S DESK

The control room for the whole account — **twelve repositories, one read**. Three things live
here and only here: the **desk** (every decision that is the author's to make), the
**register** (every book and every chapter-bearing tree, measured), and the **records**
(the dated close notes and audit artifacts of every operation).

No serial's text lives in this repository. The texts live in their own homes — every Soul Land
project in [`soul-land-universal-kit`](https://github.com/gm5206663-bit/soul-land-universal-kit),
the reading site in [`soul-library`](https://github.com/gm5206663-bit/soul-library).

---

## The layout

| Path | What it is |
|---|---|
| `THE-AUTHORS-DESK.md` | **The desk** — every decision awaiting the author, each with its evidence and both outcomes. The items no agent may rule on. |
| `THE-COMPLETE-REGISTER.md` | **The register** — every book, every chapter-bearing tree, every count, generated. On 2026-10-13: 24 registered books · 377 chapters · 1,624,963 words · coverage 59 of 59 trees — reconciled the same day, see [`reports/REGISTER-RECONCILE-2026-10-13.md`](reports/REGISTER-RECONCILE-2026-10-13.md). |
| `repos.txt` | The account map — which repository is the home of what. |
| `docs/index.html` | The desk as a page — the front door on GitHub Pages: [gm5206663-bit.github.io/the-authors-desk](https://gm5206663-bit.github.io/the-authors-desk/). |
| `reports/` | The dated records — close notes per lane, the account audit, the scope sweep, the CI rollout. Index in `reports/README.md`. |
| `NOTICE.md` | The fan-work disclaimer. |

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
