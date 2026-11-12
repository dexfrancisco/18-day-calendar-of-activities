import os
import glob
import re

# Load Calendar HTML
with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    cal_html = f.read()

# Load Calendar Text File
with open('18-Day_Campaign_Calendar_Extracted_Text.txt', 'r', encoding='utf-8') as f:
    cal_txt = f.read()

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

fab_files = sorted(glob.glob('scratch/final_html/*.html'))

print(f"Total FABMAT files to verify: {len(fab_files)}")

# Build structured data for each day
days_audit = []

for idx, fpath in enumerate(fab_files):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract clean text from HTML
    # Day / Date
    day_m = re.search(r'class="[^"]*stroke-day[^"]*">(.*?)</div>', html, re.DOTALL)
    date_m = re.search(r'class="[^"]*stroke-date[^"]*">(.*?)</div>', html, re.DOTALL)
    title_m = re.search(r'class="[^"]*stroke-title[^"]*">(.*?)</div>', html, re.DOTALL)
    sub_m = re.search(r'class="[^"]*stroke-subtitle[^"]*">(.*?)</div>', html, re.DOTALL)
    
    # Detail values
    partners_m = re.search(r'class="[^"]*detail-label-col[^"]*">PARTNERS:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', html, re.DOTALL)
    venue_m = re.search(r'class="[^"]*detail-label-col[^"]*">VENUE:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', html, re.DOTALL)
    lead_m = re.search(r'class="[^"]*detail-label-col[^"]*">LEAD OFFICE:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', html, re.DOTALL)
    
    # Activity items
    act_items = re.findall(r'<div class="act-item">(.*?)</div>\s*(?=<div class="act-item"|<div class="bottom-block"|</div>\s*</div>)', html, re.DOTALL)
    acts = []
    for ai in act_items:
        num = re.search(r'class="[^"]*act-num[^"]*">(.*?)</div>', ai, re.DOTALL)
        d = re.search(r'class="[^"]*act-desc[^"]*">(.*?)</div>', ai, re.DOTALL)
        l = re.search(r'class="[^"]*act-lead-val[^"]*">(.*?)</span>', ai, re.DOTALL)
        acts.append({
            "num": clean(num.group(1)) if num else "",
            "desc": clean(d.group(1)) if d else "",
            "lead": clean(l.group(1)) if l else ""
        })
        
    # Hybrid tracks
    hybrid_m = re.findall(r'<div class="track-block">(.*?)</div>\s*(?=<div class="track-block"|<div class="bottom-block"|</div>\s*</div>)', html, re.DOTALL)
    hybrid_tracks = []
    for ht in hybrid_m:
        tag_m = re.search(r'class="[^"]*track-tag[^"]*">(.*?)</div>', ht, re.DOTALL)
        desc_m = re.search(r'class="[^"]*stroke-act-desc[^"]*">(.*?)</div>', ht, re.DOTALL)
        lead_val_m = re.search(r'class="[^"]*stroke-val[^"]*">(.*?)</span>', ht, re.DOTALL)
        # also sub items if any
        sub_items = re.findall(r'<div style="display:flex; align-items:baseline; gap:16px;">(.*?)</div>', ht, re.DOTALL)
        sub_parsed = []
        for si in sub_items:
            sn = re.search(r'class="[^"]*stroke-num[^"]*">(.*?)</div>', si, re.DOTALL)
            sd = re.search(r'class="[^"]*stroke-act-desc[^"]*">(.*?)</div>', si, re.DOTALL)
            if sn and sd:
                sub_parsed.append(f"{clean(sn.group(1))} {clean(sd.group(1))}")
        
        hybrid_tracks.append({
            "tag": clean(tag_m.group(1)) if tag_m else "",
            "desc": clean(desc_m.group(1)) if desc_m else "",
            "lead": clean(lead_val_m.group(1)) if lead_val_m else "",
            "subs": sub_parsed
        })
        
    days_audit.append({
        "index": idx,
        "fname": fname,
        "day": clean(day_m.group(1)) if day_m else ("PRE-CAMPAIGN" if idx == 0 else ""),
        "date": clean(date_m.group(1)) if date_m else "",
        "title": clean(title_m.group(1)) if title_m else "",
        "subtitle": clean(sub_m.group(1)) if sub_m else "",
        "lead": clean(lead_m.group(1)) if lead_m else "",
        "partners": clean(partners_m.group(1)) if partners_m else "",
        "venue": clean(venue_m.group(1)) if venue_m else "",
        "acts": acts,
        "hybrid": hybrid_tracks
    })

# Write a comprehensive verification log
with open('scratch/fabmat_full_verification_log.txt', 'w', encoding='utf-8') as out:
    for d in days_audit:
        out.write(f"\n{'='*70}\n")
        out.write(f"FILE: {d['fname']} ({d['day']})\n")
        out.write(f"{'='*70}\n")
        out.write(f"DATE:     {d['date']}\n")
        if d['title']:
            out.write(f"TITLE:    {d['title']}\n")
        if d['subtitle']:
            out.write(f"SUBTITLE: {d['subtitle']}\n")
        if d['lead']:
            out.write(f"LEAD:     {d['lead']}\n")
        if d['acts']:
            out.write(f"ACTIVITIES ({len(d['acts'])}):\n")
            for a in d['acts']:
                out.write(f"  - [{a['num']}] {a['desc']}\n")
                out.write(f"      LEAD: {a['lead']}\n")
        if d['hybrid']:
            out.write(f"HYBRID TRACKS:\n")
            for h in d['hybrid']:
                out.write(f"  - [{h['tag']}]\n")
                if h['desc']:
                    out.write(f"      Desc: {h['desc']}\n")
                if h['lead']:
                    out.write(f"      Lead: {h['lead']}\n")
                if h['subs']:
                    for sub in h['subs']:
                        out.write(f"      Sub:  {sub}\n")
        out.write(f"PARTNERS: {d['partners']}\n")
        out.write(f"VENUE:    {d['venue']}\n")

print("Full verification log written to scratch/fabmat_full_verification_log.txt")

