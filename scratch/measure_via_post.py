import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import json
import urllib.parse

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
PORT = 9197
received_data = {}

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode('utf-8')
        global received_data
        received_data = json.loads(body)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

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
            results.push({{ name: 'safe-zone', top: safeZone.offsetTop, left: safeZone.offsetLeft, width: safeZone.offsetWidth, height: safeZone.offsetHeight }});
            
            const icon = doc.querySelector('.hero-icon');
            if (icon) results.push({{ name: 'hero-icon', top: icon.offsetTop, left: icon.offsetLeft, width: icon.offsetWidth, height: icon.offsetHeight }});
            
            const dayDate = doc.querySelector('.day-date-group');
            if (dayDate) results.push({{ name: 'day-date-group', top: dayDate.offsetTop, left: dayDate.offsetLeft, width: dayDate.offsetWidth, height: dayDate.offsetHeight }});
            
            const mid = doc.querySelector('.middle-block');
            if (mid) results.push({{ name: 'middle-block', top: mid.offsetTop, left: mid.offsetLeft, width: mid.offsetWidth, height: mid.offsetHeight }});
            
            const acts = doc.querySelectorAll('.act-item');
            acts.forEach((a, i) => results.push({{ name: 'act-item-' + (i+1), top: a.offsetTop, left: a.offsetLeft, width: a.offsetWidth, height: a.offsetHeight }}));
            
            const btm = doc.querySelector('.bottom-block');
            if (btm) results.push({{ name: 'bottom-block', top: btm.offsetTop, left: btm.offsetLeft, width: btm.offsetWidth, height: btm.offsetHeight }});
            
            return results;
        }}
        
        fetch('http://127.0.0.1:{PORT}/', {{
            method: 'POST',
            body: JSON.stringify({{
                f0: getBounds('f0'),
                f1: getBounds('f1')
            }})
        }});
    }}, 2000);
}});
</script>
</body>
</html>
"""

test_path = os.path.join(BASE_DIR, "scratch", "post_bounds.html")
with open(test_path, "w", encoding="utf-8") as f:
    f.write(test_html)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--window-size=2500,3600",
    "--virtual-time-budget=5000",
    f"http://127.0.0.1:{PORT}/scratch/post_bounds.html"
]

print("Starting Chrome...")
subprocess.run(cmd, timeout=15)
print("Received data:")
print(json.dumps(received_data, indent=2))
server.shutdown()

