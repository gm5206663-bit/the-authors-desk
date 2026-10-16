#!/usr/bin/env python3
"""Check the desk's current navigation and account-map consistency.

Historical reports are not rewritten or treated as current claims. This local
check cannot discover newly created GitHub repositories; the account-wide
Control Centre does that against a fresh inventory.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NUMBERS = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split()
COUNT = re.compile(r'\b(\d+|' + '|'.join(NUMBERS) + r')(?:-|\s+)repositor(?:y|ies)\b', re.I)
LINK = re.compile(r'\]\(([^)\s]+)\)|(?:href|src)="([^"]+)"')


def check(root=ROOT):
    errors = []
    lines = (root / 'repos.txt').read_text(encoding='utf-8').splitlines()
    repos = [line.strip() for line in lines if line.strip() and not line.lstrip().startswith('#')]
    if not repos or len(repos) != len(set(repos)):
        errors.append('repos.txt is empty or contains duplicate names')
    if any(not re.fullmatch(r'[A-Za-z0-9_.-]+', name) for name in repos):
        errors.append('repos.txt contains an unsafe name')
    header = next((line for line in lines if line.startswith('# THE ACCOUNT')), '')
    if not re.search(rf'\b{len(repos)} repositories\b', header):
        errors.append('repos.txt header does not match its entries')
    for relative in ('README.md', 'docs/index.html'):
        text = (root / relative).read_text(encoding='utf-8')
        visible = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', text))
        matches = list(COUNT.finditer(visible))
        if not matches:
            errors.append(f'{relative}: repository count is missing')
        for match in matches:
            word = match.group(1).lower()
            count = int(word) if word.isdigit() else NUMBERS.index(word)
            if count != len(repos):
                errors.append(f'{relative}: {match.group(0)} disagrees with {len(repos)} map entries')
    for relative in ('README.md', 'docs/index.html', 'reports/README.md'):
        path = root / relative
        text = path.read_text(encoding='utf-8')
        text = re.sub(r'```.*?```', '', text, flags=re.S)
        for match in LINK.finditer(text):
            target = match.group(1) or match.group(2)
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith(('#', '//')):
                continue
            local = target.split('#', 1)[0].split('?', 1)[0]
            if local and not (path.parent / local).exists():
                errors.append(f'{relative}: missing local target {target}')
    return errors


def main():
    errors = check()
    for error in errors:
        print('FAIL: ' + error)
    print(f'DESK CHECK: {len(errors)} error(s); current front doors + report index + map')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
