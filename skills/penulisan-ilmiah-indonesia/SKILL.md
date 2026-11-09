---
name: penulisan-ilmiah-indonesia
description: Tulis karya ilmiah dan proposal Indonesia berbasis bukti.
version: 0.1.0
author: Fahri Zanuar Pradian (Fahrizp24), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Bahasa Indonesia, akademik, proposal, sitasi, humanizer]
    related_skills: []
---

# Penulisan ilmiah Indonesia

Skill untuk menyusun, mengaudit, dan mengedit karya ilmiah serta proposal berbahasa Indonesia. Fokusnya ke argumen yang dapat diperiksa, bahasa akademik yang wajar, dan penghapusan pola AI-slop. Skill ini tidak menjanjikan tulisan lolos AI detector dan tidak menggantikan kontribusi, verifikasi, atau keputusan penulis.

## Kapan digunakan

- Menulis atau merevisi makalah, artikel, skripsi, laporan riset, PKM, proposal lomba, atau proposal hibah.
- Mengubah catatan teknis menjadi narasi akademik berbahasa Indonesia.
- Mengurangi kalimat generik, promosi, repetisi, dan struktur yang terasa dibuat mesin.
- Memeriksa klaim, sitasi, angka, istilah, batasan, dan konsistensi proposal.

Jangan gunakan untuk memalsukan data, membuat referensi tanpa sumber, menyamarkan plagiarisme, atau menjamin hasil deteksi tertentu.

## Prinsip inti

1. Baca pedoman, template, konsep proyek, dan sumber yang tersedia sebelum menulis.
2. Bedakan fakta proyek, target, asumsi, dan hasil yang sudah terbukti.
3. Jangan mengarang angka, responden, mitra, validasi, kutipan, DOI, atau capaian.
4. Gunakan istilah Indonesia yang tepat; pertahankan istilah teknis Inggris bila padanan mengaburkan makna.
5. Tulis kalimat aktif dan konkret. Hindari slogan, hiperbola, dan kesimpulan kosong.
6. Variasikan panjang kalimat secara alami, tetapi jangan menambah kesalahan tata bahasa demi terlihat manusiawi.
7. Pertahankan suara penulis. Jika tidak ada contoh tulisan, gunakan nada formal, lugas, dan tidak promosi.
8. Sitasi harus mendukung klaim yang benar-benar diambil dari sumber. Klaim yang belum diverifikasi ditandai secara internal, bukan disamarkan.

## Alur kerja

### 1. Tetapkan batas tugas

Catat jenis dokumen, pembaca, tujuan, format, batas halaman/kata, gaya sitasi, dan tenggat. Jika informasi wajib hilang, gunakan `[DATA BELUM DIISI]`; jangan menebak.

### 2. Bangun ledger bukti

Untuk setiap klaim penting, catat:

`klaim → sumber primer → lokasi halaman/bagian/URL → kutipan atau data pendukung → batasan`

Prioritaskan pedoman resmi, paper asli, dokumentasi resmi, dataset primer, dan hasil pengujian proyek. Hasil pencarian hanya petunjuk sampai halaman sumber dibaca.

### 3. Susun argumen

Urutan umum karya ilmiah:

`masalah → bukti → celah → tujuan → metode → hasil/target → batasan → implikasi`

Urutan umum proposal:

`pengguna/penerima manfaat → masalah terukur → solusi → bukti kelayakan → pembeda → target → metode pelaksanaan → risiko → adopsi`

Sesuaikan urutan dengan pedoman resmi. Pedoman dan jawaban panitia mengalahkan pola umum.

### 4. Tulis draf pertama

Mulai dari isi, bukan pembukaan retoris. Setiap paragraf harus menjawab satu fungsi. Gunakan angka hanya jika sumbernya jelas. Nyatakan target sebagai target dan hasil sebagai hasil; jangan menukar keduanya.

### 5. Audit anti-AI-slop

Hapus atau tulis ulang:

- pembukaan seperti `di era digital`, `seiring perkembangan zaman`, dan `pada era modern`;
- kata promosi seperti `revolusioner`, `holistik`, `inovatif` tanpa bukti, `solusi komprehensif`, dan `berkelanjutan` tanpa definisi;
- rangkaian tiga manfaat yang dibuat-buat;
- kalimat `tidak hanya ..., tetapi juga ...` jika hubungan logisnya tidak perlu;
- klaim kabur seperti `para ahli menyatakan` tanpa nama dan sumber;
- frasa `hal ini menunjukkan pentingnya` tanpa penjelasan mekanisme;
- pengulangan sinonim untuk istilah yang sama;
- paragraf penutup yang hanya menyatakan masa depan cerah;
- tanda baca khas AI (lihat bagian berikut);
- subjudul dan butir daftar yang terlalu seragam;
- rincian teknis yang tidak membantu keputusan pembaca.

Ganti dengan subjek yang jelas, tindakan, angka yang bersumber, batasan, dan konsekuensi nyata. Jangan memasukkan typo, fakta pribadi palsu, atau pengalaman fiktif untuk menurunkan sinyal AI.

### 6. Audit akademik

Periksa:

- setiap tujuan memiliki metode atau indikator;
- setiap hasil memiliki metode pengukuran;
- setiap klaim eksternal memiliki sitasi;
- semua sitasi tercantum di daftar pustaka dan sebaliknya;
- istilah, singkatan, angka, satuan, dan nama produk konsisten;
- novelty dibedakan dari fitur umum;
- keterbatasan disebutkan;
- privasi, keamanan, etika, dan risiko tidak diklaim lebih luas dari arsitektur;
- proposal tidak menyebut fitur yang belum diputuskan atau belum ada buktinya.

### 7. Verifikasi akhir

Baca draf dari awal tanpa konteks proses. Tandai kalimat yang tidak dapat dijawab dengan `siapa, melakukan apa, berdasarkan apa, diukur bagaimana, dan dengan batasan apa`. Periksa dokumen final terhadap pedoman, panjang, format, sitasi, dan placeholder. Simpan daftar perubahan substantif.

## Tanda baca khas AI

Batas ini panduan, bukan angka mutlak. Periksa per paragraf, lalu per dokumen.

- Kurung berlebihan: maksimal satu kurung penjelas per paragraf. Kurung untuk singkatan (`Kecerdasan Buatan (AI)`) dan sitasi sesuai gaya yang diminta boleh. Kurung berisi anak kalimat, contoh, atau keraguan dijadikan kalimat biasa atau dibuang. Hindari kurung ganda dan pola `istilah (terjemahan) (singkatan)`.
- Tanda hubung `-` dan tanda pisah `—`/`–` berlebihan: jangan memakai tanda pisah sebagai pengganti koma, titik dua, atau kata hubung. Satu per beberapa paragraf sudah banyak. Tanda hubung tetap dipakai pada kata ulang (`peneliti-peneliti` hanya jika perlu; utamakan `para peneliti`), rentang angka, dan istilah baku.
- Jangan membuat frasa majemuk dengan tanda hubung secara seragam, misalnya `berbasis-data`, `real-time`, `end-to-end`, kecuali istilah itu memang baku di bidangnya.
- Titik dua dan titik koma: jangan membuka hampir setiap kalimat dengan `X: Y`. Satu titik dua per paragraf cukup.
- Tanda kutip: pakai tanda kutip lurus `"..."`, konsisten dengan dokumen. Hindari tanda kutip lengkung campuran dan kutip untuk memberi penekanan pada istilah biasa.
- Garis miring `/`: jangan menumpuk alternatif (`dosen/mahasiswa/peneliti`). Pilih yang sesuai atau pakai `atau`.
- Huruf tebal, miring, dan butir daftar: jangan memberi tebal pada frasa di setiap kalimat atau membuat daftar berjudul tebal ber-titik dua. Karya ilmiah ditulis sebagai paragraf, kecuali pedoman meminta daftar.
- Elipsis `...`, tanda seru, tanda tanya retoris, dan emoji tidak dipakai dalam karya ilmiah.

Cek cepat: hitung `(`, ` - `, `—`, `:` dan `;` per paragraf. Jika satu jenis muncul di hampir setiap paragraf, tulis ulang sebagian menjadi kalimat biasa. Jangan menghapus tanda baca yang diwajibkan tata bahasa, sitasi, atau pedoman.

## Gaya Bahasa Indonesia

- Pilih `karena`, `sehingga`, dan `namun` sesuai hubungan logis; jangan menumpuk konjungsi.
- Gunakan `adalah` atau `merupakan` bila sudah cukup; hindari konstruksi yang dibuat rumit.
- Gunakan istilah baku, tetapi jangan memaksakan padanan yang tidak dipakai bidangnya.
- Hindari kalimat panjang dengan lebih dari satu gagasan utama.
- Jangan memakai kata `tentunya`, `secara signifikan`, atau `sangat` tanpa dasar.
- Hindari klaim absolut seperti `100% akurat`, `tanpa risiko`, `pasti`, dan `terbaik`.
- Pertahankan tingkat formalitas sesuai dokumen dan contoh tulisan pengguna.

## Format keluaran

Saat mengerjakan teks, keluarkan secara ringkas:

1. draf atau hasil revisi;
2. klaim yang membutuhkan sumber atau keputusan pengguna;
3. masalah bahasa/struktur yang diperbaiki;
4. batasan verifikasi yang masih tersisa.

Untuk dokumen final, sertakan daftar pustaka sesuai gaya yang diminta. Jangan mengklaim sumber telah diverifikasi jika belum membaca sumber primernya.

## Verifikasi

Dokumen dianggap siap ditinjau ketika:

- pedoman dan format sudah dicocokkan;
- tidak ada data atau sitasi rekaan;
- klaim utama memiliki jejak bukti;
- target dan hasil tidak tertukar;
- istilah dan nomor sitasi konsisten;
- audit anti-AI-slop selesai tanpa mengubah fakta;
- semua placeholder yang tersisa terlihat jelas.
