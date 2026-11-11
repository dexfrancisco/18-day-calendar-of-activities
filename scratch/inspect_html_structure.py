import os
import glob
import re

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
html_files = sorted(glob.glob(os.path.join(BASE_DIR, "scratch", "final_html", "*.html")))

for h in html_files:
    fname = os.path.basename(h)
    with open(h, "r", encoding="utf-8") as f:
        content = f.read()
    sz_idx = content.find('<div class="safe-zone">')
    if sz_idx != -1:
        body_part = content[sz_idx:content.find('</body>')]
        divs = re.findall(r'<div class="([a-zA-Z0-9_-]+)"', body_part)
        print(f"{fname:22s} -> {divs[:6]}")
