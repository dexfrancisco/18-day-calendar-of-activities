import os
import subprocess
import time
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
PORT = 9194

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)
    def log_message(self, format, *args):
        pass

server = HTTPServer(("127.0.0.1", PORT), Handler)
t = threading.Thread(target=server.serve_forever, daemon=True)
t.start()

# Let's run a test using python urllib / or Chrome debugging protocol or write a verification script
print("Server started on port", PORT)

# Let's verify by testing with a script that runs inside chrome
test_js = """
console.log('--- TEST BEGIN ---');
console.log('Total layers:', layers.length);
layers.forEach(l => console.log('Layer:', l.id, l.name, 'pos:', l.x, l.y, 'type:', l.type));

// Test selecting hero icon
selectLayer('icon_00');
console.log('Selected after click:', selectedLayerId);
const iconLayer = getSelectedLayer();
console.log('Icon layer pos before nudge:', iconLayer.x, iconLayer.y);

// Nudge icon by +50px
iconLayer.x += 50;
iconLayer.y += 30;
updateTransformBox();
console.log('Icon layer pos after nudge:', iconLayer.x, iconLayer.y);

// Check that badge layer pos is UNCHANGED
const badgeLayer = layers.find(l => l.id === 'badge_00');
console.log('Badge layer pos (should be unchanged):', badgeLayer.x, badgeLayer.y);

// Test selecting Day 1
loadDay('01');
console.log('Day 1 layers count:', layers.length);
layers.forEach(l => console.log('Day 1 Layer:', l.id, l.name, 'pos:', l.x, l.y));

console.log('--- TEST END ---');
"""

# Let's write an html test runner that loads editor.html in an iframe or executes test_js
runner_html = f"""<!DOCTYPE html>
<html>
<body>
<iframe id="editorFrame" src="http://127.0.0.1:{PORT}/editor.html" width="1920" height="1080"></iframe>
<script>
window.addEventListener('load', () => {{
    setTimeout(() => {{
        const win = document.getElementById('editorFrame').contentWindow;
        {test_js}
        document.title = 'TEST_PASSED';
    }}, 2000);
}});
</script>
</body>
</html>
"""

runner_path = os.path.join(BASE_DIR, "scratch", "test_runner.html")
with open(runner_path, "w", encoding="utf-8") as f:
    f.write(runner_html)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--dump-dom",
    f"http://127.0.0.1:{PORT}/scratch/test_runner.html"
]

print("Running test in headless Chrome...")
res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=15)
print("Return code:", res.returncode)
print("Output snippet:", res.stdout[:500])

