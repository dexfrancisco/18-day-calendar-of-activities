import os
import time
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PIL import Image
import numpy as np
from pypdf import PdfWriter
import json

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9355
ARTIFACTS_DIR = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()
print(f"Server started on port {PORT}")

fn = "02-day-02"
h_url = f"http://127.0.0.1:{PORT}/scratch/final_html/{fn}.html?v={int(time.time()*1000)}"
out_1x = os.path.join(BASE_DIR, "output", "1x", f"{fn}.png")
fabmat_png = os.path.join(BASE_DIR, "FABMAT", f"{fn}.png")
out_2x = os.path.join(BASE_DIR, "output", "2x", f"{fn}.png")
thumb_png = os.path.join(BASE_DIR, "scratch", "final_thumbs", f"{fn}_thumb.png")

# Render 1x (2480x3508)
cmd_1x = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--incognito",
    "--disable-application-cache",
    "--disk-cache-size=0",
    "--hide-scrollbars",
    "--force-device-scale-factor=1",
    "--window-size=2480,3508",
    f"--screenshot={os.path.abspath(out_1x)}",
    h_url
]
t0 = time.time()
subprocess.run(cmd_1x, check=True)

img = Image.open(out_1x)
img.save(fabmat_png, dpi=(300, 300))
img_thumb = img.copy()
img_thumb.thumbnail((800, 1132))
img_thumb.save(thumb_png)
print(f"Rendered 1x & saved to FABMAT/{fn}.png (300 DPI) in {time.time()-t0:.2f}s")

# Render 2x
cmd_2x = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--incognito",
    "--disable-application-cache",
    "--disk-cache-size=0",
    "--hide-scrollbars",
    "--force-device-scale-factor=2",
    "--window-size=2480,3508",
    f"--screenshot={os.path.abspath(out_2x)}",
    h_url
]
t0 = time.time()
subprocess.run(cmd_2x, check=True)
print(f"Rendered 2x to output/2x/{fn}.png in {time.time()-t0:.2f}s")

# Verification: Lowest text pixel y by comparing row-by-row from bottom up against fabmat_template.png
tmpl = Image.open(os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png")).convert('RGB')
fab_img = Image.open(fabmat_png).convert('RGB')

y_start = 2000
y_end = 3115
crop_eval = fab_img.crop((190, y_start, 2290, y_end))
crop_tmpl = tmpl.crop((190, y_start, 2290, y_end))

arr = np.array(crop_eval).astype(int)
tmpl_arr = np.array(crop_tmpl).astype(int)
diff = np.abs(arr - tmpl_arr).sum(axis=-1)

lowest_y = None
for y_rel in range(len(diff) - 1, -1, -1):
    pts = np.where(diff[y_rel] > 50)[0]
    if len(pts) > 5:
        lowest_y = y_start + y_rel
        break

if lowest_y is not None:
    print(f"[{fn}] Lowest text pixel: y = {lowest_y} px | Clearance to hazard line (2950px): {2950 - lowest_y} px | Clearance to jeepney (3115px): {3115 - lowest_y} px")
else:
    print(f"[{fn}] Warning: No text pixels detected in {y_start}-{y_end}")

# Save verification crops into Artifacts
# 1. FABMAT Day 2 crop
fab_crop = fab_img.crop((100, 1250, 2380, 3150))
fab_crop_path = os.path.join(ARTIFACTS_DIR, "crop_fabmat_d2_peso_cswdo.png")
fab_crop.save(fab_crop_path)
print(f"Saved FABMAT verification crop: {fab_crop_path}")

# 2. A3 Calendar Day 2 crop
cal_a3 = Image.open(os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_A3.png"))
cal_a3_crop = cal_a3.crop((840, 470, 1780, 1440))
cal_a3_crop_path = os.path.join(ARTIFACTS_DIR, "crop_cal_a3_d2_peso_cswdo.png")
cal_a3_crop.save(cal_a3_crop_path)
print(f"Saved A3 verification crop: {cal_a3_crop_path}")

# 3. A4 Page 1 Calendar Day 2 crop (Row 1 Col 3 of 4-col grid on 2480x3508)
cal_a4 = Image.open(os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_A4_Page1.png"))
cal_a4_crop = cal_a4.crop((1150, 350, 1950, 1650))
cal_a4_crop_path = os.path.join(ARTIFACTS_DIR, "crop_cal_a4_d2_peso_cswdo.png")
cal_a4_crop.save(cal_a4_crop_path)
print(f"Saved A4 verification crop: {cal_a4_crop_path}")

# Rebuild combined PDF
with open(os.path.join(BASE_DIR, "scratch", "schedule_data.json"), "r", encoding="utf-8") as f:
    schedule_data = json.load(f)

pdf_writer = PdfWriter()
temp_pdf_files = []
for day in schedule_data:
    dfn = day["filename"].replace(".png", "")
    src_png = os.path.join(BASE_DIR, "output", "1x", f"{dfn}.png")
    temp_pdf = os.path.join(BASE_DIR, "output", f"temp_{dfn}.pdf")
    pimg = Image.open(src_png).convert("RGB")
    pimg.save(temp_pdf, "PDF", resolution=300.0)
    temp_pdf_files.append(temp_pdf)
    pdf_writer.append(temp_pdf)

out_pdf = os.path.join(BASE_DIR, "output", "18-day-campaign-posters.pdf")
with open(out_pdf, "wb") as f:
    pdf_writer.write(f)

for tp in temp_pdf_files:
    try: os.remove(tp)
    except: pass

print(f"Rebuilt combined PDF: {out_pdf}")
server.shutdown()
