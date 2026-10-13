# KIT AT-CONTENT REVIEW — the one-copy question, measured

**2026-10-13 · for desk item C: AT-family files in the kit — pointers, or both stand?**
**No default is applied. Nothing was deleted. This is the measurement the decision needs.**

## What was measured

- **205 kit files carry AT content** (Adaptation Talent mentioned in text or filename,
  outside archives).
- **10 of them share a filename with a file in `adaptation-talent`**;
  **0 are byte-identical** to their AT-repo copy, 10 differ.
- The rest are the serial-side working files (per-serial module/status/log files that live
  in their own serial trees — the trees the gates actually run in).

## The twin table (candidates for the pointer question)

| Kit path | adaptation-talent path | Hash |
|---|---|---|
| `README.md` | `README.md` | DIFFERS |
| `SOUL_LAND_WORKSPACE/README.md` | `README.md` | DIFFERS |
| `Soul_Land_2_Project/README.md` | `README.md` | DIFFERS |
| `qian_xunji/README.md` | `README.md` | DIFFERS |
| `seed_of_creation/README.md` | `README.md` | DIFFERS |
| `soul_land_1_fire_dragon_lizard/README.md` | `README.md` | DIFFERS |
| `soul_land_2_clear_sky_lion/README.md` | `README.md` | DIFFERS |
| `soul_land_2_new/README.md` | `README.md` | DIFFERS |
| `soul_land_devouring_dragon/README.md` | `README.md` | DIFFERS |
| `soul_land_holy_spirit/README.md` | `README.md` | DIFFERS |

## The mirror — settled by measurement, not deleted

`SOUL_LAND_WORKSPACE/kit/` is a **deliberate working copy** of `SOUL_LAND_UNIVERSAL_KIT/`:
18/18 tools files and 14/14 top-level docs byte-identical, templates identical, and the
**library sentinel enforces the equality as a live check** (`workspace` — "kit trees
byte-identical (D1 law)"); it passed 26/26 on 2026-10-13. It is also invoked: the sentinel
and sync tooling read the workspace-side copy for the parked Blue Silver gate. Its hub now
carries a current-state note saying exactly this. **Recommendation recorded: no change — it
is by design, documented, and enforced. The author may still rule otherwise.**

## What each outcome means

**(a) The kit keeps its copies, and the AT repo is the reading home (current state).**
The kit's own charter is self-containment — verified wording: it is "built to be dropped into a new project and followed". A new serial
starting from the kit must find the AT inputs in-tree. The twins are already recorded, with
hashes, in `adaptation-talent/provenance/COPIES-AND-TWINS.md`.

**(b) The kit files become pointers to `adaptation-talent`.**
The kit stops being droppable-whole: a new session must fetch the AT repo to learn the law
its own gates assume. The claim map (which file lives where) would live in the kit README;
the work is small and safe (copy-only → later delete, history keeps every byte), but the
self-containment property is lost and the sentinel's drift checks around these trees would
need re-pointing.

**The safe window for (b), if ever wanted:** after the author rules, done as one lane with
the sentinel re-pointed in the same commit, so no day passes with a broken working tree.
