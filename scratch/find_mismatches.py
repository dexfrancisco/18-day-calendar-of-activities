import json
import re

with open('scratch/audit_report.py', 'r', encoding='utf-8') as f:
    pass

import os
with open('scratch/audit_summary.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

# Let's inspect sections
sections = md_content.split('---')

for sec in sections:
    sec = sec.strip()
    if not sec:
        continue
    # get Day header
    hdr_m = re.search(r'## (DAY \d+|PRE-CAMPAIGN)', sec)
    if not hdr_m:
        continue
    day_name = hdr_m.group(1)
    
    # get venue
    f_ven = re.search(r'- \*\*FABMAT:\*\* `([^`]*)`', sec.split('- **Venue:**')[1]) if '- **Venue:**' in sec else None
    c_ven = re.search(r'- \*\*Calendar:\*\* `([^`]*)`', sec.split('- **Venue:**')[1]) if '- **Venue:**' in sec else None
    
    # get partners
    part_sec = sec.split('- **Partners:**')[1].split('- **Venue:**')[0] if '- **Partners:**' in sec and '- **Venue:**' in sec else ""
    f_part = re.search(r'- \*\*FABMAT:\*\* `([^`]*)`', part_sec)
    c_part = re.search(r'- \*\*Calendar:\*\* `([^`]*)`', part_sec)
    
    fv = f_ven.group(1).strip() if f_ven else ""
    cv = c_ven.group(1).strip() if c_ven else ""
    
    fp = f_part.group(1).strip() if f_part else ""
    cp = c_part.group(1).strip() if c_part else ""
    
    print(f"[{day_name}]")
    if fv != cv:
        print(f"  [VENUE DIFFERENCE]")
        print(f"    FABMAT:   '{fv}'")
        print(f"    Calendar: '{cv}'")
    else:
        print(f"  ✓ Venue exact match: '{fv}'")
        
    if fp != cp:
        print(f"  [PARTNERS DIFFERENCE]")
        print(f"    FABMAT:   '{fp}'")
        print(f"    Calendar: '{cp}'")
    else:
        print(f"  ✓ Partners exact match: '{fp}'")

