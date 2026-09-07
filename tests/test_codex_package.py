# SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
# Required Notice: Copyright (c) 2026 Hyeonoh Hur (https://github.com/H-Hur/study-kit)
"""Regression coverage for the two installable editions and relocated Codex skills."""
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_codex', ROOT / 'scripts/build_codex.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
ROLES = {'source-scout', 'drill-designer', 'textbook-auditor', 'comprehension-auditor'}
LEARNING = {'learner-intake', 'source-index', 'curriculum-design',
            'textbook-authoring', 'textbook-revision', 'textbook-publish'}
ENTRY_POINTS = {'study-start', 'study-session', 'study-review', 'study-publish'}


class CodexPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = build.render()

    def skill(self, name):
        return self.files[Path('skills') / name / 'SKILL.md'].decode()

    def test_both_packages_retain_their_components_and_share_version(self):
        source_files = {p: hashlib.sha256(p.read_bytes()).digest()
                        for p in build.SOURCE.rglob('*') if p.is_file()}
        build.render()
        self.assertEqual(source_files, {p: hashlib.sha256(p.read_bytes()).digest()
                                        for p in source_files})
        self.assertEqual(ROLES, {p.stem for p in (build.SOURCE / 'agents').glob('*.md')})
        self.assertEqual(ENTRY_POINTS, {p.stem for p in (build.SOURCE / 'commands').glob('*.md')})
        self.assertEqual(LEARNING, {p.parent.name for p in (build.SOURCE / 'skills').glob('*/SKILL.md')})
        for name in ROLES:
            self.assertIn('\ntools:', (build.SOURCE / 'agents' / (name + '.md')).read_text())
        self.assertIn('~/.claude/projects/', (build.SOURCE / 'agents/comprehension-auditor.md').read_text())
        source_manifest = json.loads((build.SOURCE / '.claude-plugin/plugin.json').read_text())
        codex_manifest = json.loads(self.files[Path('.codex-plugin/plugin.json')])
        self.assertEqual(source_manifest['version'], codex_manifest['version'])
        self.assertEqual('./skills/', codex_manifest['skills'])
        self.assertEqual(ENTRY_POINTS | LEARNING | ROLES,
                         {p.parent.name for p in self.files if p.name == 'SKILL.md'})

    def test_installed_editions_ship_scope_and_complete_license_texts(self):
        for relative in ['LICENSE', 'licenses/PolyForm-Noncommercial-1.0.0.txt',
                         'licenses/CC-BY-NC-SA-4.0.txt']:
            path = Path(relative)
            self.assertEqual((build.SOURCE / path).read_bytes(), self.files[path])
            incomplete = dict(self.files)
            del incomplete[path]
            with self.assertRaisesRegex(ValueError, 'Missing bundled license'):
                build.validate(incomplete)
        manifest = json.loads(self.files[Path('.codex-plugin/plugin.json')])
        self.assertEqual('PolyForm-Noncommercial-1.0.0 AND CC-BY-NC-SA-4.0', manifest['license'])

    def test_relocated_install_resolves_every_bundled_link(self):
        with tempfile.TemporaryDirectory(prefix='study kit relocated ') as tmp:
            installed = Path(tmp).resolve() / 'cache' / 'new-version' / 'study-kit-codex'
            for relative, content in self.files.items():
                p = installed / relative
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(content)
            for relative in self.files:
                if relative.suffix != '.md' or 'templates' in relative.parts:
                    continue
                p = installed / relative
                for match in build.LINK.finditer(p.read_text()):
                    target = match[2].split('#')[0]
                    if not target or ':' in target or target.startswith('/'):
                        continue
                    resolved = (p.parent / target).resolve()
                    self.assertTrue(resolved.is_relative_to(installed), (relative, target))
                    self.assertTrue(resolved.is_file(), (relative, target))
            for name in ENTRY_POINTS | LEARNING | ROLES:
                self.assertIn('(../../docs/codex-runtime.md)', self.skill(name))
            self.assertFalse((installed / 'docs/runtime.md').exists())

    def test_workflows_link_to_the_procedures_they_need(self):
        workflows = {
            'study-start': {'learner-intake', 'source-index', 'source-scout', 'curriculum-design'},
            'study-session': {'comprehension-auditor', 'drill-designer'},
            'study-review': {'comprehension-auditor'},
            'study-publish': {'textbook-authoring', 'textbook-auditor', 'textbook-publish'},
            'textbook-authoring': {'drill-designer', 'textbook-auditor'},
            'textbook-revision': {'comprehension-auditor', 'textbook-publish'},
        }
        for entry, dependencies in workflows.items():
            for dependency in dependencies:
                self.assertIn(f'(../{dependency}/SKILL.md)', self.skill(entry), (entry, dependency))
        start = self.skill('study-start')
        for name in ['PROJECT-AGENTS.md', 'worklog.md', 'toolbox-log.md', 'inbox-README.md']:
            self.assertIn(f'(../../templates/{name})', start)
        self.assertIn('docs/study-kit-style-rules.md', start)

    def test_role_contracts_cover_dispatch_evidence_and_write_ownership(self):
        runtime = self.files[Path('docs/codex-runtime.md')].decode()
        for name in ROLES:
            role = self.skill(name)
            self.assertIn('## Codex role execution', role)
            self.assertIn('do not delegate this same role again', role)
            self.assertIn(f'(../skills/{name}/SKILL.md)', runtime)
        self.assertIn('main session conducts intake', self.skill('learner-intake'))
        self.assertIn('evidence is incomplete', self.skill('comprehension-auditor'))
        self.assertNotIn('~/.claude/', self.skill('comprehension-auditor'))
        self.assertIn('does not edit the textbook or other existing files', self.skill('textbook-auditor'))

    def test_host_model_guides_and_historical_limits_are_distinct(self):
        claude = (build.SOURCE / 'docs/runtime.md').read_text()
        codex = self.files[Path('docs/codex-runtime.md')].decode()
        self.assertIn('Opus at high reasoning', claude)
        for setting in ['gpt-6-astra', 'gpt-5.6-sol', '`high`', '`xhigh`']:
            self.assertIn(setting, codex)
        self.assertIn("inherit the parent's selected model", codex)
        self.assertIn('Respect a model choice', codex)
        budget = self.files[Path('docs/budget.md')].decode()
        current = budget.split('## Rules for current work')[1].split('## Historical operating rules')[0]
        self.assertIn('An unknown token budget alone is not a reason to stop', current)
        self.assertNotIn('150k', current)
        history = budget.split('## Historical operating rules')[1].split('## The one-line check')[0]
        for rule in ['> **① Keep the artifact written in one response under 8k tokens.',
                     '> **② Do not start unless the remaining budget is at least three times',
                     '>   **150k or more** left.']:
            self.assertIn(rule, history)
        self.assertIn('original Claude Code course', self.skill('source-index'))

    def test_conversion_does_not_rewrite_existing_links_or_code_samples(self):
        target = Path('skills/study-session/SKILL.md')
        value = ('---\nname: example\ndescription: Use `source-scout`\n---\n'
                 '`source-scout` and [`drill-designer`](../drill-designer/SKILL.md)\n'
                 '```text\n`source-scout`\n```\n')
        converted = build.link_skill_mentions(value, target)
        self.assertIn('description: Use `source-scout`', converted)
        self.assertIn('[`source-scout`](../source-scout/SKILL.md)', converted)
        self.assertIn('[`drill-designer`](../drill-designer/SKILL.md)', converted)
        self.assertIn('```text\n`source-scout`\n```', converted)

    def test_validator_rejects_broken_host_links_and_foreign_instructions(self):
        path = Path('skills/source-scout/SKILL.md')
        original = self.files[path]
        variants = [
            original.replace(b'../../docs/codex-runtime.md', b'../../docs/missing.md'),
            original.replace(b'## Codex role execution', b'## Unspecified role'),
            original + b'\nRead ~/.claude/projects/current/*.jsonl\n',
            original + b'\nRun /study-kit:study-start\n',
            original.replace(b'name: source-scout', b'name: source-scout\nmodel: opus'),
        ]
        for value in variants:
            files = dict(self.files)
            files[path] = value
            with self.subTest(value=value[-80:]), self.assertRaises(ValueError):
                build.validate(files)


if __name__ == '__main__':
    unittest.main()
