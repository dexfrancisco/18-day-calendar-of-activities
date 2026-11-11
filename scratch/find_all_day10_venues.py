import glob
import re

for fp in glob.glob('**/*calendar*.html', recursive=True):
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # search for DAY 10 block
    m = re.search(r'DAY 10.*?(?=DAY 11|\Z)', c, re.DOTALL)
    if m:
        venue_m = re.search(r'<strong>Venue:</strong>\s*([^<]+)', m.group(0))
        if venue_m:
            print(f"{fp} -> {venue_m.group(1).strip()}")
        else:
            print(f"{fp} -> Venue not found in DAY 10 block")

