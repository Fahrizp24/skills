#!/usr/bin/env python3
"""
Skrip konversi massal gambar raster (JPEG/PNG) ke format WebP modern
dengan penghitungan otomatis penghematan bandwidth.

Penggunaan:
    python convert_webp.py --dir ./uploads --quality 82
"""

import os
import sys
import argparse
from PIL import Image

def convert_to_webp(target_dir, quality=82, keep_original=True):
    supported_exts = ('.jpg', '.jpeg', '.png')
    total_orig_bytes = 0
    total_webp_bytes = 0
    converted_count = 0

    print(f"[*] Memindai direktori: {target_dir}")
    for root, _, files in os.walk(target_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in supported_exts:
                orig_path = os.path.join(root, file)
                webp_path = os.path.splitext(orig_path)[0] + '.webp'

                # Lewati jika file webp sudah ada
                if os.path.exists(webp_path):
                    continue

                try:
                    orig_size = os.path.getsize(orig_path)
                    with Image.open(orig_path) as img:
                        # Tangani transparansi RGBA
                        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                            img.save(webp_path, 'WEBP', quality=quality, method=6)
                        else:
                            img = img.convert('RGB')
                            img.save(webp_path, 'WEBP', quality=quality, method=6)

                    webp_size = os.path.getsize(webp_path)
                    total_orig_bytes += orig_size
                    total_webp_bytes += webp_size
                    converted_count += 1

                    ratio = (1 - (webp_size / orig_size)) * 100 if orig_size > 0 else 0
                    print(f"[OK] {file} -> {os.path.basename(webp_path)} ({orig_size//1024}KB -> {webp_size//1024}KB, -{ratio:.1f}%)")

                    if not keep_original:
                        os.remove(orig_path)

                except Exception as e:
                    print(f"[ERR] Gagal mengonversi {file}: {e}", file=sys.stderr)

    saved_bytes = total_orig_bytes - total_webp_bytes
    print("\n" + "="*50)
    print(f"Total file dikonversi : {converted_count}")
    print(f"Ukuran asli total     : {total_orig_bytes / (1024*1024):.2f} MB")
    print(f"Ukuran WebP total     : {total_webp_bytes / (1024*1024):.2f} MB")
    if total_orig_bytes > 0:
        overall_saved = (saved_bytes / total_orig_bytes) * 100
        print(f"Penghematan bandwidth : {saved_bytes / (1024*1024):.2f} MB ({overall_saved:.1f}%)")
    print("="*50)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Konversi gambar ke WebP untuk performa web")
    parser.add_argument('--dir', required=True, help="Direktori target gambar")
    parser.add_argument('--quality', type=int, default=82, help="Kualitas kompresi WebP (default: 82)")
    parser.add_argument('--remove-original', action='store_true', help="Hapus file asli setelah konversi")
    args = parser.parse_args()

    convert_to_webp(args.dir, quality=args.quality, keep_original=not args.remove_original)
