# Revisi sidang, SDLC, evaluasi empiris, dan pengujian PI

Gunakan panduan ini saat mempersiapkan naskah siap sidang, mengaudit kesiapan presentasi, atau menindaklanjuti lembar catatan perbaikan dari dosen penguji pascasidang. Bagian ini merangkum pola temuan revisi yang berulang kali diuji oleh penguji Prodi Informatika Gunadarma, standar pemodelan SDLC, serta prosedur evaluasi teknis dan UAT.

## 1. Pola catatan kritis penguji sidang PI Informatika

Berdasarkan arsip evaluasi sidang nyata Prodi Informatika Gunadarma, berikut sepuluh poin kritis yang paling sering diperiksa oleh dosen penguji:

1. Ruang Lingkup vs Batasan Masalah (Bab 1):
   - Walaupun pedoman tertulis di PDF 13 memakai istilah `Ruang Lingkup`, sebagian besar dosen penguji meminta judul subbab 1.2 diubah menjadi `Batasan Masalah` mengikuti konvensi penulisan teknis Informatika.
   - Isi batasan masalah harus mencakup batasan kuantitatif yang tegas: batasan format dan ukuran input (misal: durasi maksimal audio, format berkas yang didukung), batasan kemampuan sistem (misal: maksimal pengiriman notifikasi, toleransi waktu), batasan lingkungan perangkat lunak, serta batasan peran pengguna.
2. Nama orang tua di Kata Pengantar:
   - Pedoman mewajibkan nama orang tua (ayah dan ibu) ditulis secara lengkap pada urutan keluarga di Kata Pengantar [PDF 11 / cetak 10]. Penguji kerap menolak naskah jika hanya menyebut `kedua orang tua` tanpa nama jelas.
3. Listing program Bab 3 dilarang screenshot:
   - Potongan kode program di Bab 3 wajib berupa teks tercetak (copy-paste kode asli dengan font monospasi), DILARANG berupa gambar screenshot layar monitor. Screenshot hanya untuk tampilan visual antarmuka pengguna (UI).
4. Penamaan tabel dan gambar (size 12 dan warna hitam):
   - Teks caption tabel dan gambar harus Times New Roman 12 pt, warna font hitam pekat (bukan abu-abu atau biru bawaan perangkat lunak pengolah kata).
5. Pemiringan istilah asing (Italic):
   - Seluruh kata berbahasa Inggris atau istilah teknis asing yang belum diserap ke KBBI wajib dicetak miring (*italic*) secara konsisten (contoh: *speech-to-text*, *voice note*, *framework*, *open-source*, *dataset*). Nama diri, nama lembaga, dan merek dagang tidak dimiringkan.
6. Pemodelan UML dan kejelasan aktor:
   - Use Case Diagram harus memiliki batasan sistem yang jelas dan aktor yang teridentifikasi secara eksplisit (misalnya: Pengguna Mahasiswa dan Administrator). Hindari use case yang terlalu atomik atau operasional kecil (seperti `Menekan Tombol` atau `Membuka Menu`).
   - Activity Diagram harus mencerminkan alur nyata pemrosesan, termasuk swimlane yang memisahkan aktivitas sisi pengguna (client) dan sisi server/sistem bila melibatkan arsitektur jaringan.
7. Tanda tangan digital pada naskah elektronik:
   - Lembar Pernyataan Orisinalitas dan lembar Kata Pengantar yang dikumpulkan dalam berkas PDF siap sidang wajib dilengkapi tanda tangan digital penulis.
8. Penjelasan tahapan metode penelitian:
   - Pada subbab 1.4 (Metode Penelitian), nama metode pengembangan perangkat lunak (SDLC) yang dipilih harus dijabarkan tahapan-tahapannya secara runtut, bukan sekadar menyebutkan nama metodenya.
9. Definisi istilah teknologi pada judul (Bab 2):
   - Semua kata kunci utama yang tercantum pada judul PI wajib memiliki subbab teori dasar atau definisi konseptual di Bab 2 (misalnya jika judul menyebut *voice note*, maka Bab 2 wajib memiliki subbab definisi *voice note* dan karakteristik audionya).
10. Batasan tingkatan hak akses (Role Play):
    - Pada pembahasan antarmuka dan perancangan sistem, jelaskan tingkatan hak akses (role pengguna vs admin) serta mekanisme keamanan data antarperan.

## 2. Metodologi pengembangan perangkat lunak (SDLC)

Penelitian pembuatan aplikasi atau sistem di Informatika Gunadarma wajib memiliki keselarasan antara tahapan yang dijanjikan pada Bab 1.4 dengan penjabaran implementasinya pada Bab 3:

1. Metode Prototyping (Pressman):
   - Cocok untuk sistem interaktif, bot, atau aplikasi baru yang memerlukan evaluasi berkala dari pengguna.
   - Lima tahapan baku:
     1. Planning: analisis kebutuhan pengguna, perumusan batasan masalah, dan perancangan awal spesifikasi.
     2. Modeling (Quick Design): pembuatan flowchart sistem, diagram UML (Use Case, Activity), struktur navigasi, dan storyboard antarmuka.
     3. Construction: penulisan kode program (coding), integrasi modul backend/API, dan pembuatan prototipe fungsional.
     4. Deployment: pengujian sistem, penerapan pada lingkungan operasional, dan penyampaian prototipe kepada responden/pengguna.
     5. Communication: pengumpulan umpan balik (feedback) pengguna melalui kuesioner atau observasi untuk evaluasi perbaikan.
2. Metode Waterfall:
   - Cocok untuk proyek dengan spesifikasi kebutuhan yang sudah matang dan pasti sejak awal.
   - Tahapan baku: Analisis Kebutuhan -> Perancangan Sistem -> Implementasi (Pengkodean) -> Pengujian -> Penerapan dan Pemeliharaan.
3. Struktur penulisan di naskah:
   - Bab 1.4 memaparkan rencana tahapan secara ringkas dalam narasi metodologis.
   - Bab 3 memaparkan hasil nyata pelaksanaan setiap tahapan tersebut disertai bukti diagram, skema database, antarmuka, dan konfigurasi lingkungan.

## 3. Metodologi pengujian dan evaluasi empiris

Setiap karya PI di Informatika Gunadarma wajib menyajikan bukti pengujian yang dapat dipertanggungjawabkan:

1. Pengujian Fungsional (Black-Box Testing):
   - Menguji apakah setiap fitur masukan menghasilkan keluaran yang diharapkan tanpa memeriksa alur internal kode.
   - Sajikan dalam tabel matriks: Nomor Uji, Fitur yang Diuji, Skenario Masukan, Hasil yang Diharapkan, dan Status Hasil (Berhasil / Gagal).
2. Pengujian Akurasi dan Kinerja Teknis:
   - Komponen Speech Recognition: Word Error Rate (WER) dihitung dengan rumus:
     `WER = (S + D + I) / N`
     di mana S = jumlah kata substitusi (salah kata), D = jumlah kata penghapusan (kata hilang), I = jumlah kata penyisipan (kata tambahan), dan N = total jumlah kata pada ground truth acuan.
   - Komponen Ekstraksi / Klasifikasi Machine Learning:
     - Precision: `TP / (TP + FP)`
     - Recall: `TP / (TP + FN)`
     - F1-Score: `2 * (Precision * Recall) / (Precision + Recall)`
   - Pengukuran Latensi: catat waktu pemrosesan dalam milidetik (ms) atau detik (s), laporkan nilai rata-rata, nilai tercepat (minimum), dan nilai terlama (maksimum) beserta analisis penyebab latensi.
3. Pengujian Penerimaan Pengguna (User Acceptance Testing / UAT):
   - Gunakan instrumen baku System Usability Scale (SUS) yang terdiri atas 10 pernyataan (skala Likert 1 sampai 5):
     1. Saya berpikir akan sering menggunakan sistem ini.
     2. Saya merasa sistem ini rumit untuk digunakan.
     3. Saya merasa sistem ini mudah digunakan.
     4. Saya pikir saya membutuhkan bantuan ahli untuk menggunakan sistem ini.
     5. Saya menemukan berbagai fitur dalam sistem ini terintegrasi dengan baik.
     6. Saya merasa ada terlalu banyak inkonsistensi dalam sistem ini.
     7. Saya membayangkan kebanyakan orang akan belajar menggunakan sistem ini dengan cepat.
     8. Saya merasa sistem ini sangat janggal atau membingungkan untuk digunakan.
     9. Saya merasa sangat percaya diri menggunakan sistem ini.
     10. Saya perlu mempelajari banyak hal sebelum saya dapat menggunakan sistem ini.
   - Aturan konversi skor SUS:
     - Untuk pernyataan bernomor ganjil (positif): skor kontribusi = `jawaban responden - 1`.
     - Untuk pernyataan bernomor genap (negatif): skor kontribusi = `5 - jawaban responden`.
     - Jumlahkan seluruh skor kontribusi dari 10 pernyataan (skala 0-40), lalu kalikan hasilnya dengan `2,5` untuk memperoleh skor akhir berskala 0 sampai 100.
   - Standar interpretasi skor SUS:
     - Rata-rata standar industri adalah 68. Skor di atas 68 menunjukkan tingkat usability di atas rata-rata (Grade B / Acceptable).

## 4. Pembagian lampiran baku PI Informatika

Bagian akhir naskah diberi nomor halaman `L-1`, `L-2`, dan seterusnya [PDF 17 / cetak 16]. Urutan lampiran yang umum digunakan:
- Lampiran 1: Grafik Hasil Ujicoba Aplikasi / Analisis Kuantitatif Lengkap.
- Lampiran 2: Source Code / Listing Program Lengkap (font monospasi 8 pt, spasi 1).
- Lampiran 3: Output Program / Dokumentasi Antarmuka Pengguna Lengkap.
- Lampiran 4: Tautan Repository GitHub / Informasi Berkas Sumber Elektronik.

## 5. Prosedur revisi pascasidang dan pengesahan final

1. Tenggat waktu perbaikan: maksimal 14 hari kalender (2 minggu) sejak tanggal pelaksanaan sidang [PDF 21 / cetak 20].
2. Konsultasi revisi: hubungi dosen sekretaris sidang atau dosen penguji revisi sesuai nomor kontak yang tercantum pada lembar catatan perbaikan.
3. Validasi revisi: dosen penguji revisi wajib menandatangani lembar persetujuan perbaikan sebelum naskah dicetak untuk hardcover final. DILARANG mencetak hardcover sebelum revisi divalidasi.
4. Spesifikasi hardcover final:
   - Warna cover: Hitam (standar FTI Gunadarma).
   - Tulisan emas: Universitas, judul, nama/NPM, prodi, dan tahun pada halaman depan.
   - Punggung buku: Judul PI, NPM, Nama Mahasiswa, Tahun Penulisan [PDF 22 / cetak 21].
5. Berkas ke Prodi (D421): map bening berisi cover, pengesahan asli bertandatangan pembimbing, dan kata pengantar [PDF 23 / cetak 22].
6. Unggah perpustakaan: pastikan lembar pengesahan sudah memiliki 3 tanda tangan lengkap (Pembimbing, Kasubbag Sidang PI, Ketua Prodi) dan stempel resmi fakultas sebelum diunggah ke Deposit System Perpustakaan Gunadarma [PDF 24 / cetak 23].
