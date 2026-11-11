import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

icon_crop = Image.open(os.path.join(BASE_DIR, "scratch", "crop_selected_icon.png"))
arr_icon = np.array(icon_crop)
print("Selected icon shape:", arr_icon.shape)
print("Selected icon mean:", arr_icon.mean(), "std:", arr_icon.std())

dock_crop = Image.open(os.path.join(BASE_DIR, "scratch", "crop_dock_selected.png"))
arr_dock = np.array(dock_crop)
print("Selected dock shape:", arr_dock.shape)
print("Selected dock mean:", arr_dock.mean())

