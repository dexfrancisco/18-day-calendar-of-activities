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

# Let's inspect each day's exact texts
days_data = [
    # (day_num, cal_search_key, html_file)
    (0, "special-title-card", "00-pre-campaign.html"),
    (1, "DAY 1", "01-day-01.html"),
    (2, "DAY 2", "02-day-02.html"),
    (3, "DAY 3", "03-day-03.html"),
    (4, "DAY 4", "04-day-04.html"),
    (5, "DAY 5", "05-day-05.html"),
    (6, "DAY 6", "06-day-06.html"),
    (7, "DAY 7", "07-day-07.html"),
    (8, "DAY 8", "08-day-08.html"),
    (9, "DAY 9", "09-day-09.html"),
    (10, "DAY 10", "10-day-10.html"),
    (11, "DAY 11", "11-day-11.html"),
    (12, "DAY 12", "12-day-12.html"),
    (13, "DAY 13", "13-day-13.html"),
    (14, "DAY 14", "14-day-14.html"),
    (15, "DAY 15", "15-day-15.html"),
    (16, "DAY 16", "16-day-16.html"),
    (17, "DAY 17", "17-day-17.html"),
    (18, "DAY 18", "18-day-18.html"),
]

for d_num, cal_key, h_file in days_data:
    h_path = os.path.join('scratch/final_html', h_file)
    with open(h_path, 'r', encoding='utf-8') as f:
        h_content = f.read()
    
    # Extract calendar piece
    if d_num == 0:
        c_match = re.search(r'<article class="day-card special-title-card">(.*?)</article>', cal_html, re.DOTALL)
    else:
        c_match = re.search(r'<article class="day-card[^"]*">\s*<div class="card-top-bar">\s*<span class="day-pill">' + cal_key + r'</span>(.*?)</article>', cal_html, re.DOTALL)
    
    c_raw = c_match.group(1) if c_match else ""
    
    print(f"\n=======================================================")
    print(f"DAY {d_num}: {h_file}")
    print(f"=======================================================")
    
    # Check 1: Venue
    # in cal
    c_venues = re.findall(r'class="[^"]*venue-box[^"]*">(.*?)</div>', c_raw, re.DOTALL)
    if not c_venues and d_num == 0:
        c_venues = re.findall(r'class="special-title-venue">(.*?)</div>', c_raw, re.DOTALL)
    c_venue_txt = " | ".join([clean(v).replace('Venue:', '').replace('VENUE:', '').strip() for v in c_venues])
    
    # in fab
    f_venue_m = re.search(r'class="[^"]*detail-label-col[^"]*">VENUE:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', h_content, re.DOTALL)
    f_venue_txt = clean(f_venue_m.group(1)) if f_venue_m else "NONE"
    
    print(f"  VENUE:")
    print(f"    Calendar: {c_venue_txt if c_venue_txt else 'NONE'}")
    print(f"    FABMAT:   {f_venue_txt}")
    
    # Check 2: Partners
    c_partners = re.findall(r'class="[^"]*partner-box[^"]*">(.*?)</div>', c_raw, re.DOTALL)
    if not c_partners and d_num == 0:
        c_partners = re.findall(r'class="special-partner-row">(.*?)</div>', c_raw, re.DOTALL)
    c_part_txt = " | ".join([clean(p).replace('Partners:', '').strip() for p in c_partners])
    
    f_part_m = re.search(r'class="[^"]*detail-label-col[^"]*">PARTNERS:?</div>\s*<div class="[^"]*detail-val-col[^"]*">(.*?)</div>', h_content, re.DOTALL)
    f_part_txt = clean(f_part_m.group(1)) if f_part_m else "NONE"
    
    print(f"  PARTNERS:")
    print(f"    Calendar: {c_part_txt if c_part_txt else 'NONE'}")
    print(f"    FABMAT:   {f_part_txt}")
    
    # Check 3: Activities count / Titles / Lead
    print(f"  ACTIVITIES:")
    # print all lines containing activity or lead in cal and fab
    c_acts = re.findall(r'<div class="sub-act-item[^"]*">(.*?)</div>\s*(?=<div class="sub-act-item|<div class="card-partner-box|<div class="card-venue-box|</div>\s*</div>)', c_raw, re.DOTALL)
    f_acts = re.findall(r'<div class="act-item">(.*?)</div>\s*(?=<div class="act-item"|<div class="bottom-block"|</div>\s*</div>)', h_content, re.DOTALL)
    print(f"    Calendar activity count: {len(c_acts)}")
    print(f"    FABMAT activity count:   {len(f_acts)}")
    for i, ca in enumerate(c_acts):
        h = re.search(r'class="sub-act-header">([^<]+)<', ca)
        l = re.search(r'class="sub-lead-name">([^<]+)<', ca)
        d = re.search(r'class="sub-act-desc">([^<]+)<', ca)
        print(f"      Cal Act {i+1}: [{clean(h.group(1)) if h else ''}] Lead: {clean(l.group(1)) if l else ''} | Desc: {clean(d.group(1)) if d else ''}")
    for i, fa in enumerate(f_acts):
        num = re.search(r'class="[^"]*act-num[^"]*">(.*?)</div>', fa, re.DOTALL)
        d = re.search(r'class="[^"]*act-desc[^"]*">(.*?)</div>', fa, re.DOTALL)
        l = re.search(r'class="[^"]*act-lead-val[^"]*">(.*?)</span>', fa, re.DOTALL)
        print(f"      Fab Act {i+1}: [{clean(num.group(1)) if num else ''}] Lead: {clean(l.group(1)) if l else ''} | Desc: {clean(d.group(1)) if d else ''}")

