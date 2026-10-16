#!/usr/bin/env python3
"""Desk navigation regressions; fixtures never touch the real desk."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('desk_check', Path(__file__).with_name('check.py'))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class DeskTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'docs').mkdir()
        (self.root / 'reports').mkdir()
        self.write('repos.txt', '# THE ACCOUNT — 2 repositories\nalpha\nbeta\n')
        self.write('README.md', '# Desk\nTwo repositories\n[records](reports/README.md)')
        self.write('docs/index.html', '<p>A two-repository account</p>')
        self.write('reports/README.md', '# Records\n')

    def write(self, path, text):
        (self.root / path).write_text(text, encoding='utf-8')

    def test_clean(self):
        self.assertEqual(checker.check(self.root), [])

    def test_stale_page(self):
        self.write('docs/index.html', '<b>twelve</b> repositories')
        self.assertTrue(checker.check(self.root))

    def test_missing_count(self):
        self.write('README.md', '# Desk')
        self.assertTrue(checker.check(self.root))

    def test_duplicate_map(self):
        self.write('repos.txt', '# THE ACCOUNT — 2 repositories\nalpha\nalpha\n')
        self.assertTrue(checker.check(self.root))

    def test_stale_header(self):
        self.write('repos.txt', '# THE ACCOUNT — 3 repositories\nalpha\nbeta\n')
        self.assertTrue(checker.check(self.root))

    def test_broken_report_link(self):
        self.write('reports/README.md', '[receipt](missing.md)')
        self.assertTrue(checker.check(self.root))

    def test_historical_text_not_rewritten(self):
        self.write('reports/README.md', 'Published when there were twelve repositories.')
        self.assertEqual(checker.check(self.root), [])

    def test_remote_link_not_local_file(self):
        self.write('reports/README.md', '[remote](https://example.com/report)')
        self.assertEqual(checker.check(self.root), [])


if __name__ == '__main__':
    unittest.main()
