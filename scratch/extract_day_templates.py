import os
import glob
import re
import json

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"
html_files = sorted(glob.glob(os.path.join(BASE_DIR, "scratch", "final_html", "*.html")))

day_templates = {}

for h_path in html_files:
    fname = os.path.basename(h_path)
    day_id = fname.split('-')[0] # '00', '01', etc.
    with open(h_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract <style>...</style>
    style_m = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
    style_content = style_m.group(1) if style_m else ""

    # Extract <body>...</body> content
    body_m = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_m.group(1) if body_m else ""

    day_templates[day_id] = {
        "filename": fname.replace('.html', '.png'),
        "style": style_content,
        "body": body_content
    }

print(f"Extracted {len(day_templates)} day templates from scratch/final_html.")
for k, v in list(day_templates.items())[:3]:
    print(f"Day {k}: style len={len(v['style'])}, body len={len(v['body'])}")

