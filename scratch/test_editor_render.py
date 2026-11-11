import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9193

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

out_png = os.path.join(BASE_DIR, "scratch", "editor_preview.png")
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1920,1080",
    f"--screenshot={os.path.abspath(out_png)}",
    f"http://127.0.0.1:{PORT}/editor.html"
]

print("Rendering editor UI preview screenshot...")
subprocess.run(cmd, check=True)
print(f"✓ Screenshot saved to {out_png}")

