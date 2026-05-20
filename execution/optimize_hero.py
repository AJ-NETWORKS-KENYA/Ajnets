from PIL import Image
import os

img_path = r"c:\My Web Sites\ajnets\images\slider\slide1-home1.jpg"
out_path = r"c:\My Web Sites\ajnets\images\slider\slide1-home1.webp"

if os.path.exists(img_path):
    img = Image.open(img_path)
    img.save(out_path, "WEBP", quality=80)
    print("Converted slide image to WebP")
    
    # Update index.html to refer to the webp
    with open(r"c:\My Web Sites\ajnets\index.html", "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("images/slider/slide1-home1.jpg", "images/slider/slide1-home1.webp")
    with open(r"c:\My Web Sites\ajnets\index.html", "w", encoding="utf-8") as f:
        f.write(content)
else:
    print("Image not found")
