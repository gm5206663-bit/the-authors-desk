# Agent guidance evidence — 2026-10-16

Narrative and filled handoff: [rollout receipt](../AGENT-GUIDANCE-2026-10-16.md).
This is a dated evidence bundle, not another story-state authority.

- [Implementation revisions](implementation-revisions.json): exact public commits.
- [Public-source check](public-source-check.txt) and [preparation](source-preparation.txt):
  clean triggering desk revision plus the freshly cloned public dependencies.
- [Guidance tests](guidance-tests.txt): 46 passing fixture tests, not a model-comprehension evaluation.
- [Desk tests](desk-tests.txt) and [kit detector tests](kit-detector-tests.txt).
- [Public entrypoint checks](public-entrypoints.json): raw `AGENTS.md` links and start page HTTP status.
- [CI snapshot](ci-results.json): all verification/sentinel jobs completed success;
  the desk Pages job was still in progress at that recorded snapshot.
- [Chapter integrity](chapter-integrity.json): 377 live chapter files unchanged
  from their base Git objects; no acceptance hashes were updated.
- [Account report](account.md), [JSON](account.json), [HTML](account.html):
  measured while preparing the rollout, before adding this receipt bundle.
- [Shelf baseline](shelf-before.txt) versus [repaired result](shelf-after.txt),
  [sentinel selftest](shelf-selftest.txt) and [continuity lint](shelf-continuity.txt).
- [Supergirl baseline selftest](supergirl-baseline-selftest.txt) versus
  [after selftest](supergirl-after-selftest.txt): same two failures; both 51/53.
  [Pinned CI wrapper output](supergirl-pinned-ci.txt) is successful without
  changing that known pending-acceptance state. Raw selftests are not called green.
- [StoryOS pinned wrapper](storyos-pinned-ci.txt): four known stage issues remain.
- [MCU Eternal verifier](eternal-verifier.txt), [Stark verifier](stark-verifier.txt),
  [Pokemon gate selftest](pokemon-selftest.txt) and [storyline selftest](storyline-selftest.txt).
- [SHA256SUMS](SHA256SUMS) covers every other file in this bundle.

Verify with `sha256sum -c SHA256SUMS` from this directory. Revisions, test counts
and statuses describe this run, not permanent claims. Public dependency checks do
not discover private repositories, grade prose/canon or supply author permission.
