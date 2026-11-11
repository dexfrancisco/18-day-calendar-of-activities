import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9199

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--enable-logging=stderr",
    "--v=1",
    f"http://127.0.0.1:{PORT}/editor.html"
]

print("Running chrome to capture console errors...")
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=10)
print("Stderr output:")
for line in res.stderr.split('\n'):
    if 'CONSOLE' in line or 'error' in line.lower() or 'exception' in line.lower():
        print(line)
server.shutdown()

