import os
import subprocess
import shutil
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9194

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()
print(f"HTTP Server running on port {PORT}")

# 1. Render A3 Landscape (4961 x 3508 px)
a3_out = os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_A3.png")
a3_cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=1",
    "--window-size=4961,3508",
    f"--screenshot={os.path.abspath(a3_out)}",
    f"http://127.0.0.1:{PORT}/18-day-campaign-calendar-a3.html"
]
print("Rendering A3 Calendar...")
subprocess.run(a3_cmd, check=True)
print(f"✓ Rendered A3: {a3_out}")
shutil.copy2(a3_out, os.path.join(BASE_DIR, "Final Copy", "18-Day_Campaign_Calendar_A3.png"))
print("✓ Copied A3 to Final Copy")

# 2. Render A4 Page 1 (2480 x 3508 px)
p1_out = os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_A4_Page1.png")
p1_cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=1",
    "--window-size=2480,3508",
    f"--screenshot={os.path.abspath(p1_out)}",
    f"http://127.0.0.1:{PORT}/18-day-campaign-calendar-a4-page1.html"
]
print("Rendering A4 Page 1...")
subprocess.run(p1_cmd, check=True)
print(f"✓ Rendered A4 Page 1: {p1_out}")

# 3. Render A4 Page 2 (2480 x 3508 px)
p2_out = os.path.join(BASE_DIR, "18-Day_Campaign_Calendar_A4_Page2.png")
p2_cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=1",
    "--window-size=2480,3508",
    f"--screenshot={os.path.abspath(p2_out)}",
    f"http://127.0.0.1:{PORT}/18-day-campaign-calendar-a4-page2.html"
]
print("Rendering A4 Page 2...")
subprocess.run(p2_cmd, check=True)
print(f"✓ Rendered A4 Page 2: {p2_out}")

print("\nAll calendar renders completed successfully!")

