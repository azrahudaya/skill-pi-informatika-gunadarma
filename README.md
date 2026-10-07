# Skill PI Informatika Gunadarma

![Thumbnail PI Informatika Gunadarma](assets/thumbnail.png)

Skill untuk menulis dan mengaudit Penulisan Ilmiah (PI) Prodi Informatika Gunadarma berdasarkan [pedoman resmi 2025](https://drive.google.com/file/d/1PJt6gNmPIAneWNRWJ77XT3Lz-gTEb07o/view). Baca [SKILL.md](SKILL.md) untuk aturan lengkap. Bisa dipakai di Claude Code, Codex, dan Hermes Agent. Ini proyek independen, bukan publikasi resmi universitas dan bukan pengganti keputusan pembimbing atau prodi.

## Mulai di sini

Siapkan naskah PI versi terakhir. Untuk audit isi dan format yang lengkap, sertakan file sumber (misalnya DOCX atau LyX/LaTeX), PDF hasil render, dan PDF pedoman resmi. Kalau hanya ada teks, agent bisa memeriksa isi, tetapi tidak boleh memastikan margin, font, posisi caption, atau nomor halaman. Untuk sidang/pengumpulan, sertakan juga catatan revisi atau instruksi prodi terbaru bila ada. Jangan kirim identitas pribadi yang tidak diperlukan.

1. Pasang skill lewat petunjuk di bawah, lalu mulai sesi agent baru.
2. Berikan berkas yang tersedia dan pilih salah satu contoh permintaan.
3. Periksa laporan: tiap temuan harus punya lokasi di naskah, halaman pedoman, status, dan tindakan. Lihat [contoh laporan fiktif](examples/contoh-audit.md).

## Pasang skill

Salin SKILL.md bersama seluruh `references/`. Pilih satu `DEST` sesuai agent yang kamu pakai:

```sh
git clone https://github.com/azrahudaya/skill-pi-informatika-gunadarma.git
cd skill-pi-informatika-gunadarma
SKILL=pedoman-pi-informatika-gunadarma-2025
DEST="$HOME/.claude/skills/$SKILL" # Claude Code
# DEST="$HOME/.agents/skills/$SKILL" # Codex
# DEST="$HOME/.hermes/skills/productivity/$SKILL" # Hermes Agent
mkdir -p "$DEST/references"
cp SKILL.md "$DEST/"
cp -R references/. "$DEST/references/"
```

Mulai sesi baru agar agent mengenali skill. PDF pedoman tidak disertakan di repo. Berikan PDF resmi jika perlu audit kutipan dan tata letak yang presisi.

## Contoh permintaan

- Audit format: "Pakai skill pedoman-pi-informatika-gunadarma-2025 untuk audit format dan isi naskah PI ini. Ini DOCX, PDF hasil render, dan PDF pedoman 2025. Buat matriks aturan, status, bukti lokasi naskah, halaman pedoman, dan tindakan. Tandai yang belum bisa diuji."
- Kerangka PI: "Bantu buat kerangka PI Informatika untuk topik [topik] berdasarkan pedoman 2025. Pisahkan aturan wajib dari contoh, dan jangan buat hasil penelitian atau sumber pustaka fiktif."
- Sidang: "Cek kesiapan sidang PI saya berdasarkan berkas yang saya berikan. Bedakan syarat pedoman 2025 dari prosedur administrasi yang harus dicek ulang ke kanal resmi. Jangan mengirim berkas."

Hasil audit memakai status `sesuai`, `tidak sesuai`, `belum dapat diuji`, atau `pedoman ambigu`. [Alur audit](references/alur-audit.md) menjelaskan arti status dan bukti yang diperlukan. [Daftar konflik pedoman](references/ketidakselarasan.md) mencegah contoh lampiran dibaca sebagai aturan baru. Contoh keluaran bukan sertifikat kelulusan PI.

## Pemeriksaan paket

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

Pemeriksaan ini menguji kelengkapan paket dan kontrak dokumentasi, bukan menjamin agent mengaudit naskah secara benar. [Skenario uji perilaku agent](tests/skenario-agent.md) tersedia untuk pengujian manual; belum diklaim lulus otomatis. Audit nyata tetap memerlukan naskah, sumber, render visual, dan pemeriksaan manusia.

## Hak penggunaan

Azra Hudaya belum menetapkan lisensi penggunaan ulang untuk teks skill ini (`license: Proprietary`). Ketersediaan repo secara publik dan petunjuk pemasangan bukan pernyataan izin untuk memakai ulang, memodifikasi, atau mendistribusikan teks skill. Hubungi pemilik untuk meminta izin atau menanyakan ketentuannya. PDF pedoman universitas tidak disertakan dan tidak dilisensikan ulang di sini. Periksa prosedur pengumpulan terbaru di kanal resmi prodi sebelum menyerahkan data atau berkas.

Dibuat oleh [Azra Hudaya](https://github.com/azrahudaya).
