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
PORT = 9365
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

days_to_render = ["10-day-10", "11-day-11", "13-day-13"]
tmpl = Image.open(os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png")).convert("RGB")
tmpl_arr = np.array(tmpl.crop((190, 2000, 2290, 3115))).astype(int)

for fn in days_to_render:
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

    # Clearance & color check
    fab_img = Image.open(fabmat_png).convert("RGB")
    arr = np.array(fab_img.crop((190, 2000, 2290, 3115))).astype(int)
    diff = np.abs(arr - tmpl_arr).sum(axis=-1)
    lowest_y = None
    for y_rel in range(len(diff) - 1, -1, -1):
        if len(np.where(diff[y_rel] > 50)[0]) > 5:
            lowest_y = 2000 + y_rel
            break

    text_zone = np.array(fab_img.crop((190, 1300, 2290, 2940)))
    black_px = int(np.sum(np.all(text_zone < 30, axis=-1)))
    print(f"[{fn}] lowest_y={lowest_y} px | clearance_to_2950={2950 - lowest_y if lowest_y else 'N/A'} px | black_px={black_px}")

# Save verification crops
crop_map = {
    "10-day-10": "crop_fabmat_d10_swapped.png",
    "11-day-11": "crop_fabmat_d11_swapped.png",
    "13-day-13": "crop_fabmat_d13_leveling.png",
}
for fn, out_name in crop_map.items():
    fab_img = Image.open(os.path.join(BASE_DIR, "FABMAT", f"{fn}.png"))
    fab_img.crop((100, 1250, 2380, 3150)).save(os.path.join(ARTIFACTS_DIR, out_name))
    print(f"Saved {out_name}")

cal_a3 = Image.open(os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_A3.png"))
cal_a3.crop((2450, 1350, 4450, 2400)).save(os.path.join(ARTIFACTS_DIR, "crop_cal_a3_d10_d11.png"))
cal_a3.crop((50, 2350, 1000, 3450)).save(os.path.join(ARTIFACTS_DIR, "crop_cal_a3_d13.png"))
print("Saved A3 calendar verification crops")

cal_a4 = Image.open(os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_A4_Page2.png"))
cal_a4.crop((0, 300, 2480, 3450)).save(os.path.join(ARTIFACTS_DIR, "crop_cal_a4_d10_d11_d13.png"))
print("Saved A4 Page 2 verification crop")

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
