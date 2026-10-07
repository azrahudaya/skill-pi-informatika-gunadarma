"""Regression tests for the published skill package checks."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageValidationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.package = Path(self.workspace.name) / "skill"
        self.package.mkdir()
        for source in [ROOT / "README.md", ROOT / "SKILL.md", *(ROOT / "references").glob("*.md"), *(ROOT / "examples").glob("*.md")]:
            target = self.package / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        (self.package / "scripts").mkdir()
        shutil.copy2(ROOT / "scripts/validate.py", self.package / "scripts/validate.py")

    def validate(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/validate.py"],
            cwd=self.package,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_valid_package(self) -> None:
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_rejects_missing_frontmatter_end(self) -> None:
        path = self.package / "SKILL.md"
        path.write_text(path.read_text().replace("\n---\n# Pedoman", "\n# Pedoman", 1))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("closing ---", result.stderr)

    def test_rejects_missing_new_reference(self) -> None:
        missing = self.package / "references/administrasi.md"
        missing.unlink()
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing reference", result.stderr)

    def test_rejects_missing_page(self) -> None:
        path = self.package / "references/cakupan-halaman.md"
        path.write_text(path.read_text().replace("| 36 | 35 |", "| 40 | 35 |"))
        result = self.validate()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ordered index", result.stderr)


if __name__ == "__main__":
    unittest.main()
