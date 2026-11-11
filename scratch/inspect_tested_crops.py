import os
from PIL import Image

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
p = Image.open(os.path.join(BASE_DIR, "scratch", "perfect_studio_tested.png"))

# Crop title area: x: 500..1400, y: 550..750
title_crop = p.crop((500, 550, 1400, 750))
title_crop.save(os.path.join(BASE_DIR, "scratch", "tested_title_crop.png"))

# Crop dock layers panel: x: 1550..1920, y: 85..450
dock_crop = p.crop((1550, 85, 1920, 450))
dock_crop.save(os.path.join(BASE_DIR, "scratch", "tested_dock_crop.png"))

print("✓ Saved title and dock crops from tested studio.")

