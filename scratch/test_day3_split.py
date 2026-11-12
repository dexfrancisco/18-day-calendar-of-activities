import os
import subprocess
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PIL import Image
import numpy as np

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9346

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

# Build test HTML for Day 3
d3_html = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
@font-face { font-family: 'Gotham Ultra'; src: url('/Gotham-font-family/Gotham/Gotham-Ultra.otf') format('opentype'); font-weight: 900; }
@font-face { font-family: 'Gotham Bold'; src: url('/Gotham-font-family/Gotham/Gotham-Bold.otf') format('opentype'); font-weight: 700; }
@font-face { font-family: 'Gotham Medium'; src: url('/Gotham-font-family/Gotham/Gotham-Medium.otf') format('opentype'); font-weight: 500; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    width: 2480px; height: 3508px; margin: 0; padding: 0; overflow: hidden;
    background: url('/FABMAT/fabmat_template.png') no-repeat top left;
    background-size: 2480px 3508px;
    font-family: 'Gotham Bold', sans-serif;
    -webkit-font-smoothing: antialiased;
}
.stroke-day {
    color: #FFFFFF; font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 3px; line-height: 1.05; paint-order: stroke fill;
    -webkit-text-stroke: 18px #FF6D00; font-size: 136px;
}
.stroke-date {
    color: #FFFFFF; font-family: 'Gotham Bold', sans-serif;
    letter-spacing: 2px; line-height: 1.15; paint-order: stroke fill;
    -webkit-text-stroke: 12px #FF6D00; font-size: 60px;
}
.stroke-num {
    color: #FFFFFF; font-family: 'Gotham Ultra', sans-serif;
    line-height: 1.1; paint-order: stroke fill; -webkit-text-stroke: 13px #FF6D00;
    font-size: 50px; flex-shrink: 0; width: 56px;
}
.stroke-act-desc {
    color: #FFFFFF; font-family: 'Gotham Bold', sans-serif;
    paint-order: stroke fill; -webkit-text-stroke: 11px #FF6D00;
    font-size: 45px; line-height: 1.15; flex: 1;
}
.stroke-label {
    color: #FFFFFF; font-family: 'Gotham Ultra', sans-serif;
    letter-spacing: 2px; line-height: 1.25; text-transform: uppercase;
    paint-order: stroke fill; -webkit-text-stroke: 10px #FF6D00;
}
.stroke-val {
    color: #FFFFFF; font-family: 'Gotham Bold', sans-serif;
    line-height: 1.25; paint-order: stroke fill; -webkit-text-stroke: 10px #FF6D00;
}
.detail-row {
    display: flex; align-items: baseline; gap: 16px;
}
.safe-zone {
    position: absolute; top: 1270px; left: 190px; width: 2100px;
    display: flex; flex-direction: column; gap: 16px;
}
.hero-icon { width: 480px; height: 480px; object-fit: contain; flex-shrink: 0; }
.top-row { display: flex; align-items: center; gap: 36px; width: 100%; }
.day-date-group { display: flex; flex-direction: column; gap: 8px; }

.venue-section {
    display: flex; flex-direction: column; gap: 10px; width: 100%;
}
.acts-block { display: flex; flex-direction: column; gap: 10px; width: 100%; }
.act-item { display: flex; flex-direction: column; gap: 3px; }
.act-header-row { display: flex; align-items: baseline; gap: 14px; }
.act-lead-row { display: flex; align-items: baseline; gap: 14px; margin-left: 70px; }
.act-lead-lbl { font-size: 36px; flex-shrink: 0; }
.act-lead-val { font-size: 40px; flex: 1; }

.bottom-block { display: flex; flex-direction: column; gap: 8px; width: 100%; }
.detail-label-col { width: 350px; flex-shrink: 0; font-size: 42px; }
.detail-val-col { flex: 1; font-size: 42px; line-height: 1.18; }

.section-divider {
    width: 100%; height: 3px; background: rgba(255, 109, 0, 0.4); margin: 3px 0;
}
</style></head><body>
<div class="safe-zone">
    <div class="top-row">
        <img class="hero-icon" src="/icons/DAY 3.png">
        <div class="day-date-group">
            <div class="stroke-day">DAY 3</div>
            <div class="stroke-date">NOVEMBER 27, 2026 | FRIDAY</div>
        </div>
    </div>

    <!-- VENUE 1 SECTION -->
    <div class="venue-section">
        <div class="acts-block">
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">1.</div>
                    <div class="stroke-act-desc act-desc">Inclusive Protection, Accessible Services, and Sign Language Orientation for Women with Disabilities and Senior Women</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">PDAO & OSCA</span>
                </div>
            </div>
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">2.</div>
                    <div class="stroke-act-desc act-desc">Namnama (PWD Film Viewing)</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">GAD Office</span>
                </div>
            </div>
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">3.</div>
                    <div class="stroke-act-desc act-desc">Project SUNSHINE Survivor – Centered Case Management and Referral Review</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">CSWDO</span>
                </div>
            </div>
        </div>
        <div class="bottom-block">
            <div class="detail-row">
                <div class="detail-label-col stroke-label">PARTNERS:</div>
                <div class="detail-val-col stroke-val">CSWDO, Health Office, PNP, PNP-WCPD, NGAs, CSOs, ISAC, Women with Disabilities Group</div>
            </div>
            <div class="detail-row">
                <div class="detail-label-col stroke-label">VENUE:</div>
                <div class="detail-val-col stroke-val">F. L. Dy Colliseum, District III, Cauayan City, Isabela</div>
            </div>
        </div>
    </div>

    <div class="section-divider"></div>

    <!-- VENUE 2 SECTION -->
    <div class="venue-section">
        <div class="acts-block">
            <div class="act-item">
                <div class="act-header-row">
                    <div class="stroke-num act-num">4.</div>
                    <div class="stroke-act-desc act-desc">KABATAAN PRO-TECT (Teen Empowerment and Care Team): Peer Helping Training on Safe Spaces, Mental Health, and ASRH</div>
                </div>
                <div class="act-lead-row">
                    <span class="stroke-label act-lead-lbl">LEAD OFFICE:</span>
                    <span class="stroke-val act-lead-val">City Population Office</span>
                </div>
            </div>
        </div>
        <div class="bottom-block">
            <div class="detail-row">
                <div class="detail-label-col stroke-label">PARTNERS:</div>
                <div class="detail-val-col stroke-val">City Health Office, Local Youth Development Office, Cauayan City Stand Alone Senior High School</div>
            </div>
            <div class="detail-row">
                <div class="detail-label-col stroke-label">VENUE:</div>
                <div class="detail-val-col stroke-val">Cauayan City Stand Alone Senior High School</div>
            </div>
        </div>
    </div>
</div>
</body></html>
"""

test_d3_path = os.path.join(BASE_DIR, "scratch", "test_split_d3.html")
with open(test_d3_path, "w", encoding="utf-8") as f:
    f.write(d3_html)

out_png = os.path.join(BASE_DIR, "scratch", "test_split_d3.png")
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=1",
    "--window-size=2480,3508",
    f"--screenshot={os.path.abspath(out_png)}",
    f"http://127.0.0.1:{PORT}/scratch/test_split_d3.html"
]
subprocess.run(cmd, check=True)

# Measure clearance
im = Image.open(out_png)
tmpl = Image.open(os.path.join(BASE_DIR, "FABMAT", "fabmat_template.png"))
arr = np.array(im)
tmpl_arr = np.array(tmpl)
diff = np.abs(arr[:,:,:3].astype(int) - tmpl_arr[:,:,:3].astype(int))
mask = np.max(diff, axis=2) > 30

ys, xs = np.where(mask[2000:3200, 190:2290])
if len(ys) > 0:
    max_y = 2000 + np.max(ys)
    print(f"Day 3 Max text y: {max_y} px (Hazard line is 2950 px, clearance = +{2950 - max_y} px)")
else:
    print("No text detected in range")

server.shutdown()

