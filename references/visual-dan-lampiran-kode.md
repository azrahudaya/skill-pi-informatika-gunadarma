# Visual, tabel, diagram, dan lampiran kode PI

Gunakan panduan ini saat PI memuat tabel data, diagram alur, arsitektur sistem, rancangan antarmuka, grafik numerik, atau listing program. Pedoman 2025 mengatur posisi caption dan penomoran [PDF 17-18 / cetak 16-17] serta memperbolehkan listing program sebagai lampiran [PDF 15 / cetak 14]. Grafik dan diagram bukan wajib ada pada setiap subbagian; pedoman tidak mensyaratkannya. Pilih visual hanya bila ia membantu pembaca memeriksa angka, alur pemrosesan, atau perbandingan yang sulit dipahami melalui prosa semata. Jangan mengisi ruang halaman demi mengejar ketebalan naskah dengan visual yang berulang atau tanpa makna analitis.

## 1. Aturan penomoran, caption, dan rujukan naskah

1. Penomoran berbasis bab: nomor gambar dan tabel menggunakan format dua angka yang dipisahkan titik, yaitu `[Nomor Bagian].[Nomor Urut]`. Contoh: `Gambar 3.1` adalah gambar pertama pada Bagian 3, dan `Tabel 2.2` adalah tabel kedua pada Bagian 2 [PDF 17 / cetak 16]. Penomoran diulang dari angka 1 pada setiap bab baru.
2. Posisi dan tipografi caption:
   - Caption tabel: diletakkan di sebelah **atas tengah** tabel. Times New Roman 12 pt (boleh disesuaikan 11 pt bila tabel padat), spasi tunggal (spasi 1) mulai dari judul tabel hingga isi tabel [PDF 17 / cetak 16].
   - Caption gambar: diletakkan di sebelah **bawah tengah** gambar. Times New Roman 12 pt, spasi tunggal, posisi simetris terhadap gambar [PDF 17 / cetak 16].
   - Huruf judul caption memakai Title Case (kapital pada awal setiap kata kecuali kata tugas seperti dan, atau, pada, untuk, dengan, terhadap, dari).
3. Rujukan wajib dalam teks (in-text callout): setiap gambar dan tabel WAJIB dirujuk secara eksplisit dengan menyebutkan nomornya di dalam alinea pembahasan sebelum atau tepat di samping visual tersebut diletakkan.
   - Bentuk yang benar: "...seperti yang ditunjukkan pada Gambar 3.1..." atau "...sebagaimana dirangkum pada Tabel 3.2..." [PDF 18 / cetak 17].
   - Bentuk yang DILARANG: "...seperti pada gambar di atas...", "...dapat dilihat pada tabel di bawah...", atau visual yang diletakkan menggantung tanpa narasi pengantar.
4. Pencantuman sumber kutipan: jika gambar atau tabel diambil, diolah, atau diadaptasi dari karya pihak ketiga, cantumkan sumber sitasi di akhir teks caption atau di bawah tabel dengan format: `(Sumber: Penulis, Tahun)`. Jika merupakan karya mandiri dari eksperimen, tidak perlu menuliskan sumber atau cukup sebutkan sumber data aslinya pada teks pengantar alinea.
5. Sinkronisasi daftar awal: semua judul dan nomor yang tertera pada caption harus sinkron persis dengan entri pada Daftar Tabel dan Daftar Gambar di bagian awal naskah, termasuk nomor halaman hasil render akhir [PDF 12 / cetak 11].

## 2. Format dan anatomi tabel akademik FTI

1. Anatomi garis border: tabel akademik mengutamakan keterbacaan data. Gunakan gaya tabel formal tiga garis batas horizontal utama (garis batas atas tabel, garis pemisah di bawah baris kepala kolom, dan garis penutup paling bawah). Hindari garis batas vertikal yang tebal atau kisi-kisi kotak yang membuat mata lelah, kecuali pada tabel formulir tertentu yang memerlukan sekat tegas.
2. Judul kolom (table header): pedoman menegaskan bahwa judul-judul kolom **tidak dicetak tebal** (normal font) [PDF 17 / cetak 16]. Spasi di dalam sel adalah spasi 1. Font di dalam tabel adalah Times New Roman 10 pt atau 11 pt (dapat diperkecil hingga 9 pt pada tabel data yang padat agar muat dalam lebar margin).
3. Perataan sel (alignment):
   - Kolom teks deskriptif atau nama entitas: rata kiri (align left).
   - Kolom nomor urut, kode singkat, status, atau simbol: rata tengah (align center).
   - Kolom nilai angka, kuantitas numerik, atau persentase: rata kanan (align right) atau rata tengah berpatokan pada tanda desimal agar mudah diperbandingkan.
4. Penanganan tabel bersambung lintas halaman: jika tabel panjang terpotong pergantian halaman, judul tabel dan kepala kolom harus tetap muncul pada halaman sambungan [PDF 17 / cetak 16].
   - Di Microsoft Word: gunakan fitur `Table Properties > Row > Repeat as header row at the top of each page`.
   - Di naskah akhir: cantumkan teks penanda di atas tabel sambungan: `Lanjutan Tabel 3.2 Judul Tabel` agar pembaca tidak kehilangan konteks kolom saat membaca lembar berikutnya.

## 3. Jenis-jenis tabel umum dalam PI Informatika

1. Tabel Spesifikasi Perangkat Keras dan Perangkat Lunak (Bab 3): merinci lingkungan pengembangan dan lingkungan pengujian. Kolom: Komponen, Spesifikasi Minimum/Aktual, Keterangan Peran.
2. Tabel Kamus Data dan Skema Basis Data (Bab 3): memetakan struktur tabel database atau koleksi data. Kolom: Nama Kolom (Field), Tipe Data, Panjang/Ukuran, Keterangan / Constraint (Primary Key, Foreign Key, Not Null).
3. Tabel Matriks State of the Art / Penelitian Terdahulu (Bab 2): membandingkan rujukan ilmiah yang relevan. Kolom: Peneliti & Tahun, Objek/Dataset, Metode & Model, Metrik Evaluasi & Hasil, Celah Penelitian terhadap PI ini (lihat `references/penelitian-terdahulu.md`).
4. Tabel Skenario Pengujian / Test Case (Bab 3): mendokumentasikan rencana uji fungsi (black-box atau validasi skenario). Kolom: Nomor Kasus, Fitur/Skenario Uji, Masukan (Input), Luaran yang Diharapkan, Kondisi Batas.
5. Tabel Hasil Evaluasi dan Metrik Kinerja (Bab 3): melaporkan hasil pengukuran empiris. Kolom: Metrik (Akurasi, Presisi, Recall, F1-Score, WER, Waktu Latensi), Nilai Rata-rata, Nilai Minimum, Nilai Maksimum, Standar Deviasi.
6. Tabel Simbol Notasi Standar (Bab 2 atau Bab 3): merangkum glosarium simbol pemodelan seperti Flowchart, Use Case Diagram, atau Activity Diagram bila pembaca memerlukan panduan notasi. Kolom: Simbol Gambar, Nama Notasi, Deskripsi Fungsi.

## 4. Jenis-jenis diagram dan standar pemodelan sistem

1. Diagram Alur (Flowchart):
   - Menggambarkan logika prosedural eksekusi program atau alur metodologi penelitian.
   - Wajib mematuhi standar simbol baku ISO/ANSI: terminator (elips/kapsul) untuk awal dan akhir, proses (persegi panjang) untuk kalkulasi/tindakan internal, keputusan (belah ketupat) untuk percabangan ya/tidak, input/output (jajar genjang) untuk baca/tulis data, serta konektor lingkaran untuk sambungan alur pada halaman yang sama.
   - Setiap garis panah alur harus memiliki arah yang tegas dan tidak boleh bercabang tanpa blok keputusan.
2. Unified Modeling Language (UML):
   - Use Case Diagram: memetakan interaksi fungsional antara aktor pengguna dengan sistem. Aktor digambarkan dengan figur orang atau kotak sistem, use case digambarkan dengan elips horizontal, relasi include/extend menggunakan garis putus-putus berarah panah.
   - Activity Diagram: menggambarkan alur aktivitas sistem, status awal (lingkaran solid), status akhir (lingkaran cincin solid), aktivitas (persegi panjang berujung bulat), percabangan/decision (belah ketupat), dan swimlane vertikal jika melibatkan aktor dan server yang berbeda.
   - Class Diagram / Entity Relationship Diagram: memetakan struktur entitas data, atribut, tipe, serta relasi kardinalitas (1:1, 1:N, M:N).
3. Struktur Navigasi Sistem:
   - Digunakan pada aplikasi web, mobile, atau multimedia interaktif.
   - Terdiri atas 4 pola baku: (1) Linier (alur sekuensial satu arah dari halaman awal ke akhir); (2) Non-Linier (bebas berpindah antarmenu tanpa urutan kaku); (3) Hierarki (pola pohon bercabang dari menu utama ke submenu bertingkat); (4) Campuran / Komposit (kombinasi hierarki dan linier yang paling umum dipakai pada aplikasi modern).
4. Diagram Arsitektur dan Blok Sistem:
   - Menjelaskan hubungan fisik atau logis antarkomponen perangkat lunak dan perangkat keras (misal: mikrokontroler sensor IoT, gateway komunikasi, cloud API, database lokal, dan aplikasi mobile).
   - Setiap blok harus memiliki label nama modul yang jelas, protokol komunikasi (HTTP, MQTT, WebSocket, UART), dan arah aliran data yang terdefinisi.

## 5. Tangkapan layar antarmuka dan grafik eksperimen

1. Tangkapan Layar (Screenshots / UI Mockups):
   - Tampilkan antarmuka yang benar-benar mewakili alur kerja aplikasi (tampilan formulir utama, hasil output, atau pesan status).
   - Pastikan teks di dalam tangkapan layar beresolusi tajam dan terbaca jelas pada skala cetak dokumen.
   - Berikan garis tepi bingkai tipis (border 0.5 pt warna abu-abu netral) jika latar belakang antarmuka berwarna putih agar tidak menyatu tanpa batas dengan kertas dokumen.
   - Hindari mengambil foto layar monitor menggunakan kamera ponsel. Selalu gunakan fitur screenshot bawaan sistem operasi.
2. Grafik Kuantitatif Hasil Eksperimen:
   - Gunakan data asli dari dataset, hasil program, atau observasi yang dapat dilacak. Pertahankan satuan, urutan label, penyebut, periode, dan jumlah sampel.
   - Default visual untuk naskah: hitam putih atau abu-abu kontras tinggi berlatar putih bersih, tanpa warna bawaan matplotlib, gradien, efek 3D, bayangan, ikon AI, dan gambar ilustratif generik.
   - Pembedaan seri data harus bertahan saat dokumen difotokopi: gunakan label teks langsung pada batang/garis, pola garis putus-putus yang berbeda, arsiran tekstur (hatching), serta penanda titik geometris (lingkaran, kotak, segitiga).
   - Satu grafik satu pertanyaan. Sumbu, angka, legenda, dan label harus singkat padat jelas; jangan menambah judul di dalam gambar jika caption sudah menamai gambar.
   - Skala sumbu kuantitas (terutama diagram batang) harus dimulai dari angka nol untuk mencegah pembacaan panjang batang yang menyesatkan. Buat keluaran PNG RGB resolusi tinggi (minimal 1600 piksel sisi panjang atau 300 DPI) atau format vektor.

## 6. Lampiran listing program lengkap

1. Tentukan seluruh kode yang benar-benar dipakai untuk hasil yang dilaporkan: skrip utama, prapemrosesan, konfigurasi nonrahasia, analisis lanjutan, pembuat grafik, dan penguji yang relevan. Bukan hanya daftar nama berkas atau cuplikan beberapa fungsi. Berkas sumber elektronik tetap disertakan dengan manifest nama, versi, peran, dan hash SHA-256. Jangan sertakan lingkungan virtual, paket pihak ketiga, cache, dataset pribadi, token, kata sandi, atau kredensial.
2. Masukkan seluruh kode proyek yang relevan ke lampiran naskah dalam urutan yang logis, satu judul lampiran per berkas, dengan nomor baris bila memungkinkan dan font monospasi 8 pt, spasi tunggal sesuai ketentuan isi lampiran [PDF 16 / cetak 15]. Jika volume kode terlalu besar untuk berkas cetak, jelaskan pemisahan: lampiran naskah berisi kode yang diperlukan untuk mereproduksi hasil utama, sedangkan arsip elektronik menyimpan seluruh kode proyek; jangan mengklaim lampiran cetak berisi semuanya jika ada yang hanya di arsip.
3. Lindungi sumber dari penyalinan yang mengubah perilaku. Ekstrak teks lampiran PDF dan bandingkan baris nonkosong dengan berkas sumber asli dalam urutan yang sama; line wrapping visual boleh terjadi, tetapi token, string, parameter, dan urutan blok tidak boleh hilang. Simpan hash sumber serta hasil uji ini dalam laporan verifikasi. Rujukan di tubuh tulisan harus sesuai nama berkas dan nomor lampiran.
4. Lakukan eksekusi ulang kode terhadap input tetap, cocokkan keluaran mentah dengan tabel/grafik pada naskah dan catat lingkungan perangkat lunak. Jangan menyamakan kode yang terlihat benar dengan hasil yang sudah benar-benar dijalankan. Setiap hasil yang tidak dapat diuji ditandai, bukan direka.
5. Setelah render, audit nomor halaman `L-1`, `L-2` dan seterusnya, Daftar Lampiran, header per berkas, tabel/gambar di lampiran, pemenggalan baris kode, serta tidak ada potongan kode yang tertinggal di luar halaman. Jangan menambah halaman kosong atau mengklaim minimum 50 halaman bagian pokok terpenuhi dengan memperbanyak listing lampiran.

## 7. Bukti minimum saat menyerahkan

Laporkan untuk setiap visual: tujuan, sumber data, skrip, kesamaan angka dengan output, ukuran cetak dan lokasi halaman. Untuk lampiran: daftar berkas, hash, cakupan kode tercetak dan elektronik, hasil eksekusi ulang, kesamaan isi lampiran dengan sumber, dan status pemeriksaan PDF akhir. Jika Microsoft Word asli tidak tersedia, nyatakan bahwa DOCX belum diverifikasi dengan Word, lalu jangan menyamakan render Chrome/LibreOffice dengan hasil cetak Word.
