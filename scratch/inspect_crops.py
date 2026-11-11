import os
from PIL import Image

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
preview_path = os.path.join(BASE_DIR, "scratch", "editor_preview.png")

img = Image.open(preview_path)
print("Preview size:", img.size)

# Crop zones:
# 1. Top Bar: x: 0..1920, y: 0..60
top_bar = img.crop((0, 0, 1920, 60))
top_bar.save(os.path.join(BASE_DIR, "scratch", "editor_crop_topbar.png"))

# 2. Canvas Center: x: 450..1450, y: 60..1020
canvas_crop = img.crop((450, 60, 1450, 1020))
canvas_crop.save(os.path.join(BASE_DIR, "scratch", "editor_crop_canvas.png"))

# 3. Right Inspector: x: 1560..1920, y: 60..1080
inspector_crop = img.crop((1560, 60, 1920, 1080))
inspector_crop.save(os.path.join(BASE_DIR, "scratch", "editor_crop_inspector.png"))

# 4. Overview thumbnail: 960x540
thumb = img.resize((960, 540), Image.Resampling.LANCZOS)
thumb.save(os.path.join(BASE_DIR, "scratch", "editor_thumb.png"))

print("✓ Saved crops and thumbnail successfully")

