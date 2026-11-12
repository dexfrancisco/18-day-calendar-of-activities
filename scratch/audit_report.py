import glob
import re
import os

with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    cal_html = f.read()

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

report = []

for idx, fpath in enumerate(fab_files):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        f_html = f.read()
    
    # Strip styles & scripts
    f_body = re.sub(r'<style.*?</style>', '', f_html, flags=re.DOTALL)
    f_body = re.sub(r'<script.*?</script>', '', f_body, flags=re.DOTALL)
    
    # Calendar article
    day_label = f"DAY {idx}" if idx > 0 else "PRE-CAMPAIGN"
    if idx == 0:
        c_m = re.search(r'<article class="day-card special-title-card">(.*?)</article>', cal_html, re.DOTALL)
    else:
        c_m = re.search(r'<article class="day-card[^"]*">\s*<div class="card-top-bar">\s*<span class="day-pill">' + day_label + r'</span>(.*?)</article>', cal_html, re.DOTALL)
        
    c_raw = c_m.group(1) if c_m else ""
    c_clean = clean(c_raw)
    f_clean = clean(f_body)
    
    # FABMAT fields
    day_m = re.search(r'class="[^"]*stroke-day[^"]*">(.*?)</div>', f_body, re.DOTALL)
    date_m = re.search(r'class="[^"]*stroke-date[^"]*">(.*?)</div>', f_body, re.DOTALL)
    title_m = re.search(r'class="[^"]*stroke-title[^"]*">(.*?)</div>', f_body, re.DOTALL)
    sub_m = re.search(r'class="[^"]*stroke-subtitle[^"]*">(.*?)</div>', f_body, re.DOTALL)
    
    # Details in FABMAT
    lead_m = re.search(r'class="[^"]*detail-label-col[^"]*">LEAD OFFICE:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', f_body, re.DOTALL)
    part_m = re.search(r'class="[^"]*detail-label-col[^"]*">PARTNERS:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', f_body, re.DOTALL)
    venue_m = re.search(r'class="[^"]*detail-label-col[^"]*">VENUE:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', f_body, re.DOTALL)
    
    # Activities in FABMAT
    f_acts = re.findall(r'<div class="act-item">(.*?)</div>\s*(?=<div class="act-item"|<div class="bottom-block"|</div>\s*</div>)', f_body, re.DOTALL)
    
    # Details in Calendar
    c_venues = re.findall(r'class="[^"]*venue-box[^"]*">(.*?)</div>', c_raw, re.DOTALL)
    if not c_venues and idx == 0:
        c_venues = re.findall(r'class="special-title-venue">(.*?)</div>', c_raw, re.DOTALL)
    c_venue_txt = " | ".join([clean(v).replace('Venue:', '').replace('VENUE:', '').strip() for v in c_venues])
    
    c_parts = re.findall(r'class="[^"]*partner-box[^"]*">(.*?)</div>', c_raw, re.DOTALL)
    if not c_parts and idx == 0:
        c_parts = re.findall(r'class="special-partner-row">(.*?)</div>', c_raw, re.DOTALL)
    c_part_txt = " | ".join([clean(p).replace('Partners:', '').strip() for p in c_parts])
    
    report.append({
        "day_label": day_label,
        "fname": fname,
        "fab_day": clean(day_m.group(1)) if day_m else "",
        "fab_date": clean(date_m.group(1)) if date_m else "",
        "fab_title": clean(title_m.group(1)) if title_m else "",
        "fab_sub": clean(sub_m.group(1)) if sub_m else "",
        "fab_lead": clean(lead_m.group(1)) if lead_m else "",
        "fab_part": clean(part_m.group(1)) if part_m else "",
        "fab_venue": clean(venue_m.group(1)) if venue_m else "",
        "fab_acts_count": len(f_acts),
        "cal_part": c_part_txt,
        "cal_venue": c_venue_txt,
        "cal_clean": c_clean,
        "fab_clean": f_clean
    })

# Write markdown audit artifact
with open('scratch/audit_summary.md', 'w', encoding='utf-8') as f:
    f.write("# Comprehensive Audit: 18-Day Campaign FABMAT vs Master Calendar\n\n")
    for r in report:
        f.write(f"## {r['day_label']} (`{r['fname']}`)\n")
        f.write(f"- **Day / Date (FABMAT):** `{r['fab_day']}` | `{r['fab_date']}`\n")
        if r['fab_title']:
            f.write(f"- **Title / Subtitle:** {r['fab_title']} — *{r['fab_sub']}*\n")
        if r['fab_lead']:
            f.write(f"- **Lead Office (FABMAT):** {r['fab_lead']}\n")
        f.write(f"- **Partners:**\n")
        f.write(f"  - **FABMAT:** `{r['fab_part']}`\n")
        f.write(f"  - **Calendar:** `{r['cal_part']}`\n")
        f.write(f"- **Venue:**\n")
        f.write(f"  - **FABMAT:** `{r['fab_venue']}`\n")
        f.write(f"  - **Calendar:** `{r['cal_venue']}`\n")
        f.write(f"- **Text Content Alignment:**\n")
        f.write(f"  - **FABMAT Full Text:** {r['fab_clean']}\n")
        f.write(f"  - **Calendar Full Text:** {r['cal_clean']}\n")
        f.write("\n---\n\n")

print("Audit summary written to scratch/audit_summary.md")

