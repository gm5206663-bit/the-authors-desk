# Maintenance evidence — 2026-10-16

Main narrative: [maintenance receipt](../../MAINTENANCE-2026-10-16.md).
All files here are dated evidence, not current story authority.

| Evidence | Meaning |
|---|---|
| [account.md](account.md) · [JSON](account.json) · [HTML](account.html) | Final authenticated Control Centre run over a fresh public clone set. Snapshot taken before this evidence bundle was committed. 24 books / 377 chapters / 1,624,963 words / 30,865 spoken; 70 hard / 242 advisory. |
| [inventory.json](inventory.json) | Public discovery and clone operation completed, 13 expected / 13 cloned / zero archived. Public visibility does not prove the absence of private repositories. |
| [repositories.txt](repositories.txt) · [clone-heads.json](clone-heads.json) | Exactly which repositories and revisions the final report read. Discovery and clones are sequential, not atomic. |
| [chapter-integrity.json](chapter-integrity.json) | 377 registered live chapter files hash-identical between the starting checkout and final public rehearsal. The per-file SHA-256 is the same in both. Does not claim every non-chapter document stayed unchanged. |
| [stale-before-fix.json](stale-before-fix.json) · [stale-after-fix.json](stale-after-fix.json) | New front-door detector reproduces both old twelve-count claims, then clears after the desk HTML correction. These detector-only reports do not measure chapter facts; their zero chapter summary is not an empty corpus. |
| [detector-tests.txt](detector-tests.txt) | 50 passing detector checks. |
| [inventory-tests.txt](inventory-tests.txt) · [evidence-tests.txt](evidence-tests.txt) | 14 discovery/clone tests and 12 evidence-validation tests, offline. |
| [desk-tests.txt](desk-tests.txt) | Eight desk navigation/map regression tests. |
| [live-gate-tests.txt](live-gate-tests.txt) · [scope-tests.txt](scope-tests.txt) · [kit-verifier-tests.txt](kit-verifier-tests.txt) | Existing gate/verifier suites still pass; all seven scope perturbations caught. |
| [ci-results.json](ci-results.json) | Exact run IDs, implementation revisions, status and conclusion. All verification and hardened sweep jobs completed success; kit Pages was separately queued at this snapshot. This is dated evidence, not a live status feed. |
| [live-sites.json](live-sites.json) | Seven HTTP 200 reading sites; desk HTML checked for corrected count and Sara link. |
| [SHA256SUMS](SHA256SUMS) | Integrity manifest for every other file in this bundle, including this index. Verify from this directory with `sha256sum -c SHA256SUMS`. |

The account report's known findings remain untouched. The broad standalone house
gate and registered-book Control Centre use different discovery scopes; see the
main receipt rather than interpreting their counts as interchangeable.
