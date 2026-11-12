import json
import glob
import re
import os

with open('scratch/check_days.py', 'r', encoding='utf-8') as f:
    pass

# We have the calendar content extracted cleanly in check_days.py
# Let's write a comprehensive comparator
with open('18-day-campaign-calendar-a3.html', 'r', encoding='utf-8') as f:
    cal_html = f.read()

fabmat_files = sorted(glob.glob('scratch/final_html/*.html'))

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

print("="*90)
print("EXHAUSTIVE AUDIT: ALL 19 FABMAT HTML FILES VS CALENDAR")
print("="*90)

audit_results = []

for idx, fpath in enumerate(fabmat_files):
    fname = os.path.basename(fpath)
    with open(fpath, 'r', encoding='utf-8') as f:
        fab_raw = f.read()
    
    # Extract visible texts from FABMAT HTML
    # Remove head/style/script
    body_content = re.sub(r'<head>.*?</head>', '', fab_raw, flags=re.DOTALL)
    body_content = re.sub(r'<style.*?</style>', '', body_content, flags=re.DOTALL)
    
    # Extract key elements from FABMAT:
    day_m = re.search(r'class="[^"]*stroke-day[^"]*">(.*?)</div>', body_content, re.DOTALL)
    date_m = re.search(r'class="[^"]*stroke-date[^"]*">(.*?)</div>', body_content, re.DOTALL)
    
    # Extract Partners & Venue
    partners_m = re.search(r'class="[^"]*detail-label-col[^"]*">PARTNERS:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', body_content, re.DOTALL)
    venue_m = re.search(r'class="[^"]*detail-label-col[^"]*">VENUE:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', body_content, re.DOTALL)
    
    # Also check if Lead Office is in detail-row (like Day 4, 6, 7, etc.)
    lead_detail_m = re.search(r'class="[^"]*detail-label-col[^"]*">LEAD OFFICE:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', body_content, re.DOTALL)
    
    # Get all text chunks
    fab_text_clean = clean(body_content)
    
    day_name = f"DAY {idx}" if idx > 0 else "PRE-CAMPAIGN"
    
    # Calendar article
    if idx == 0:
        cal_art_m = re.search(r'<article class="day-card special-title-card">(.*?)</article>', cal_html, re.DOTALL)
    else:
        cal_art_m = re.search(r'<article class="day-card[^"]*">\s*<div class="card-top-bar">\s*<span class="day-pill">' + day_name + r'</span>(.*?)</article>', cal_html, re.DOTALL)
        
    cal_raw = cal_art_m.group(1) if cal_art_m else ""
    cal_text_clean = clean(cal_raw)
    
    print(f"\n{'#'*40} {day_name} ({fname}) {'#'*40}")
    print(f"--- FABMAT EXTRACTED ---")
    print(f"  Day / Date:  {clean(day_m.group(1)) if day_m else 'N/A'} | {clean(date_m.group(1)) if date_m else 'N/A'}")
    if lead_detail_m:
        print(f"  Lead Office: {clean(lead_detail_m.group(1))}")
    print(f"  Partners:    {clean(partners_m.group(1)) if partners_m else 'NONE'}")
    print(f"  Venue:       {clean(venue_m.group(1)) if venue_m else 'NONE'}")
    
    # Full clean body
    print(f"  Full Text in FABMAT:\n    {fab_text_clean}")
    print(f"--- CALENDAR EXTRACTED ---")
    print(f"  Full Text in Calendar:\n    {cal_text_clean}")
    
    # Check key comparison points
    discrepancies = []
    
    # Check date
    # In calendar: e.g. "NOV 25 WED" vs FABMAT "NOVEMBER 25, 2026 | WEDNESDAY"
    # That is the standard design distinction (calendar uses compact date, poster uses full date)
    
    audit_results.append({
        "day": day_name,
        "file": fname,
        "fab_text": fab_text_clean,
        "cal_text": cal_text_clean
    })

