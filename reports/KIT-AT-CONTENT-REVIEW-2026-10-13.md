# KIT AT-CONTENT REVIEW — the one-copy question, measured

**2026-10-13 · for desk item C: AT-family files in the kit — pointers, or both stand?**
**No default is applied. Nothing was deleted. This is the measurement the decision needs.**

## What was measured

- **209 kit files carry AT content** (the words *Adaptation Talent* in text,
  outside the archives) — mostly the serial-side working files: per-serial module, status,
  and log files that live in the trees the gates actually run in.
- **32 kit files are byte-identical twins of files in `adaptation-talent`**
  (matched by full SHA-256, not by name — including the kit's archive trees; the AT repo's
  own provenance file already records them). They are listed below with their hashes.

## The twins (hash-matched, byte-identical)

| Kit path | adaptation-talent path | sha256 (16) |
|---|---|---|
| `CODEX/GENESIS_CODEX_ADAPTIVE.md` | `canon/GENESIS-CODEX-ADAPTIVE.md` | `49898ca407e19d4a` |
| `LICENSE` | `LICENSE` | `c317d8d48606c85a` |
| `SL_ARCHIVE/Adaptation-Talent-Definitive-Master-Foundation.md` | `canon/MASTER-FOUNDATION.md` | `eaced0a52af1ca30` |
| `adaptive_prodigy/library/Adaptation-Talent-Definitive-Master-Foundation-1.md` | `canon/MASTER-FOUNDATION.md` | `eaced0a52af1ca30` |
| `adaptive_prodigy/library/GENESIS_CODEX_ADAPTIVE.md` | `canon/GENESIS-CODEX-ADAPTIVE.md` | `49898ca407e19d4a` |
| `adaptive_prodigy/library/LESSONS_ABSORBED.md` | `practice/lessons-absorbed.md` | `66e0b952798d4f77` |
| `adaptive_prodigy/library/STORYOS_ADAPTATION_FIREWALL.md` | `canon/STORYOS-ADAPTATION-FIREWALL.md` | `d535cf570cf53a1e` |
| `adaptive_prodigy/library/STORYOS_MASTER_SKILL_ULTIMATE.md` | `practice/storyos-master-skill-ultimate.md` | `eb8e9a4680ad21c9` |
| `adaptive_prodigy/library/StoryOS-Naagin-S1-Control-Book.md` | `practice/naagin-s1-control-book.md` | `eea640ae7280f68e` |
| `adaptive_prodigy/library/adaptation_talent_framework.md` | `canon/LEVEL-FRAMEWORK.md` | `7d49f87ccf34d057` |
| `adaptive_prodigy/library/storyos_master_skill.md` | `practice/storyos-master-skill.md` | `339c992a8c6a860c` |
| `adaptive_prodigy/library/storyos_master_skill_v3_UNIVERSAL.md` | `practice/storyos-master-skill-v3-universal.md` | `afdf9c82b19bd445` |
| `adaptive_prodigy/library/storyos_system_index.md` | `practice/storyos-system-index.md` | `ecf9c7701ee51304` |
| `adaptive_prodigy/library/storyos_toolkit.md` | `practice/storyos-toolkit.md` | `f4cc820901a89c1e` |
| `dragon_prince_yuan_native_oc_fanfiction/bible/OC_ADAPTATION_TALENT.md` | `modules/zhou-xu-dragon-prince-yuan.md` | `4e452a4582ed2df8` |
| `lan_shen/LICENSE` | `LICENSE` | `c317d8d48606c85a` |
| `qian_xunji/foundation/ADAPTATION_TALENT_QIAN_XUNJI.md` | `modules/qian-xunji.md` | `55883ef274e1748d` |
| `seed_of_creation/bible/ADAPTATION_TALENT_MODULE.md` | `modules/seed-of-creation.md` | `881ce4eae7a67540` |
| `soul_land_1_fire_dragon_lizard/LICENSE` | `LICENSE` | `c317d8d48606c85a` |
| `soul_land_1_fire_dragon_lizard/bible/ADAPTATION_TALENT.md` | `modules/fire-dragon-lizard.md` | `075afdc25d13481c` |
| `soul_land_2_clear_sky_lion/LICENSE` | `LICENSE` | `c317d8d48606c85a` |
| `soul_land_3_new/foundation/ADAPTATION_TALENT_MODULE.md` | `modules/silver-golden-wolf.md` | `368a3141cab31a09` |
| `soul_land_3_oc/bible/ADAPTATION_MODULE.md` | `modules/su-yan-one-in-a-thousand.md` | `ff96d5e9342f648d` |
| `soul_land_4_fire_phoenix/LICENSE` | `LICENSE` | `c317d8d48606c85a` |
| `soul_land_4_fire_phoenix/bible/ADAPTATION_TALENT_LOCAL.md` | `modules/yan-shuo-fire-phoenix.md` | `bbef1c1366f51eeb` |
| `soul_land_4_fire_phoenix/bible/LAN_XUANYU_PRESSURE_ADAPTATION.md` | `modules/lan-xuanyu-pressure-adaptation.md` | `883a121c57fee883` |
| `soul_land_devouring_dragon/bible/ADAPTATION_LOG.md` | `modules/devouring-dragon-log.md` | `f382511f16aff58d` |
| `soul_land_devouring_dragon/bible/ADAPTATION_MODULE.md` | `modules/devouring-dragon.md` | `a6f43862285a2f9f` |
| `soul_land_holy_spirit/bible/ADAPTATION_HUMAN.md` | `modules/luo-chen-holy-spirit.md` | `f478a48994d1e606` |
| `soul_land_new/bible/ADAPTATION_LOG.md` | `modules/lan-shen-log.md` | `674473aa266914a7` |
| `soul_land_new/bible/ADAPTATION_MODULE.md` | `modules/lan-shen.md` | `2fb62d952e6b7313` |
| `soul_land_new/foundation/ADAPTATION_AUDIT_2026-09-15.md` | `modules/lan-shen-audit-2026-09-15.md` | `045f2cb257740433` |

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
The kit's own charter is self-containment — it is built to be *dropped into a new project
and followed*. A new serial starting from the kit must find the AT inputs in-tree. The twins
are already recorded, with hashes, in `adaptation-talent/provenance/COPIES-AND-TWINS.md`.

**(b) The kit files become pointers to `adaptation-talent`.**
The kit stops being droppable-whole: a new session must fetch the AT repo to learn the law
its own gates assume. The claim map (which file lives where) would live in the kit README;
the work is small and safe (copy-only → later delete, history keeps every byte), but the
self-containment property is lost and the sentinel's drift checks around these trees would
need re-pointing.

**The safe window for (b), if ever wanted:** after the author rules, done as one lane with
the sentinel re-pointed in the same commit, so no day passes with a broken working tree.
