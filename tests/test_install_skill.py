"""Exercise the installer CLI against isolated repository and runtime trees."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install-skill.py"
IDENTITY = SCRIPT.parent.parent / "skills" / "coding-review-loop" / "scripts" / "skill_identity.py"


class InstallSkillTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.script = self.root / "repo" / "scripts" / SCRIPT.name
        self.script.parent.mkdir(parents=True)
        shutil.copyfile(SCRIPT, self.script)
        helper = self.root / "repo" / "skills" / "coding-review-loop" / "scripts" / "skill_identity.py"
        helper.parent.mkdir(parents=True)
        shutil.copyfile(IDENTITY, helper)
        self.source = self.root / "repo" / "skills" / "example"
        (self.source / "references").mkdir(parents=True)
        (self.source / "SKILL.md").write_text('---\nname: example\ndescription: Example\n---\n')
        (self.source / "references" / "contract.md").write_text("Original contract\n")
        self.runtime = self.root / "runtime"

    def run_default_cli(self, *args, code=0, codex_home=None):
        env = dict(os.environ, HOME=str(self.root / "home"))
        env.pop("CODEX_HOME", None)
        if codex_home:
            env["CODEX_HOME"] = str(codex_home)
        result = subprocess.run([sys.executable, "-B", str(self.script), *args],
                                capture_output=True, text=True, timeout=10, env=env)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def test_default_inspection_finds_agents_install_and_reports_multiple_copies(self):
        agents = self.root / "home" / ".agents" / "skills" / "example"
        agents.parent.mkdir(parents=True)
        shutil.copytree(self.source, agents)
        output = self.run_default_cli("--inspect", "example")
        self.assertIn("matches repository", output)
        self.assertIn(str(agents.parent), output)
        self.assertNotIn("runtime missing", output)
        codex_home = self.root / "custom-codex"
        second = codex_home / "skills" / "example"
        shutil.copytree(self.source, second)
        (second / "references" / "contract.md").write_text("Different copy\n")
        output = self.run_default_cli("--inspect", "example", codex_home=codex_home)
        self.assertIn(str(second.parent), output)
        self.assertIn(str(agents.parent), output)
        self.assertIn("differs from repository", output)
        self.assertIn("matches repository", output)
        self.assertIn(str(agents.parent), self.run_default_cli("--list"))

    def test_explicit_inspection_root_and_install_destination_are_preserved(self):
        agents = self.root / "home" / ".agents" / "skills" / "example"
        agents.parent.mkdir(parents=True)
        shutil.copytree(self.source, agents)
        output = self.run_default_cli("--inspect", "example", "--runtime-root", str(self.runtime), code=1)
        self.assertIn("runtime missing", output)
        self.assertNotIn(str(agents.parent), output)
        output = self.run_default_cli("--install", "example", "--dry-run")
        self.assertIn(str(self.root / "home" / ".codex" / "skills"), output)
        self.assertFalse((self.root / "home" / ".codex").exists())

    def test_packaged_identity_runs_from_copy_without_repository_and_detects_drift(self):
        package = self.root / "standalone" / "coding-review-loop"
        shutil.copytree(IDENTITY.parent.parent, package)
        helper = package / "scripts" / "skill_identity.py"

        def receipt():
            result = subprocess.run([sys.executable, "-B", str(helper)], cwd=self.root,
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)

        before_files = sorted(p.relative_to(package) for p in package.rglob("*"))
        first = receipt()
        self.assertEqual(first, receipt())
        self.assertEqual(before_files, sorted(p.relative_to(package) for p in package.rglob("*")))
        self.assertNotIn(str(self.root), json.dumps(first))
        contract = package / "references" / "case-note-shape.md"
        contract.write_text(contract.read_text() + "\nChanged contract\n")
        self.assertNotEqual(first["fingerprint"], receipt()["fingerprint"])
        shutil.copytree(package, self.runtime / "example")
        shutil.rmtree(self.source)
        shutil.copytree(package, self.source)
        output = self.run_cli("--inspect", "example")
        self.assertIn(receipt()["fingerprint"], output)

    def run_cli(self, *args, code=0):
        result = subprocess.run(
            [sys.executable, str(self.script), "--runtime-root", str(self.runtime), *args],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return result.stdout + result.stderr

    def test_copy_matches_and_reference_only_drift_is_detected(self):
        self.run_cli("--install", "example", "--copy")
        output = self.run_cli("--inspect", "example")
        self.assertIn("matches repository", output)
        fingerprints = [line.split(": ", 1)[1] for line in output.splitlines() if "fingerprint:" in line]
        self.assertEqual(fingerprints[0], fingerprints[1])
        self.assertRegex(fingerprints[0], r"^sha256-v1:[0-9a-f]{64}$")
        (self.runtime / "example" / "references" / "contract.md").write_text("Changed\n")
        self.assertIn("differs from repository", self.run_cli("--inspect", "example"))
        self.assertIn("differs from repository", self.run_cli("--list"))

    def test_symlink_tracks_repository_and_broken_link_is_missing(self):
        self.run_cli("--install", "example")
        self.assertTrue((self.runtime / "example").is_symlink())
        (self.source / "references" / "contract.md").write_text("Updated\n")
        self.assertIn("matches repository", self.run_cli("--inspect", "example"))
        (self.runtime / "example").unlink()
        (self.runtime / "example").symlink_to(self.root / "absent")
        self.assertIn("runtime missing", self.run_cli("--inspect", "example", code=1))

    def test_missing_inspection_and_dry_run_do_not_write(self):
        self.assertIn("runtime missing", self.run_cli("--inspect", "example", code=1))
        self.run_cli("--install", "example", "--dry-run")
        self.assertFalse(self.runtime.exists())
        self.assertIn("repository missing", self.run_cli("--inspect", "unknown", code=1))
        self.run_cli("--inspect", "../example", code=1)
        self.run_cli("--inspect", "example", "--copy", code=1)

    def test_existing_destination_is_preserved(self):
        self.run_cli("--install", "example", "--copy")
        note = self.runtime / "example" / "SKILL.md"
        note.write_text("User content\n")
        self.run_cli("--install", "example", code=1)
        self.assertEqual(note.read_text(), "User content\n")

    def test_fingerprint_tracks_paths_extra_files_and_executable_bits(self):
        self.run_cli("--install", "example", "--copy")
        contract = self.runtime / "example" / "references" / "contract.md"
        contract.rename(contract.with_name("renamed.md"))
        self.assertIn("differs from repository", self.run_cli("--inspect", "example"))
        contract.with_name("renamed.md").rename(contract)
        extra = self.runtime / "example" / "extra"
        extra.write_text("")
        self.assertIn("differs from repository", self.run_cli("--inspect", "example"))
        extra.unlink()
        contract.chmod(contract.stat().st_mode | 0o100)
        self.assertIn("differs from repository", self.run_cli("--inspect", "example"))

    def test_timestamps_do_not_change_fingerprint(self):
        self.run_cli("--install", "example", "--copy")
        os.utime(self.runtime / "example" / "SKILL.md", (1, 1))
        self.assertIn("matches repository", self.run_cli("--inspect", "example"))

    def test_internal_links_and_special_files_are_not_followed(self):
        self.run_cli("--install", "example", "--copy")
        extra = self.runtime / "example" / "external"
        extra.symlink_to(self.root)
        self.assertIn("runtime unsupported", self.run_cli("--inspect", "example", code=1))
        extra.unlink()
        os.mkfifo(extra)
        self.assertIn("runtime unsupported", self.run_cli("--inspect", "example", code=1))

    @unittest.skipIf(os.geteuid() == 0, "root bypasses file read permissions")
    def test_unreadable_runtime_is_reported(self):
        self.run_cli("--install", "example", "--copy")
        contract = self.runtime / "example" / "references" / "contract.md"
        previous_mode = contract.stat().st_mode
        try:
            contract.chmod(0)
            self.assertIn("runtime unreadable", self.run_cli("--inspect", "example", code=1))
            self.assertIn("runtime unreadable", self.run_cli("--list"))
        finally:
            contract.chmod(previous_mode)


if __name__ == "__main__":
    unittest.main()
