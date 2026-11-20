# Optimasi Performa Web & SEO Modern

Skill untuk mendiagnosis dan merekayasa percepatan website hingga mencapai skor **PageSpeed 90+**, mengeliminasi **CLS (Cumulative Layout Shift)**, kompresi massal **WebP**, konfigurasi **Nginx 1-Year Immutable Caching**, serta implementasi standar baru **Agentic Browsing** (Lighthouse v13.3+).

---

## Bukti Hasil Uji Kinerja Nyata (PageSpeed Insights)

Berikut hasil benchmark nyata implementasi metodologi teknis skill ini pada portal web dinamis berbasis SSR:

![Bukti Skor PageSpeed 99](./assets/pagespeed-99-proof.jpg)

### Rekapitulasi Metrik:
* **Performance:** **99 / 100** 🟢
* **Best Practices:** **100 / 100** 🟢
* **SEO:** **100 / 100** 🟢
* **Accessibility:** **91 / 100** 🟢
* **Agentic Browsing:** **2 / 3** 🟡

---

## Fitur & Cakupan

1. **Konversi Media Massal ke WebP:** Skrip otomatis untuk merampingkan seluruh gambar raster JPEG/PNG ke WebP dengan penghematan payload 30% hingga 95% tanpa distorsi visual.
2. **Nginx High-Performance Caching:** Pengaturan *1-Year Immutable Cache* (`Cache-Control: public, max-age=31536000, immutable`) dan kompresi Gzip level 6 untuk aset statis dan font woff2.
3. **Eliminasi Total CLS:** Penetapan geometri pasti (`width`, `height`, dan CSS `aspect-ratio`) pada komponen grid dan banner gambar.
4. **Optimasi Rendering Teks (FOIT):** Penerapan `font-display: swap` untuk mencegah jeda rendering font.
5. **Standar Favicon Google Search Snippet:** Konfigurasi ikon 48px multi-resolusi (`48x48`, `96x96`, `192x192`, `apple-touch-icon`) dan aturan Googlebot-Image.
6. **Agentic Web & AI Discovery:** Penerapan `/llms.txt`, *Web App Manifest* (`/manifest.json`), *Agentic Resource Discovery* (`/ard.json`), serta pendaftaran tool WebMCP ke `document.modelContext`.

---

## Instalasi

```bash
npx skills add Fahrizp24/skills --skill optimasi-performa-seo
```

---

## Struktur Folder

```text
optimasi-performa-seo/
├── SKILL.md                          # Panduan alur kerja & pedoman teknis lengkap
├── README.md                         # Ringkasan & bukti uji kinerja
├── assets/
│   └── pagespeed-99-proof.jpg        # Bukti tangkapan layar PageSpeed Insights (tersanitasi)
├── templates/
│   ├── nginx-performance.conf        # Template konfigurasi Nginx caching & gzip
│   ├── llms.txt                      # Template discovery agen AI & LLM
│   ├── manifest.json                 # Template Web App Manifest
│   ├── ard.json                      # Template Agentic Resource Discovery
│   └── robots.txt                    # Template robots.txt dengan izin AI crawler
└── scripts/
    └── convert_webp.py               # Skrip python konversi gambar WebP otomatis
```

---

## Lisensi

MIT
