# Laporan Praktikum Tugas 6 — Visualisasi Data Supermarket

Aplikasi dashboard ini dibuat menggunakan PySide6 untuk membuat tampilan GUI-nya dan digabungkan dengan Matplotlib untuk menampilkan grafik secara dinamis. Proyek ini bertujuan untuk menyajikan data transaksi penjualan dari sebuah jaringan supermarket agar lebih gampang dibaca dan dianalisis.

## Identitas Mahasiswa
* Nama : WIWIK PUTRI
* NIM : F1D02310096
* Kelas : C


## Penjelasan Dataset
Dataset yang dipakai di tugas ini adalah Supermarket Sales Analysis. Isinya berupa rekaman data riwayat transaksi penjualan di beberapa cabang supermarket selama periode bulan Januari sampai April 2019.

Beberapa kolom penting yang diolah di dalam program ini:
* Invoice ID: Nomor nota atau kode unik tiap transaksi.
* Branch & City: Nama cabang toko dan kotanya (ada Yangon, Naypyitaw, sama Mandalay).
* Customer type: Jenis pelanggan yang beli (apakah Member atau pelanggan Normal).
* Product line: Kategori produk yang dibeli (misal: Health and beauty, Electronic accessories, dll).
* Quantity: Jumlah item atau unit barang yang dibeli konsumen.
* Sales: Total duit masuk (omset kotor) dari transaksi tersebut dalam satuan USD.


## Fitur-Fitur Aplikasi
1. **Tabel Data Transaksi**: Menampilkan semua baris data penjualan di tabel sebelah kiri menggunakan QTableWidget. Warna barisnya dibuat selang-seling (abu-abu dan hitam) agar lebih rapi.
2. **Ringkasan Performa (KPI)**: Ada teks di panel kanan bawah yang otomatis menghitung total jumlah barang terjual (Total Kuantitas) dan total omset (Total Penjualan). Angkanya akan otomatis berubah sendiri kalau filternya diganti.
3. **Filter Ganda Interaktif**:
   * **Filter Data**: Bisa memilih mau menampilkan lini produk tertentu atau "Semua Kategori".
   * **Filter Tampilan Grafik**: Bisa gonta-ganti jenis chart langsung di tempat tanpa perlu membuka window baru.
4. **Visualisasi Grafik Dinamis (Matplotlib)**:
   * **Bar Chart**: Untuk membandingkan total penjualan di tiap kota cabang.
   * **Pie Chart**: Untuk mencari tahu proporsi pembeli antara member vs pelanggan biasa.
   * **Line Chart**: Untuk melihat tren naik-turunnya omset harian. Datanya sudah diurutkan otomatis dari tanggal paling awal sampai akhir agar garisnya rapi dan tidak tumpang tindih.
   * **Donut Chart**: Untuk mencari tahu kontribusi penjualan berdasarkan gender pembeli.


## Struktur Folder Proyek
Kode program di proyek ini dipecah menjadi beberapa file (modular) agar rapi dan gampang dimodifikasi kalau ada bug:
* main.py : File utama untuk menjalankan aplikasi pertama kali.
* dashboard.py : File untuk mengatur semua tata letak layout komponen GUI, tabel, tombol filter, dan teks KPI.
* chart_widget.py : File khusus yang isinya logika untuk menggambar dan me-refresh kanvas grafiknya Matplotlib.
* data_handler.py : Backend program yang fungsinya membaca file CSV menggunakan bantuan library Pandas, membersihkan data, sekaligus menghitung total statistik filternya.
