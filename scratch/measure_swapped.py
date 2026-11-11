import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9230

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

test_js = f"""<!DOCTYPE html>
<html><body>
<iframe id="f9" src="http://127.0.0.1:{PORT}/scratch/final_html/09-day-09.html" style="width:2480px;height:3508px;"></iframe>
<iframe id="f10" src="http://127.0.0.1:{PORT}/scratch/final_html/10-day-10.html" style="width:2480px;height:3508px;"></iframe>
<script>
window.addEventListener('load', () => {{
    setTimeout(() => {{
        function getBottom(id) {{
            const win = document.getElementById(id).contentWindow;
            const btm = win.document.querySelector('.bottom-block');
            const r = btm.getBoundingClientRect();
            return Math.round(r.bottom);
        }}
        const b9 = getBottom('f9');
        const b10 = getBottom('f10');
        const res = document.createElement('div');
        res.id = 'results';
        res.setAttribute('data-b9', b9);
        res.setAttribute('data-b10', b10);
        document.body.appendChild(res);
    }}, 2000);
}});
</script>
</body></html>"""

with open(os.path.join(BASE_DIR, "scratch", "measure_swapped_bounds.html"), "w", encoding="utf-8") as f:
    f.write(test_js)

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--window-size=2500,3600",
    "--virtual-time-budget=6000",
    "--dump-dom",
    f"http://127.0.0.1:{PORT}/scratch/measure_swapped_bounds.html"
]

res = subprocess.run(cmd, capture_output=True, text=True)
match = re.search(r'<div id="results"([^>]+)>', res.stdout)
if match:
    print('Bounds results:', match.group(1))
else:
    print('No results tag found. Dump len:', len(res.stdout))

server.shutdown()

