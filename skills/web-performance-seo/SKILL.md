---
name: web-performance-seo
description: Technical web performance optimization, Core Web Vitals, and modern SEO (PageSpeed 90+, zero CLS, WebP compression, Nginx caching, and Agentic Browsing discovery).
version: 0.1.0
author: Fahri Zanuar Pradian (Fahrizp24), Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [SEO, Core Web Vitals, PageSpeed Insights, WebP, Nginx, Caching, CLS, LCP, Agentic Browsing, llms.txt, WebMCP]
    related_skills: [penulisan-ilmiah-indonesia]
---

# Web Performance & Technical SEO

An expert skill to analyze, diagnose, and execute technical web performance optimizations, Core Web Vitals (LCP, CLS, INP), on-page/technical SEO, and modern agentic web standards (*Agentic Browsing* and AI crawlers). This skill focuses on real engineering solutions backed by empirical metric data (Lighthouse, Google PageSpeed Insights, Chrome DevTools), not superficial keyword manipulation.

## When to Use

- Diagnosing low PageSpeed Insights / Lighthouse scores (e.g. red/orange zone < 70) and elevating them to the green zone (90–100).
- Eliminating visual instability and layout shifts (*Cumulative Layout Shift / CLS*).
- Reducing media transfer payloads through batch modern format conversion (WebP/AVIF).
- Hardening web servers (Nginx/Apache) for payload compression (Gzip/Brotli) and 1-year immutable browser caching.
- Eliminating font render-blocking (*Flash of Invisible Text / FOIT*) using the `font-display: swap` strategy.
- Fixing official favicon discovery for Google Search snippet logos.
- Implementing *Agentic Browsing* standards (Lighthouse v13.3+): `llms.txt`, *Web App Manifest*, *Agentic Resource Discovery* (`ard.json`), and WebMCP protocol integration.
- Deploying valid *Structured Data* (JSON-LD Schema.org) for NewsMediaOrganization, WebSite, and article breadcrumbs.

Do not use this skill for black-hat SEO, cloaking, link farming, or manipulative keyword stuffing.

## Core Principles

1. **Always Audit Canonical URLs:** Measure performance on the final canonical destination (e.g., `https://www.your-domain.com/`), never on redirect paths (HTTP or non-www) that incur 301 latency penalties.
2. **Server-Side Asset Optimization:** Do not rely on client-side scaling for oversized images. Perform WebP/AVIF conversion upstream in the server or build pipeline.
3. **Immutable Caching for Static Assets:** Deliver hashed static bundles (`/_astro/`, CSS, JS, WOFF2) with `Cache-Control: public, max-age=31536000, immutable`.
4. **Explicit Image Geometries:** Every `<img>` element must declare explicit `width`, `height`, and `aspect-ratio` attributes to prevent browser geometry recalculations (*reflow/CLS*).
5. **Non-Blocking Font Rendering:** Apply `display: swap` to all web fonts so text is immediately legible using system fallback fonts.
6. **Machine-Friendly Agentic Discovery:** Expose structured metadata for automated agents via `/llms.txt`, `/manifest.json`, and WebMCP integration (`document.modelContext`).

---

## Workflow & Step-by-Step Execution

### 1. Initial Diagnostic & Metric Audit

Run PageSpeed Insights / Lighthouse audits and categorize findings into five primary vectors:
- **Document Request Latency:** Are there redirect chains (HTTP &rarr; HTTPS or non-www &rarr; www)?
- **Media Transfer Weight:** How many KiB/MiB of uncompressed JPEG/PNG images exist?
- **Cache Lifetime Policies:** Are static assets being served without long-term expiration headers?
- **Visual Stability (CLS):** Which components cause elements to jump during render?
- **Agentic Browsing Score:** Are machine-discovery endpoints (`llms.txt`, manifest, WebMCP) active?

---

### 2. Media Optimization (Batch WebP Conversion)

Batch convert all raster images in the media/uploads directory to high-efficiency WebP format:

```bash
python scripts/convert_webp.py --dir ./uploads --quality 82
```

**Database & Content Synchronization:**
- If the application uses a database (SQLite/MySQL/PostgreSQL), update media references in content tables (`posts`, `pages`, `media`) from `.jpg`/`.png` to `.webp`.
- Always back up the database before running batch SQL replacements.
- Ensure primary UI brand assets (header logos, icons) are compressed without visual artifacts.

---

### 3. Web Server & Caching Engine (Nginx)

Apply hardened caching and compression directives to the Nginx server block:

```nginx
# High-Efficiency Gzip Compression
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

# 1-Year Immutable Caching for Build Bundles & Fonts
location /_astro/ {
    proxy_pass http://127.0.0.1:PORT;
    expires 1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
    access_log off;
}

# 1-Year Caching for WebP Media & Static Assets
location ~* \.(?:ico|css|js|gif|jpe?g|png|webp|svg|woff2?|eot|ttf)$ {
    proxy_pass http://127.0.0.1:PORT;
    expires 1y;
    add_header Cache-Control "public, max-age=31536000, immutable";
    access_log off;
}
```

Validate with `nginx -t` and reload the service.

---

### 4. Layout Shift (CLS) Elimination & Font Optimization

#### A. Preventing Layout Shift (CLS < 0.05)
Assign explicit dimensions and CSS aspect ratios across all card and banner templates:
```html
<img 
  src="/uploads/article-banner.webp" 
  alt="Article Title" 
  width="560" 
  height="380" 
  style="aspect-ratio: 16 / 10; object-fit: cover;" 
  loading="lazy" 
  decoding="async"
/>
```
*(Note: Use `loading="eager"` and `fetchpriority="high"` strictly for the primary above-the-fold hero / LCP candidate).*

#### B. Font Optimization (FOIT Elimination)
In the framework font configuration (Astro / Next.js / HTML):
```javascript
fonts: [
  {
    provider: fontProviders.google(),
    name: "Inter",
    weights: [400, 500, 600, 700],
    display: "swap", // Mandatory: renders text immediately with fallback
    fallbacks: ["sans-serif"],
  }
]
```

---

### 5. Google Search Snippet & Favicon Standard

Google Search utilizes an asynchronous image crawler (**Googlebot-Image**) to index site favicons:

1. **Size Requirement:** Provide icons in multiples of 48px square (`48x48`, `96x96`, `192x192`, and root `favicon.ico`).
2. **Head Declarations:**
   ```html
   <link rel="icon" href="/favicon.ico" sizes="any" />
   <link rel="icon" type="image/png" sizes="48x48" href="/favicon-48x48.png" />
   <link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png" />
   <link rel="icon" type="image/png" sizes="192x192" href="/favicon-192x192.png" />
   <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
   ```
3. **Robots Permission:** Ensure `public/robots.txt` explicitly allows the image crawler:
   ```txt
   User-agent: Googlebot-Image
   Allow: /
   ```
4. **Acceleration:** In Google Search Console &rarr; inspect homepage URL &rarr; click **Request Indexing**.

> [!IMPORTANT]
> **Favicons MUST NOT be added to `sitemap.xml`**. Sitemaps are reserved for indexable content pages. Listing UI assets in a sitemap wastes crawl budget and generates non-HTML errors in Search Console.

---

### 6. Agentic Browsing & AI Discovery (Lighthouse 13.3+)

To pass the *Agentic Browsing* audit category with top marks:

1. **Place `/llms.txt` at the Domain Root:**
   A clean Markdown context file detailing brand identity, editorial policies, and official feed links for AI crawlers.
2. **Deploy Web App Manifest (`/manifest.json`):**
   Standard PWA metadata including name, theme colors, and high-resolution icons.
3. **Deploy Agentic Resource Discovery (`/ard.json`):**
   Machine-readable declaration of site capabilities (search API, archives, RSS).
4. **Integrate WebMCP Protocol:**
   Register structured search tools with browser model context APIs (`document.modelContext` / `navigator.modelContext`) enabling AI agents to search content programmatically without fragile DOM clicking.
5. **Permit AI Crawlers in `robots.txt`:**
   ```txt
   User-agent: GPTBot
   Allow: /

   User-agent: ClaudeBot
   Allow: /

   User-agent: PerplexityBot
   Allow: /
   ```

---

## Verification & Acceptance Checklist

A website is considered fully optimized when:

- [ ] PageSpeed Insights audit on the canonical URL achieves a **Performance score of 90+**.
- [ ] **SEO** and **Best Practices** scores reach **95–100**.
- [ ] **CLS (Cumulative Layout Shift)** is strictly below **0.05**.
- [ ] 100% of public images serve modern WebP/AVIF formats.
- [ ] Static asset HTTP responses return `Cache-Control: public, max-age=31536000, immutable`.
- [ ] Discovery endpoints (`/llms.txt`, `/manifest.json`, `/ard.json`) return `HTTP 200 OK`.
- [ ] Zero dead anchors (`href="#"` or missing `href`) exist in production templates.
