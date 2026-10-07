"""Require grounded visuals and complete, verifiable source appendices."""

from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class VisualCodeGuidanceTest(unittest.TestCase):
    def test_skill_routes_visual_and_code_appendix(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`references/visual-dan-lampiran-kode.md`", skill)

    def test_visual_rules_are_purposeful_and_monochrome(self) -> None:
        guide = (ROOT / "references/visual-dan-lampiran-kode.md").read_text(encoding="utf-8")
        for text in (
            "hitam putih", "bukan wajib", "matplotlib", "data asli",
            "caption gambar", "Daftar Gambar", "warna bawaan", "diagram",
            "kontras", "ukuran cetak",
        ):
            with self.subTest(text=text):
                self.assertIn(text.lower(), guide.lower())

    def test_code_appendix_is_complete_and_checked_against_source(self) -> None:
        guide = (ROOT / "references/visual-dan-lampiran-kode.md").read_text(encoding="utf-8")
        for text in (
            "seluruh kode", "berkas sumber", "baris nonkosong", "hash",
            "eksekusi ulang", "kredensial", "lampiran", "nomor halaman",
        ):
            with self.subTest(text=text):
                self.assertIn(text.lower(), guide.lower())


if __name__ == "__main__":
    unittest.main()
