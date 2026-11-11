import os
import glob
import re
import json

BASE_DIR = r"c:\Users\CODEX\Desktop\18 day calendar of activity\18 day calendar of activity"

# Load schedule data
with open(os.path.join(BASE_DIR, "scratch", "schedule_data.json"), "r", encoding="utf-8") as f:
    schedule_data = json.load(f)

# Load HTML templates from scratch/final_html
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
    # Remove body rules and make paths relative
    style_content = re.sub(r'body\s*\{[^}]*\}', '', style_content)
    style_content = style_content.replace("url('/", "url('").replace('url("/', 'url("')

    # Extract <body>...</body> content
    body_m = re.search(r'<body>(.*?)</body>', html, re.DOTALL)
    body_content = body_m.group(1) if body_m else ""
    # Make icon paths relative (remove leading slash)
    body_content = body_content.replace('src="/icons/', 'src="icons/').replace("src='/icons/", "src='icons/")

    day_templates[day_id] = {
        "filename": fname.replace('.html', '.png'),
        "style": style_content,
        "body": body_content
    }

# List available icons
available_icons = sorted([f for f in os.listdir(os.path.join(BASE_DIR, "icons")) if f.lower().endswith(".png")])

schedule_json_str = json.dumps(schedule_data, indent=2, ensure_ascii=False)
templates_json_str = json.dumps(day_templates, indent=2, ensure_ascii=False)
icons_json_str = json.dumps(available_icons, indent=2, ensure_ascii=False)

print("Template keys count:", len(day_templates))
print("Day 00 body snippet:", day_templates["00"]["body"][:200])

