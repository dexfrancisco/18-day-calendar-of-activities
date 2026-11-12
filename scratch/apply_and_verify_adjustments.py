import os
import re
import subprocess
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PIL import Image
import numpy as np
from pypdf import PdfWriter
import json

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9349

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()
print(f"Server started on port {PORT}")

tmpl_path = os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png")
tmpl = Image.open(tmpl_path)
tmpl_arr = np.array(tmpl)[:, :, :3].astype(int)

def measure(fpath):
    im = Image.open(fpath)
    arr = np.array(im)[:, :, :3].astype(int)
    diff = np.abs(arr - tmpl_arr)
    mask = np.max(diff, axis=2) > 30
    ys, xs = np.where(mask[1350:3200, 180:2300])
    if len(ys) > 0:
        max_y = 1350 + int(np.max(ys))
        clearance = 2950 - max_y
        return max_y, clearance
    return 0, 9999

def render(fn):
    h_url = f"http://127.0.0.1:{PORT}/scratch/final_html/{fn}.html?v={int(time.time()*1000)}"
    out_1x = os.path.join(BASE_DIR, "output", "1x", f"{fn}.png")
    fabmat_png = os.path.join(BASE_DIR, "FABMAT", f"{fn}.png")
    out_2x = os.path.join(BASE_DIR, "output", "2x", f"{fn}.png")
    thumb_png = os.path.join(BASE_DIR, "scratch", "final_thumbs", f"{fn}_thumb.png")

    cmd_1x = [
        CHROME_PATH, "--headless=new", "--disable-gpu", "--incognito",
        "--disable-application-cache", "--disk-cache-size=0", "--hide-scrollbars",
        "--force-device-scale-factor=1", "--window-size=2480,3508",
        f"--screenshot={os.path.abspath(out_1x)}", h_url
    ]
    subprocess.run(cmd_1x, check=True)
    img = Image.open(out_1x)
    img.save(fabmat_png, dpi=(300, 300))
    img.thumbnail((800, 1132))
    img.save(thumb_png)

    cmd_2x = [
        CHROME_PATH, "--headless=new", "--disable-gpu", "--incognito",
        "--disable-application-cache", "--disk-cache-size=0", "--hide-scrollbars",
        "--force-device-scale-factor=2", "--window-size=2480,3508",
        f"--screenshot={os.path.abspath(out_2x)}", h_url
    ]
    subprocess.run(cmd_2x, check=True)
    return measure(fabmat_png)

# -------------------------------------------------------------
# 1. 00-pre-campaign.html
# -------------------------------------------------------------
p00 = os.path.join(BASE_DIR, "scratch", "final_html", "00-pre-campaign.html")
with open(p00, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".stroke-title { font-size: 112px; }", ".stroke-title { font-size: 122px; line-height: 1.15; }")
c = c.replace(".stroke-subtitle { font-size: 76px; }", ".stroke-subtitle { font-size: 82px; }")
c = c.replace("gap: 36px;", "gap: 46px;")
c = c.replace("gap: 16px; width: 100%;", "gap: 22px; width: 100%;")
c = c.replace(".detail-label-col { width: 420px; flex-shrink: 0; font-size: 54px; }", ".detail-label-col { width: 440px; flex-shrink: 0; font-size: 58px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 58px; }", ".detail-val-col { flex: 1; font-size: 62px; }")
with open(p00, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 2. 02-day-02.html
# -------------------------------------------------------------
p02 = os.path.join(BASE_DIR, "scratch", "final_html", "02-day-02.html")
with open(p02, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 12px #FF6D00;\n    font-size: 52px;", ".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 12px #FF6D00;\n    font-size: 56px;")
c = c.replace(".act-lead-lbl {\n    font-size: 40px;", ".act-lead-lbl {\n    font-size: 44px;")
c = c.replace(".act-lead-val {\n    font-size: 44px;", ".act-lead-val {\n    font-size: 48px;")
c = c.replace(".detail-label-col {\n    width: 360px;\n    flex-shrink: 0;\n    font-size: 44px;", ".detail-label-col {\n    width: 380px;\n    flex-shrink: 0;\n    font-size: 48px;")
c = c.replace(".detail-val-col {\n    flex: 1;\n    font-size: 44px;", ".detail-val-col {\n    flex: 1;\n    font-size: 48px;")
c = c.replace("gap: 20px;", "gap: 24px;")
c = c.replace("margin: 4px 0;", "margin: 8px 0;")
with open(p02, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 3. 03-day-03.html
# -------------------------------------------------------------
p03 = os.path.join(BASE_DIR, "scratch", "final_html", "03-day-03.html")
with open(p03, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 11px #FF6D00;\n    font-size: 45px;", ".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 11px #FF6D00;\n    font-size: 48px;")
c = c.replace(".act-lead-lbl {\n    font-size: 36px;", ".act-lead-lbl {\n    font-size: 38px;")
c = c.replace(".act-lead-val {\n    font-size: 40px;", ".act-lead-val {\n    font-size: 42px;")
c = c.replace(".detail-label-col {\n    width: 350px;\n    flex-shrink: 0;\n    font-size: 42px;", ".detail-label-col {\n    width: 360px;\n    flex-shrink: 0;\n    font-size: 44px;")
c = c.replace(".detail-val-col {\n    flex: 1;\n    font-size: 42px;", ".detail-val-col {\n    flex: 1;\n    font-size: 44px;")
c = c.replace("gap: 16px;\n}", "gap: 18px;\n}")
c = c.replace("margin: 3px 0;", "margin: 6px 0;")
with open(p03, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 4. 05-day-05.html
# -------------------------------------------------------------
p05 = os.path.join(BASE_DIR, "scratch", "final_html", "05-day-05.html")
with open(p05, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("gap: 40px;", "gap: 55px;")
c = c.replace("margin-top: 20px;", "margin-top: 40px;")
c = c.replace(".stroke-title { font-size: 96px; line-height: 1.25; max-width: 1850px; }", ".stroke-title { font-size: 112px; line-height: 1.25; max-width: 1950px; }")
c = c.replace(".online-pill { font-size: 68px; letter-spacing: 3px; }", ".online-pill { font-size: 78px; letter-spacing: 4px; }")
with open(p05, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 5. 06-day-06.html
# -------------------------------------------------------------
p06 = os.path.join(BASE_DIR, "scratch", "final_html", "06-day-06.html")
with open(p06, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".stroke-title { font-size: 92px; line-height: 1.16; }", ".stroke-title { font-size: 102px; line-height: 1.18; }")
c = c.replace("gap: 28px;", "gap: 36px;")
c = c.replace(".detail-label-col { width: 420px; flex-shrink: 0; font-size: 52px; }", ".detail-label-col { width: 440px; flex-shrink: 0; font-size: 56px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 56px; }", ".detail-val-col { flex: 1; font-size: 60px; line-height: 1.2; }")
c = c.replace("gap: 12px; width: 100%;", "gap: 18px; width: 100%;")
with open(p06, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 6. 07-day-07.html
# -------------------------------------------------------------
p07 = os.path.join(BASE_DIR, "scratch", "final_html", "07-day-07.html")
with open(p07, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".stroke-title { font-size: 108px; line-height: 1.16; }", ".stroke-title { font-size: 122px; line-height: 1.18; }")
c = c.replace("gap: 36px;", "gap: 46px;")
c = c.replace(".detail-label-col { width: 420px; flex-shrink: 0; font-size: 54px; }", ".detail-label-col { width: 440px; flex-shrink: 0; font-size: 60px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 58px; }", ".detail-val-col { flex: 1; font-size: 64px; }")
c = c.replace("gap: 16px; width: 100%;", "gap: 22px; width: 100%;")
with open(p07, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 7. 08-day-08.html
# -------------------------------------------------------------
p08 = os.path.join(BASE_DIR, "scratch", "final_html", "08-day-08.html")
with open(p08, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".acts-block {\n            display: flex;\n            flex-direction: column;\n            gap: 30px;", ".acts-block {\n            display: flex;\n            flex-direction: column;\n            gap: 36px;")
c = c.replace(".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 12px #FF6D00;\n}", ".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 12px #FF6D00;\n    font-size: 78px;\n}")
c = c.replace(".detail-label-col { width: 420px; flex-shrink: 0; font-size: 54px; }", ".detail-label-col { width: 440px; flex-shrink: 0; font-size: 58px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 58px; }", ".detail-val-col { flex: 1; font-size: 62px; }")
with open(p08, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 8. 11-day-11.html
# -------------------------------------------------------------
p11 = os.path.join(BASE_DIR, "scratch", "final_html", "11-day-11.html")
with open(p11, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("gap: 32px;", "gap: 46px;")
c = c.replace(".hybrid-container {\n            display: flex;\n            flex-direction: column;\n            gap: 22px;", ".hybrid-container {\n            display: flex;\n            flex-direction: column;\n            gap: 34px;")
c = c.replace(".track-tag {\n            font-size: 46px;", ".track-tag {\n            font-size: 54px;\n            letter-spacing: 2px;")
c = c.replace('font-size:64px; line-height:1.18;', 'font-size:76px; line-height:1.2;')
c = c.replace('font-size:56px; line-height:1.18;', 'font-size:66px; line-height:1.2;')
c = c.replace('font-size:46px;', 'font-size:50px;')
c = c.replace('font-size:48px;', 'font-size:54px;')
c = c.replace(".detail-label-col { width: 400px; flex-shrink: 0; font-size: 50px; }", ".detail-label-col { width: 420px; flex-shrink: 0; font-size: 54px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 54px; }", ".detail-val-col { flex: 1; font-size: 58px; }")
with open(p11, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 9. 12-day-12.html
# -------------------------------------------------------------
p12 = os.path.join(BASE_DIR, "scratch", "final_html", "12-day-12.html")
with open(p12, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("gap: 40px;", "gap: 55px;")
c = c.replace("margin-top: 20px;", "margin-top: 40px;")
c = c.replace(".stroke-title { font-size: 96px; line-height: 1.25; max-width: 1850px; }", ".stroke-title { font-size: 112px; line-height: 1.25; max-width: 1950px; }")
c = c.replace(".online-pill { font-size: 68px; letter-spacing: 3px; }", ".online-pill { font-size: 78px; letter-spacing: 4px; }")
with open(p12, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 10. 15-day-15.html
# -------------------------------------------------------------
p15 = os.path.join(BASE_DIR, "scratch", "final_html", "15-day-15.html")
with open(p15, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".act-desc {\n            font-size: 58px;\n            line-height: 1.15;\n            flex: 1;\n        }", ".act-desc {\n            font-size: 68px;\n            line-height: 1.18;\n            flex: 1;\n        }")
c = c.replace(".act-num {\n            font-size: 64px;", ".act-num {\n            font-size: 72px;")
c = c.replace(".act-lead-lbl {\n            font-size: 40px;", ".act-lead-lbl {\n            font-size: 46px;")
c = c.replace(".act-lead-val {\n            font-size: 44px;", ".act-lead-val {\n            font-size: 50px;")
c = c.replace("gap: 18px;\n            width: 100%;", "gap: 26px;\n            width: 100%;")
c = c.replace("gap: 20px;\n        }", "gap: 28px;\n        }")
c = c.replace(".detail-label-col { width: 380px; flex-shrink: 0; font-size: 46px; }", ".detail-label-col { width: 420px; flex-shrink: 0; font-size: 52px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 48px; }", ".detail-val-col { flex: 1; font-size: 52px; line-height: 1.2; }")
c = c.replace("gap: 10px;\n            width: 100%;", "gap: 16px;\n            width: 100%;")
with open(p15, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 11. 16-day-16.html
# -------------------------------------------------------------
p16 = os.path.join(BASE_DIR, "scratch", "final_html", "16-day-16.html")
with open(p16, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 12px #FF6D00;\n}", ".stroke-act-desc {\n    color: #FFFFFF;\n    font-family: 'Gotham Bold', sans-serif;\n    paint-order: stroke fill;\n    -webkit-text-stroke: 12px #FF6D00;\n    font-size: 80px;\n}")
c = c.replace("gap: 30px;\n            width: 100%;", "gap: 38px;\n            width: 100%;")
c = c.replace(".detail-label-col { width: 420px; flex-shrink: 0; font-size: 54px; }", ".detail-label-col { width: 440px; flex-shrink: 0; font-size: 60px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 58px; }", ".detail-val-col { flex: 1; font-size: 64px; }")
c = c.replace("gap: 16px;\n            width: 100%;", "gap: 22px;\n            width: 100%;")
with open(p16, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 12. 17-day-17.html
# -------------------------------------------------------------
p17 = os.path.join(BASE_DIR, "scratch", "final_html", "17-day-17.html")
with open(p17, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("gap: 32px;\n        }", "gap: 46px;\n        }")
c = c.replace(".hybrid-container {\n            display: flex;\n            flex-direction: column;\n            gap: 22px;", ".hybrid-container {\n            display: flex;\n            flex-direction: column;\n            gap: 32px;")
c = c.replace(".track-tag {\n            font-size: 46px;", ".track-tag {\n            font-size: 54px;\n            letter-spacing: 2px;")
c = c.replace('font-size:64px; line-height:1.18;', 'font-size:76px; line-height:1.2;')
c = c.replace('font-size:56px; line-height:1.18;', 'font-size:66px; line-height:1.2;')
c = c.replace('font-size:46px;', 'font-size:50px;')
c = c.replace('font-size:48px;', 'font-size:54px;')
c = c.replace(".detail-label-col { width: 400px; flex-shrink: 0; font-size: 50px; }", ".detail-label-col { width: 420px; flex-shrink: 0; font-size: 56px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 54px; }", ".detail-val-col { flex: 1; font-size: 60px; }")
with open(p17, "w", encoding="utf-8") as f:
    f.write(c)

# -------------------------------------------------------------
# 13. 18-day-18.html
# -------------------------------------------------------------
p18 = os.path.join(BASE_DIR, "scratch", "final_html", "18-day-18.html")
with open(p18, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("gap: 26px;\n        }", "gap: 36px;\n        }")
c = c.replace(".hybrid-container {\n            display: flex;\n            flex-direction: column;\n            gap: 18px;", ".hybrid-container {\n            display: flex;\n            flex-direction: column;\n            gap: 26px;")
c = c.replace(".track-tag {\n            font-size: 46px;", ".track-tag {\n            font-size: 52px;\n            letter-spacing: 2px;")
c = c.replace('font-size:58px; line-height:1.18;', 'font-size:66px; line-height:1.18;')
c = c.replace('font-size:58px; width:66px;', 'font-size:66px; width:74px;')
c = c.replace('font-size:56px; line-height:1.18;', 'font-size:62px; line-height:1.18;')
c = c.replace('font-size:46px;', 'font-size:48px;')
c = c.replace('font-size:48px;', 'font-size:52px;')
c = c.replace(".detail-label-col { width: 400px; flex-shrink: 0; font-size: 50px; }", ".detail-label-col { width: 420px; flex-shrink: 0; font-size: 54px; }")
c = c.replace(".detail-val-col { flex: 1; font-size: 54px; }", ".detail-val-col { flex: 1; font-size: 58px; }")
with open(p18, "w", encoding="utf-8") as f:
    f.write(c)

print("All HTML files updated. Now rendering and measuring...")

adjusted_files = [
    "00-pre-campaign", "02-day-02", "03-day-03", "05-day-05", "06-day-06",
    "07-day-07", "08-day-08", "11-day-11", "12-day-12", "15-day-15",
    "16-day-16", "17-day-17", "18-day-18"
]

results = []
for fn in adjusted_files:
    my, cl = render(fn)
    results.append((fn, my, cl))
    print(f"✓ {fn:18s}: max_y = {my:4d} px | clearance = +{cl:3d} px")

# Rebuild combined PDF
print("\nRebuilding combined PDF...")
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

