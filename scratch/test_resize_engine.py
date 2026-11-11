import os
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PORT = 9205

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
        console.log('1. Selecting layer_icon...');
        win.selectLayer('layer_icon');

        setTimeout(() => {{
            console.log('2. Testing handle drag resize on layer_icon...');
            const handleSe = win.document.querySelector('.transform-handle.se');
            const rect = handleSe.getBoundingClientRect();
            
            // Dispatch mousedown on SE handle
            handleSe.dispatchEvent(new MouseEvent('mousedown', {{
                clientX: rect.left + rect.width / 2,
                clientY: rect.top + rect.height / 2,
                bubbles: true
            }}));

            // Drag by +80px horizontally and vertically on window
            win.dispatchEvent(new MouseEvent('mousemove', {{
                clientX: rect.left + rect.width / 2 + 80,
                clientY: rect.top + rect.height / 2 + 80,
                bubbles: true
            }}));

            // Mouseup to finalize
            win.dispatchEvent(new MouseEvent('mouseup', {{
                bubbles: true
            }}));

            setTimeout(() => {{
                console.log('3. Selecting layer_title...');
                win.selectLayer('layer_title');

                setTimeout(() => {{
                    console.log('4. Testing handle drag on layer_title...');
                    const handleSeTitle = win.document.querySelector('.transform-handle.se');
                    const rTitle = handleSeTitle.getBoundingClientRect();

                    handleSeTitle.dispatchEvent(new MouseEvent('mousedown', {{
                        clientX: rTitle.left + rTitle.width / 2,
                        clientY: rTitle.top + rTitle.height / 2,
                        bubbles: true
                    }}));

                    win.dispatchEvent(new MouseEvent('mousemove', {{
                        clientX: rTitle.left + rTitle.width / 2 + 50,
                        clientY: rTitle.top + rTitle.height / 2 + 50,
                        bubbles: true
                    }}));

                    win.dispatchEvent(new MouseEvent('mouseup', {{
                        bubbles: true
                    }}));

                    document.body.setAttribute('data-ready', 'true');
                }}, 500);
            }}, 600);
        }}, 600);
    }}, 1500);
}});
</script>
</body>
</html>
"""

test_page_path = os.path.join(BASE_DIR, "scratch", "auto_resize_test.html")
with open(test_page_path, "w", encoding="utf-8") as f:
    f.write(test_page_html)

out_png = os.path.join(BASE_DIR, "scratch", "studio_resized_tested.png")
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1920,1080",
    "--virtual-time-budget=8000",
    f"--screenshot={os.path.abspath(out_png)}",
    f"http://127.0.0.1:{PORT}/scratch/auto_resize_test.html"
]

print("Rendering screenshot of studio resize test...")
subprocess.run(cmd, check=True)
print(f"✓ Screenshot saved to {out_png}")
server.shutdown()

