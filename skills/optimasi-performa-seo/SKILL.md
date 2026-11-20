---
name: optimasi-performa-seo
description: Optimasi teknis performa web, Core Web Vitals, dan SEO modern (PageSpeed 90+, eliminasi CLS, WebP, Nginx caching, dan Agentic Browsing Discovery).
version: 0.1.0
author: Fahri Zanuar Pradian (Fahrizp24), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [SEO, Core Web Vitals, PageSpeed Insights, WebP, Nginx, Caching, CLS, LCP, Agentic Browsing, llms.txt, WebMCP]
    related_skills: [penulisan-ilmiah-indonesia]
---

# Optimasi Performa & SEO Modern

Skill untuk menganalisis, mendiagnosis, dan mengeksekusi perbaikan teknis performa web, Core Web Vitals (LCP, CLS, INP), SEO on-page/teknis, serta kepatuhan standar web modern (*Agentic Browsing* dan AI crawler). Skill ini berfokus pada rekayasa teknis nyata berbasis bukti metrik (Lighthouse, PageSpeed Insights, Chrome DevTools), bukan sekadar manipulasi kata kunci.

## Kapan Digunakan

- Mendiagnosis skor PageSpeed Insights / Lighthouse yang rendah (misal: zona merah/oranye < 70) dan meningkatkannya ke zona hijau (90–100).
- Mengeliminasi pergeseran tata letak visual (*Cumulative Layout Shift / CLS*).
- Mengurangi beban transfer data media melalui konversi massal format modern (WebP/AVIF).
- Mengonfigurasi web server (Nginx/Apache) untuk kompresi payload (Gzip/Brotli) dan *immutable browser caching* jangka panjang (1 tahun).
- Mengatasi pemblokiran render font (*Flash of Invisible Text / FOIT*) dengan strategi `font-display: swap`.
- Memperbaiki pengenalan favicon resmi pada cuplikan hasil pencarian Google (*Google Search snippet*).
- Menyiapkan standar *Agentic Browsing* (Lighthouse v13.3+): integrasi `llms.txt`, *Web App Manifest*, *Agentic Resource Discovery* (`ard.json`), dan protokol WebMCP.
- Menerapkan *Structured Data* (JSON-LD Schema.org) yang valid untuk media organisasi, artikel, dan breadcrumb.

Jangan gunakan skill ini untuk teknik *black-hat SEO*, *cloaking*, spam link, atau pengisian kata kunci manipulatif (*keyword stuffing*).

## Prinsip Inti

1. **Ukur Dulu URL Kanonikal:** Selalu jalankan audit kecepatan pada URL final kanonikal (misal: `https://www.your-domain.com/`), bukan URL pengalihan (non-www atau HTTP) yang menambahkan penalti latensi request 301.
2. **Kompilasi Aset di Sisi Server:** Jangan mengandalkan browser klien untuk merampingkan gambar besar. Lakukan konversi WebP/AVIF di server atau build pipeline.
3. **Statik Harus Memiliki Cache Lifetime Panjang:** Berikan header `Cache-Control: public, max-age=31536000, immutable` pada seluruh bundel aset yang memiliki hashing unik (`/_astro/`, CSS, JS, WOFF2).
4. **Dimensi Gambar Harus Pasti:** Setiap elemen `<img>` wajib memiliki atribut `width`, `height`, dan `aspect-ratio` untuk mencegah browser menghitung ulang geometri (*reflow/CLS*).
5. **Teks Jangan Tertahan Font:** Terapkan `display: swap` pada web font agar teks dapat langsung dibaca seketika menggunakan font fallback sistem.
6. **AI Agent Ramah Mesin:** Sediakan metadata terstruktur yang dapat dikonsumsi mesin secara aman melalui `/llms.txt`, `/manifest.json`, dan integrasi WebMCP (`document.modelContext`).

---

## Alur Kerja Diagnostik & Eksekusi

### 1. Audit & Pengumpulan Data Awal

Jalankan audit PageSpeed Insights / Lighthouse dan kelompokkan temuan ke dalam 5 pilar utama:
- **Latensi Dokumen:** Apakah ada rantai redirect 301 (HTTP &rarr; HTTPS atau non-www &rarr; www)?
- **Ukuran Transfer Media:** Berapa ratus KiB/MiB gambar JPEG/PNG yang belum dioptimalkan?
- **Kebijakan Cache:** Apakah aset statis disajikan tanpa header masa pakai (*cache lifetime*)?
- **Stabilitas Visual (CLS):** Komponen mana yang menyebabkan pergeseran elemen saat render?
- **Agentic Browsing Ratio:** Apakah file discovery mesin (`llms.txt`, manifest, WebMCP) sudah terpasang?

---

### 2. Rekayasa Media (Konversi Massal WebP)

Lakukan konversi seluruh gambar di direktori media/unggahan ke WebP kualitas optimal:

```bash
python scripts/convert_webp.py --input ./uploads --quality 82
```

**Aturan Penanganan Database:**
- Jika CMS menggunakan database (SQLite/MySQL/PostgreSQL), perbarui referensi URL di tabel konten (`posts`, `pages`, `media`) dari `.jpg`/`.png` ke `.webp`.
- Selalu buat cadangan database (*backup/snapshot*) sebelum menjalankan skrip pembaruan massal.
- Pastikan logo antarmuka (header, logo horizontal) dikompresi maksimal tanpa degradasi visual.

---

### 3. Konfigurasi Web Server & Caching (Nginx)

Terapkan konfigurasi caching dan kompresi pada blok server Nginx:

```nginx
# Gzip Compression
gzip on;
gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_min_length 256;
gzip_types
    text/plain
    text/css
    text/xml
    text/javascript
    application/json
    application/javascript
    application/xml
    image/svg+xml;

# 1-Year Immutable Caching untuk Aset Build & Font
location /_astro/ {
    proxy_pass http://127.0.0.1:PORT;
    expires 1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
    access_log off;
}

# 1-Year Caching untuk Media WebP & Static Files
location ~* \.(?:ico|css|js|gif|jpe?g|png|webp|svg|woff2?|eot|ttf)$ {
    proxy_pass http://127.0.0.1:PORT;
    expires 1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
    access_log off;
}
```

Uji konfigurasi dengan `nginx -t` lalu reload server secara berkala.

---

### 4. Eliminasi CLS & Optimasi Font Rendering

#### A. Mencegah Layout Shift (CLS < 0.05)
Tambahkan atribut lebar, tinggi, dan aspek rasio pada seluruh komponen kartu berita/banner:
```html
<img 
  src="/uploads/berita.webp" 
  alt="Judul Berita" 
  width="560" 
  height="380" 
  style="aspect-ratio: 16 / 10; object-fit: cover;" 
  loading="lazy" 
  decoding="async"
/>
```
*(Catatan: Gambar kartu teratas / LCP hero dapat menggunakan `loading="eager"` dan `fetchpriority="high"`)*.

#### B. Font Rendering (FOIT Elimination)
Di konfigurasi font framework (Astro/Next.js/HTML):
```javascript
fonts: [
  {
    provider: fontProviders.google(),
    name: "Inter",
    weights: [400, 500, 600, 700],
    display: "swap", // Wajib: teks langsung muncul seketika
    fallbacks: ["sans-serif"],
  }
]
```

---

### 5. Standar Favicon Google Search Snippet

Google Search menggunakan crawler gambar asinkron (**Googlebot-Image**) untuk mengambil favicon situs:

1. **Ukuran Wajib:** Siapkan ikon kelipatan 48 piksel persegi (`48x48`, `96x96`, `192x192`, dan `favicon.ico`).
2. **Deklarasi di `<head>`:**
   ```html
   <link rel="icon" href="/favicon.ico" sizes="any" />
   <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png" />
   <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png" />
   <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png" />
   <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
   ```
3. **Izin Robot:** Pastikan `public/robots.txt` tidak memblokir bot gambar:
   ```txt
   User-agent: Googlebot-Image
   Allow: /
   ```
4. **Percepatan:** Buka Google Search Console &rarr; Inspeksi URL Homepage &rarr; Klik **Minta Pengindeksan**.

> [!IMPORTANT]
> **Favicon TIDAK BOLEH dimasukkan ke dalam `sitemap.xml`**. Sitemap hanya untuk URL konten yang dapat diakses pengguna. Memasukkan file gambar antarmuka ke sitemap memboroskan crawl budget dan memicu peringatan non-HTML di Search Console.

---

### 6. Agentic Browsing & AI Discovery (Lighthouse 13.3+)

Agar lulus kategori audit *Agentic Browsing* dengan rasio sempurna:

1. **Pasang `/llms.txt` di Root Domain:**
   File Markdown ringkas yang memaparkan identitas redaksi/bisnis, bagian utama situs, dan tautan feed terverifikasi bagi crawler LLM.
2. **Pasang Web App Manifest (`/manifest.json`):**
   Metadata identitas aplikasi web, icon resolusi tinggi, tema warna, dan scope navigasi.
3. **Pasang Agentic Resource Discovery (`/ard.json`):**
   Spesifikasi kapabilitas situs (pencarian, arsip berita, RSS).
4. **Integrasikan Protokol WebMCP:**
   Daftarkan tool pencarian terstruktur ke API konteks peramban (`document.modelContext` / `navigator.modelContext`) agar AI Agent dapat mengeksekusi pencarian tanpa bergantung pada klik antarmuka visual.
5. **Buka Akses untuk AI Crawlers di `robots.txt`:**
   ```txt
   User-agent: GPTBot
   Allow: /

   User-agent: ClaudeBot
   Allow: /

   User-agent: PerplexityBot
   Allow: /
   ```

---

## Verifikasi & Standar Keberhasilan

Website dianggap selesai dioptimalkan ketika:

- [ ] Audit PageSpeed Insights pada URL kanonikal mencapai skor **Performance 90+**.
- [ ] Skor **SEO** dan **Best Practices** berada di angka **95–100**.
- [ ] Nilai **CLS (Cumulative Layout Shift)** kurang dari **0.05**.
- [ ] 100% gambar publik disajikan dalam format modern (WebP/AVIF).
- [ ] Header HTTP `Cache-Control` pada aset statis mengembalikan `public, max-age=31536000, immutable`.
- [ ] Endpoint `/llms.txt`, `/manifest.json`, dan `/ard.json` mengembalikan status `HTTP 200 OK`.
- [ ] Tidak ada tautan kosong (`href="#"` atau anchor tanpa `href`) yang memutus penelusuran crawler.
