# Checking the guidance

From the author-desk repository root:

```bash
python3 tools/agent_check.py
python3 tools/agent_selftest.py
```

The first command validates the local guidance bundle: required pages and template
fields, registry structure, safe paths, route references, onboarding evidence
references, local relative links and coordinated fixture answer keys. It does
not fetch GitHub, execute registry commands or claim that remote sources exist.

To prepare a new public source set using the triggering desk checkout:

```bash
python3 tools/agent_sources.py --root /tmp/agent-account-fresh
```

The destination must be new/empty and outside the desk checkout. Existing local
work is never reset. A clone failure is fatal. To validate an already complete
sibling checkout set:

```bash
python3 tools/agent_check.py --root /path/to/account
```

That directory must contain every repository named in `repos.txt`, each as a Git
checkout. The checker validates each root entrypoint, required-reading/current
source paths, command script paths, explicit onboarding links and project routes.
It also inspects extra Git checkouts: a map smaller than the provided account
root fails, instead of silently shrinking scope. It prints per-repository HEADs and flags modified working trees; a dirty checkout
is not represented as the exact bytes of its HEAD.

The pinned desk workflow clones the public repositories in the reviewed registry
on pushes/PRs and weekly. It uses tokenless URLs and fails if a clone is missing.
This is a live cross-repository dependency check, not an atomic snapshot or
proof that a private/new unlisted remote repository does not exist. The separate
kit public-inventory sweep discovers the owner's account.

## What these tests cannot prove

They do not certify an agent's comprehension, literary judgment, canon accuracy,
permission interpretation or freshness of every sentence. They prove structural
contracts and the presence of the declared evidence paths. The onboarding answer
key supports a human/agent exercise; fixture tests are not a model evaluation.
No checker promotes a proposal, changes a lock or supplies missing authorization.

Add a regression whenever a guidance defect is fixed. A clean fixture must stay
clean, and the specific broken fixture must fail. Never lower an acceptance
standard just to make the guidance badge green.

[Back to start](START-HERE.md)
