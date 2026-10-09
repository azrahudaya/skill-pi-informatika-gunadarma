# Pedoman visual, diagram AI, gambar, dan metodologi evaluasi PI

Gunakan panduan ini saat membuat, mengaudit, atau merevisi ilustrasi sistem, perancangan diagram, visual berbasis data, serta skema metodologi pada Penulisan Ilmiah Informatika Gunadarma.

## 1. Standar diagram yang digenerate AI dan tool visual

Saat membuat diagram menggunakan AI (Midjourney, ChatGPT Canvas, DALL-E) atau tool diagram berbasis kode (draw.io, Mermaid, Graphviz, PlantUML):

1. Larangan AI slop dan dekorasi non-akademik:
   - DILARANG menggunakan gaya 3D glossy, gradien warna warni neon, bayangan berlebihan (*drop shadow* tebal), atau karakter ilustrasi kartun generik.
   - DILARANG menghasilkan teks berbahasa asing acak/gibberish yang sering dibuat oleh model difusi gambar AI. Semua teks label diagram WAJIB menggunakan Bahasa Indonesia baku yang tajam dan terbaca jelas.
   - Jika menggunakan AI image generator, tambahkan prompt pembatas: `"clean academic technical diagram, draw.io style, flat design, white background, high-contrast monochrome/subtle grayscale, crisp legible typography, sharp vector outlines, Indonesian language labels"`.
2. Format dan resolusi ekspor:
   - Ekspor dalam format PNG resolusi tinggi (minimal 2400 piksel sisi panjang atau 300 DPI) atau format vektor SVG.
   - Canvas berlatar putih bersih (background #FFFFFF), bukan transparan, agar kontras garis dan teks tidak rusak saat dirender ke PDF atau dicetak pada kertas HVS.
3. Keterbacaan fotokopi (Grayscale Safe):
   - Diagram harus tetap terbaca 100% saat difotokopi hitam putih. Gunakan outline tegas (minimal 1.5 pt), teks sans-serif (Arial, Helvetica, atau Segoe UI) ukuran minimal 10 pt, serta arsiran atau label teks langsung untuk membedakan jalur/blok.

## 2. Katalog variasi diagram wajib dalam PI Informatika

Setiap topik penelitian Informatika memiliki kebutuhan diagram pemodelan yang spesifik. Jangan mencampuradukkan diagram alur sistem dengan diagram metodologi penelitian.

### A. Diagram Metodologi Penelitian vs Diagram Alur Kerja Sistem (Pemisahan Gambar 3.1)
- **Diagram Alur Kerja Sistem (System Workflow):**
  - Menggambarkan jalannya data dan logika komputasi dari input pengguna (misal: pesan teks/voice note WhatsApp) -> validasi durasi/ukuran -> konversi audio FFmpeg -> inferensi STT & NLU -> interaksi konfirmasi -> penyimpanan database -> penjadwalan reminder -> pengiriman notifikasi akhir.
  - Menggunakan simbol baku flowchart (Terminator oval, Proses persegi, Decision belah ketupat, I/O jajar genjang, Database silinder).
- **Diagram Metodologi Penelitian (Research Methodology Flow):**
  - Menggambarkan tahapan aktivitas peneliti dari awal hingga penarikan kesimpulan.
  - Untuk metode Prototyping: digambarkan sebagai siklus iteratif (Planning -> Modeling -> Construction -> Deployment -> Communication) yang berputar jika sistem belum memadai, lalu bermuara ke tahap evaluasi empiris (evaluasi akurasi, latensi, dan analisis hasil).
  - Untuk metode Waterfall: digambarkan sebagai tahapan linier bertingkat dari Analisis Kebutuhan hingga Pengujian dan Pemeliharaan.

### B. Pemodelan UML (Unified Modeling Language)
- **Use Case Diagram:**
  - Wajib memiliki batasan sistem (*system boundary*) berupa kotak persegi panjang yang membungkus semua use case elips.
  - Aktor di luar kotak mewakili pihak yang berinteraksi (misalnya Aktor Pengguna Mahasiswa di sisi kiri dan Aktor Administrator di sisi kanan).
  - Use case harus ringkas dan berorientasi fungsional bernilai (contoh: *Mengirim Voice Note*, *Mengonfirmasi Pengingat*, *Melihat Daftar Pengingat*, *Menandai Pengingat Selesai*, *Mengelola Pengguna*).
  - DILARANG membuat use case untuk aksi mekanis sepele (seperti *Mengetik Nama*, *Menekan Tombol Poll*, *Membuka WhatsApp*).
- **Activity Diagram:**
  - Menggambarkan langkah-langkah pemrosesan sistem secara detail.
  - Wajib menggunakan partisi jalur (*swimlane*) vertikal untuk memisahkan tanggung jawab: Jalur Pengguna (User), Jalur Antarmuka Bot (Client), dan Jalur Server / Backend API.
  - Menyertakan status awal (lingkaran solid), aktivitas proses (persegi panjang bersudut bulat), percabangan kondisi (belah ketupat keputusan), dan status akhir (lingkaran cincin solid).

### C. Storyboard dan Perancangan Antarmuka (Wireframe)
- Digunakan untuk menggambarkan skenario percakapan atau alur navigasi aplikasi dari sudut pandang layar perangkat.
- Disusun dalam format multi-panel (misal: 4 panel horizontal atau 2x2 grid) dengan judul panel dan nomor urut yang jelas.
- Setiap panel menampilkan tahapan interaksi kunci (contoh pada bot: Panel 1 Registrasi Interaktif, Panel 2 Penerimaan Voice Note dan Poll Konfirmasi, Panel 3 Pengiriman Notifikasi Otomatis, Panel 4 Perintah Teks Manajemen).
- Setiap panel diberi nomor dan caption resmi: `Gambar 3.X Storyboard Antarmuka Aplikasi`.

### D. Struktur Navigasi Aplikasi
- Wajib membedakan 4 arsitektur navigasi baku:
  1. *Linier:* alur berurutan satu arah dari halaman awal hingga selesai (cocok untuk wizard instalasi atau form pendaftaran bertahap).
  2. *Non-Linier:* navigasi bebas di mana setiap halaman/menu dapat berpindah ke halaman mana pun tanpa aturan urutan.
  3. *Hierarki:* struktur pohon bercabang dari menu utama ke sub-menu tingkat satu dan sub-menu tingkat dua.
  4. *Campuran / Komposit:* kombinasi hierarki pada menu utama dengan alur linier pada transaksi atau proses tertentu (arsitektur paling umum pada aplikasi modern).

## 3. Standar grafik hasil evaluasi kuantitatif

1. Diagram Batang (Bar Chart):
   - Wajib dimulai dari angka 0 pada sumbu Y (kuantitas) agar perbandingan visual panjang batang akurat dan tidak bias.
   - Berikan nilai angka di atas setiap batang (*data labels*) agar pembaca tidak perlu mengira-ngira angka dari garis kisi.
   - Pembedaan kategori menggunakan pola garis arsir (*hatching*), bukan warna pelangi.
2. Histogram dan Distribusi Frekuensi:
   - Digunakan untuk menampilkan sebaran data empiris (misal: distribusi Word Error Rate per voice note, distribusi durasi rekaman, atau distribusi skor SUS).
   - Cantumkan garis vertikal putus-putus untuk menandai nilai rata-rata (mean) dan median.
3. Grafik Latensi dan Komposisi Waktu (Stacked Bar / Area):
   - Membedakan porsi waktu pemrosesan per komponen (misal: waktu unduh audio, konversi FFmpeg, inferensi Whisper, inferensi GPT, dan latensi jaringan).

## 4. Struktur naskah Bab 1 sampai Bab 3

1. **Subbab 1.2: Batasan Masalah:**
   - Memakai judul `Batasan Masalah`.
   - Wajib memuat batasan kuantitatif terukur: batasan format audio/data masukan (format yang didukung, durasi maksimal per berkas, ukuran maksimal file), batasan fungsional (jumlah toleransi pengiriman notifikasi pengingat, batasan pengenalan bahasa), batasan lingkungan operasional (API yang dipakai, sistem operasi), dan batasan tingkatan hak akses pengguna.
2. **Subbab 1.4: Metode Penelitian:**
   - Menjabarkan tahapan SDLC yang dipilih secara kronologis dan prosedural, bukan hanya menyebut nama metodenya.
3. **Bab 2: Tinjauan Pustaka:**
   - Wajib mendefinisikan seluruh istilah kunci yang ada pada judul karya ilmiah (misal: definisi kecerdasan buatan, speech recognition, model transformer Whisper, natural language understanding LLM, voice note, arsitektur bot WhatsApp, dan SQLite).
   - Memuat minimal dua artikel jurnal atau prosiding ilmiah pendukung yang relevan.
4. **Bab 3: Pembahasan dan Implementasi:**
   - Kode program berupa teks tercetak asli dengan font monospasi, bukan gambar screenshot.
   - Menyajikan pengujian fungsional black-box serta pengujian akurasi kuantitatif.
