import glob
import re

for hfile in sorted(glob.glob('scratch/final_html/*.html')):
    with open(hfile, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check for tags or headers
    tags = re.findall(r'<div class="[^"]*tag[^"]*">([^<]+)</div>', html, re.IGNORECASE)
    has_online = 'online' in html.lower()
    has_advocacy = 'advocacy' in html.lower()
    
    print(f"\n{hfile}:")
    print(f"  Tags found: {tags}")
    if has_online or has_advocacy:
        print(f"  Mentions online: {has_online}, advocacy: {has_advocacy}")

