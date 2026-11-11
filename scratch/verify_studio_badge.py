import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
img = Image.open(os.path.join(BASE_DIR, "scratch", "clean_editor_preview.png"))

# Crop logo area: x: 10..150, y: 5..40
logo_crop = img.crop((10, 5, 150, 40))
logo_crop.save(os.path.join(BASE_DIR, "scratch", "studio_badge_crop.png"))

arr = np.array(logo_crop)
# Find orange pixels (R > 200, G in [70, 150], B < 50)
is_orange = (arr[:, :, 0] > 200) & (arr[:, :, 1] > 70) & (arr[:, :, 1] < 160) & (arr[:, :, 2] < 50)
print("Orange pixels count:", np.sum(is_orange))
print("Badge crop size:", logo_crop.size)

