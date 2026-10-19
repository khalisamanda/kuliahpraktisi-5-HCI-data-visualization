# Implementasi Dashboard Interaktif untuk Analisis Perilaku Pengunjung dan Pembelian pada Website Retail

## Ringkasan

Proyek ini menganalisis perilaku pengunjung website retail berdasarkan data sesi belanja online. Hasil analisis disajikan melalui visualisasi dan dashboard interaktif untuk membantu pengguna memahami pola kunjungan serta hubungan antara aktivitas pengunjung dan terjadinya pembelian.

## Dataset

- **Nama:** Online Shoppers Purchasing Intention Dataset
- **Sumber resmi:** UCI Machine Learning Repository
- **Halaman dataset:** https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset
- **Jumlah observasi:** 12.330 sesi website.
- **Target:** `Revenue`, yang menunjukkan apakah sesi berakhir dengan pembelian.

Notebook mengolah data sesi pengunjung dan menyiapkan ringkasan yang dapat digunakan oleh dashboard Streamlit.

## Tujuan

1. Memeriksa struktur dan kualitas dataset.
2. Menganalisis distribusi sesi yang menghasilkan pembelian.
3. Menghitung conversion rate.
4. Membandingkan perilaku sesi yang menghasilkan pembelian dan yang tidak.
5. Menyajikan ringkasan melalui grafik dan dashboard interaktif.
6. Memudahkan pengguna mengeksplorasi informasi melalui filter dan visualisasi.

## Metode dan komponen

- Pemeriksaan data dan statistik deskriptif.
- Analisis distribusi target `Revenue`.
- Perhitungan conversion rate.
- Pengelompokan data berdasarkan kategori perilaku pengunjung.
- Visualisasi menggunakan Plotly.
- Dashboard interaktif menggunakan Streamlit.
- Penyajian ringkasan dan indikator utama (*key performance indicators*).

## Batasan dan penggunaan yang bertanggung jawab

- Dataset merepresentasikan sesi website, bukan riwayat lengkap setiap pelanggan.
- Hubungan antara perilaku pengunjung dan pembelian tidak membuktikan hubungan sebab-akibat.
- Conversion rate dari dataset tidak otomatis mewakili website lain.
- Dashboard merupakan demonstrasi visualisasi data; evaluasi HCI yang menyeluruh memerlukan pengujian langsung dengan pengguna.
- Kesimpulan harus disesuaikan dengan hasil analisis yang benar-benar diperoleh.
