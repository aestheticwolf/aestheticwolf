import shutil
from PIL import Image

src = r"C:/Users/richa/.gemini/antigravity/brain/c55eedce-f2fe-4537-a7bd-91c8d58d1d9e/.user_uploaded/media_1795120831650_addc655e.png"
dst = r"assets/richard-portrait.png"

im = Image.open(src)
print(f"Source image format: {im.format}, size: {im.size}, mode: {im.mode}")

# Check if image has an alpha channel
has_alpha = 'A' in im.getbands()
print(f"Has alpha channel: {has_alpha}")

if has_alpha:
    alpha = im.split()[-1]
    bbox = alpha.getbbox()
    extrema = alpha.getextrema()
    print(f"Alpha extrema: {extrema}")
    print(f"Non-zero alpha bounding box: {bbox}")

# Save working copy to assets/richard-portrait.png
im.save(dst, format="PNG")
print(f"Saved working copy to {dst}")
