import os
import glob
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
tmpl_path = os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png")
tmpl = Image.open(tmpl_path)
tmpl_arr = np.array(tmpl)[:, :, :3].astype(int)

files = sorted(glob.glob(os.path.join(BASE_DIR, "FABMAT", "*.png")))
print(f"Measuring {len(files)} FABMAT posters against template...")
print(f"Target hazard line: y = 2950 px\n")

measurements = []

for fpath in files:
    fname = os.path.basename(fpath)
    if fname == "fabmat_template.png":
        continue
    
    im = Image.open(fpath)
    arr = np.array(im)[:, :, :3].astype(int)
    
    # Calculate difference with template
    diff = np.abs(arr - tmpl_arr)
    mask = np.max(diff, axis=2) > 30
    
    # Text region below top row: y from 1350 to 3200, x from 180 to 2300
    ys, xs = np.where(mask[1350:3200, 180:2300])
    if len(ys) > 0:
        max_y = 1350 + int(np.max(ys))
        clearance = 2950 - max_y
        measurements.append((fname, max_y, clearance))
    else:
        measurements.append((fname, 0, 9999))

print(f"{'FILENAME':22s} | {'MAX_Y':7s} | {'CLEARANCE':15s} | STATUS")
print("-" * 65)
for fn, my, cl in measurements:
    if cl > 180:
        status = "TOO MUCH SPACE (Clearance > 180px)"
    elif cl >= 70:
        status = "WELL BALANCED (70px-180px)"
    else:
        status = "TIGHT (< 70px)"
    print(f"{fn:22s} | {my:5d} px | +{cl:4d} px        | {status}")

