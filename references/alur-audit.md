# Alur audit PI

Pakai alur ini bila pengguna meminta audit naskah. Laporan contoh ada di `examples/contoh-audit.md` pada repo; berkas contoh tidak diperlukan saat skill dipasang.

## Input dan batas audit

1. Minta naskah versi terakhir dan, untuk audit tepat sampai tata letak, PDF hasil render serta PDF pedoman resmi 2025 Prodi Informatika. DOCX atau sumber LyX/LaTeX membantu memeriksa properti asli. Catatan pembimbing, catatan revisi, dan berkas administratif diminta hanya bila tugasnya mencakup itu. Jangan minta data pribadi yang tidak relevan.
2. Pastikan jenis naskah PI Informatika dan edisi pedoman cocok. Bila pedoman tidak tersedia, gunakan rujukan halaman dalam skill secara tentatif dan tandai aturan yang perlu dicocokkan ke sumber primer. Bila hanya ada teks, jangan mengklaim font, margin, posisi caption, nomor halaman, atau tampilan visual sudah sesuai.
3. Nyatakan cakupan di awal: isi, format, sitasi, sidang, atau pengumpulan; sebut berkas yang diperiksa dan yang tidak tersedia.

## Pemeriksaan

1. Cocokkan struktur awal, empat bagian isi, dan bagian akhir. Periksa isi terhadap tujuan serta metode yang bisa diulangi, bukan hanya kehadiran judul. Hitung abstrak, sumber pustaka yang benar-benar dipakai, dan artikel jurnal/prosiding pendukung. Periksa pasangan sitasi dan pustaka dua arah serta keberadaan sumber asli. Sumber yang belum terverifikasi jangan disebut sudah valid.
2. Untuk DOCX, cek properti halaman, gaya, font, paragraf, dan tabel pada sumber. Untuk PDF final, cek tampilan halaman awal, transisi penomoran, caption, tabel lintas halaman, daftar isi, daftar gambar/tabel, dan halaman akhir. Bandingkan teks dengan render; pencarian teks saja tidak cukup untuk audit format.
3. Sebelum menilai contoh lampiran sebagai aturan, baca `references/konflik-visual-lampiran.md` dan `references/ketidakselarasan.md`. Untuk pertentangan pedoman, tampilkan kedua halaman dan minta konfirmasi pembimbing/prodi jika memengaruhi penerimaan.
4. Administrasi sidang dan pengumpulan diperiksa hanya jika diminta. Cek instruksi resmi terkini sebelum menyebut alamat email, pejabat, atau alur pengiriman sebagai prosedur yang masih berlaku. Jangan mengirim atau mengunggah tanpa izin.

## Format laporan

Awali dengan cakupan dan batas pemeriksaan. Untuk setiap butir yang relevan, isi matriks:

| Aturan | Status | Bukti lokasi naskah | Halaman pedoman | Tindakan |
| --- | --- | --- | --- | --- |

Status hanya `sesuai`, `tidak sesuai`, `belum dapat diuji`, atau `pedoman ambigu`. Status `belum dapat diuji` dipakai saat berkas, render, atau sumber tidak ada, bukan ditebak sebagai kesalahan. Status `pedoman ambigu` dipakai saat sumber resmi sendiri kurang jelas atau bertentangan, dengan kedua rujukan halaman bila ada. Lokasi bukti harus cukup spesifik: nama berkas, halaman, paragraf, tabel, atau gaya. Jika belum ada berkas naskah, tulis `naskah belum diberikan`, jangan buat nomor halaman. Bedakan temuan pasti dan catatan yang membutuhkan pemeriksaan manusia.

Akhiri dengan urutan perbaikan yang bisa dikerjakan: isi dan sumber, struktur/sitasi, tata letak, lalu administrasi. Jangan menyatakan naskah lulus atau siap dikumpulkan bila masih ada butir kritis `tidak sesuai` atau `belum dapat diuji`. Verifikasi ulang hasil pada sumber dan PDF final sesudah perubahan.
