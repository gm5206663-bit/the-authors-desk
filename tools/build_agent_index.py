#!/usr/bin/env python3
"""Render path-only agent navigation from its single registry source."""
from agent_check import ROOT, read_json, render_index

if __name__ == '__main__':
    target = ROOT / 'agents/REPOSITORIES.md'
    target.write_text(render_index(read_json(ROOT / 'agents/registry.json')), encoding='utf-8')
    print('Rendered agents/REPOSITORIES.md')
