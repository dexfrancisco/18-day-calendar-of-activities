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
PORT = 9349
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

days_to_render = ["11-day-11", "17-day-17", "18-day-18"]

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
    img.thumbnail((800, 1132))
    img.save(thumb_png)
    print(f"✓ Rendered 1x & saved to FABMAT/{fn}.png (300 DPI) in {time.time()-t0:.2f}s")

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
    print(f"✓ Rendered 2x to output/2x/{fn}.png in {time.time()-t0:.2f}s")

# Verification: Clearance & Crop into Artifacts
tmpl = Image.open(os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png")).convert('RGB')
tmpl_arr = np.array(tmpl.crop((190, 2400, 2290, 3100))).astype(int)

for fn in days_to_render:
    img = Image.open(os.path.join(BASE_DIR, "FABMAT", f"{fn}.png")).convert('RGB')
    crop_eval = img.crop((190, 2400, 2290, 3100))
    arr = np.array(crop_eval).astype(int)
    diff = np.abs(arr - tmpl_arr).sum(axis=-1)
    ys, xs = np.where(diff > 50)
    if len(ys) > 0:
        max_y = 2400 + np.max(ys)
        print(f"[{fn}] Lowest text pixel: y = {max_y} px | Clearance to hazard line (2950px): {2950-max_y} px | Clearance to jeepney (3115px): {3115-max_y} px")
    else:
        print(f"[{fn}] No text in 2400-3100 px")

    # Save artifact crop (content area)
    artifact_crop = img.crop((120, 1100, 2360, 2900))
    artifact_path = os.path.join(ARTIFACTS_DIR, f"crop_advocacy_{fn}.png")
    artifact_crop.save(artifact_path)
    print(f"✓ Saved verification artifact: {artifact_path}")

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

print(f"✓ Rebuilt combined PDF: {out_pdf}")
server.shutdown()

