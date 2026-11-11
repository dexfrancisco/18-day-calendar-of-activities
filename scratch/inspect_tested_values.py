import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

t_crop = Image.open(os.path.join(BASE_DIR, "scratch", "tested_title_crop.png"))
arr_t = np.array(t_crop)
print("Title crop shape:", arr_t.shape, "mean:", arr_t.mean(), "std:", arr_t.std())

d_crop = Image.open(os.path.join(BASE_DIR, "scratch", "tested_dock_crop.png"))
arr_d = np.array(d_crop)
print("Dock crop shape:", arr_d.shape, "mean:", arr_d.mean())

