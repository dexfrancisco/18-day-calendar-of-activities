import os
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

canvas_crop = Image.open(os.path.join(BASE_DIR, "scratch", "editor_crop_canvas.png"))
arr = np.array(canvas_crop)
print("Canvas crop shape:", arr.shape)
# Inspect top of poster in viewport (around y=80..200), center (y=400..700), bottom (y=800..950)
print("Canvas crop top mean:", arr[80:200, 200:800].mean())
print("Canvas crop center mean:", arr[400:700, 200:800].mean())
print("Canvas crop bottom mean:", arr[800:950, 200:800].mean())

inspector_crop = Image.open(os.path.join(BASE_DIR, "scratch", "editor_crop_inspector.png"))
arr_ins = np.array(inspector_crop)
print("Inspector shape:", arr_ins.shape)
print("Inspector mean:", arr_ins.mean())

