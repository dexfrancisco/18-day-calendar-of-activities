import os
import glob
import re

def clean(s):
    if not s:
        return ""
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'&amp;', '&', s)
    s = re.sub(r'&ndash;', '–', s)
    s = re.sub(r'&mdash;', '—', s)
    s = re.sub(r'&quot;', '"', s)
    s = re.sub(r'&#39;', "'", s)
    s = re.sub(r'&ldquo;', '“', s)
    s = re.sub(r'&rdquo;', '”', s)
    s = re.sub(r'&bull;', '•', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

# Let's inspect each FABMAT HTML directly
fabmats = {}
for fpath in sorted(glob.glob('scratch/final_html/*.html')):
    fname = os.path.basename(fpath).replace('.html', '')
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hero icon
    icon_m = re.search(r'src=["\']([^"\']+)["\']', content)
    icon = icon_m.group(1) if icon_m else ""
    
    # Day / Date
    day_m = re.search(r'class="stroke-day[^"]*">(.*?)</div>', content, re.DOTALL)
    date_m = re.search(r'class="stroke-date[^"]*">(.*?)</div>', content, re.DOTALL)
    
    # Single title/subtitle (like pre-campaign or single activity days)
    title_m = re.search(r'class="stroke-title[^"]*">(.*?)</div>', content, re.DOTALL)
    sub_m = re.search(r'class="stroke-subtitle[^"]*">(.*?)</div>', content, re.DOTALL)
    
    # Activities
    act_items = re.findall(r'<div class="act-item">(.*?)</div>\s*(?=<div class="act-item"|<div class="bottom-block"|</div>\s*</div>)', content, re.DOTALL)
    acts = []
    for ai in act_items:
        num_m = re.search(r'class="[^"]*act-num[^"]*">(.*?)</div>', ai, re.DOTALL)
        desc_m = re.search(r'class="[^"]*act-desc[^"]*">(.*?)</div>', ai, re.DOTALL)
        lead_lbl_m = re.search(r'class="[^"]*act-lead-lbl[^"]*">(.*?)</span>', ai, re.DOTALL)
        lead_val_m = re.search(r'class="[^"]*act-lead-val[^"]*">(.*?)</span>', ai, re.DOTALL)
        acts.append({
            "num": clean(num_m.group(1)) if num_m else "",
            "desc": clean(desc_m.group(1)) if desc_m else "",
            "lead_lbl": clean(lead_lbl_m.group(1)) if lead_lbl_m else "",
            "lead_val": clean(lead_val_m.group(1)) if lead_val_m else ""
        })
        
    # Bottom block details (Partners, Venue)
    detail_rows = re.findall(r'<div class="detail-row">(.*?)</div>\s*(?=<div class="detail-row"|</div>\s*</div>)', content, re.DOTALL)
    details = {}
    for dr in detail_rows:
        lbl_m = re.search(r'class="[^"]*detail-label-col[^"]*">(.*?)</div>', dr, re.DOTALL)
        val_m = re.search(r'class="[^"]*detail-val-col[^"]*">(.*?)</div>', dr, re.DOTALL)
        if lbl_m and val_m:
            lbl = clean(lbl_m.group(1)).rstrip(':').upper()
            val = clean(val_m.group(1))
            details[lbl] = val
            
    fabmats[fname] = {
        "icon": icon,
        "day": clean(day_m.group(1)) if day_m else "",
        "date": clean(date_m.group(1)) if date_m else "",
        "title": clean(title_m.group(1)) if title_m else "",
        "subtitle": clean(sub_m.group(1)) if sub_m else "",
        "acts": acts,
        "details": details
    }

print(f"Loaded {len(fabmats)} FABMAT HTML definitions.")

# Dump all FABMAT details cleanly to a report file
with open('scratch/fabmat_extracted_dump.json', 'w', encoding='utf-8') as f:
    import json
    json.dump(fabmats, f, indent=2, ensure_ascii=False)

print("Dumped to scratch/fabmat_extracted_dump.json")

