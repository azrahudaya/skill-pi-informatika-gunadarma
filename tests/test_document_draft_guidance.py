"""Guard the manuscript-draft rules against missing placeholders and indentation."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class DocumentDraftGuidanceTest(unittest.TestCase):
    def test_skill_routes_document_drafts_to_reference(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`references/draf-dokumen.md`", skill)

    def test_reference_defines_indentation_and_honest_placeholders(self) -> None:
        guide = (ROOT / "references/draf-dokumen.md").read_text(encoding="utf-8")
        for phrase in (
            "inden baris pertama", "1,25 cm", "(.....................)",
            "kuning", "Daftar Isi", "tidak menetapkan", "tanda tangan",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, guide)


if __name__ == "__main__":
    unittest.main()
