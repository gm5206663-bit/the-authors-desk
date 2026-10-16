#!/usr/bin/env python3
"""Offline red/green regressions for the agent onboarding contract.

Fixtures model missing sources, bad routes and unsafe paths, not an agent's
literary comprehension. No network, story edits or registry command execution.
"""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import agent_check as ac
import agent_sources as sources


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.registry = ac.read_json(ac.ROOT / 'agents/registry.json')
        self.names = ac.repo_names(ac.ROOT)
        self.onboarding = ac.read_json(ac.ROOT / 'agents/onboarding.json')

    def errors(self):
        return ac.validate_registry(self.registry, self.names)

    def test_clean_registry(self):
        self.assertEqual(self.errors(), [])

    def test_missing_repository(self):
        self.registry['repositories'].pop()
        self.assertTrue(self.errors())

    def test_duplicate_repository(self):
        self.registry['repositories'].append(copy.deepcopy(self.registry['repositories'][0]))
        self.assertTrue(self.errors())

    def test_unsafe_repository(self):
        self.registry['repositories'][0]['name'] = '../escape'
        self.assertTrue(self.errors())

    def test_unsafe_source_path(self):
        self.registry['repositories'][0]['current_state'] = ['../secret']
        self.assertTrue(self.errors())

    def test_missing_permission_boundary(self):
        self.registry['repositories'][0]['boundaries'] = []
        self.assertTrue(self.errors())

    def test_shell_command_not_accepted(self):
        self.registry['repositories'][0]['commands'][0]['argv'] = ['sh', '-c', 'unsafe']
        self.assertTrue(self.errors())

    def test_duplicate_command_id(self):
        commands = self.registry['repositories'][0]['commands']
        commands[1]['id'] = commands[0]['id']
        self.assertTrue(self.errors())

    def test_unowned_project(self):
        self.registry['projects'][0]['repo'] = 'unknown'
        self.assertTrue(self.errors())

    def test_unknown_task_command(self):
        self.registry['tasks'][0]['commands'] = ['not-a-command']
        self.assertTrue(self.errors())

    def test_unknown_task_owner(self):
        self.registry['tasks'][0]['owners'] = ['unknown']
        self.assertTrue(self.errors())

    def test_bad_task_guide(self):
        self.registry['tasks'][0]['guide'] = 'missing.md'
        self.assertTrue(self.errors())

    def test_clean_onboarding_key(self):
        self.assertEqual(ac.validate_onboarding(self.onboarding, self.names), [])

    def test_missing_exercise(self):
        self.onboarding['cases'].pop()
        self.assertTrue(ac.validate_onboarding(self.onboarding, self.names))

    def test_duplicate_exercise(self):
        self.onboarding['cases'].append(copy.deepcopy(self.onboarding['cases'][0]))
        self.assertTrue(ac.validate_onboarding(self.onboarding, self.names))

    def test_missing_answer_behavior(self):
        self.onboarding['cases'][0]['expected_behavior'] = ''
        self.assertTrue(ac.validate_onboarding(self.onboarding, self.names))

    def test_unknown_evidence_owner(self):
        self.onboarding['cases'][0]['evidence'][0]['repo'] = 'unknown'
        self.assertTrue(ac.validate_onboarding(self.onboarding, self.names))

    def test_evidence_path_escape(self):
        self.onboarding['cases'][0]['evidence'][0]['path'] = '../private'
        self.assertTrue(ac.validate_onboarding(self.onboarding, self.names))

    def test_blank_template_not_valid_handoff(self):
        text = (ac.ROOT / 'agents/templates/HANDOFF.md').read_text()
        self.assertTrue(ac.validate_handoff(text))
        self.assertEqual(ac.validate_handoff(text, filled=False), [])

    def test_filled_handoff(self):
        text = '\n'.join('## ' + field + '\nActual evidence or explicitly none.\n' for field in ac.FIELDS['HANDOFF.md'])
        self.assertEqual(ac.validate_handoff(text), [])

    def test_missing_handoff_field(self):
        self.assertTrue(ac.validate_handoff('## Goal\nA task\n'))

    def test_duplicate_handoff_field(self):
        text = '\n'.join('## ' + field + '\nActual evidence.\n' for field in ac.FIELDS['HANDOFF.md'])
        self.assertTrue(ac.validate_handoff(text + '\n## Goal\nAnother\n'))

    def test_paths(self):
        for path in ('../x', '/x', 'C:\\x', 'https://example.com', 'a/../x', 'a//b'):
            with self.subTest(path=path):
                self.assertFalse(ac.safe_path(path))
        self.assertTrue(ac.safe_path('foundation/STATUS.md'))


class GuidanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'desk'
        shutil.copytree(ac.ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def errors(self):
        return ac.check(self.root)[0]

    def test_clean_guidance_bundle(self):
        self.assertEqual(self.errors(), [])

    def test_bootstrap_missing(self):
        (self.root / 'agents/BOOTSTRAP.txt').unlink()
        self.assertTrue(self.errors())

    def test_bootstrap_loses_canonical_link(self):
        (self.root / 'agents/BOOTSTRAP.txt').write_text('Unusable stale packet')
        self.assertTrue(self.errors())

    def test_required_page_missing(self):
        (self.root / 'agents/PERMISSIONS.md').unlink()
        self.assertTrue(self.errors())

    def test_template_field_missing(self):
        p = self.root / 'agents/templates/HANDOFF.md'
        p.write_text(p.read_text().replace('## Next safe action', '## Something else'))
        self.assertTrue(self.errors())

    def test_stale_generated_index(self):
        p = self.root / 'agents/REPOSITORIES.md'; p.write_text(p.read_text() + '\nStale edit\n')
        self.assertTrue(self.errors())

    def test_broken_guidance_link(self):
        p = self.root / 'agents/START-HERE.md'; p.write_text(p.read_text() + '\n[bad](missing.md)\n')
        self.assertTrue(self.errors())

    def test_local_link_escape(self):
        p = self.root / 'agents/START-HERE.md'; p.write_text(p.read_text() + '\n[bad](../../outside.md)\n')
        self.assertTrue(self.errors())

    def test_symlink_source_escape(self):
        outside = Path(self.temp.name) / 'outside.md'; outside.write_text('not a valid local source')
        (self.root / 'escape.md').symlink_to(outside)
        self.assertIsNone(ac.within(self.root, 'escape.md'))

    def make_account(self):
        account = Path(self.temp.name) / 'account'; account.mkdir()
        registry = ac.read_json(self.root / 'agents/registry.json')
        for row in registry['repositories']:
            base = account / row['name']; (base / '.git').mkdir(parents=True)
            paths = row['required_read'] + row['current_state'] + [row['entrypoint']]
            paths += [cmd['argv'][1] for cmd in row['commands']]
            for relative in paths:
                target = base / relative
                if relative.endswith('/'):
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text('fixture evidence\n')
            (base / 'AGENTS.md').write_text('[Start](' + ac.START_URL + ')\n')
        for project in registry['projects']:
            for relative in project['read'] + project['current_state']:
                target = account / project['repo'] / project['path'] / relative
                target.parent.mkdir(parents=True, exist_ok=True); target.write_text('fixture source\n')
        onboarding = ac.read_json(self.root / 'agents/onboarding.json')
        for case in onboarding['cases']:
            for source in case['evidence']:
                target = account / source['repo'] / source['path']
                if not target.exists():
                    target.parent.mkdir(parents=True, exist_ok=True); target.write_text('fixture evidence\n')
        # Cross-repository Markdown pointers must also resolve in fixtures.
        for relative in ('agents/START-HERE.md', 'agents/registry.json'):
            target = account / 'the-authors-desk' / relative
            target.parent.mkdir(parents=True, exist_ok=True); target.write_text('fixture source\n')
        return account

    def account_errors(self, account):
        with patch.object(ac.subprocess, 'check_output', return_value='a' * 40 + '\n'):
            return ac.check(self.root, account)[0]

    def test_cross_repo_clean(self):
        account = self.make_account()
        self.assertEqual(self.account_errors(account), [])

    def test_missing_checkout_is_not_clean(self):
        account = self.make_account(); shutil.rmtree(account / 'sara')
        self.assertTrue(self.account_errors(account))

    def test_extra_checkout_detected(self):
        account = self.make_account(); (account / 'unexpected/.git').mkdir(parents=True)
        self.assertTrue(self.account_errors(account))

    def test_missing_command_script(self):
        account = self.make_account(); (account / 'sara/tools/check.py').unlink()
        self.assertTrue(self.account_errors(account))

    def test_missing_current_state(self):
        account = self.make_account(); (account / 'soul-land-universal-kit/soul_land_4_fire_phoenix/foundation/CURRENT_STATE_MANIFEST.json').unlink()
        self.assertTrue(self.account_errors(account))

    def test_missing_onboarding_evidence(self):
        account = self.make_account(); (account / 'pokemon-adaptation/.github/workflows/stage0-gate.yml').unlink()
        self.assertTrue(self.account_errors(account))

    def test_entrypoint_lost_navigation(self):
        account = self.make_account(); (account / 'sara/AGENTS.md').write_text('# No route\n')
        self.assertTrue(self.account_errors(account))

    def test_command_values_never_executed(self):
        with patch.object(ac.subprocess, 'run', side_effect=AssertionError('must not execute registry commands')):
            self.assertEqual(self.errors(), [])


class SourcePreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'source'
        self.root.mkdir(); (self.root / '.git').mkdir()
        (self.root / 'marker.txt').write_text('triggering checkout, not remote main')
        self.dest = Path(self.temp.name) / 'fresh'

    def prepare(self):
        with patch.object(sources, 'ROOT', self.root), \
             patch.object(sources, 'check', return_value=([], {})), \
             patch.object(sources, 'read_json', return_value={'repositories': [{'name': 'the-authors-desk'}, {'name': 'sara'}]}):
            return sources.prepare(self.dest)

    def test_existing_source_set_refused(self):
        self.dest.mkdir(); (self.dest / 'old').write_text('stale')
        with self.assertRaises(ValueError):
            self.prepare()

    def test_inside_checkout_refused(self):
        self.dest = self.root / 'recursive'
        with self.assertRaises(ValueError):
            self.prepare()

    def test_parent_of_checkout_refused(self):
        self.dest = self.root.parent
        with self.assertRaises(ValueError):
            self.prepare()

    def test_triggering_desk_preserved(self):
        with patch.object(sources.subprocess, 'run'):
            self.prepare()
        self.assertEqual((self.dest / 'the-authors-desk/marker.txt').read_text(), 'triggering checkout, not remote main')

    def test_only_public_tokenless_clone(self):
        with patch.object(sources.subprocess, 'run') as run:
            self.prepare()
        argv = run.call_args.args[0]
        self.assertIn('https://github.com/gm5206663-bit/sara.git', argv)
        self.assertIn('credential.helper=', argv)
        self.assertFalse(run.call_args.kwargs.get('shell', False))

    def test_failed_clone_is_fatal(self):
        with patch.object(sources.subprocess, 'run', side_effect=ac.subprocess.CalledProcessError(128, ['git'])):
            with self.assertRaises(ac.subprocess.CalledProcessError):
                self.prepare()


if __name__ == '__main__':
    unittest.main()
