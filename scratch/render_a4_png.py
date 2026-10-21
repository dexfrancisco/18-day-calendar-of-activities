import subprocess
import time
import os
import http.server
import socketserver
import threading

PORT = 8992
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

pages = [
    ("18-day-campaign-calendar-a4-page1.html", "18-Day_Campaign_Calendar_A4_Page1.png"),
    ("18-day-campaign-calendar-a4-page2.html", "18-Day_Campaign_Calendar_A4_Page2.png")
]

for html_file, out_name in pages:
    out_png = os.path.join(DIRECTORY, out_name)
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--window-size=2480,3508",
        "--hide-scrollbars",
        "--virtual-time-budget=5000",
        f"--screenshot={out_png}",
        f"http://localhost:{PORT}/{html_file}"
    ]
    print(f"Rendering {html_file} -> {out_name}...")
    subprocess.run(cmd, check=True)
    print(f"Screenshot saved to {out_png}")

print("All A4 pages rendered successfully!")
