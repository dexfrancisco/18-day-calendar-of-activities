import os
import time
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PIL import Image
from pypdf import PdfWriter
import json

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9265

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

