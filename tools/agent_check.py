#!/usr/bin/env python3
"""Validate the agent navigation contract without executing registry commands.

Local-only by default. --root requires a complete sibling Git checkout set and
validates declared evidence/source/command paths at the revisions actually read.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
START_URL = 'https://github.com/gm5206663-bit/the-authors-desk/blob/main/agents/START-HERE.md'
PAGES = ('START-HERE.md', 'AUTHORITY-AND-STATE.md', 'PERMISSIONS.md',
         'TASK-ROUTES.md', 'COORDINATION.md', 'EVIDENCE-AND-SECURITY.md',
         'HANDOFF-AND-DELIVERY.md', 'CHECKS.md', 'ONBOARDING.md', 'REPOSITORIES.md', 'examples/README.md',
         'examples/NAVIGATION-REPAIR.md', 'examples/CONTINUITY-CONFLICT.md',
         'examples/CHAPTER-WORKFLOW.md')
FIELDS = {
    'HANDOFF.md': ('Goal', 'Authorization', 'Target', 'Base revision', 'Delivered revision',
                   'Files changed', 'Work completed', 'Checks run', 'Known failures',
                   'Pending decisions', 'Next safe action'),
    'TASK-CLAIM.md': ('Task ID', 'Agent label', 'Goal', 'Authorization', 'Target',
                      'Base revision', 'Files in scope', 'Started UTC',
                      'Next checkpoint UTC', 'Overlap check', 'Status', 'Handoff location'),
    'DECISION.md': ('Question', 'Status', 'Source evidence', 'Authority class',
                    'Author wording', 'Scope', 'Options and consequences',
                    'Dependent work stopped', 'Next safe action'),
    'SOURCE-RECEIPT.md': ('Claim', 'Source URL or repository', 'Revision or edition',
                         'Path and location', 'Accessed UTC', 'Source tier',
                         'Quotation or summary', 'Uncertainty', 'Authorization scope'),
    'CHECK-RECEIPT.md': ('Purpose', 'Command', 'Working directory', 'Revision',
                        'Actual exit status', 'Coverage', 'Evidence location',
                        'Known failures', 'Not-run checks', 'Interpretation'),
}
LINK = re.compile(r'\]\(([^)\s]+)\)|(?:href|src)="([^"]+)"')
SLUG = re.compile(r'[A-Za-z0-9][A-Za-z0-9_.-]*\Z')


def safe_path(value):
    if not isinstance(value, str) or not value or '\\' in value:
        return False
    return (not value.startswith('/') and not re.match(r'^[A-Za-z]+:', value)
            and all(part not in ('', '.', '..') for part in value.rstrip('/').split('/')))


def within(base, relative):
    if not safe_path(relative):
        return None
    base = Path(base).resolve()
    target = (base / relative).resolve()
    return target if target.is_relative_to(base) else None


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def repo_names(root):
    return [line.strip() for line in (root / 'repos.txt').read_text().splitlines()
            if line.strip() and not line.lstrip().startswith('#')]


def validate_registry(data, names):
    errors = []
    if data.get('schema_version') != 1 or data.get('owner') != 'gm5206663-bit':
        errors.append('registry: unsupported schema or owner')
    repositories = data.get('repositories', [])
    known = [row.get('name') for row in repositories]
    if len(known) != len(set(known)) or set(known) != set(names):
        errors.append('registry: repository set differs from repos.txt or contains duplicates')
    commands = set()
    for row in repositories:
        name = row.get('name', '')
        if not isinstance(name, str) or not SLUG.fullmatch(name):
            errors.append('registry: unsafe repository name')
        for key in ('purpose', 'entrypoint', 'required_read', 'current_state', 'commands', 'boundaries'):
            if key not in row:
                errors.append(f'{name}: missing {key}')
        if row.get('entrypoint') != 'AGENTS.md':
            errors.append(f'{name}: missing conventional root entrypoint')
        for key in ('required_read', 'current_state'):
            values = row.get(key, [])
            if not isinstance(values, list) or any(not safe_path(p) for p in values):
                errors.append(f'{name}: unsafe {key} path list')
        if not row.get('boundaries'):
            errors.append(f'{name}: no explicit boundary')
        for command in row.get('commands', []):
            ident, argv = command.get('id'), command.get('argv')
            if not ident or ident in commands:
                errors.append(f'{name}: duplicate or missing command id')
            commands.add(ident)
            if (not isinstance(argv, list) or len(argv) < 2
                    or any(not isinstance(a, str) for a in argv)
                    or argv[0] not in ('python3', 'bash', 'sh')
                    or not safe_path(argv[1])
                    or argv[1].startswith('-')
                    or not argv[1].endswith('.py' if argv[0] == 'python3' else '.sh')):
                errors.append(f'{name}: unsafe command structure')
            if not command.get('purpose'):
                errors.append(f'{name}: command purpose missing')
    projects = data.get('projects', [])
    ids = [p.get('id') for p in projects]
    if not ids or len(ids) != len(set(ids)):
        errors.append('registry: duplicate or missing project routes')
    for project in projects:
        if project.get('repo') not in known or not safe_path(project.get('path')):
            errors.append('registry: invalid project owner/path')
        for key in ('read', 'current_state'):
            if not project.get(key) or any(not safe_path(p) for p in project[key]):
                errors.append('registry: invalid project source list')
        if not project.get('restriction'):
            errors.append('registry: project restriction missing')
    tasks = data.get('tasks', [])
    ids = [t.get('id') for t in tasks]
    if not ids or len(ids) != len(set(ids)):
        errors.append('registry: duplicate or missing task routes')
    for task in tasks:
        if not task.get('owners') or not set(task['owners']).issubset(known):
            errors.append('registry: unknown task owner')
        if not set(task.get('commands', [])).issubset(commands):
            errors.append('registry: unknown task command')
        if task.get('guide') not in PAGES or not task.get('approval'):
            errors.append('registry: invalid task guide/approval boundary')
    return errors


def validate_onboarding(data, names):
    errors = []
    cases = data.get('cases', [])
    ids = [c.get('id') for c in cases]
    expected = {'current-edge', 'proposal-not-approval', 'frozen-reference', 'agent-ownership',
                'reproduce-check', 'lifecycle-conflict', 'untrusted-instruction', 'resume-handoff'}
    if data.get('schema_version') != 1 or set(ids) != expected or len(ids) != len(set(ids)):
        errors.append('onboarding: missing/duplicate required exercises or unsupported schema')
    for case in cases:
        if not case.get('question') or not case.get('expected_behavior') or not case.get('forbidden_actions'):
            errors.append('onboarding: missing question, answer guidance or forbidden behavior')
        if not case.get('evidence'):
            errors.append('onboarding: missing evidence')
        for source in case.get('evidence', []):
            if source.get('repo') not in names or not safe_path(source.get('path')):
                errors.append('onboarding: invalid evidence reference')
    return errors


def markdown_links(path, boundary, account_root=None, names=()):
    errors = []
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    for match in LINK.finditer(text):
        target = match.group(1) or match.group(2)
        url = urlsplit(target)
        if url.scheme or target.startswith('//'):
            if not account_root or url.netloc != 'github.com':
                continue
            parts = unquote(url.path).strip('/').split('/')
            if len(parts) < 2 or parts[0] != 'gm5206663-bit':
                continue
            if parts[1] not in names:
                errors.append(f'{path.name}: unknown account repository in {target}')
                continue
            if len(parts) >= 4 and parts[2] in ('blob', 'tree') and parts[3] == 'main':
                rel = '/'.join(parts[4:])
                if rel:
                    resolved = within(account_root / parts[1], rel)
                    if resolved is None or not resolved.exists():
                        errors.append(f'{path.name}: missing cross-repo link {target}')
            continue
        if not url.path:
            continue
        resolved = (path.parent / unquote(url.path)).resolve()
        if not resolved.is_relative_to(boundary.resolve()) or not resolved.exists():
            errors.append(f'{path.name}: missing/escaping local link {target}')
    return errors


def validate_handoff(text, filled=True):
    errors = []
    sections = {}
    for match in re.finditer(r'^## ([^\n]+)\n(.*?)(?=^## |\Z)', text, flags=re.M | re.S):
        name, body = match.groups()
        if name in sections:
            errors.append(f'handoff: duplicate {name}')
        sections[name] = body.strip()
    for name in FIELDS['HANDOFF.md']:
        if name not in sections:
            errors.append(f'handoff: missing {name}')
        elif filled and (not sections[name] or re.fullmatch(r'<[^>]*>|\[[^\]]*\]|TBD|TODO', sections[name], re.I)):
            errors.append(f'handoff: unfilled {name}')
    return errors


def render_index(data):
    lines = ['# Repository and project routes', '',
             'Generated from [registry.json](registry.json); edit that source, then run',
             '`python3 tools/build_agent_index.py` from the desk root. No live story numbers live here.', '',
             '| Repository entry | Owns | Current source locations |', '|---|---|---|']
    def link(repo, path, label=None):
        kind = 'tree' if path.endswith('/') else 'blob'
        return f'[{label or path}](https://github.com/gm5206663-bit/{repo}/{kind}/main/{path})'
    for row in data['repositories']:
        sources = ' · '.join(link(row['name'], p) for p in row['current_state']) or 'No narrative state'
        lines.append(f"| {link(row['name'], 'AGENTS.md', row['name'])} | {row['purpose']} | {sources} |")
    lines += ['', '## Explicit serial routes', '',
              'Other serials: use the kit cockpit and their local instructions. A route is not permission.', '',
              '| Project | Read next | State source | Boundary |', '|---|---|---|---|']
    for row in data['projects']:
        reads = ' · '.join(link(row['repo'], row['path'] + '/' + p, p) for p in row['read'])
        states = ' · '.join(link(row['repo'], row['path'] + '/' + p, p) for p in row['current_state'])
        lines.append(f"| {row['id']} | {reads} | {states} | {row['restriction']} |")
    lines += ['', '[Back to start](START-HERE.md)', '']
    return '\n'.join(lines)


def check(root=ROOT, account_root=None):
    root = Path(root)
    errors = []
    names = repo_names(root)
    registry = read_json(root / 'agents/registry.json')
    onboarding = read_json(root / 'agents/onboarding.json')
    errors += validate_registry(registry, names)
    errors += validate_onboarding(onboarding, names)
    index = root / 'agents/REPOSITORIES.md'
    if not index.exists() or index.read_text(encoding='utf-8') != render_index(registry):
        errors.append('guidance: generated repository index differs from registry')
    for page in PAGES:
        path = root / 'agents' / page
        if not path.is_file() or not path.read_text().strip():
            errors.append(f'guidance: required page missing/empty: {page}')
    for name, fields in FIELDS.items():
        path = root / 'agents/templates' / name
        if not path.is_file():
            errors.append(f'guidance: missing template {name}')
            continue
        text = path.read_text()
        for field in fields:
            if f'## {field}\n' not in text:
                errors.append(f'template {name}: missing {field}')
    for path in [root / 'AGENTS.md', *(root / 'agents').rglob('*.md')]:
        if not path.is_file():
            errors.append(f'guidance: missing {path.name}')
        else:
            errors += markdown_links(path, root, account_root, names)
    heads = {}
    if account_root is not None:
        account_root = Path(account_root)
        actual = {p.name for p in account_root.iterdir() if p.is_dir() and (p / '.git').exists()}
        if actual != set(names):
            errors.append(f'account root: checkout set mismatch; missing={sorted(set(names)-actual)}, extra={sorted(actual-set(names))}')
        for row in registry.get('repositories', []):
            name = row.get('name', '')
            if not isinstance(name, str) or not SLUG.fullmatch(name):
                continue
            base = account_root / name
            if not (base / '.git').exists():
                errors.append(f'{name}: missing Git checkout')
                continue
            try:
                head = subprocess.check_output(['git', '-C', str(base), 'rev-parse', 'HEAD'], text=True, stderr=subprocess.DEVNULL, timeout=15).strip()
                if not re.fullmatch(r'[0-9a-f]{40}', head):
                    raise ValueError('invalid HEAD')
                dirty = subprocess.check_output(['git', '-C', str(base), 'status', '--porcelain'], text=True, stderr=subprocess.DEVNULL, timeout=15).strip()
                heads[name] = head + (' (working tree modified)' if dirty else '')
            except (ValueError, subprocess.SubprocessError):
                errors.append(f'{name}: cannot resolve Git HEAD')
            paths = [row.get('entrypoint')] + row.get('required_read', []) + row.get('current_state', [])
            paths += [cmd.get('argv', [None, None])[1] for cmd in row.get('commands', []) if len(cmd.get('argv', [])) >= 2]
            for rel in paths:
                target = within(base, rel)
                if target is None or not target.exists():
                    errors.append(f'{name}: missing/unsafe registered path {rel}')
            entry = base / 'AGENTS.md'
            if entry.is_file():
                if START_URL not in entry.read_text(encoding='utf-8'):
                    errors.append(f'{name}: entrypoint does not link the canonical start')
                errors += markdown_links(entry, base, account_root, names)
        for project in registry.get('projects', []):
            base = within(account_root / project.get('repo', ''), project.get('path'))
            for rel in project.get('read', []) + project.get('current_state', []):
                target = within(base, rel) if base else None
                if target is None or not target.exists():
                    errors.append(f'project {project.get("id")}: missing/unsafe source {rel}')
        for case in onboarding.get('cases', []):
            for source in case.get('evidence', []):
                if source.get('repo') not in names:
                    continue
                target = within(account_root / source['repo'], source.get('path'))
                if target is None or not target.exists():
                    errors.append(f'onboarding {case.get("id")}: missing evidence {source.get("path")}')
    return errors, heads


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, help='complete sibling checkout root; no network fetch')
    parser.add_argument('--handoff', type=Path, help='also require a filled standard handoff')
    args = parser.parse_args()
    try:
        errors, heads = check(ROOT, args.root)
        if args.handoff:
            errors += validate_handoff(args.handoff.read_text(encoding='utf-8'))
    except (OSError, ValueError, KeyError, TypeError, AttributeError, IndexError) as error:
        errors, heads = [f'guidance validation could not complete: {error}'], {}
    for error in errors:
        print('FAIL: ' + error)
    scope = f'{len(heads)} Git checkouts; declared sources/commands/evidence inspected' if args.root else 'local structure only; cross-repo sources NOT checked'
    print(f'AGENT GUIDANCE: {len(errors)} error(s) — {scope}')
    for name, head in sorted(heads.items()):
        print(f'  {name} {head}')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
