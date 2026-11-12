import glob
import re
import os

files = sorted(glob.glob('scratch/final_html/*.html'))

for fpath in files:
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # count PARTNERS
    partners_count = len(re.findall(r'>PARTNERS:?<', html))
    venue_count = len(re.findall(r'>VENUE:?<', html))
    lead_count = len(re.findall(r'>LEAD OFFICE:?<', html))
    
    # check bottom block
    bb_matches = re.findall(r'class="bottom-block"', html)
    
    print(f"{fname:20s}: PARTNERS={partners_count}, VENUE={venue_count}, LEAD={lead_count}, bottom_blocks={len(bb_matches)}")

