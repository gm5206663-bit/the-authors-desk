#!/usr/bin/env python3
"""WHOLE-ACCOUNT SWEEP — find every instance of the scope defect.

For every repository, find every "book project" (a directory holding a
chapters/ folder) and every gate/check script, then answer the three
questions the Scope Law asks:

  1. does the check cover what SHIPS?   (chapters/ vs manuscript/ vs docs/)
  2. does it say how much it covered?   (a COVERAGE line)
  3. does it fail when it covers nothing? (empty scope)

Writes /home/user/scope-sweep/INVENTORY.md and sweep.json
"""
import os, re, json, glob, subprocess, sys

ROOT = '/tmp/all'
OUT = '/home/user/scope-sweep'
os.makedirs(OUT, exist_ok=True)

GATE_HINT = re.compile(r'(gate|check|verify|valid|audit|sentinel|selftest|fixture|lint|test)', re.I)


def md_files(d):
    out = []
    for f in sorted(glob.glob(os.path.join(d, '*.md'))):
        b = os.path.basename(f).lower()
        if b.startswith(('readme', 'index', 'changelog')):
            continue
        if 'template' in b:
            continue
        out.append(f)
    return out


def dialogue_spans(text):
    """Spoken lines in EITHER quote style. Straight quotes and curly quotes
    are both used in this account, and counting only one of them invents
    violations that do not exist — which is how the first pass of this
    sweep produced two false findings."""
    body = re.split(r'\n---\n\n## Footer|\n## Footer|\n## Production', text)[0]
    return (len(re.findall(r'"([^"\n]+)"', body))
            + len(re.findall(r'\u201c([^\u201d\n]+)\u201d', body)))


def words_of(text):
    body = re.split(r'\n---\n\n## Footer|\n## Footer|\n## Production', text)[0]
    lines = [l for l in body.split('\n') if l.strip() and not l.startswith('# ')]
    return len('\n'.join(lines).split())


def body_of(text):
    return re.split(r'\n---\n\n## Footer|\n## Footer|\n## Production', text)[0].rstrip()


repos = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
result = {'repos': {}, 'gate_files': [], 'book_projects': []}

for repo in repos:
    rp = os.path.join(ROOT, repo)
    entry = {'book_projects': [], 'gates': [], 'tools_dirs': [], 'selftests': []}

    # ── book projects ──────────────────────────────────────────────────
    for dirpath, dirnames, filenames in os.walk(rp):
        parts = dirpath.split(os.sep)
        if '.git' in parts or 'node_modules' in parts:
            dirnames[:] = []
            continue
        if os.path.basename(dirpath) == 'chapters':
            auth = md_files(dirpath)
            if not auth:
                continue
            proj = os.path.dirname(dirpath)
            man_dir = os.path.join(proj, 'manuscript')
            docs_dir = os.path.join(proj, 'docs')
            readers = md_files(man_dir) if os.path.isdir(man_dir) else []
            fulls = [f for f in readers if 'FULL' in os.path.basename(f).upper()]
            readers = [f for f in readers if f not in fulls]
            an = {os.path.basename(f): f for f in auth}
            rn = {os.path.basename(f): f for f in readers}
            docs = sorted(glob.glob(os.path.join(docs_dir, '*.html'))) if os.path.isdir(docs_dir) else []
            docs_ch = [d for d in docs if re.search(r'chapter[_-]?\d', os.path.basename(d), re.I)]

            rel = os.path.relpath(proj, rp)
            dead = re.search(r'(_archive|/sources/|stale|STALE|_alt_drafts|promotion_proposal|'
                             r'staging|_kit_reference|/reference/|snapshot|rebuild)', rel, re.I)
            p = {'repo': repo, 'path': rel, 'live': not bool(dead), 'chapters': len(an),
                 'manuscript': len(rn), 'docs_pages': len(docs_ch),
                 'full_chapters': 0, 'orphans': sorted(set(rn) - set(an)),
                 'unpublished': sorted(set(an) - set(rn)), 'stale': [], 'floor_violations': [],
                 'low': [], 'words': {}, 'dlg': {}}
            if fulls:
                p['full_chapters'] = len(re.findall(r'(?m)^# Chapter \d+',
                                                    open(fulls[0], encoding='utf-8', errors='replace').read()))
            for name in sorted(set(an) & set(rn)):
                a = open(an[name], encoding='utf-8', errors='replace').read()
                r = open(rn[name], encoding='utf-8', errors='replace').read()
                if re.sub(r'\s+$', '', body_of(a)) != re.sub(r'\s+$', '', body_of(r)):
                    p['stale'].append(name)
            for name, f in sorted(an.items()):
                t = open(f, encoding='utf-8', errors='replace').read()
                d, w = dialogue_spans(t), words_of(t)
                p['dlg'][name] = d
                p['words'][name] = w
                if d < 3:
                    p['floor_violations'].append(name)
                elif w and d / w * 1000 < 8:
                    p['low'].append(name)
            entry['book_projects'].append(p)
            result['book_projects'].append(p)

    # ── gate / check scripts ───────────────────────────────────────────
    for dirpath, dirnames, filenames in os.walk(rp):
        parts = dirpath.split(os.sep)
        if '.git' in parts or 'node_modules' in parts:
            dirnames[:] = []
            continue
        for f in filenames:
            if not f.endswith(('.py', '.sh', '.yml', '.yaml', '.js', '.ts')):
                continue
            if not GATE_HINT.search(f):
                continue
            full = os.path.join(dirpath, f)
            try:
                src = open(full, encoding='utf-8', errors='replace').read()
            except Exception:
                continue
            if len(src) < 40:
                continue
            g = {
                'repo': repo, 'path': os.path.relpath(full, rp), 'bytes': len(src),
                'reads_chapters': bool(re.search(r'chapters', src)),
                'reads_manuscript': bool(re.search(r'manuscript', src)),
                'reads_docs': bool(re.search(r'docs', src)),
                'has_coverage': bool(re.search(r'COVERAGE', src)),
                'has_exit': bool(re.search(r'sys\.exit|exit 1|exit\(1\)|raise SystemExit', src)),
                'passes_empty': bool(re.search(r'passes empty|no chapters yet', src)),
                'has_floor': bool(re.search(r'dlg\s*<\s*3|DIALOGUE_FLOOR|dialogue.*floor', src, re.I)),
                'is_selftest': bool(re.search(r'selftest|fixture', f, re.I)),
            }
            g['kind'] = 'selftest' if g['is_selftest'] else (
                'gate' if re.search(r'gate|check|verify|valid|audit|sentinel|lint', f, re.I) else 'other')
            entry['gates'].append(g)
            result['gate_files'].append(g)

    result['repos'][repo] = entry

json.dump(result, open(os.path.join(OUT, 'sweep.json'), 'w'), indent=1)

# ── report ─────────────────────────────────────────────────────────────
L = []
L.append('# WHOLE-ACCOUNT SWEEP\n')
L.append(f'{len(repos)} repositories · {len(result["book_projects"])} book projects · '
         f'{len(result["gate_files"])} gate/check scripts\n')
L.append('\n## Book projects — chapters / reader editions / published pages\n')
L.append('| repo | project | author | reader | docs | FULL | orphans | unpublished | stale | floor<3 | low |')
L.append('|---|---|---:|---:|---:|---:|---|---|---|---:|---:|')
for p in result['book_projects']:
    L.append(f"| {p['repo']} | `{p['path'] or '.'}` | {p['chapters']} | {p['manuscript']} | "
             f"{p['docs_pages']} | {p['full_chapters']} | {len(p['orphans'])} | {len(p['unpublished'])} | "
             f"{len(p['stale'])} | {len(p['floor_violations'])} | {len(p['low'])} |")

L.append('\n## Every gate and check script\n')
L.append('| repo | path | kind | bytes | chapters | manuscript | docs | COVERAGE | fails | passes empty | floor |')
L.append('|---|---|---|---:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|')
for g in sorted(result['gate_files'], key=lambda x: (x['repo'], x['path'])):
    b = lambda v: 'yes' if v else '—'
    L.append(f"| {g['repo']} | `{g['path']}` | {g['kind']} | {g['bytes']} | {b(g['reads_chapters'])} | "
             f"{b(g['reads_manuscript'])} | {b(g['reads_docs'])} | {b(g['has_coverage'])} | {b(g['has_exit'])} | "
             f"{'YES' if g['passes_empty'] else '—'} | {b(g['has_floor'])} |")

open(os.path.join(OUT, 'INVENTORY.md'), 'w').write('\n'.join(L) + '\n')

# ── console digest ─────────────────────────────────────────────────────
print(f"{len(result['book_projects'])} book projects, {len(result['gate_files'])} gate/check scripts\n")
print("FLOOR VIOLATIONS (chapters with < 3 spoken lines):")
any_v = False
for p in result['book_projects']:
    if p['floor_violations']:
        any_v = True
        print(f"  {p['repo']}/{p['path']}: {len(p['floor_violations'])} → {', '.join(p['floor_violations'][:6])}")
if not any_v:
    print("  none")
print("\nORPHANS (reader edition published with no author edition):")
any_o = False
for p in result['book_projects']:
    if p['orphans']:
        any_o = True
        print(f"  {p['repo']}/{p['path']}: {len(p['orphans'])} → {', '.join(p['orphans'][:6])}")
if not any_o:
    print("  none")
print("\nGATES THAT PASS EMPTY:")
any_e = False
for g in result['gate_files']:
    if g['passes_empty']:
        any_e = True
        print(f"  {g['repo']}/{g['path']}")
if not any_e:
    print("  none")
print("\nGATES WITH NO COVERAGE LINE (excluding selftests):")
for g in result['gate_files']:
    if not g['has_coverage'] and g['kind'] != 'selftest':
        print(f"  {g['repo']}/{g['path']}  ({g['bytes']}b)")
