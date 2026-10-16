#!/usr/bin/env python3
"""Prepare a fresh public source set for guidance checks; never execute registry commands.

The desk checkout is copied at the triggering revision, not replaced by remote
main. Other repositories are cloned tokenlessly at the public revisions read.
This is a dependency check, not account discovery or a history backup.
"""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
from agent_check import ROOT, check, read_json


def prepare(destination):
    destination = Path(destination).resolve()
    if destination.is_relative_to(ROOT.resolve()) or ROOT.resolve().is_relative_to(destination):
        raise ValueError('source root must be separate from the desk checkout')
    if destination.exists() and any(destination.iterdir()):
        raise ValueError('destination must be new or empty; refusing stale sources')
    errors, _ = check(ROOT)
    if errors:
        raise ValueError('local guidance invalid: ' + '; '.join(errors))
    data = read_json(ROOT / 'agents/registry.json')
    destination.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
    for row in data['repositories']:
        name = row['name']
        target = destination / name
        if name == 'the-authors-desk':
            shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'), symlinks=True)
        else:
            subprocess.run(['git', '-c', 'credential.helper=', 'clone', '-q', '--depth', '1',
                            f'https://github.com/gm5206663-bit/{name}.git', str(target)],
                           check=True, timeout=180, env=env)
        print('prepared ' + name, flush=True)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    try:
        prepare(args.root)
    except (OSError, ValueError, subprocess.SubprocessError) as error:
        print('SOURCE SET INCOMPLETE: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
