import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
canvas_crop = Image.open(os.path.join(BASE_DIR, "scratch", "clean_canvas_crop.png"))
arr = np.array(canvas_crop)

# Let's inspect the icon zone (y: 120..350, x: 100..400)
icon_area = arr[120:350, 100:400]
print("Icon area mean:", icon_area.mean(), "std:", icon_area.std())

# Let's inspect the title zone (y: 400..600, x: 100..800)
title_area = arr[400:600, 100:800]
print("Title area mean:", title_area.mean(), "std:", title_area.std())

# Let's inspect the bottom details zone (y: 650..850, x: 100..800)
btm_area = arr[650:850, 100:800]
print("Bottom details area mean:", btm_area.mean(), "std:", btm_area.std())

