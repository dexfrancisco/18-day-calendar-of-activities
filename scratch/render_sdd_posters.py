import os
import sys
import time
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9361
ARTIFACTS_DIR = r"C:\Users\CODEX\.gemini\antigravity\brain\b7c2e81a-36ee-4a46-9056-c62523c3de30"
SDD_HTML_DIR = os.path.join(BASE_DIR, "scratch", "final_html_sdd")
SDD_OUT_DIR = os.path.join(BASE_DIR, "FABMAT with SDD")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

def render_poster(fn):
    h_url = f"http://127.0.0.1:{PORT}/scratch/final_html_sdd/{fn}.html?v={int(time.time()*1000)}"
    out_png = os.path.join(SDD_OUT_DIR, f"{fn}.png")
    temp_png = os.path.join(BASE_DIR, "scratch", f"_temp_sdd_{fn}.png")

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
        f"--screenshot={os.path.abspath(temp_png)}",
        h_url
    ]
    t0 = time.time()
    subprocess.run(cmd_1x, check=True)
    img = Image.open(temp_png)
    img.save(out_png, dpi=(300, 300))
    img.close()
    os.remove(temp_png)
    print(f"Rendered {fn}.png to FABMAT with SDD/ (300 DPI) in {time.time()-t0:.2f}s")
    return out_png

def measure_poster(fn, out_png):
    tmpl = Image.open(os.path.join(SDD_OUT_DIR, "fabmat_template.png")).convert("RGB")
    img = Image.open(out_png).convert("RGB")

    # Measure lowest text pixel
    y_start = 2000
    y_end = 3115
    diff_bot = np.abs(
        np.array(img.crop((190, y_start, 2290, y_end))).astype(int)
        - np.array(tmpl.crop((190, y_start, 2290, y_end))).astype(int)
    ).sum(axis=-1)

    lowest_y = None
    for y_rel in range(len(diff_bot) - 1, -1, -1):
        if len(np.where(diff_bot[y_rel] > 50)[0]) > 5:
            lowest_y = y_start + y_rel
            break

    # Measure right-most changed pixel across content area (y in 2000..2950)
    diff_content = np.abs(
        np.array(img.crop((0, 2000, 2480, 2950))).astype(int)
        - np.array(tmpl.crop((0, 2000, 2480, 2950))).astype(int)
    ).sum(axis=-1)
    xs_content = np.where(diff_content > 50)[1]
    content_xmax = int(xs_content.max()) if len(xs_content) > 0 else -1

    # Check pure black pixels in text zone
    text_zone = np.array(img.crop((190, 1300, 2290, 2940)))
    black_px = int(np.sum(np.all(text_zone < 30, axis=-1)))

    print(f"[{fn}] lowest_y={lowest_y} px | clearance_to_2950={2950 - lowest_y if lowest_y else 'N/A'} px | content_xmax={content_xmax} px | black_px={black_px}")
    return lowest_y, content_xmax, black_px

def main():
    poster_ids = sys.argv[1:] if len(sys.argv) > 1 else ["01-day-01"]
    server = HTTPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    print(f"Server started on port {PORT}")

    try:
        for fn in poster_ids:
            out_png = render_poster(fn)
            lowest_y, content_xmax, black_px = measure_poster(fn, out_png)

            img = Image.open(out_png)
            crop = img.crop((100, 1250, 2420, 3150))
            crop_path = os.path.join(ARTIFACTS_DIR, f"crop_sdd_{fn}.png")
            crop.save(crop_path)
            print(f"Saved verification crop: {crop_path}")
    finally:
        server.shutdown()

if __name__ == "__main__":
    main()
