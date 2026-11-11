import os
from PIL import Image

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
preview_path = os.path.join(BASE_DIR, "scratch", "editor_selected_preview.png")

img = Image.open(preview_path)

# Crop around the Hero Icon area: x: 500..850, y: 380..650
icon_crop = img.crop((500, 380, 850, 650))
icon_crop.save(os.path.join(BASE_DIR, "scratch", "crop_selected_icon.png"))

# Crop options bar: x: 0..1200, y: 40..85
opt_crop = img.crop((0, 40, 1200, 85))
opt_crop.save(os.path.join(BASE_DIR, "scratch", "crop_options_bar.png"))

# Crop dock layers panel: x: 1550..1920, y: 85..500
dock_crop = img.crop((1550, 85, 1920, 500))
dock_crop.save(os.path.join(BASE_DIR, "scratch", "crop_dock_selected.png"))

print("✓ Saved inspection crops.")

