"""Check the task-specific comparison guardrails are shipped."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class StateOfArtGuidanceTest(unittest.TestCase):
    def test_skill_routes_comparison_tasks(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`references/penelitian-terdahulu.md`", skill)

    def test_guidance_requires_source_checked_table_and_gap(self) -> None:
        text = (ROOT / "references/penelitian-terdahulu.md").read_text(encoding="utf-8")
        for phrase in (
            "Tabel 2.1", "metode", "hasil", "perbedaan", "teks lengkap",
            "metadata", "gap", "contoh", "PDF 21", "belum terverifikasi",
            "daftar pustaka", "caption", "halaman",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase.lower(), text.lower())


if __name__ == "__main__":
    unittest.main()
