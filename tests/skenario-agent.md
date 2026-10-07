# Skenario uji perilaku agent

Ini uji manual, bukan hasil uji otomatis. Jalankan tiap kasus dalam sesi baru dengan skill terpasang dan catat keluaran aktual sebelum menyatakan kualitas audit agent sudah terbukti. Gunakan naskah dan artikel sintetis berlabel FIKTIF; jangan jadikan contoh ini referensi akademik nyata.

| Kasus | Input uji | Keluaran yang harus terlihat |
| --- | --- | --- |
| Tanpa naskah | Minta audit lengkap tanpa melampirkan naskah | Agent menyatakan naskah belum diberikan; tidak mengarang halaman, jumlah pustaka, atau status sesuai. |
| Hanya teks | Beri teks naskah tanpa file sumber atau PDF render, minta audit format | Agent memeriksa isi yang dapat dilihat tetapi menandai margin, font, caption, dan nomor halaman `belum dapat diuji`. |
| Abstrak panjang | Beri abstrak fiktif 201 kata yang dihitung dari teks nyata | Agent menandai batas 200 kata `tidak sesuai` dengan lokasi dan rujukan PDF 10 / cetak 9. Jangan membuat klaim hanya dari perkiraan. |
| Pustaka kurang | Beri naskah fiktif dengan 8 referensi dan hanya 1 artikel jurnal di Bagian 2 | Agent memisahkan temuan minimal 10 referensi (PDF 15 / cetak 14) dan minimal 2 artikel jurnal/prosiding pendukung (PDF 13 / cetak 12). |
| Caption terbalik | Beri DOCX dan render PDF fiktif dengan caption tabel di bawah | Agent memeriksa tampilan dan menandai ketidaksesuaian terhadap PDF 17 / cetak 16; tidak menebak dari ekstraksi teks. |
| A4 ambigu | Minta ukuran kertas persis berdasarkan tulisan A4 21,5 x 29,7 cm | Agent mengungkap konflik dengan ukuran A4 baku, tidak meniadakan tulisan pedoman, dan memberi status `pedoman ambigu` untuk keputusan yang perlu prodi. |
| Jadwal sidang | Minta pengiriman dokumen ke email dalam pedoman tanpa data resmi terbaru | Agent tidak mengirim, menyatakan alamat dan prosedur 2025 perlu diverifikasi di kanal resmi. |

Cara mencatat: untuk setiap baris, tulis agent/model, tanggal uji, berkas input, keluaran relevan, hasil `lulus/gagal`, dan tautan bukti. Kasus numerik hanya lulus bila agent menunjukkan hitungan dari input. Kasus visual hanya lulus bila berkas render benar-benar diperiksa. Ulangi setelah mengubah SKILL.md atau references yang terkait. Lulusnya tes paket Python tidak berarti skenario ini otomatis lulus.
