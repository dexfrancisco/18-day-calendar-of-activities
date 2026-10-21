import subprocess
import time
import os
import http.server
import socketserver
import threading

PORT = 8991
DIRECTORY = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(1)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
out_png = os.path.join(DIRECTORY, "18-Day_Campaign_Calendar_A3.png")

cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--window-size=4961,3508",
    "--hide-scrollbars",
    "--virtual-time-budget=5000",
    f"--screenshot={out_png}",
    f"http://localhost:{PORT}/18-day-campaign-calendar-a3.html"
]

print("Rendering screenshot...")
subprocess.run(cmd, check=True)
print(f"Screenshot saved to {out_png}")
