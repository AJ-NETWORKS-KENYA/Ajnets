"""
Generate favicon files from SVG logo
Requires: pip install Pillow cairosvg
"""

import os
from pathlib import Path

try:
    from PIL import Image
    import cairosvg
    
    print("\n🎨 Generating Favicon from SVG...")
    print("=" * 40)
    
    # Paths
    svg_path = "images/logo-transparent.svg"
    output_dir = "images"
    
    # Read SVG content
    with open(svg_path, 'rb') as f:
        svg_data = f.read()
    
    # Generate PNG at high resolution first (for better quality)
    print("\n📐 Converting SVG to PNG (512x512)...")
    png_data = cairosvg.svg2png(
        bytestring=svg_data,
        output_width=512,
        output_height=512
    )
    
    # Open with Pillow
    from io import BytesIO
    img = Image.open(BytesIO(png_data))
    
    # Generate different sizes
    sizes = {
        'favicon-16x16.png': (16, 16),
        'favicon-32x32.png': (32, 32),
        'favicon-48x48.png': (48, 48),
        'apple-touch-icon.png': (180, 180),
        'android-chrome-192x192.png': (192, 192),
        'android-chrome-512x512.png': (512, 512),
    }
    
    print("\n📦 Generating favicon files...")
    for filename, size in sizes.items():
        resized = img.resize(size, Image.Resampling.LANCZOS)
        output_path = os.path.join(output_dir, filename)
        resized.save(output_path, 'PNG', optimize=True)
        file_size = os.path.getsize(output_path) / 1024
        print(f"  ✓ {filename:30s} ({file_size:.1f} KB)")
    
    # Generate .ico file with multiple sizes
    print("\n🎯 Generating favicon.ico (multi-size)...")
    ico_sizes = [(16, 16), (32, 32), (48, 48)]
    ico_images = [img.resize(size, Image.Resampling.LANCZOS) for size in ico_sizes]
    ico_path = os.path.join(output_dir, 'favicon.ico')
    ico_images[0].save(
        ico_path,
        format='ICO',
        sizes=ico_sizes,
        append_images=ico_images[1:]
    )
    ico_size = os.path.getsize(ico_path) / 1024
    print(f"  ✓ favicon.ico (16x16, 32x32, 48x48) ({ico_size:.1f} KB)")
    
    print("\n✅ SUCCESS! All favicon files generated")
    print(f"\n📁 Files saved to: {os.path.abspath(output_dir)}")
    
except ImportError as e:
    print("\n❌ Missing required packages!")
    print("\nPlease install:")
    print("  pip install Pillow cairosvg")
    print("\nFor Windows, you may also need:")
    print("  1. Download GTK runtime from: https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer")
    print("  2. Or use: pip install pillow cairosvg pycairo")
    print(f"\nError: {e}")

except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nAlternative: Use an online tool like:")
    print("  • https://realfavicongenerator.net/")
    print("  • https://favicon.io/")
