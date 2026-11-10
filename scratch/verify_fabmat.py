import os
import json
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
tmpl = np.array(Image.open(os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png")).convert("RGB"))

with open(os.path.join(BASE_DIR, "scratch", "schedule_data.json"), "r", encoding="utf-8") as f:
    sched = json.load(f)

print(f"{'POSTER':<18} | {'MAX Y':<8} | {'BUFFER TO JEEP (2950)':<24} | {'STATUS'}")
print("-" * 70)
all_safe = True

for d in sched:
    fn = d["filename"]
    img_path = os.path.join(BASE_DIR, "FABMAT", fn)
    img = np.array(Image.open(img_path).convert("RGB"))
    diff = np.abs(img.astype(np.int32) - tmpl.astype(np.int32))
    mask = diff.max(axis=-1) > 40
    mask[:1310, :] = False
    y_idxs, x_idxs = np.where(mask)
    max_y = int(y_idxs.max())
    buf = 2950 - max_y
    is_safe = (max_y <= 2930)
    if not is_safe:
        all_safe = False
        stat = "⚠️ TOUCHING"
    else:
        stat = "✅ 100% SAFE"
    print(f"{fn:<18} | y={max_y:<5} | {buf:>4}px buffer              | {stat}")

print("-" * 70)
print(f"ALL 19 POSTERS IN FABMAT SAFE AND CLEAR: {all_safe}")

