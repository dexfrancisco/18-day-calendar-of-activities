import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9198

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

test_page_html = f"""<!DOCTYPE html>
<html>
<head>
<style>
body, html {{ margin: 0; padding: 0; width: 1920px; height: 1080px; overflow: hidden; }}
iframe {{ width: 1920px; height: 1080px; border: none; }}
</style>
</head>
<body>
<iframe id="app" src="http://127.0.0.1:{PORT}/editor.html"></iframe>
<script>
window.addEventListener('load', () => {{
    setTimeout(() => {{
        const win = document.getElementById('app').contentWindow;
        console.log('Selecting layer_icon...');
        win.selectLayer('layer_icon');
        // Nudge icon down by 50px
        win.nudgeSelected(0, 50);
        
        setTimeout(() => {{
            console.log('Selecting layer_title...');
            win.selectLayer('layer_title');
            win.nudgeSelected(0, 30);
            document.body.setAttribute('data-ready', 'true');
        }}, 600);
    }}, 1200);
}});
</script>
</body>
</html>
"""

test_page_path = os.path.join(BASE_DIR, "scratch", "auto_layer_test.html")
with open(test_page_path, "w", encoding="utf-8") as f:
    f.write(test_page_html)

out_png = os.path.join(BASE_DIR, "scratch", "perfect_studio_tested.png")
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1920,1080",
    "--virtual-time-budget=6000",
    f"--screenshot={os.path.abspath(out_png)}",
    f"http://127.0.0.1:{PORT}/scratch/auto_layer_test.html"
]

print("Rendering screenshot of perfect studio test...")
subprocess.run(cmd, check=True)
print(f"✓ Screenshot saved to {out_png}")
server.shutdown()

