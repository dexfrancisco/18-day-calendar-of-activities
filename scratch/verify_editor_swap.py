import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9235

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
        
        // 1. Switch to Day 9
        win.selectDay('09');
        setTimeout(() => {{
            const d9Text = win.document.getElementById('posterCanvasInner').innerText;
            const hasForum = d9Text.includes('End VAWC Action Forum');
            const hasIcon = d9Text.includes('ICON');
            
            // 2. Switch to Day 10
            win.selectDay('10');
            setTimeout(() => {{
                const d10Text = win.document.getElementById('posterCanvasInner').innerText;
                const hasMove = d10Text.includes('Men as Allies');
                const hasSafeline = d10Text.includes('Safeline 922');
                const hasFLDy = d10Text.includes('F. L. Dy Colliseum');
                
                const res = document.createElement('div');
                res.id = 'results';
                res.setAttribute('data-d9-forum', hasForum);
                res.setAttribute('data-d9-icon', hasIcon);
                res.setAttribute('data-d10-move', hasMove);
                res.setAttribute('data-d10-safeline', hasSafeline);
                res.setAttribute('data-d10-fldy', hasFLDy);
                document.body.appendChild(res);
            }}, 500);
        }}, 500);
    }}, 1500);
}});
</script>
</body></html>"""

with open(os.path.join(BASE_DIR, "scratch", "verify_editor_swap.html"), "w", encoding="utf-8") as f:
    f.write(test_js)

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--virtual-time-budget=6000",
    "--dump-dom",
    f"http://127.0.0.1:{PORT}/scratch/verify_editor_swap.html"
]

res = subprocess.run(cmd, capture_output=True, text=True)
match = re.search(r'<div id="results"([^>]+)>', res.stdout)
if match:
    print('Editor Verification Results:', match.group(1))
else:
    print('No results tag found. Dump len:', len(res.stdout))

server.shutdown()

