"""
Auto-fix script for broken links and missing assets found in audit
"""
import os, re
from pathlib import Path

ROOT = Path(r"c:\My Web Sites\ajnets")

# ── FIX 1: Remove 'cart-page' link from pages that still reference it ──────
cart_re = re.compile(r'''<div class="octf-header-module cart-btn-hover">.*?</div>\s*</div>''', re.S)
cart_icon_re = re.compile(r'''<div class="octf-header-module cart-btn-hover">.*?</div>\s*\n?\s*</div>''', re.S)

# More targeted: remove just the cart icon wrapper
cart_block_re = re.compile(r'\s*<div class="octf-header-module cart-btn-hover">.*?</div>\s*(?=\s*<div)', re.S)
href_cart_re = re.compile(r'href="cart-page"', re.I)

fixes_made = 0
for html_path in sorted(ROOT.glob("*.html")):
    with open(html_path, encoding="utf-8", errors="ignore") as f:
        content = f.read()

    original = content
    # Fix cart-page href to point to book-consultation.html
    new_content = href_cart_re.sub('href="book-consultation.html"', content)
    # Also remove portfolio-details-[2,3] orphan hrefs -> point to client-success.html
    new_content = re.sub(r'href="portfolio-details-[23](?:\.html)?"', 'href="client-success.html"', new_content)
    
    if new_content != original:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        fixes_made += 1
        print(f"Fixed: {html_path.name}")

# ── FIX 2: Create placeholder client logo images that are missing ──────────
missing_assets = [
    "images/clients/client1.png",
    "images/clients/client2.png",
    "images/clients/client3.png",
    "images/clients/client4.png",
    "images/clients/client5.png",
    "images/clients/client6.png",
]

for asset in missing_assets:
    path = ROOT / asset
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        # Create a 1x1 transparent PNG
        import struct, zlib
        def create_tiny_png():
            sig = b'\x89PNG\r\n\x1a\n'
            ihdr_data = struct.pack('>IIBBBBB', 1, 1, 8, 2, 0, 0, 0)
            ihdr_crc = zlib.crc32(b'IHDR' + ihdr_data) & 0xffffffff
            ihdr = struct.pack('>I', 13) + b'IHDR' + ihdr_data + struct.pack('>I', ihdr_crc)
            raw = b'\x00\xFF\xFF\xFF'
            compressed = zlib.compress(raw)
            idat_crc = zlib.crc32(b'IDAT' + compressed) & 0xffffffff
            idat = struct.pack('>I', len(compressed)) + b'IDAT' + compressed + struct.pack('>I', idat_crc)
            iend_crc = zlib.crc32(b'IEND') & 0xffffffff
            iend = struct.pack('>I', 0) + b'IEND' + b'' + struct.pack('>I', iend_crc)
            return sig + ihdr + idat + iend
        with open(path, 'wb') as f:
            f.write(create_tiny_png())
        print(f"Created placeholder: {asset}")

print(f"\nTotal files fixed: {fixes_made}")
print("Done.")
