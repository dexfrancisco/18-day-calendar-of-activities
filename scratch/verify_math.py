import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9222

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
<iframe id="app" src="http://127.0.0.1:{PORT}/editor.html" style="width:1920px;height:1080px;border:none;"></iframe>
<script>
window.addEventListener('load', () => {{
    setTimeout(() => {{
        const win = document.getElementById('app').contentWindow;
        win.selectLayer('layer_icon');
        const iconEl = win.document.querySelector('.layer-target[data-layer-id="layer_icon"]');
        const w1 = iconEl.offsetWidth;

        const handleSe = win.document.querySelector('.transform-handle.se');
        const rect = handleSe.getBoundingClientRect();

        handleSe.dispatchEvent(new MouseEvent('mousedown', {{
            clientX: rect.left + rect.width / 2,
            clientY: rect.top + rect.height / 2,
            bubbles: true
        }}));

        win.dispatchEvent(new MouseEvent('mousemove', {{
            clientX: rect.left + rect.width / 2 + 100,
            clientY: rect.top + rect.height / 2 + 100,
            bubbles: true
        }}));

        win.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));

        const w2 = iconEl.offsetWidth;

        // Check text layer
        win.selectLayer('layer_title');
        const titleEl = win.document.querySelector('.stroke-title');
        const fs1 = parseFloat(win.getComputedStyle(titleEl).fontSize);

        const handleSe2 = win.document.querySelector('.transform-handle.se');
        const r2 = handleSe2.getBoundingClientRect();
        handleSe2.dispatchEvent(new MouseEvent('mousedown', {{
            clientX: r2.left + r2.width / 2,
            clientY: r2.top + r2.height / 2,
            bubbles: true
        }}));

        win.dispatchEvent(new MouseEvent('mousemove', {{
            clientX: r2.left + r2.width / 2 + 100,
            clientY: r2.top + r2.height / 2 + 100,
            bubbles: true
        }}));
        win.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));

        const fs2 = parseFloat(win.getComputedStyle(titleEl).fontSize);

        const res = document.createElement('div');
        res.id = 'results';
        res.setAttribute('data-w1', w1);
        res.setAttribute('data-w2', w2);
        res.setAttribute('data-fs1', fs1);
        res.setAttribute('data-fs2', fs2);
        document.body.appendChild(res);
    }}, 1500);
}});
</script>
</body></html>"""

with open(os.path.join(BASE_DIR, "scratch", "verify_math_page.html"), "w", encoding="utf-8") as f:
    f.write(test_js)

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--virtual-time-budget=6000",
    "--dump-dom",
    f"http://127.0.0.1:{PORT}/scratch/verify_math_page.html"
]

res = subprocess.run(cmd, capture_output=True, text=True)
match = re.search(r'<div id="results"([^>]+)>', res.stdout)
if match:
    print('SUCCESS! Results attribute:', match.group(1))
else:
    print('No results tag found. Dump len:', len(res.stdout))

server.shutdown()

