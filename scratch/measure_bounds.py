import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import json

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
PORT = 9196

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

# Let's inspect 00-pre-campaign.html and 01-day-01.html
test_html = f"""<!DOCTYPE html>
<html>
<body>
<iframe id="f0" src="http://127.0.0.1:{PORT}/scratch/final_html/00-pre-campaign.html" width="2480" height="3508"></iframe>
<iframe id="f1" src="http://127.0.0.1:{PORT}/scratch/final_html/01-day-01.html" width="2480" height="3508"></iframe>
<script>
window.addEventListener('load', () => {{
    setTimeout(() => {{
        function getBounds(iframeId) {{
            const win = document.getElementById(iframeId).contentWindow;
            const doc = win.document;
            const results = [];
            const safeZone = doc.querySelector('.safe-zone');
            results.push({{ name: 'safe-zone', rect: safeZone.getBoundingClientRect() }});
            
            const icon = doc.querySelector('.hero-icon');
            if (icon) results.push({{ name: 'hero-icon', rect: icon.getBoundingClientRect() }});
            
            const dayDate = doc.querySelector('.day-date-group');
            if (dayDate) results.push({{ name: 'day-date-group', rect: dayDate.getBoundingClientRect() }});
            
            const mid = doc.querySelector('.middle-block');
            if (mid) results.push({{ name: 'middle-block', rect: mid.getBoundingClientRect() }});
            
            const acts = doc.querySelectorAll('.act-item');
            acts.forEach((a, i) => results.push({{ name: 'act-item-' + (i+1), rect: a.getBoundingClientRect() }}));
            
            const btm = doc.querySelector('.bottom-block');
            if (btm) results.push({{ name: 'bottom-block', rect: btm.getBoundingClientRect() }});
            
            return results;
        }}
        
        console.log('F0_BOUNDS:' + JSON.stringify(getBounds('f0')));
        console.log('F1_BOUNDS:' + JSON.stringify(getBounds('f1')));
    }}, 1500);
}});
</script>
</body>
</html>
"""

test_path = os.path.join(BASE_DIR, "scratch", "measure_bounds.html")
with open(test_path, "w", encoding="utf-8") as f:
    f.write(test_html)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--window-size=2500,3600",
    "--virtual-time-budget=4000",
    f"http://127.0.0.1:{PORT}/scratch/measure_bounds.html"
]

print("Measuring bounds in Chrome...")
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("Stderr output:")
for line in res.stderr.split('\n'):
    if 'F0_BOUNDS' in line or 'F1_BOUNDS' in line or 'console-message' in line:
        print(line)

