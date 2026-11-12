import os
import re
import subprocess
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9348

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

def measure_image(fpath):
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

def render_html(fn):
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

print("Starting surgical spacing adjustments...")

