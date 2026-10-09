"""Check that the published package includes a usable audit contract."""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class UsageContractTest(unittest.TestCase):
    def test_readme_has_indonesian_onboarding_and_prompts(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for phrase in ("## Mulai di sini", "## Contoh permintaan", "audit format", "kerangka PI", "sidang"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, readme)

    def test_audit_contract_covers_evidence_and_unknowns(self) -> None:
        guide = (ROOT / "references/alur-audit.md").read_text(encoding="utf-8")
        for phrase in (
            "Bukti lokasi naskah", "Halaman pedoman", "belum dapat diuji",
            "pedoman ambigu", "DOCX", "PDF", "tidak sesuai",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, guide)
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`references/alur-audit.md`", skill)
        self.assertIn("`references/administrasi.md`", skill)
        self.assertIn("`references/ketidakselarasan.md`", skill)
        self.assertIn("`references/pedoman-visual-dan-evaluasi.md`", skill)

    def test_split_preserves_source_rules_and_conflicts(self) -> None:
        current = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        admin = (ROOT / "references/administrasi.md").read_text(encoding="utf-8")
        conflicts = (ROOT / "references/ketidakselarasan.md").read_text(encoding="utf-8")
        for phrase in (
            "Pembimbing membimbing penulisan hingga presentasi",
            "Setelah naskah selesai dan pembimbing memberi ACC",
            "Busana sidang pria",
            "Sesudah sidang, terima catatan perbaikan",
            "PDF 22 menyebut setelah lulus sidang",
            "Daftar `Susunan Isi File Penulisan Ilmiah yang terpisah`",
            "Presentasi maksimal 15 slide utama",
            "Tanda tangan Ketua Prodi:",
            "Tanda tangan Kasubag Sidang PI:",
            "Perpustakaan: sebelum upload",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, admin)
                self.assertNotIn(phrase, current)
        self.assertEqual(
            [int(n) for n in re.findall(r"(?m)^(\d+)\. ", conflicts)],
            list(range(1, 19)),
        )
        self.assertNotIn("1. Ukuran:", current)

    def test_examples_are_labeled_not_real_audits(self) -> None:
        example = (ROOT / "examples/contoh-audit.md").read_text(encoding="utf-8")
        self.assertIn("FIKTIF", example)
        for phrase in ("sesuai", "tidak sesuai", "belum dapat diuji", "pedoman ambigu"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, example)

    def test_reuse_status_is_explicit_without_granting_new_rights(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("belum menetapkan lisensi penggunaan ulang", readme)
        self.assertIn("tidak disertakan", readme)
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("license: Proprietary", skill)


if __name__ == "__main__":
    unittest.main()
