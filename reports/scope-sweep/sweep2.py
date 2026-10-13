#!/usr/bin/env python3
"""WHOLE-ACCOUNT SWEEP, second pass.

The first pass had the defect it was hunting: it looked for directories named
`chapters` and therefore missed `chapters_rebuilt` — which is where Blue
Silver's live book lives, because `chapters/` there holds the draft the author
rejected. A sweep that decides what is live by directory NAME will always be
wrong somewhere. This pass finds every chapter-bearing directory, then reads
each project's own status files to decide what is live.

Answers, per book: how many chapters, do they carry speech, is there a second
copy of them anywhere, and does the project's own gate cover the live text?
"""
import os, re, json, glob, hashlib, subprocess

ROOT = '/tmp/all'
OUT = '/home/user/scope-sweep'
CHDIR = re.compile(r'^chapters?(_.*)?$', re.I)
DEAD = re.compile(r'(_archive|/archive/|/sources/|rejected|stale|_alt_drafts|promotion_proposal|'
                  r'staging|park|snapshot)', re.I)
STATUS_FILES = ('HANDOFF.md', 'STATUS.md', 'STATE.md', 'README.md', 'NEXT.md', 'AGENTS.md')
DEAD_WORDS = re.compile(r'(superseded|do not use|deprecated|rejected|historical|archive only|'
                        r'not authoritative|do not edit|parked|frozen)', re.I)


def chapter_dirs(proj):
    out = []
    for d in sorted(os.listdir(proj)):
        full = os.path.join(proj, d)
        if os.path.isdir(full) and CHDIR.match(d):
            n = len([f for f in os.listdir(full) if f.endswith('.md')
                     and 'template' not in f.lower()])
            if n:
                out.append((d, n))
    return out


def spans(text):
    """Spoken lines in EITHER quote style."""
    body = re.split(r'\n---\n\n## Footer|\n## Footer|\n## Production', text)[0]
    return (len(re.findall(r'"([^"\n]+)"', body))
            + len(re.findall(r'\u201c([^\u201d\n]+)\u201d', body)))


def words(text):
    body = re.split(r'\n---\n\n## Footer|\n## Footer|\n## Production', text)[0]
    lines = [l for l in body.split('\n') if l.strip() and not l.startswith('# ')]
    return len('\n'.join(lines).split())


def status_evidence(proj):
    for f in STATUS_FILES:
        p = os.path.join(proj, f)
        if not os.path.exists(p):
            continue
        t = open(p, encoding='utf-8', errors='replace').read()
        flat = ' '.join(t.split())
        m = DEAD_WORDS.search(flat)
        if m:
            i = max(0, m.start() - 90)
            return f, flat[i:m.start() + 130]
    return None, ''


repos = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
books, gates, files = [], [], {}

for repo in repos:
    rp = os.path.join(ROOT, repo)
    for dirpath, dirnames, filenames in os.walk(rp):
        parts = dirpath.split(os.sep)
        if '.git' in parts or 'node_modules' in parts:
            dirnames[:] = []
            continue
        for f in filenames:
            if f.endswith('.md'):
                files.setdefault(f, []).append(os.path.relpath(os.path.join(dirpath, f), ROOT))
        if os.path.basename(dirpath) in ('chapters', 'chapters_rebuilt'):
            continue  # handled per project below

    # ── book projects: any dir holding a chapter-bearing subdir ─────────
    seen = set()
    for dirpath, dirnames, filenames in os.walk(rp):
        parts = dirpath.split(os.sep)
        if '.git' in parts or 'node_modules' in parts:
            dirnames[:] = []
            continue
        cd = [(d, n) for d, n in [(d, 0) for d in dirnames] if False]
        hits = [(d, n) for d, n in chapter_dirs(dirpath)]
        if not hits:
            continue
        proj = dirpath
        if proj in seen:
            continue
        seen.add(proj)
        rel = os.path.relpath(proj, rp)
        dead_path = bool(DEAD.search(rel))
        ev_file, ev = status_evidence(proj)
        b = {'repo': repo, 'path': rel, 'archived_path': dead_path,
             'status_file': ev_file, 'status_evidence': ev[:200], 'dirs': {}}
        for dname, n in hits:
            dpath = os.path.join(proj, dname)
            per = {}
            for f in sorted(os.listdir(dpath)):
                if not f.endswith('.md') or 'template' in f.lower():
                    continue
                t = open(os.path.join(dpath, f), encoding='utf-8', errors='replace').read()
                per[f] = {'dlg': spans(t), 'words': words(t),
                          'sha': hashlib.sha1(t.encode('utf-8', 'replace')).hexdigest()[:12]}
            b['dirs'][dname] = per
        books.append(b)

    # ── gates ───────────────────────────────────────────────────────────
    for dirpath, dirnames, filenames in os.walk(rp):
        parts = dirpath.split(os.sep)
        if '.git' in parts or 'node_modules' in parts:
            dirnames[:] = []
            continue
        for f in filenames:
            if not re.search(r'(gate|check|verify|valid|audit|sentinel|lint|selftest)', f, re.I):
                continue
            if not f.endswith(('.py', '.sh', '.yml', '.yaml')):
                continue
            full = os.path.join(dirpath, f)
            src = open(full, encoding='utf-8', errors='replace').read()
            if len(src) < 60:
                continue
            gates.append({
                'repo': repo, 'path': os.path.relpath(full, rp), 'bytes': len(src),
                'chapters': bool(re.search(r'chapters', src)),
                'rebuilt': bool(re.search(r'chapters_rebuilt|rebuilt', src)),
                'manuscript': bool(re.search(r'manuscript', src)),
                'published': bool(re.search(r'published-site|published_site|docs', src)),
                'coverage': bool(re.search(r'COVERAGE', src)),
                'floor': bool(re.search(r'DIALOGUE_FLOOR|dlg\s*<\s*3', src)),
                'empty_ok': bool(re.search(r'passes empty|no chapters yet', src)),
                'exits': bool(re.search(r'sys\.exit|exit 1|exit\(1\)', src)),
            })

result = {'books': books, 'gates': gates}
json.dump(result, open(os.path.join(OUT, 'sweep2.json'), 'w'), indent=1)

# ── cross-copy duplicate report ────────────────────────────────────────
dups = {k: v for k, v in files.items() if len(v) > 1 and re.match(r'chapter', k, re.I)}

L = ['# WHOLE-ACCOUNT SWEEP — pass 2\n',
     f'{len(books)} book projects · {len(gates)} gate scripts · {len(dups)} chapter filenames in 2+ places\n',
     '\n## Book projects\n',
     '| repo | project | chapter dirs | chapters | words | spoken | floor<3 | archived path | status evidence |',
     '|---|---|---|---:|---:|---:|---:|---|---|']
for b in sorted(books, key=lambda x: (x['repo'], x['path'])):
    for dname, per in b['dirs'].items():
        ch = len(per); w = sum(v['words'] for v in per.values())
        d = sum(v['dlg'] for v in per.values())
        bad = [k for k, v in per.items() if v['dlg'] < 3]
        ev = (b['status_evidence'][:60].replace('|', '/') if b['status_evidence'] else '')
        L.append(f"| {b['repo']} | `{b['path']}` | `{dname}` | {ch} | {w} | {d} | {len(bad)} | "
                 f"{'archive' if b['archived_path'] else ''} | {ev} |")
open(os.path.join(OUT, 'INVENTORY2.md'), 'w').write('\n'.join(L) + '\n')

# ── console ────────────────────────────────────────────────────────────
print("LIVE BOOKS WITH ZERO-SPEECH CHAPTERS (archived paths excluded):")
for b in books:
    if b['archived_path']:
        continue
    for dname, per in b['dirs'].items():
        bad = [k for k, v in per.items() if v['dlg'] < 3]
        if bad:
            print(f"  {b['repo']}/{b['path']} [{dname}]  {len(bad)}/{len(per)} chapters — "
                  f"{', '.join(bad[:4])}")
print("\nPROJECTS WHOSE own STATUS FILE CALLS THE CONTENT SUPERSEDED/REJECTED:")
for b in books:
    if b['status_evidence']:
        print(f"  {b['repo']}/{b['path']}  ({b['status_file']}) — …{b['status_evidence'][:120]}…")
print("\nCHAPTER FILENAMES APPEARING IN 2+ PLACES (two-copies candidates):")
for k in sorted(dups)[:14]:
    print(f"  {k:44s} {len(dups[k])} copies")
