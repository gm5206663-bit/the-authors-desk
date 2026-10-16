# Worked example — a safe navigation repair

**Real case:** the desk Pages front door said twelve after the account gained
Sara. [The maintenance receipt](../../reports/MAINTENANCE-2026-10-16.md) records it.

1. Establish scope: fix account navigation, not story text.
2. Compare the current inventory, `repos.txt` and live HTML. Capture both stale
   visible claims; do not rewrite old dated reports that correctly said twelve.
3. Reproduce the defect with a failing spelled-out/HTML count fixture. Also prove
   a matching count and historical record stay quiet.
4. Fix the front door, rerun the test and inspect the actual published HTML.
5. Commit the source and regression; publish a dated receipt with exact revisions.

**Why it is safe:** the source is unambiguous, scope is management, history stays
intact and no author decision changes. The test catches the root class of defect,
not just a single string replacement.
