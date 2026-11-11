import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
preview_path = os.path.join(BASE_DIR, "scratch", "editor_preview.png")

img = Image.open(preview_path)
print("Preview size:", img.size)

# Crop zones:
# 1. Top bar & Options bar: x: 0..1920, y: 0..85
top_crop = img.crop((0, 0, 1920, 85))
top_crop.save(os.path.join(BASE_DIR, "scratch", "ps_crop_top.png"))

# 2. Left toolbar: x: 0..48, y: 85..600
left_crop = img.crop((0, 85, 48, 600))
left_crop.save(os.path.join(BASE_DIR, "scratch", "ps_crop_toolbar.png"))

# 3. Canvas area: x: 450..1540, y: 85..1050
canvas_crop = img.crop((450, 85, 1540, 1050))
canvas_crop.save(os.path.join(BASE_DIR, "scratch", "ps_crop_canvas.png"))

# 4. Right Dock (Layers panel): x: 1550..1920, y: 85..1050
dock_crop = img.crop((1550, 85, 1920, 1050))
dock_crop.save(os.path.join(BASE_DIR, "scratch", "ps_crop_dock.png"))

# Overview thumb: 960x540
thumb = img.resize((960, 540), Image.Resampling.LANCZOS)
thumb.save(os.path.join(BASE_DIR, "scratch", "ps_studio_thumb.png"))

# Inspect canvas colors
arr_can = np.array(canvas_crop)
print("Canvas crop mean:", arr_can.mean(), "std:", arr_can.std())
print("Unique colors in canvas crop:", len(np.unique(arr_can.reshape(-1, arr_can.shape[-1]), axis=0)))

# Inspect dock
arr_dock = np.array(dock_crop)
print("Dock crop mean:", arr_dock.mean())

