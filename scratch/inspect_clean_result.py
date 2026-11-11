import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
img = Image.open(os.path.join(BASE_DIR, "scratch", "clean_editor_preview.png"))

arr = np.array(img)
# 1. Top bar: y=0..44. Mean color should be dark (#2c2c2c = ~44)
print("Top bar mean color:", arr[0:44, 100:1500].mean(axis=(0,1)))

# 2. Canvas center: x=500..1400, y=100..900
center = arr[100:900, 500:1400]
print("Canvas center mean:", center.mean())
print("Canvas center unique colors:", len(np.unique(center.reshape(-1, center.shape[-1]), axis=0)))

# 3. Crop canvas and save
canvas_crop = img.crop((500, 85, 1400, 1000))
canvas_crop.save(os.path.join(BASE_DIR, "scratch", "clean_canvas_crop.png"))

# 4. Crop top bar and save
top_crop = img.crop((0, 0, 1920, 85))
top_crop.save(os.path.join(BASE_DIR, "scratch", "clean_top_crop.png"))

# 5. Crop right dock
dock_crop = img.crop((1550, 44, 1920, 800))
dock_crop.save(os.path.join(BASE_DIR, "scratch", "clean_dock_crop.png"))

print("✓ Saved inspection crops successfully.")

